from .metadata_filters import filter_parameters
from .metadata_find import find_custom_type
from .metadata_find import find_size_parameter
from .parameter_usage_options import ParameterUsageOptions
import pprint

pp = pprint.PrettyPrinter(indent=4)

_parameterUsageOptionsSnippet = {}

_parameterUsageOptionsSnippet[ParameterUsageOptions.SESSION_METHOD_DECLARATION] = {
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
    assert output_parameter['direction'] == 'out', pp.pformat(output_parameter)
    return_type_snippet = ''

    # Custom types (I.e. inherit from ctypes.Structure) don't need a .value but do need a module name
    val_suffix = '.value'
    module_name = ''
    c = find_custom_type(output_parameter, config)
    if c is not None:
        val_suffix = ''
        module_name = c['file_name'] + '.'

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
            else:
                size_parameter = find_size_parameter(output_parameter, parameters)
                size = size_parameter['ctypes_variable_name'] + val_suffix

            snippet = '[' + return_type_snippet + output_parameter['ctypes_variable_name'] + '[i]) for i in range(' + size + ')]'
    else:
        snippet = return_type_snippet + output_parameter['ctypes_variable_name'] + val_suffix + ')'

    return snippet


def get_method_return_snippet(parameters, config):
    '''Returns a string suitable to use as the return argument of a Session method, i.e. "return reading_ctype.value"'''
    snippets = []
    for x in parameters:
        if x['direction'] == 'out' or x['size']['mechanism'] == 'ivi-dance':
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


def get_ctype_variable_declaration_snippet(parameter, parameters, config):
    '''Returns python snippet that declares and initializes a ctypes variable for the parameter that can be passed to the Library.

    We've identified many different cases on how these need to be initialized based on the parameter:
        1. Input session handle:                                        visatype.ViSession(self._vi)
        2. Input repeated capability:                                   ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))
        3. Input string:                                                ctypes.create_string_buffer(parameter_name.encode(self._encoding))
        4. Input buffer (not string):                                   (visatype.ViInt32 * len(list))(*list)
        5. Input is size of input buffer:                               visatype.ViInt32(len(list))
        6. Input is size of output buffer with mechanism ivi-dance:     visatype.ViInt32()
        7. Input is size of output buffer with mechanism passed-in:     visatype.ViInt32(buffer_size)
        8. Input scalar:                                                visatype.ViInt32(parameter_name)
        9. Input enum:                                                  visatype.ViInt32(parameter_name.value)
       10. Output buffer with mechanism fixed-size:                     visatype.ViInt32 * 256
       11. Output buffer with mechanism ivi-dance:                      None
       12. Output buffer with mechanism passed-in:                      (visatype.ViInt32 * buffer_size)()
       13. Output scalar or enum:                                       visatype.ViInt32()
    '''

    # First we need to determine the module. If it is a custom type then the module is the file associated wit that type, otherwise 'visatype'
    module_name = 'visatype'
    c = find_custom_type(parameter, config)
    if c is not None:
        module_name = c['file_name']

    # And now: A large block of conditional logic for getting to each of these cases. The following will not win any beauty pageants.
    # Suggestions on how to improve readability are welcome.
    # Note that we append "# case x". It's ugly in the generated code but it's sooo useful for debugging code generation problems.
    if parameter['direction'] == 'in':
        if parameter['is_session_handle'] is True:
            definition = '{0}.{1}(self._{2})  # case 1'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
        elif parameter['is_repeated_capability'] is True:
            definition = 'ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2'
        elif parameter['type'] == 'ViChar':
            definition = 'ctypes.create_string_buffer({0}.encode(self._encoding))  # case 3'.format(parameter['python_name'])
        elif parameter['is_buffer'] is True:
            definition = '({0}.{1} * len({2}))(*{2})  # case 4'.format(module_name, parameter['ctypes_type'], parameter['python_name'], parameter['python_name'])
        else:
            corresponding_buffer_parameter = _get_buffer_parameter_for_size_parameter(parameter, parameters)
            if corresponding_buffer_parameter is not None:
                if corresponding_buffer_parameter['direction'] == 'in':
                    definition = '{0}.{1}(len({2}))  # case 5'.format(module_name, parameter['ctypes_type'], corresponding_buffer_parameter['python_name'])
                else:
                    assert corresponding_buffer_parameter['direction'] == 'out'
                    if corresponding_buffer_parameter['size']['mechanism'] == 'ivi-dance':
                        definition = '{0}.{1}()  # case 6'.format(module_name, parameter['ctypes_type'])
                    else:
                        assert corresponding_buffer_parameter['size']['mechanism'] == 'passed-in', 'mechanism fixed-size makes no sense here! Check metadata'
                        definition = '{0}.{1}({2})  # case 7'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
            elif parameter['enum'] is None:
                definition = '{0}.{1}({2})  # case 8'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
            else:
                definition = '{0}.{1}({2}.value)  # case 9'.format(module_name, parameter['ctypes_type'], parameter['python_name'])
    else:
        assert parameter['direction'] == 'out'
        if parameter['is_buffer'] is True:
            assert 'size' in parameter, 'Warning: \'size\' not in parameter: ' + str(parameter)
            if parameter['size']['mechanism'] == 'fixed':
                definition = '({0}.{1} * {2})()  # case 10'.format(module_name, parameter['ctypes_type'], parameter['size']['value'])
            elif parameter['size']['mechanism'] == 'ivi-dance':
                definition = 'None  # case 11'
            elif parameter['size']['mechanism'] == 'passed-in':
                size_parameter = find_size_parameter(parameter, parameters)
                definition = '({0}.{1} * {2})()  # case 12'.format(module_name, parameter['ctypes_type'], size_parameter['python_name'])
            else:
                assert False, 'Unknown mechanism: ' + str(parameter)
        else:
            definition = '{0}.{1}()  # case 13'.format(module_name, parameter['ctypes_type'])

    return parameter['ctypes_variable_name'] + ' = ' + definition


def get_dictionary_snippet(d, indent=4):
    '''Returns a formatted dictionary'''
    d_str = pprint.pformat(d)
    d_lines = d_str.splitlines()
    return ('\n' + (' ' * indent)).join(d_lines)

