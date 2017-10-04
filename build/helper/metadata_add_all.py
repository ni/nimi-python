# Useful functions for use in the metadata modules

from .helper import camelcase_to_snakecase
from .helper import get_python_type_for_visa_type

import copy
import pprint

pp = pprint.PrettyPrinter(indent=4, width=80)

# Functions to add information to metadata structures that are specific to our codegen needs.


def _add_name(function, name):
    '''Adds a name' key/value pair to the function metadata'''
    assert 'name' not in function, "'name' is already populated which means issue #372 is closed, rendering _add_name() redundant."
    function['name'] = name
    return function


def _add_python_method_name(function, name):
    '''Adds a python_name' key/value pair to the function metadata'''
    if function['codegen_method'] == 'private':
        function['python_name'] = '_' + camelcase_to_snakecase(name)
    else:
        function['python_name'] = camelcase_to_snakecase(name)
    return function


def _add_python_parameter_name(parameter):
    '''Adds a python_name key/value pair to the parameter metadata'''
    parameter['python_name'] = camelcase_to_snakecase(parameter['name'])
    return parameter


def _add_python_type(parameter):
    '''Adds the type to use in the Python API to the parameter metadata'''
    if parameter['enum'] is None:
        parameter['python_type'] = get_python_type_for_visa_type(parameter['type'])
    else:
        parameter['python_type'] = 'enums.' + parameter['enum']
    return parameter


def _add_ctypes_variable_name(parameter):
    '''Adds a ctypes_variable_name key/value pair to the parameter metadata for a corresponding ctypes variable'''
    parameter['ctypes_variable_name'] = parameter['python_name'] + '_ctype'
    return parameter


def _add_ctypes_type(parameter):
    '''Adds a ctypes_type key/value pair to the parameter metadata for calling into the library'''
    parameter['ctypes_type'] = parameter['type']
    if parameter['direction'] == 'out':
        if parameter['type'] == 'ViString' or parameter['type'] == 'ViRsrc' or parameter['type'] == 'ViConstString':
            # These are defined as c_char_p which is already a pointer!
            parameter['ctypes_type_library_call'] = parameter['ctypes_type']
        else:
            parameter['ctypes_type_library_call'] = "ctypes.POINTER(" + parameter['ctypes_type'] + ")"
    else:
        parameter['ctypes_type_library_call'] = parameter['ctypes_type']

    return parameter


def _add_is_error_handling(f):
    '''Adds is_error_handling information to the function metadata if it isn't already defined. Defaults to False.'''
    # TODO(marcoskirsch): The information is added in functions_addon.py. I think we can instead infer from method
    # name but I am not sure if it's a good idea (heuristics vs being explicit - both error prone in different ways).
    try:
        f['is_error_handling']
    except KeyError:
        # Not populated, assume False
        f['is_error_handling'] = False
    return f


def _add_buffer_info(parameter):
    '''Adds buffer information to the parameter metadata iff 'size' is defined else assume not a buffer'''
    try:
        parameter['size']
        parameter['is_buffer'] = True
    except KeyError:
        # Not populated, assume False
        parameter['size'] = {'mechanism': 'fixed', 'value': 1}
        parameter['is_buffer'] = False
    return parameter


def _add_library_method_call_snippet(parameter, session_handle_parameter_name):
    '''Code snippet for calling a method of Library for this parameter.'''
    if parameter['direction'] == 'in':
        if parameter['name'] == session_handle_parameter_name:
            library_method_call_snippet = 'self._' + session_handle_parameter_name
        elif parameter['is_repeated_capability']:
            # TODO(marcoskirsch): .encode('ascii') is a problem if the repeated capability contains non-ASCII characters.
            library_method_call_snippet = 'self._repeated_capability.encode(\'ascii\')'
        else:
            library_method_call_snippet = parameter['python_name']
            library_method_call_snippet += '.value' if parameter['enum'] is not None else ''
            if parameter['type'] == 'ViString' or parameter['type'] == 'ViConstString' or parameter['type'] == 'ViRsrc':
                library_method_call_snippet += '.encode(\'ascii\')'
    else:
        assert parameter['direction'] == 'out', pp.pformat(parameter)
        if parameter['size']['mechanism'] == 'ivi-dance':
            library_method_call_snippet = parameter['ctypes_variable_name']
        elif parameter['is_buffer']:
            library_method_call_snippet = 'ctypes.cast(' + parameter['ctypes_variable_name'] + ', ctypes.POINTER(ctypes_types.' + parameter['ctypes_type'] + '))'
        else:
            library_method_call_snippet = 'ctypes.pointer(' + (parameter['ctypes_variable_name']) + ')'
    parameter['library_method_call_snippet'] = library_method_call_snippet


