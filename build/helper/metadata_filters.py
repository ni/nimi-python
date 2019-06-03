from .metadata_find import find_size_parameter
from .parameter_usage_options import ParameterUsageOptions

import pprint
pp = pprint.PrettyPrinter(indent=4)
# Filters

_ParameterUsageOptionsFiltering = {
    ParameterUsageOptions.SESSION_METHOD_DECLARATION: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': True,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': True,
        'reordered_for_default_values': True,
        'skip_repeated_capability_parameter': True,
        'skip_non_enum_parameter': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'fixed, passed-in, len',
        'python_api_list': True,
    },
    ParameterUsageOptions.SESSION_NUMPY_INTO_METHOD_DECLARATION: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': True,
        'but_keep_output_numpy_array_parameters': True,
        'skip_size_parameter': False,
        'reordered_for_default_values': True,
        'skip_repeated_capability_parameter': True,
        'skip_non_enum_parameter': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'fixed, passed-in',
        'python_api_list': False,
    },
    ParameterUsageOptions.SESSION_METHOD_CALL: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': True,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': True,
        'reordered_for_default_values': True,
        'skip_repeated_capability_parameter': True,
        'skip_non_enum_parameter': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'fixed, passed-in',
        'python_api_list': True,
    },
    ParameterUsageOptions.DOCUMENTATION_SESSION_METHOD: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': True,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': True,
        'reordered_for_default_values': True,
        'skip_repeated_capability_parameter': True,
        'skip_non_enum_parameter': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'any',
        'python_api_list': True,
    },
    ParameterUsageOptions.CTYPES_CALL: {
        'skip_session_handle': False,
        'skip_input_parameters': False,
        'skip_output_parameters': False,
        'but_keep_output_numpy_array_parameters': True,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'any',
        'python_api_list': True,
    },
    ParameterUsageOptions.LIBRARY_METHOD_CALL: {
        'skip_session_handle': False,
        'skip_input_parameters': False,
        'skip_output_parameters': False,
        'but_keep_output_numpy_array_parameters': True,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'any',
        'python_api_list': True,
    },
    ParameterUsageOptions.CTYPES_ARGTYPES: {
        'skip_session_handle': False,
        'skip_input_parameters': False,
        'skip_output_parameters': False,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'any',
        'python_api_list': True,
    },
    ParameterUsageOptions.LIBRARY_METHOD_DECLARATION: {
        'skip_session_handle': False,
        'skip_input_parameters': False,
        'skip_output_parameters': False,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'any',
        'python_api_list': True,
    },
    ParameterUsageOptions.INPUT_PARAMETERS: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': True,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': True,
        'skip_non_enum_parameter': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'any',
        'python_api_list': True,
    },
    ParameterUsageOptions.OUTPUT_PARAMETERS: {
        'skip_session_handle': True,
        'skip_input_parameters': True,
        'skip_output_parameters': False,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'fixed, passed-in, len, python-code',  # any but ivi-dance
        'python_api_list': True,
    },
    ParameterUsageOptions.NUMPY_PARAMETERS: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': False,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_all_except_numpy_parameters': True,
        'mechanism': 'any',
        'python_api_list': True,
    },
    ParameterUsageOptions.IVI_DANCE_PARAMETER: {
        'skip_session_handle': True,
        'skip_input_parameters': True,
        'skip_output_parameters': False,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'ivi-dance, ivi-dance-with-a-twist',
        'python_api_list': True,
    },
    ParameterUsageOptions.LEN_PARAMETER: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': True,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': False,
        'skip_non_enum_parameter': False,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'len',
        'python_api_list': True,
    },
    ParameterUsageOptions.INPUT_ENUM_PARAMETERS: {
        'skip_session_handle': True,
        'skip_input_parameters': False,
        'skip_output_parameters': True,
        'but_keep_output_numpy_array_parameters': False,
        'skip_size_parameter': False,
        'reordered_for_default_values': False,
        'skip_repeated_capability_parameter': True,
        'skip_non_enum_parameter': True,
        'skip_all_except_numpy_parameters': False,
        'mechanism': 'any',
        'python_api_list': True,
    },
}
# Only difference is we want to skip parameters not in api
_ParameterUsageOptionsFiltering[ParameterUsageOptions.SESSION_INIT_DECLARATION] = _ParameterUsageOptionsFiltering[ParameterUsageOptions.SESSION_METHOD_DECLARATION].copy()
_ParameterUsageOptionsFiltering[ParameterUsageOptions.SESSION_INIT_DECLARATION]['python_api_list'] = False

