#!/usr/bin/python
# This file was generated
<%
enums = template_parameters['metadata'].enums
config = template_parameters['metadata'].config
module_name = config['module_name']
%>
% if len(enums) > 0:
from ${module_name}.enums import *          # noqa: F403,F401,H303
% endif
from ${module_name}.errors import DriverWarning   # noqa: F401
from ${module_name}.errors import Error     # noqa: F401
from ${module_name}.session import Session  # noqa: F401
<%
 # Blank lines are to make each import separate so that they do not need to be sorted
 # Otherwise flake8 test fails
%>\
% for c in config['custom_types']:

from ${module_name}.${c['file_name']} import ${c['python_name']}  # noqa: F401

from ${module_name}.${c['file_name']} import ${c['ctypes_type']}  # noqa: F401
% endfor

