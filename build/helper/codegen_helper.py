import builtins

from .helper import get_array_type_for_api_type
from .metadata_filters import filter_parameters
from .metadata_find import find_custom_type
from .metadata_find import find_size_parameter
from .parameter_usage_options import ParameterUsageOptions
from enum import Enum
import pprint

pp = pprint.PrettyPrinter(indent=4, width=200)

_ParameterUsageOptionsSnippet = {
    ParameterUsageOptions.SESSION_METHOD_DECLARATION: {
        'skip_self': False,
        'name_to_use': 'python_name_with_default',
    },
    ParameterUsageOptions.SESSION_METHOD_PASSTHROUGH_CALL: {
        'skip_self': True,
        'name_to_use': 'python_name',
    },
    ParameterUsageOptions.SESSION_INIT_DECLARATION: {
        'skip_self': False,
        'name_to_use': 'python_name_with_default',
    },
    ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION: {
        'skip_self': False,
        'name_to_use': 'python_name_with_default',
    },
    ParameterUsageOptions.INTERPRETER_NUMPY_INTO_METHOD_DECLARATION: {
        'skip_self': False,
        'name_to_use': 'python_name',
    },
    ParameterUsageOptions.INTERPRETER_NUMPY_INTO_METHOD_CALL: {
        'skip_self': True,
        'name_to_use': 'interpreter_method_call_snippet',
    },
    ParameterUsageOptions.SESSION_METHOD_CALL: {
        'skip_self': True,
        'name_to_use': 'python_name',
    },
    ParameterUsageOptions.SESSION_INIT_CALL: {
        'skip_self': True,
        'name_to_use': 'python_name_or_default_for_init',
    },
    ParameterUsageOptions.DOCUMENTATION_SESSION_METHOD: {
        'skip_self': True,
        'name_to_use': 'python_name_with_doc_default',
    },
    ParameterUsageOptions.LIBRARY_METHOD_DECLARATION: {
        'skip_self': False,
        'name_to_use': 'python_name',
    },
    ParameterUsageOptions.LIBRARY_METHOD_CALL: {
        'skip_self': True,
        # when calling into Library, we need to build and pass parameters as ctypes types
        'name_to_use': 'ctypes_method_call_snippet',
    },
    ParameterUsageOptions.CDLL_METHOD_CALL: {
        'skip_self': True,
        'name_to_use': 'python_name',
    },
    ParameterUsageOptions.INTERPRETER_METHOD_CALL: {
        'skip_self': True,
        'name_to_use': 'interpreter_method_call_snippet',
    },
    ParameterUsageOptions.CTYPES_ARGTYPES: {
        'skip_self': True,
        'name_to_use': 'ctypes_type_library_call',
    },
    ParameterUsageOptions.INTERPRETER_METHOD_DECLARATION: {
        'skip_self': False,
        'name_to_use': 'python_name',
    },
    ParameterUsageOptions.GRPC_REQUEST_PARAMETERS: {
        'skip_self': True,
        'name_to_use': 'grpc_request_snippet',
    },
}
# Only used for filtering
#   ParameterUsageOptions.INPUT_PARAMETERS
#   ParameterUsageOptions.LIBRARY_OUTPUT_PARAMETERS
#   ParameterUsageOptions.API_OUTPUT_PARAMETERS
#   ParameterUsageOptions.API_NUMPY_OUTPUT_PARAMETERS
#   ParameterUsageOptions.IVI_DANCE_PARAMETER
#   ParameterUsageOptions.LEN_PARAMETER
#   ParameterUsageOptions.INPUT_ENUM_PARAMETERS
#   ParameterUsageOptions.GRPC_OUTPUT_PARAMETERS


# Functions that return snippets that can be placed directly in the templates.
def get_params_snippet(function, parameter_usage_options):
    '''get_params_snippet

    Get a parameter list snippet based on parameter_usage_options.
    '''
    if type(parameter_usage_options) is not ParameterUsageOptions:
        raise TypeError('parameter_usage_options must be of type ' + str(ParameterUsageOptions))

    options_to_use = _ParameterUsageOptionsSnippet[parameter_usage_options]

    parameters_to_use = filter_parameters(function['parameters'], parameter_usage_options)

    snippets = []
    if not options_to_use['skip_self']:
        snippets.append('self')

    # Render based on options
    for p in parameters_to_use:
        snippets.append(p[options_to_use['name_to_use']])
    return ', '.join(snippets)


def _get_interpreter_output_param_return_type(output_parameter, config):
    assert output_parameter['direction'] == 'out', 'Expected parameter {0} (a.k.a. {1}) to have direction out'.format(output_parameter['name'], output_parameter['python_name'])

    custom_type = find_custom_type(output_parameter, config)
    is_custom_type = custom_type is not None

    module_name = custom_type['file_name'] + '.' if is_custom_type else ''

    if output_parameter['enum'] is not None:
        return 'enums.' + output_parameter['enum'], is_custom_type
    else:
        return module_name + output_parameter['python_type'], is_custom_type


def _get_library_interpreter_output_param_return_snippet(output_parameter, parameters, config):
    '''Returns the snippet for returning a single output parameter from a LibraryInterpreter method, i.e. "reading_ctype.value"'''
    return_type, is_custom_type = _get_interpreter_output_param_return_type(output_parameter, config)
    # Custom types (i.e. inherit from ctypes.Structure) don't need a .value
    val_suffix = '' if is_custom_type else '.value'

    if output_parameter['use_array']:
        snippet = '{0}_array'.format(output_parameter['python_name'])
    elif output_parameter['is_buffer']:
        if output_parameter['size']['mechanism'] == 'fixed':
            size = str(output_parameter['size']['value'])
        elif output_parameter['size']['mechanism'] == 'python-code':
            size = output_parameter['size']['value']
        else:
            size_parameter = find_size_parameter(output_parameter, parameters)
            size = size_parameter['ctypes_variable_name'] + '.value'

        snippet = '[' + return_type + '(' + output_parameter['ctypes_variable_name'] + '[i]) for i in range(' + size + ')]'
    else:
        if output_parameter['is_string']:
            # '_encoding' is a variable on the LibraryInterpreter object
            snippet = output_parameter['ctypes_variable_name'] + '.value.decode(self._encoding)'
        else:
            snippet = return_type + '(' + output_parameter['ctypes_variable_name'] + val_suffix + ')'

    return snippet


def _get_grpc_interpreter_output_param_return_snippet(output_parameter, parameters, config):
    param_accessor = 'response.' + output_parameter['grpc_name']
    if output_parameter['grpc_enum'] is not None:
        param_accessor += '_raw'

    return_type, is_custom_type = _get_interpreter_output_param_return_type(output_parameter, config)
    if hasattr(builtins, return_type):
        return_type = None

    convert_array_elements = output_parameter['is_buffer'] and return_type is not None
    if output_parameter.get('python_api_converter_name') == 'convert_to_bytes':
        # Don't convert individual array elements; convert_to_bytes will handle it
        convert_array_elements = False

    if convert_array_elements:
        return '[' + return_type + '(x) for x in ' + param_accessor + ']'
    elif return_type is not None:
        return return_type + '(' + param_accessor + ')'
    else:
        return param_accessor


def _get_session_output_param_return_snippet(output_parameter, parameters, config):
    '''Returns the snippet for returning a single output parameter from a Session method'''
    snippet = output_parameter['python_name']

    # Handle output converter
    if 'python_api_converter_name' in output_parameter:
        snippet = '_converters.' + output_parameter['python_api_converter_name'] + '(' + snippet + ')'

    return snippet


def get_library_interpreter_method_return_snippet(parameters, config, use_numpy_array=False):
    '''Returns a string suitable to use as the return argument of a LibraryInterpreter method, i.e. "return reading_ctype.value"'''
    options = ParameterUsageOptions.API_NUMPY_OUTPUT_PARAMETERS if use_numpy_array else ParameterUsageOptions.API_OUTPUT_PARAMETERS
    parameters_to_use = filter_parameters(parameters, options)
    snippets = [_get_library_interpreter_output_param_return_snippet(p, parameters, config) for p in parameters_to_use]
    return ('return ' + ', '.join(snippets)).strip()


def get_grpc_interpreter_method_return_snippet(parameters, config):
    '''Returns a string suitable to use as the return argument of a _gprc.LibraryInterpreter method'''
    parameters_to_use = filter_parameters(parameters, ParameterUsageOptions.API_OUTPUT_PARAMETERS)
    snippets = [_get_grpc_interpreter_output_param_return_snippet(p, parameters, config) for p in parameters_to_use]
    return ('return ' + ', '.join(snippets)).strip()


