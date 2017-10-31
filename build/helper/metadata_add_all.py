# Useful functions for use in the metadata modules

from .helper import camelcase_to_snakecase
from .helper import get_python_type_for_visa_type
from .metadata_filters import filter_codegen_functions
from .metadata_merge_dicts import merge_dicts

import copy
import pprint

pp = pprint.PrettyPrinter(indent=4, width=80)

# Functions to add information to metadata structures that are specific to our codegen needs.


def _add_name(function, name):
    '''Adds a name' key/value pair to the function metadata'''
    assert 'name' not in function, "'name' is already populated which means issue #372 is closed, rendering _add_name() redundant."
    function['name'] = name
    return function


def _add_python_method_name(function, name):
    '''Adds a python_name' key/value pair to the function metadata'''
    if function['codegen_method'] == 'private':
        function['python_name'] = '_' + camelcase_to_snakecase(name)
    else:
        function['python_name'] = camelcase_to_snakecase(name)
    return function


def _add_python_parameter_name(parameter):
    '''Adds a python_name key/value pair to the parameter metadata'''
    parameter['python_name'] = camelcase_to_snakecase(parameter['name'])
    return parameter


def _add_python_type(parameter):
    '''Adds the type to use in the Python API to the parameter metadata'''
    if parameter['enum'] is None:
        parameter['python_type'] = get_python_type_for_visa_type(parameter['type'])
    else:
        parameter['python_type'] = 'enums.' + parameter['enum']
    return parameter


def _add_ctypes_variable_name(parameter):
    '''Adds a ctypes_variable_name key/value pair to the parameter metadata for a corresponding ctypes variable'''
    parameter['ctypes_variable_name'] = parameter['python_name'] + '_ctype'
    return parameter


def _add_ctypes_type(parameter):
    '''Adds a ctypes_type key/value pair to the parameter metadata for calling into the library'''
    parameter['ctypes_type'] = parameter['type']
    if parameter['direction'] == 'out' or parameter['is_buffer'] is True:
        parameter['ctypes_type_library_call'] = "ctypes.POINTER(" + parameter['ctypes_type'] + ")"
    else:
        parameter['ctypes_type_library_call'] = parameter['ctypes_type']

    return parameter


def _add_is_error_handling(f):
    '''Adds is_error_handling information to the function metadata if it isn't already defined. Defaults to False.'''
    # TODO(marcoskirsch): The information is added in functions_addon.py. I think we can instead infer from method
    # name but I am not sure if it's a good idea (heuristics vs being explicit - both error prone in different ways).
    if 'is_error_handling' not in f:
        # Not populated, assume False
        f['is_error_handling'] = False
    return f


def _add_buffer_info(parameter):
    '''Adds buffer information to the parameter metadata iff 'size' is defined else assume not a buffer'''

    # For simplicity, we are going to treat ViChar[], ViString, ViConstString, and ViRsrc the same: As ViChar
    # and is_buffer True
    t = parameter['type']
    if t == 'ViString' or t == 'ViConstString' or t == 'ViRsrc':
        parameter['type'] = 'ViChar'
        parameter['original_type'] = t
        parameter['is_buffer'] = True

    if (t.find('[ ]') > 0) or (t.find('[]') > 0):
        parameter['type'] = t.replace('[ ]', '').replace('[]', '')
        parameter['original_type'] = t
        parameter['is_buffer'] = True

    if 'size' not in parameter:
        # Not populated, assume {'mechanism': 'fixed', 'value': 1}
        parameter['size'] = {'mechanism': 'fixed', 'value': 1}

    if 'is_buffer' not in parameter:
        # Not populated, assume False
        parameter['is_buffer'] = False

    return parameter


def _add_library_method_call_snippet(parameter):
    '''Code snippet for calling a method of Library for this parameter.'''
    if parameter['direction'] == 'out' and parameter['is_buffer'] is False:
        parameter['library_method_call_snippet'] = 'ctypes.pointer({0})'.format(parameter['ctypes_variable_name'])
    else:
        parameter['library_method_call_snippet'] = parameter['ctypes_variable_name']


