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
    The parameter can be a single element or an iterable that implements sequence semantics, like list, tuple, range and slice.

    The recommended way of accessing a single repeated capability is with an integer :python:`[0]` for capabilities that support it and a string :python:`['Dev1']`
    for those that don't support integers.

    The recommended way of accessing multiple repeated capabilites at once is with a tuple (:python:`[0, 1]` or :python:`['Dev1', 'Dev2']`) or slice :python:`[0:2]`.

% for rep_cap in config['repeated_capabilities']:
<%
name = rep_cap['python_name']

single_index_snippet, single_index_explanation = helper.get_repeated_capability_single_index_python_example(rep_cap)
tuple_index_snippet, tuple_index_explanation = helper.get_repeated_capability_tuple_index_python_example(rep_cap)

%>\
${helper.get_rst_header_snippet(name, '-')}

    .. py:attribute:: ${module_name}.Session.${name}[]

        .. code:: python

            ${single_index_snippet}

        ${single_index_explanation}

        .. code:: python

            ${tuple_index_snippet}

        ${tuple_index_explanation}

% endfor

