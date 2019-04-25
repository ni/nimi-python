# Find utilities
def find_parameter(name, parameters):
    parameter = [x for x in parameters if x['name'] == name]
    assert len(parameter) == 1, 'Parameter {0} not found. Check your metadata.'.format(name)
    return parameter[0]


def find_size_parameter(parameter_list, parameters, key='value'):
    '''Returns the parameter that is used to specify the size other parameters. Applies to 'ivi-dance' and 'passed-in'.'''
    if len(parameter_list) == 0:
        return None
    # Assumption: all parameters have the same size parameter, so we only need to use the first one
    try:
        # Try first as a list
        return find_parameter(parameter_list[0]['size'][key], parameters)
    except KeyError:
        # Not a list, so must be a single parameter
        return find_parameter(parameter_list['size'][key], parameters)


def find_custom_type(p, config):
    for c in config['custom_types']:
        if p['ctypes_type'] == c['ctypes_type']:
            return c
    return None