def _add_default_value_name(parameter):
    '''Declaration with default value, if set'''
    if 'default_value' in parameter:
        if 'enum' in parameter and parameter['enum'] is not None:
            name = parameter['python_name'] + "=enums." + parameter['default_value']
        else:
            name = parameter['python_name'] + "=" + repr(parameter['default_value'])

    else:
        name = parameter['python_name']

    parameter['python_name_with_default'] = name


def _add_default_value_name_for_docs(parameter, module_name):
    '''Declaration with default value, if set'''
    if 'default_value' in parameter:
        if 'enum' in parameter and parameter['enum'] is not None:
            name = parameter['python_name'] + "=" + module_name + '.' + parameter['default_value']
        else:
            name = parameter['python_name'] + "=" + repr(parameter['default_value'])

    else:
        name = parameter['python_name']

    parameter['python_name_with_doc_default'] = name


# Parameter names denoting channel/repeated capabilities was compiled by looking at public header files for different MI drivers.
_repeated_capability_parameter_names = ['channelName', 'channelList', 'channel', 'channelNameList']


def _add_has_repeated_capability(f):
    '''Adds a boolean 'has_repeated_capability' to the function metadata by inferring it from its parameter names, if not previously populated..'''
    if 'has_repeated_capability' not in f:
        f['has_repeated_capability'] = False
        for p in f['parameters']:
            f['has_repeated_capability'] = f['has_repeated_capability'] or p['name'] in _repeated_capability_parameter_names


def _add_is_repeated_capability(parameter):
    '''Adds a boolean 'is_repeated_capability' to the parameter metadata by inferring it from its name, if not previously populated.'''
    if 'is_repeated_capability' not in parameter:
        parameter['is_repeated_capability'] = parameter['name'] in _repeated_capability_parameter_names


def _add_is_session_handle(parameter):
    '''Adds a boolean 'is_session_handle' to the parameter metadata by inferring it from its type, if not previously populated.'''
    if 'is_session_handle' not in parameter:
        parameter['is_session_handle'] = parameter['type'] == 'ViSession' and parameter['direction'] == 'in'


def add_all_function_metadata(functions, config):
    '''Merges and Adds all codegen-specific metada to the function metadata list'''
    if 'modules' in config and 'metadata.functions_addon' in config['modules']:
        for m in dir(config['modules']['metadata.functions_addon']):
            if m.startswith('functions_'):
                merge_dicts(functions, config['modules']['metadata.functions_addon'].__getattribute__(m))

    for f in filter_codegen_functions(functions):
        _add_name(functions[f], f)
        _add_python_method_name(functions[f], f)
        _add_is_error_handling(functions[f])
        _add_has_repeated_capability(functions[f])
        for p in functions[f]['parameters']:
            _add_buffer_info(p)
            _add_python_parameter_name(p)
            _add_python_type(p)
            _add_ctypes_variable_name(p)
            _add_ctypes_type(p)
            _add_default_value_name(p)
            _add_default_value_name_for_docs(p, config['module_name'])
            _add_is_repeated_capability(p)
            _add_is_session_handle(p)
            _add_library_method_call_snippet(p)
    return functions


def _add_codegen_method(a, attributes):
    '''Adds 'codegen_method' that will determine whether and how the attribute is code genned. Default is public'''
    if 'codegen_method' not in attributes[a]:
        attributes[a]['codegen_method'] = 'public'


def _add_python_name(a, attributes):
    '''Adds 'python_name' - lower case + leading '_' if first character is a digit'''
    n = attributes[a]['name'].lower()
    if attributes[a]['name'][0].isdigit():
        n = '_' + n
    attributes[a]['python_name'] = n


def add_all_attribute_metadata(attributes, config):
    '''Merges and Adds all codegen-specific metada to the function metadata list'''
    if 'modules' in config and 'metadata.functions_addon' in config['modules']:
        for m in dir(config['modules']['metadata.attributes_addon']):
            if m.startswith('attributes_'):
                merge_dicts(attributes, config['modules']['metadata.attributes_addon'].__getattribute__(m))

    for a in attributes:
        _add_codegen_method(a, attributes)
        _add_python_name(a, attributes)

    return attributes


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


