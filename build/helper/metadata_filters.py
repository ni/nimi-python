# Filters


def filter_codegen_functions(functions):
    '''Returns function metadata only for those functions to be included in codegen'''
    return {k: v for k, v in functions.items() if v['codegen_method'] != 'no'}


def filter_input_parameters(parameters):
    '''Returns list of parameters that includes only input parameters, except the session parameter or repeated capability parameter if they exists'''
    return [x for x in parameters if x['direction'] == 'in' and not x['is_session_handle'] and not x['is_repeated_capability']]


def filter_output_parameters(parameters):
    '''Returns list of parameters that includes only output parameters, except the ivi-dance parameter if it exists'''
    return [x for x in parameters if x['direction'] == 'out' and x['size']['mechanism'] != 'ivi-dance']


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



