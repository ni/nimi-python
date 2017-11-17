from .metadata_find import find_size_parameter
from .parameter_usage_options import ParameterUsageOptions

import pprint
pp = pprint.PrettyPrinter(indent=4)
# Filters

_parameterUsageOptionsFiltering = {}

_parameterUsageOptionsFiltering[ParameterUsageOptions.SESSION_METHOD_DECLARATION] = {
    'skip_session_handle': True,
    'skip_input_parameters': False,
    'skip_output_parameters': True,
    'skip_size_parameter': True,
    'reordered_for_default_values': True,
    'skip_repeated_capability_parameter': True,
    'skip_non_enum_parameter': False,
    'mechanism': 'fixed, passed-in, len',
}
_parameterUsageOptionsFiltering[ParameterUsageOptions.SESSION_METHOD_CALL] = {
    'skip_session_handle': True,
    'skip_input_parameters': False,
    'skip_output_parameters': True,
    'skip_size_parameter': True,
    'reordered_for_default_values': True,
    'skip_repeated_capability_parameter': True,
    'skip_non_enum_parameter': False,
    'mechanism': 'fixed, passed-in',
}
_parameterUsageOptionsFiltering[ParameterUsageOptions.DOCUMENTATION_SESSION_METHOD] = {
    'skip_session_handle': True,
    'skip_input_parameters': False,
    'skip_output_parameters': True,
    'skip_size_parameter': True,
    'reordered_for_default_values': True,
    'skip_repeated_capability_parameter': True,
    'skip_non_enum_parameter': False,
    'mechanism': 'any',
}
_parameterUsageOptionsFiltering[ParameterUsageOptions.CTYPES_CALL] = {
    'skip_session_handle': False,
    'skip_input_parameters': False,
    'skip_output_parameters': False,
    'skip_size_parameter': False,
    'reordered_for_default_values': False,
    'skip_repeated_capability_parameter': False,
    'skip_non_enum_parameter': False,
    'mechanism': 'any',
}
_parameterUsageOptionsFiltering[ParameterUsageOptions.LIBRARY_METHOD_CALL] = {
    'skip_session_handle': False,
    'skip_input_parameters': False,
    'skip_output_parameters': False,
    'skip_size_parameter': False,
    'reordered_for_default_values': False,
    'skip_repeated_capability_parameter': False,
    'skip_non_enum_parameter': False,
    'mechanism': 'any',
}
_parameterUsageOptionsFiltering[ParameterUsageOptions.CTYPES_ARGTYPES] = {
    'skip_session_handle': False,
    'skip_input_parameters': False,
    'skip_output_parameters': False,
    'skip_size_parameter': False,
    'reordered_for_default_values': False,
    'skip_repeated_capability_parameter': False,
    'skip_non_enum_parameter': False,
    'mechanism': 'any',
}
_parameterUsageOptionsFiltering[ParameterUsageOptions.LIBRARY_METHOD_DECLARATION] = {
    'skip_session_handle': False,
    'skip_input_parameters': False,
    'skip_output_parameters': False,
    'skip_size_parameter': False,
    'reordered_for_default_values': False,
    'skip_repeated_capability_parameter': False,
    'skip_non_enum_parameter': False,
    'mechanism': 'any',
}
_parameterUsageOptionsFiltering[ParameterUsageOptions.INPUT_PARAMETERS] = {
    'skip_session_handle': True,
    'skip_input_parameters': False,
    'skip_output_parameters': True,
    'skip_size_parameter': False,
    'reordered_for_default_values': False,
    'skip_repeated_capability_parameter': True,
    'skip_non_enum_parameter': False,
    'mechanism': 'any',
}
_parameterUsageOptionsFiltering[ParameterUsageOptions.OUTPUT_PARAMETERS] = {
    'skip_session_handle': True,
    'skip_input_parameters': True,
    'skip_output_parameters': False,
    'skip_size_parameter': False,
    'reordered_for_default_values': False,
    'skip_repeated_capability_parameter': False,
    'skip_non_enum_parameter': False,
    'mechanism': 'fixed, passed-in, len, python-code',  # any but ivi-dance
}
_parameterUsageOptionsFiltering[ParameterUsageOptions.IVI_DANCE_PARAMETER] = {
    'skip_session_handle': True,
    'skip_input_parameters': True,
    'skip_output_parameters': False,
    'skip_size_parameter': False,
    'reordered_for_default_values': False,
    'skip_repeated_capability_parameter': False,
    'skip_non_enum_parameter': False,
    'mechanism': 'ivi-dance',
}
_parameterUsageOptionsFiltering[ParameterUsageOptions.LEN_PARAMETER] = {
    'skip_session_handle': True,
    'skip_input_parameters': False,
    'skip_output_parameters': True,
    'skip_size_parameter': False,
    'reordered_for_default_values': False,
    'skip_repeated_capability_parameter': False,
    'skip_non_enum_parameter': False,
    'mechanism': 'len',
}
_parameterUsageOptionsFiltering[ParameterUsageOptions.INPUT_ENUM_PARAMETERS] = {
    'skip_session_handle': True,
    'skip_input_parameters': False,
    'skip_output_parameters': True,
    'skip_size_parameter': False,
    'reordered_for_default_values': False,
    'skip_repeated_capability_parameter': True,
    'skip_non_enum_parameter': True,
    'mechanism': 'any',
}


