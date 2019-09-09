# Find utilities
def find_parameter(name, parameters):
    parameter = [x for x in parameters if x['name'] == name]
    assert len(parameter) == 1, 'Parameter {0} not found. Check your metadata.'.format(name)
    return parameter[0]


def find_size_parameter(parameter_list, parameters, key='value'):
    '''Returns the parameter that is used to specify the size other parameters. Applies to 'ivi-dance', 'ivi-dance-with-a-twist' and 'passed-in'.

    Most behaviors will use 'value', but 'ivi-dance-with-a-twist' uses 'value' and 'value_twist'
    '''
    assert type(parameter_list) is list or type(parameter_list) is dict, 'Wrong type: {}'.format(type(parameter_list))
    if len(parameter_list) == 0:
        return None
    # Assumption: all parameters have the same size parameter, so we only need to use the first one
    try:
        # Try first as a list
        if key in parameter_list[0]['size']:
            return find_parameter(parameter_list[0]['size'][key], parameters)
    except KeyError:
        # Not a list, so must be a single parameter
        if key in parameter_list['size']:
            return find_parameter(parameter_list['size'][key], parameters)

    return None


def find_custom_type(p, config):
    for c in config['custom_types']:
        if p['ctypes_type'] == c['ctypes_type']:
            return c
    return None



