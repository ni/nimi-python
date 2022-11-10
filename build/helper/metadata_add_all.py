# Useful functions for use in the metadata modules

from .documentation_helper import add_notes_re_links
from .documentation_helper import square_up_tables
from .documentation_snippets import options_table_body
from .documentation_snippets import options_table_header
from .documentation_snippets import options_text
from .documentation_snippets import session_return_text
from .helper import camelcase_to_snakecase
from .helper import enum_uses_converter
from .helper import get_numpy_type_for_api_type
from .helper import get_python_type_for_api_type
from .metadata_filters import filter_codegen_attributes
from .metadata_filters import filter_codegen_functions
from .metadata_find import find_custom_type
from .metadata_find import find_size_parameter
from .metadata_merge_dicts import merge_helper

import codecs
import copy
import os
import pprint

pp = pprint.PrettyPrinter(indent=4, width=80)

# Functions to add information to metadata structures that are specific to our codegen needs.


# These functions can be used by any type, function, attribute or enum


def _add_name(n, name):
    '''Adds a name' key/value pair to the function metadata'''
    assert 'name' not in n, "'name' is already populated which means issue #372 is closed, rendering _add_name() redundant."
    n['name'] = name


def _add_codegen_method(n):
    '''Add 'codegen_method' as public if it isn't already there'''
    if 'codegen_method' not in n:
        n['codegen_method'] = 'public'


def _add_enum(n):
    '''Add 'enum' as None if it isn't already there'''
    if 'enum' not in n:
        n['enum'] = None


def _add_grpc_enum(n):
    '''Add 'grpc_enum' if it isn't already there'''
    if 'grpc_enum' not in n:
        if 'enum' in n:
            n['grpc_enum'] = n['enum']
        else:
            n['grpc_enum'] = None


def _add_python_method_name(function, name):
    '''Adds 'python_name' to the function metadata if not already there'''
    if 'python_name' not in function:
        if function['codegen_method'] == 'private':
            function['python_name'] = '_' + camelcase_to_snakecase(name)
        else:
            function['python_name'] = camelcase_to_snakecase(name)
            assert function['codegen_method'] == 'no' or 'method_name_for_documentation' not in function, "'method_name_for_documentation' not allowed to be set: function['method_name_for_documentation'] = '{0}', function['python_name'] = '{1}'".format(function['method_name_for_documentation'], function['python_name'])


def _add_interpreter_method_name(function, name):
    '''Adds 'interpreter_name' to the function metadata if not already there'''
    if 'interpreter_name' not in function:
        function['interpreter_name'] = function['python_name'].lstrip('_')


def _add_python_parameter_name(parameter):
    '''Adds a python_name key/value pair to the parameter metadata'''
    if 'python_name' not in parameter:
        parameter['python_name'] = camelcase_to_snakecase(parameter['name'])


def _add_grpc_parameter_name(parameter):
    '''Adds a grpc_name key/value pair to the parameter metadata'''
    if 'grpc_name' not in parameter:
        parameter['grpc_name'] = parameter['python_name']


def _add_python_type(item, config):
    '''Adds the type to use in the Python API and the documentation to the item metadata, if not already there'''
    if 'python_type' not in item:
        if item['enum'] is None:
            item['python_type'] = get_python_type_for_api_type(item['type'], config)
        else:
            item['python_type'] = 'enums.' + item['enum']

    # If 'type_in_documentation' isn't in the item, use 'python_type'
    item['type_in_documentation_was_calculated'] = False
    if 'type_in_documentation' not in item:
        item['type_in_documentation'] = item['python_type']
        item['type_in_documentation_was_calculated'] = True


def _add_ctypes_variable_name(parameter):
    '''Adds a ctypes_variable_name key/value pair to the parameter metadata for a corresponding ctypes variable'''
    parameter['ctypes_variable_name'] = parameter['python_name'] + '_ctype'


def _add_ctypes_type(parameter, config):
    '''Adds a ctypes_type key/value pair to the parameter metadata for calling into the library'''
    if parameter['type'] == 'ViAddr' and (parameter['use_array'] or parameter['use_list']):
        parameter['ctypes_type'] = 'ViInt8'
    else:
        parameter['ctypes_type'] = parameter['type']
    module_name = ''
    custom_type = find_custom_type(parameter, config)
    if custom_type is not None:
        module_name = custom_type['file_name'] + '.'

    if parameter['is_string']:
        parameter['ctypes_type_library_call'] = 'ctypes.POINTER(ViChar)'
    elif parameter['direction'] == 'out' or parameter['is_buffer'] is True:
        parameter['ctypes_type_library_call'] = "ctypes.POINTER(" + module_name + parameter['ctypes_type'] + ")"
    else:
        parameter['ctypes_type_library_call'] = module_name + parameter['ctypes_type']


def _add_numpy_info(parameter, parameters, config):
    '''Adds the following numpy-related information:

             numpy: Default to False unless already set. True for buffers that allow being passed as a numpy.ndarray.
        numpy_type: The name of the element type to use in the numpy.ndarray.
    '''

    if 'numpy' not in parameter:
        parameter['numpy'] = False

    if parameter['numpy']:
        parameter['numpy_type'] = get_numpy_type_for_api_type(parameter['type'], config)

        if parameter['size']['mechanism'] == 'passed-in':
            size_param = find_size_parameter(parameter, parameters)
            if size_param:
                size_param['use_in_python_api'] = False


def _add_is_error_handling(f):
    '''Adds is_error_handling information to the function metadata if it isn't already defined. Defaults to False.'''
    # TODO(marcoskirsch): The information is added in functions_addon.py. I think we can instead infer from method
    # name but I am not sure if it's a good idea (heuristics vs being explicit - both error prone in different ways).
    if 'is_error_handling' not in f:
        # Not populated, assume False
        f['is_error_handling'] = False


def _add_buffer_info(parameter, config):
    '''Adds buffer information to the parameter metadata

    These are the pieces of information that will be added to metadata:
        'is_string' - Used for any string type - see below for complete list
        'use_list'  - Used for an array of custom types. We are not putting custom types into array.array or numpy.array
        'use_array' - Used for arrays of simple types
        'is_buffer' - True when either 'use_list' or 'use_array' is True
        'size'      - set to default value of {'mechanism': 'fixed', 'value': 1} if it doesn't already exist
    '''

    assert 'is_buffer' not in parameter or not parameter['is_buffer'], "if 'is_buffer' is in metadata then it must be set to False"
    assert 'is_string' not in parameter, "'is_string' should not be set by metadata or in addons"
    assert 'use_list' not in parameter, "'use_list' should not be set by metadata or in addons"

    is_string = False
    use_array = False
    use_list = False
    original_type = parameter['type']

    # We set all string types to ViString, and say it is NOT a buffer/array
    string_types = ['ViConstString', 'ViRsrc', 'ViString', 'ViChar[]', ]
    if original_type in string_types:
        is_string = True
    elif original_type.find('[]') > 0:
        parameter['type'] = original_type.replace('[]', '')  # TODO(marcoskirsch) Don't change metadata, add new key
        parameter['original_type'] = original_type

        if 'use_array' not in parameter or parameter['use_array'] is False:
            use_list = True
        else:
            use_array = True

    # If 'is_buffer' is in the parameter information and False, we also force 'use_list' and 'use_array' to False
    use_list = parameter['is_buffer'] if 'is_buffer' in parameter else use_list
    use_array = parameter['is_buffer'] if 'is_buffer' in parameter else use_array

    # If not populated, assume {'mechanism': 'fixed', 'value': 1}
    parameter['size'] = parameter['size'] if 'size' in parameter else {'mechanism': 'fixed', 'value': 1}

    parameter['use_array'] = parameter['use_array'] if 'use_array' in parameter else use_array
    parameter['use_list'] = parameter['use_list'] if 'use_list' in parameter else use_list
    parameter['is_string'] = parameter['is_string'] if 'is_string' in parameter else is_string
    parameter['is_buffer'] = parameter['is_buffer'] if 'is_buffer' in parameter else (use_array or use_list)

    assert parameter['is_buffer'] is False or parameter['is_string'] is False


