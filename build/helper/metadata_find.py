# Find utilities
def find_parameter(name, parameters):
    parameter = [x for x in parameters if x['name'] == name]
    assert len(parameter) == 1, 'Parameter {0} not found. Check your metadata.'.format(name)
    return parameter[0]


def find_size_parameter(parameter, parameters):
    '''Returns the parameter that is used to specify the size of another parameter. Applies to 'ivi-dance' and 'passed-in'.'''
    if not parameter:
        return None
    return find_parameter(parameter['size']['value'], parameters)



