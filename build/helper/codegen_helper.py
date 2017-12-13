from .metadata_filters import filter_parameters
from .metadata_find import find_custom_type
from .metadata_find import find_size_parameter
from .parameter_usage_options import ParameterUsageOptions
from enum import Enum
import pprint

pp = pprint.PrettyPrinter(indent=4)

_parameterUsageOptionsSnippet = {}

_parameterUsageOptionsSnippet[ParameterUsageOptions.SESSION_METHOD_DECLARATION] = {
    'skip_self': False,
    'name_to_use': 'python_name_with_default',
}
_parameterUsageOptionsSnippet[ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION] = {
    'skip_self': False,
    'name_to_use': 'python_name_with_default',
}
_parameterUsageOptionsSnippet[ParameterUsageOptions.SESSION_METHOD_CALL] = {
    'skip_self': True,
    'name_to_use': 'python_name',
}
_parameterUsageOptionsSnippet[ParameterUsageOptions.DOCUMENTATION_SESSION_METHOD] = {
    'skip_self': True,
    'name_to_use': 'python_name_with_doc_default',
}
_parameterUsageOptionsSnippet[ParameterUsageOptions.CTYPES_CALL] = {
    'skip_self': True,
    'name_to_use': 'python_name',
}
_parameterUsageOptionsSnippet[ParameterUsageOptions.LIBRARY_METHOD_CALL] = {
    'skip_self': True,
    'name_to_use': 'library_method_call_snippet',
}
_parameterUsageOptionsSnippet[ParameterUsageOptions.CTYPES_ARGTYPES] = {
    'skip_self': True,
    'name_to_use': 'ctypes_type_library_call',
}
_parameterUsageOptionsSnippet[ParameterUsageOptions.LIBRARY_METHOD_DECLARATION] = {
    'skip_self': False,
    'name_to_use': 'python_name',
}
# Only used for filtering
#   ParameterUsageOptions.INPUT_PARAMETERS
#   ParameterUsageOptions.OUTPUT_PARAMETERS
#   ParameterUsageOptions.IVI_DANCE_PARAMETER
#   ParameterUsageOptions.LEN_PARAMETER
#   ParameterUsageOptions.INPUT_ENUM_PARAMETERS


# Functions that return snippets that can be placed directly in the templates.
def get_params_snippet(function, parameter_usage_options):
    '''get_params_snippet

    Get a parameter list snippet based on parameter_usage_options.
    '''
    if type(parameter_usage_options) is not ParameterUsageOptions:
        raise TypeError('parameter_usage_options must be of type ' + str(ParameterUsageOptions))

    options_to_use = _parameterUsageOptionsSnippet[parameter_usage_options]

    parameters_to_use = filter_parameters(function, parameter_usage_options)

    snippets = []
    if not options_to_use['skip_self']:
        snippets.append('self')

    # Render based on options
    for p in parameters_to_use:
            snippets.append(p[options_to_use['name_to_use']])
    return ', '.join(snippets)


def _get_output_param_return_snippet(output_parameter, parameters, config):
    '''Returns the snippet for returning a single output parameter from a Session method, i.e. "reading_ctype.value"'''
    assert output_parameter['direction'] == 'out', 'Expected parameter {0} (a.k.a. {1}) to have direction out'.format(output_parameter['name'], output_parameter['python_name'])
    return_type_snippet = ''

    # Custom types (I.e. inherit from ctypes.Structure) don't need a .value but do need a module name
    val_suffix = '.value'
    module_name = ''
    custom_type = find_custom_type(output_parameter, config)
    if custom_type is not None:
        val_suffix = ''
        module_name = custom_type['file_name'] + '.'

    if output_parameter['enum'] is not None:
        return_type_snippet = 'enums.' + output_parameter['enum'] + '('
    else:
        return_type_snippet = module_name + output_parameter['python_type'] + '('

    if output_parameter['is_buffer']:
        if output_parameter['type'] == 'ViChar':
            # 'self._encoding' is a variable on the session object
            snippet = output_parameter['ctypes_variable_name'] + '.value.decode(self._encoding)'
        else:
            if output_parameter['size']['mechanism'] == 'fixed':
                size = str(output_parameter['size']['value'])
            elif output_parameter['size']['mechanism'] == 'python-code':
                size = output_parameter['size']['value']
            else:
                size_parameter = find_size_parameter(output_parameter, parameters)
                size = size_parameter['ctypes_variable_name'] + '.value'

            snippet = '[' + return_type_snippet + output_parameter['ctypes_variable_name'] + '[i]) for i in range(' + size + ')]'
    else:
        snippet = return_type_snippet + output_parameter['ctypes_variable_name'] + val_suffix + ')'

    return snippet


