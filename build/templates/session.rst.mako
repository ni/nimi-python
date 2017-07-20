<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    attributes = template_parameters['metadata'].attributes
    attribute_docs = helper.normalize_string_type(template_parameters['metadata'].attribute_docs)
%>\
${helper.get_rst_header_snippet(driver_name + ' Session', '=')}

.. py:module:: ${module_name}

.. py:class:: Session

   ${helper.get_indented_docstring_snippet(config['session_description'], indent=3)}


% for attr in sorted(attributes):
<% 
if attributes[attr]['enum'] is not None:
    t = 'enums.' + attributes[attr]['enum']
else:
    t = attributes[attr]["type"]
%>\
   :ivar ${t} ${attr.lower()}:
% endfor

% for attr in sorted(attributes):
%   if str(attributes[attr]['id']) in attribute_docs:
   .. py:attribute:: ${attr.lower()}

%   if attributes[attr]['enum'] is not None:
      See :py:data:`${module_name}.${attributes[attr]['enum']}` 

%   endif
      ${helper.get_indented_docstring_snippet(attribute_docs[str(attributes[attr]['id'])]['longDescription'], indent=6)}

%   endif
% endfor