def _do_the_test_add_all_metadata(functions, expected):
    actual = copy.deepcopy(functions)
    actual = add_all_function_metadata(actual, {'session_handle_parameter_name': 'vi', 'module_name': 'nifake'})
    _compare_dicts(actual, expected)


def test_add_all_metadata_simple():
    functions = {
        'MakeAFoo': {
            'codegen_method': 'public',
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
                    'direction': 'in',
                    'enum': None,
                    'name': 'channelName',
                    'type': 'ViString',
                    'documentation': {
                        'description': 'The channel to call this on.',
                    },
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
                }
            ],
            'documentation': {
                'description': 'Perform actions as method defined',
            },
        },
    }
    expected = {
        'MakeAFoo': {
            'name': 'MakeAFoo',
            'codegen_method': 'public',
            'documentation': {
                'description': 'Performs a foo, and performs it well.'
            },
            'has_repeated_capability': True,
            'is_error_handling': False,
            'parameters': [
                {
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
                    'python_type': 'int',
                    'is_buffer': False,
                    'name': 'vi',
                    'python_name': 'vi',
                    'python_name_with_default': 'vi',
                    'python_name_with_doc_default': 'vi',
                    'size': {
                        'mechanism': 'fixed',
                        'value': 1
                    },
                    'type': 'ViSession',
                    'library_method_call_snippet': 'vi_ctype',
                },
                {
                    'ctypes_type': 'ViChar',
                    'ctypes_variable_name': 'channel_name_ctype',
                    'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
                    'direction': 'in',
                    'documentation': {
                        'description': 'The channel to call this on.'
                    },
                    'is_repeated_capability': True,
                    'is_session_handle': False,
                    'enum': None,
                    'python_type': 'int',
                    'is_buffer': True,
                    'name': 'channelName',
                    'python_name': 'channel_name',
                    'python_name_with_default': 'channel_name',
                    'python_name_with_doc_default': 'channel_name',
                    'size': {'mechanism': 'fixed', 'value': 1},
                    'type': 'ViChar',
                    'original_type': 'ViString',
                    'library_method_call_snippet': 'channel_name_ctype',
                },
            ],
            'python_name': 'make_a_foo',
            'returns': 'ViStatus',
        },
        'MakeAPrivateMethod': {
            'codegen_method': 'private',
            'returns': 'ViStatus',
            'parameters': [{
                'direction': 'in',
                'enum': None,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'python_name': 'vi',
                'python_type': 'int',
                'ctypes_variable_name': 'vi_ctype',
                'ctypes_type': 'ViSession',
                'ctypes_type_library_call': 'ViSession',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'is_buffer': False,
                'python_name_with_default': 'vi',
                'python_name_with_doc_default': 'vi',
                'is_repeated_capability': False,
                'is_session_handle': True,
                'library_method_call_snippet': 'vi_ctype'
            }, {
                'direction': 'out',
                'enum': None,
                'name': 'status',
                'type': 'ViChar',
                'original_type': 'ViString',
                'documentation': {
                    'description': 'Return a device status'
                },
                'python_name': 'status',
                'python_type': 'int',
                'ctypes_variable_name': 'status_ctype',
                'ctypes_type': 'ViChar',
                'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'is_buffer': True,
                'python_name_with_default': 'status',
                'python_name_with_doc_default': 'status',
                'is_repeated_capability': False,
                'is_session_handle': False,
                'library_method_call_snippet': 'status_ctype'
            }],
            'documentation': {
                'description': 'Perform actions as method defined'
            },
            'name': 'MakeAPrivateMethod',
            'python_name': '_make_a_private_method',
            'is_error_handling': False,
            'has_repeated_capability': False
        }
    }

    _do_the_test_add_all_metadata(functions, expected)