def get_session_method_return_snippet(parameters, config, use_numpy_array=False):
    '''Returns a string suitable to use as the return argument of a Session method'''
    options = ParameterUsageOptions.API_NUMPY_OUTPUT_PARAMETERS if use_numpy_array else ParameterUsageOptions.API_OUTPUT_PARAMETERS
    parameters_to_use = filter_parameters(parameters, options)
    snippets = [_get_session_output_param_return_snippet(p, parameters, config) for p in parameters_to_use]
    return ('return ' + ', '.join(snippets)).strip()


def get_enum_type_check_snippet(parameter, indent):
    '''Returns python snippet to check that the type of a parameter is what is expected'''
    assert parameter['enum'] is not None, pp.pformat(parameter)
    assert parameter['direction'] == 'in', pp.pformat(parameter)
    enum_check = 'if type(' + parameter['python_name'] + ') is not ' + parameter['python_type'] + ':\n'
    enum_check += (' ' * indent) + 'raise TypeError(\'Parameter {0} must be of type \' + str({1}))'.format(parameter['python_name'], parameter['python_type'])
    return enum_check


def _get_buffer_parameters_for_size_parameter(parameter, parameters):
    '''Return all parameters that use this parameter for size. Empty list if none'''
    buffer_params = []
    for p in parameters:
        if (p['is_buffer'] or p['is_string']) and p['size']['value'] == parameter['name']:
            buffer_params.append(p)
        elif (p['is_buffer'] or p['is_string']) and 'value_twist' in p['size'] and p['size']['value_twist'] == parameter['name']:
            buffer_params.append(p)
    return buffer_params


class IviDanceStep(Enum):
    NOT_APPLICABLE = 0
    'Use this when the function in question does not do the IVI dance.'

    QUERY_SIZE = 1
    'Step 1: Call into the driver in order to query the size of the buffer to be allocated.'

    GET_DATA = 2
    'Step 2: Allocate the buffer, call back into the driver to get the actual data.'


def get_ctype_variable_declaration_snippet(parameter, parameters, ivi_dance_step, config, use_numpy_array=False):
    '''Returns array of python snippets that declares and initializes a ctypes variable for the parameter that can be passed to the Library.

    Logic for creating the appropriate snippet is split up in two helper functions. One for scalars and one for buffers.
    '''

    custom_type = find_custom_type(parameter, config)

    # Determine the module.
    if custom_type is not None:
        # Module is the file associated with that type.
        module_name = custom_type['file_name']
    elif parameter['numpy'] is True and use_numpy_array is True:
        assert parameter['is_buffer'] is True
        module_name = 'numpy'
    else:
        module_name = '_visatype'

    if parameter['is_string'] is True:
        definitions = _get_ctype_variable_definition_snippet_for_string(parameter, parameters, ivi_dance_step, module_name)
    elif parameter['is_buffer'] is True:
        definitions = _get_ctype_variable_definition_snippet_for_buffers(parameter, parameters, ivi_dance_step, use_numpy_array, custom_type, module_name)
    else:
        definitions = _get_ctype_variable_definition_snippet_for_scalar(parameter, parameters, ivi_dance_step, module_name, config)

    return definitions


def _get_ctype_variable_definition_snippet_for_string(parameter, parameters, ivi_dance_step, module_name):
    '''These are the different cases for initializing the ctype variables for strings

    C010. Input repeated capability:                                           ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))
    C020. Input string:                                                        ctypes.create_string_buffer(parameter_name.encode(self._encoding))
    C030. Input string enum:                                                   ctypes.create_string_buffer(parameter_name.value.encode(self._encoding))
    C050. Output buffer with mechanism ivi-dance, QUERY_SIZE:                  None
    C060. Output buffer with mechanism ivi-dance, GET_DATA:                    (visatype.ViChar * buffer_size_ctype.value)()
    C070. Output buffer with mechanism fixed-size:                             visatype.ViChar * 256
    C080. Output buffer with mechanism python-code:                            visatype.ViChar * <python_code>
    C090. Output buffer with mechanism ivi-dance-with-a-twist, QUERY_SIZE:     None
    C100. Output buffer with mechanism ivi-dance-with-a-twist, GET_DATA:       (visatype.ViChar * buffer_size_ctype.value)()
    '''
    definitions = []
    definition = None

    if parameter['direction'] == 'in':
        if parameter['is_repeated_capability'] is True:
            definition = 'ctypes.create_string_buffer({0}.encode(self._encoding))  # case C010'.format(parameter['python_name'])
        elif parameter['enum'] is not None:
            definition = 'ctypes.create_string_buffer({0}.value.encode(self._encoding))  # case C030'.format(parameter['python_name'])
        else:
            definition = 'ctypes.create_string_buffer({0}.encode(self._encoding))  # case C020'.format(parameter['python_name'])
    else:
        assert parameter['direction'] == 'out'
        if parameter['size']['mechanism'] == 'ivi-dance':
            if ivi_dance_step == IviDanceStep.QUERY_SIZE:
                definition = 'None  # case C050'
            elif ivi_dance_step == IviDanceStep.GET_DATA:
                size_parameter = find_size_parameter(parameter, parameters)
                definition = '({0}.ViChar * {1}.value)()  # case C060'.format(module_name, size_parameter['ctypes_variable_name'])
            else:
                assert False, "ivi_dance_step {0} not valid for parameter {1} with ['size']['mechanism'] == 'ivi-dance'".format(ivi_dance_step, parameter['name'])

        elif parameter['size']['mechanism'] == 'ivi-dance-with-a-twist':
            if ivi_dance_step == IviDanceStep.QUERY_SIZE:
                definition = 'None  # case C090'
            elif ivi_dance_step == IviDanceStep.GET_DATA:
                size_parameter = find_size_parameter(parameter, parameters, key='value_twist')
                definition = '({0}.ViChar * {1}.value)()  # case C100'.format(module_name, size_parameter['ctypes_variable_name'])
            else:
                assert False, "ivi_dance_step {0} not valid for parameter {1} with ['size']['mechanism'] == 'ivi-dance-with-a-twist'".format(ivi_dance_step, parameter['name'])

        elif parameter['size']['mechanism'] == 'fixed':
            assert parameter['size']['value'] != 1, "Parameter {0} has 'direction':'out' and 'size':{1}... seems wrong. Check your metadata, maybe you forgot to specify?".format(parameter['name'], parameter['size'])
            definition = '({0}.ViChar * {1})()  # case C070'.format(module_name, parameter['size']['value'])

        elif parameter['size']['mechanism'] == 'python-code':
            assert parameter['size']['value'] != 1, "Parameter {0} has 'direction':'out' and 'size':{1}... seems wrong. Check your metadata, maybe you forgot to specify?".format(parameter['name'], parameter['size'])
            definition = '({0}.ViChar * {1})()  # case C080'.format(module_name, parameter['size']['value'])

        else:
            assert False, "Invalid mechanism for parameters with 'direction':'out': " + str(parameter)

    if definition is not None:
        definitions.append(parameter['ctypes_variable_name'] + ' = ' + definition)

    return definitions