def _add_ctypes_method_call_snippet(parameter):
    '''Code snippet for calling a ctypes method for this parameter.'''
    if parameter['direction'] == 'out' and not parameter['is_buffer'] and not parameter['is_string']:
        parameter['ctypes_method_call_snippet'] = 'None if {0} is None else (ctypes.pointer({0}))'.format(parameter['ctypes_variable_name'])
    else:
        parameter['ctypes_method_call_snippet'] = parameter['ctypes_variable_name']


def _add_interpreter_method_call_snippet(parameter, config):
    '''Code snippet for calling a method of Library for this parameter.'''
    if parameter['is_session_handle']:
        parameter['interpreter_method_call_snippet'] = 'self._' + config['session_handle_parameter_name']
    elif parameter['is_repeated_capability']:
        parameter['interpreter_method_call_snippet'] = 'self._repeated_capability'
    else:
        parameter['interpreter_method_call_snippet'] = parameter['python_name']


def _add_grpc_request_snippet(parameter, config):
    param_name = parameter['grpc_name']
    if parameter.get('grpc_mapped_enum') is not None or parameter['grpc_enum'] is not None:
        param_name += '_raw'

    if parameter['use_list']:
        param_accessor = 'x'
    else:
        param_accessor = parameter['python_name']

    if parameter['is_session_handle']:
        param_value = 'self._' + config['session_handle_parameter_name']
    elif parameter['size']['mechanism'] == 'python-code' and parameter['direction'] == 'in':
        param_value = parameter['size']['value']
    elif parameter['enum'] is not None:
        param_value = param_accessor + '.value'
    elif parameter['type'].startswith('struct_'):
        for custom_type in config['custom_types']:
            if parameter['type'] == custom_type['ctypes_type']:
                ct_grpc_name = custom_type.get('grpc_name', custom_type['python_name'])
                param_value = param_accessor + '.create_copy(grpc_types.' + ct_grpc_name + ')'
                break
        else:
            ctypes_types = [t["ctypes_type"] for t in config["custom_types"]]
            assert False, f'Custom type not found for {parameter["type"]} among {ctypes_types}'
    else:
        param_value = param_accessor

    if parameter['use_list']:
        if param_value == param_accessor:
            param_value = parameter['python_name']
        else:
            param_value = parameter['python_name'] + ' and [' + param_value + ' for x in ' + parameter['python_name'] + ']'

    parameter['grpc_request_snippet'] = param_name + '=' + param_value


def _add_default_value_name(parameter):
    '''Declaration with default value, if set'''
    if 'default_value' in parameter:
        if 'enum' in parameter and parameter['enum'] is not None and parameter['default_value'] is not None:
            name_with_default = parameter['python_name'] + "=enums." + parameter['default_value']
        else:
            name_with_default = parameter['python_name'] + "=" + str(parameter['default_value'])

        if 'python_api_converter_name' in parameter:
            name_for_init = '_converters.{0}({1}, self._encoding)'.format(parameter['python_api_converter_name'], parameter['python_name'])
        elif parameter['use_in_python_api']:
            name_for_init = parameter['python_name']
        else:
            name_for_init = parameter['default_value']

    else:
        name_with_default = parameter['python_name']
        name_for_init = parameter['python_name']

    parameter['python_name_with_default'] = name_with_default
    parameter['python_name_or_default_for_init'] = str(name_for_init)


def _add_default_value_name_for_docs(parameter, module_name):
    '''Declaration with default value, if set'''
    if 'default_value' in parameter:
        if 'enum' in parameter and parameter['enum'] is not None and parameter['default_value'] is not None:
            name = parameter['python_name'] + "=" + module_name + '.' + parameter['default_value']
        else:
            name = parameter['python_name'] + "=" + str(parameter['default_value'])

    else:
        name = parameter['python_name']

    parameter['python_name_with_doc_default'] = name


# Parameter names denoting channel/repeated capabilities was compiled by looking at public header files for different MI drivers.
_repeated_capability_parameter_names = ['channelName', 'channelList', 'channel', 'channelNameList', 'channelsString']


def _add_method_templates(f):
    '''Adds a list of 'method_template_filenames' value to function metadata if not found. This are the mako templates that will be used to render the method.'''
    if 'method_templates' not in f:
        f['method_templates'] = [{'session_filename': '/default_method', 'library_interpreter_filename': '/default_method', 'documentation_filename': '/default_method', 'method_python_name_suffix': '', }, ]
    # Prefix the templates with a / so mako can find them. Not sure mako it works this way.
    for method_template in f['method_templates']:
        method_template['session_filename'] = '/' + method_template['session_filename'] if method_template['session_filename'][0] != '/' else method_template['session_filename']
        method_template['library_interpreter_filename'] = '/' + method_template['library_interpreter_filename'] if method_template['library_interpreter_filename'][0] != '/' else method_template['library_interpreter_filename']
        # Some functions don't get code-generated documentation (i.e. private methods) so no need to specify template for those.
        if 'documentation_filename' in method_template and method_template['documentation_filename'] is not None:
            method_template['documentation_filename'] = '/' + method_template['documentation_filename'] if method_template['documentation_filename'][0] != '/' else method_template['documentation_filename']


def _add_has_repeated_capability(f):
    '''Adds a boolean 'has_repeated_capability' to the function metadata by inferring it from its parameter names, if not previously populated.'''
    if 'has_repeated_capability' not in f:
        f['has_repeated_capability'] = False
        for p in f['parameters']:
            if p['is_repeated_capability']:
                f['has_repeated_capability'] = True
                f['repeated_capability_type'] = p['repeated_capability_type']


def _add_render_in_session_base(f):
    '''Adds a boolean 'render_in_session_base' to the function metadata if not previously populated.

    This tells the code generator to render those methods in _SessionBase class and not Session.
    By default, we want all functions that have repeated capability input and all error handling related functions in _SessionBase but there are exceptions to this rule.
    '''
    if 'render_in_session_base' not in f:
        f['render_in_session_base'] = f['has_repeated_capability'] or f['is_error_handling']


def _add_is_repeated_capability(parameter):
    '''Adds a boolean 'is_repeated_capability' to the parameter metadata by inferring it from its name, if not previously populated.'''
    if 'is_repeated_capability' not in parameter:
        if parameter['name'] in _repeated_capability_parameter_names:
            parameter['is_repeated_capability'] = True
            parameter['repeated_capability_type'] = 'channels'
        else:
            parameter['is_repeated_capability'] = False


def _add_use_session_lock(f):
    '''Set 'use_session_lock' to True unless it already exists

    Only nimodinst doesn't have session locking and the modinst session.py.mako doesn't even look at this
    '''
    f['use_session_lock'] = True if 'use_session_lock' not in f else f['use_session_lock']


def _add_is_session_handle(parameter):
    '''Adds a boolean 'is_session_handle' to the parameter metadata by inferring it from its type, if not previously populated.'''
    if 'is_session_handle' not in parameter:
        parameter['is_session_handle'] = parameter['type'] == 'ViSession' and parameter['direction'] == 'in'


def _fix_type(parameter):
    '''Replace any spaces in the parameter type with an underscore.'''
    parameter['type'] = parameter['type'].replace('[ ]', '[]').replace(' []', '[]').replace(' ', '_')


