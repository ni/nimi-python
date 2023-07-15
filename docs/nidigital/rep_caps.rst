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
    The parameter can be a single element or an iterable that implements sequence semantics, like list, tuple, range and slice.

    A single element will access one repeated capability.

    An iterable will access multiple repeated capabilites at once.

channels
--------

    .. py:attribute:: nidigital.Session.channels[]

        The basic element for indexing this repeated capability is an integer.

        .. code:: python

            session.channels[0].vil = 2

        sets :py:attr:`vil` to :python:`2` for channels 0.

        .. code:: python

            session.channels[0, 2].vil = 2

        sets :py:attr:`vil` to :python:`2` for channels 0, 2.

pins
----

    .. py:attribute:: nidigital.Session.pins[]

        The basic element for indexing this repeated capability is a string.

        .. code:: python

            session.pins['PinA'].vil = 2

        sets :py:attr:`vil` to :python:`2` for pins 'PinA'.

        .. code:: python

            session.pins['PinA', 'PinB', 'CPin'].vil = 2

        sets :py:attr:`vil` to :python:`2` for pins 'PinA', 'PinB', 'CPin'.

instruments
-----------

    .. py:attribute:: nidigital.Session.instruments[]

        The basic element for indexing this repeated capability is a string.

        .. code:: python

            session.instruments['Dev1'].timing_absolute_delay = 5e-09

        sets :py:attr:`timing_absolute_delay` to :python:`5e-09` for instruments 'Dev1'.

        .. code:: python

            session.instruments['Dev1', 'Dev2', '3rdDevice'].timing_absolute_delay = 5e-09

        sets :py:attr:`timing_absolute_delay` to :python:`5e-09` for instruments 'Dev1', 'Dev2', '3rdDevice'.

pattern_opcode_events
---------------------

    .. py:attribute:: nidigital.Session.pattern_opcode_events[]

        The basic element for indexing this repeated capability is an integer.

        .. code:: python

            session.pattern_opcode_events[0].exported_pattern_opcode_event_output_terminal = '/Dev1/PXI_Trig0'

        sets :py:attr:`exported_pattern_opcode_event_output_terminal` to :python:`'/Dev1/PXI_Trig0'` for pattern_opcode_events 0.

        .. code:: python

            session.pattern_opcode_events[0, 2].exported_pattern_opcode_event_output_terminal = '/Dev1/PXI_Trig0'

        sets :py:attr:`exported_pattern_opcode_event_output_terminal` to :python:`'/Dev1/PXI_Trig0'` for pattern_opcode_events 0, 2.

conditional_jump_triggers
-------------------------

    .. py:attribute:: nidigital.Session.conditional_jump_triggers[]

        The basic element for indexing this repeated capability is an integer.

        .. code:: python

            session.conditional_jump_triggers[0].conditional_jump_trigger_type = nidigital.TriggerType.DIGITAL_EDGE

        sets :py:attr:`conditional_jump_trigger_type` to :py:data:`~nidigital.TriggerType.DIGITAL_EDGE` for conditional_jump_triggers 0.

        .. code:: python

            session.conditional_jump_triggers[0, 2].conditional_jump_trigger_type = nidigital.TriggerType.DIGITAL_EDGE

        sets :py:attr:`conditional_jump_trigger_type` to :py:data:`~nidigital.TriggerType.DIGITAL_EDGE` for conditional_jump_triggers 0, 2.

sites
-----

    .. py:attribute:: nidigital.Session.sites[]

        The basic element for indexing this repeated capability is an integer.

        .. code:: python

            session.sites[0].disable_sites()

        calls :py:meth:`disable_sites` for sites 0.

        .. code:: python

            session.sites[0, 2].disable_sites()

        calls :py:meth:`disable_sites` for sites 0, 2.

rio_events
----------

    .. py:attribute:: nidigital.Session.rio_events[]

        The basic element for indexing this repeated capability is an integer.

        .. code:: python

            session.rio_events[0].exported_rio_event_output_terminal = '/Dev1/PXI_Trig0'

        sets :py:attr:`exported_rio_event_output_terminal` to :python:`'/Dev1/PXI_Trig0'` for rio_events 0.

        .. code:: python

            session.rio_events[0, 2].exported_rio_event_output_terminal = '/Dev1/PXI_Trig0'

        sets :py:attr:`exported_rio_event_output_terminal` to :python:`'/Dev1/PXI_Trig0'` for rio_events 0, 2.

rio_triggers
------------

    .. py:attribute:: nidigital.Session.rio_triggers[]

        The basic element for indexing this repeated capability is an integer.

        .. code:: python

            session.rio_triggers[0].rio_trigger_type = nidigital.TriggerType.DIGITAL_EDGE

        sets :py:attr:`rio_trigger_type` to :py:data:`~nidigital.TriggerType.DIGITAL_EDGE` for rio_triggers 0.

        .. code:: python

            session.rio_triggers[0, 2].rio_trigger_type = nidigital.TriggerType.DIGITAL_EDGE

        sets :py:attr:`rio_trigger_type` to :py:data:`~nidigital.TriggerType.DIGITAL_EDGE` for rio_triggers 0, 2.


