# Filters


def filter_codegen_functions(functions):
    '''Returns function metadata only for those functions to be included in codegen'''
    return {k: v for k, v in functions.items() if v['codegen_method'] != 'no'}


def filter_input_parameters(parameters):
    '''Returns list of parameters that includes only input parameters, except the session parameter if it exists'''
    return [x for x in parameters if x['direction'] == 'in' and not x['is_session_handle'] and not x['is_repeated_capability']]


def filter_output_parameters(parameters):
    '''Returns list of parameters that includes only output parameters, except the ivi-dance parameter if it exists'''
    return [x for x in parameters if x['direction'] == 'out' and x['size']['mechanism'] != 'ivi-dance']


def filter_enum_parameters(parameters):
    '''Returns a list of parameters whose type is an enum'''
    return [x for x in parameters if x['enum'] is not None]


def filter_ivi_dance_parameter(parameters):
    '''Returns the ivi-dance parameter of a session method if there is one. This is the parameter whose size is determined at runtime.'''
    param = [x for x in parameters if x['size']['mechanism'] == 'ivi-dance']
    assert len(param) <= 1, '{0} ivi-dance parameters. No more than one is allowed'.format(len(param))
    if len(param) == 0:
        return None
    assert param[0]['direction'] == 'out', "ivi-dance parameter must have 'direction':'out'. Check your metadata."
    assert param[0]['is_buffer'], "ivi-dance parameter must have 'is_buffer':True. Check your metadata."
    return param[0]



