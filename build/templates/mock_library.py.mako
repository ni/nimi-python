# This file was generated
<%
import helper

functions     = template_parameters['metadata'].functions
attributes    = template_parameters['metadata'].attributes
config        = template_parameters['metadata'].config

module_name = config['module_name']
c_function_prefix = config['c_function_prefix']
driver_name = config['driver_name']

functions = template_parameters['metadata'].functions
functions = helper.extract_codegen_functions(functions)
functions = helper.add_all_metadata(functions)
%>\

import ctypes
from unittest.mock import DEFAULT
import ${module_name}.ctypes_types
import ${module_name}.python_types

# Create side effect functions for all entry points that take byref/pointer parameters
% for f in functions:
<% 
params = f['parameters']
output_params = helper.extract_output_parameters(params)
%>\
% if len(output_params) > 0:
def ${c_function_prefix}${f['name']}_side_effect(${helper.get_function_parameters_snippet(params)}):
%    for p in output_params:
    ${p['python_name']}.contents.value = ${p['default_for_test']}
%    endfor
    return DEFAULT

% endif
% endfor

# Helper function to setup Mock object with default side affects and return values
def set_side_effects_and_return_values(mock_library):
% for f in functions:
<% 
params = f['parameters']
output_params = helper.extract_output_parameters(params)
%>\
% if len(output_params) > 0:
    mock_library.${c_function_prefix}${f['name']}.side_effect = ${c_function_prefix}${f['name']}_side_effect
% endif
    mock_library.${c_function_prefix}${f['name']}.return_value = ${module_name}.python_types.${f['returns_python']}(0)
% endfor




