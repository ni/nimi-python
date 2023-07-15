.. py:module:: nidcpower
    :noindex:

.. py:currentmodule:: nidcpower.Session

.. role:: c(code)
    :language: c

.. role:: python(code)
    :language: python

Repeated Capabilities
=====================

    :py:class:`nidcpower.Session` supports "Repeated Capabilities", which are multiple instances of the same type of
    functionality. The repeated capabilities supported by :py:class:`nidcpower.Session` are:

    #. channels_
    #. instruments_

    Use the indexing operator :python:`[]` to indicate which repeated capability instance you are trying to access.
    The parameter can be a single element or an iterable that implements sequence semantics, like list, tuple, range and slice.

    A single element will access one repeated capability.

    An iterable will access multiple repeated capabilites at once.

channels
--------

    .. py:attribute:: nidcpower.Session.channels[]

        The basic element for indexing this repeated capability is an integer.

        .. code:: python

            session.channels[0].output_function = nidcpower.OutputFunction.DC_CURRENT

        sets :py:attr:`output_function` to :py:data:`~nidcpower.OutputFunction.DC_CURRENT` for channels 0.

        .. code:: python

            session.channels[0, 2].output_function = nidcpower.OutputFunction.DC_CURRENT

        sets :py:attr:`output_function` to :py:data:`~nidcpower.OutputFunction.DC_CURRENT` for channels 0, 2.

instruments
-----------

    .. py:attribute:: nidcpower.Session.instruments[]

        The basic element for indexing this repeated capability is a string.

        .. code:: python

            print(session.instruments['Dev1'].serial_number)

        prints :py:attr:`serial_number` for instruments 'Dev1'.

        .. code:: python

            print(session.instruments['Dev1', 'Dev2', '3rdDevice'].serial_number)

        prints :py:attr:`serial_number` for instruments 'Dev1', 'Dev2', '3rdDevice' or errors if the value is not the same for all.


