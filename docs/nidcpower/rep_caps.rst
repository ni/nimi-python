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

    The recommended way of accessing a single repeated capability is with an integer :python:`[0]` for capabilities that support it and a string :python:`['Dev1']`
    for those that don't support integers.

    The recommended way of accessing multiple repeated capabilites at once is with a tuple (:python:`[0, 1]` or :python:`['Dev1', 'Dev2']`) or slice :python:`[0:2]`.

channels
--------

    .. py:attribute:: nidcpower.Session.channels[]

        .. code:: python

            session.channels[0].output_function = nidcpower.OutputFunction.DC_CURRENT

        sets :py:attr:`output_function` to :py:data:`~nidcpower.OutputFunction.DC_CURRENT` for channels 0.

        .. code:: python

            session.channels[0, 2].output_function = nidcpower.OutputFunction.DC_CURRENT

        sets :py:attr:`output_function` to :py:data:`~nidcpower.OutputFunction.DC_CURRENT` for channels 0, 2.

instruments
-----------

    .. py:attribute:: nidcpower.Session.instruments[]

        .. code:: python

            print(session.instruments['Dev1'].serial_number)

        prints :py:attr:`serial_number` for instruments 'Dev1'.

        .. code:: python

            print(session.instruments['Dev1', 'Dev2', '3rdDevice'].serial_number)

        prints :py:attr:`serial_number` for instruments 'Dev1', 'Dev2', '3rdDevice' or errors if the value is not the same for all.


