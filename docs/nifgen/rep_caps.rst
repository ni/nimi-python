.. py:module:: nifgen
    :noindex:

.. py:currentmodule:: nifgen.Session

.. role:: c(code)
    :language: c

.. role:: python(code)
    :language: python

Repeated Capabilities
=====================

    Repeated capabilities attributes are used to set the `channel_string` parameter to the
    underlying driver function call. This can be the actual function based on the :py:class:`Session`
    method being called, or it can be the appropriate Get/Set Attribute function, such as :c:`niFgen_SetAttributeViInt32()`.

    Repeated capabilities attributes use the indexing operator :python:`[]` to indicate the repeated capabilities.
    The parameter can be a string, list, tuple, or slice (range). Each element of those can be a string or
    an integer.

    The recommended way of accessing repeated capabilities is with an integer :python:`[0]` or range :python:`[0:2]`.

channels
--------

    .. py:attribute:: nifgen.Session.channels[]

        .. code:: python

            session.channels[0].channel_enabled = True

        sets :py:attr:`channel_enabled` to :python:`True` for channels 0.

        .. code:: python

            session.channels[0:2].channel_enabled = True
        
        sets :py:attr:`channel_enabled` to :python:`True` for channels 0, 1, 2.

        Note that :py:attr:`channel_enabled` is only used as an example and is not necessarily a property which
        supports this repeated capability. See documentation for individual properties and methods to
        learn what repeated capabilites they support, if any.

script_triggers
---------------

    .. py:attribute:: nifgen.Session.script_triggers[]

        ..
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

        .. code:: python

            session.script_triggers[0].channel_enabled = True

        sets :py:attr:`channel_enabled` to :python:`True` for script_triggers 0.

        .. code:: python

            session.script_triggers[0:2].channel_enabled = True
        
        sets :py:attr:`channel_enabled` to :python:`True` for script_triggers 0, 1, 2.

        Note that :py:attr:`channel_enabled` is only used as an example and is not necessarily a property which
        supports this repeated capability. See documentation for individual properties and methods to
        learn what repeated capabilites they support, if any.

markers
-------

    .. py:attribute:: nifgen.Session.markers[]

        ..
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

        .. code:: python

            session.markers[0].channel_enabled = True

        sets :py:attr:`channel_enabled` to :python:`True` for markers 0.

        .. code:: python

            session.markers[0:2].channel_enabled = True
        
        sets :py:attr:`channel_enabled` to :python:`True` for markers 0, 1, 2.

        Note that :py:attr:`channel_enabled` is only used as an example and is not necessarily a property which
        supports this repeated capability. See documentation for individual properties and methods to
        learn what repeated capabilites they support, if any.

data_markers
------------

    .. py:attribute:: nifgen.Session.data_markers[]

        ..
            If no prefix is added to the items in the parameter, the correct prefix will be added when
            the driver function call is made.

            .. code:: python

                session.data_markers['0-2'].channel_enabled = True

            passes a string of :python:`'DataMarker0, DataMarker1, DataMarker2'` to the set attribute function.

            If an invalid repeated capability is passed to the driver, the driver will return an error.

            You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
            for the specific repeated capability.

            .. code:: python

                session.data_markers['DataMarker0-DataMarker2'].channel_enabled = True

            passes a string of :python:`'DataMarker0, DataMarker1, DataMarker2'` to the set attribute function.

        .. code:: python

            session.data_markers[0].channel_enabled = True

        sets :py:attr:`channel_enabled` to :python:`True` for data_markers 0.

        .. code:: python

            session.data_markers[0:2].channel_enabled = True
        
        sets :py:attr:`channel_enabled` to :python:`True` for data_markers 0, 1, 2.

        Note that :py:attr:`channel_enabled` is only used as an example and is not necessarily a property which
        supports this repeated capability. See documentation for individual properties and methods to
        learn what repeated capabilites they support, if any.


