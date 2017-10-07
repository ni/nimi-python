import pprint
import re

pp = pprint.PrettyPrinter(indent=4)


# Coding convention transformation functions.
# TODO(marcoskirsch): not being used
def shoutcase_to_camelcase(shout_string):
    '''Converts a C-style SHOUT_CASE string to camelCase'''
    components = shout_string.split('_')
    return components[0].lower() \
        + "".join(component.title() for component in components[1:])


def camelcase_to_snakecase(camelcase_string):
    '''Converts a camelCase string to lower_case_snake_case'''
    # https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camelcase_string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


# TODO(marcoskirsch): not being used
def function_to_method_name(f):
    '''Returns an appropriate session method name for a given function'''
    # Method name is camelCase.
    return f['name'][0].lower() + f['name'][1:]


def sorted_attrs(a):
    return sorted(a, key=lambda k: a[k]['name'])


def get_python_type_for_visa_type(visa_type):
    '''Returns the type to use in the Python API from the original visa type used in the C API

    Do not use this with enums.
    '''
    type_map = {
        'ViString': 'str',
        'ViConstString': 'str',
        'ViString': 'str',
        'ViInt16': 'int',
        'ViUInt16': 'int',
        'ViInt32': 'int',
        'ViUInt32': 'int',
        'ViInt64': 'int',
        'ViUInt64': 'int',
        'ViReal32': 'float',
        'ViReal64': 'float',
        'ViStatus': 'int',
        'ViSession': 'int',
        'ViAttr': 'int',
        'ViChar': 'int',
        'ViBoolean': 'bool',
        'ViRsrc': 'str',
    }

    return type_map[visa_type]



