.. role:: c(code)
    :language: c

.. role:: python(code)
    :language: python

Repeated Capabilities
=====================

    Repeated capabilities attributes are used to set the `channel_string` parameter to the
    underlying driver function call. This can be the actual function based on the :py:class:`Session`
    method being called, or it can be the appropriate Get/Set Attribute function, such as :c:`niFgen_SetAttributeViInt32()`.

    Repeated capbilities attributes use the indexing operator :python:`[]` to indicate the repeated capabilities.
    The parameter can be a string, list, tuple, or slice (range). Each element of those can be a string or
    an integer. If it is a string, you can indicate a range using the same format as the driver: :python:`'0-2'` or
    :python:`'0:2'`

    Some repeated capabilities use a prefix before the number and this is optional

channels
--------

    .. py:attribute:: nifgen.Session.channels[]

        .. code:: python

            session.channels['0-2'].channel_enabled = True

        passes a string of :python:`'0, 1, 2'` to the set attribute function.


script_triggers
---------------

    .. py:attribute:: nifgen.Session.script_triggers[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.script_triggers['0-2'].channel_enabled = True

        passes a string of :python:`'ScriptTrigger0, ScriptTrigger1, ScriptTrigger2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.script_triggers['ScriptTrigger0-ScriptTrigger2'].channel_enabled = True

        passes a string of :python:`'ScriptTrigger0, ScriptTrigger1, ScriptTrigger2'` to the set attribute function.


markers
-------

    .. py:attribute:: nifgen.Session.markers[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.markers['0-2'].channel_enabled = True

        passes a string of :python:`'Marker0, Marker1, Marker2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.markers['Marker0-Marker2'].channel_enabled = True

        passes a string of :python:`'Marker0, Marker1, Marker2'` to the set attribute function.



