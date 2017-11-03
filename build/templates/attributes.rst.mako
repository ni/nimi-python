<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    c_function_prefix = config['c_function_prefix']
    attributes = helper.filter_codegen_attributes(config['attributes'])
%>\
${helper.get_rst_header_snippet(module_name + '.Session properties', '=')}

.. py:currentmodule:: ${module_name}

% for attr in helper.sorted_attrs(attributes):
.. py:attribute:: ${attributes[attr]["python_name"]}

<%
a = attributes[attr]
data_type = helper.get_python_type_for_visa_type(a['type'])
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

rep_cap_attr_desc = '''
This property can use repeated capabilities (usually channels). If set or get directly on the 
{0}.Session object, then the set/get will use all repeated capabilities in the session. 
You can specify a subset of repeated capabilities using the Python index notation on an 
{0}.Session instance, and calling set/get value on the result.:

.. code:: python

    session['0,1'].{0} = var
    var = session['0,1'].{0}
'''

if a['channel_based'] == 'True':
    a['documentation']['tip'] = rep_cap_attr_desc.format(a["name"].lower())

desc = helper.get_documentation_for_node_rst(a, config, indent=0)
%>\
    ${helper.get_indented_docstring_snippet(desc, indent=4)}

    The following table lists the characteristics of this property.

    ${helper.get_indented_docstring_snippet(table, indent=4)}

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

%   if 'lv_property' in attributes[attr] and len(attributes[attr]['lv_property'].strip()) > 0:
            - LabVIEW Property: **${attributes[attr]['lv_property'].strip()}**
%   endif
            - C Attribute: **${c_function_prefix.upper()}ATTR_${attributes[attr]["name"].upper()}**

% endfor

