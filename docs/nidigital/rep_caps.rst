.. py:module:: nidigital
    :noindex:

.. py:currentmodule:: nidigital.Session

.. role:: c(code)
    :language: c

.. role:: python(code)
    :language: python

Repeated Capabilities
=====================

    :py:class:`nidigital.Session` supports "Repeated Capabilities", which are multiple instances of the same type of
    functionality. The repeated capabilities supported by :py:class:`nidigital.Session` are:

    #. channels_
    #. pins_
    #. instruments_
    #. pattern_opcode_events_
    #. conditional_jump_triggers_
    #. sites_
    #. rio_events_
    #. rio_triggers_

    Use the indexing operator :python:`[]` to indicate which repeated capability instance you are trying to access.
    The parameter can be an integer, a string, a list, a tuple, or slice (range).

    The recommended way of accessing repeated capabilities is with an integer :python:`[0]` or range :python:`[0:2]`.

channels
--------

    .. py:attribute:: nidigital.Session.channels[]

        .. code:: python

            session.channels[0].channel_enabled = True

        sets :py:attr:`channel_enabled` to :python:`True` for channels 0.

        .. code:: python

            session.channels[0:2].channel_enabled = True
        
        sets :py:attr:`channel_enabled` to :python:`True` for channels 0, 1, 2.

        Note that :py:attr:`channel_enabled` is only used as an example and is not necessarily a property which
        supports this repeated capability. See documentation for individual properties and methods to
        learn what repeated capabilites they support, if any.

pins
----

    .. py:attribute:: nidigital.Session.pins[]

        .. code:: python

            session.pins[0].channel_enabled = True

        sets :py:attr:`channel_enabled` to :python:`True` for pins 0.

        .. code:: python

            session.pins[0:2].channel_enabled = True
        
        sets :py:attr:`channel_enabled` to :python:`True` for pins 0, 1, 2.

        Note that :py:attr:`channel_enabled` is only used as an example and is not necessarily a property which
        supports this repeated capability. See documentation for individual properties and methods to
        learn what repeated capabilites they support, if any.

instruments
-----------

    .. py:attribute:: nidigital.Session.instruments[]

        .. code:: python

            session.instruments[0].channel_enabled = True

        sets :py:attr:`channel_enabled` to :python:`True` for instruments 0.

        .. code:: python

            session.instruments[0:2].channel_enabled = True
        
        sets :py:attr:`channel_enabled` to :python:`True` for instruments 0, 1, 2.

        Note that :py:attr:`channel_enabled` is only used as an example and is not necessarily a property which
        supports this repeated capability. See documentation for individual properties and methods to
        learn what repeated capabilites they support, if any.

pattern_opcode_events
---------------------

    .. py:attribute:: nidigital.Session.pattern_opcode_events[]

        ..
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

        .. code:: python

            session.pattern_opcode_events[0].channel_enabled = True

        sets :py:attr:`channel_enabled` to :python:`True` for pattern_opcode_events 0.

        .. code:: python

            session.pattern_opcode_events[0:2].channel_enabled = True
        
        sets :py:attr:`channel_enabled` to :python:`True` for pattern_opcode_events 0, 1, 2.

        Note that :py:attr:`channel_enabled` is only used as an example and is not necessarily a property which
        supports this repeated capability. See documentation for individual properties and methods to
        learn what repeated capabilites they support, if any.

conditional_jump_triggers
-------------------------

    .. py:attribute:: nidigital.Session.conditional_jump_triggers[]

        ..
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

        .. code:: python

            session.conditional_jump_triggers[0].channel_enabled = True

        sets :py:attr:`channel_enabled` to :python:`True` for conditional_jump_triggers 0.

        .. code:: python

            session.conditional_jump_triggers[0:2].channel_enabled = True
        
        sets :py:attr:`channel_enabled` to :python:`True` for conditional_jump_triggers 0, 1, 2.

        Note that :py:attr:`channel_enabled` is only used as an example and is not necessarily a property which
        supports this repeated capability. See documentation for individual properties and methods to
        learn what repeated capabilites they support, if any.

sites
-----

    .. py:attribute:: nidigital.Session.sites[]

        ..
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

        .. code:: python

            session.sites[0].channel_enabled = True

        sets :py:attr:`channel_enabled` to :python:`True` for sites 0.

        .. code:: python

            session.sites[0:2].channel_enabled = True
        
        sets :py:attr:`channel_enabled` to :python:`True` for sites 0, 1, 2.

        Note that :py:attr:`channel_enabled` is only used as an example and is not necessarily a property which
        supports this repeated capability. See documentation for individual properties and methods to
        learn what repeated capabilites they support, if any.

rio_events
----------

    .. py:attribute:: nidigital.Session.rio_events[]

        ..
            If no prefix is added to the items in the parameter, the correct prefix will be added when
            the driver function call is made.

            .. code:: python

                session.rio_events['0-2'].channel_enabled = True

            passes a string of :python:`'RIOEvent0, RIOEvent1, RIOEvent2'` to the set attribute function.

            If an invalid repeated capability is passed to the driver, the driver will return an error.

            You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
            for the specific repeated capability.

            .. code:: python

                session.rio_events['RIOEvent0-RIOEvent2'].channel_enabled = True

            passes a string of :python:`'RIOEvent0, RIOEvent1, RIOEvent2'` to the set attribute function.

        .. code:: python

            session.rio_events[0].channel_enabled = True

        sets :py:attr:`channel_enabled` to :python:`True` for rio_events 0.

        .. code:: python

            session.rio_events[0:2].channel_enabled = True
        
        sets :py:attr:`channel_enabled` to :python:`True` for rio_events 0, 1, 2.

        Note that :py:attr:`channel_enabled` is only used as an example and is not necessarily a property which
        supports this repeated capability. See documentation for individual properties and methods to
        learn what repeated capabilites they support, if any.

rio_triggers
------------

    .. py:attribute:: nidigital.Session.rio_triggers[]

        ..
            If no prefix is added to the items in the parameter, the correct prefix will be added when
            the driver function call is made.

            .. code:: python

                session.rio_triggers['0-2'].channel_enabled = True

            passes a string of :python:`'RIOTrigger0, RIOTrigger1, RIOTrigger2'` to the set attribute function.

            If an invalid repeated capability is passed to the driver, the driver will return an error.

            You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
            for the specific repeated capability.

            .. code:: python

                session.rio_triggers['RIOTrigger0-RIOTrigger2'].channel_enabled = True

            passes a string of :python:`'RIOTrigger0, RIOTrigger1, RIOTrigger2'` to the set attribute function.

        .. code:: python

            session.rio_triggers[0].channel_enabled = True

        sets :py:attr:`channel_enabled` to :python:`True` for rio_triggers 0.

        .. code:: python

            session.rio_triggers[0:2].channel_enabled = True
        
        sets :py:attr:`channel_enabled` to :python:`True` for rio_triggers 0, 1, 2.

        Note that :py:attr:`channel_enabled` is only used as an example and is not necessarily a property which
        supports this repeated capability. See documentation for individual properties and methods to
        learn what repeated capabilites they support, if any.


