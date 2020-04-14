.. py:module:: nidigital
    :noindex:

.. py:currentmodule:: nidigital.Session

.. role:: c(code)
    :language: c

.. role:: python(code)
    :language: python

Repeated Capabilities
=====================

    Repeated capabilities attributes are used to set the `channel_string` parameter to the
    underlying driver function call. This can be the actual function based on the :py:class:`Session`
    method being called, or it can be the appropriate Get/Set Attribute function, such as :c:`niDigital_SetAttributeViInt32()`.

    Repeated capabilities attributes use the indexing operator :python:`[]` to indicate the repeated capabilities.
    The parameter can be a string, list, tuple, or slice (range). Each element of those can be a string or
    an integer. If it is a string, you can indicate a range using the same format as the driver: :python:`'0-2'` or
    :python:`'0:2'`

    Some repeated capabilities use a prefix before the number and this is optional

channels
--------

    .. py:attribute:: nidigital.Session.channels[]

        .. code:: python

            session.channels['0-2'].channel_enabled = True

        passes a string of :python:`'0, 1, 2'` to the set attribute function.


pins
----

    .. py:attribute:: nidigital.Session.pins[]

        .. code:: python

            session.pins['0-2'].channel_enabled = True

        passes a string of :python:`'0, 1, 2'` to the set attribute function.


instruments
-----------

    .. py:attribute:: nidigital.Session.instruments[]

        .. code:: python

            session.instruments['0-2'].channel_enabled = True

        passes a string of :python:`'0, 1, 2'` to the set attribute function.


pattern_opcode_events
---------------------

    .. py:attribute:: nidigital.Session.pattern_opcode_events[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.pattern_opcode_events['0-2'].channel_enabled = True

        passes a string of :python:`'patternOpcodeEvent0, patternOpcodeEvent1, patternOpcodeEvent2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.pattern_opcode_events['patternOpcodeEvent0-patternOpcodeEvent2'].channel_enabled = True

        passes a string of :python:`'patternOpcodeEvent0, patternOpcodeEvent1, patternOpcodeEvent2'` to the set attribute function.


conditional_jump_triggers
-------------------------

    .. py:attribute:: nidigital.Session.conditional_jump_triggers[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.conditional_jump_triggers['0-2'].channel_enabled = True

        passes a string of :python:`'conditionalJumpTrigger0, conditionalJumpTrigger1, conditionalJumpTrigger2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.conditional_jump_triggers['conditionalJumpTrigger0-conditionalJumpTrigger2'].channel_enabled = True

        passes a string of :python:`'conditionalJumpTrigger0, conditionalJumpTrigger1, conditionalJumpTrigger2'` to the set attribute function.


sites
-----

    .. py:attribute:: nidigital.Session.sites[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.sites['0-2'].channel_enabled = True

        passes a string of :python:`'site0, site1, site2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.sites['site0-site2'].channel_enabled = True

        passes a string of :python:`'site0, site1, site2'` to the set attribute function.