# TODO(marcoskirsch): Retrofit to call filter_parameters(function, parameter_usage_options)
def get_method_return_snippet(parameters, config, use_numpy_array=False):
    '''Returns a string suitable to use as the return argument of a Session method, i.e. "return reading_ctype.value"'''
    snippets = []
    for x in parameters:
        if x['direction'] == 'out' or x['size']['mechanism'] == 'ivi-dance':
            if x['numpy'] is False or use_numpy_array is False:
                snippets.append(_get_output_param_return_snippet(x, parameters, config))
    return ('return ' + ', '.join(snippets)).strip()


def get_enum_type_check_snippet(parameter, indent):
    '''Returns python snippet to check that the type of a parameter is what is expected'''
    assert parameter['enum'] is not None, pp.pformat(parameter)
    assert parameter['direction'] == 'in', pp.pformat(parameter)
    enum_check = 'if type(' + parameter['python_name'] + ') is not ' + parameter['python_type'] + ':\n'
    enum_check += (' ' * indent) + 'raise TypeError(\'Parameter mode must be of type \' + str(' + parameter['python_type'] + '))'
    return enum_check


def _get_buffer_parameter_for_size_parameter(parameter, parameters):
    '''If parameter represents the size of another parameter in the C API, returns that other parameter. Otherwise None.'''
    for p in parameters:
        if p['is_buffer'] and p['size']['value'] == parameter['name']:
            return p
    return None


class IviDanceStep(Enum):
    NOT_APPLICABLE = 0
    'Use this when the function in question does not do the IVI dance.'

    QUERY_SIZE = 1
    'Step 1: Call into the driver in order to query the size of the buffer to be allocated.'

    GET_DATA = 2
    'Step 2: Allocate the buffer, call back into the driver to get the actual data.'


