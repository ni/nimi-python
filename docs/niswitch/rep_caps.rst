.. py:module:: niswitch
    :noindex:

.. py:currentmodule:: niswitch.Session

.. role:: c(code)
    :language: c

.. role:: python(code)
    :language: python

Repeated Capabilities
=====================

    :py:class:`niswitch.Session` supports "Repeated Capabilities", which are multiple instances of the same type of
    functionality. The repeated capabilities supported by :py:class:`niswitch.Session` are:

    #. channels_

    Use the indexing operator :python:`[]` to indicate which repeated capability instance you are trying to access.
    The parameter can be a single element or an iterable that implements sequence semantics, like list, tuple, range and slice.

    A single element will access one repeated capability.

    An iterable will access multiple repeated capabilites at once.

channels
--------

    .. py:attribute:: niswitch.Session.channels[]

        The basic element for indexing this repeated capability is an integer.

        .. code:: python

            session.channels[0].is_source_channel = True

        sets :py:attr:`is_source_channel` to :python:`True` for channels 0.

        .. code:: python

            session.channels[0, 2].is_source_channel = True

        sets :py:attr:`is_source_channel` to :python:`True` for channels 0, 2.


