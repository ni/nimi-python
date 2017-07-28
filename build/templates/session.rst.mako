<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    c_function_prefix = config['c_function_prefix']
    attributes = template_parameters['metadata'].attributes
%>\
${helper.get_rst_header_snippet(driver_name + ' Session', '=')}

.. py:module:: ${module_name}

.. py:class:: Session

   ${helper.get_indented_docstring_snippet(config['session_description'], indent=3)}


% for attr in helper.sorted_attrs(attributes):
<% 
if attributes[attr]['enum'] is not None:
    t = 'enums.' + attributes[attr]['enum']
else:
    t = attributes[attr]["type"]
%>\
   :ivar ${t} ${attributes[attr]["name"].lower()}: 
      ${helper.get_indented_docstring_snippet(attributes[attr]['short_description'], indent=6)}
% endfor


