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

    # Add a CloseDoc entry - only used to add close() to the Session documentation
    close_doc = helper.close_function_def_for_doc(functions_all, config)
    if close_doc is not None:
        functions['CloseDoc'] = close_doc

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
.. py:module:: ${module_name}

${helper.get_rst_header_snippet('Session', '=')}

.. py:class:: Session(${init_method_params})

    ${helper.get_documentation_for_node_rst(init_function, config, indent=4)}

% for p in input_params:
    :param ${p['python_name']}:
        ${helper.get_documentation_for_node_rst(p, config, 8)}
    :type ${p['python_name']}: ${helper.format_type_for_rst_documentation(p, numpy, config)}

% endfor

${helper.get_rst_header_snippet('Methods', '=')}

% for item in sorted(doc_list):
<%
function_item = doc_list[item]
%>\
${helper.get_rst_header_snippet(item, '-')}

    .. py:currentmodule:: ${module_name}.Session

<%include file="${'/functions.rst' + function_item['filename'] + '.rst.mako'}" args="function=function_item['function'], config=config, method_template=function_item['method_template'], indent=8" />\

% endfor

% if len(config['repeated_capabilities']) > 0:
.. role:: c(code)
    :language: c

.. role:: python(code)
    :language: python

${helper.get_rst_header_snippet('Repeated Capabilities', '=')}

    Repeated capabilities attributes are used to set the `channel_string` parameter to the
    underlying driver function call. This can be the actual function based on the :py:class:`Session`
    method being called, or it can be the appropriate Get/Set Attribute function, such as :c:`${config['c_function_prefix']}SetAttributeViInt32()`.

    Repeated capbilities attributes use the indexing operator :python:`[]` to indicate the repeated capabilities.
    The parameter can be a string, list, tuple, or slice (range). Each element of those can be a string or
    an integer. If it is a string, you can indicate a range using the same format as the driver: :python:`'0-2'` or
    :python:`'0:2'`

    Some repeated capabilities use a prefix before the number and this is optional

% for rep_cap in config['repeated_capabilities']:
<%
name = rep_cap['python_name']
prefix = rep_cap['prefix']
%>\
${helper.get_rst_header_snippet(name, '-')}

    .. py:attribute:: ${module_name}.Session.${name}[]

% if len(prefix) > 0:
        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.${name}['0-2'].channel_enabled = True

        passes a string of :python:`'${prefix}0, ${prefix}1, ${prefix}2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

% endif
        .. code:: python

            session.${name}['${prefix}0-${prefix}2'].channel_enabled = True

        passes a string of :python:`'${prefix}0, ${prefix}1, ${prefix}2'` to the set attribute function.


% endfor
% endif

% if len(attributes) > 0:
${helper.get_rst_header_snippet('Properties', '=')}

% for attr in helper.sorted_attrs(attributes):
${helper.get_rst_header_snippet(attributes[attr]['python_name'], '-')}

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
% endif

.. contents:: Session


