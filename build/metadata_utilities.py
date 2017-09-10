# Useful functions for use in the metadata modules

import build.helper
import copy
import pprint
import re

pp = pprint.PrettyPrinter(indent=4, width=80)

def merge_dicts(into, outof):
    '''merge_dicts

    Recursively merges the contents of dictionary 'outof' into dictionary 'into'.
    'into' may contain lists as values.
    'outof' may contain regular expressions as keys, in which case values are
    merged with all key matches in into.
    '''
    for item in sorted(outof):
        if type(outof[item]) is dict:
            if item in into:
                merge_dicts(into[item], outof[item])
            elif type(into) is list:
                for item2 in outof[item]:
                    into[item][item2] = outof[item][item2]
            else:
                # Handle regex in addon
                for item2 in into:
                    if re.search(item, item2):
                        assert type(into[item2]) is dict
                        merge_dicts(into[item2], outof[item])
        else:
            into[item] = outof[item]

# Functions to add information to metadata structures that are specific to our codegen needs.

def _add_python_method_name(function, name):
    '''Adds a python_name' key/value pair to the function metadata'''
    if function['codegen_method'] == 'private':
        function['python_name'] = '_' + build.helper.camelcase_to_snakecase(name)
    else:
        function['python_name'] = build.helper.camelcase_to_snakecase(name)
    return function

def _add_python_parameter_name(parameter):
    '''Adds a python_name' key/value pair to the parameter metadata'''
    parameter['python_name'] = build.helper.camelcase_to_snakecase(parameter['name'])
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
        parameter['intrinsic_type'] = build.helper.get_intrinsic_type_from_visa_type(parameter['type'])
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
        parameter['size'] = {'mechanism':'fixed','value':1}
        parameter['is_buffer'] = False
    return parameter

def add_all_metadata(functions):
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
    return functions

# Unit Tests

def _do_the_test_merge_dicts(a, b, expected):
    actual   = a.copy()
    merge_dicts(actual, b)
    assert expected == actual, "\na = {0}\nb = {1}\nexpected = {2}\nactual = {3}".format(a, b, expected, actual)

def test_merge_dict_second_is_empty():
    a        = {'a':1, 'b':2}
    b        = {}
    expected = {'a':1, 'b':2}
    _do_the_test_merge_dicts(a,b, expected)

def test_merge_dict_simple():
    a        = {'a':1, 'b':2}
    b        = {'c':3}
    expected = {'a':1, 'b':2, 'c':3}
    _do_the_test_merge_dicts(a,b, expected)

def test_merge_dict_first_is_empty():
    a        = {}
    b        = {'a':1, 'b':2}
    expected = {'a':1, 'b':2}
    _do_the_test_merge_dicts(a,b, expected)

def test_merge_dict_key_exists():
    a        = {'a':1, 'b':2}
    b        = {'b':3, 'c':4}
    expected = {'a':1, 'b':3, 'c':4}
    _do_the_test_merge_dicts(a,b, expected)

def test_merge_dict_recurse():
    a        = {'a':1, 'b':{'b1':5, 'b2':6}}
    b        = {'b':{'b3':7}, 'c':4}
    expected = {'a':1, 'b':{'b1':5, 'b2':6, 'b3':7}, 'c':4}
    _do_the_test_merge_dicts(a,b, expected)

def test_merge_dict_replace_in_list():
    a        = {'a':1, 'b':{'b1':5, 'b2':6}, 'c':['x', 'y', 'z']}
    b        = {'b':{'b3':7, 'b1':8}, 'c':{0:'r', 1:'s', 2:'t'}}
    expected = {'a':1, 'b':{'b1':8, 'b2':6, 'b3':7}, 'c':['r', 's', 't']}
    _do_the_test_merge_dicts(a,b, expected)

def test_merge_dict_replace_in_dict_and_list():
    a        = {'a':1, 'b':{'b1':2, 'b2':3}, 'c':['x', 'y', 'z']}
    b        = {'b':{'b3':7, 'b1':8}, 'c':{0:'r', 1:'s', 2:'t'}}
    expected = {'a':1, 'b':{'b1':8, 'b2':3, 'b3':7}, 'c':['r', 's', 't']}
    _do_the_test_merge_dicts(a,b, expected)

def test_merge_dict_with_regex():
    a        = {'aaa':{}, 'aaaa':{'x':98}, 'aaaaa':{}, 'bbb':{'bbb1':2, 'bbb2':3}, 'ccc':['x', 'y', 'z']}
    b        = {'a+':{'z':99}}
    expected = {'aaa':{'z':99}, 'aaaa':{'x':98, 'z':99}, 'aaaaa':{'z':99}, 'bbb':{'bbb1':2, 'bbb2':3}, 'ccc':['x', 'y', 'z']}
    _do_the_test_merge_dicts(a,b, expected)

def _do_the_test_add_all_metadata(functions, expected):
    actual = copy.deepcopy(functions)
    actual = add_all_metadata(actual)
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
                    'direction': 'in',
                    'documentation': {
                        'description': 'Identifies a particular instrument session.'
                    },
                    'enum': None,
                    'intrinsic_type': 'int',
                    'is_buffer': False,
                    'name': 'vi',
                    'python_name': 'vi',
                    'python_type': 'ViSession',
                    'size': {   'mechanism': 'fixed',
                                'value': 1},
                    'type': 'ViSession'
                }
            ],
            'python_name': 'close',
            'returns': 'ViStatus',
            'returns_ctype': 'ViStatus_ctype',
            'returns_python': 'ViStatus'
        }
    }

    _do_the_test_add_all_metadata(functions, expected)