def _get_ctype_variable_definition_snippet_for_scalar(parameter, parameters, ivi_dance_step, module_name, config):
    '''These are the different cases for initializing the ctype variable for scalars:

        S110. Input session handle:                                                visatype.ViSession(self._vi)
        S120. Input is size of buffer with mechanism is python-code:               visatype.ViInt32(<custom python code>)
        S130. Input enum:                                                          visatype.ViInt32(parameter_name.value)
        S150. Input scalar:                                                        visatype.ViInt32(parameter_name)
        S160. Input is size of input buffer:                                       visatype.ViInt32(0 if list is None else len(list))
        S170. Input is size of output buffer with mechanism ivi-dance, QUERY_SIZE: visatype.ViInt32()
        S180. Input is size of output buffer with mechanism ivi-dance, GET_DATA:   visatype.ViInt32(error_code)
        S190. Input is size of output buffer with mechanism ivi-dance-with-a-twist, QUERY_SIZE: visatype.ViInt32()
        S200. Input is size of output buffer with mechanism ivi-dance-with-a-twist, GET_DATA:   visatype.ViInt32(error_code)
        S210. Input is size of output buffer with mechanism passed-in:             visatype.ViInt32(buffer_size)
        S220. Output scalar or enum:                                               visatype.ViInt32()

    Return Value (list): each item in the list will be one line needed for the declaration of that parameter
    '''

    assert parameter['is_buffer'] is False, 'Parameter {}'.format(parameter)
    assert parameter['numpy'] is False, 'Parameter {}'.format(parameter)
    corresponding_buffer_parameters = _get_buffer_parameters_for_size_parameter(parameter, parameters)

    definitions = []
    definition = None

    if parameter['direction'] == 'in':
        if parameter['is_session_handle'] is True:
            definition = '{0}.{1}(self._{2})  # case S110'.format(module_name, parameter['ctypes_type'], config['session_handle_parameter_name'])
        elif parameter['size']['mechanism'] == 'python-code':
            definition = '{0}.{1}({2})  # case S120'.format(module_name, parameter['ctypes_type'], parameter['size']['value'])
        elif parameter['enum'] is not None:
            definition = '{0}.{1}({2}.value)  # case S130'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
        elif not corresponding_buffer_parameters:
            definition = '{0}.{1}({2})  # case S150'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
        elif corresponding_buffer_parameters and corresponding_buffer_parameters[0]['direction'] == 'in':  # We are only looking at the first one to see if it is 'in'. Assumes all are the same here, assert below if not
            # Parameter denotes the size of another (the "corresponding") parameter.
            definitions.append(parameter['ctypes_variable_name'] + ' = {0}.{1}(0 if {2} is None else len({2}))  # case S160'.format(module_name, parameter['ctypes_type'], corresponding_buffer_parameters[0]['python_name']))
            for i in range(1, len(corresponding_buffer_parameters)):
                definitions.append('if {0} is not None and len({0}) != len({1}):  # case S160'.format(corresponding_buffer_parameters[i]['python_name'], corresponding_buffer_parameters[0]['python_name']))
                definitions.append('    raise ValueError("Length of {0} and {1} parameters do not match.")  # case S160'.format(corresponding_buffer_parameters[i]['python_name'], corresponding_buffer_parameters[0]['python_name']))
        else:
            if corresponding_buffer_parameters[0]['size']['mechanism'] == 'ivi-dance':  # We are only looking at the first one. Assumes all are the same here, assert below if not
                # Verify all corresponding_buffer_parameters are 'out' and 'ivi-dance'
                for p in corresponding_buffer_parameters:
                    assert p['direction'] == 'out'
                    assert p['size']['mechanism'] == 'ivi-dance'
                if ivi_dance_step == IviDanceStep.QUERY_SIZE:
                    definition = '{0}.{1}()  # case S170'.format(module_name, parameter['ctypes_type'])
                elif ivi_dance_step == IviDanceStep.GET_DATA:
                    definition = '{0}.{1}(error_code)  # case S180'.format(module_name, parameter['ctypes_type'])
                else:
                    assert False, "ivi_dance_step {0} not valid for parameter {1} with ['size']['mechanism'] == 'ivi-dance'".format(ivi_dance_step, parameter['name'])
            elif corresponding_buffer_parameters[0]['size']['mechanism'] == 'ivi-dance-with-a-twist':  # We are only looking at the first one. Assumes all are the same here, assert below if not
                # Verify all corresponding_buffer_parameters are 'out' and 'ivi-dance-with-a-twist'
                for p in corresponding_buffer_parameters:
                    assert p['direction'] == 'out'
                    assert p['size']['mechanism'] == 'ivi-dance-with-a-twist'
                if ivi_dance_step == IviDanceStep.QUERY_SIZE:
                    definition = '{0}.{1}(0)  # case S190'.format(module_name, parameter['ctypes_type'])
                elif ivi_dance_step == IviDanceStep.GET_DATA:
                    size_parameter_twist = find_size_parameter(corresponding_buffer_parameters[0], parameters, key='value_twist')
                    definition = '{0}.{1}({2}.value)  # case S200'.format(module_name, parameter['ctypes_type'], size_parameter_twist['ctypes_variable_name'])
                else:
                    assert False, "ivi_dance_step {0} not valid for parameter {1} with ['size']['mechanism'] == 'ivi-dance-with-a-twist'".format(ivi_dance_step, parameter['name'])
            else:
                # Verify all corresponding_buffer_parameters are 'out' and not 'fixed-size'
                for p in corresponding_buffer_parameters:
                    assert p['direction'] == 'out', 'Parameter direction not "out", Parameter: {}'.format(p['name'])
                    assert p['size']['mechanism'] != 'fixed-size' and p['size']['mechanism'] != 'fixed-size', 'Parameter: {0}, Actual mechanism: {1}'.format(p['name'], p['size']['mechanism'])
                definition = '{0}.{1}({2})  # case S210'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
    else:
        assert parameter['direction'] == 'out'
        definition = '{0}.{1}()  # case S220'.format(module_name, parameter['ctypes_type'])

    if definition is not None:
        definitions.append(parameter['ctypes_variable_name'] + ' = ' + definition)
    return definitions


