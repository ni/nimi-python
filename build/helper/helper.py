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


def get_python_type_for_api_type(api_type, config):
    '''Returns the type to use in the Python API from the original visa or custom type used in the C API

    Do not use this with enums.
    '''
    type_map = {
        'ViString': 'str',
        'ViConstString': 'str',
        'ViString': 'str',
        'ViInt8': 'int',
        'ViUInt8': 'int',
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

    if api_type in type_map:
        return type_map[api_type]
    else:
        for c in config['custom_types']:
            if c['ctypes_type'] == api_type:
                return c['python_name']
        # We didn't find it so assert
        assert False, 'Unknown api_type: {0}'.format(api_type)


def get_numpy_type_for_api_type(api_type, config):
    '''Returns the numpy type to use in the Python API from the original visa or custom type used in the C API

    Do not use this with enums.
    '''
    type_map = {
        'ViBoolean': 'bool_',
        'ViInt8': 'int8',
        'ViUInt8': 'uint8',
        'ViInt16': 'int16',
        'ViUInt16': 'uint16',
        'ViInt32': 'int32',
        'ViUInt32': 'uint32',
        'ViInt64': 'int64',
        'ViUInt64': 'uint64',
        'ViReal32': 'float32',
        'ViReal64': 'float64',
    }

    if api_type in type_map:
        return type_map[api_type]
    else:
        for c in config['custom_types']:
            if c['ctypes_type'] == api_type:
                return c['python_name']
        # We didn't find it so assert
        assert False, 'Unknown api_type: {0}'.format(api_type)