# TODO(olsl21): Metadata is inconsistent with regards to how structs are treated.
#  This is a hack to workaround that inconsistency. The real root cause is tracked
#  by internal NI bug 1918101. Once that is addressed, this method can be removed.
def _fix_custom_type(parameter, config):
    '''Add "struct_" prefix to custom type if necessary to match its ctypes_type.'''
    parameter_type_with_struct_prefix = 'struct_' + parameter['type']
    for custom_type in config['custom_types']:
        if parameter_type_with_struct_prefix == custom_type['ctypes_type']:
            parameter['type'] = custom_type['ctypes_type']
            break


def _add_use_in_python_api(p, parameters):
    '''Add 'use_in_python_api' if not there with value of True'''
    if 'use_in_python_api' not in p:
        p['use_in_python_api'] = True

    if p['size']['mechanism'] == 'len' or p['size']['mechanism'] == 'ivi-dance':
        size_param = find_size_parameter(p, parameters)
        size_param['use_in_python_api'] = False

    if p['size']['mechanism'] == 'ivi-dance-with-a-twist':
        # We have two parameters to remove from the API
        size_param = find_size_parameter(p, parameters)
        size_param['use_in_python_api'] = False
        size_param = find_size_parameter(p, parameters, key='value_twist')
        size_param['use_in_python_api'] = False


def _setup_init_function(functions, config):
    '''Copy the selected init function to a known name and update information about it for documentation purposes'''
    try:
        init_function = copy.deepcopy(functions[config['init_function']])
        init_function['codegen_method'] = 'no'

        # Change the init_function information for generating the docstring
        # We are assuming the last parameter is vi out
        for p in init_function['parameters']:
            if p['name'] == config['session_handle_parameter_name']:
                p['documentation']['description'] = session_return_text
                p['type_in_documentation'] = config['module_name'] + '.Session'
                p['python_name'] = 'session'
            elif p['python_name'] == 'option_string':
                p['python_name'] = 'options'
                p['python_name_with_default'] = 'options={}'
                p['documentation']['description'] = options_text
                p['documentation']['table_header'] = options_table_header
                p['documentation']['table_body'] = options_table_body
                # Additional options documentation may be added in metadata __init__ if it is driver specific

        functions['_init_function'] = init_function
    except KeyError:
        if 'init_function' not in config or config['init_function'] is None:
            # We don't have an init function or it is set to None (same thing) so we can't
            # do anything here
            pass
        else:
            print("Couldn't find {} init function".format(config['init_function']))


def add_all_function_metadata(functions, config):
    '''Merges and Adds all codegen-specific metada to the function metadata list'''
    functions = merge_helper(functions, 'functions', config, use_re=True)

    for f in functions:
        _add_codegen_method(functions[f])
        # Some drivers do not have any documentation, so make sure the
        # documentation key exists
        if 'documentation' not in functions[f]:
            functions[f]['documentation'] = {}

    for f in functions:
        _add_name(functions[f], f)
        _add_python_method_name(functions[f], f)
        _add_interpreter_method_name(functions[f], f)
        _add_is_error_handling(functions[f])
        _add_method_templates(functions[f])
        _add_use_session_lock(functions[f])
        for p in functions[f]['parameters']:
            if 'documentation' not in p:
                p['documentation'] = {}
            _add_enum(p)
            _add_grpc_enum(p)
            _fix_type(p)
            _add_buffer_info(p, config)
            _fix_custom_type(p, config)
            _add_use_in_python_api(p, functions[f]['parameters'])
            _add_python_parameter_name(p)
            _add_grpc_parameter_name(p)
            _add_python_type(p, config)
            _add_ctypes_variable_name(p)
            _add_ctypes_type(p, config)
            _add_numpy_info(p, functions[f]['parameters'], config)
            _add_default_value_name(p)
            _add_default_value_name_for_docs(p, config['module_name'])
            _add_is_repeated_capability(p)
            _add_is_session_handle(p)
            _add_ctypes_method_call_snippet(p)
            _add_interpreter_method_call_snippet(p, config)
            _add_grpc_request_snippet(p, config)

        # We can't do these until the parameters have been processed
        _add_has_repeated_capability(functions[f])
        _add_render_in_session_base(functions[f])

    _setup_init_function(functions, config)

    return functions


def _add_python_name(a, attributes):
    '''Adds 'python_name' - lower case + leading '_' if first character is a digit'''
    if 'python_name' not in attributes[a]:
        n = attributes[a]['name'].lower()
        if attributes[a]['codegen_method'] == 'private':
            n = '_' + n

        attributes[a]['python_name'] = n

    assert not attributes[a]['python_name'][0].isdigit()


def _add_default_attribute_class(a, attributes):
    '''Set 'attribute_class' if not set.

    By default, the 'attribute_class' is only based on the 'type'.
    It can be set in attributes_addon if we want to convert to/from a different datatype, such as hightime.timedelta
    '''
    if 'attribute_class' not in attributes[a]:
        attributes[a]['attribute_class'] = 'Attribute' + attributes[a]['type']


def add_all_attribute_metadata(attributes, config):
    '''Merges and Adds all codegen-specific metada to the function metadata list'''
    attributes = merge_helper(attributes, 'attributes', config, use_re=False)

    for a in attributes:
        _add_codegen_method(attributes[a])
        _add_enum(attributes[a])
        _add_grpc_enum(attributes[a])
        _add_python_name(a, attributes)
        _add_python_type(attributes[a], config)
        _add_default_attribute_class(a, attributes)

    return attributes


def _add_enum_codegen_method(enums, config):
    '''Adds 'codegen_method' if not explicitly specified that will determine whether and how the enum is code-generated.

    If an enum does not explicitly specify its 'codegen_method' in metadata, it will be assigned the
    least restrictive codegen_method based on the codegen_method of all the functions and attributes
    that use it. The default codegen_method is 'no' (if no function nor attribute uses it).

    If an enum explicitly specifies its 'codegen_method' in metadata, it will be checked against the
    least restrictive codegen_method based on the codegen_method of all the functions and attributes
    that use it (if its explicit 'codegen_method' is more restrictive than the calculated least
    restrictive codegen_method and it does not use converter, a ValueError would be thrown).

    The restrictiveness of the codegen_method is as follows (most restrictive -> least restrictive):
    'no' -> 'private' -> 'public' / 'python-only' (will be converted to 'public' if not explicitly specified)
    '''
    enum_to_client_functions = _get_functions_that_use_enums(enums, config)
    enum_to_client_attributes = _get_attributes_that_use_enums(enums, config)
    for e in enums:
        least_restrictive_codegen_method = _get_least_restrictive_codegen_method(
            set.union(
                set(config['functions'][f]['codegen_method'] for f in enum_to_client_functions[e]),
                set(config['attributes'][a]['codegen_method'] for a in enum_to_client_attributes[e])
            )
        )
        if 'codegen_method' not in enums[e]:
            enums[e]['codegen_method'] = least_restrictive_codegen_method
        else:
            explicit_codegen_method = enums[e]['codegen_method']
            # Check if explicit_codegen_method is more restrictive than
            #  least_restrictive_codegen_method and the enum does not use converter
            # _get_least_restrictive_codegen_method() might change 'python-only' to 'public',
            #  so avoid comparing explicit_codegen_method with the output of
            #  _get_least_restrictive_codegen_method() directly
            if _get_least_restrictive_codegen_method([
                explicit_codegen_method,
                least_restrictive_codegen_method
            ]) != _get_least_restrictive_codegen_method([
                explicit_codegen_method
            ]) and not enum_uses_converter(enums[e]):
                client_function_names = enum_to_client_functions[e]
                client_attribute_names = [
                    config['attributes'][a]['name'] for a in enum_to_client_attributes[e]
                ]
                raise ValueError(
                    f'Codegen_method of enum {e} used by functions {client_function_names} and attributes {client_attribute_names} must be {least_restrictive_codegen_method}, is {explicit_codegen_method}'
                )


