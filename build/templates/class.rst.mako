<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    c_function_prefix = config['c_function_prefix']

    functions = template_parameters['metadata'].functions
    functions = helper.filter_public_functions(functions)

    # Add a CloseDoc entry - only used to add close() to the Session documentation
    functions['CloseDoc'] = helper.close_function_def_for_doc(functions)

    doc_list = {}
    for fname in sorted(functions):
        for method_template in functions[fname]['method_templates']:
            name =  functions[fname]['python_name'] + method_template['method_python_name_suffix']
            doc_list[name] = { 'filename': method_template['documentation_filename'], 'method_template': method_template, 'function': functions[fname], }

    attributes = helper.filter_codegen_attributes_public_only(config['attributes'])

    init_function = config['functions']['_init_function']
    init_method_params = helper.get_params_snippet(init_function, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)
    constructor_params = helper.filter_parameters(init_function, helper.ParameterUsageOptions.SESSION_INIT_DECLARATION)
    input_params = helper.filter_parameters(init_function, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)
%>\
${helper.get_rst_header_snippet(module_name + '.Session', '=')}

.. py:module:: ${module_name}

.. py:class:: Session(${init_method_params})

    ${helper.get_documentation_for_node_rst(init_function, config, indent=4)}

% for p in input_params:
    :param ${p['python_name']}:
        ${helper.get_documentation_for_node_rst(p, config, 8)}
    :type ${p['python_name']}: ${helper.format_type_for_rst_documentation(p, numpy, config)}

% endfor

<%
table_contents = []
table_contents.append(('Property', 'Datatype'))
for attr in helper.sorted_attrs(helper.filter_codegen_attributes_public_only(attributes)):
    if attributes[attr]['enum'] is not None:
        t = ':py:data:`' + attributes[attr]["enum"] + '`'
    else:
        t = attributes[attr]["type_in_documentation"]

    table_contents.append((':py:attr:`' + attributes[attr]["python_name"] + '`', t))

attr_table = helper.as_rest_table(table_contents)
%>\
    **Properties**

    ${helper.get_indented_docstring_snippet(attr_table, indent=4)}

<%
function_names = []
for f in sorted(functions):
    name = functions[f]['python_name']
    for method_template in functions[f]['method_templates']:
        function_names.append('{0}{1}'.format(name, method_template['method_python_name_suffix']))

table_contents = []
table_contents.append(['Method name'])

for f in sorted(function_names):
    table_contents.append([':py:func:`{0}`'.format(f)])

func_table = helper.as_rest_table(table_contents)
%>\
    **Public methods**

    ${helper.get_indented_docstring_snippet(func_table, indent=4)}


${helper.get_rst_header_snippet('Properties', '-')}

% for attr in helper.sorted_attrs(attributes):
${helper.get_rst_header_snippet(attributes[attr]["python_name"], '~')}

    .. py:currentmodule:: ${module_name}.Session

    .. py:attribute:: ${attributes[attr]["python_name"]}

<%
a = attributes[attr]
table_contents = [
         ('Characteristic', 'Value'),
         ('Datatype', a['type_in_documentation']),
         ('Permissions', a['access']),
         ('Channel Based', 'Yes' if a['channel_based'] else 'No'),
         ('Resettable', 'Yes' if a['resettable'] else 'No'),
         ]
table = helper.as_rest_table(table_contents)

helper.add_attribute_rep_cap_tip_rst(a, config)

desc = helper.get_documentation_for_node_rst(a, config, indent=0)
%>\
        ${helper.get_indented_docstring_snippet(desc, indent=8)}

        The following table lists the characteristics of this property.

            ${helper.get_indented_docstring_snippet(table, indent=12)}

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

%   if 'lv_property' in attributes[attr] and len(attributes[attr]['lv_property']) > 0:
                - LabVIEW Property: **${attributes[attr]['lv_property'].strip()}**
%   endif
                - C Attribute: **${c_function_prefix.upper()}ATTR_${attributes[attr]["name"].upper()}**

% endfor

${helper.get_rst_header_snippet('Methods', '-')}


% for item in sorted(doc_list):
<%
function_item = doc_list[item]
%>\
${helper.get_rst_header_snippet(item, '~')}

    .. py:currentmodule:: ${module_name}.Session

<%include file="${'/functions.rst' + function_item['filename'] + '.rst.mako'}" args="function=function_item['function'], config=config, method_template=function_item['method_template'], indent=8" />\

% endfor


${helper.get_rst_header_snippet('Properties', '-')}

<%
table_contents = []
table_contents.append(('Property', 'Datatype'))
for attr in helper.sorted_attrs(helper.filter_codegen_attributes_public_only(attributes)):
    if attributes[attr]['enum'] is not None:
        t = ':py:data:`' + attributes[attr]["enum"] + '`'
    else:
        t = attributes[attr]["type_in_documentation"]

    table_contents.append((':py:attr:`' + module_name + '.Session.' + attributes[attr]["python_name"] + '`', t))

attr_table = helper.as_rest_table(table_contents)
%>\
${helper.get_indented_docstring_snippet(attr_table, indent=0)}

${helper.get_rst_header_snippet('Methods', '-')}

<%
function_names = []
for f in sorted(functions):
    name = functions[f]['python_name']
    for method_template in functions[f]['method_templates']:
        function_names.append('{0}{1}'.format(name, method_template['method_python_name_suffix']))

table_contents = []
table_contents.append(['Method name'])

for f in sorted(function_names):
    table_contents.append([':py:func:`{0}.Session.{1}`'.format(module_name, f)])

func_table = helper.as_rest_table(table_contents)
%>\
${helper.get_indented_docstring_snippet(func_table, indent=0)}

