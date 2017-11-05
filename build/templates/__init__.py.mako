#!/usr/bin/python
# This file was generated
<%
enums = template_parameters['metadata'].enums
config = template_parameters['metadata'].config
module_name = config['module_name']
module_name_class = module_name.title()
%>
% if len(enums) > 0:
from ${module_name}.enums import *          # noqa: F403,F401,H303
% endif
from ${module_name}.errors import Error     # noqa: F401
from ${module_name}.errors import ${module_name_class}Warning   # noqa: F401
from ${module_name}.session import Session  # noqa: F401
% for c in config['custom_types']:

from ${module_name}.${c['file_name']} import ${c['python_name']}  # noqa: F401
from ${module_name}.${c['file_name']} import ${c['ctypes_name']}  # noqa: F401
% endfor

