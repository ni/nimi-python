<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    c_function_prefix = config['c_function_prefix']
    attributes = config['attributes']
%>\
${helper.get_rst_header_snippet(module_name + '.Session properties', '=')}

.. py:currentmodule:: ${module_name}

% for attr in helper.sorted_attrs(attributes):
.. py:attribute:: ${attributes[attr]["name"].lower()}

<%
a = attributes[attr]
data_type = helper.get_intrinsic_type_from_visa_type(a['type'])
if attributes[attr]['enum'] is not None:
    data_type = ':py:data:`' + attributes[attr]["enum"] + '`'
table_contents = [
         ('Characteristic', 'Value'),
         ('Datatype', data_type),
         ('Permissions', a['access']),
         ('Channel Based', a['channel_based']),
         ('Resettable', a['resettable']),
         ]
table = helper.as_rest_table(table_contents)

desc = helper.get_documentation_for_node_rst(a, config, indent=0)
%>\
    ${helper.get_indented_docstring_snippet(desc, indent=4)}

    The following table lists the characteristics of this property.

    ${helper.get_indented_docstring_snippet(table, indent=4)}

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

%   if 'lv_property' in attributes[attr]:
            - LabVIEW Property: **${attributes[attr]['lv_property'].strip()}**
%   endif
            - C Attribute: **${c_function_prefix.upper()}ATTR_${attributes[attr]["name"].upper()}**

% endfor

