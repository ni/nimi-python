from .parameter_usage_options import ParameterUsageOptions
# Filters

_parameterUsageOptionsFiltering = {}

def filter_codegen_functions(functions):
    '''Returns function metadata only for those functions to be included in codegen'''
    return {k: v for k, v in functions.items() if v['codegen_method'] != 'no'}
_parameterUsageOptionsFiltering[ParameterUsageOptions.SESSION_METHOD_DECLARATION] = {
    'skip_session_handle': True,
    'skip_input_parameters': False,
    'skip_output_parameters': True,
    'skip_size_parameter': True,
    'reordered_for_default_values': True,
    'skip_repeated_capability_parameter': True,
    'skip_non_enum_parameter': False,
    'mechanism': 'any',
}
_parameterUsageOptionsFiltering[ParameterUsageOptions.SESSION_METHOD_CALL] = {
    'skip_session_handle': True,
    'skip_input_parameters': False,
    'skip_output_parameters': True,
    'skip_size_parameter': True,
    'reordered_for_default_values': True,
    'skip_repeated_capability_parameter': True,
    'skip_non_enum_parameter': False,
    'mechanism': 'any',
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
    'mechanism': 'fixed, passed-in, len',  # any but ivi-dance
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



def filter_enum_parameters(parameters):
    '''Returns a list of parameters whose type is an enum'''
    return [x for x in parameters if x['enum'] is not None]


def _filter_size_parameter(parameters, mechanism, direction):
    '''Returns the parameter what matches the given mechanism

    Args:
        paramaters: Parameters from function
        mechanism: which mechanism we are looking for
        direction: optional, will be used to verify the direction of the found parameter

    Returns:
        Parameter that matches the mechanism
    '''
    param = [x for x in parameters if x['size']['mechanism'] == mechanism]
    assert len(param) <= 1, '{0} {1} parameters. No more than one is allowed'.format(len(param), mechanism)
    if len(param) == 0:
        return None
    if direction is not None:
        assert param[0]['direction'] == direction, "{0} parameter must have 'direction':'{1}'. Check your metadata.".format(mechanism, direction)
    assert param[0]['is_buffer'], "{0} parameter must have 'is_buffer':True. Check your metadata.".format(mechanism)
    return param[0]


def filter_ivi_dance_parameter(parameters):
    '''Returns the ivi-dance parameter of a session method if there is one. This is the parameter whose size is determined at runtime.'''
    return _filter_size_parameter(parameters, 'ivi-dance', 'out')


def filter_len_parameter(parameters):
    '''Returns the len parameter of a session method if there is one. This is the parameter whose size is determined at runtime.'''
    return _filter_size_parameter(parameters, 'len', 'in')



