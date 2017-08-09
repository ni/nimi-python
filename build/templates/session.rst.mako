<%
    import build.helper as helper

    config        = template_parameters['metadata'].config
    attributes    = config['attributes']
    module_name = config['module_name']
    driver_name = config['driver_name']
    c_function_prefix = config['c_function_prefix']
%>\
${helper.get_rst_header_snippet(driver_name + ' Session', '=')}

.. py:module:: ${module_name}

.. py:class:: Session

   ${helper.get_indented_docstring_snippet(config['session_description'], indent=3)}

<%
table_contents = []
table_contents.append(('Name', 'Type'))
for attr in helper.sorted_attrs(attributes):
    if attributes[attr]['enum'] is not None:
        t = ':py:data:`' + attributes[attr]["enum"] + '`'
    else:
        t = attributes[attr]["type"]

    table_contents.append((':py:attr:`' + attributes[attr]["name"].lower() + '`', t))

table = helper.as_rest_table(table_contents, full=True)
%>\
   **Attributes**

   ${helper.get_indented_docstring_snippet(table, indent=3)}


