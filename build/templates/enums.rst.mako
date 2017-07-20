<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    enums = template_parameters['metadata'].enums
    enum_docs = template_parameters['metadata'].enum_docs
%>\
${helper.get_rst_header_snippet(driver_name + ' Enums', '=')}

Enums used in ${driver_name}

.. py:currentmodule:: ${module_name}

% for enum_name in sorted(enums):


.. py:data:: ${enum_name}
    % for enum_value in enums[enum_name]['values']:

   .. py:attribute:: ${enum_value['name']}
<%
enum_val_doc = None
lookup_name = enums[enum_name]['documentation_lookup'] if 'documentation_lookup' in enums[enum_name] else enum_name
val = enum_value['value']
if lookup_name is not None and val in enum_docs[lookup_name]:
    enum_val_doc = enum_docs[lookup_name][val]['description'].strip()
%>\

    % if enum_val_doc is not None:
      ${helper.get_indented_docstring_snippet(enum_val_doc, indent=6)}
    % endif
    % endfor
% endfor