def get_ctype_variable_declaration_snippet(parameter, parameters, ivi_dance_step, config, use_numpy_array=False):
    '''Returns python snippet that declares and initializes a ctypes variable for the parameter that can be passed to the Library.

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
        module_name = 'visatype'

    if parameter['is_buffer'] is True:
        definition = _get_ctype_variable_definition_snippet_for_buffers(parameter, parameters, ivi_dance_step, use_numpy_array, custom_type, module_name)
    else:
        definition = _get_ctype_variable_definition_snippet_for_scalar(parameter, parameters, ivi_dance_step, module_name)

    return parameter['ctypes_variable_name'] + ' = ' + definition


def _get_ctype_variable_definition_snippet_for_scalar(parameter, parameters, ivi_dance_step, module_name):
    '''These are the different cases for initializing the ctype variable for scalars:

        1. Input session handle:                                                visatype.ViSession(self._vi)
      0.0. Input is size of buffer with mechanism is python-code:               visatype.ViInt32(<custom python code>)
       10. Input enum:                                                          visatype.ViInt32(parameter_name.value)
        9. Input scalar:                                                        visatype.ViInt32(parameter_name)
        6. Input is size of input buffer:                                       visatype.ViInt32(0 if list is None else len(list))
        7. Input is size of output buffer with mechanism ivi-dance, QUERY_SIZE: visatype.ViInt32()
      7.5. Input is size of output buffer with mechanism ivi-dance, GET_DATA:   visatype.ViInt32(error_code)
        8. Input is size of output buffer with mechanism passed-in:             visatype.ViInt32(buffer_size)
       14. Output scalar or enum:                                               visatype.ViInt32()
    '''

    assert parameter['is_buffer'] is False
    assert parameter['numpy'] is False
    corresponding_buffer_parameter = _get_buffer_parameter_for_size_parameter(parameter, parameters)

    if parameter['direction'] == 'in':
        if parameter['is_session_handle'] is True:
            definition = '{0}.{1}(self._{2})  # case 1'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
        elif parameter['size']['mechanism'] == 'python-code':
            definition = '{0}.{1}({2})  # case 0.0'.format(module_name, parameter['ctypes_type'], parameter['size']['value'])
        elif parameter['enum'] is not None:
            definition = '{0}.{1}({2}.value)  # case 10'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
        elif corresponding_buffer_parameter is None:
            definition = '{0}.{1}({2})  # case 9'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
        elif corresponding_buffer_parameter['direction'] == 'in':
            # Parameter denotes the size of another (the "corresponding") parameter.
            definition = '{0}.{1}(0 if {2} is None else len({2}))  # case 6'.format(module_name, parameter['ctypes_type'], corresponding_buffer_parameter['python_name'])
        else:
            assert corresponding_buffer_parameter['direction'] == 'out'
            if corresponding_buffer_parameter['size']['mechanism'] == 'ivi-dance':
                if ivi_dance_step == IviDanceStep.QUERY_SIZE:
                    definition = '{0}.{1}()  # case 7'.format(module_name, parameter['ctypes_type'])
                elif ivi_dance_step == IviDanceStep.GET_DATA:
                    definition = '{0}.{1}(error_code)  # case 7.5'.format(module_name, parameter['ctypes_type'])
                else:
                    assert False, "ivi_dance_step {0} not valid for parameter {1} with ['size']['mechanism'] == 'ivi-dance'".format(ivi_dance_step, parameter['name'])
            else:
                assert corresponding_buffer_parameter['size']['mechanism'] != 'fixed-size', 'mechanism fixed-size makes no sense here! Check metadata'
                definition = '{0}.{1}({2})  # case 8'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
    else:
        assert parameter['direction'] == 'out'
        definition = '{0}.{1}()  # case 14'.format(module_name, parameter['ctypes_type'])

    return definition


def _get_ctype_variable_definition_snippet_for_buffers(parameter, parameters, ivi_dance_step, use_numpy_array, custom_type, module_name):
    '''These are the different cases for initializing the ctype variable for buffers:

        2. Input repeated capability:                                           ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))
        3. Input string:                                                        ctypes.create_string_buffer(parameter_name.encode(self._encoding))
        5. Input buffer (custom type):                                          (custom_struct * len(list))(*[custom_struct(l) for l in list])
      5.5. Input buffer (numpy):                                                Not yet implemented
        4. Input buffer of simple types:                                        None if list is None else (visatype.ViInt32 * len(list))(*list)
     13.5. Output buffer with mechanism passed-in (numpy):                      numpy.ctypeslib.as_ctypes(waveform)
      0.4. Output buffer with mechanism python-code:                            (visatype.ViInt32 * (<custom python code>))()
       11. Output buffer with mechanism fixed-size:                             visatype.ViInt32 * 256
       12. Output buffer with mechanism ivi-dance, QUERY_SIZE:                  None
     12.5. Output buffer with mechanism ivi-dance, GET_DATA:                    (visatype.ViInt32 * buffer_size_ctype.value)()
       13. Output buffer with mechanism passed-in:                              (visatype.ViInt32 * buffer_size)()
    '''

    assert parameter['is_buffer'] is True

    if parameter['direction'] == 'in':
        if parameter['is_repeated_capability'] is True:
            definition = 'ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2'
        elif parameter['type'] == 'ViChar':
            definition = 'ctypes.create_string_buffer({0}.encode(self._encoding))  # case 3'.format(parameter['python_name'])
        elif custom_type is not None:
            definition = '({0}.{1} * len({2}))(*[{0}.{1}(c) for c in {2}])  # case 5'.format(module_name, parameter['ctypes_type'], parameter['python_name'], parameter['python_name'])
        elif parameter['numpy'] is True and use_numpy_array is True:
            assert False, "Yet to implement numpy.array as input parameter.  # case 5.5"
        else:
            definition = 'None if {2} is None else ({0}.{1} * len({2}))(*{2})  # case 4'.format(module_name, parameter['ctypes_type'], parameter['python_name'], parameter['python_name'])
    else:
        assert parameter['direction'] == 'out'
        assert 'size' in parameter, "Parameter {0} is output buffer but metadata doesn't define its 'size'".format(parameter['name'])
        if parameter['numpy'] is True and use_numpy_array is True:
            definition = '{0}.ctypeslib.as_ctypes({1})  # case 13.5'.format(module_name, parameter['python_name'])
        elif parameter['size']['mechanism'] == 'python-code':
            definition = '({0}.{1} * {2})()  # case 0.4'.format(module_name, parameter['ctypes_type'], parameter['size']['value'])
        elif parameter['size']['mechanism'] == 'fixed':
            assert parameter['size']['value'] != 1, "Parameter {0} has 'direction':'out' and 'size':{1}... seems wrong. Check your metadata, maybe you forgot to specify?".format(parameter['name'], parameter['size'])
            definition = '({0}.{1} * {2})()  # case 11'.format(module_name, parameter['ctypes_type'], parameter['size']['value'])
        elif parameter['size']['mechanism'] == 'ivi-dance':
            if ivi_dance_step == IviDanceStep.QUERY_SIZE:
                definition = 'None  # case 12'
            elif ivi_dance_step == IviDanceStep.GET_DATA:
                size_parameter = find_size_parameter(parameter, parameters)
                definition = '({0}.{1} * {2}.value)()  # case 12.5'.format(module_name, parameter['ctypes_type'], size_parameter['ctypes_variable_name'])
            else:
                assert False, "ivi_dance_step {0} not valid for parameter {1} with ['size']['mechanism'] == 'ivi-dance'".format(ivi_dance_step, parameter['name'])
        elif parameter['size']['mechanism'] == 'passed-in':
            size_parameter = find_size_parameter(parameter, parameters)
            definition = '({0}.{1} * {2})()  # case 13'.format(module_name, parameter['ctypes_type'], size_parameter['python_name'])
        else:
            assert False, "Invalid mechanism for parameters with 'direction':'out': " + str(parameter)

    return definition


def get_dictionary_snippet(d, indent=4):
    '''Returns a formatted dictionary'''
    d_str = pprint.pformat(d)
    d_lines = d_str.splitlines()
    return ('\n' + (' ' * indent)).join(d_lines)


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
    {
        'ctypes_type': 'ViSession',
        'ctypes_type_library_call': 'ViSession',
        'ctypes_variable_name': 'vi_ctype',
        'direction': 'in',
        'documentation': {'description': 'Identifies a particular instrument session.'},
        'enum': None,
        'is_buffer': False,
        'is_repeated_capability': False,
        'is_session_handle': True,
        'library_method_call_snippet': 'vi_ctype',
        'name': 'vi',
        'python_name': 'vi',
        'python_name_with_default': 'vi',
        'python_name_with_doc_default': 'vi',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViSession',
        'numpy': False,
    },
    {
        'ctypes_type': 'ViInt64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt64)',
        'ctypes_variable_name': 'output_ctype',
        'direction': 'out',
        'documentation': {'description': 'A big number on its way out.'},
        'enum': None,
        'is_buffer': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'library_method_call_snippet': 'ctypes.pointer(output_ctype)',
        'name': 'output',
        'python_name': 'output',
        'python_name_with_default': 'output',
        'python_name_with_doc_default': 'output',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt64',
        'numpy': False,
    },
    {
        'ctypes_type': 'ViChar',
        'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
        'ctypes_variable_name': 'error_message_ctype',
        'direction': 'out',
        'documentation': {'description': 'The error information formatted into a string.'},
        'enum': None,
        'is_buffer': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'library_method_call_snippet': 'error_message_ctype',
        'name': 'errorMessage',
        'python_name': 'error_message',
        'python_name_with_default': 'error_message',
        'python_name_with_doc_default': 'error_message',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 256},
        'type': 'ViChar',
        'numpy': False,
    },
    {
        'ctypes_type': 'custom_struct',
        'ctypes_type_library_call': 'ctypes.POINTER(custom_struct)',
        'ctypes_variable_name': 'array_out_ctype',
        'direction': 'out',
        'documentation': {'description': 'Array of custom type using python-code size mechanism'},
        'enum': None,
        'is_buffer': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'library_method_call_snippet': 'array_out_ctype',
        'name': 'arrayOut',
        'original_type': 'custom_struct[]',
        'python_name': 'array_out',
        'python_name_with_default': 'array_out',
        'python_name_with_doc_default': 'array_out',
        'python_type': 'CustomStruct',
        'size': {'mechanism': 'python-code', 'value': 'self.get_array_size_for_python_code()'},
        'type': 'custom_struct',
        'numpy': False,
    },
    {
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ViInt32',
        'ctypes_variable_name': 'number_of_elements_ctype',
        'direction': 'in',
        'documentation': {'description': 'Number of elements in the array.'},
        'enum': None,
        'is_buffer': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'library_method_call_snippet': 'number_of_elements_ctype',
        'name': 'numberOfElements',
        'python_name': 'number_of_elements',
        'python_name_with_default': 'number_of_elements',
        'python_name_with_doc_default': 'number_of_elements',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt32',
        'numpy': False,
    },
    {
        'ctypes_type': 'ViInt16',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt16)',
        'ctypes_variable_name': 'an_array_ctype',
        'direction': 'out',
        'documentation': {'description': 'Contains an array of enums, stored as 16 bit integers under the hood '},
        'enum': 'Turtle',
        'is_buffer': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'library_method_call_snippet': 'an_array_ctype',
        'name': 'anArray',
        'python_name': 'an_array',
        'python_name_with_default': 'an_array',
        'python_name_with_doc_default': 'an_array',
        'python_type': 'enums.Turtle',
        'size': {'mechanism': 'passed-in', 'value': 'numberOfElements'},
        'type': 'ViInt16',
        'numpy': False,
    },
    {
        'ctypes_type': 'ViInt16',
        'ctypes_type_library_call': 'ViInt16',
        'ctypes_variable_name': 'an_int_enum_ctype',
        'direction': 'in',
        'documentation': {
            'description': 'Indicates a ninja turtle',
            'table_body': [['0', 'Leonardo'], ['1', 'Donatello'], ['2', 'Raphael'], ['3', 'Mich elangelo']]
        },
        'enum': 'Turtle',
        'is_buffer': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'library_method_call_snippet': 'an_int_enum_ctype',
        'name': 'anIntEnum',
        'python_name': 'an_int_enum',
        'python_name_with_default': 'an_int_enum',
        'python_name_with_doc_default': 'an_int_enum',
        'python_type': 'enums.Turtle',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt16',
        'numpy': False,
    },
    {
        'ctypes_type': 'ViInt64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViInt64)',
        'ctypes_variable_name': 'output_ctype',
        'direction': 'out',
        'documentation': {'description': 'A big number on its way out.'},
        'enum': None,
        'is_buffer': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'library_method_call_snippet': 'ctypes.pointer(output_ctype)',
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
    },
    {
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ViInt32',
        'ctypes_variable_name': 'number_of_elements_python_code_ctype',
        'direction': 'in',
        'documentation': {'description': 'Number of elements in the array, determined via mechanism python-code.'},
        'enum': None,
        'is_buffer': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'library_method_call_snippet': 'number_of_elements_python_code_ctype',
        'name': 'numberOfElementsPythonCode',
        'numpy': False,
        'python_name': 'number_of_elements_python_code',
        'python_name_with_default': 'number_of_elements_python_code',
        'python_name_with_doc_default': 'number_of_elements_python_code',
        'python_type': 'int',
        'size': {'mechanism': 'python-code', 'value': 'self.get_array_size_for_python_code()'},
        'type': 'ViInt32'
    },
    {
        'ctypes_type': 'ViInt16',
        'ctypes_type_library_call': 'ViInt16',
        'ctypes_variable_name': 'input_ctype',
        'direction': 'in',
        'documentation': {'description': 'An input value.'},
        'enum': None,
        'is_buffer': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'library_method_call_snippet': 'input_ctype',
        'name': 'input',
        'numpy': False,
        'python_name': 'input',
        'python_name_with_default': 'input',
        'python_name_with_doc_default': 'input',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt16'
    },
    {
        'ctypes_type': 'ViReal64',
        'ctypes_type_library_call': 'ctypes.POINTER(ViReal64)',
        'ctypes_variable_name': 'input_array_ctype',
        'default_value': None,
        'direction': 'in',
        'documentation': {'description': 'Input array of floats'},
        'enum': None,
        'is_buffer': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'library_method_call_snippet': 'input_array_ctype',
        'name': 'inputArray',
        'numpy': False,
        'python_name': 'input_array',
        'python_name_with_default': 'input_array=None',
        'python_name_with_doc_default': 'input_array=None',
        'python_type': 'float',
        'size': {'mechanism': 'len', 'value': 'inputArraySize'},
        'type': 'ViReal64'
    },
    {
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ViInt32',
        'ctypes_variable_name': 'input_array_size_ctype',
        'direction': 'in',
        'documentation': {'description': 'Size of inputArray'},
        'enum': None,
        'is_buffer': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'library_method_call_snippet': 'input_array_size_ctype',
        'name': 'inputArraySize',
        'numpy': False,
        'python_name': 'input_array_size',
        'python_name_with_default': 'input_array_size',
        'python_name_with_doc_default': 'input_array_size',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt32'
    },
    {
        'ctypes_type': 'ViInt32',
        'ctypes_type_library_call': 'ViInt32',
        'ctypes_variable_name': 'string_size_ctype',
        'direction': 'in',
        'documentation': {'description': 'Number of bytes allocated for aString'},
        'enum': None,
        'is_buffer': False,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'library_method_call_snippet': 'string_size_ctype',
        'name': 'stringSize',
        'numpy': False,
        'python_name': 'string_size',
        'python_name_with_default': 'string_size',
        'python_name_with_doc_default': 'string_size',
        'python_type': 'int',
        'size': {'mechanism': 'fixed', 'value': 1},
        'type': 'ViInt32'
    },
    {
        'ctypes_type': 'ViChar',
        'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
        'ctypes_variable_name': 'a_string_ctype',
        'direction': 'out',
        'documentation': {'description': 'An IVI dance string.'},
        'enum': None,
        'is_buffer': True,
        'is_repeated_capability': False,
        'is_session_handle': False,
        'library_method_call_snippet': 'a_string_ctype',
        'name': 'aString',
        'numpy': False,
        'python_name': 'a_string',
        'python_name_with_default': 'a_string',
        'python_name_with_doc_default': 'a_string',
        'python_type': 'int',
        'size': {'mechanism': 'ivi-dance', 'value': 'stringSize'},
        'type': 'ViChar'
    },
]


def test_get_method_return_snippet_vi():
    param = [parameters_for_testing[0]]
    assert get_method_return_snippet(param, config_for_testing) == 'return'


def test_get_method_return_snippet_int():
    param = [parameters_for_testing[1]]
    assert get_method_return_snippet(param, config_for_testing) == 'return int(output_ctype.value)'


def test_get_method_return_snippet_string():
    param = [parameters_for_testing[2]]
    assert get_method_return_snippet(param, config_for_testing) == 'return error_message_ctype.value.decode(self._encoding)'


def test_get_method_return_snippet_custom_type():
    param = [parameters_for_testing[3]]
    assert get_method_return_snippet(param, config_for_testing) == 'return [custom_struct.CustomStruct(array_out_ctype[i]) for i in range(self.get_array_size_for_python_code())]'


def test_get_method_return_snippet_enum():
    param = [parameters_for_testing[4], parameters_for_testing[5]]
    assert get_method_return_snippet(param, config_for_testing) == 'return [enums.Turtle(an_array_ctype[i]) for i in range(number_of_elements_ctype.value)]'


def test_get_method_return_snippet_into():
    param = [parameters_for_testing[4], parameters_for_testing[7]]
    assert get_method_return_snippet(param, config_for_testing, use_numpy_array=True) == 'return'


def test_get_enum_type_check_snippet():
    param = parameters_for_testing[6]
    assert get_enum_type_check_snippet(param, 0) == "if type(an_int_enum) is not enums.Turtle:\nraise TypeError('Parameter mode must be of type ' + str(enums.Turtle))"


def test_get_buffer_parameter_for_size_parameter_none():
    param = _get_buffer_parameter_for_size_parameter(parameters_for_testing[0], parameters_for_testing)
    assert param is None


def test_get_buffer_parameter_for_size_parameter():
    param = _get_buffer_parameter_for_size_parameter(parameters_for_testing[4], parameters_for_testing)
    assert param == parameters_for_testing[5]


def test_get_ctype_variable_declaration_snippet_case_1():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[0], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == "vi_ctype = visatype.ViSession(self._vi)  # case 1"


def test_get_ctype_variable_declaration_snippet_case_0_0():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[8], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == "number_of_elements_python_code_ctype = visatype.ViInt32(self.get_array_size_for_python_code())  # case 0.0"


def test_get_ctype_variable_declaration_snippet_case_10():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[6], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == "an_int_enum_ctype = visatype.ViInt16(an_int_enum.value)  # case 10"


def test_get_ctype_variable_declaration_snippet_case_9():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[9], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == "input_ctype = visatype.ViInt16(input)  # case 9"


def test_get_ctype_variable_declaration_snippet_case_6():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[11], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == "input_array_size_ctype = visatype.ViInt32(0 if input_array is None else len(input_array))  # case 6"


def test_get_ctype_variable_declaration_snippet_case_7():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[12], parameters_for_testing, IviDanceStep.QUERY_SIZE, config_for_testing, use_numpy_array=False)
    assert snippet == "string_size_ctype = visatype.ViInt32()  # case 7"


def test_get_ctype_variable_declaration_snippet_case_7_5():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[12], parameters_for_testing, IviDanceStep.GET_DATA, config_for_testing, use_numpy_array=False)
    assert snippet == "string_size_ctype = visatype.ViInt32(error_code)  # case 7.5"


def test_get_ctype_variable_declaration_snippet_case_8():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[4], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == "number_of_elements_ctype = visatype.ViInt32(number_of_elements)  # case 8"


def test_get_ctype_variable_declaration_snippet_case_14():
    snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[1], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
    assert snippet == "output_ctype = visatype.ViInt64()  # case 14"


def test_get_ctype_variable_declaration_snippet_bad_ivi_dance_step():
    try:
        snippet = get_ctype_variable_declaration_snippet(parameters_for_testing[12], parameters_for_testing, IviDanceStep.NOT_APPLICABLE, config_for_testing, use_numpy_array=False)
        assert False
    except AssertionError:
        pass



