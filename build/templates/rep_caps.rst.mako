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
    The parameter can be an integer, a string, a list, a tuple, or slice (range).

    The recommended way of accessing repeated capabilities is with an integer :python:`[0]` or range :python:`[0:2]`.

% for rep_cap in config['repeated_capabilities']:
<%
name = rep_cap['python_name']
prefix = rep_cap['prefix']
%>\
${helper.get_rst_header_snippet(name, '-')}

    .. py:attribute:: ${module_name}.Session.${name}[]

        .. code:: python

            session.${name}[0].channel_enabled = True

        sets :py:attr:`channel_enabled` to :python:`True` for ${name} 0.

        .. code:: python

            session.${name}[0:2].channel_enabled = True
        
        sets :py:attr:`channel_enabled` to :python:`True` for ${name} 0, 1, 2.

        Note that :py:attr:`channel_enabled` is only used as an example and is not necessarily a property which
        supports this repeated capability. See documentation for individual properties and methods to
        learn what repeated capabilites they support, if any.

% endfor

