.. py:module:: nirfsa
    :noindex:

.. py:currentmodule:: nirfsa.Session

.. role:: c(code)
    :language: c

.. role:: python(code)
    :language: python

Repeated Capabilities
=====================

    Repeated capabilities attributes are used to set the `channel_string` parameter to the
    underlying driver function call. This can be the actual function based on the :py:class:`Session`
    method being called, or it can be the appropriate Get/Set Attribute function, such as :c:`niRFSA_SetAttributeViInt32()`.

    Repeated capabilities attributes use the indexing operator :python:`[]` to indicate the repeated capabilities.
    The parameter can be a string, list, tuple, or slice (range). Each element of those can be a string or
    an integer. If it is a string, you can indicate a range using the same format as the driver: :python:`'0-2'` or
    :python:`'0:2'`

    Some repeated capabilities use a prefix before the number and this is optional

ports
-----

    .. py:attribute:: nirfsa.Session.ports[]

        .. code:: python

            session.ports['0-2'].channel_enabled = True

        passes a string of :python:`'0, 1, 2'` to the set attribute function.


los
---

    .. py:attribute:: nirfsa.Session.los[]

        If no prefix is added to the items in the parameter, the correct prefix will be added when
        the driver function call is made.

        .. code:: python

            session.los['0-2'].channel_enabled = True

        passes a string of :python:`'LO0, LO1, LO2'` to the set attribute function.

        If an invalid repeated capability is passed to the driver, the driver will return an error.

        You can also explicitly use the prefix as part of the parameter, but it must be the correct prefix
        for the specific repeated capability.

        .. code:: python

            session.los['LO0-LO2'].channel_enabled = True

        passes a string of :python:`'LO0, LO1, LO2'` to the set attribute function.


device_temperatures
-------------------

    .. py:attribute:: nirfsa.Session.device_temperatures[]

        .. code:: python

            session.device_temperatures['0-2'].channel_enabled = True

        passes a string of :python:`'0, 1, 2'` to the set attribute function.


channels
--------

    .. py:attribute:: nirfsa.Session.channels[]

        .. code:: python

            session.channels['0-2'].channel_enabled = True

        passes a string of :python:`'0, 1, 2'` to the set attribute function.



