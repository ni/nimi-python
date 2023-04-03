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
    The parameter can be an integer, a string, a list, a tuple, or slice (range).

    The recommended way of accessing repeated capabilities is with an integer :python:`[0]` or range :python:`[0:2]`.

channels
--------

    .. py:attribute:: niscope.Session.channels[]

        .. code:: python

            session.channels[0].channel_enabled = True

        sets :py:attr:`channel_enabled` to :python:`True` for channels 0.

        .. code:: python

            session.channels[0:2].channel_enabled = True
        
        sets :py:attr:`channel_enabled` to :python:`True` for channels 0, 1, 2.

        Note that :py:attr:`channel_enabled` is only used as an example and is not necessarily a property which
        supports this repeated capability. See documentation for individual properties and methods to
        learn what repeated capabilites they support, if any.

instruments
-----------

    .. py:attribute:: niscope.Session.instruments[]

        .. code:: python

            session.instruments[0].channel_enabled = True

        sets :py:attr:`channel_enabled` to :python:`True` for instruments 0.

        .. code:: python

            session.instruments[0:2].channel_enabled = True
        
        sets :py:attr:`channel_enabled` to :python:`True` for instruments 0, 1, 2.

        Note that :py:attr:`channel_enabled` is only used as an example and is not necessarily a property which
        supports this repeated capability. See documentation for individual properties and methods to
        learn what repeated capabilites they support, if any.


