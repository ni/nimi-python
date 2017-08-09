<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    c_function_prefix = config['c_function_prefix']
    attributes = config['attributes']
%>\
${helper.get_rst_header_snippet(driver_name + ' Attributes', '=')}

.. py:currentmodule:: ${module_name}

% for attr in helper.sorted_attrs(attributes):
.. py:attribute:: ${attributes[attr]["name"].lower()}

<%
a = attributes[attr]
data_type = helper.get_python_type_from_visa_type(a['type'])
if attributes[attr]['enum'] is not None:
    data_type = ':py:data:`' + attributes[attr]["enum"] + '`'
table_contents = [
         ('Characteristic', 'Value'),
         ('Datatype', data_type),
         ('Permissions', a['access']),
         ('Channel Based', a['channel_based']),
         ('Resettable', a['resettable']),
         ]
table = helper.as_rest_table(table_contents, full=True)

desc = a['long_description'] if 'long_description' in a else a['short_description']
%>\
   ${helper.get_indented_docstring_snippet(desc, indent=3)}

   The following table lists the characteristics of this property.

   ${helper.get_indented_docstring_snippet(table, indent=3)}

   .. tip:: 
      This attribute corresponds to the following LabVIEW Property or C Attribute:

%   if 'lv_property' in attributes[attr]:
        - LabVIEW Property: **${attributes[attr]['lv_property'].strip()}**
%   endif
        - C Attribute: **${c_function_prefix.upper()}ATTR_${attributes[attr]["name"].upper()}**

% endfor