def _get_ctype_variable_definition_snippet_for_buffers(parameter, parameters, ivi_dance_step, use_numpy_array, custom_type, module_name):
    '''These are the different cases for initializing the ctype variable for buffers:

        B510. Input/output numpy array:                                            _get_ctypes_pointer_for_buffer(value=waveform)
        B540. Input buffer (custom type):                                          _get_ctypes_pointer_for_buffer(value=[custom_struct(l) for l in list], library_type=custom_struct)
        B550. Input buffer of simple types:                                        _get_ctypes_pointer_for_buffer(value=array.array('d', list), library_type=visatype.ViReal64)
        B560. Output buffer with mechanism python-code:                            _get_ctypes_pointer_for_buffer(value=array.array('d'), library_type=ViInt32)
        B570. Output buffer with mechanism fixed-size:                             _get_ctypes_pointer_for_buffer(library_type=ViInt32, size=256)
        B580. Output buffer with mechanism ivi-dance, QUERY_SIZE:                  None
        B590. Output buffer with mechanism ivi-dance, GET_DATA:                    _get_ctypes_pointer_for_buffer(value=array.array('d', [0] * buffer_size_ctype.value, library_type=ViInt32)
        B600. Output buffer with mechanism passed-in:                              _get_ctypes_pointer_for_buffer(value-array.array('d', [0] * buffer_size, library_type=ViInt32)
        B610. Output buffer with mechanism ivi-dance-with-a-twist, QUERY_SIZE:     None
        B620. Output buffer with mechanism ivi-dance-with-a-twist, GET_DATA:       _get_ctypes_pointer_for_buffer(value=array.array('d', [0] * buffer_size_ctype.value, library_type=ViInt32)

    Return Value (list): each item in the list will be one line needed for the declaration of that parameter

    All versions that have array.array have an alternate format for lists
    '''

    assert parameter['is_buffer'] is True
    definitions = []
    definition = None

    if parameter['numpy'] is True and use_numpy_array is True:
        definition = '_get_ctypes_pointer_for_buffer(value={0})  # case B510'.format(parameter['python_name'])
    elif parameter['direction'] == 'in':
        if custom_type is not None:
            definition = '_get_ctypes_pointer_for_buffer([{0}.{1}(c) for c in {2}], library_type={0}.{1})  # case B540'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
        else:
            if parameter['use_array']:
                # If the incoming type is array.array, we can just use that, otherwise we need to create an array.array that is initialized with the passed in value, which must be iterable
                array_declaration = '{0}_array = _convert_to_array(value={0}, array_type="{1}")  # case B550'.format(parameter['python_name'], get_array_type_for_api_type(parameter['ctypes_type']))
                definitions.append(array_declaration)
                definition = '_get_ctypes_pointer_for_buffer(value={0}_array, library_type={1}.{2})  # case B550'.format(parameter['python_name'], module_name, parameter['ctypes_type'])
            elif parameter['use_list']:
                definition = '_get_ctypes_pointer_for_buffer(value={0}, library_type={1}.{2})  # case B550'.format(parameter['python_name'], module_name, parameter['ctypes_type'])
            else:
                assert False, "Expected either 'use_array' or 'use_list' to be True. Both False."
    else:
        assert parameter['direction'] == 'out'
        assert 'size' in parameter, "Parameter {0} is output buffer but metadata doesn't define its 'size'".format(parameter['name'])
        if parameter['size']['mechanism'] == 'python-code':
            line1 = '{0}_size = {1}  # case B560'.format(parameter['python_name'], parameter['size']['value'])
            definitions.append(line1)
            if parameter['use_array']:
                line2 = '{0}_array = array.array("{1}", [0] * {0}_size)  # case B560'.format(parameter['python_name'], get_array_type_for_api_type(parameter['ctypes_type']))
                definitions.append(line2)
                definition = '_get_ctypes_pointer_for_buffer(value={1}_array, library_type={0}.{2})  # case B560'.format(module_name, parameter['python_name'], parameter['ctypes_type'])
            elif parameter['use_list']:
                definition = '_get_ctypes_pointer_for_buffer(library_type={0}.{1}, size={2}_size)  # case B560'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
            else:
                assert False, "Expected either 'use_array' or 'use_list' to be True. Both False."
        elif parameter['size']['mechanism'] == 'fixed':
            assert parameter['size']['value'] != 1, "Parameter {0} has 'direction':'out' and 'size':{1}... seems wrong. Check your metadata, maybe you forgot to specify?".format(parameter['name'], parameter['size'])
            line1 = '{0}_size = {1}  # case B570'.format(parameter['python_name'], parameter['size']['value'])
            definitions.append(line1)
            if parameter['use_array']:
                line2 = '{0}_array = array.array("{1}", [0] * {0}_size)  # case B570'.format(parameter['python_name'], get_array_type_for_api_type(parameter['ctypes_type']))
                definitions.append(line2)
                definition = '_get_ctypes_pointer_for_buffer(value={1}_array, library_type={0}.{2})  # case B570'.format(module_name, parameter['python_name'], parameter['ctypes_type'])
            elif parameter['use_list']:
                definition = '_get_ctypes_pointer_for_buffer(library_type={0}.{1}, size={2}_size)  # case B570'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
            else:
                assert False, "Expected either 'use_array' or 'use_list' to be True. Both False."
        elif parameter['size']['mechanism'] == 'ivi-dance':
            if ivi_dance_step == IviDanceStep.QUERY_SIZE:
                definition = 'None  # case B580'
            elif ivi_dance_step == IviDanceStep.GET_DATA:
                size_parameter = find_size_parameter(parameter, parameters)
                line1 = '{0}_size = {1}.value  # case B590'.format(parameter['python_name'], size_parameter['ctypes_variable_name'])
                definitions.append(line1)
                if parameter['use_array']:
                    line2 = '{0}_array = array.array("{1}", [0] * {0}_size)  # case B590'.format(parameter['python_name'], get_array_type_for_api_type(parameter['ctypes_type']))
                    definition = '_get_ctypes_pointer_for_buffer(value={1}_array, library_type={0}.{2})  # case B590'.format(module_name, parameter['python_name'], parameter['ctypes_type'])
                    definitions.append(line2)
                elif parameter['use_list']:
                    definition = '_get_ctypes_pointer_for_buffer(library_type={0}.{1}, size={2}_size)  # case B590'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
                else:
                    assert False, "Expected either 'use_array' or 'use_list' to be True. Both False."
            else:
                assert False, "ivi_dance_step {0} not valid for parameter {1} with ['size']['mechanism'] == 'ivi-dance'".format(ivi_dance_step, parameter['name'])
        elif parameter['size']['mechanism'] == 'ivi-dance-with-a-twist':
            if ivi_dance_step == IviDanceStep.QUERY_SIZE:
                definition = 'None  # case B610'
            elif ivi_dance_step == IviDanceStep.GET_DATA:
                size_parameter_twist = find_size_parameter(parameter, parameters, key='value_twist')
                line1 = '{0}_size = {1}.value  # case B620'.format(parameter['python_name'], size_parameter_twist['ctypes_variable_name'])
                definitions.append(line1)
                if parameter['use_array']:
                    line2 = '{0}_array = array.array("{1}", [0] * {0}_size)  # case B620'.format(parameter['python_name'], get_array_type_for_api_type(parameter['ctypes_type']))
                    definitions.append(line2)
                    definition = '_get_ctypes_pointer_for_buffer(value={1}_array, library_type={0}.{2})  # case B620'.format(module_name, parameter['python_name'], parameter['ctypes_type'])
                elif parameter['use_list']:
                    definition = '_get_ctypes_pointer_for_buffer(library_type={0}.{1}, size={2}_size)  # case B620'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
                else:
                    assert False, "Expected either 'use_array' or 'use_list' to be True. Both False."
            else:
                assert False, "ivi_dance_step {0} not valid for parameter {1} with ['size']['mechanism'] == 'ivi-dance-with-a-twist'".format(ivi_dance_step, parameter['name'])
        elif parameter['size']['mechanism'] == 'passed-in':
            size_parameter = find_size_parameter(parameter, parameters)
            line1 = '{0}_size = {1}  # case B600'.format(parameter['python_name'], size_parameter['python_name'])
            definitions.append(line1)
            if parameter['use_array']:
                line2 = '{0}_array = array.array("{1}", [0] * {0}_size)  # case B600'.format(parameter['python_name'], get_array_type_for_api_type(parameter['ctypes_type']))
                definition = '_get_ctypes_pointer_for_buffer(value={1}_array, library_type={0}.{2})  # case B600'.format(module_name, parameter['python_name'], parameter['ctypes_type'])
                definitions.append(line2)
            elif parameter['use_list']:
                definition = '_get_ctypes_pointer_for_buffer(library_type={0}.{1}, size={2}_size)  # case B600'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
            else:
                assert False, "Expected either 'use_array' or 'use_list' to be True. Both False."
        else:
            assert False, "Invalid mechanism for parameters with 'direction':'out': " + str(parameter)

    definitions.append(parameter['ctypes_variable_name'] + ' = ' + definition)
    return definitions


def get_dictionary_snippet(d, indent=4):
    '''Returns a formatted dictionary'''
    d_str = pprint.pformat(d)
    d_lines = d_str.splitlines()
    return ('\n' + (' ' * indent)).join(d_lines)


def get_enum_value_snippet(value):
    '''Returns value formatted into string, surrounding it with single quotes if it is of str type'''
    return ("'{}'" if type(value) is str else "{}").format(value)


#
# Let's do some unit testing!
#


# We need a config object for our testing
config_for_testing = {
    'session_handle_parameter_name': 'vi',
    'module_name': 'nifake',
    'functions': {},
    'attributes': {},
    'modules': {
        'metadata.enums_addon': {}
    },
    'custom_types': [
        {'file_name': 'custom_struct', 'python_name': 'CustomStruct', 'ctypes_type': 'custom_struct', },
    ],
}