def _get_functions_that_use_enums(enums, config):
    '''Generate a dict that maps each enum to a list of functions that use it in their parameters'''
    enum_to_client_functions = {e: [] for e in enums}
    for f in filter_codegen_functions(config['functions']):
        for p in config['functions'][f]['parameters']:
            e = p['enum']
            if e is not None:
                if e not in enum_to_client_functions:
                    print('Missing enum {0} referenced by function {1}'.format(e, f))
                else:
                    enum_to_client_functions[e].append(f)
    return enum_to_client_functions


def _get_attributes_that_use_enums(enums, config):
    '''Generate a dict that maps each enum to a list of attributes that use it'''
    enum_to_client_attributes = {e: [] for e in enums}
    for a in filter_codegen_attributes(config['attributes']):
        e = config['attributes'][a]['enum']
        if e is not None:
            if e not in enum_to_client_attributes:
                print('Missing enum {0} referenced by attribute {1}'.format(e, a))
            else:
                enum_to_client_attributes[e].append(a)
    return enum_to_client_attributes


def _get_least_restrictive_codegen_method(codegen_methods):
    '''Get the least restrictive codegen_method among the input codegen_methods.

    If the codegen_methods parameter is empty, return 'no'.
    The restrictiveness of the codegen_method is as follows (most restrictive -> least restrictive):
    'no' -> 'private' -> 'public' / 'python-only' (will be converted to 'public')
    '''
    if len(codegen_methods) == 0:
        return 'no'

    codegen_method_to_permissiveness = {
        'no': 0,
        'private': 1,
        'python-only': 2,
        'public': 2
    }
    permissiveness_to_codegen_method = {
        0: 'no',
        1: 'private',
        2: 'public'
    }
    return permissiveness_to_codegen_method[
        max(codegen_method_to_permissiveness[codegen_method] for codegen_method in codegen_methods)
    ]


def _add_enum_value_python_name(enum_info, config):
    '''Add 'python_name' for all values, removing any common prefixes and suffixes'''
    for v in enum_info['values']:
        if 'python_name' not in v:
            v['python_name'] = v['name'].replace('{0}_VAL_'.format(config['module_name'].upper()), '')

    # We are using an os.path function do find any common prefix. So that we don't
    # get 'O' in 'ON' and 'OFF' we remove characters at the end until they are '_'
    names = [v['python_name'] for v in enum_info['values']]
    prefix = os.path.commonprefix(names)
    while len(prefix) > 0 and prefix[-1] != '_':
        prefix = prefix[:-1]

    # If the prefix is in the whitelist, we don't want to remove it so set to empty string
    if 'enum_whitelist_prefix' in config and prefix in config['enum_whitelist_prefix']:
        prefix = ''

    # We only remove the prefix if there is one and it isn't '_'.
    # '_' only means the name starts with a number
    if len(prefix) > 0 and prefix != '_':
        for v in enum_info['values']:
            assert v['python_name'].startswith(prefix), '{0} does not start with {1}'.format(v['name'], prefix)
            v['prefix'] = prefix
            v['python_name'] = v['python_name'].replace(prefix, '')

    # Now we need to look for common suffixes
    # Using the slow method of reversing a string for readability
    rev_names = [''.join(reversed(v['python_name'])) for v in enum_info['values']]
    suffix = os.path.commonprefix(rev_names)
    while len(suffix) > 0 and suffix[-1] != '_':
        suffix = suffix[:-1]

    # Unreverse the suffix
    suffix = ''.join(reversed(suffix))

    # If the suffix is in the whitelist, we don't want to remove it so set to empty string
    if 'enum_whitelist_suffix' in config and suffix in config['enum_whitelist_suffix']:
        suffix = ''

    # We only remove the suffix if there is one.
    # '_' only means the name starts with a number
    if len(suffix) > 0:
        for v in enum_info['values']:
            assert v['python_name'].endswith(suffix), '{0} does not end with {1}'.format(v['name'], suffix)
            v['suffix'] = suffix
            v['python_name'] = v['python_name'][:-len(suffix)]

    # We need to check again to see if we have any values that start with a digit
    # If we are not going to code generate this enum, we don't care about this
    for v in enum_info['values']:
        assert v['python_name'], enum_info
        if enum_info['codegen_method'] != 'no' and v['python_name'][0].isdigit():
            raise ValueError('Invalid name: {}'.format(v['python_name']))  # pragma: no cover

    return enum_info


def fixup_enum_names(config):
    '''Fix enum types for private enums

    Now that we have all the metadata calculated, we need to fix any enum types in attributes and functions
    where the underlying enum is private. At the time the 'python_type' was set, we hadn't yet calculated
    whether the enum would be private or not. We couldn't because we needed to process all the functions and
    attributes first.
    '''
    # Check all the functions that will be code generated
    for f in config['functions']:
        if config['functions'][f]['codegen_method'] != 'no':
            for p in config['functions'][f]['parameters']:
                if p['enum'] is not None and config['enums'][p['enum']]['codegen_method'] == 'private':
                    # We need to update the python type since the enum is private
                    p['python_type'] = 'enums.' + config['enums'][p['enum']]['python_name']

    # Check all attributes that will be code generated
    for a in config['attributes']:
        attr = config['attributes'][a]
        if attr['codegen_method'] != 'no':
            if attr['enum'] is not None and config['enums'][attr['enum']]['codegen_method'] == 'private':
                # We need to update the python type since the enum is private
                attr['python_type'] = 'enums.' + config['enums'][attr['enum']]['python_name']


def add_all_enum_metadata(enums, config):
    '''Merges and Adds all codegen-specific metada to the function metadata list'''
    enums = merge_helper(enums, 'enums', config, use_re=False)

    # Workaround for NI Internal CAR #675174
    try:
        replacement_enums = config['modules']['metadata.enums_addon'].__getattribute__('replacement_enums')
        for e in replacement_enums:
            enums[e] = replacement_enums[e]
    except AttributeError:
        pass

    _add_enum_codegen_method(enums, config)
    for e in enums:
        enums[e] = _add_enum_value_python_name(enums[e], config)
        enums[e]['python_name'] = ('_' if enums[e]['codegen_method'] == 'private' else '') + (enums[e]['python_name'] if 'python_name' in enums[e] else e)

    return enums


def add_all_config_metadata(config):
    '''add_all_config_metadata

    Ensure all defaults added to config
    '''
    config = merge_helper(config, 'config', config, use_re=False)

    if 'use_locking' not in config:
        config['use_locking'] = True

    if 'uses_nitclk' not in config:
        config['uses_nitclk'] = False

    return config


def add_all_metadata(functions, attributes, enums, config, persist_output=True):
    '''merge and add all additional metadata_dir

    Updates all parameters
        functions, attributes, enums - addon data merged, additional metadata
        config - functions, attributes, enums added
    '''
    config = add_all_config_metadata(config)

    functions = add_all_function_metadata(functions, config)
    config['functions'] = functions

    attributes = add_all_attribute_metadata(attributes, config)
    config['attributes'] = attributes

    enums = add_all_enum_metadata(enums, config)
    config['enums'] = enums

    add_notes_re_links(config)

    square_up_tables(config)

    fixup_enum_names(config)

    pp_persist = pprint.PrettyPrinter(indent=4, width=200)
    metadata_dir = os.path.join('generated', 'processed_metadata')

    # If we are not persisting the output (I.e. during a test) we return early
    if not persist_output:
        return config

    if not os.path.exists(metadata_dir):
        os.makedirs(metadata_dir)

    with codecs.open(os.path.join(metadata_dir, config['module_name'] + '_functions.py'), "w", "utf-8") as text_file:
        text_file.write("function =\n{0}".format(pp_persist.pformat(functions)))

    with codecs.open(os.path.join(metadata_dir, config['module_name'] + '_attributes.py'), "w", "utf-8") as text_file:
        text_file.write("attributes =\n{0}".format(pp_persist.pformat(attributes)))

    with codecs.open(os.path.join(metadata_dir, config['module_name'] + '_enums.py'), "w", "utf-8") as text_file:
        text_file.write("enums =\n{0}".format(pp_persist.pformat(enums)))

    # We need to delete modules before we deepcopy, otherwise we get an error
    # These were needed only for merging, which has already happened
    del config['modules']

    # We need to make a copy so we can delete functions, attributes and enums since
    # they are already in individual files
    config_copy = copy.deepcopy(config)
    del config_copy['functions']
    del config_copy['attributes']
    del config_copy['enums']

    with codecs.open(os.path.join(metadata_dir, config['module_name'] + '_config.py'), "w", "utf-8") as text_file:
        text_file.write("enums =\n{0}".format(pp_persist.pformat(config_copy)))

    return config


