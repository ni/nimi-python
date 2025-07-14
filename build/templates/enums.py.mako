${template_parameters['encoding_tag']}
# This file was generated
<%
import build.helper as helper
config = template_parameters['metadata'].config
enums = config['enums']
%>
from enum import Enum
% if any(enums[e].get('enum_class', 'Enum') == 'IntFlag' for e in enums):
from enum import IntFlag
% endif
% for enum_name in sorted(helper.filter_codegen_enums(enums)):


class ${enums[enum_name]['python_name']}(${enums[enum_name].get('enum_class', 'Enum')}):
<%
    print_list = []
%>\
    % for enum_value in enums[enum_name]['values']:
    % if type(enum_value['value']) is str:
    ${enum_value['python_name']} = '${enum_value['value']}'
    % else:
    ${enum_value['python_name']} = ${enum_value['value']}
    % endif
    % if 'documentation' in enum_value and len(helper.get_documentation_for_node_docstring(enum_value, config, indent=4).strip()) > 0:
    r'''
    ${helper.get_documentation_for_node_docstring(enum_value, config, indent=4)}
    '''
    % endif
<%
if 'pretty_name' in enum_value:
    print_list.append(enum_value)
%>\
    % endfor
    % if print_list:

    def __str__(self):
        return {
    % for enum_value in print_list:
            '${enum_value['python_name']}': '${enum_value['pretty_name']}',
    % endfor
        }.get(self.name, self.name)
    % endif
% endfor
