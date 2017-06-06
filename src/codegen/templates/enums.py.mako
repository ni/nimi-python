# This file was generated
<%
enums = template_parameters['metadata'].enums
%>

from enum import Enum

% for enum_name in enums:
class ${enum_name}(Enum):
    % for enum_value in enums[enum_name]:
    ${enum_value['name']} = ${enum_value['value']}
    % endfor

% endfor
