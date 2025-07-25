.. py:module:: nirfsg
    :noindex:

.. py:currentmodule:: nirfsg.Session

.. role:: c(code)
    :language: c

.. role:: python(code)
    :language: python

Repeated Capabilities
=====================

    Repeated capabilities attributes are used to set the `channel_string` parameter to the
    underlying driver function call. This can be the actual function based on the :py:class:`Session`
    method being called, or it can be the appropriate Get/Set Attribute function, such as :c:`niRFSG_SetAttributeViInt32()`.

    Repeated capabilities attributes use the indexing operator :python:`[]` to indicate the repeated capabilities.
    The parameter can be a string, list, tuple, or slice (range). Each element of those can be a string or
    an integer. If it is a string, you can indicate a range using the same format as the driver: :python:`'0-2'` or
    :python:`'0:2'`

    Some repeated capabilities use a prefix before the number and this is optional

markers
-------

    .. py:attribute:: nirfsg.Session.markers[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.markers['0-2'].channel_enabled = True

        passes a string of :python:`'marker0, marker1, marker2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.markers['marker0-marker2'].channel_enabled = True

        passes a string of :python:`'marker0, marker1, marker2'` to the set attribute function.


script_triggers
---------------

    .. py:attribute:: nirfsg.Session.script_triggers[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.script_triggers['0-2'].channel_enabled = True

        passes a string of :python:`'scripttrigger0, scripttrigger1, scripttrigger2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.script_triggers['scripttrigger0-scripttrigger2'].channel_enabled = True

        passes a string of :python:`'scripttrigger0, scripttrigger1, scripttrigger2'` to the set attribute function.


waveforms
---------

    .. py:attribute:: nirfsg.Session.waveforms[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.waveforms['0-2'].channel_enabled = True

        passes a string of :python:`'waveform::0, waveform::1, waveform::2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.waveforms['waveform::0-waveform::2'].channel_enabled = True

        passes a string of :python:`'waveform::0, waveform::1, waveform::2'` to the set attribute function.


ports
-----

    .. py:attribute:: nirfsg.Session.ports[]

        .. code:: python

            session.ports['0-2'].channel_enabled = True

        passes a string of :python:`'0, 1, 2'` to the set attribute function.


lo_channels
-----------

    .. py:attribute:: nirfsg.Session.lo_channels[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.lo_channels['0-2'].channel_enabled = True

        passes a string of :python:`'LO0, LO1, LO2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.lo_channels['LO0-LO2'].channel_enabled = True

        passes a string of :python:`'LO0, LO1, LO2'` to the set attribute function.