# We also need some function parameters that cover all cases.
parameters_for_testing = [
    {  # 0
        'ctypes_method_call_snippet': 'vi_ctype',
        'ctypes_type': 'ViSession',
        'ctypes_type_library_call': 'ViSession',
        'ctypes_variable_name': 'vi_ctype',
        'direction': 'in',
        'documentation': {'description': 'Identifies a particular instrument session.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'vi',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': True,
        'interpreter_method_call_snippet': 'self._vi',
        'name': 'vi',
        'python_name': 'vi',
        'python_name_with_default': 'vi',
        'python_name_with_doc_default': 'vi',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViSession',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 1
        'ctypes_method_call_snippet': 'ctypes.pointer(output_ctype)',
        'ctypes_type': 'ViInt64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt64)',
        'ctypes_variable_name': 'output_ctype',
        'direction': 'out',
        'documentation': {'description': 'A big number on its way out.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'output',
        'is_buffer': False,
        'is_string': False,
        'use_array': False,
        'use_list': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'output',
        'name': 'output',
        'python_name': 'output',
        'python_name_with_default': 'output',
        'python_name_with_doc_default': 'output',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt64',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 2
        'ctypes_method_call_snippet': 'error_message_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ViString',
        'ctypes_variable_name': 'error_message_ctype',
        'direction': 'out',
        'documentation': {'description': 'The error information formatted into a string.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'error_message',
        'is_buffer': False,
        'use_array': False,
        'use_list': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'error_message',
        'name': 'errorMessage',
        'python_name': 'error_message',
        'python_name_with_default': 'error_message',
        'python_name_with_doc_default': 'error_message',
        'python_type': 'str',
        'size': {'mechanism': 'fixed', 'value': 256},
        'type': 'ViString',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 3
        'ctypes_method_call_snippet': 'array_out_ctype',
        'ctypes_type': 'custom_struct',
        'ctypes_type_library_call': 'ctypes.POINTER(custom_struct)',
        'ctypes_variable_name': 'array_out_ctype',
        'direction': 'out',
        'documentation': {'description': 'Array of custom type using python-code size mechanism'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'array_out',
        'is_buffer': True,
        'use_array': False,
        'use_list': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'array_out',
        'name': 'arrayOut',
        'original_type': 'custom_struct[]',
        'python_name': 'array_out',
        'python_name_with_default': 'array_out',
        'python_name_with_doc_default': 'array_out',
        'python_type': 'CustomStruct',
        'size': {'mechanism': 'python-code', 'value': 'self.get_array_size_for_python_code()'},
        'type': 'custom_struct',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 4
        'ctypes_method_call_snippet': 'number_of_elements_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ViInt32',
        'ctypes_variable_name': 'number_of_elements_ctype',
        'direction': 'in',
        'documentation': {'description': 'Number of elements in the array.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'number_of_elements',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'number_of_elements',
        'name': 'numberOfElements',
        'python_name': 'number_of_elements',
        'python_name_with_default': 'number_of_elements',
        'python_name_with_doc_default': 'number_of_elements',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt32',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 5
        'ctypes_method_call_snippet': 'an_array_ctype',
        'ctypes_type': 'ViInt16',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt16)',
        'ctypes_variable_name': 'an_array_ctype',
        'direction': 'out',
        'documentation': {'description': 'Contains an array of enums, stored as 16 bit integers under the hood '},
        'enum': 'Turtle',
        'grpc_enum': 'Turtle',
        'grpc_name': 'an_array',
        'is_buffer': True,
        'use_array': False,
        'use_list': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'an_array',
        'name': 'anArray',
        'python_name': 'an_array',
        'python_name_with_default': 'an_array',
        'python_name_with_doc_default': 'an_array',
        'python_type': 'enums.Turtle',
        'size': {'mechanism': 'passed-in', 'value': 'numberOfElements'},
        'type': 'ViInt16',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 6
        'ctypes_method_call_snippet': 'an_int_enum_ctype',
        'ctypes_type': 'ViInt16',
        'ctypes_type_library_call': 'ViInt16',
        'ctypes_variable_name': 'an_int_enum_ctype',
        'direction': 'in',
        'documentation': {
            'description': 'Indicates a ninja turtle',
            'table_body': [['0', 'Leonardo'], ['1', 'Donatello'], ['2', 'Raphael'], ['3', 'Mich elangelo']]
        },
        'enum': 'Turtle',
        'grpc_enum': 'Turtle',
        'grpc_name': 'an_int_enum',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'an_int_enum',
        'name': 'anIntEnum',
        'python_name': 'an_int_enum',
        'python_name_with_default': 'an_int_enum',
        'python_name_with_doc_default': 'an_int_enum',
        'python_type': 'enums.Turtle',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt16',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 7
        'ctypes_method_call_snippet': 'ctypes.pointer(output_ctype)',
        'ctypes_type': 'ViInt64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt64)',
        'ctypes_variable_name': 'output_ctype',
        'direction': 'out',
        'documentation': {'description': 'A big number on its way out.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'output',
        'is_buffer': True,
        'use_array': True,
        'use_list': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'output',
        'name': 'output',
        'python_name': 'output',
        'python_name_with_default': 'output',
        'python_name_with_doc_default': 'output',
        'python_type': 'int',
        'size': {'mechanism': 'passed-in', 'value': 'numberOfElements'},
        'type': 'ViInt64',
        'numpy': True,
        'numpy_type': 'int64',
        'numpy_type_library_call': 'numpy.int64',
        'use_in_python_api': True,
    },
    {  # 8
        'ctypes_method_call_snippet': 'number_of_elements_python_code_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ViInt32',
        'ctypes_variable_name': 'number_of_elements_python_code_ctype',
        'direction': 'in',
        'documentation': {'description': 'Number of elements in the array, determined via mechanism python-code.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'number_of_elements_python_code',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'number_of_elements_python_code',
        'name': 'numberOfElementsPythonCode',
        'numpy': False,
        'python_name': 'number_of_elements_python_code',
        'python_name_with_default': 'number_of_elements_python_code',
        'python_name_with_doc_default': 'number_of_elements_python_code',
        'python_type': 'int',
        'size': {'mechanism': 'python-code', 'value': 'self.get_array_size_for_python_code()'},
        'type': 'ViInt32',
        'use_in_python_api': True,
    },
    {  # 9
        'ctypes_method_call_snippet': 'input_ctype',
        'ctypes_type': 'ViInt16',
        'ctypes_type_library_call': 'ViInt16',
        'ctypes_variable_name': 'input_ctype',
        'direction': 'in',
        'documentation': {'description': 'An input value.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input',
        'name': 'input',
        'numpy': False,
        'python_name': 'input',
        'python_name_with_default': 'input',
        'python_name_with_doc_default': 'input',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt16',
        'use_in_python_api': True,
    },
    {  # 10
        'ctypes_method_call_snippet': 'input_array_ctype',
        'ctypes_type': 'ViReal64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
        'ctypes_variable_name': 'input_array_ctype',
        'default_value': None,
        'direction': 'in',
        'documentation': {'description': 'Input array of floats'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array',
        'is_buffer': True,
        'is_string': False,
        'use_array': True,
        'use_list': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array',
        'name': 'inputArray',
        'numpy': False,
        'python_name': 'input_array',
        'python_name_with_default': 'input_array=None',
        'python_name_with_doc_default': 'input_array=None',
        'python_type': 'float',
        'size': {'mechanism': 'len', 'value': 'inputArraySize'},
        'type': 'ViReal64',
        'use_in_python_api': True,
    },
    {  # 11
        'ctypes_method_call_snippet': 'input_array_size_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ViInt32',
        'ctypes_variable_name': 'input_array_size_ctype',
        'direction': 'in',
        'documentation': {'description': 'Size of inputArray'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array_size',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array_size',
        'name': 'inputArraySize',
        'numpy': False,
        'python_name': 'input_array_size',
        'python_name_with_default': 'input_array_size',
        'python_name_with_doc_default': 'input_array_size',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt32',
        'use_in_python_api': True,
    },
    {  # 12
        'ctypes_method_call_snippet': 'string_size_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ViInt32',
        'ctypes_variable_name': 'string_size_ctype',
        'direction': 'in',
        'documentation': {'description': 'Number of bytes allocated for aString'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'string_size',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'string_size',
        'name': 'stringSize',
        'numpy': False,
        'python_name': 'string_size',
        'python_name_with_default': 'string_size',
        'python_name_with_doc_default': 'string_size',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt32',
        'use_in_python_api': True,
    },
    {  # 13
        'ctypes_method_call_snippet': 'a_string_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
        'ctypes_variable_name': 'a_string_ctype',
        'direction': 'out',
        'documentation': {'description': 'An IVI dance string.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_string',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_string',
        'name': 'aString',
        'numpy': False,
        'python_name': 'a_string',
        'python_name_with_default': 'a_string',
        'python_name_with_doc_default': 'a_string',
        'python_type': 'str',
        'size': {'mechanism': 'ivi-dance', 'value': 'stringSize'},
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 14
        'ctypes_method_call_snippet': 'timeout_ctype',
        'ctypes_type': 'ViReal64',
        'ctypes_type_library_call': 'ViReal64',
        'ctypes_variable_name': 'timeout_ctype',
        'default_value': 1.0,
        'direction': 'in',
        'documentation': {'description': 'Timeout in seconds'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'timeout',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'timeout',
        'name': 'Timeout',
        'numpy': False,
        'python_name': 'timeout',
        'python_name_with_default': 'timeout=1.0',
        'python_name_with_doc_default': 'timeout=1.0',
        'python_type': 'float',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViReal64',
        'use_in_python_api': True,
        'python_api_converter_name': 'timedelta_converter_seconds_real64',
    },
    {  # 15
        'ctypes_method_call_snippet': 'channel_list_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ViString',
        'ctypes_variable_name': 'channel_list_ctype',
        'direction': 'in',
        'documentation': {
            'description': 'The channel to configure. For more information, refer to `Channel String'
        },
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'channel_list',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': True,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'self._repeated_capability',
        'name': 'channelList',
        'numpy': False,
        'original_type': 'ViChar[]',
        'python_name': 'channel_list',
        'python_name_with_default': 'channel_list',
        'python_name_with_doc_default': 'channel_list',
        'python_type': 'str',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 16
        'ctypes_method_call_snippet': 'a_string_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ViString',
        'ctypes_variable_name': 'a_string_ctype',
        'direction': 'in',
        'documentation': {'description': 'An input string.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_string',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_string',
        'name': 'aString',
        'numpy': False,
        'python_name': 'a_string',
        'python_name_with_default': 'a_string',
        'python_name_with_doc_default': 'a_string',
        'python_type': 'int',
        'size': {'mechanism': 'len', 'value': 'a_string'},
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 17
        'ctypes_method_call_snippet': 'array_in_ctype',
        'ctypes_type': 'custom_struct',
        'ctypes_type_library_call': 'ctypes.POINTER(custom_struct)',
        'ctypes_variable_name': 'array_in_ctype',
        'direction': 'in',
        'documentation': {'description': 'Array of custom type using python-code size mechanism'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'array_in',
        'is_buffer': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'array_in',
        'name': 'arrayOut',
        'original_type': 'custom_struct[]',
        'python_name': 'array_in',
        'python_name_with_default': 'array_in',
        'python_name_with_doc_default': 'array_in',
        'python_type': 'CustomStruct',
        'size': {'mechanism': 'len', 'value': 'array_in'},
        'type': 'custom_struct',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 18
        'ctypes_method_call_snippet': 'an_int_ctype',
        'ctypes_type': 'ViInt16',
        'ctypes_type_library_call': 'ViInt16',
        'ctypes_variable_name': 'an_int_ctype',
        'direction': 'out',
        'documentation': {
            'description': 'Indicates a ninja turtle',
        },
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'an_int',
        'is_buffer': True,
        'use_array': True,
        'use_list': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'an_int',
        'name': 'anInt',
        'python_name': 'an_int',
        'python_name_with_default': 'an_int',
        'python_name_with_doc_default': 'an_int',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 256},
        'type': 'ViInt16',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 19
        'ctypes_method_call_snippet': 'a_string_2_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
        'ctypes_variable_name': 'a_string_2_ctype',
        'direction': 'out',
        'documentation': {'description': 'A fixed size string.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_string_2',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_string_2',
        'name': 'aString2',
        'numpy': False,
        'python_name': 'a_string_2',
        'python_name_with_default': 'a_string_2',
        'python_name_with_doc_default': 'a_string_2',
        'python_type': 'str',
        'size': {'mechanism': 'fixed', 'value': 256},
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 20
        'ctypes_method_call_snippet': 'a_string_3_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
        'ctypes_variable_name': 'a_string_3_ctype',
        'direction': 'out',
        'documentation': {'description': 'A python-code size string.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_string_3',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_string_3',
        'name': 'aStrin3g',
        'numpy': False,
        'python_name': 'a_string_3',
        'python_name_with_default': 'a_string_3',
        'python_name_with_doc_default': 'a_string_3',
        'python_type': 'str',
        'size': {'mechanism': 'python-code', 'value': 'string_size'},
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 21
        'ctypes_method_call_snippet': 'a_string_twist_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
        'ctypes_variable_name': 'a_string_twist_ctype',
        'direction': 'out',
        'documentation': {'description': 'An IVI dance with a twist string.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_string_twist',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_string_twist',
        'name': 'aStringTwist',
        'numpy': False,
        'python_name': 'a_string_twist',
        'python_name_with_default': 'a_string_twist',
        'python_name_with_doc_default': 'a_string_twist',
        'python_type': 'str',
        'size': {'mechanism': 'ivi-dance-with-a-twist', 'value': 'stringSizeTwist', 'value_twist': 'output_twist', },
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 22
        'ctypes_method_call_snippet': 'ctypes.pointer(output_twist_ctype)',
        'ctypes_type': 'ViInt64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt64)',
        'ctypes_variable_name': 'output_twist_ctype',
        'direction': 'out',
        'documentation': {'description': 'A big number on its way out.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'output_twist',
        'is_buffer': False,
        'is_string': False,
        'use_array': False,
        'use_list': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'output_twist',
        'name': 'output_twist',
        'python_name': 'output_twist',
        'python_name_with_default': 'output_twist',
        'python_name_with_doc_default': 'output_twist',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt64',
        'numpy': False,
        'use_in_python_api': True,
    },
    {  # 23
        'ctypes_method_call_snippet': 'string_size_twist_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ViInt32',
        'ctypes_variable_name': 'string_size_twist_ctype',
        'direction': 'in',
        'documentation': {'description': 'Number of bytes allocated for aStringTwist'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'string_size_twist',
        'is_buffer': False,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'string_size_twist',
        'name': 'stringSizeTwist',
        'numpy': False,
        'python_name': 'string_size_twist',
        'python_name_with_default': 'string_size_twist',
        'python_name_with_doc_default': 'string_size_twist',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt32',
        'use_in_python_api': True,
    },
    {  # 24
        'ctypes_method_call_snippet': 'a_buffer_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt32)',
        'ctypes_variable_name': 'a_buffer_array_ctype',
        'direction': 'out',
        'documentation': {'description': 'An IVI dance buffer using array.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_buffer_array',
        'is_buffer': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_buffer',
        'name': 'aBufferArray',
        'numpy': False,
        'python_name': 'a_buffer_array',
        'python_name_with_default': 'a_buffer_array',
        'python_name_with_doc_default': 'a_buffer_array',
        'python_type': 'int',
        'size': {'mechanism': 'ivi-dance', 'value': 'stringSize'},
        'type': 'ViInt32',
        'use_array': True,
        'use_list': False,
        'use_in_python_api': True,
    },
    {  # 25
        'ctypes_method_call_snippet': 'a_buffer_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt32)',
        'ctypes_variable_name': 'a_buffer_list_ctype',
        'direction': 'out',
        'documentation': {'description': 'An IVI dance buffer using a list.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_buffer_list',
        'is_buffer': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_buffer',
        'name': 'aBufferList',
        'numpy': False,
        'python_name': 'a_buffer_list',
        'python_name_with_default': 'a_buffer_list',
        'python_name_with_doc_default': 'a_buffer_list',
        'python_type': 'int',
        'size': {'mechanism': 'ivi-dance', 'value': 'stringSize'},
        'type': 'ViInt32',
        'use_array': False,
        'use_list': True,
        'use_in_python_api': True,
    },
    {  # 26
        'ctypes_method_call_snippet': 'a_buffer_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt32)',
        'ctypes_variable_name': 'a_buffer_twist_array_ctype',
        'direction': 'out',
        'documentation': {'description': 'An IVI dance with a twist buffer using an array.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_buffer_twist_array',
        'is_buffer': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_buffer',
        'name': 'aBufferTwistArray',
        'numpy': False,
        'python_name': 'a_buffer_twist_array',
        'python_name_with_default': 'a_buffer_twist_array',
        'python_name_with_doc_default': 'a_buffer_twist_array',
        'python_type': 'int',
        'size': {'mechanism': 'ivi-dance-with-a-twist', 'value': 'stringSizeTwist', 'value_twist': 'output_twist', },
        'type': 'ViInt32',
        'use_array': True,
        'use_list': False,
        'use_in_python_api': True,
    },
    {  # 27
        'ctypes_method_call_snippet': 'a_buffer_ctype',
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt32)',
        'ctypes_variable_name': 'a_buffer_twist_list_ctype',
        'direction': 'out',
        'documentation': {'description': 'An IVI dance with a twist buffer using a list.'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_buffer_twist_list',
        'is_buffer': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_buffer',
        'name': 'aBufferTwistList',
        'numpy': False,
        'python_name': 'a_buffer_twist_list',
        'python_name_with_default': 'a_buffer_twist_list',
        'python_name_with_doc_default': 'a_buffer_twist_list',
        'python_type': 'int',
        'size': {'mechanism': 'ivi-dance-with-a-twist', 'value': 'stringSizeTwist', 'value_twist': 'output_twist', },
        'type': 'ViInt32',
        'use_array': False,
        'use_list': True,
        'use_in_python_api': True,
    },
    {  # 28
        'ctypes_method_call_snippet': 'input_array_2_ctype',
        'ctypes_type': 'ViReal64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
        'ctypes_variable_name': 'input_array_2_ctype',
        'default_value': None,
        'direction': 'in',
        'documentation': {'description': 'Input array of floats'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array_2',
        'is_buffer': True,
        'is_string': False,
        'use_array': False,
        'use_list': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array_2',
        'name': 'inputArray2',
        'numpy': False,
        'python_name': 'input_array_2',
        'python_name_with_default': 'input_array_2=None',
        'python_name_with_doc_default': 'input_array_2=None',
        'python_type': 'float',
        'size': {'mechanism': 'len', 'value': 'inputArraySize2'},
        'type': 'ViReal64',
        'use_in_python_api': True,
    },
    {  # 29
        'ctypes_method_call_snippet': 'input_array_2_ctype',
        'ctypes_type': 'ViReal64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
        'ctypes_variable_name': 'input_array_2_ctype',
        'default_value': None,
        'direction': 'in',
        'documentation': {'description': 'Input array of floats'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array_2',
        'is_buffer': True,
        'is_string': False,
        'use_array': False,
        'use_list': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array_2',
        'name': 'inputArray2',
        'numpy': False,
        'python_api_converter_name': 'convert_to_nitclk_session_num_list',
        'python_name': 'input_array_2',
        'python_name_with_default': 'input_array_2=None',
        'python_name_with_doc_default': 'input_array_2=None',
        'python_type': 'float',
        'size': {'mechanism': 'len', 'value': 'inputArraySize2'},
        'type': 'ViReal64',
        'use_in_python_api': True,
    },
    {  # 30
        'ctypes_method_call_snippet': 'input_array_3_ctype',
        'ctypes_type': 'ViReal64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
        'ctypes_variable_name': 'input_array_3_ctype',
        'default_value': None,
        'direction': 'in',
        'documentation': {'description': 'Input array of floats'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array_3',
        'is_buffer': True,
        'is_string': False,
        'use_array': True,
        'use_list': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array_3',
        'name': 'inputArray3',
        'numpy': False,
        'python_api_converter_name': 'convert_to_nitclk_session_num_list',
        'python_name': 'input_array_3',
        'python_name_with_default': 'input_array_3=None',
        'python_name_with_doc_default': 'input_array_3=None',
        'python_type': 'float',
        'size': {'mechanism': 'len', 'value': 'inputArraySize3'},
        'type': 'ViReal64',
        'use_in_python_api': True,
    },
    {  # 31
        'ctypes_method_call_snippet': 'input_array_3_ctype',
        'ctypes_type': 'custom_struct',
        'ctypes_type_library_call': 'ctypes.POINTER(custom_struct)',
        'ctypes_variable_name': 'input_array_4_ctype',
        'default_value': None,
        'direction': 'in',
        'documentation': {'description': 'Input array of floats'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array_4',
        'is_buffer': True,
        'is_string': False,
        'use_array': False,
        'use_list': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array_3',
        'name': 'inputArray4',
        'numpy': False,
        'python_api_converter_name': 'convert_to_nitclk_session_num_list',
        'python_name': 'input_array_4',
        'python_name_with_default': 'input_array_4=None',
        'python_name_with_doc_default': 'input_array_4=None',
        'python_type': 'float',
        'size': {'mechanism': 'len', 'value': 'inputArraySize4'},
        'type': 'ViReal64',
        'use_in_python_api': True,
    },
    {  # 32
        'ctypes_method_call_snippet': 'input_array_3_ctype',
        'ctypes_type': 'custom_struct',
        'ctypes_type_library_call': 'ctypes.POINTER(custom_struct)',
        'ctypes_variable_name': 'input_array_4_ctype',
        'default_value': None,
        'direction': 'in',
        'documentation': {'description': 'Input array of floats'},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'input_array_4',
        'is_buffer': True,
        'is_string': False,
        'use_array': False,
        'use_list': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'input_array_3',
        'name': 'inputArray4',
        'numpy': False,
        'python_api_converter_name': 'convert_to_nitclk_session_num_list',
        'python_name': 'input_array_4',
        'python_name_with_default': 'input_array_4=None',
        'python_name_with_doc_default': 'input_array_4=None',
        'python_type': 'float',
        'size': {'mechanism': 'len', 'value': 'inputArraySize4'},
        'type': 'ViReal64',
        'use_in_python_api': True,
    },
    {  # 33
        'ctypes_method_call_snippet': 'a_string_enum_ctype',
        'ctypes_type': 'ViString',
        'ctypes_type_library_call': 'ViString',
        'ctypes_variable_name': 'a_string_enum_ctype',
        'direction': 'in',
        'documentation': {'description': 'An input string-valued enum.'},
        'enum': 'Color',
        'grpc_enum': 'Color',
        'grpc_name': 'a_string_enum',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'a_string_enum',
        'name': 'aStringEnum',
        'numpy': False,
        'python_name': 'a_string_enum',
        'python_name_with_default': 'a_string_enum',
        'python_name_with_doc_default': 'a_string_enum',
        'python_type': 'enums.Color',
        'size': {'mechanism': 'len', 'value': 'a_string_enum'},
        'type': 'ViString',
        'use_in_python_api': True,
    },
    {  # 34
        'ctypes_method_call_snippet': 'indices_ctype',
        'ctypes_type': 'ViConstString',
        'ctypes_type_library_call': 'ViConstString',
        'ctypes_variable_name': 'indices_ctype',
        'direction': 'in',
        'documentation': {
            'description': 'Specifies a list of indices for the channels in the session.'
        },
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'indices',
        'is_buffer': False,
        'is_string': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'indices',
        'name': 'indices',
        'numpy': False,
        'original_type': 'ViChar[]',
        'python_api_converter_name': 'convert_repeated_capabilities_without_prefix',
        'python_name': 'indices',
        'python_name_with_default': 'indices',
        'python_name_with_doc_default': 'indices',
        'python_type': 'str',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViConstString',
        'use_in_python_api': True,
    },
    {  # 35
        'ctypes_method_call_snippet': 'an_array_ctype',
        'ctypes_type': 'ViInt8',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt8)',
        'ctypes_variable_name': 'an_array_ctype',
        'direction': 'out',
        'documentation': {'description': 'Contains an array of enums, stored as 8 bit integers under the hood '},
        'enum': None,
        'grpc_enum': None,
        'grpc_name': 'a_grpc_array',
        'is_buffer': True,
        'use_array': False,
        'use_list': True,
        'is_string': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'interpreter_method_call_snippet': 'an_array',
        'name': 'anArray',
        'python_api_converter_name': 'convert_to_bytes',
        'python_name': 'an_array',
        'python_name_with_default': 'an_array',
        'python_name_with_doc_default': 'an_array',
        'python_type': 'int',
        'size': {'mechanism': 'passed-in', 'value': 'numberOfElements'},
        'type': 'ViInt8',
        'numpy': False,
        'use_in_python_api': True,
    },
]


def test_get_library_interpreter_method_return_snippet_vi():
    param = [parameters_for_testing[0]]
    assert get_library_interpreter_method_return_snippet(param, config_for_testing) == 'return'


def test_get_library_interpreter_method_return_snippet_int():
    param = [parameters_for_testing[1]]
    assert get_library_interpreter_method_return_snippet(param, config_for_testing) == 'return int(output_ctype.value)'


def test_get_library_interpreter_method_return_snippet_string():
    param = [parameters_for_testing[2]]
    assert get_library_interpreter_method_return_snippet(param, config_for_testing) == 'return error_message_ctype.value.decode(self._encoding)'


def test_get_library_interpreter_method_return_snippet_custom_type():
    param = [parameters_for_testing[3]]
    assert get_library_interpreter_method_return_snippet(param, config_for_testing) == 'return [custom_struct.CustomStruct(array_out_ctype[i]) for i in range(self.get_array_size_for_python_code())]'


def test_get_library_interpreter_method_return_snippet_enum():
    param = [parameters_for_testing[4], parameters_for_testing[5]]
    assert get_library_interpreter_method_return_snippet(param, config_for_testing) == 'return [enums.Turtle(an_array_ctype[i]) for i in range(number_of_elements_ctype.value)]'


def test_get_library_interpreter_method_return_snippet_into():
    param = [parameters_for_testing[4], parameters_for_testing[7]]
    assert get_library_interpreter_method_return_snippet(param, config_for_testing, use_numpy_array=True) == 'return'


def test_get_grpc_interpreter_method_return_snippet_vi():
    param = [parameters_for_testing[0]]
    assert get_grpc_interpreter_method_return_snippet(param, config_for_testing) == 'return'


def test_get_grpc_interpreter_method_return_snippet_int():
    param = [parameters_for_testing[1]]
    assert get_grpc_interpreter_method_return_snippet(param, config_for_testing) == 'return response.output'


def test_get_grpc_interpreter_method_return_snippet_string():
    param = [parameters_for_testing[2]]
    assert get_grpc_interpreter_method_return_snippet(param, config_for_testing) == 'return response.error_message'


def test_get_grpc_interpreter_method_return_snippet_custom_type():
    param = [parameters_for_testing[3]]
    assert get_grpc_interpreter_method_return_snippet(param, config_for_testing) == 'return [custom_struct.CustomStruct(x) for x in response.array_out]'


def test_get_grpc_interpreter_method_return_snippet_enum():
    param = [parameters_for_testing[4], parameters_for_testing[5]]
    assert get_grpc_interpreter_method_return_snippet(param, config_for_testing) == 'return [enums.Turtle(x) for x in response.an_array_raw]'


def test_get_grpc_interpreter_method_return_snippet_bytes():
    param = [parameters_for_testing[35]]
    assert get_grpc_interpreter_method_return_snippet(param, config_for_testing) == 'return response.a_grpc_array'


def test_get_session_method_return_snippet():
    param = [dict(parameters_for_testing[14])]
    param[0]['direction'] = 'out'
    assert get_session_method_return_snippet(param, config_for_testing) == 'return _converters.timedelta_converter_seconds_real64(timeout)'


def test_get_session_method_return_snippet_non_numpy():
    param = [parameters_for_testing[4], parameters_for_testing[7]]
    assert get_session_method_return_snippet(param, config_for_testing) == 'return output'


def test_get_session_method_return_snippet_numpy():
    param = [parameters_for_testing[4], parameters_for_testing[7]]
    assert get_session_method_return_snippet(param, config_for_testing, use_numpy_array=True) == 'return'


def test_get_enum_type_check_snippet():
    param = parameters_for_testing[6]
    assert get_enum_type_check_snippet(param, 0) == "if type(an_int_enum) is not enums.Turtle:\nraise TypeError('Parameter an_int_enum must be of type ' + str(enums.Turtle))"


def test_get_buffer_parameters_for_size_parameter_none():
    params = _get_buffer_parameters_for_size_parameter(parameters_for_testing[0], parameters_for_testing)
    assert len(params) == 0


def test_get_buffer_parameters_for_size_parameter():
    params = _get_buffer_parameters_for_size_parameter(parameters_for_testing[4], parameters_for_testing)
    assert params[0] == parameters_for_testing[5]


def test_get_ctype_variable_declaration_snippet_case_c010():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[15], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010"]


def test_get_ctype_variable_declaration_snippet_case_c020():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[16], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_ctype = ctypes.create_string_buffer(a_string.encode(self._encoding))  # case C020"]


def test_get_ctype_variable_declaration_snippet_case_c030():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[33], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_enum_ctype = ctypes.create_string_buffer(a_string_enum.value.encode(self._encoding))  # case C030"]


def test_get_ctype_variable_declaration_snippet_case_c050():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[13], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_ctype = None  # case C050"]


def test_get_ctype_variable_declaration_snippet_case_c060():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[13], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_ctype = (_visatype.ViChar * string_size_ctype.value)()  # case C060"]


def test_get_ctype_variable_declaration_snippet_case_c070():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[19], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_2_ctype = (_visatype.ViChar * 256)()  # case C070"]


def test_get_ctype_variable_declaration_snippet_case_c080():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[20], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_3_ctype = (_visatype.ViChar * string_size)()  # case C080"]


def test_get_ctype_variable_declaration_snippet_case_c090():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[21], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_twist_ctype = None  # case C090"]


def test_get_ctype_variable_declaration_snippet_case_c100():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[21], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_string_twist_ctype = (_visatype.ViChar * output_twist_ctype.value)()  # case C100"]


def test_get_ctype_variable_declaration_snippet_case_s110():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[0], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["vi_ctype = _visatype.ViSession(self._vi)  # case S110"]


def test_get_ctype_variable_declaration_snippet_case_s120():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[8], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["number_of_elements_python_code_ctype = _visatype.ViInt32(self.get_array_size_for_python_code())  # case S120"]


def test_get_ctype_variable_declaration_snippet_case_s130():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[6], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["an_int_enum_ctype = _visatype.ViInt16(an_int_enum.value)  # case S130"]


def test_get_ctype_variable_declaration_snippet_case_s150():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[9], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["input_ctype = _visatype.ViInt16(input)  # case S150"]


def test_get_ctype_variable_declaration_snippet_case_s160():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[11], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert actual == ["input_array_size_ctype = _visatype.ViInt32(0 if input_array is None else len(input_array))  # case S160"]


def test_get_ctype_variable_declaration_snippet_case_s170():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[12], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["string_size_ctype = _visatype.ViInt32()  # case S170"]


def test_get_ctype_variable_declaration_snippet_case_s180():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[12], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    assert snippet == ["string_size_ctype = _visatype.ViInt32(error_code)  # case S180"]


def test_get_ctype_variable_declaration_snippet_case_s2190():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[23], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["string_size_twist_ctype = _visatype.ViInt32(0)  # case S190"]


def test_get_ctype_variable_declaration_snippet_case_s200():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[23], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    assert snippet == ["string_size_twist_ctype = _visatype.ViInt32(output_twist_ctype.value)  # case S200"]


def test_get_ctype_variable_declaration_snippet_case_s210():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[4], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["number_of_elements_ctype = _visatype.ViInt32(number_of_elements)  # case S210"]


def test_get_ctype_variable_declaration_snippet_case_s220():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[1], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["output_ctype = _visatype.ViInt64()  # case S220"]


def test_get_ctype_variable_declaration_snippet_case_b510():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[7], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=True)
    assert snippet == ["output_ctype = _get_ctypes_pointer_for_buffer(value=output)  # case B510"]


def test_get_ctype_variable_declaration_snippet_case_b540():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[17], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["array_in_ctype = _get_ctypes_pointer_for_buffer([custom_struct.custom_struct(c) for c in array_in], library_type=custom_struct.custom_struct)  # case B540"]


def test_get_ctype_variable_declaration_snippet_case_b550_array():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[10], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    expected = [
        'input_array_array = _convert_to_array(value=input_array, array_type="d")  # case B550',
        'input_array_ctype = _get_ctypes_pointer_for_buffer(value=input_array_array, library_type=_visatype.ViReal64)  # case B550',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b550_list():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[28], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == ["input_array_2_ctype = _get_ctypes_pointer_for_buffer(value=input_array_2, library_type=_visatype.ViReal64)  # case B550"]


def test_get_ctype_variable_declaration_snippet_case_b560():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[3], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    expected = [
        'array_out_size = self.get_array_size_for_python_code()  # case B560',
        'array_out_ctype = _get_ctypes_pointer_for_buffer(library_type=custom_struct.custom_struct, size=array_out_size)  # case B560',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b570():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[18], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    expected = [
        'an_int_size = 256  # case B570',
        'an_int_array = array.array("h", [0] * an_int_size)  # case B570',
        'an_int_ctype = _get_ctypes_pointer_for_buffer(value=an_int_array, library_type=_visatype.ViInt16)  # case B570',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b580_array():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[24], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_buffer_array_ctype = None  # case B580"]


def test_get_ctype_variable_declaration_snippet_case_b590_array():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[24], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    expected = [
        'a_buffer_array_size = string_size_ctype.value  # case B590',
        'a_buffer_array_array = array.array("l", [0] * a_buffer_array_size)  # case B590',
        'a_buffer_array_ctype = _get_ctypes_pointer_for_buffer(value=a_buffer_array_array, library_type=_visatype.ViInt32)  # case B590',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b580_list():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[25], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_buffer_list_ctype = None  # case B580"]


def test_get_ctype_variable_declaration_snippet_case_b590_list():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[25], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    expected = [
        'a_buffer_list_size = string_size_ctype.value  # case B590',
        'a_buffer_list_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=a_buffer_list_size)  # case B590',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b600():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[7], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    expected = [
        'output_size = number_of_elements  # case B600',
        'output_array = array.array("q", [0] * output_size)  # case B600',
        'output_ctype = _get_ctypes_pointer_for_buffer(value=output_array, library_type=_visatype.ViInt64)  # case B600',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b610_array():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[26], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_buffer_twist_array_ctype = None  # case B610"]


def test_get_ctype_variable_declaration_snippet_case_b620_array():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[26], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    expected = [
        'a_buffer_twist_array_size = output_twist_ctype.value  # case B620',
        'a_buffer_twist_array_array = array.array("l", [0] * a_buffer_twist_array_size)  # case B620',
        'a_buffer_twist_array_ctype = _get_ctypes_pointer_for_buffer(value=a_buffer_twist_array_array, library_type=_visatype.ViInt32)  # case B620',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_case_b610_list():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[27], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == ["a_buffer_twist_list_ctype = None  # case B610"]


def test_get_ctype_variable_declaration_snippet_case_b620_list():
    actual = get_ctype_variable_declaration_snippet(parameters_for_testing[27], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    expected = [
        'a_buffer_twist_list_size = output_twist_ctype.value  # case B620',
        'a_buffer_twist_list_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=a_buffer_twist_list_size)  # case B620',
    ]
    assert len(actual) == len(expected)
    for i in range(max(len(actual), len(expected))):
        assert actual[i] == expected[i]


def test_get_ctype_variable_declaration_snippet_bad_ivi_dance_step():
    try:
        get_ctype_variable_declaration_snippet(parameters_for_testing[12], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
        assert False
    except AssertionError:
        pass


# TODO(marcoskirsch): unit tests for reamining cases of get_ctype_variable_declaration_snippet(): parameter is a buffer.


def test_get_enum_value_snippet():
    assert get_enum_value_snippet(None) == 'None'
    assert get_enum_value_snippet(True) == 'True'
    assert get_enum_value_snippet(0) == '0'
    assert get_enum_value_snippet('True') == "'True'"
    assert get_enum_value_snippet('0') == "'0'"
