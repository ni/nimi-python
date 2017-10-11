from .metadata_filters import filter_ivi_dance_parameter
from .metadata_filters import filter_len_parameter
from .metadata_find import find_size_parameter
from enum import Enum
import pprint

pp = pprint.PrettyPrinter(indent=4)


# Functions that return snippets that can be placed directly in the templates.
class ParameterUsageOptions(Enum):
    '''Different usage options for parameter lists.'''

    SESSION_METHOD_DECLARATION = 1
    '''For declaring a method in Session'''
    SESSION_METHOD_CALL = 2
    '''For calling into a Session method.'''
    DOCUMENTATION_SESSION_METHOD = 3
    '''For documentation (rst) of Session methods'''
    CTYPES_CALL = 4
    '''For Library implementation calling into the DLL via ctypes'''
    LIBRARY_METHOD_CALL = 5
    '''For calling into a method in Library.'''
    CTYPES_ARGTYPES = 6
    '''For setting up the ctypes argument types'''
    LIBRARY_METHOD_DECLARATION = 7
    '''For declaring a method in Library'''


_parameterUsageOptions = {}

_parameterUsageOptions[ParameterUsageOptions.SESSION_METHOD_DECLARATION] = {
    'skip_self': False,
    'skip_session_handle': True,
    'skip_input_parameters': False,
    'skip_output_parameters': True,
    'skip_size_parameter': True,
    'reordered_for_default_values': True,
    'name_to_use': 'python_name_with_default',
    'skip_repeated_capability_parameter': True,
}
_parameterUsageOptions[ParameterUsageOptions.SESSION_METHOD_CALL] = {
    'skip_self': True,
    'skip_session_handle': True,
    'skip_input_parameters': False,
    'skip_output_parameters': True,
    'skip_size_parameter': True,
    'reordered_for_default_values': True,
    'name_to_use': 'python_name',
    'skip_repeated_capability_parameter': True,
}
_parameterUsageOptions[ParameterUsageOptions.DOCUMENTATION_SESSION_METHOD] = {
    'skip_self': True,
    'skip_session_handle': True,
    'skip_input_parameters': False,
    'skip_output_parameters': True,
    'skip_size_parameter': True,
    'reordered_for_default_values': True,
    'name_to_use': 'python_name_with_doc_default',
    'skip_repeated_capability_parameter': True,
}
_parameterUsageOptions[ParameterUsageOptions.CTYPES_CALL] = {
    'skip_self': True,
    'skip_session_handle': False,
    'skip_input_parameters': False,
    'skip_output_parameters': False,
    'skip_size_parameter': False,
    'reordered_for_default_values': False,
    'name_to_use': 'python_name',
    'skip_repeated_capability_parameter': False,
}
_parameterUsageOptions[ParameterUsageOptions.LIBRARY_METHOD_CALL] = {
    'skip_self': True,
    'skip_session_handle': False,
    'skip_input_parameters': False,
    'skip_output_parameters': False,
    'skip_size_parameter': False,
    'reordered_for_default_values': False,
    'name_to_use': 'library_method_call_snippet',
    'skip_repeated_capability_parameter': False,
}
_parameterUsageOptions[ParameterUsageOptions.CTYPES_ARGTYPES] = {
    'skip_self': True,
    'skip_session_handle': False,
    'skip_input_parameters': False,
    'skip_output_parameters': False,
    'skip_size_parameter': False,
    'reordered_for_default_values': False,
    'name_to_use': 'ctypes_type_library_call',
    'skip_repeated_capability_parameter': False,
}
_parameterUsageOptions[ParameterUsageOptions.LIBRARY_METHOD_DECLARATION] = {
    'skip_self': False,
    'skip_session_handle': False,
    'skip_input_parameters': False,
    'skip_output_parameters': False,
    'skip_size_parameter': False,
    'reordered_for_default_values': False,
    'name_to_use': 'python_name',
    'skip_repeated_capability_parameter': False,
}


