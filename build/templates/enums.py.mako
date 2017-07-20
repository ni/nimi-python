# This file was generated
<%
import build.helper as helper
enums = template_parameters['metadata'].enums
enum_docs = template_parameters['metadata'].enum_docs
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
<%
enum_val_doc = None
lookup_name = enums[enum_name]['documentation_lookup'] if 'documentation_lookup' in enums[enum_name] else enum_name
val = enum_value['value']
if lookup_name is not None and val in enum_docs[lookup_name]:
    enum_val_doc = enum_docs[lookup_name][val]['description'].strip()
%>\
    % if enum_val_doc is not None:
    '''
    ${helper.get_indented_docstring_snippet(enum_val_doc, indent=4)}
    '''
    % endif
    % endfor
% endfor
