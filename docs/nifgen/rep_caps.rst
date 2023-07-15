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

    A single element will access one repeated capability.

    An iterable will access multiple repeated capabilites at once.

channels
--------

    .. py:attribute:: nifgen.Session.channels[]

        The basic element for indexing this repeated capability is an integer.

        .. code:: python

            session.channels[0].func_amplitude = 0.5

        sets :py:attr:`func_amplitude` to :python:`0.5` for channels 0.

        .. code:: python

            session.channels[0, 1].func_amplitude = 0.5

        sets :py:attr:`func_amplitude` to :python:`0.5` for channels 0, 1.

script_triggers
---------------

    .. py:attribute:: nifgen.Session.script_triggers[]

        The basic element for indexing this repeated capability is an integer.

        .. code:: python

            session.script_triggers[0].exported_script_trigger_output_terminal = '/Dev1/PXI_Trig0'

        sets :py:attr:`exported_script_trigger_output_terminal` to :python:`'/Dev1/PXI_Trig0'` for script_triggers 0.

        .. code:: python

            session.script_triggers[0, 2].exported_script_trigger_output_terminal = '/Dev1/PXI_Trig0'

        sets :py:attr:`exported_script_trigger_output_terminal` to :python:`'/Dev1/PXI_Trig0'` for script_triggers 0, 2.

markers
-------

    .. py:attribute:: nifgen.Session.markers[]

        The basic element for indexing this repeated capability is an integer.

        .. code:: python

            session.markers[0].marker_event_output_terminal = '/Dev1/PXI_Trig0'

        sets :py:attr:`marker_event_output_terminal` to :python:`'/Dev1/PXI_Trig0'` for markers 0.

        .. code:: python

            session.markers[0, 2].marker_event_output_terminal = '/Dev1/PXI_Trig0'

        sets :py:attr:`marker_event_output_terminal` to :python:`'/Dev1/PXI_Trig0'` for markers 0, 2.

data_markers
------------

    .. py:attribute:: nifgen.Session.data_markers[]

        The basic element for indexing this repeated capability is an integer.

        .. code:: python

            session.data_markers[0].data_marker_event_level_polarity = nifgen.DataMarkerEventLevelPolarity.LOW

        sets :py:attr:`data_marker_event_level_polarity` to :py:data:`~nifgen.DataMarkerEventLevelPolarity.LOW` for data_markers 0.

        .. code:: python

            session.data_markers[0, 2].data_marker_event_level_polarity = nifgen.DataMarkerEventLevelPolarity.LOW

        sets :py:attr:`data_marker_event_level_polarity` to :py:data:`~nifgen.DataMarkerEventLevelPolarity.LOW` for data_markers 0, 2.


