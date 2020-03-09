# This file was generated
<%
import build.helper as helper
config = template_parameters['metadata'].config
enums = config['enums']
%>
from enum import Enum
% for enum_name in sorted(helper.filter_codegen_enums(enums)):


class ${enums[enum_name]['python_name']}(Enum):
    % for enum_value in enums[enum_name]['values']:
    % if type(enum_value['value']) is str:
    ${enum_value['python_name']} = '${enum_value['value']}'
    % else:
    ${enum_value['python_name']} = ${enum_value['value']}
    % endif
    % if 'documentation' in enum_value and len(helper.get_documentation_for_node_docstring(enum_value, config, indent=4).strip()) > 0:
    '''
    ${helper.get_documentation_for_node_docstring(enum_value, config, indent=4)}
    '''
    % endif
    % endfor
% endfor
