.. py:module:: nifgen
    :noindex:

.. py:currentmodule:: nifgen.Session

.. role:: c(code)
    :language: c

.. role:: python(code)
    :language: python

Repeated Capabilities
=====================

    :py:class:`nifgen.Session` supports "Repeated Capabilities", which are multiple instances of the same type of
    functionality. The repeated capabilities supported by :py:class:`nifgen.Session` are:

    #. channels_
    #. script_triggers_
    #. markers_
    #. data_markers_

    Use the indexing operator :python:`[]` to indicate which repeated capability instance you are trying to access.
    The parameter can be an integer, a string, a list, a tuple, or slice (range).

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

        .. code:: python

            session.data_markers[0].channel_enabled = True

        sets :py:attr:`channel_enabled` to :python:`True` for data_markers 0.

        .. code:: python

            session.data_markers[0:2].channel_enabled = True
        
        sets :py:attr:`channel_enabled` to :python:`True` for data_markers 0, 1, 2.

        Note that :py:attr:`channel_enabled` is only used as an example and is not necessarily a property which
        supports this repeated capability. See documentation for individual properties and methods to
        learn what repeated capabilites they support, if any.


