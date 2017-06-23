# This file was generated
<%
enums = template_parameters['metadata'].enums
%>

from enum import Enum

% for enum_name in enums:
class ${enum_name}(Enum):
    % for enum_value in enums[enum_name]:
    % if type(enum_value['value']) is str:
    ${enum_value['name']} = '${enum_value['value']}'
    % else:
    ${enum_value['name']} = ${enum_value['value']}
    % endif
    % endfor

% endfor
