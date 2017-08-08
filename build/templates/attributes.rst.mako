<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    c_function_prefix = config['c_function_prefix']
    attributes = template_parameters['metadata'].attributes
%>\
${helper.get_rst_header_snippet(driver_name + ' Attributes', '=')}

.. py:currentmodule:: ${module_name}

% for attr in helper.sorted_attrs(attributes):
%   if 'longDescription' in attributes[attr]:
.. py:attribute:: ${attributes[attr]["name"].lower()}

%   if attributes[attr]['enum'] is not None:
   See :py:data:`${module_name}.${attributes[attr]['enum']}` 

%   endif
   ${helper.get_indented_docstring_snippet(attributes[attr]['longDescription'], indent=3)}

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

%   if 'lv_property' in attributes[attr]:
        - LabVIEW Property: **${attributes[attr]['lv_property'].strip()}**
%   endif
        - C Attribute: **${c_function_prefix.upper()}ATTR_${attributes[attr]["name"].upper()}**
%   endif

% endfor

