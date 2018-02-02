<%
    import build.helper as helper

    config        = template_parameters['metadata'].config
    attributes    = helper.filter_codegen_attributes(config['attributes'])
    functions     = helper.filter_codegen_functions(config['functions'])
    module_name   = config['module_name']
    driver_name   = config['driver_name']
    c_function_prefix = config['c_function_prefix']
%>\
${helper.get_rst_header_snippet(module_name + '.Session', '=')}

.. py:module:: ${module_name}

.. py:class:: Session

   ${helper.get_indented_docstring_snippet(config['session_class_description'], indent=3)}

<%
table_contents = []
table_contents.append(('Property', 'Datatype'))
for attr in helper.sorted_attrs(helper.filter_codegen_attributes(attributes)):
    if attributes[attr]['enum'] is not None:
        t = ':py:data:`' + attributes[attr]["enum"] + '`'
    else:
        t = attributes[attr]["python_type"]

    table_contents.append((':py:attr:`' + attributes[attr]["python_name"] + '`', t))

table = helper.as_rest_table(table_contents)
%>\
   **Properties**

   ${helper.get_indented_docstring_snippet(table, indent=3)}

<%
function_names = []
for f in sorted(functions):
    if functions[f]['codegen_method'] == 'public':
        name = functions[f]['python_name']
        for method_template in functions[f]['method_templates']:
            function_names.append('{0}{1}'.format(name, method_template['method_python_name_suffix']))

table_contents = []
table_contents.append(['Method name'])

for f in sorted(function_names):
    table_contents.append([':py:func:`{0}`'.format(f)])

table = helper.as_rest_table(table_contents)
%>\
   **Public methods**

   ${helper.get_indented_docstring_snippet(table, indent=3)}