# Unit Tests
def _compare_values(actual, expected, k):
    if type(actual) is dict:
        _compare_dicts(actual, expected)
    elif type(actual) is list:
        _compare_lists(actual, expected)
    else:
        assert actual == expected, "Value mismatch with key/index '{0}', {1} != {2}".format(k, actual, expected)


def _compare_lists(actual, expected):
    assert type(actual) == type(expected), 'Type mismatch, {0} != {1}'.format(type(actual), type(expected))
    assert len(actual) == len(expected), 'Length mismatch, {0} != {1}'.format(len(actual), len(expected))
    for k in range(len(actual)):
        _compare_values(actual[k], expected[k], k)


def _compare_dicts(actual, expected):
    assert type(actual) == type(expected), 'Type mismatch, {0} != {1}'.format(type(actual), type(expected))
    for k in actual:
        assert k in expected, 'Key {0} not in expected'.format(k)
        _compare_values(actual[k], expected[k], k)
    for k in expected:
        assert k in actual, 'Key {0} not in actual'.format(k)


functions_input = {
    'MakeAFoo': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'method_templates': [{'session_filename': '/cool_template', 'library_interpreter_filename': '/cool_template', 'documentation_filename': '/cool_template', 'method_python_name_suffix': '', }, ],
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'enum': None,
                'name': 'channelName',
                'python_name': 'name',
                'is_repeated_capability': False,
                'type': 'ViString',
                'documentation': {
                    'description': 'The channel to call this on.',
                },
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'buffer size input',
                },
                'enum': None,
                'name': 'pinDataBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'python-code input',
                },
                'enum': None,
                'name': 'pythonCodeInput',
                'size': {
                    'mechanism': 'python-code',
                    'value': '2 ** 14'
                },
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'buffer size output',
                },
                'enum': None,
                'name': 'actualNumPinData',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'buffer',
                },
                'enum': None,
                'name': 'expectedPinStates',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'pinDataBufferSize',
                    'value_twist': 'actualNumPinData'
                },
                'type': 'ViUInt8[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'custom type input',
                },
                'enum': None,
                'name': 'customTypeInput',
                'type': 'struct CustomStruct'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'custom type output',
                },
                'enum': None,
                'name': 'customTypeOutput',
                'type': 'struct CustomStruct'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'custom type without struct prefix input',
                },
                'enum': None,
                'name': 'customTypeWithoutStructPrefixInput',
                'type': 'CustomStruct'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'custom type without struct prefix output',
                },
                'enum': None,
                'name': 'customTypeWithoutStructPrefixOutput',
                'type': 'CustomStruct'
            },
        ],
        'documentation': {
            'description': 'Performs a foo, and performs it well.',
        },
    },
    'MakeAPrivateMethod': {
        'codegen_method': 'private',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'out',
                'enum': None,
                'name': 'status',
                'type': 'ViString',
                'documentation': {
                    'description': 'Return a device status',
                },
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'buffer size',
                },
                'enum': None,
                'name': 'dataBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'buffer',
                },
                'enum': None,
                'name': 'data',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'dataBufferSize'
                },
                'type': 'ViUInt32[]'
            },
        ],
        'documentation': {
            'description': 'Perform actions as method defined',
        },
    },
    'MakeANoCodegenMethod': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'This is a method with codegen_method set to no',
        },
        'method_name_for_documentation': 'MakeAPublicMethod',
        'method_templates': [
            {
                'session_filename': '/cool_template',
                'library_interpreter_filename': '/cool_template',
                'documentation_filename': '/cool_template',
                'method_python_name_suffix': '',
            },
        ],
        'parameters': [],
        'returns': 'ViStatus',
    },
}