def filter_parameters(function, parameter_usage_options):
    '''filter_parameters

    Filters and reorders the parameters of the function passed in based on parameter_usage_options.
    '''
    if type(parameter_usage_options) is not ParameterUsageOptions:
        raise TypeError('parameter_usage_options must be of type ' + str(ParameterUsageOptions))

    options_to_use = _parameterUsageOptions[parameter_usage_options]

    parameters_to_use = []

    # Filter based on options
    # Find the size parameter - we are assuming there can only be one, other from mechanism == 'ivi-dance' or mechanism == 'len'
    size_parameter = find_size_parameter(filter_ivi_dance_parameter(function['parameters']), function['parameters'])
    if size_parameter is None:
        size_parameter = find_size_parameter(filter_len_parameter(function['parameters']), function['parameters'])
    for x in function['parameters']:
        skip = False
        if x['direction'] == 'out' and options_to_use['skip_output_parameters']:
            skip = True
        if x['direction'] == 'in' and options_to_use['skip_input_parameters']:
            skip = True
        if x == size_parameter and options_to_use['skip_size_parameter']:
            skip = True
        if x['is_session_handle'] is True and options_to_use['skip_session_handle']:
            skip = True
        if x['is_repeated_capability'] is True and options_to_use['skip_repeated_capability_parameter']:
            skip = True
        if not skip:
            parameters_to_use.append(x)

    # Reorder based on options
    if options_to_use['reordered_for_default_values']:
        new_order = []
        for x in parameters_to_use:
            if 'default_value' not in x:
                new_order.append(x)
        for x in parameters_to_use:
            if 'default_value' in x:
                new_order.append(x)
        parameters_to_use = new_order

    return parameters_to_use


def get_params_snippet(function, parameter_usage_options):
    '''get_params_snippet

    Get a parameter list snippet based on parameter_usage_options.
    '''
    if type(parameter_usage_options) is not ParameterUsageOptions:
        raise TypeError('parameter_usage_options must be of type ' + str(ParameterUsageOptions))

    options_to_use = _parameterUsageOptions[parameter_usage_options]

    parameters_to_use = filter_parameters(function, parameter_usage_options)

    snippets = []
    if not options_to_use['skip_self']:
        snippets.append('self')

    # Render based on options
    for p in parameters_to_use:
            snippets.append(p[options_to_use['name_to_use']])
    return ', '.join(snippets)


def _get_output_param_return_snippet(output_parameter, parameters):
    '''Returns the snippet for returning a single output parameter from a Session method, i.e. "reading_ctype.value"'''
    assert output_parameter['direction'] == 'out', pp.pformat(output_parameter)
    return_type_snippet = ''
    if output_parameter['enum'] is not None:
        return_type_snippet = 'enums.' + output_parameter['enum'] + '('
    else:
        return_type_snippet = output_parameter['python_type'] + '('

    if output_parameter['is_buffer']:
        if output_parameter['type'] == 'ViChar':
            # 'self._encoding' is a variable on the session object
            snippet = output_parameter['ctypes_variable_name'] + '.value.decode(self._encoding)'
        else:
            if output_parameter['size']['mechanism'] == 'fixed':
                size = str(output_parameter['size']['value'])
            else:
                size_parameter = find_size_parameter(output_parameter, parameters)
                size = size_parameter['python_name']
            snippet = '[' + output_parameter['ctypes_variable_name'] + '[i] for i in range(' + size + ')]'
    else:
        snippet = return_type_snippet + output_parameter['ctypes_variable_name'] + '.value)'

    return snippet


def get_method_return_snippet(parameters):
    '''Returns a string suitable to use as the return argument of a Session method, i.e. "return reading_ctype.value"'''
    snippets = []
    for x in parameters:
        if x['direction'] == 'out' or x['size']['mechanism'] == 'ivi-dance':
            snippets.append(_get_output_param_return_snippet(x, parameters))
    return ('return ' + ', '.join(snippets)).strip()


