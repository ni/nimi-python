# This file was generated
<%
import build.helper as helper
config = template_parameters['metadata'].config
enums = config['enums']
%>
from enum import Enum
% for enum_name in sorted(enums):


class ${enum_name}(Enum):
    % for enum_value in enums[enum_name]['values']:
    % if type(enum_value['value']) is str:
    ${enum_value['name']} = '${enum_value['value']}'
    % else:
    ${enum_value['name']} = ${enum_value['value']}
    % endif
    % if 'description' in enum_value:
    '''
    ${helper.get_indented_docstring_snippet(enum_value['description'], indent=4)}
    '''
    % endif
    % endfor
% endfor
