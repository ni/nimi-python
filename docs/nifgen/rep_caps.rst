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
    The parameter can be a single element or an iterable that implements sequence semantics, like list, tuple, range and slice.

    The recommended way of accessing a single repeated capability is with an integer :python:`[0]` for capabilities that support it and a string :python:`['Dev1']`
    for those that don't support integers.

    The recommended way of accessing multiple repeated capabilites at once is with a tuple (:python:`[0, 1]` or :python:`['Dev1', 'Dev2']`) or slice :python:`[0:2]`.

channels
--------

    .. py:attribute:: nifgen.Session.channels[]

        .. code:: python

            session.channels[0].func_amplitude = 0.5

        sets :py:attr:`func_amplitude` to :python:`0.5` for channels 0.

        .. code:: python

            session.channels[0, 1].func_amplitude = 0.5

        sets :py:attr:`func_amplitude` to :python:`0.5` for channels 0, 1.

script_triggers
---------------

    .. py:attribute:: nifgen.Session.script_triggers[]

        .. code:: python

            session.script_triggers[0].exported_script_trigger_output_terminal = '/Dev1/PXI_Trig0'

        sets :py:attr:`exported_script_trigger_output_terminal` to :python:`'/Dev1/PXI_Trig0'` for script_triggers 0.

        .. code:: python

            session.script_triggers[0, 2].exported_script_trigger_output_terminal = '/Dev1/PXI_Trig0'

        sets :py:attr:`exported_script_trigger_output_terminal` to :python:`'/Dev1/PXI_Trig0'` for script_triggers 0, 2.

markers
-------

    .. py:attribute:: nifgen.Session.markers[]

        .. code:: python

            session.markers[0].marker_event_output_terminal = '/Dev1/PXI_Trig0'

        sets :py:attr:`marker_event_output_terminal` to :python:`'/Dev1/PXI_Trig0'` for markers 0.

        .. code:: python

            session.markers[0, 2].marker_event_output_terminal = '/Dev1/PXI_Trig0'

        sets :py:attr:`marker_event_output_terminal` to :python:`'/Dev1/PXI_Trig0'` for markers 0, 2.

data_markers
------------

    .. py:attribute:: nifgen.Session.data_markers[]

        .. code:: python

            session.data_markers[0].data_marker_event_level_polarity = nifgen.DataMarkerEventLevelPolarity.LOW

        sets :py:attr:`data_marker_event_level_polarity` to :py:data:`~nifgen.DataMarkerEventLevelPolarity.LOW` for data_markers 0.

        .. code:: python

            session.data_markers[0, 2].data_marker_event_level_polarity = nifgen.DataMarkerEventLevelPolarity.LOW

        sets :py:attr:`data_marker_event_level_polarity` to :py:data:`~nifgen.DataMarkerEventLevelPolarity.LOW` for data_markers 0, 2.


