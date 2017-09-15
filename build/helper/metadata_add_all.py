# Useful functions for use in the metadata modules

from .helper import camelcase_to_snakecase
from .helper import get_intrinsic_type_from_visa_type

import copy
import pprint

pp = pprint.PrettyPrinter(indent=4, width=80)

# Functions to add information to metadata structures that are specific to our codegen needs.


def _add_python_method_name(function, name):
    '''Adds a python_name' key/value pair to the function metadata'''
    if function['codegen_method'] == 'private':
        function['python_name'] = '_' + camelcase_to_snakecase(name)
    else:
        function['python_name'] = camelcase_to_snakecase(name)
    return function


def _add_python_parameter_name(parameter):
    '''Adds a python_name' key/value pair to the parameter metadata'''
    parameter['python_name'] = camelcase_to_snakecase(parameter['name'])
    return parameter


def _add_python_type(parameter):
    '''Adds a python_type key/value pair to the parameter metadata'''
    if parameter['enum'] is None:
        parameter['python_type'] = parameter['type']
    else:
        parameter['python_type'] = 'enums.' + parameter['enum']
    return parameter


def _add_intrinsic_type(parameter):
    '''Adds a intrinsic (basic python type) key/value pair to the parameter metadata'''
    if parameter['enum'] is None:
        parameter['intrinsic_type'] = get_intrinsic_type_from_visa_type(parameter['type'])
    else:
        parameter['intrinsic_type'] = parameter['python_type']
    return parameter


def _add_ctypes_variable_name(parameter):
    '''Adds a ctypes_variable_name key/value pair to the parameter metadata for a corresponding ctypes variable'''
    parameter['ctypes_variable_name'] = parameter['python_name'] + '_ctype'
    return parameter


def _add_ctypes_type(parameter):
    '''Adds a ctypes_type key/value pair to the parameter metadata for calling into the library'''
    parameter['ctypes_type'] = parameter['type'] + '_ctype'
    if parameter['direction'] == 'out':
        if parameter['type'] == 'ViString' or parameter['type'] == 'ViRsrc' or parameter['type'] == 'ViConstString':
            # These are defined as c_char_p which is already a pointer!
            parameter['ctypes_type_library_call'] = parameter['ctypes_type']
        else:
            parameter['ctypes_type_library_call'] = "ctypes.POINTER(" + parameter['ctypes_type'] + ")"
    else:
        parameter['ctypes_type_library_call'] = parameter['ctypes_type']

    return parameter


def _add_ctypes_return_type(f):
    '''Adds the ctypes_type key/value pair to the function metadata for the return type'''
    f['returns_ctype'] = f['returns'] + '_ctype'
    return f


def _add_python_return_type(f):
    '''Adds the ctypes_type key/value pair to the function metadata for the return type'''
    f['returns_python'] = f['returns']
    return f


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


def _add_library_call_name(parameter, session_name):
    if parameter['direction'] == 'in':
        if parameter['name'] == session_name:
            library_call_name = 'self.' + session_name
        else:
            library_call_name = parameter['python_name']
            library_call_name += '.value' if parameter['enum'] is not None else ''
            if parameter['type'] == 'ViString' or parameter['type'] == 'ViConstString' or parameter['type'] == 'ViRsrc':
                library_call_name += '.encode(\'ascii\')'
    else:
        assert parameter['direction'] == 'out', pp.pformat(parameter)
        if parameter['size']['mechanism'] == 'ivi-dance':
            library_call_name = parameter['ctypes_variable_name']
        elif parameter['is_buffer']:
            library_call_name = 'ctypes.cast(' + parameter['ctypes_variable_name'] + ', ctypes.POINTER(ctypes_types.' + parameter['ctypes_type'] + '))'
        else:
            library_call_name = 'ctypes.pointer(' + (parameter['ctypes_variable_name']) + ')'
    parameter['library_call_name'] = library_call_name


def _add_default_value_name(parameter):
    '''Declaration with default value, if set'''
    if 'default_value' in parameter:
        if type(parameter['default_value']) is str:
            name = parameter['python_name'] + "='" + parameter['default_value'] + "'"
        else:
            name = parameter['python_name'] + "=" + str(parameter['default_value'])
    else:
        name = parameter['python_name']

    parameter['name_with_default'] = name


def add_all_function_metadata(functions, config):
    '''Adds all codegen-specific metada to the function metadata list'''
    for f in functions:
        _add_python_method_name(functions[f], f)
        _add_ctypes_return_type(functions[f])
        _add_python_return_type(functions[f])
        _add_is_error_handling(functions[f])
        for p in functions[f]['parameters']:
            _add_python_parameter_name(p)
            _add_python_type(p)
            _add_intrinsic_type(p)
            _add_ctypes_variable_name(p)
            _add_ctypes_type(p)
            _add_buffer_info(p)
            _add_library_call_name(p, config['session_handle_parameter_name'])
            _add_default_value_name(p)
    return functions


# Unit Tests
def _do_the_test_add_all_metadata(functions, expected):
    actual = copy.deepcopy(functions)
    actual = add_all_function_metadata(actual, {'session_handle_parameter_name': 'vi'})
    assert expected == actual, "\nfunctions = {0}\nexpected = {1}\nactual = {2}".format(pp.pformat(functions), pp.pformat(expected), pp.pformat(actual))


def test_add_all_metadata_simple():
    functions = {
        'close': {
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
            ],
            'documentation': {
                'description': 'Closes the specified session and deallocates resources that it reserved.',
            },
        },
    }
    expected = {
        'close': {
            'codegen_method': 'public',
            'documentation': {
                'description': 'Closes the specified session and deallocates resources that it reserved.'
            },
            'is_error_handling': False,
            'parameters': [
                {
                    'ctypes_type': 'ViSession_ctype',
                    'ctypes_variable_name': 'vi_ctype',
                    'ctypes_type_library_call': 'ViSession_ctype',
                    'direction': 'in',
                    'documentation': {
                        'description': 'Identifies a particular instrument session.'
                    },
                    'enum': None,
                    'intrinsic_type': 'int',
                    'is_buffer': False,
                    'name': 'vi',
                    'name_with_default': 'vi',
                    'python_name': 'vi',
                    'python_type': 'ViSession',
                    'size': {
                        'mechanism': 'fixed',
                        'value': 1
                    },
                    'type': 'ViSession',
                    'library_call_name': 'self.vi',
                }
            ],
            'python_name': 'close',
            'returns': 'ViStatus',
            'returns_ctype': 'ViStatus_ctype',
            'returns_python': 'ViStatus'
        }
    }

    _do_the_test_add_all_metadata(functions, expected)