functions_expected = {
    'MakeAFoo': {
        'name': 'MakeAFoo',
        'codegen_method': 'public',
        'use_session_lock': True,
        'documentation': {
            'description': 'Performs a foo, and performs it well.'
        },
        'has_repeated_capability': False,
        'is_error_handling': False,
        'render_in_session_base': False,
        'method_templates': [{'session_filename': '/cool_template', 'library_interpreter_filename': '/cool_template', 'documentation_filename': '/cool_template', 'method_python_name_suffix': '', }, ],
        'parameters': [
            {
                'ctypes_method_call_snippet': 'vi_ctype',
                'ctypes_type': 'ViSession',
                'ctypes_variable_name': 'vi_ctype',
                'ctypes_type_library_call': 'ViSession',
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'is_repeated_capability': False,
                'is_session_handle': True,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'vi',
                'grpc_name': 'vi',
                'python_name': 'vi',
                'python_name_with_default': 'vi',
                'python_name_with_doc_default': 'vi',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViSession',
                'interpreter_method_call_snippet': 'self._vi',
                'grpc_request_snippet': 'vi=self._vi',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'vi',
            },
            {
                'ctypes_method_call_snippet': 'name_ctype',
                'ctypes_type': 'ViString',
                'ctypes_variable_name': 'name_ctype',
                'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
                'direction': 'in',
                'documentation': {
                    'description': 'The channel to call this on.'
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'str',
                'type_in_documentation': 'str',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': True,
                'name': 'channelName',
                'grpc_name': 'name',
                'python_name': 'name',
                'python_name_with_default': 'name',
                'python_name_with_doc_default': 'name',
                'size': {'mechanism': 'fixed', 'value': 1},
                'type': 'ViString',
                'interpreter_method_call_snippet': 'name',
                'grpc_request_snippet': 'name=name',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'name',
            },
            {
                'ctypes_method_call_snippet': 'pin_data_buffer_size_ctype',
                'ctypes_type': 'ViInt32',
                'ctypes_variable_name': 'pin_data_buffer_size_ctype',
                'ctypes_type_library_call': 'ViInt32',
                'direction': 'in',
                'documentation': {
                    'description': 'buffer size input',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'pinDataBufferSize',
                'grpc_name': 'pin_data_buffer_size',
                'python_name': 'pin_data_buffer_size',
                'python_name_with_default': 'pin_data_buffer_size',
                'python_name_with_doc_default': 'pin_data_buffer_size',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViInt32',
                'interpreter_method_call_snippet': 'pin_data_buffer_size',
                'grpc_request_snippet': 'pin_data_buffer_size=pin_data_buffer_size',
                'use_in_python_api': False,
                'python_name_or_default_for_init': 'pin_data_buffer_size',
            },
            {
                'ctypes_method_call_snippet': 'python_code_input_ctype',
                'ctypes_type': 'ViInt32',
                'ctypes_variable_name': 'python_code_input_ctype',
                'ctypes_type_library_call': 'ViInt32',
                'direction': 'in',
                'documentation': {
                    'description': 'python-code input',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'pythonCodeInput',
                'grpc_name': 'python_code_input',
                'python_name': 'python_code_input',
                'python_name_with_default': 'python_code_input',
                'python_name_with_doc_default': 'python_code_input',
                'size': {
                    'mechanism': 'python-code',
                    'value': '2 ** 14'
                },
                'type': 'ViInt32',
                'interpreter_method_call_snippet': 'python_code_input',
                'grpc_request_snippet': 'python_code_input=2 ** 14',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'python_code_input',
            },
            {
                'ctypes_method_call_snippet': 'None if actual_num_pin_data_ctype is None else (ctypes.pointer(actual_num_pin_data_ctype))',
                'ctypes_type': 'ViInt32',
                'ctypes_variable_name': 'actual_num_pin_data_ctype',
                'ctypes_type_library_call': 'ctypes.POINTER(ViInt32)',
                'direction': 'out',
                'documentation': {
                    'description': 'buffer size output',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'actualNumPinData',
                'grpc_name': 'actual_num_pin_data',
                'python_name': 'actual_num_pin_data',
                'python_name_with_default': 'actual_num_pin_data',
                'python_name_with_doc_default': 'actual_num_pin_data',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViInt32',
                'interpreter_method_call_snippet': 'actual_num_pin_data',
                'grpc_request_snippet': 'actual_num_pin_data=actual_num_pin_data',
                'use_in_python_api': False,
                'python_name_or_default_for_init': 'actual_num_pin_data',
            },
            {
                'ctypes_method_call_snippet': 'expected_pin_states_ctype',
                'ctypes_type': 'ViUInt8',
                'ctypes_variable_name': 'expected_pin_states_ctype',
                'ctypes_type_library_call': 'ctypes.POINTER(ViUInt8)',
                'direction': 'out',
                'documentation': {
                    'description': 'buffer',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': True,
                'use_list': True,
                'is_string': False,
                'name': 'expectedPinStates',
                'original_type': 'ViUInt8[]',
                'grpc_name': 'expected_pin_states',
                'python_name': 'expected_pin_states',
                'python_name_with_default': 'expected_pin_states',
                'python_name_with_doc_default': 'expected_pin_states',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'pinDataBufferSize',
                    'value_twist': 'actualNumPinData'
                },
                'type': 'ViUInt8',
                'interpreter_method_call_snippet': 'expected_pin_states',
                'grpc_request_snippet': 'expected_pin_states=expected_pin_states',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'expected_pin_states',
            },
            {
                'ctypes_method_call_snippet': 'custom_type_input_ctype',
                'ctypes_type': 'struct_CustomStruct',
                'ctypes_variable_name': 'custom_type_input_ctype',
                'ctypes_type_library_call': 'custom_struct.struct_CustomStruct',
                'direction': 'in',
                'documentation': {
                    'description': 'custom type input',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'CustomStruct',
                'type_in_documentation': 'CustomStruct',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'customTypeInput',
                'grpc_name': 'custom_type_input',
                'python_name': 'custom_type_input',
                'python_name_with_default': 'custom_type_input',
                'python_name_with_doc_default': 'custom_type_input',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'struct_CustomStruct',
                'interpreter_method_call_snippet': 'custom_type_input',
                'grpc_request_snippet': 'custom_type_input=custom_type_input.create_copy(grpc_types.CustomStruct)',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'custom_type_input',
            },
            {
                'ctypes_method_call_snippet': 'None if custom_type_output_ctype is None else (ctypes.pointer(custom_type_output_ctype))',
                'ctypes_type': 'struct_CustomStruct',
                'ctypes_variable_name': 'custom_type_output_ctype',
                'ctypes_type_library_call': 'ctypes.POINTER(custom_struct.struct_CustomStruct)',
                'direction': 'out',
                'documentation': {
                    'description': 'custom type output',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'CustomStruct',
                'type_in_documentation': 'CustomStruct',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'customTypeOutput',
                'grpc_name': 'custom_type_output',
                'python_name': 'custom_type_output',
                'python_name_with_default': 'custom_type_output',
                'python_name_with_doc_default': 'custom_type_output',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'struct_CustomStruct',
                'interpreter_method_call_snippet': 'custom_type_output',
                'grpc_request_snippet': 'custom_type_output=custom_type_output.create_copy(grpc_types.CustomStruct)',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'custom_type_output',
            },
            {
                'ctypes_method_call_snippet': 'custom_type_without_struct_prefix_input_ctype',
                'ctypes_type': 'struct_CustomStruct',
                'ctypes_variable_name': 'custom_type_without_struct_prefix_input_ctype',
                'ctypes_type_library_call': 'custom_struct.struct_CustomStruct',
                'direction': 'in',
                'documentation': {
                    'description': 'custom type without struct prefix input',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'CustomStruct',
                'type_in_documentation': 'CustomStruct',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'customTypeWithoutStructPrefixInput',
                'grpc_name': 'custom_type_without_struct_prefix_input',
                'python_name': 'custom_type_without_struct_prefix_input',
                'python_name_with_default': 'custom_type_without_struct_prefix_input',
                'python_name_with_doc_default': 'custom_type_without_struct_prefix_input',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'struct_CustomStruct',
                'interpreter_method_call_snippet': 'custom_type_without_struct_prefix_input',
                'grpc_request_snippet': 'custom_type_without_struct_prefix_input=custom_type_without_struct_prefix_input.create_copy(grpc_types.CustomStruct)',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'custom_type_without_struct_prefix_input',
            },
            {
                'ctypes_method_call_snippet': 'None if custom_type_without_struct_prefix_output_ctype is None else (ctypes.pointer(custom_type_without_struct_prefix_output_ctype))',
                'ctypes_type': 'struct_CustomStruct',
                'ctypes_variable_name': 'custom_type_without_struct_prefix_output_ctype',
                'ctypes_type_library_call': 'ctypes.POINTER(custom_struct.struct_CustomStruct)',
                'direction': 'out',
                'documentation': {
                    'description': 'custom type without struct prefix output',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'CustomStruct',
                'type_in_documentation': 'CustomStruct',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'customTypeWithoutStructPrefixOutput',
                'grpc_name': 'custom_type_without_struct_prefix_output',
                'python_name': 'custom_type_without_struct_prefix_output',
                'python_name_with_default': 'custom_type_without_struct_prefix_output',
                'python_name_with_doc_default': 'custom_type_without_struct_prefix_output',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'struct_CustomStruct',
                'interpreter_method_call_snippet': 'custom_type_without_struct_prefix_output',
                'grpc_request_snippet': 'custom_type_without_struct_prefix_output=custom_type_without_struct_prefix_output.create_copy(grpc_types.CustomStruct)',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'custom_type_without_struct_prefix_output',
            },
        ],
        'python_name': 'make_a_foo',
        'interpreter_name': 'make_a_foo',
        'returns': 'ViStatus',
    },
    'MakeAPrivateMethod': {
        'codegen_method': 'private',
        'returns': 'ViStatus',
        'use_session_lock': True,
        'method_templates': [{'session_filename': '/default_method', 'library_interpreter_filename': '/default_method', 'documentation_filename': '/default_method', 'method_python_name_suffix': '', }, ],
        'parameters': [
            {
                'ctypes_method_call_snippet': 'vi_ctype',
                'direction': 'in',
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'grpc_name': 'vi',
                'python_name': 'vi',
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'ctypes_variable_name': 'vi_ctype',
                'ctypes_type': 'ViSession',
                'ctypes_type_library_call': 'ViSession',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'python_name_with_default': 'vi',
                'python_name_with_doc_default': 'vi',
                'is_repeated_capability': False,
                'is_session_handle': True,
                'interpreter_method_call_snippet': 'self._vi',
                'grpc_request_snippet': 'vi=self._vi',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'vi',
            },
            {
                'ctypes_method_call_snippet': 'status_ctype',
                'direction': 'out',
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'name': 'status',
                'type': 'ViString',
                'documentation': {
                    'description': 'Return a device status'
                },
                'grpc_name': 'status',
                'python_name': 'status',
                'python_type': 'str',
                'type_in_documentation': 'str',
                'type_in_documentation_was_calculated': True,
                'ctypes_variable_name': 'status_ctype',
                'ctypes_type': 'ViString',
                'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': True,
                'python_name_with_default': 'status',
                'python_name_with_doc_default': 'status',
                'is_repeated_capability': False,
                'is_session_handle': False,
                'interpreter_method_call_snippet': 'status',
                'grpc_request_snippet': 'status=status',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'status',
            },
            {
                'ctypes_method_call_snippet': 'data_buffer_size_ctype',
                'ctypes_type': 'ViInt32',
                'ctypes_variable_name': 'data_buffer_size_ctype',
                'ctypes_type_library_call': 'ViInt32',
                'direction': 'in',
                'documentation': {
                    'description': 'buffer size',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'name': 'dataBufferSize',
                'grpc_name': 'data_buffer_size',
                'python_name': 'data_buffer_size',
                'python_name_with_default': 'data_buffer_size',
                'python_name_with_doc_default': 'data_buffer_size',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViInt32',
                'interpreter_method_call_snippet': 'data_buffer_size',
                'grpc_request_snippet': 'data_buffer_size=data_buffer_size',
                'use_in_python_api': False,
                'python_name_or_default_for_init': 'data_buffer_size',
            },
            {
                'ctypes_method_call_snippet': 'data_ctype',
                'ctypes_type': 'ViUInt32',
                'ctypes_variable_name': 'data_ctype',
                'ctypes_type_library_call': 'ctypes.POINTER(ViUInt32)',
                'direction': 'out',
                'documentation': {
                    'description': 'buffer',
                },
                'is_repeated_capability': False,
                'is_session_handle': False,
                'enum': None,
                'grpc_enum': None,
                'numpy': False,
                'python_type': 'int',
                'type_in_documentation': 'int',
                'type_in_documentation_was_calculated': True,
                'use_array': False,
                'is_buffer': True,
                'use_list': True,
                'is_string': False,
                'name': 'data',
                'original_type': 'ViUInt32[]',
                'grpc_name': 'data',
                'python_name': 'data',
                'python_name_with_default': 'data',
                'python_name_with_doc_default': 'data',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'dataBufferSize',
                },
                'type': 'ViUInt32',
                'interpreter_method_call_snippet': 'data',
                'grpc_request_snippet': 'data=data',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'data',
            },
        ],
        'documentation': {
            'description': 'Perform actions as method defined'
        },
        'name': 'MakeAPrivateMethod',
        'python_name': '_make_a_private_method',
        'interpreter_name': 'make_a_private_method',
        'is_error_handling': False,
        'render_in_session_base': False,
        'has_repeated_capability': False
    },
    'MakeANoCodegenMethod': {
        'name': 'MakeANoCodegenMethod',
        'codegen_method': 'no',
        'method_name_for_documentation': 'MakeAPublicMethod',
        'use_session_lock': True,
        'documentation': {
            'description': 'This is a method with codegen_method set to no'
        },
        'has_repeated_capability': False,
        'is_error_handling': False,
        'render_in_session_base': False,
        'method_templates': [
            {
                'session_filename': '/cool_template',
                'library_interpreter_filename': '/cool_template',
                'documentation_filename': '/cool_template',
                'method_python_name_suffix': ''
            }
        ],
        'parameters': [],
        'python_name': 'make_a_no_codegen_method',
        'interpreter_name': 'make_a_no_codegen_method',
        'returns': 'ViStatus',
    }
}


attributes_input = {
    1000000: {
        'access': 'read-write',
        'enum': None,
        'lv_property': 'Fake attributes:Read Write Bool',
        'name': 'READ_WRITE_BOOL',
        'type': 'ViBoolean',
        'documentation': {
            'description': 'An attribute of type bool with read/write access.',
        },
    },
}


attributes_expected = {
    1000000: {
        'access': 'read-write',
        'codegen_method': 'public',
        'documentation': {'description': 'An attribute of type bool with read/write access.'},
        'enum': None,
        'grpc_enum': None,
        'lv_property': 'Fake attributes:Read Write Bool',
        'name': 'READ_WRITE_BOOL',
        'python_name': 'read_write_bool',
        'type': 'ViBoolean',
        'python_type': 'bool',
        'type_in_documentation': 'bool',
        'type_in_documentation_was_calculated': True,
        'attribute_class': 'AttributeViBoolean',
    },
}


enums_input = {
    'Color': {
        'values': [
            {
                'name': 'RED',
                'value': 1,
                'documentation': {
                    'description': 'Like blood.',
                }
            },
            {
                'name': 'BLUE',
                'value': 2,
                'documentation': {
                    'description': 'Like the sky.',
                }
            },
            {
                'name': 'YELLOW',
                'value': 2,
                'documentation': {
                    'description': 'Like a banana.',
                }
            },
            {
                'name': 'BLACK',
                'value': 2,
                'documentation': {
                    'description': 'Like this developer\'s conscience.',
                }
            },
        ],
    },
    'EnumWithConverter': {
        'codegen_method': 'private',
        'converted_value_to_enum_function_name': 'convert_to_enum_with_converter_enum',
        'enum_to_converted_value_function_name': 'convert_from_enum_with_converter_enum',
        'values': [
            {
                'converts_to_value': True,
                'name': 'RED',
                'value': 1
            },
            {
                'converts_to_value': False,
                'name': 'BLUE',
                'value': 2
            },
            {
                'converts_to_value': 'yellow',
                'name': 'YELLOW',
                'value': 5
            },
            {
                'converts_to_value': 42,
                'name': 'BLACK',
                'value': 42
            }
        ]
    },
}


enums_expected = {
    'Color': {
        'codegen_method': 'no',
        'python_name': 'Color',
        'values': [
            {'documentation': {'description': 'Like blood.'}, 'name': 'RED', 'value': 1, 'python_name': 'RED'},
            {'documentation': {'description': 'Like the sky.'}, 'name': 'BLUE', 'value': 2, 'python_name': 'BLUE'},
            {'documentation': {'description': 'Like a banana.'}, 'name': 'YELLOW', 'value': 2, 'python_name': 'YELLOW'},
            {'documentation': {'description': "Like this developer's conscience."}, 'name': 'BLACK', 'value': 2, 'python_name': 'BLACK'}
        ]
    },
    'EnumWithConverter': {
        'codegen_method': 'private',
        'python_name': '_EnumWithConverter',
        'converted_value_to_enum_function_name': 'convert_to_enum_with_converter_enum',
        'enum_to_converted_value_function_name': 'convert_from_enum_with_converter_enum',
        'values': [
            {'name': 'RED', 'value': 1, 'converts_to_value': True, 'python_name': 'RED'},
            {'name': 'BLUE', 'value': 2, 'converts_to_value': False, 'python_name': 'BLUE'},
            {'name': 'YELLOW', 'value': 5, 'converts_to_value': 'yellow', 'python_name': 'YELLOW'},
            {'name': 'BLACK', 'value': 42, 'converts_to_value': 42, 'python_name': 'BLACK'}
        ]
    },
}


config_input = {
    'metadata_version': '1.0',
    'module_name': 'nifake',
    'module_version': '1.1.1.dev0',
    'c_function_prefix': 'niFake_',
    'driver_name': 'NI-FAKE',
    'session_class_description': 'An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation',
    'session_handle_parameter_name': 'vi',
    'library_info':
    {
        'Windows': {
            '32bit': {'name': 'nifake_32.dll', 'type': 'windll'},
            '64bit': {'name': 'nifake_64.dll', 'type': 'cdll'},
        },
        'Linux': {
            '64bit': {'name': 'libnifake.so', 'type': 'cdll'},
        },
    },
    'context_manager_name': {
        'task': 'acquisition',
        'initiate_function': 'Initiate',
        'abort_function': 'Abort',
    },
    'init_function': 'InitWithOptions',
    'close_function': 'close',
    'custom_types': [
        {
            'ctypes_type': 'struct_CustomStruct',
            'file_name': 'custom_struct',
            'grpc_name': 'CustomStruct',
            'python_name': 'CustomStruct',
        },
    ],
    'enum_whitelist_suffix': ['_POINT_FIVE'],
    'repeated_capabilities': [
        {'python_name': 'channels', 'prefix': '', },
    ],
    # These are added here strictly for testing.
    'functions': {},
    'attributes': {},
    'modules': {
        'metadata.enums_addon': {}
    },
}


config_expected = {
    'metadata_version': '1.0',
    'module_name': 'nifake',
    'module_version': '1.1.1.dev0',
    'c_function_prefix': 'niFake_',
    'driver_name': 'NI-FAKE',
    'session_class_description': 'An NI-FAKE session to a fake MI driver whose sole purpose is to test nimi-python code generation',
    'session_handle_parameter_name': 'vi',
    'library_info':
    {
        'Windows': {
            '32bit': {'name': 'nifake_32.dll', 'type': 'windll'},
            '64bit': {'name': 'nifake_64.dll', 'type': 'cdll'},
        },
        'Linux': {
            '64bit': {'name': 'libnifake.so', 'type': 'cdll'},
        },
    },
    'context_manager_name': {
        'task': 'acquisition',
        'initiate_function': 'Initiate',
        'abort_function': 'Abort',
    },
    'init_function': 'InitWithOptions',
    'close_function': 'close',
    'custom_types': [
        {
            'ctypes_type': 'struct_CustomStruct',
            'file_name': 'custom_struct',
            'grpc_name': 'CustomStruct',
            'python_name': 'CustomStruct',
        },
    ],
    'enum_whitelist_suffix': ['_POINT_FIVE'],
    'repeated_capabilities': [
        {'python_name': 'channels', 'prefix': '', },
    ],
    'use_locking': True,
    'functions': functions_expected,
    'attributes': attributes_expected,
    'enums': enums_expected,
    'modules': {
        'metadata.enums_addon': {}
    },
    'uses_nitclk': False,
}


def _do_the_test_add_functions_metadata(functions, expected):
    actual = copy.deepcopy(functions)
    actual = add_all_function_metadata(actual, config_input)
    _compare_dicts(actual, expected)


def test_add_functions_metadata_simple():
    _do_the_test_add_functions_metadata(functions=functions_input, expected=functions_expected)


def _do_the_test_add_attributes_metadata(attributes, expected):
    actual = copy.deepcopy(attributes)
    actual = add_all_attribute_metadata(actual, config_input)
    _compare_dicts(actual, expected)


def test_add_attributes_metadata_simple():
    _do_the_test_add_attributes_metadata(attributes=attributes_input, expected=attributes_expected)


def _do_the_test_add_enums_metadata(enums, expected):
    actual = copy.deepcopy(enums)
    actual = add_all_enum_metadata(actual, config_input)
    _compare_dicts(actual, expected)


def test_add_enums_metadata_simple():
    _do_the_test_add_enums_metadata(enums_input, expected=enums_expected)


def _do_the_test_add_all_metadata(functions, attributes, enums, config, expected):
    actual = add_all_metadata(functions, attributes, enums, config, persist_output=False)
    _compare_dicts(actual, expected)


def test_add_all_metadata_defaults():
    actual_functions = copy.deepcopy(functions_input)
    actual_attributes = copy.deepcopy(attributes_input)
    actual_enums = copy.deepcopy(enums_input)
    actual_config = copy.deepcopy(config_input)
    _do_the_test_add_all_metadata(
        functions=actual_functions,
        attributes=actual_attributes,
        enums=actual_enums,
        config=actual_config,
        expected=config_expected)


def test_add_all_metadata():
    actual_functions = copy.deepcopy(functions_input)
    actual_attributes = copy.deepcopy(attributes_input)
    actual_enums = copy.deepcopy(enums_input)
    actual_config = copy.deepcopy(config_input)
    actual_config['use_locking'] = False
    expected = copy.deepcopy(config_expected)
    expected['use_locking'] = False
    _do_the_test_add_all_metadata(
        functions=actual_functions,
        attributes=actual_attributes,
        enums=actual_enums,
        config=actual_config,
        expected=expected)


def _setup_inputs_for_enum_codegen_method_tests():
    actual_enums = copy.deepcopy(enums_input)
    actual_config = copy.deepcopy(config_input)
    # Set up minimal input functions metadata
    actual_config['functions'] = {
        'PublicMethod': {
            'codegen_method': 'public',
            'parameters': [{'enum': None}, {'enum': 'EnumWithConverter'}],
        },
        'PythonOnlyMethod': {
            'codegen_method': 'python-only',
            'parameters': [{'enum': 'Color'}, {'enum': None}],
        },
        'PrivateMethod': {
            'codegen_method': 'private',
            'parameters': [{'enum': 'EnumWithConverter'}],
        },
        'NoCodegenMethod': {
            'codegen_method': 'no',
            'parameters': [{'enum': 'Color'}],
        },
    }
    # Set up minimal input attributes metadata
    actual_config['attributes'] = {
        '1000000': {'codegen_method': 'public', 'name': 'PUBLIC_ATTR', 'enum': None},
        '1000001': {'codegen_method': 'public', 'name': 'PUBLIC_ATTR_2', 'enum': 'EnumWithConverter'},
        '1000002': {'codegen_method': 'private', 'name': 'PRIVATE_ATTR', 'enum': 'Color'},
        '1000003': {'codegen_method': 'private', 'name': 'PRIVATE_ATTR_2', 'enum': 'EnumWithConverter'},
        '1000004': {'codegen_method': 'no', 'name': 'NO_CODEGEN_ATTR', 'enum': 'Color'},
    }
    return actual_enums, actual_config


def test_add_enum_codegen_method():
    actual_enums, actual_config = _setup_inputs_for_enum_codegen_method_tests()
    _add_enum_codegen_method(actual_enums, actual_config)
    assert actual_enums['Color']['codegen_method'] == 'public'
    assert actual_enums['EnumWithConverter']['codegen_method'] == 'private'


def test_add_enum_codegen_method_error():
    actual_enums, actual_config = _setup_inputs_for_enum_codegen_method_tests()
    actual_enums['Color']['codegen_method'] = 'private'
    expected_error_description = "Codegen_method of enum Color used by functions ['PythonOnlyMethod'] and attributes ['PRIVATE_ATTR'] must be public, is private"
    try:
        _add_enum_codegen_method(actual_enums, actual_config)
    except ValueError as actual_error:
        actual_error_message = actual_error.args[0]
        assert actual_error_message == expected_error_description


def test_get_functions_that_use_enums():
    actual_enums, actual_config = _setup_inputs_for_enum_codegen_method_tests()
    expected_output = {
        'Color': ['PythonOnlyMethod'],
        'EnumWithConverter': ['PublicMethod', 'PrivateMethod'],
    }
    actual_output = _get_functions_that_use_enums(actual_enums, actual_config)
    _compare_dicts(actual_output, expected_output)


def test_get_attributes_that_use_enums():
    actual_enums, actual_config = _setup_inputs_for_enum_codegen_method_tests()
    expected_output = {
        'Color': ['1000002'],
        'EnumWithConverter': ['1000001', '1000003'],
    }
    actual_output = _get_attributes_that_use_enums(actual_enums, actual_config)
    _compare_dicts(actual_output, expected_output)


def test_get_least_restrictive_codegen_method():
    for codegen_methods, expected_least_restrictive_codegen_method in (
        ([], 'no'),
        (['no'], 'no'),
        (['private', 'private'], 'private'),
        (['no', 'private'], 'private'),
        (['public', 'private'], 'public'),
        (['private', 'python-only', 'private', 'no'], 'public'),
        (['public', 'python-only', 'public'], 'public')
    ):
        assert _get_least_restrictive_codegen_method(
            codegen_methods
        ) == expected_least_restrictive_codegen_method
