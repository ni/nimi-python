<%
    import build.helper as helper

    config = template_parameters['metadata'].config
    module_name = config['module_name']
    c_function_prefix = config['c_function_prefix']

%>\
.. py:module:: ${module_name}
    :noindex:

.. py:currentmodule:: ${module_name}.Session

.. role:: c(code)
    :language: c

.. role:: python(code)
    :language: python

${helper.get_rst_header_snippet('Repeated Capabilities', '=')}

    Repeated capabilities attributes are used to set the `channel_string` parameter to the
    underlying driver function call. This can be the actual function based on the :py:class:`Session`
    method being called, or it can be the appropriate Get/Set Attribute function, such as :c:`${config['c_function_prefix']}SetAttributeViInt32()`.

    Repeated capabilities attributes use the indexing operator :python:`[]` to indicate the repeated capabilities.
    The parameter can be a string, list, tuple, or slice (range). Each element of those can be a string or
    an integer. If it is a string, you can indicate a range using the same format as the driver: :python:`'0-2'` or
    :python:`'0:2'`

    Some repeated capabilities use a prefix before the number and this is optional

% for rep_cap in config['repeated_capabilities']:
<%
name = rep_cap['python_name']
rep_cap_doc = rep_cap['documentation']
%>\
${helper.get_rst_header_snippet(name, '-')}

    .. py:attribute:: ${module_name}.Session.${name}[]

% if rep_cap_doc['description']:
    ${rep_cap_doc['description'].replace('\n', '\n        ')}

% endif
% if rep_cap_doc['valid_identifiers']:
        Valid identifiers: :python:`'${", ".join(rep_cap_doc["valid_identifiers"])}'`.

% endif
% for example in rep_cap_doc['examples']:
        .. code:: python

            ${example.split('\n\n', 1)[0].replace('\n', '\n            ')}

% if '\n\n' in example:
        ${example.split('\n\n', 1)[1].replace('\n', '\n        ')}

% endif
% endfor
% endfor
