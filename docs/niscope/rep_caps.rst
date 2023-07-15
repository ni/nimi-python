.. py:module:: niscope
    :noindex:

.. py:currentmodule:: niscope.Session

.. role:: c(code)
    :language: c

.. role:: python(code)
    :language: python

Repeated Capabilities
=====================

    :py:class:`niscope.Session` supports "Repeated Capabilities", which are multiple instances of the same type of
    functionality. The repeated capabilities supported by :py:class:`niscope.Session` are:

    #. channels_
    #. instruments_

    Use the indexing operator :python:`[]` to indicate which repeated capability instance you are trying to access.
    The parameter can be a single element or an iterable that implements sequence semantics, like list, tuple, range and slice.

    A single element will access one repeated capability.

    An iterable will access multiple repeated capabilites at once.

channels
--------

    .. py:attribute:: niscope.Session.channels[]

        The basic element for indexing this repeated capability is an integer.

        .. code:: python

            session.channels[0].channel_enabled = True

        sets :py:attr:`channel_enabled` to :python:`True` for channels 0.

        .. code:: python

            session.channels[0, 2].channel_enabled = True

        sets :py:attr:`channel_enabled` to :python:`True` for channels 0, 2.

instruments
-----------

    .. py:attribute:: niscope.Session.instruments[]

        The basic element for indexing this repeated capability is a string.

        .. code:: python

            print(session.instruments['Dev1'].serial_number)

        prints :py:attr:`serial_number` for instruments 'Dev1'.

        .. code:: python

            print(session.instruments['Dev1', 'Dev2', '3rdDevice'].serial_number)

        prints :py:attr:`serial_number` for instruments 'Dev1', 'Dev2', '3rdDevice'.


