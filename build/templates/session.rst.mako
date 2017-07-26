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


% for attr in sorted(attributes):
<% 
if attributes[attr]['enum'] is not None:
    t = 'enums.' + attributes[attr]['enum']
else:
    t = attributes[attr]["type"]
%>\
   :ivar ${t} ${attributes[attr]["name"].lower()}:
% endfor

% for attr in sorted(attributes):
%   if 'longDescription' in attributes[attr]:
   .. py:attribute:: ${attributes[attr]["name"].lower()}

%   if attributes[attr]['enum'] is not None:
      See :py:data:`${module_name}.${attributes[attr]['enum']}` 

%   endif
      ${helper.get_indented_docstring_snippet(attributes[attr]['longDescription'], indent=6)}

      .. note::
         This attribute corresponds to:

%   if 'lv_property' in attributes[attr]:
           - LV Property: **${attributes[attr]['lv_property'].strip()}**
%   endif
           - C Attribute: **${c_function_prefix.upper()}ATTR_${attributes[attr]["name"].upper()}**
%   endif

% endfor
