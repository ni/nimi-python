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
    an integer.

    The recommended way of accessing repeated capabilities is with an integer :python:`[0]` or range :python:`[0:2]`.

% for rep_cap in config['repeated_capabilities']:
<%
name = rep_cap['python_name']
prefix = rep_cap['prefix']
%>\
${helper.get_rst_header_snippet(name, '-')}

    .. py:attribute:: ${module_name}.Session.${name}[]

% if len(prefix) > 0:
        ..
            If no prefix is added to the items in the parameter, the correct prefix will be added when
            the driver function call is made.

            .. code:: python

                session.${name}['0-2'].channel_enabled = True

            passes a string of :python:`'${prefix}0, ${prefix}1, ${prefix}2'` to the set attribute function.

            If an invalid repeated capability is passed to the driver, the driver will return an error.

            You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
            for the specific repeated capability.

            .. code:: python

                session.${name}['${prefix}0-${prefix}2'].channel_enabled = True

            passes a string of :python:`'${prefix}0, ${prefix}1, ${prefix}2'` to the set attribute function.

% endif
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