def _add_default_value_name(parameter):
    '''Declaration with default value, if set'''
    if 'default_value' in parameter:
        if 'enum' in parameter and parameter['enum'] is not None:
            name = parameter['python_name'] + "=enums." + parameter['default_value']
        else:
            name = parameter['python_name'] + "=" + repr(parameter['default_value'])

    else:
        name = parameter['python_name']

    parameter['python_name_with_default'] = name


def _add_default_value_name_for_docs(parameter, module_name):
    '''Declaration with default value, if set'''
    if 'default_value' in parameter:
        if 'enum' in parameter and parameter['enum'] is not None:
            name = parameter['python_name'] + "=" + module_name + '.' + parameter['default_value']
        else:
            name = parameter['python_name'] + "=" + repr(parameter['default_value'])

    else:
        name = parameter['python_name']

    parameter['python_name_with_doc_default'] = name


# Parameter names denoting channel/repeated capabilities was compiled by looking at public header files for different MI drivers.
_repeated_capability_parameter_names = ['channelName', 'channelList', 'channel', 'channelNameList']


def _add_has_repeated_capability(f):
    '''Adds a boolean 'has_repeated_capability' to the function metadata by inferring it from its parameter names, if not previously populated..'''
    if 'has_repeated_capability' not in f:
        f['has_repeated_capability'] = False
        for p in f['parameters']:
            f['has_repeated_capability'] = f['has_repeated_capability'] or p['name'] in _repeated_capability_parameter_names


def _add_is_repeated_capability(parameter):
    '''Adds a boolean 'is_repeated_capability' to the parameter metadata by inferring it from its name, if not previously populated.'''
    if 'is_repeated_capability' not in parameter:
        parameter['is_repeated_capability'] = parameter['name'] in _repeated_capability_parameter_names


def add_all_function_metadata(functions, config):
    '''Adds all codegen-specific metada to the function metadata list'''
    for f in functions:
        _add_name(functions[f], f)
        _add_python_method_name(functions[f], f)
        _add_is_error_handling(functions[f])
        _add_has_repeated_capability(functions[f])
        for p in functions[f]['parameters']:
            _add_python_parameter_name(p)
            _add_python_type(p)
            _add_ctypes_variable_name(p)
            _add_ctypes_type(p)
            _add_buffer_info(p)
            _add_default_value_name(p)
            _add_default_value_name_for_docs(p, config['module_name'])
            _add_is_repeated_capability(p)
            _add_library_method_call_snippet(p, config['session_handle_parameter_name'])
    return functions


# Unit Tests
def _compare_values(actual, expected):
    if type(actual) is dict:
        _compare_dicts(actual, expected)
    elif type(actual) is list:
        _compare_lists(actual, expected)
    else:
        assert actual == expected, 'Value mismatch, {0} != {1}'.format(actual, expected)


def _compare_lists(actual, expected):
    assert type(actual) == type(expected), 'Type mismatch, {0} != {1}'.format(type(actual), type(expected))
    assert len(actual) == len(expected), 'Length mismatch, {0} != {1}'.format(len(actual), len(expected))
    for k in range(len(actual)):
        _compare_values(actual[k], expected[k])


def _compare_dicts(actual, expected):
    assert type(actual) == type(expected), 'Type mismatch, {0} != {1}'.format(type(actual), type(expected))
    for k in actual:
        assert k in expected, 'Key {0} not in expected'.format(k)
        _compare_values(actual[k], expected[k])
    for k in expected:
        assert k in actual, 'Key {0} not in actual'.format(k)


def _do_the_test_add_all_metadata(functions, expected):
    actual = copy.deepcopy(functions)
    actual = add_all_function_metadata(actual, {'session_handle_parameter_name': 'vi', 'module_name': 'nifake'})
    _compare_dicts(actual, expected)


