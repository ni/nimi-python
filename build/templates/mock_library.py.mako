# This file was generated
<%
functions     = template_parameters['metadata'].functions
attributes    = template_parameters['metadata'].attributes
config        = template_parameters['metadata'].config
types         = template_parameters['types']

module_name = config['module_name']
c_function_prefix = config['c_function_prefix']
driver_name = config['driver_name']
%>

import ctypes
from unittest.mock import DEFAULT
import pprint
from ctypes import *
pp = pprint.PrettyPrinter(indent=4)

# Create side effect functions for all entry points that take byref/pointer parameters
% for f in functions:
<% params = f['parameters']
 has_pointer = (len([x['direction'] for x in params if x['direction'] == 'out']) > 0)
%>\
% if has_pointer:
<%
    param_list = ''
    for p in f['parameters']:
        if len(param_list) > 0:
            param_list += ', '
        param_list += p['name']
%>
def ${c_function_prefix}${f['name']}_side_effect(${param_list}):
%    for p in f['parameters']:
%        if p['direction'] == 'out':
    ${p['name']}.contents.value = ${p['default_for_test']}
%        endif
%    endfor
    return DEFAULT
% endif
% endfor

# Helper function to setup Mock object with default side affects and return values
def set_side_effects_and_return_values(mock_library):
% for f in functions:
<% params = f['parameters']
 has_pointer = (len([x['direction'] for x in params if x['direction'] == 'out']) > 0)
%>\
% if has_pointer:
    mock_library.${c_function_prefix}${f['name']}.side_effect = ${c_function_prefix}${f['name']}_side_effect
% endif
    mock_library.${c_function_prefix}${f['name']}.return_value = 0
% endfor