def filter_parameters(function, parameter_usage_options):
    '''filter_parameters

    Filters and reorders the parameters of the function passed in based on parameter_usage_options.
    '''
    if type(parameter_usage_options) is not ParameterUsageOptions:
        raise TypeError('parameter_usage_options must be of type ' + str(ParameterUsageOptions))

    options_to_use = _parameterUsageOptionsFiltering[parameter_usage_options]

    parameters_to_use = []

    # Filter based on options
    size_parameter = None
    # If we are being called looking for the ivi-dance, len or code param, we do not care about the size param so we do
    #  not call back into ourselves, to avoid infinite recursion
    if parameter_usage_options not in [ParameterUsageOptions.IVI_DANCE_PARAMETER, ParameterUsageOptions.LEN_PARAMETER]:
        # Find the size parameter - we are assuming there can only be one
        size_parameter = find_size_parameter(filter_ivi_dance_parameter(function), function['parameters'])
        if size_parameter is None:
            size_parameter = find_size_parameter(filter_len_parameter(function), function['parameters'])
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


def filter_ivi_dance_parameter(function):
    '''Returns the ivi-dance parameter of a session method if there is one. This is the parameter whose size is determined at runtime.

    asserts if more than one parameter found
    Args:
        function: function whose parameters should be checked

    Return:
        None if no ivi-dance parameter found
        Parameter dict if one is found
    '''
    params = filter_parameters(function, ParameterUsageOptions.IVI_DANCE_PARAMETER)
    if len(params) == 0:
        return None
    assert len(params) == 1, 'Found several ivi-dance parameters, expected only one. Found: {0}'.format([x['name'] for x in params])
    return params[0]


def filter_len_parameter(function):
    '''Returns the len parameter of a session method if there is one. This is the parameter whose size is determined at runtime.


    asserts if more than one parameter found

    Args:
        function: function whose parameters should be checked

    Return:
        None if no len parameter found
        Parameter dict if one is found
    '''
    params = filter_parameters(function, ParameterUsageOptions.LEN_PARAMETER)
    if len(params) == 0:
        return None
    assert len(params) == 1, 'Found more than one len parameter: {0}'.format(pp.pformat(params))
    return params[0]


def filter_codegen_functions(functions):
    '''Returns function metadata only for those functions to be included in codegen'''
    return {k: v for k, v in functions.items() if v['codegen_method'] != 'no'}


def filter_codegen_attributes(attributes):
    '''Returns attribute metadata only for those attributes to be included in codegen'''
    return {k: v for k, v in attributes.items() if v['codegen_method'] != 'no'}


def filter_codegen_enums(enums):
    '''Returns enum metadata only for those enums to be included in codegen'''
    return {k: v for k, v in enums.items() if v['codegen_method'] != 'no'}