def test_add_all_metadata_simple():
    functions = {
        'makeAFoo': {
            'codegen_method': 'public',
            'returns': 'ViStatus',
            'parameters': [
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'vi',
                    'type': 'ViSession',
                    'documentation': {
                        'description': 'Identifies a particular instrument session.',
                    },
                },
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'channelName',
                    'type': 'ViString',
                    'documentation': {
                        'description': 'The channel to call this on.',
                    },
                },
            ],
            'documentation': {
                'description': 'Performs a foo, and performs it well.',
            },
        },
        'makeAPrivateMethod': {
            'codegen_method': 'private',
            'returns': 'ViStatus',
            'parameters': [
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'vi',
                    'type': 'ViSession',
                    'documentation': {
                        'description': 'Identifies a particular instrument session.',
                    },
                },
                {
                    'direction': 'out',
                    'enum': None,
                    'name': 'status',
                    'type': 'ViString',
                    'documentation': {
                        'description': 'Return a device status',
                    },
                }
            ],
            'documentation': {
                'description': 'Perform actions as method defined',
            },
        },
    }
    expected = {
        'makeAFoo': {
            'name': 'makeAFoo',
            'codegen_method': 'public',
            'documentation': {
                'description': 'Performs a foo, and performs it well.'
            },
            'has_repeated_capability': True,
            'is_error_handling': False,
            'parameters': [
                {
                    'ctypes_type': 'ViSession',
                    'ctypes_variable_name': 'vi_ctype',
                    'ctypes_type_library_call': 'ViSession',
                    'direction': 'in',
                    'documentation': {
                        'description': 'Identifies a particular instrument session.'
                    },
                    'is_repeated_capability': False,
                    'enum': None,
                    'python_type': 'int',
                    'is_buffer': False,
                    'name': 'vi',
                    'python_name': 'vi',
                    'python_name_with_default': 'vi',
                    'python_name_with_doc_default': 'vi',
                    'size': {
                        'mechanism': 'fixed',
                        'value': 1
                    },
                    'type': 'ViSession',
                    'library_method_call_snippet': 'self._vi',
                },
                {
                    'ctypes_type': 'ViString',
                    'ctypes_variable_name': 'channel_name_ctype',
                    'ctypes_type_library_call': 'ViString',
                    'direction': 'in',
                    'documentation': {
                        'description': 'The channel to call this on.'
                    },
                    'is_repeated_capability': True,
                    'enum': None,
                    'python_type': 'str',
                    'is_buffer': False,
                    'name': 'channelName',
                    'python_name': 'channel_name',
                    'python_name_with_default': 'channel_name',
                    'python_name_with_doc_default': 'channel_name',
                    'size': {'mechanism': 'fixed', 'value': 1},
                    'type': 'ViString',
                    'library_method_call_snippet': 'self._repeated_capability.encode(\'ascii\')',
                },
            ],
            'python_name': 'make_a_foo',
            'returns': 'ViStatus',
            'returns_ctype': 'ViStatus_ctype',
            'returns_python': 'ViStatus'
        },
        'makeAPrivateMethod': {
            'codegen_method': 'private',
            'documentation': {
                'description': 'Perform actions as method defined'
            },
            'has_repeated_capability': False,
            'is_error_handling': False,
            'name': 'makeAPrivateMethod',
            'parameters': [
                {
                    'ctypes_type': 'ViSession_ctype',
                    'ctypes_type_library_call': 'ViSession_ctype',
                    'ctypes_variable_name': 'vi_ctype',
                    'direction': 'in',
                    'documentation': {
                        'description': 'Identifies a particular instrument session.'
                    },
                    'enum': None,
                    'intrinsic_type': 'int',
                    'is_buffer': False,
                    'is_repeated_capability': False,
                    'library_method_call_snippet': 'self._vi',
                    'name': 'vi',
                    'python_name': 'vi',
                    'python_name_with_default': 'vi',
                    'python_name_with_doc_default': 'vi',
                    'python_type': 'ViSession',
                    'size': {
                        'mechanism': 'fixed',
                        'value': 1
                    },
                    'type': 'ViSession'
                },
                {
                    'ctypes_type': 'ViString_ctype',
                    'ctypes_type_library_call': 'ViString_ctype',
                    'ctypes_variable_name': 'status_ctype',
                    'direction': 'out',
                    'documentation': {
                        'description': 'Return a device status'
                    },
                    'enum': None,
                    'intrinsic_type': 'str',
                    'is_buffer': False,
                    'is_repeated_capability': False,
                    'library_method_call_snippet': 'ctypes.pointer(status_ctype)',
                    'name': 'status',
                    'python_name': 'status',
                    'python_name_with_default': 'status',
                    'python_name_with_doc_default': 'status',
                    'python_type': 'ViString',
                    'size': {
                        'mechanism': 'fixed',
                        'value': 1
                    },
                    'type': 'ViString'
                }
            ],
            'python_name': '_make_a_private_method',
            'returns': 'ViStatus',
            'returns_ctype': 'ViStatus_ctype',
            'returns_python': 'ViStatus'
        }
    }

    _do_the_test_add_all_metadata(functions, expected)