# Only difference is we want to skip parameters not in api
_ParameterUsageOptionsFiltering[ParameterUsageOptions.SESSION_INIT_CALL] = _ParameterUsageOptionsFiltering[ParameterUsageOptions.SESSION_METHOD_CALL].copy()


def filter_parameters(function, parameter_usage_options):
    '''filter_parameters

    Filters and reorders the parameters of the function passed in based on parameter_usage_options.
    '''
    if type(parameter_usage_options) is not ParameterUsageOptions:
        raise TypeError('parameter_usage_options must be of type ' + str(ParameterUsageOptions))

    options_to_use = _ParameterUsageOptionsFiltering[parameter_usage_options]

    parameters_to_use = []

    # Filter based on options
    size_parameter = None
    # If we are being called looking for the ivi-dance, len or code param, we do not care about the size param so we do
    #  not call back into ourselves, to avoid infinite recursion
    if parameter_usage_options not in [ParameterUsageOptions.IVI_DANCE_PARAMETER, ParameterUsageOptions.LEN_PARAMETER]:
        # Find the size parameter - we are assuming there can only be one type, either from ivi-dance or len
        size_parameter = find_size_parameter(filter_ivi_dance_parameters(function), function['parameters'])
        if size_parameter is None:
            size_parameter = find_size_parameter(filter_len_parameters(function), function['parameters'])
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
        if x['enum'] is None and options_to_use['skip_non_enum_parameter']:
            skip = True
        if options_to_use['mechanism'] != 'any' and x['size']['mechanism'] not in options_to_use['mechanism']:
            skip = True
        if options_to_use['skip_all_except_numpy_parameters'] and not x['numpy']:
            skip = True
        if options_to_use['but_keep_output_numpy_array_parameters'] is True and x['numpy'] is True:
            skip = False
        if not options_to_use['python_api_list'] and not x['use_in_python_api']:
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


def filter_ivi_dance_parameters(function):
    '''Returns the ivi-dance parameters of a session method if there are any. These are the parameters whose size is determined at runtime using the ivi-dance.

    asserts all parameters that use ivi-dance reference the same parameter
    Args:
        function: function whose parameters should be checked

    Return:
        None if no ivi-dance parameter found
        Parameters dict if one is found
    '''
    params = filter_parameters(function, ParameterUsageOptions.IVI_DANCE_PARAMETER)
    if len(params) > 0:
        size_param = params[0]['size']['value']
        assert all(x['size']['value'] == size_param for x in params)
    return params


def filter_len_parameters(function):
    '''Returns the len parameters of a session method if there are any. These are the parameters whose size is determined at runtime using the value of a different parameter.

    asserts all parameters that use len reference the same parameter
    Args:
        function: function whose parameters should be checked

    Return:
        None if no len parameter found
        Parameters dict if one is found
    '''
    params = filter_parameters(function, ParameterUsageOptions.LEN_PARAMETER)
    if len(params) > 0:
        size_param = params[0]['size']['value']
        assert all(x['size']['value'] == size_param for x in params)
    return params


def filter_codegen_functions(functions):
    '''Returns function metadata only for those functions to be included in codegen'''
    return {k: v for k, v in functions.items() if v['codegen_method'] != 'no'}


def filter_library_functions(functions):
    '''Returns function metadata only for those functions to included the library layer (library.py and mock_helper.py)'''
    return {k: v for k, v in functions.items() if v['codegen_method'] != 'no' and v['codegen_method'] != 'python-only'}


def filter_public_functions(functions):
    '''Returns function metadata only for those functions that are public'''
    return {k: v for k, v in functions.items() if v['codegen_method'] == 'public' or v['codegen_method'] == 'python-only'}


def filter_codegen_attributes(attributes):
    '''Returns attribute metadata only for those attributes to be included in codegen'''
    return {k: v for k, v in attributes.items() if v['codegen_method'] != 'no'}


def filter_codegen_attributes_public_only(attributes):
    '''Returns attribute metadata only for those attributes to be included in codegen'''
    return {k: v for k, v in attributes.items() if v['codegen_method'] == 'public'}


def filter_codegen_enums(enums):
    '''Returns enum metadata only for those enums to be included in codegen'''
    return {k: v for k, v in enums.items() if v['codegen_method'] != 'no'}


