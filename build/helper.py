# TODO(marcoskirsch): This file should definitely not live here but I had trouble getting import to work.
# TODO(marcoskirsch): Figure out unit test for this.

import re

# Coding convention transformation functions.

# TODO(marcoskirsch): not being used
def  shoutcase_to_camelcase(shout_string):
    '''Converts a C-style SHOUT_CASE string to camelCase'''
    components = snake_string.split('_')
    return components[0].lower() + "".join(component.title() for component in components[1:])

def camelcase_to_snakecase(camelcase_string):
    '''Converts a camelCase string to lower_case_snake_case'''
    # https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camelcase_string)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def function_to_method_name(f):
    '''Returns an appropriate session method name for a given function'''
    # Method name is camelCase.
    # TODO(marcoskirsch): Some of these should be "_private" if user doesn't need to call directly.
    return f['name'][0].lower() + f['name'][1:]

# Filters

def extract_codegen_functions(functions):
    '''Returns function metadata only for those functions to be included in codegen'''
    return [x for x in functions if x['codegen_method'] is not 'no']

def extract_input_parameters(parameters):
    '''Returns list of parameters only with input parameters'''
    return [x for x in parameters if x['direction'] is 'in' and x['name'] is not 'vi']

def extract_output_parameters(parameters):
    '''Returns list of parameters only with output parameters'''
    return [x for x in parameters if x['direction'] is 'out']

def extract_enum_parameters(parameters):
    '''Returns a dictionary with information about the output parameters of a session method'''
    return [x for x in parameters if x['enum'] is not None]


# Functions to add information to metadata structures that are specific to our codegen needs.

def _add_python_method_name(function):
    '''Adds a python_name' key/value pair to the function metadata'''
    if function['codegen_method'] is 'private':
        function['python_name'] = '_' + camelcase_to_snakecase(function['name'])
    else:
        function['python_name'] = camelcase_to_snakecase(function['name'])
    return function

def _add_python_parameter_name(parameter):
    '''Adds a python_name' key/value pair to the parameter metadata'''
    parameter['python_name'] = camelcase_to_snakecase(parameter['name'])
    return parameter

def _add_python_type(parameter, types_map):
    '''Adds a python_type key/value pair to the parameter metadata'''
    if parameter['enum'] is None:
        parameter['python_type'] = types_map[parameter['type']]['python_type']
    else:
        parameter['python_type'] = 'enums.' + parameter['enum']
    return parameter

def _add_ctypes_variable_name(parameter):
    '''Adds a ctypes_variable_name key/value pair to the parameter metadata for a corresponding ctypes variable'''
    parameter['ctypes_variable_name'] = parameter['python_name'] + '_ctype'
    return parameter

def _add_ctypes_type(parameter, types_map):
    '''Adds a ctypes_type key/value pair to the parameter metadata for calling into the library'''
    # TODO(marcoskirsch): handle buffers and strings.
    parameter['ctypes_type'] = 'ctypes.' + types_map[parameter['type']]['ctypes_type']
    return parameter

def add_all_metadata(functions, types_map):
    '''Adds all codegen-specific metada to the function metadata list'''
    for f in functions:
        _add_python_method_name(f)
        for p in f['parameters']:
            _add_python_parameter_name(p)
            _add_python_type(p, types_map)
            _add_ctypes_variable_name(p)
            _add_ctypes_type(p, types_map)
    return functions


# Functions that return snippets that can be placed directly in the templates.

def get_method_parameters_snippet(parameters):
    '''Returns a string suitable for the parameter list of a method given a list of parameter objects'''
    snippet = 'self'
    for x in parameters:
        snippet += ', ' + x['python_name']
    return snippet

def get_library_call_parameter_snippet(parameters_list):
    '''Returns a string suitable to use as the parameters to the library object, i.e. "self, mode, range, digits_of_resolution"'''
    snippet = 'self.session_handle'
    for x in parameters_list:
        if x['name'] is not 'vi':
            if x['direction'] is 'in':
                snippet += (', ' + x['python_name'])
                snippet += '.value' if x['enum'] is not None else ''
                if x['type'] is 'ViConstString':
                    snippet += '.encode(\'ascii\')'
            else:
                assert x['direction'] is 'out'
                snippet += ', ctypes.byref(' + (x['ctypes_variable_name']) + ')'
    return snippet

def get_method_return_snippet(output_parameters):
    '''Returns a string suitable to use as the return argument of a Session method, i.e. "reading_ctype.value"'''
    if len(output_parameters) is 0:
        return 'return'
    snippet = 'return ' + output_parameters[0]['ctypes_variable_name'] + '.value'
    for x in output_parameters[1:]:
        snippet += ', ' + x['ctypes_variable_name'] + '.value'
    return snippet

def get_enum_type_check_snippet(parameter):
    '''Returns Python snippet to check that the type of a parameter is what is expected'''
    assert parameter['enum'] is not None
    assert parameter['direction'] is 'in'
    return 'if type(' + parameter['python_name'] + ') is not ' + parameter['python_type'] + ': raise TypeError(\'Parameter mode must be of type \' + str(' + parameter['python_type'] + '))'
