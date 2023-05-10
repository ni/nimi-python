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


def get_parameter_size_check_snippets(parameters):
    '''Returns python snippets to check that parameter sizes are correct.'''
    snippets = []

    for parameter in parameters:
        if parameter['is_string'] or parameter['is_buffer']:
            continue
        else:
            snippets.extend(_get_parameter_size_check_snippets(parameter, parameters))

    return snippets


def _get_parameter_size_check_snippets(parameter, parameters):
    snippets = []

    corresponding_buffer_parameters = _get_buffer_parameters_for_size_parameter(parameter, parameters)
    if not corresponding_buffer_parameters:
        return snippets

    if parameter['direction'] == 'in':
        if parameter['is_session_handle'] or parameter['size']['mechanism'] == 'python-code' or parameter['enum']:
            pass
        elif corresponding_buffer_parameters[0]['direction'] == 'in':  # We are only looking at the first one to see if it is 'in'. Assumes all are the same here, assert below if not
            # Parameter denotes the size of another (the "corresponding") parameter.
            for i in range(1, len(corresponding_buffer_parameters)):
                snippets.append('if {0} is not None and len({0}) != len({1}):  # case S160'.format(corresponding_buffer_parameters[i]['python_name'], corresponding_buffer_parameters[0]['python_name']))
                snippets.append('    raise ValueError("Length of {0} and {1} parameters do not match.")  # case S160'.format(corresponding_buffer_parameters[i]['python_name'], corresponding_buffer_parameters[0]['python_name']))

    return snippets


def get_dictionary_snippet(d, indent=4):
    '''Returns a formatted dictionary'''
    d_str = pprint.pformat(d)
    d_lines = d_str.splitlines()
    return ('\n' + (' ' * indent)).join(d_lines)


def get_enum_value_snippet(value):
    '''Returns value formatted into string, surrounding it with single quotes if it is of str type'''
    return ("'{}'" if type(value) is str else "{}").format(value)

