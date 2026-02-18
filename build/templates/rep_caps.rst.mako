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

    :py:class:`${module_name}.Session` supports "Repeated Capabilities", which are multiple instances of the same type of
    functionality. The repeated capabilities supported by :py:class:`${module_name}.Session` are:

% for rep_cap in config['repeated_capabilities']:
<%
name = rep_cap['python_name']
%>\
    #. ${name}_
% endfor

    Use the indexing operator :python:`[]` to indicate which repeated capability instance you are trying to access.
    The parameter can be a single element or an iterable that implements sequence semantics, such as list, tuple, range and slice.

    A single element will access one repeated capability.

    An iterable will access multiple repeated capabilites at once.

% for rep_cap in config['repeated_capabilities']:
<%
name = rep_cap['python_name']

single_index_snippet, single_index_explanation = helper.get_repeated_capability_single_index_python_example(rep_cap)
tuple_index_snippet, tuple_index_explanation = helper.get_repeated_capability_tuple_index_python_example(rep_cap)

%>\
${helper.get_rst_header_snippet(name, '-')}

    .. py:attribute:: ${module_name}.Session.${name}[]

        ${helper.get_repeated_capability_element_recommendation(rep_cap)}

        .. code:: python

            ${single_index_snippet}

        ${single_index_explanation}

        .. code:: python

            ${tuple_index_snippet}

        ${tuple_index_explanation}

% endfor

