<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    driver_name = config['driver_name']
    c_function_prefix = config['c_function_prefix']

    functions_all = template_parameters['metadata'].functions
    functions = helper.filter_public_functions(functions_all)

    if 'context_manager_name' in config:
        # Add a InitiateDoc entry - only used to add initiate() to the Session documentation
        initiate_doc = helper.initiate_function_def_for_doc(functions_all, config)
        if initiate_doc is not None:
            functions['InitiateDoc'] = initiate_doc

    doc_list = {}
    for fname in sorted(functions):
        for method_template in functions[fname]['method_templates']:
            name =  functions[fname]['python_name'] + method_template['method_python_name_suffix']
            doc_list[name] = { 'filename': method_template['documentation_filename'], 'method_template': method_template, 'function': functions[fname], }

    attributes = helper.filter_codegen_attributes_public_only(config['attributes'])
%>\
${helper.get_rst_header_snippet(module_name + '.Session', '=')}

.. py:module:: ${module_name}

.. py:class:: SessionReference(session_number)

    Helper class that contains all NI-TClk properties. This class is what is returned by
    any nimi-python Session class tclk attribute when the driver supports NI-TClk

    .. code:: python

        with niscope.Session('dev1') as session:
            session.tclk.sample_clock_delay = .42

    :param session_number:
        nitclk session
    :type session_number: int, nimi-python Session class, SessionReference


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
    **Public functions**

    ${helper.get_indented_docstring_snippet(func_table, indent=4)}


${helper.get_rst_header_snippet('Properties', '-')}

% for attr in helper.sorted_attrs(attributes):
${helper.get_rst_header_snippet(attributes[attr]["python_name"], '~')}

    .. py:currentmodule:: ${module_name}

    .. py:function:: ${attributes[attr]["python_name"]}

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

${helper.get_rst_header_snippet('Functions', '-')}

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

