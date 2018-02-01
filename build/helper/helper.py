import pprint
import re

pp = pprint.PrettyPrinter(indent=4)


# noqa statements because we want to format the table in a readable way
_type_map = {
    'ViConstString': { 'array_type': None,     'python_type': 'str',   'numpy_type': None,         },  # noqa: E201, E202, E241
    'ViString':      { 'array_type': None,     'python_type': 'str',   'numpy_type': None,         },  # noqa: E201, E202, E241
    'ViInt8':        { 'array_type': 'b',      'python_type': 'int',   'numpy_type': 'int8',       },  # noqa: E201, E202, E241
    'ViUInt8':       { 'array_type': 'B',      'python_type': 'int',   'numpy_type': 'uint8',      },  # noqa: E201, E202, E241
    'ViInt16':       { 'array_type': 'h',      'python_type': 'int',   'numpy_type': 'int16',      },  # noqa: E201, E202, E241
    'ViUInt16':      { 'array_type': 'H',      'python_type': 'int',   'numpy_type': 'uint16',     },  # noqa: E201, E202, E241
    'ViInt32':       { 'array_type': 'l',      'python_type': 'int',   'numpy_type': 'int32',      },  # noqa: E201, E202, E241
    'ViUInt32':      { 'array_type': 'L',      'python_type': 'int',   'numpy_type': 'uint32',     },  # noqa: E201, E202, E241
    'ViInt64':       { 'array_type': 'q',      'python_type': 'int',   'numpy_type': 'int64',      },  # noqa: E201, E202, E241
    'ViUInt64':      { 'array_type': 'Q',      'python_type': 'int',   'numpy_type': 'uint64',     },  # noqa: E201, E202, E241
    'ViReal32':      { 'array_type': 'f',      'python_type': 'float', 'numpy_type': 'float32',    },  # noqa: E201, E202, E241
    'ViReal64':      { 'array_type': 'd',      'python_type': 'float', 'numpy_type': 'float64',    },  # noqa: E201, E202, E241
    'ViStatus':      { 'array_type': None,     'python_type': 'int',   'numpy_type': None,         },  # noqa: E201, E202, E241
    'ViSession':     { 'array_type': None,     'python_type': 'int',   'numpy_type': None,         },  # noqa: E201, E202, E241
    'ViAttr':        { 'array_type': None,     'python_type': 'int',   'numpy_type': None,         },  # noqa: E201, E202, E241
    'ViChar':        { 'array_type': None,     'python_type': 'int',   'numpy_type': None,         },  # noqa: E201, E202, E241
    'ViChar[]':      { 'array_type': None,     'python_type': 'str',   'numpy_type': None,         },  # noqa: E201, E202, E241
    'ViBoolean':     { 'array_type': None,     'python_type': 'bool',  'numpy_type': None,         },  # noqa: E201, E202, E241
    'ViRsrc':        { 'array_type': None,     'python_type': 'str',   'numpy_type': 'bool_',      },  # noqa: E201, E202, E241
}


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

    if api_type in _type_map and _type_map[api_type]['python_type'] is not None:
        return _type_map[api_type]['python_type']
    else:
        for c in config['custom_types']:
            if c['ctypes_type'] == api_type:
                return c['python_name']

    # We didn't find it anywhere so return as is
    return api_type


def get_numpy_type_for_api_type(api_type, config):
    '''Returns the numpy type to use in the Python API from the original visa or custom type used in the C API

    Do not use this with enums.
    '''

    if api_type in _type_map and _type_map[api_type]['numpy_type'] is not None:
        return _type_map[api_type]['numpy_type']
    else:
        for c in config['custom_types']:
            if c['ctypes_type'] == api_type:
                return c['python_name']
        # We didn't find it so assert
        assert False, 'Unknown value for api_type: {0}'.format(api_type)


def get_array_type_for_api_type(api_type):
    '''Returns the array type to use in the Python API from the original visa or custom type used in the C API

    Do not use this with enums.
    '''

    if api_type in _type_map and _type_map[api_type]['array_type'] is not None:
        return _type_map[api_type]['array_type']
    else:
        raise TypeError('Only simple types allowed for arrays: {0}'.format(api_type))

