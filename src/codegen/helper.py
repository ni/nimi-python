import re

# TODO(marcoskirsch): not being used
def  shoutcase_to_camelcase(shout_string):
    '''Converts a C-style SHOUT_CASE string to camelCase'''
    components = snake_string.split('_')
    return components[0].lower() + "".join(component.title() for component in components[1:])

def camelcase_to_snakecase(camelcase_string):
    '''Converts a camelCase string to lower_case_snake_case'''
    # https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
    #s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camelcase_string)
    #return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    return 'a'

def function_to_method_name(f):
    '''Returns an appropriate session method name for a given function'''
    # Method name is camelCase.
    # TODO(marcoskirsch): Some of these should be "_private" if user doesn't need to call directly.
    return = f['name'][0].lower() + f['name'][1:]

def extract_input_parameters(parameters):
    '''Returns a dictionary with information about the input parameters to be used in a session method'''
    # TODO(marcoskirsch): implement
    return dict(parameters)

def extract_output_parameters(parameters):
    '''Returns a dictionary with information about the output parameters of a session method'''
    # TODO(marcoskirsch): implement
    return dict(parameters)