def get_enum_type_check_snippet(parameter, indent):
    '''Returns python snippet to check that the type of a parameter is what is expected'''
    assert parameter['enum'] is not None, pp.pformat(parameter)
    assert parameter['direction'] == 'in', pp.pformat(parameter)
    enum_check = 'if type(' + parameter['python_name'] + ') is not ' + parameter['python_type'] + ':\n'
    enum_check += (' ' * indent) + 'raise TypeError(\'Parameter mode must be of type \' + str(' + parameter['python_type'] + '))'
    return enum_check


def _is_size_parameter(parameter, parameters):
    '''Returns true if the parameter represents the size of another parameter in the C API.'''
    for p in parameters:
        if p['is_buffer'] and p['size']['value'] == parameter['name']:
            return True
    return False


def get_ctype_variable_declaration_snippet(parameter, parameters):
    '''Returns python snippet that declares and initializes a ctypes variable for the parameter.

    These are several flavors on how to initialize these based on the parameter:
        1. Input session handle:                                    visatype.ViSession(self._vi)
        2. Input repeated capability:                               ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))
        3. Input string:                                            ctypes.create_string_buffer(parameter_name.encode(self._encoding))
        4. Input array (not string):                                (visatype.ViInt32 * len(list))(*list)
        5. Input is size of output buffer:                          visatype.ViInt32(0)
        6. Input scalar:                                            visatype.ViInt32(parameter_name)
        7. Input enum:                                              visatype.ViInt32(parameter_name.value)
        8. Output buffer with mechanism fixed-size:                 visatype.ViInt32 * 256
        9. Output buffer with mechanism ivi-dance:                  None
       10. Output buffer with mechanism passed-in:                  (visatype.ViInt32 * buffer_size)()
       11. Output scalar:                                           visatype.ViInt32()
    '''
    if parameter['direction'] == 'in':
        if parameter['is_session_handle'] is True:
            definition = 'visatype.{0}(self._{1})  # case 1'.format(parameter['ctypes_type'], parameter['python_name'])
        elif parameter['is_repeated_capability'] is True:
            definition = 'ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2'
        elif parameter['type'] == 'ViChar':
            definition = 'ctypes.create_string_buffer({0}.encode(self._encoding))  # case 3'.format(parameter['python_name'])
        elif parameter['is_buffer'] is True:
            definition = '(visatype.{0} * len({1}))(*{1})  # case 4'.format(parameter['ctypes_type'], parameter['python_name'], parameter['python_name'])
        else:
            if _is_size_parameter(parameter, parameters):
                definition = 'visatype.{0}(0)  # case 5'.format(parameter['ctypes_type'])
            elif parameter['enum'] is None:
                definition = 'visatype.{0}({1})  # case 6'.format(parameter['ctypes_type'], parameter['python_name'])
            else:
                definition = 'visatype.{0}({1}.value)  # case 7'.format(parameter['ctypes_type'], parameter['python_name'])
    else:
        assert parameter['direction'] == 'out'
        if parameter['is_buffer'] is True:
            assert 'size' in parameter, 'Warning: \'size\' not in parameter: ' + str(parameter)
            if parameter['size']['mechanism'] == 'fixed':
                definition = '(visatype.{0} * {1})()  # case 8'.format(parameter['ctypes_type'], parameter['size']['value'])
            elif parameter['size']['mechanism'] == 'ivi-dance':
                definition = 'None  # case 9'
            elif parameter['size']['mechanism'] == 'passed-in':
                size_parameter = find_size_parameter(parameter, parameters)
                definition = '(visatype.{0} * {1})()  # case 10'.format(parameter['ctypes_type'], size_parameter['python_name'])
            else:
                assert False, 'Unknown mechanism: ' + str(parameter)
        else:
            definition = 'visatype.{0}()  # case 11'.format(parameter['ctypes_type'])

    return parameter['ctypes_variable_name'] + ' = ' + definition


def get_dictionary_snippet(d, indent=4):
    '''Returns a formatted dictionary'''
    d_str = pprint.pformat(d)
    d_lines = d_str.splitlines()
    return ('\n' + (' ' * indent)).join(d_lines)

