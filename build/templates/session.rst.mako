<%
    import build.helper as helper

    config        = template_parameters['metadata'].config
    attributes    = config['attributes']
    functions     = config['functions']
    functions     = helper.filter_codegen_functions(functions)
    module_name = config['module_name']
    driver_name = config['driver_name']
    c_function_prefix = config['c_function_prefix']
%>\
${helper.get_rst_header_snippet(module_name + '.Session', '=')}

.. py:module:: ${module_name}

.. py:class:: Session

   ${helper.get_indented_docstring_snippet(config['session_class_description'], indent=3)}

<%
table_contents = []
table_contents.append(('Property', 'Datatype'))
for attr in helper.sorted_attrs(attributes):
    if attributes[attr]['enum'] is not None:
        t = ':py:data:`' + attributes[attr]["enum"] + '`'
    else:
        t = helper.get_python_type_for_visa_type(attributes[attr]["type"])

    table_contents.append((':py:attr:`' + attributes[attr]["name"].lower() + '`', t))

table = helper.as_rest_table(table_contents)
%>\
   **Properties**

   ${helper.get_indented_docstring_snippet(table, indent=3)}

<%
table_contents = []
for f in sorted(functions):
    if functions[f]['codegen_method'] == 'public':
        name = functions[f]['python_name']
        param_list = helper.get_params_snippet(functions[f], helper.ParameterUsageOptions.DOCUMENTATION_SESSION_METHOD)
        table_contents.append((':py:func:`{0}`'.format(name),))

table = helper.as_rest_table(table_contents)
%>\
   **Public methods**

   ${helper.get_indented_docstring_snippet(table, indent=3)}


