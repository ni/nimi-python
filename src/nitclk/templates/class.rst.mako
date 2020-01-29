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

.. py:module:: ${module_name}

${helper.get_rst_header_snippet('Public API', '=')}

The `nitclk` module provides synchronization facilites to allow multiple instruments to simultaneously
respond to triggers, to align Sample Clocks on multiple instruments, and/or to simultaneously start multiple
instruments.

It consists of a set of functions that act on a list of :py:class:`SessionReference` objects or nimi-python `Session`
objects for drivers that support NI-TClk. :py:class:`SessionReference` also has a set of properties for configuration.

.. code:: python

    with niscope.Session('dev1') as scope1, niscope.Session('dev2') as scope2:
        nitclk.configure_for_homogeneous_triggers([scope1, scope2])
        nitclk.initiate([scope1, scope2])
        wfm1 = scope1.fetch()
        wfm2 = scope2.fetch()

% for item in sorted(doc_list):
<%
function_item = doc_list[item]
%>\
${helper.get_rst_header_snippet(item, '-')}

    .. py:currentmodule:: ${module_name}

    ${helper.get_function_rst(function_item['function'], method_template=function_item['method_template'], numpy=False, config=config, indent=4, method_or_function='function')}

% endfor

${helper.get_rst_header_snippet('SessionReference', '=')}
.. py:currentmodule:: ${module_name}

.. py:class:: SessionReference(session_number)

    Helper class that contains all NI-TClk properties. This class is what is returned by
    any nimi-python Session class tclk attribute when the driver supports NI-TClk

    ..note:: Constructing this class is an advanced use case and should not be needed in most circumstances.

    :param session_number:
        nitclk session
    :type session_number: int, nimi-python Session class, SessionReference


% for attr in helper.sorted_attrs(attributes):
${helper.get_rst_header_snippet(attributes[attr]["python_name"], '-')}

    .. py:currentmodule:: ${module_name}.SessionReference

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

.. contents:: nitclk


