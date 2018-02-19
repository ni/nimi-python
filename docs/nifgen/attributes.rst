nifgen.Session properties
=========================

.. py:currentmodule:: nifgen.Session

.. py:attribute:: all_marker_events_latched_status

    Returns a bit field of the latched status of all Marker Events.  Write 0 to this attribute to clear the latched status of all Marker Events.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Marker:Advanced:All Marker Events Latched Status**
            - C Attribute: **NIFGEN_ATTR_ALL_MARKER_EVENTS_LATCHED_STATUS**

.. py:attribute:: all_marker_events_live_status

    Returns a bit field of the live status of all Marker Events.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Marker:Advanced:All Marker Events Live Status**
            - C Attribute: **NIFGEN_ATTR_ALL_MARKER_EVENTS_LIVE_STATUS**

.. py:attribute:: analog_data_mask

    Specifies the mask to apply to the analog output. The masked data is replaced with the data in NIFGEN_ATTR_ANALOG_STATIC_VALUE.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Data Mask:Analog Data Mask**
            - C Attribute: **NIFGEN_ATTR_ANALOG_DATA_MASK**

.. py:attribute:: analog_filter_enabled

    Controls whether the signal generator applies to an analog filter to the output signal. This attribute is valid in arbitrary waveform, arbitrary sequence, and script modes. This attribute can also be used in standard function and frequency list modes for user-defined waveforms.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Filters:Analog Filter Enabled**
            - C Attribute: **NIFGEN_ATTR_ANALOG_FILTER_ENABLED**

.. py:attribute:: analog_path

    Specifies the analog signal path that should be used. The main path allows you to configure gain, offset, analog filter status, output impedance, and output enable. The main path has two amplifier options, high- and low-gain.
    The direct path presents a much smaller gain range, and you cannot adjust offset or the filter status. The direct path also provides a smaller output range but also lower distortion. NI-FGEN normally chooses the amplifier based on the user-specified gain.

    The following table lists the characteristics of this property.

    +----------------+------------------+
    | Characteristic | Value            |
    +================+==================+
    | Datatype       | enums.AnalogPath |
    +----------------+------------------+
    | Permissions    | read-write       |
    +----------------+------------------+
    | Channel Based  | False            |
    +----------------+------------------+
    | Resettable     | Yes              |
    +----------------+------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Analog Path**
            - C Attribute: **NIFGEN_ATTR_ANALOG_PATH**

.. py:attribute:: analog_static_value

    Specifies the static value that replaces data masked by NIFGEN_ATTR_ANALOG_DATA_MASK.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Data Mask:Analog Static Value**
            - C Attribute: **NIFGEN_ATTR_ANALOG_STATIC_VALUE**

.. py:attribute:: arb_gain

    Specifies the factor by which the signal generator scales the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this attribute to scale the arbitrary waveform to other ranges.
    For example, when you set this attribute to 2.0, the output signal ranges from -2.0 V to +2.0 V.
    Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB or NIFGEN_VAL_OUTPUT_SEQ.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Gain**
            - C Attribute: **NIFGEN_ATTR_ARB_GAIN**

.. py:attribute:: arb_marker_position

    Specifies the position for a marker to be asserted in the arbitrary waveform. This attribute defaults to -1 when no marker position is specified. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB.
    Use niFgen_ExportSignal to export the marker signal.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Arbitrary Waveform Mode:Marker Position**
            - C Attribute: **NIFGEN_ATTR_ARB_MARKER_POSITION**

.. py:attribute:: arb_offset

    Specifies the value that the signal generator adds to the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this attribute to shift the arbitrary waveform range.
    For example, when you set this attribute to 1.0, the output signal ranges from 2.0 V to 0.0 V.
    Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB or NIFGEN_VAL_OUTPUT_SEQ.
    Units: Volts

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Offset**
            - C Attribute: **NIFGEN_ATTR_ARB_OFFSET**

.. py:attribute:: arb_repeat_count

    Specifies number of times to repeat the arbitrary waveform when the triggerMode parameter of nifgen_ConfigureTriggerMode is set to NIFGEN_VAL_SINGLE or NIFGEN_VAL_STEPPED. This attribute is ignored if the triggerMode parameter is set to NIFGEN_VAL_CONTINUOUS or NIFGEN_VAL_BURST. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB.
    When used during streaming, this attribute specifies the number of times to repeat the streaming waveform (the onboard memory allocated for streaming).  For more information about streaming, refer to the Streaming topic.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Arbitrary Waveform Mode:Repeat Count**
            - C Attribute: **NIFGEN_ATTR_ARB_REPEAT_COUNT**

.. py:attribute:: arb_sample_rate

    Specifies the rate at which the signal generator outputs the points in arbitrary waveforms.  Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set  to NIFGEN_VAL_OUTPUT_ARB or NIFGEN_VAL_OUTPUT_SEQ.
    Units: Samples/s

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Sample Clock:Rate**
            - C Attribute: **NIFGEN_ATTR_ARB_SAMPLE_RATE**

.. py:attribute:: arb_sequence_handle

    This channel-based attribute identifies which sequence the signal generator produces. You can create multiple sequences using niFgen_CreateArbSequence. niFgen_CreateArbSequence returns a handle that you can use to identify the particular sequence. To configure the signal generator to produce a particular sequence, set this attribute to the sequence handle.
    Use this attribute only when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_SEQ.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Arbitrary Sequence Mode:Arbitrary Sequence Handle**
            - C Attribute: **NIFGEN_ATTR_ARB_SEQUENCE_HANDLE**

.. py:attribute:: arb_waveform_handle

    Selects which arbitrary waveform the signal generator produces. You can create multiple arbitrary waveforms using one of the following niFgen Create Waveform functions:
    niFgen_CreateWaveformF64
    niFgen_CreateWaveformI16
    niFgen_CreateWaveformFromFileI16
    niFgen_CreateWaveformFromFileF64
    niFgen_CreateWaveformFromFileHWS
    These functions return a handle that you can use to identify the particular waveform. To configure the signal generator to produce a particular waveform, set this attribute to the waveform handle.
    Use this attribute only when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Arbitrary Waveform Mode:Arbitrary Waveform Handle**
            - C Attribute: **NIFGEN_ATTR_ARB_WAVEFORM_HANDLE**

.. py:attribute:: aux_power_enabled

    Controls the specified auxiliary power pin. Setting this attribute to TRUE energizes the auxiliary power when the session is committed. When this attribute is FALSE, the power pin of the connector outputs no power.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Advanced:AUX Power Enabled**
            - C Attribute: **NIFGEN_ATTR_AUX_POWER_ENABLED**

.. py:attribute:: bus_type

    The bus type of the signal generator.

    The following table lists the characteristics of this property.

    +----------------+---------------+
    | Characteristic | Value         |
    +================+===============+
    | Datatype       | enums.BusType |
    +----------------+---------------+
    | Permissions    | read only     |
    +----------------+---------------+
    | Channel Based  | False         |
    +----------------+---------------+
    | Resettable     | No            |
    +----------------+---------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Bus Type**
            - C Attribute: **NIFGEN_ATTR_BUS_TYPE**

.. py:attribute:: cache

    Specifies whether to cache the value of attributes.   When caching is enabled, NI-FGEN keeps track of  the current device settings and avoids sending redundant commands to  the device. Thus, you can significantly increase execution speed.
    NI-FGEN can choose to always cache or to never cache  particular attributes regardless of the setting of this attribute.  Use niFgen_InitWithOptions to override the default value.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Inherent IVI Attributes:User Options:Cache**
            - C Attribute: **NIFGEN_ATTR_CACHE**

.. py:attribute:: cal_adc_input

    Specifies the input of the calibration ADC. The ADC can take a reading from several inputs: the analog output, a 2.5 V reference, and ground.

    The following table lists the characteristics of this property.

    +----------------+-------------------+
    | Characteristic | Value             |
    +================+===================+
    | Datatype       | enums.CalADCInput |
    +----------------+-------------------+
    | Permissions    | read-write        |
    +----------------+-------------------+
    | Channel Based  | False             |
    +----------------+-------------------+
    | Resettable     | Yes               |
    +----------------+-------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Calibration:Cal ADC Input**
            - C Attribute: **NIFGEN_ATTR_CAL_ADC_INPUT**

.. py:attribute:: channel_delay

    Specifies, in seconds, the delay to apply to the analog output of the channel specified by the channel string. You can use the channel delay to configure the timing relationship between channels on a multichannel device. Values for this attribute can be zero or positive. A value of zero indicates that the channels are aligned. A positive value delays the analog output by the specified number of seconds.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Channel Delay**
            - C Attribute: **NIFGEN_ATTR_CHANNEL_DELAY**

.. py:attribute:: clock_mode

    Controls which clock mode is used for the signal generator.
    For signal generators that support it, this attribute allows switching the sample  clock to High-Resolution mode. When in Divide-Down  mode, the sample rate can only be set to certain frequences, based on  dividing down the update clock. However, in High-Resolution mode, the  sample rate may be set to any value.

    The following table lists the characteristics of this property.

    +----------------+-----------------+
    | Characteristic | Value           |
    +================+=================+
    | Datatype       | enums.ClockMode |
    +----------------+-----------------+
    | Permissions    | read-write      |
    +----------------+-----------------+
    | Channel Based  | False           |
    +----------------+-----------------+
    | Resettable     | Yes             |
    +----------------+-----------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Sample Clock:Mode**
            - C Attribute: **NIFGEN_ATTR_CLOCK_MODE**

.. py:attribute:: common_mode_offset

    Specifies, in volts, the value the signal generator adds to or subtracts from the arbitrary waveform data. This attribute applies only when you set the NIFGEN_ATTR_TERMINAL_CONFIGURATION attribute to NIFGEN_VAL_DIFFERENTIAL. Common mode offset is applied to the signals generated at each differential output terminal.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Common Mode Offset**
            - C Attribute: **NIFGEN_ATTR_COMMON_MODE_OFFSET**

.. py:attribute:: data_marker_events_count

    Returns the number of Data Marker Events supported by the device.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Data Marker Events Count**
            - C Attribute: **NIFGEN_ATTR_DATA_MARKER_EVENTS_COUNT**

.. py:attribute:: data_marker_event_data_bit_number

    Specifies the bit number to assign to the Data Marker Event.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Data Marker:Data Bit Number**
            - C Attribute: **NIFGEN_ATTR_DATA_MARKER_EVENT_DATA_BIT_NUMBER**

.. py:attribute:: data_marker_event_level_polarity

    Specifies the output polarity of the Data marker event.

    The following table lists the characteristics of this property.

    +----------------+------------------------------------+
    | Characteristic | Value                              |
    +================+====================================+
    | Datatype       | enums.DataMarkerEventLevelPolarity |
    +----------------+------------------------------------+
    | Permissions    | read-write                         |
    +----------------+------------------------------------+
    | Channel Based  | False                              |
    +----------------+------------------------------------+
    | Resettable     | Yes                                |
    +----------------+------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Data Marker:Level:Active Level**
            - C Attribute: **NIFGEN_ATTR_DATA_MARKER_EVENT_LEVEL_POLARITY**

.. py:attribute:: data_marker_event_output_terminal

    Specifies the destination terminal for the Data Marker Event.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Data Marker:Output Terminal**
            - C Attribute: **NIFGEN_ATTR_DATA_MARKER_EVENT_OUTPUT_TERMINAL**

.. py:attribute:: data_transfer_block_size

    The number of samples at a time to download to onboard memory. Useful when the total data to be transferred to onboard memory is large.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Data Transfer Block Size**
            - C Attribute: **NIFGEN_ATTR_DATA_TRANSFER_BLOCK_SIZE**

.. py:attribute:: data_transfer_maximum_bandwidth

    Specifies the maximum amount of bus bandwidth (in bytes per second) to use for data transfers. The signal generator limits data transfer speeds on the PCIe bus to the value you specify for this attribute. Set this attribute to optimize bus bandwidth usage for multi-device streaming applications by preventing the signal generator from consuming all of the available bandwidth on a PCI express link when waveforms are being written to the onboard memory of the device.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Maximum Bandwidth**
            - C Attribute: **NIFGEN_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH**

.. py:attribute:: data_transfer_maximum_in_flight_reads

    Specifies the maximum number of concurrent PCI Express read requests the signal generator can issue.
    When transferring data from computer memory to device onboard memory across the PCI Express bus, the signal generator can issue multiple memory reads at the same time. In general, the larger the number of read requests, the more efficiently the device uses the bus because the multiple read requests keep the data flowing, even in a PCI Express topology that has high latency due to PCI Express switches in the data path. Most NI devices can issue a large number of read requests (typically 8 or 16). By default, this attribute is set to the highest value the signal generator supports.
    If other devices in your system cannot tolerate long data latencies, it may be helpful to decrease the number of in-flight read requests the NI signal generator issues. This helps to reduce the amount of data the signal generator reads at one time.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Advanced:Maximum In-Flight Read Requests**
            - C Attribute: **NIFGEN_ATTR_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS**

.. py:attribute:: data_transfer_preferred_packet_size

    Specifies the preferred size of the data field in a PCI Express read request packet. In general, the larger the packet size, the more efficiently the device uses the bus. By default, NI signal generators use the largest packet size allowed by the system. However, due to different system implementations, some systems may perform better with smaller packet sizes.
    Recommended values for this attribute are powers of two between 64 and 512.
    In some cases, the signal generator generates packets smaller than  the preferred size you set with this attribute.
    You cannot change this attribute while the device is generating a waveform. If you want to change the device configuration, call the niFgen_AbortGeneration function or wait for the generation to complete.



    .. note:: :

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Advanced:Preferred Packet Size**
            - C Attribute: **NIFGEN_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE**

.. py:attribute:: digital_data_mask

    Specifies the mask to apply to the output on the digital connector. The masked data is replaced with the data in NIFGEN_ATTR_DIGITAL_STATIC_VALUE.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Data Mask:Digital Data Mask**
            - C Attribute: **NIFGEN_ATTR_DIGITAL_DATA_MASK**

.. py:attribute:: digital_edge_script_trigger_edge

    Specifies the active edge for the Script trigger. This attribute is used when NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE is set to Digital Edge.

    The following table lists the characteristics of this property.

    +----------------+------------------------------------+
    | Characteristic | Value                              |
    +================+====================================+
    | Datatype       | enums.ScriptTriggerDigitalEdgeEdge |
    +----------------+------------------------------------+
    | Permissions    | read-write                         |
    +----------------+------------------------------------+
    | Channel Based  | False                              |
    +----------------+------------------------------------+
    | Resettable     | Yes                                |
    +----------------+------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Script:Digital Edge:Edge**
            - C Attribute: **NIFGEN_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE**

.. py:attribute:: digital_edge_script_trigger_source

    Specifies the source terminal for the Script trigger. This attribute is used when NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE is set to Digital Edge.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Script:Digital Edge:Source**
            - C Attribute: **NIFGEN_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE**

.. py:attribute:: digital_edge_start_trigger_edge

    Specifies the active edge for the Start trigger. This attribute is used only when NIFGEN_ATTR_START_TRIGGER_TYPE is set to Digital Edge.

    The following table lists the characteristics of this property.

    +----------------+-----------------------------------+
    | Characteristic | Value                             |
    +================+===================================+
    | Datatype       | enums.StartTriggerDigitalEdgeEdge |
    +----------------+-----------------------------------+
    | Permissions    | read-write                        |
    +----------------+-----------------------------------+
    | Channel Based  | False                             |
    +----------------+-----------------------------------+
    | Resettable     | Yes                               |
    +----------------+-----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Start:Digital Edge:Edge**
            - C Attribute: **NIFGEN_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE**

.. py:attribute:: digital_edge_start_trigger_source

    Specifies the source terminal for the Start trigger. This attribute is used only when NIFGEN_ATTR_START_TRIGGER_TYPE is set to Digital Edge.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Start:Digital Edge:Source**
            - C Attribute: **NIFGEN_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE**

.. py:attribute:: digital_filter_enabled

    Controls whether the signal generator applies a digital filter to the output signal. This attribute is valid in arbitrary waveform, arbitrary sequence, and script modes. This attribute can also be used in standard function and frequency list modes for user-defined waveforms.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Filters:Digital Filter Enabled**
            - C Attribute: **NIFGEN_ATTR_DIGITAL_FILTER_ENABLED**

.. py:attribute:: digital_filter_interpolation_factor

    This attribute only affects the device when NIFGEN_ATTR_DIGITAL_FILTER_ENABLED is set to VI_TRUE. If you do not set this attribute directly, NI-FGEN automatically selects the maximum interpolation factor allowed for the current sample rate. Valid values are 2, 4, and 8.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Filters:Digital Filter Interpolation Factor**
            - C Attribute: **NIFGEN_ATTR_DIGITAL_FILTER_INTERPOLATION_FACTOR**

.. py:attribute:: digital_gain

    Specifies a factor by which the signal generator digitally multiplies generated data before converting it to an analog signal in the DAC. For a digital gain greater than 1.0, the product of digital gain times the generated data must be inside the range plus or minus 1.0 (assuming floating point data).  If the product exceeds these limits, the signal generator clips the output signal, and an error results.
    Some signal generators support both digital gain and an analog gain (analog gain is specified with the NIFGEN_ATTR_FUNC_AMPLITUDE attribute or the NIFGEN_ATTR_ARB_GAIN attribute). Digital gain can be changed during generation without the glitches that may occur when changing analog gains, due to relay switching. However, the DAC output resolution is a function of analog gain, so only analog gain makes full use of the resolution of the DAC.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Digital Gain**
            - C Attribute: **NIFGEN_ATTR_DIGITAL_GAIN**

.. py:attribute:: digital_level_script_trigger_active_level

    Specifies the active level for the Script trigger. This attribute is used when NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE is set to Digital Level.

    The following table lists the characteristics of this property.

    +----------------+--------------------------------------------+
    | Characteristic | Value                                      |
    +================+============================================+
    | Datatype       | enums.ScriptTriggerDigitalLevelActiveLevel |
    +----------------+--------------------------------------------+
    | Permissions    | read-write                                 |
    +----------------+--------------------------------------------+
    | Channel Based  | False                                      |
    +----------------+--------------------------------------------+
    | Resettable     | Yes                                        |
    +----------------+--------------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Script:Digital Level:Active Level**
            - C Attribute: **NIFGEN_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL**

.. py:attribute:: digital_level_script_trigger_source

    Specifies the source terminal for the Script trigger. This attribute is used when NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE is set to Digital Level.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Script:Digital Level:Source**
            - C Attribute: **NIFGEN_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE**

.. py:attribute:: digital_pattern_enabled

    Controls whether the signal generator generates a digital pattern of the output signal.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Advanced:Digital Pattern Enabled**
            - C Attribute: **NIFGEN_ATTR_DIGITAL_PATTERN_ENABLED**

.. py:attribute:: digital_static_value

    Specifies the static value that replaces data masked by NIFGEN_ATTR_DIGITAL_DATA_MASK.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Data Mask:Digital Static Value**
            - C Attribute: **NIFGEN_ATTR_DIGITAL_STATIC_VALUE**

.. py:attribute:: direct_dma_enabled

    Enable the device for Direct DMA writes. When enabled, all Create Waveform and Write Waveform function calls that are given a data address in the Direct DMA Window will download data residing on the Direct DMA device to the instrument's onboard memory.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Direct DMA:Direct DMA Enabled**
            - C Attribute: **NIFGEN_ATTR_DIRECT_DMA_ENABLED**

.. py:attribute:: direct_dma_window_address

    Specifies the window address (beginning of window) of the waveform data source. This window address is specified by your Direct DMA-compatible data source.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Direct DMA:Window Address**
            - C Attribute: **NIFGEN_ATTR_DIRECT_DMA_WINDOW_ADDRESS**

.. py:attribute:: direct_dma_window_size

    Specifies the size of the memory window in bytes (not samples) provided by your Direct DMA-compatible data source.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Direct DMA:Window Size in Bytes**
            - C Attribute: **NIFGEN_ATTR_DIRECT_DMA_WINDOW_SIZE**

.. py:attribute:: done_event_delay

    Specifies the amount of delay applied to a Done Event with respect to the  analog output of the signal generator. A positive delay value indicates that  the Done Event will come out after the analog data, while a negative delay  value indicates that the Done Event will come out before the analog data.  The default value is zero, which will align the Done Event with the analog output.  You can specify the units of the delay value by setting the  NIFGEN_ATTR_DONE_EVENT_DELAY attribute.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Done:Advanced:Delay Value**
            - C Attribute: **NIFGEN_ATTR_DONE_EVENT_DELAY**

.. py:attribute:: done_event_delay_units

    Specifies the units applied to the value of the NIFGEN_ATTR_DONE_EVENT_DELAY attribute. Valid units are seconds and sample clock periods.

    The following table lists the characteristics of this property.

    +----------------+---------------------------+
    | Characteristic | Value                     |
    +================+===========================+
    | Datatype       | enums.DoneEventDelayUnits |
    +----------------+---------------------------+
    | Permissions    | read-write                |
    +----------------+---------------------------+
    | Channel Based  | False                     |
    +----------------+---------------------------+
    | Resettable     | Yes                       |
    +----------------+---------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Done:Advanced:Delay Units**
            - C Attribute: **NIFGEN_ATTR_DONE_EVENT_DELAY_UNITS**

.. py:attribute:: done_event_latched_status

    Returns the latched status of the specified Done Event.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | bool      |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Done:Advanced:Latched Status**
            - C Attribute: **NIFGEN_ATTR_DONE_EVENT_LATCHED_STATUS**

.. py:attribute:: done_event_level_active_level

    Specifies the output polarity of the Done Event.

    The following table lists the characteristics of this property.

    +----------------+----------------------------+
    | Characteristic | Value                      |
    +================+============================+
    | Datatype       | enums.DoneEventActiveLevel |
    +----------------+----------------------------+
    | Permissions    | read-write                 |
    +----------------+----------------------------+
    | Channel Based  | False                      |
    +----------------+----------------------------+
    | Resettable     | Yes                        |
    +----------------+----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Done:Level:Active Level**
            - C Attribute: **NIFGEN_ATTR_DONE_EVENT_LEVEL_ACTIVE_LEVEL**

.. py:attribute:: done_event_output_behavior

    Specifies the output behavior for the Done Event.

    The following table lists the characteristics of this property.

    +----------------+-------------------------------+
    | Characteristic | Value                         |
    +================+===============================+
    | Datatype       | enums.DoneEventOutputBehavior |
    +----------------+-------------------------------+
    | Permissions    | read-write                    |
    +----------------+-------------------------------+
    | Channel Based  | False                         |
    +----------------+-------------------------------+
    | Resettable     | Yes                           |
    +----------------+-------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Done:Output Behavior**
            - C Attribute: **NIFGEN_ATTR_DONE_EVENT_OUTPUT_BEHAVIOR**

.. py:attribute:: done_event_output_terminal

    Specifies the destination terminal for the Done Event.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Done:Output Terminal**
            - C Attribute: **NIFGEN_ATTR_DONE_EVENT_OUTPUT_TERMINAL**

.. py:attribute:: done_event_pulse_polarity

    Specifies the output polarity of the Done Event.

    The following table lists the characteristics of this property.

    +----------------+------------------------------+
    | Characteristic | Value                        |
    +================+==============================+
    | Datatype       | enums.DoneEventPulsePolarity |
    +----------------+------------------------------+
    | Permissions    | read-write                   |
    +----------------+------------------------------+
    | Channel Based  | False                        |
    +----------------+------------------------------+
    | Resettable     | Yes                          |
    +----------------+------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Done:Pulse:Polarity**
            - C Attribute: **NIFGEN_ATTR_DONE_EVENT_PULSE_POLARITY**

.. py:attribute:: done_event_pulse_width

    Specifies the pulse width for the Done Event.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Done:Pulse:Width Value**
            - C Attribute: **NIFGEN_ATTR_DONE_EVENT_PULSE_WIDTH**

.. py:attribute:: done_event_pulse_width_units

    Specifies the pulse width units for the Done Event.

    The following table lists the characteristics of this property.

    +----------------+--------------------------------+
    | Characteristic | Value                          |
    +================+================================+
    | Datatype       | enums.DoneEventPulseWidthUnits |
    +----------------+--------------------------------+
    | Permissions    | read-write                     |
    +----------------+--------------------------------+
    | Channel Based  | False                          |
    +----------------+--------------------------------+
    | Resettable     | Yes                            |
    +----------------+--------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Done:Pulse:Width Units**
            - C Attribute: **NIFGEN_ATTR_DONE_EVENT_PULSE_WIDTH_UNITS**

.. py:attribute:: driver_setup

    Specifies the driver setup portion of the option string that was passed into the niFgen_InitWithOptions function.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  |         0 |
    +----------------+-----------+
    | Resettable     |         0 |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - C Attribute: **NIFGEN_ATTR_DRIVER_SETUP**

.. py:attribute:: exported_onboard_reference_clock_output_terminal

    Specifies the terminal to which to export the Onboard Reference Clock.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Reference Clock:Onboard Reference Clock:Export Output Terminal**
            - C Attribute: **NIFGEN_ATTR_EXPORTED_ONBOARD_REFERENCE_CLOCK_OUTPUT_TERMINAL**

.. py:attribute:: exported_reference_clock_output_terminal

    Specifies the terminal to which to export the Reference Clock.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Reference Clock:Export Output Terminal**
            - C Attribute: **NIFGEN_ATTR_EXPORTED_REFERENCE_CLOCK_OUTPUT_TERMINAL**

.. py:attribute:: exported_sample_clock_divisor

    Specifies the factor by which to divide the Sample clock, also known as the Update clock, before it is exported.  To export the Sample clock, use the niFgen_ExportSignal function or the  NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL attribute.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Sample Clock:Exported Sample Clock Divisor**
            - C Attribute: **NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_DIVISOR**

.. py:attribute:: exported_sample_clock_output_terminal

    Specifies the terminal to which to export the Sample Clock.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Sample Clock:Export Output Terminal**
            - C Attribute: **NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL**

.. py:attribute:: exported_sample_clock_timebase_divisor

    Specifies the factor by which to divide the sample clock timebase (board clock) before it is exported.  To export the Sample clock timebase, use the niFgen_ExportSignal function or the  NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL attribute.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Sample Clock Timebase:Exported Sample Clock Timebase Divisor**
            - C Attribute: **NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR**

.. py:attribute:: exported_sample_clock_timebase_output_terminal

    Specifies the terminal to which to export the Sample clock timebase. If you specify a divisor with the NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR attribute,   the Sample clock exported with the NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL  attribute is the value of the Sample clock timebase after it is divided-down.  For a list of the terminals available on your device, refer to the Device Routes tab in MAX.
    To change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.



    .. note:: The signal generator must not be in the Generating state when you change this attribute.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Sample Clock Timebase:Export Output Terminal**
            - C Attribute: **NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL**

.. py:attribute:: exported_script_trigger_output_terminal

    Specifies the output terminal for the exported Script trigger.
    Setting this attribute to an empty string means that when you commit the session, the signal is removed from that terminal and, if possible, the terminal is tristated.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Script:Output Terminal**
            - C Attribute: **NIFGEN_ATTR_EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL**

.. py:attribute:: exported_start_trigger_output_terminal

    Specifies the destination terminal for exporting the Start trigger.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Start:Output Terminal**
            - C Attribute: **NIFGEN_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL**

.. py:attribute:: external_clock_delay_binary_value

    Binary value of the external clock delay.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Advanced:External Clock Delay Binary Value**
            - C Attribute: **NIFGEN_ATTR_EXTERNAL_CLOCK_DELAY_BINARY_VALUE**

.. py:attribute:: external_sample_clock_multiplier

    Specifies a multiplication factor to use to obtain a desired sample rate from an external Sample clock.  The resulting sample rate is equal to this factor multiplied by the external Sample clock rate.  You can use this attribute to generate samples at a rate higher than your external clock rate.  When using this attribute, you do not need to explicitly set the external clock rate.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Advanced:External Sample Clock Multiplier**
            - C Attribute: **NIFGEN_ATTR_EXTERNAL_SAMPLE_CLOCK_MULTIPLIER**

.. py:attribute:: file_transfer_block_size

    The number of samples at a time to read from the file and download to onboard memory. Used in conjunction with the Create From File and Write From File functions.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Data Transfer:File Transfer Block Size**
            - C Attribute: **NIFGEN_ATTR_FILE_TRANSFER_BLOCK_SIZE**

.. py:attribute:: filter_correction_frequency

    Controls the filter correction frequency of the analog filter. This attribute corrects for the ripples in the analog filter frequency response at the frequency specified. For standard waveform output, the filter correction frequency should be set to be the same as the frequency of the standard waveform. To have no filter correction, set this attribute to 0 Hz.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:5401/5411/5431:Filter Correction Frequency**
            - C Attribute: **NIFGEN_ATTR_FILTER_CORRECTION_FREQUENCY**

.. py:attribute:: flatness_correction_enabled

    When VI_TRUE, the signal generator applies a flatness correction factor to the generated sine wave in order to ensure the same output power level at all frequencies.
    This attribute should be set to VI_FALSE when performing Flatness Calibration.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Filters:Flatness Correction Enabled**
            - C Attribute: **NIFGEN_ATTR_FLATNESS_CORRECTION_ENABLED**

.. py:attribute:: fpga_bitfile_path

    Gets the absolute file path to the bitfile loaded on the FPGA.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:FPGA Bitfile Path**
            - C Attribute: **NIFGEN_ATTR_FPGA_BITFILE_PATH**

.. py:attribute:: freq_list_duration_quantum

    Returns the quantum of which all durations must be a multiple in a  frequency list.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Standard Function:Frequency List Mode:Frequency List Duration Quantum**
            - C Attribute: **NIFGEN_ATTR_FREQ_LIST_DURATION_QUANTUM**

.. py:attribute:: freq_list_handle

    Sets which frequency list the signal generator  produces. Create a frequency list using niFgen_CreateFreqList.  niFgen_CreateFreqList returns a handle that you can  use to identify the list.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Standard Function:Frequency List Mode:Frequency List Handle**
            - C Attribute: **NIFGEN_ATTR_FREQ_LIST_HANDLE**

.. py:attribute:: func_amplitude

    Controls the amplitude of the standard waveform that the  signal generator produces. This value is the amplitude at the  output terminal.
    For example, to produce a waveform ranging from -5.00 V to +5.00 V, set  the amplitude to 10.00 V.
    set the Waveform parameter to NIFGEN_VAL_WFM_DC.
    Units: Vpk-pk



    .. note:: This parameter does not affect signal generator behavior when you

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Standard Function:Amplitude**
            - C Attribute: **NIFGEN_ATTR_FUNC_AMPLITUDE**

.. py:attribute:: func_buffer_size

    This attribute contains the number of samples used in the standard function waveform  buffer. This attribute is only valid on devices that implement standard function mode  in software, and is read-only for all other devices.
    implementation of Standard Function Mode on your device.



    .. note:: Refer to the Standard Function Mode topic for more information on the

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Standard Function:Standard Function Mode:Buffer Size**
            - C Attribute: **NIFGEN_ATTR_FUNC_BUFFER_SIZE**

.. py:attribute:: func_dc_offset

    Controls the DC offset of the standard waveform that the  signal generator produces.  This value is the offset at the output  terminal. The value is the offset from ground to the center of the  waveform that you specify with the Waveform parameter.
    For example, to configure a waveform with an amplitude of 10.00 V to  range from 0.00 V to +10.00 V, set DC Offset to 5.00 V.
    Units: volts

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Standard Function:DC Offset**
            - C Attribute: **NIFGEN_ATTR_FUNC_DC_OFFSET**

.. py:attribute:: func_duty_cycle_high

    Controls the duty cycle of the square wave the signal generator  produces. Specify this attribute as a percentage of  the time the square wave is high in a cycle.
    set the Waveform parameter to NIFGEN_VAL_WFM_SQUARE.
    Units: Percentage of time the waveform is high



    .. note:: This parameter only affects signal generator behavior when you

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Standard Function:Duty Cycle High**
            - C Attribute: **NIFGEN_ATTR_FUNC_DUTY_CYCLE_HIGH**

.. py:attribute:: func_frequency

    Controls the frequency of the standard waveform that the  signal generator produces.
    Units: hertz
    (1) This parameter does not affect signal generator behavior when you  set the Waveform parameter of the niFgen_ConfigureStandardWaveform function  to NIFGEN_VAL_WFM_DC.
    (2) For NIFGEN_VAL_WFM_SINE, the range is between 0 MHz and 16 MHz, but the  range is between 0 MHz and 1 MHz for all other waveforms.



    .. note:: :

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Standard Function:Standard Function Mode:Frequency**
            - C Attribute: **NIFGEN_ATTR_FUNC_FREQUENCY**

.. py:attribute:: func_max_buffer_size

    This attribute sets the maximum number of samples that can be used in the standard  function waveform buffer. Increasing this value may increase the quality of  the waveform. This attribute is only valid on devices that implement standard  function mode in software, and is read-only for all other devices.
    implementation of Standard Function Mode on your device.



    .. note:: Refer to the Standard Function Mode topic for more information on the

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Standard Function:Standard Function Mode:Maximum Buffer Size**
            - C Attribute: **NIFGEN_ATTR_FUNC_MAX_BUFFER_SIZE**

.. py:attribute:: func_start_phase

    Controls horizontal offset of the standard waveform the  signal generator produces. Specify this attribute in degrees of  one waveform cycle.
    A start phase of 180 degrees means output generation begins halfway  through the waveform. A start phase of 360 degrees offsets the output by  an entire waveform cycle, which is identical to a start phase of 0  degrees.
    set the Waveform parameter to NIFGEN_VAL_WFM_DC.
    Units: Degrees of one cycle



    .. note:: This parameter does not affect signal generator behavior when you

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Standard Function:Start Phase**
            - C Attribute: **NIFGEN_ATTR_FUNC_START_PHASE**

.. py:attribute:: func_waveform

    This channel-based attribute specifies which standard waveform the signal generator produces.
    Use this attribute only when NIFGEN_ATTR_OUTPUT_MODE is set to  NIFGEN_VAL_OUTPUT_FUNC.
    NIFGEN_VAL_WFM_SINE      - Sinusoid waveform
    NIFGEN_VAL_WFM_SQUARE    - Square waveform
    NIFGEN_VAL_WFM_TRIANGLE  - Triangle waveform
    NIFGEN_VAL_WFM_RAMP_UP   - Positive ramp waveform
    NIFGEN_VAL_WFM_RAMP_DOWN - Negative ramp waveform
    NIFGEN_VAL_WFM_DC        - Constant voltage
    NIFGEN_VAL_WFM_NOISE     - White noise
    NIFGEN_VAL_WFM_USER      - User-defined waveform as defined with
    niFgen_DefineUserStandardWaveform

    The following table lists the characteristics of this property.

    +----------------+----------------+
    | Characteristic | Value          |
    +================+================+
    | Datatype       | enums.Waveform |
    +----------------+----------------+
    | Permissions    | read-write     |
    +----------------+----------------+
    | Channel Based  | False          |
    +----------------+----------------+
    | Resettable     | No             |
    +----------------+----------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Standard Function:Waveform**
            - C Attribute: **NIFGEN_ATTR_FUNC_WAVEFORM**

.. py:attribute:: gain_dac_value

    Specifies the value programmed to the gain DAC. The value should be treated as an unsigned, right-justified number.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Calibration:Gain DAC Value**
            - C Attribute: **NIFGEN_ATTR_GAIN_DAC_VALUE**

.. py:attribute:: group_capabilities

    Returns a string that contains a comma-separated list of class-extention groups that  NI-FGEN implements.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities**
            - C Attribute: **NIFGEN_ATTR_GROUP_CAPABILITIES**

.. py:attribute:: idle_behavior

    Specifies the behavior of the output during the Idle state.  The output can be configured to hold the last generated voltage before entering the Idle state or jump to the Idle Value.

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | enums.IdleBehavior |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | Yes                |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Advanced:Idle Behavior**
            - C Attribute: **NIFGEN_ATTR_IDLE_BEHAVIOR**

.. py:attribute:: idle_value

    Specifies the value to generate in the Idle state.  The Idle Behavior must be configured to jump to this value.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Advanced:Idle Value**
            - C Attribute: **NIFGEN_ATTR_IDLE_VALUE**

.. py:attribute:: id_query_response

    

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  |         0 |
    +----------------+-----------+
    | Resettable     |         0 |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - C Attribute: **NIFGEN_ATTR_ID_QUERY_RESPONSE**

.. py:attribute:: instrument_firmware_revision

    A string that contains the firmware revision information  for the device that you are currently using.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Inherent IVI Attributes:Instrument Identification:Firmware Revision**
            - C Attribute: **NIFGEN_ATTR_INSTRUMENT_FIRMWARE_REVISION**

.. py:attribute:: instrument_manufacturer

    A string that contains the name of the device manufacturer you are currently  using.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Inherent IVI Attributes:Instrument Identification:Manufacturer**
            - C Attribute: **NIFGEN_ATTR_INSTRUMENT_MANUFACTURER**

.. py:attribute:: instrument_model

    A string that contains the model number or name of the device that you  are currently using.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Inherent IVI Attributes:Instrument Identification:Model**
            - C Attribute: **NIFGEN_ATTR_INSTRUMENT_MODEL**

.. py:attribute:: interchange_check

    Specifies whether to perform interchangeability checking and retrieve  interchangeability warnings when you call  niFgen_InitiateGeneration.
    Interchangeability warnings indicate that using your application with a  different device might cause different behavior.   Call niFgen_GetNextInterchangeWarning to extract interchange warnings.   Call niFgen_ClearInterchangeWarnings to clear the list  of interchangeability warnings without reading them.
    Interchangeability checking examines the attributes in a  capability group only if you specify a value for at least one  attribute within that group. Interchangeability warnings can  occur when an attribute affects the behavior of the device and you  have not set that attribute, or the attribute has been invalidated since you set it.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Inherent IVI Attributes:User Options:Interchange Check**
            - C Attribute: **NIFGEN_ATTR_INTERCHANGE_CHECK**

.. py:attribute:: io_resource_descriptor

    Indicates the resource descriptor that NI-FGEN uses to identify the physical device.
    If you initialize NI-FGEN with a logical name, this  attribute contains the resource descriptor that corresponds  to the entry in the IVI Configuration Utility.
    If you initialize NI-FGEN with the resource  descriptor, this attribute contains that value.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Inherent IVI Attributes:Advanced Session Information:Resource Descriptor**
            - C Attribute: **NIFGEN_ATTR_IO_RESOURCE_DESCRIPTOR**

.. py:attribute:: load_impedance

    This channel-based attribute specifies the load impedance connected to the analog output of the channel. If you set this attribute to NIFGEN_VAL_MATCHED_LOAD_IMPEDANCE (-1.0), NI-FGEN assumes that the load impedance matches the output impedance. NI-FGEN compensates to give the desired peak-to-peak voltage amplitude or arbitrary gain (relative to 1 V).

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Load Impedance**
            - C Attribute: **NIFGEN_ATTR_LOAD_IMPEDANCE**

.. py:attribute:: logical_name

    A string containing the logical name that you specified when opening the  current IVI session.
    You may pass a logical name to niFgen_init or  niFgen_InitWithOptions.  The IVI Configuration Utility must contain an entry for the logical name.   The logical name entry refers to a virtual instrument section in the  IVI Configuration file. The virtual instrument section specifies a physical  device and initial user options.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Inherent IVI Attributes:Advanced Session Information:Logical Name**
            - C Attribute: **NIFGEN_ATTR_LOGICAL_NAME**

.. py:attribute:: major_version

    Returns the major version number of NI-FGEN.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Obsolete:Major Version**
            - C Attribute: **NIFGEN_ATTR_MAJOR_VERSION**

.. py:attribute:: marker_events_count

    Returns the number of markers supported by the device. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_SCRIPT.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Marker Events Count**
            - C Attribute: **NIFGEN_ATTR_MARKER_EVENTS_COUNT**

.. py:attribute:: marker_event_delay

    Specifies the amount of delay applied to a Marker Event with respect to the  analog output of the signal generator. A positive delay value indicates that  the Marker Event will come out after the analog data, while a negative delay  value indicates that the Marker Event will come out before the analog data.  The default value is zero, which will align the Marker Event with the  analog output. You can specify the units of the delay value by setting the NIFGEN_ATTR_MARKER_EVENT_DELAY attribute.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Marker:Advanced:Delay Value**
            - C Attribute: **NIFGEN_ATTR_MARKER_EVENT_DELAY**

.. py:attribute:: marker_event_delay_units

    Specifies the units applied to the value of the NIFGEN_ATTR_MARKER_EVENT_DELAY attribute.  Valid units are seconds and sample clock periods.

    The following table lists the characteristics of this property.

    +----------------+-----------------------------+
    | Characteristic | Value                       |
    +================+=============================+
    | Datatype       | enums.MarkerEventDelayUnits |
    +----------------+-----------------------------+
    | Permissions    | read-write                  |
    +----------------+-----------------------------+
    | Channel Based  | False                       |
    +----------------+-----------------------------+
    | Resettable     | Yes                         |
    +----------------+-----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Marker:Advanced:Delay Units**
            - C Attribute: **NIFGEN_ATTR_MARKER_EVENT_DELAY_UNITS**

.. py:attribute:: marker_event_latched_status

    Specifies the latched status of the specified Marker Event.
    Write VI_TRUE to this attribute to clear the latched status of the Marker Event.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Marker:Advanced:Latched Status**
            - C Attribute: **NIFGEN_ATTR_MARKER_EVENT_LATCHED_STATUS**

.. py:attribute:: marker_event_live_status

    Returns the live status of the specified Marker Event.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | bool      |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Marker:Advanced:Live Status**
            - C Attribute: **NIFGEN_ATTR_MARKER_EVENT_LIVE_STATUS**

.. py:attribute:: marker_event_output_behavior

    Specifies the output behavior for the Marker Event.

    The following table lists the characteristics of this property.

    +----------------+---------------------------------+
    | Characteristic | Value                           |
    +================+=================================+
    | Datatype       | enums.MarkerEventOutputBehavior |
    +----------------+---------------------------------+
    | Permissions    | read-write                      |
    +----------------+---------------------------------+
    | Channel Based  | False                           |
    +----------------+---------------------------------+
    | Resettable     | Yes                             |
    +----------------+---------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Marker:Output Behavior**
            - C Attribute: **NIFGEN_ATTR_MARKER_EVENT_OUTPUT_BEHAVIOR**

.. py:attribute:: marker_event_output_terminal

    Specifies the destination terminal for the Marker Event.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Marker:Output Terminal**
            - C Attribute: **NIFGEN_ATTR_MARKER_EVENT_OUTPUT_TERMINAL**

.. py:attribute:: marker_event_pulse_polarity

    Specifies the output polarity of the Marker Event.

    The following table lists the characteristics of this property.

    +----------------+--------------------------------+
    | Characteristic | Value                          |
    +================+================================+
    | Datatype       | enums.MarkerEventPulsePolarity |
    +----------------+--------------------------------+
    | Permissions    | read-write                     |
    +----------------+--------------------------------+
    | Channel Based  | False                          |
    +----------------+--------------------------------+
    | Resettable     | Yes                            |
    +----------------+--------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Marker:Pulse:Polarity**
            - C Attribute: **NIFGEN_ATTR_MARKER_EVENT_PULSE_POLARITY**

.. py:attribute:: marker_event_pulse_width

    Specifies the pulse width for the Marker Event.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Marker:Pulse:Width Value**
            - C Attribute: **NIFGEN_ATTR_MARKER_EVENT_PULSE_WIDTH**

.. py:attribute:: marker_event_pulse_width_units

    Specifies the pulse width units for the Marker Event.

    The following table lists the characteristics of this property.

    +----------------+----------------------------------+
    | Characteristic | Value                            |
    +================+==================================+
    | Datatype       | enums.MarkerEventPulseWidthUnits |
    +----------------+----------------------------------+
    | Permissions    | read-write                       |
    +----------------+----------------------------------+
    | Channel Based  | False                            |
    +----------------+----------------------------------+
    | Resettable     | Yes                              |
    +----------------+----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Marker:Pulse:Width Units**
            - C Attribute: **NIFGEN_ATTR_MARKER_EVENT_PULSE_WIDTH_UNITS**

.. py:attribute:: marker_event_toggle_initial_state

    Specifies the output polarity of the Marker Event.

    The following table lists the characteristics of this property.

    +----------------+-------------------------------------+
    | Characteristic | Value                               |
    +================+=====================================+
    | Datatype       | enums.MarkerEventToggleInitialState |
    +----------------+-------------------------------------+
    | Permissions    | read-write                          |
    +----------------+-------------------------------------+
    | Channel Based  | False                               |
    +----------------+-------------------------------------+
    | Resettable     | Yes                                 |
    +----------------+-------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Marker:Toggle:Initial State**
            - C Attribute: **NIFGEN_ATTR_MARKER_EVENT_TOGGLE_INITIAL_STATE**

.. py:attribute:: max_freq_list_duration

    Returns the maximum duration of any one step in the frequency  list.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | float     |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Standard Function:Frequency List Mode:Maximum Frequency List Duration**
            - C Attribute: **NIFGEN_ATTR_MAX_FREQ_LIST_DURATION**

.. py:attribute:: max_freq_list_length

    Returns the maximum number of steps that can be in a frequency  list.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Standard Function:Frequency List Mode:Maximum Frequency List Length**
            - C Attribute: **NIFGEN_ATTR_MAX_FREQ_LIST_LENGTH**

.. py:attribute:: max_loop_count

    Returns the maximum number of times that the signal generator can repeat a waveform in a sequence. Typically, this value is constant for the signal generator.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Arbitrary Sequence Mode:Max Loop Count**
            - C Attribute: **NIFGEN_ATTR_MAX_LOOP_COUNT**

.. py:attribute:: max_num_freq_lists

    Returns the maximum number of frequency lists the signal generator allows.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Standard Function:Frequency List Mode:Maximum Number Of Frequency Lists**
            - C Attribute: **NIFGEN_ATTR_MAX_NUM_FREQ_LISTS**

.. py:attribute:: max_num_sequences

    Returns the maximum number of arbitrary sequences that the signal generator allows. Typically, this value is constant for the signal generator.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Arbitrary Sequence Mode:Max Number of Sequences**
            - C Attribute: **NIFGEN_ATTR_MAX_NUM_SEQUENCES**

.. py:attribute:: max_num_waveforms

    Returns the maximum number of arbitrary waveforms that the signal generator allows. Typically, this value is constant for the signal generator.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Capabilities:Max Number of Waveforms**
            - C Attribute: **NIFGEN_ATTR_MAX_NUM_WAVEFORMS**

.. py:attribute:: max_sequence_length

    Returns the maximum number of arbitrary waveforms that the signal generator allows in a sequence. Typically, this value is constant for the signal generator.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Arbitrary Sequence Mode:Max Sequence Length**
            - C Attribute: **NIFGEN_ATTR_MAX_SEQUENCE_LENGTH**

.. py:attribute:: max_waveform_size

    Returns the size, in samples, of the largest waveform that can be created. This attribute reflects the space currently available, taking into account previously allocated waveforms and instructions.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Capabilities:Max Waveform Size**
            - C Attribute: **NIFGEN_ATTR_MAX_WAVEFORM_SIZE**

.. py:attribute:: memory_size

    The total amount of memory, in bytes, on the signal generator.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Memory Size**
            - C Attribute: **NIFGEN_ATTR_MEMORY_SIZE**

.. py:attribute:: minor_version

    Returns the minor version number of NI-FGEN.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Obsolete:Minor Version**
            - C Attribute: **NIFGEN_ATTR_MINOR_VERSION**

.. py:attribute:: min_freq_list_duration

    Returns the minimum number of steps that can be in a frequency  list.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | float     |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Standard Function:Frequency List Mode:Minimum Frequency List Duration**
            - C Attribute: **NIFGEN_ATTR_MIN_FREQ_LIST_DURATION**

.. py:attribute:: min_freq_list_length

    Returns the minimum number of frequency lists that the signal generator allows.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Standard Function:Frequency List Mode:Minimum Frequency List Length**
            - C Attribute: **NIFGEN_ATTR_MIN_FREQ_LIST_LENGTH**

.. py:attribute:: min_sequence_length

    Returns the minimum number of arbitrary waveforms that the signal generator allows in a sequence. Typically, this value is constant for the signal generator.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Arbitrary Sequence Mode:Min Sequence Length**
            - C Attribute: **NIFGEN_ATTR_MIN_SEQUENCE_LENGTH**

.. py:attribute:: min_waveform_size

    Returns the minimum number of points that the signal generator allows in an arbitrary waveform. Typically, this value is constant for the signal generator.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Capabilities:Min Waveform Size**
            - C Attribute: **NIFGEN_ATTR_MIN_WAVEFORM_SIZE**

.. py:attribute:: module_revision

    A string that contains the module revision  for the device that you are currently using.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Inherent IVI Attributes:Instrument Identification:Module Revision**
            - C Attribute: **NIFGEN_ATTR_MODULE_REVISION**

.. py:attribute:: num_channels

    Indicates the number of channels that the specific instrument  driver supports.
    For each attribute for which IVI_VAL_MULTI_CHANNEL is set, the IVI Engine maintains a separate cache value for each channel.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Inherent IVI Attributes:Driver Capabilities:Channel Count**
            - C Attribute: **NIFGEN_ATTR_NUM_CHANNELS**

.. py:attribute:: offset_dac_value

    Specifies the value programmed to the offset DAC. The value should be treated as an unsigned, right-justified number.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Calibration:Offset DAC Value**
            - C Attribute: **NIFGEN_ATTR_OFFSET_DAC_VALUE**

.. py:attribute:: oscillator_freq_dac_value

    Specifies the value programmed to the oscillator frequency DAC. The value should be treated as an unsigned, right-justified number.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Calibration:Oscillator Freq DAC Value**
            - C Attribute: **NIFGEN_ATTR_OSCILLATOR_FREQ_DAC_VALUE**

.. py:attribute:: oscillator_phase_dac_value

    The value of the oscillator phase DAC.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Advanced:Oscillator Phase DAC Value**
            - C Attribute: **NIFGEN_ATTR_OSCILLATOR_PHASE_DAC_VALUE**

.. py:attribute:: osp_carrier_enabled

    Enables or disables generation of the carrier.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:Carrier Enabled**
            - C Attribute: **NIFGEN_ATTR_OSP_CARRIER_ENABLED**

.. py:attribute:: osp_carrier_frequency

    The frequency of the generated carrier.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:Carrier Frequency**
            - C Attribute: **NIFGEN_ATTR_OSP_CARRIER_FREQUENCY**

.. py:attribute:: osp_carrier_phase_i

    I Carrier Phase in degrees at the first point of the generation.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Carrier Phase:Carrier Phase I**
            - C Attribute: **NIFGEN_ATTR_OSP_CARRIER_PHASE_I**

.. py:attribute:: osp_carrier_phase_q

    Q Carrier Phase in degrees at the first point of the generation.  This attribute is only used when the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE  attribute is set to NIFGEN_VAL_OSP_COMPLEX.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Carrier Phase:Carrier Phase Q**
            - C Attribute: **NIFGEN_ATTR_OSP_CARRIER_PHASE_Q**

.. py:attribute:: osp_cic_filter_enabled

    Enables or disables the CIC filter.
    The NIFGEN_ATTR_OSP_CIC_FILTER_ENABLED and NIFGEN_ATTR_OSP_FIR_FILTER_ENABLED  attributes must have the same enable/disable setting.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:Advanced:CIC Filter Enabled**
            - C Attribute: **NIFGEN_ATTR_OSP_CIC_FILTER_ENABLED**

.. py:attribute:: osp_cic_filter_gain

    Gain applied at the final stage of the CIC filter. Commonly used to compensate  for attenuation in the FIR filter. For FIR filter types other than Custom,  NI-FGEN calculates the CIC gain in order to achieve unity gain between the FIR  and CIC filters. Setting this attribute overrides the value set by NI-FGEN.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:Advanced:CIC Filter Gain**
            - C Attribute: **NIFGEN_ATTR_OSP_CIC_FILTER_GAIN**

.. py:attribute:: osp_cic_filter_interpolation

    Interpolation factor for the CIC filter. If you do not set this value, NI-FGEN  calculates the appropriate value based on the value of the NIFGEN_ATTR_OSP_IQ_RATE attribute.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:Advanced:CIC Interpolation Factor**
            - C Attribute: **NIFGEN_ATTR_OSP_CIC_FILTER_INTERPOLATION**

.. py:attribute:: osp_compensate_for_filter_group_delay

    Compensate for OSP Filter Group Delay. If this is enabled, the Event Outputs will be aligned  with the Analog Output. The Analog output will also be aligned between synchronized devices  (using NI-TClk).

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:Advanced:Compensate for Filter Group Delay**
            - C Attribute: **NIFGEN_ATTR_OSP_COMPENSATE_FOR_FILTER_GROUP_DELAY**

.. py:attribute:: osp_data_processing_mode

    The way in which data is processed by the OSP block.

    The following table lists the characteristics of this property.

    +----------------+--------------------------+
    | Characteristic | Value                    |
    +================+==========================+
    | Datatype       | enums.DataProcessingMode |
    +----------------+--------------------------+
    | Permissions    | read-write               |
    +----------------+--------------------------+
    | Channel Based  | False                    |
    +----------------+--------------------------+
    | Resettable     | Yes                      |
    +----------------+--------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:Data Processing Mode**
            - C Attribute: **NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE**

.. py:attribute:: osp_enabled

    Enables or disables the OSP block of the signal generator. When the OSP block is disabled, all OSP-related attributes are disabled and have no effect on the generated signal.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:OSP Enabled**
            - C Attribute: **NIFGEN_ATTR_OSP_ENABLED**

.. py:attribute:: osp_fir_filter_enabled

    Enables or disables the FIR filter.
    The NIFGEN_ATTR_OSP_CIC_FILTER_ENABLED and NIFGEN_ATTR_OSP_FIR_FILTER_ENABLED  attributes must have the same enable/disable setting.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:Advanced:FIR Filter Enabled**
            - C Attribute: **NIFGEN_ATTR_OSP_FIR_FILTER_ENABLED**

.. py:attribute:: osp_fir_filter_flat_passband

    Passband value to use when calculating the FIR filter coefficients.  The FIR filter is designed to be flat to passband × IQ rate.  This attribute is used only when the NIFGEN_ATTR_OSP_FIR_FILTER_TYPE  attribute is set to NIFGEN_VAL_OSP_FLAT.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Flat:Passband**
            - C Attribute: **NIFGEN_ATTR_OSP_FIR_FILTER_FLAT_PASSBAND**

.. py:attribute:: osp_fir_filter_gaussian_bt

    BT value to use when calculating the pulse-shaping FIR filter coefficients.  Only used when the NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute is set to  NIFGEN_VAL_OSP_GAUSSIAN.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Gaussian:BT**
            - C Attribute: **NIFGEN_ATTR_OSP_FIR_FILTER_GAUSSIAN_BT**

.. py:attribute:: osp_fir_filter_interpolation

    Interpolation factor for the FIR filter. If you do not set this value,  NI-FGEN calculates the appropriate value based on the value of the NIFGEN_ATTR_OSP_IQ_RATE attribute.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:Advanced:FIR Interpolation Factor**
            - C Attribute: **NIFGEN_ATTR_OSP_FIR_FILTER_INTERPOLATION**

.. py:attribute:: osp_fir_filter_raised_cosine_alpha

    Alpha value to use when calculating the pulse shaping FIR filter  coefficients. Only used when the NIFGEN_ATTR_OSP_FIR_FILTER_TYPE  attribute is set to NIFGEN_VAL_OSP_RAISED_COSINE.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Raised Cosine:Alpha**
            - C Attribute: **NIFGEN_ATTR_OSP_FIR_FILTER_RAISED_COSINE_ALPHA**

.. py:attribute:: osp_fir_filter_root_raised_cosine_alpha

    Alpha value to use when calculating the pulse-shaping FIR filter  coefficients. This attribute is used only when the NIFGEN_ATTR_OSP_FIR_FILTER_TYPE  attribute is set to NIFGEN_VAL_OSP_ROOT_RAISED_COSINE.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Root Raised Cosine:Alpha**
            - C Attribute: **NIFGEN_ATTR_OSP_FIR_FILTER_ROOT_RAISED_COSINE_ALPHA**

.. py:attribute:: osp_fir_filter_type

    Pulse-shaping filter type for the FIR filter.

    The following table lists the characteristics of this property.

    +----------------+------------------+
    | Characteristic | Value            |
    +================+==================+
    | Datatype       | enums.FilterType |
    +----------------+------------------+
    | Permissions    | read-write       |
    +----------------+------------------+
    | Channel Based  | False            |
    +----------------+------------------+
    | Resettable     | Yes              |
    +----------------+------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Filter Type**
            - C Attribute: **NIFGEN_ATTR_OSP_FIR_FILTER_TYPE**

.. py:attribute:: osp_frequency_shift

    Specifies the amount of frequency shift applied to the baseband signal.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:Frequency Shift**
            - C Attribute: **NIFGEN_ATTR_OSP_FREQUENCY_SHIFT**

.. py:attribute:: osp_mode

    Specifies the generation mode of the OSP, which determines the type of data contained in the output signal.

    The following table lists the characteristics of this property.

    +----------------+---------------+
    | Characteristic | Value         |
    +================+===============+
    | Datatype       | enums.OSPMode |
    +----------------+---------------+
    | Permissions    | read-write    |
    +----------------+---------------+
    | Channel Based  | False         |
    +----------------+---------------+
    | Resettable     | Yes           |
    +----------------+---------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:OSP Mode**
            - C Attribute: **NIFGEN_ATTR_OSP_MODE**

.. py:attribute:: osp_overflow_error_reporting

    Configures error reporting when the OSP block detects an overflow in any of its stages.  Overflows lead to clipping of the waveform.
    You can use the NIFGEN_ATTR_OSP_OVERFLOW_STATUS attribute to query for overflow  conditions whether or not the NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING attribute is  enabled. The device will continue to generate after an overflow whether or not the  NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING attribute is enabled.

    The following table lists the characteristics of this property.

    +----------------+---------------------------------+
    | Characteristic | Value                           |
    +================+=================================+
    | Datatype       | enums.OSPOverflowErrorReporting |
    +----------------+---------------------------------+
    | Permissions    | read-write                      |
    +----------------+---------------------------------+
    | Channel Based  | False                           |
    +----------------+---------------------------------+
    | Resettable     | Yes                             |
    +----------------+---------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:Advanced:OSP Overflow Error Reporting**
            - C Attribute: **NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING**

.. py:attribute:: osp_overflow_status

    Returns a bit field of the overflow status in any stage of the OSP block.  This attribute is functional regardless of the value for the  NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING attribute.
    Write 0 to this attribute to clear the current NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING value.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:Advanced:OSP Overflow Status**
            - C Attribute: **NIFGEN_ATTR_OSP_OVERFLOW_STATUS**

.. py:attribute:: osp_pre_filter_gain_i

    Digital gain to apply to the I data stream before any filtering by the OSP block.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Gain:Pre-filter Gain I**
            - C Attribute: **NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_I**

.. py:attribute:: osp_pre_filter_gain_q

    Digital gain to apply to the Q data stream before any filtering by the OSP block.  This attribute is only used when the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute  is set to NIFGEN_VAL_OSP_COMPLEX.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Gain:Pre-filter Gain Q**
            - C Attribute: **NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_Q**

.. py:attribute:: osp_pre_filter_offset_i

    Digital offset to apply to the I data stream. This offset is applied after  the Pre-Filter Gain and before any filtering.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Offset:Pre-filter Offset I**
            - C Attribute: **NIFGEN_ATTR_OSP_PRE_FILTER_OFFSET_I**

.. py:attribute:: osp_pre_filter_offset_q

    Digital offset to apply to the Q data stream. This offset is applied after  the Pre-Filter Gain and before any filtering. This attribute is used only when  the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute is set to NIFGEN_VAL_OSP_COMPLEX.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Offset:Pre-filter Offset Q**
            - C Attribute: **NIFGEN_ATTR_OSP_PRE_FILTER_OFFSET_Q**

.. py:attribute:: output_enabled

    This channel-based attribute specifies whether the signal that the signal generator produces appears at the output connector.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Output Enabled**
            - C Attribute: **NIFGEN_ATTR_OUTPUT_ENABLED**

.. py:attribute:: output_impedance

    This channel-based attribute specifies the signal generator output impedance at the output connector. NI signal sources modules have an output impedance of 50 ohms and an optional 75 ohms on select modules. If the load impedance matches the output impedance, then the voltage at the signal output connector is at the needed level. The voltage at the signal output connector varies with load output impedance, up to doubling the voltage for a high-impedance load.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Output Impedance**
            - C Attribute: **NIFGEN_ATTR_OUTPUT_IMPEDANCE**

.. py:attribute:: output_mode

    Sets which output mode the signal generator will use. The value you specify determines which functions and attributes you use to configure the waveform the signal generator produces.



    .. note:: The signal generator must not be in the Generating state when you change this attribute. To change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.

    The following table lists the characteristics of this property.

    +----------------+------------------+
    | Characteristic | Value            |
    +================+==================+
    | Datatype       | enums.OutputMode |
    +----------------+------------------+
    | Permissions    | read-write       |
    +----------------+------------------+
    | Channel Based  | False            |
    +----------------+------------------+
    | Resettable     | No               |
    +----------------+------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Output Mode**
            - C Attribute: **NIFGEN_ATTR_OUTPUT_MODE**

.. py:attribute:: p2p_endpoint_fullness_start_trigger_level

    Specifies the Endpoint threshold for the Start trigger. This attribute is used only when NIFGEN_ATTR_START_TRIGGER_TYPE is set to P2P Endpoint Fullness.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Start:P2P Endpoint Fullness:Level**
            - C Attribute: **NIFGEN_ATTR_P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL**

.. py:attribute:: pci_dma_optimizations_enabled

    Controls whether or not NI-FGEN allows performance optimizations for DMA transfers.
    This attribute is only valid for PCI and PXI SMC-based devices.
    This attribute is enabled (VI_TRUE) by default, and NI recommends leaving it enabled.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Advanced:PCI DMA Optimizations Enabled**
            - C Attribute: **NIFGEN_ATTR_PCI_DMA_OPTIMIZATIONS_ENABLED**

.. py:attribute:: post_amplifier_attenuation

    Specifies the amount of post-amplifier attenuation that should be applied to the signal (in dB).

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Calibration:Post-Amplifier Attenuation**
            - C Attribute: **NIFGEN_ATTR_POST_AMPLIFIER_ATTENUATION**

.. py:attribute:: pre_amplifier_attenuation

    Specifies the amount of pre-amplifier attenuation that should be applied to the signal (in dB).

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Calibration:Pre-Amplifier Attenuation**
            - C Attribute: **NIFGEN_ATTR_PRE_AMPLIFIER_ATTENUATION**

.. py:attribute:: range_check

    Specifies whether to validate attribute values and function parameters.  If enabled, NI-FGEN validates the parameter values that  you pass to the functions. Range-checking  parameters is very useful for debugging. After you validate your program,  you can set this attribute to VI_FALSE to disable range checking and  maximize performance.
    Default Value: VI_TRUE
    Use niFgen_InitWithOptions to override the default value.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Inherent IVI Attributes:User Options:Range Check**
            - C Attribute: **NIFGEN_ATTR_RANGE_CHECK**

.. py:attribute:: ready_for_start_event_level_active_level

    Specifies the output polarity of the Ready for Start Event.

    The following table lists the characteristics of this property.

    +----------------+-------------------------------------+
    | Characteristic | Value                               |
    +================+=====================================+
    | Datatype       | enums.ReadyForStartEventActiveLevel |
    +----------------+-------------------------------------+
    | Permissions    | read-write                          |
    +----------------+-------------------------------------+
    | Channel Based  | False                               |
    +----------------+-------------------------------------+
    | Resettable     | Yes                                 |
    +----------------+-------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Ready For Start:Level:Active Level**
            - C Attribute: **NIFGEN_ATTR_READY_FOR_START_EVENT_LEVEL_ACTIVE_LEVEL**

.. py:attribute:: ready_for_start_event_live_status

    Returns the live status of the specified Ready For Start Event.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | bool      |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Ready For Start:Advanced:Live Status**
            - C Attribute: **NIFGEN_ATTR_READY_FOR_START_EVENT_LIVE_STATUS**

.. py:attribute:: ready_for_start_event_output_terminal

    Specifies the destination terminal for the Ready for Start Event.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Ready For Start:Output Terminal**
            - C Attribute: **NIFGEN_ATTR_READY_FOR_START_EVENT_OUTPUT_TERMINAL**

.. py:attribute:: record_coercions

    Specifies whether the IVI Engine keeps a list of  the value coercions it makes for ViInt32 and ViReal64 attributes.   Call niFgen_GetNextCoercionRecord to extract and delete the oldest  coercion record from the list.
    Default Value: VI_FALSE
    Use niFgen_InitWithOptions to override default value.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Inherent IVI Attributes:User Options:Record Value Coercions**
            - C Attribute: **NIFGEN_ATTR_RECORD_COERCIONS**

.. py:attribute:: reference_clock_source

    Specifies the reference clock source used by the signal generator.
    The signal generator derives the frequencies and sample rates that it uses  to generate waveforms from the source you specify.  For example, when you set this attribute to ClkIn, the signal  generator uses the signal it receives at the CLK IN front  panel connector as the Reference clock.
    To change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.



    .. note:: The signal generator must not be in the Generating state when you change this attribute.

    The following table lists the characteristics of this property.

    +----------------+----------------------------+
    | Characteristic | Value                      |
    +================+============================+
    | Datatype       | enums.ReferenceClockSource |
    +----------------+----------------------------+
    | Permissions    | read-write                 |
    +----------------+----------------------------+
    | Channel Based  | False                      |
    +----------------+----------------------------+
    | Resettable     | Yes                        |
    +----------------+----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Reference Clock:Source**
            - C Attribute: **NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE**

.. py:attribute:: ref_clock_frequency

    Sets the frequency of the signal generator reference  clock. The signal generator uses the reference clock to derive  frequencies and sample rates when generating output.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Reference Clock:Frequency**
            - C Attribute: **NIFGEN_ATTR_REF_CLOCK_FREQUENCY**

.. py:attribute:: sample_clock_absolute_delay

    Specifies the absolute delay adjustment of the sample clock. The  sample clock delay adjustment is expressed in seconds.
    can only be applied when an external sample clock is used.



    .. note:: For the NI 5421, absolute delay

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Advanced:Sample Clock Absolute Delay**
            - C Attribute: **NIFGEN_ATTR_SAMPLE_CLOCK_ABSOLUTE_DELAY**

.. py:attribute:: sample_clock_source

    Specifies the Sample clock source. If you specify a divisor with the NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_DIVISOR  attribute, the Sample clock exported with the NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL attribute is the  value of the Sample clock after it is divided-down. For a list of the terminals available on your device, refer  to the Device Routes tab in MAX.
    To change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.



    .. note:: The signal generator must not be in the Generating state when you change this attribute.

    The following table lists the characteristics of this property.

    +----------------+-------------------------+
    | Characteristic | Value                   |
    +================+=========================+
    | Datatype       | enums.SampleClockSource |
    +----------------+-------------------------+
    | Permissions    | read-write              |
    +----------------+-------------------------+
    | Channel Based  | False                   |
    +----------------+-------------------------+
    | Resettable     | Yes                     |
    +----------------+-------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Sample Clock:Source**
            - C Attribute: **NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE**

.. py:attribute:: sample_clock_timebase_rate

    Specifies the Sample clock timebase rate. This attribute applies only to external Sample clock timebases.
    To change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.



    .. note:: The signal generator must not be in the Generating state when you change this attribute.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Sample Clock Timebase:Rate**
            - C Attribute: **NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_RATE**

.. py:attribute:: sample_clock_timebase_source

    Specifies the Sample Clock Timebase source.
    To change the device configuration, call the niFgen_AbortGeneration function or wait for the generation to complete.



    .. note:: The signal generator must not be in the Generating state when you change this attribute.

    The following table lists the characteristics of this property.

    +----------------+---------------------------------+
    | Characteristic | Value                           |
    +================+=================================+
    | Datatype       | enums.SampleClockTimebaseSource |
    +----------------+---------------------------------+
    | Permissions    | read-write                      |
    +----------------+---------------------------------+
    | Channel Based  | False                           |
    +----------------+---------------------------------+
    | Resettable     | Yes                             |
    +----------------+---------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Sample Clock Timebase:Source**
            - C Attribute: **NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_SOURCE**

.. py:attribute:: script_to_generate

    Specifies which script the generator produces. To configure the generator to run a particular script, set this attribute to the name of the script. Use niFgen_WriteScript to create multiple scripts. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_SCRIPT.



    .. note:: The signal generator must not be in the Generating state when you change this attribute. To change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Script Mode:Script to Generate**
            - C Attribute: **NIFGEN_ATTR_SCRIPT_TO_GENERATE**

.. py:attribute:: script_triggers_count

    Specifies the number of Script triggers supported by the device. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_SCRIPT.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Script Triggers Count**
            - C Attribute: **NIFGEN_ATTR_SCRIPT_TRIGGERS_COUNT**

.. py:attribute:: script_trigger_type

    Specifies the Script trigger type. Depending upon the value of this attribute, additional attributes may need to be configured to fully configure the trigger.

    The following table lists the characteristics of this property.

    +----------------+-------------------------+
    | Characteristic | Value                   |
    +================+=========================+
    | Datatype       | enums.ScriptTriggerType |
    +----------------+-------------------------+
    | Permissions    | read-write              |
    +----------------+-------------------------+
    | Channel Based  | False                   |
    +----------------+-------------------------+
    | Resettable     | Yes                     |
    +----------------+-------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Script:Trigger Type**
            - C Attribute: **NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE**

.. py:attribute:: serial_number

    The signal generator's serial number.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Serial Number**
            - C Attribute: **NIFGEN_ATTR_SERIAL_NUMBER**

.. py:attribute:: simulate

    Specifies whether to simulate NI-FGEN I/O  operations. If simulation is enabled, NI-FGEN  functions perform range checking and call Ivi_GetAttribute and  Ivi_SetAttribute, but they do not perform device I/O.   For output parameters that represent device data, NI-FGEN  functions return calculated values.
    Default Value: VI_FALSE
    Use niFgen_InitWithOptions to override default value.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Inherent IVI Attributes:User Options:Simulate**
            - C Attribute: **NIFGEN_ATTR_SIMULATE**

.. py:attribute:: specific_driver_class_spec_major_version

    Returns the major version number of the class specification with which NI-FGEN is compliant.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Inherent IVI Attributes:Driver Identification:Class Specification Major Version**
            - C Attribute: **NIFGEN_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION**

.. py:attribute:: specific_driver_class_spec_minor_version

    Returns the minor version number of the class specification with which NI-FGEN is compliant.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Inherent IVI Attributes:Driver Identification:Class Specification Minor Version**
            - C Attribute: **NIFGEN_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION**

.. py:attribute:: specific_driver_description

    Returns a brief description of NI-FGEN.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Inherent IVI Attributes:Driver Identification:Description**
            - C Attribute: **NIFGEN_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

.. py:attribute:: specific_driver_revision

    A string that contains additional version information about  NI-FGEN.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Inherent IVI Attributes:Driver Identification:Revision**
            - C Attribute: **NIFGEN_ATTR_SPECIFIC_DRIVER_REVISION**

.. py:attribute:: specific_driver_vendor

    A string that contains the name of the vendor that supplies NI-FGEN.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Inherent IVI Attributes:Driver Identification:Driver Vendor**
            - C Attribute: **NIFGEN_ATTR_SPECIFIC_DRIVER_VENDOR**

.. py:attribute:: started_event_delay

    Specifies the amount of delay applied to a Started Event with respect to the  analog output of the signal generator. A positive delay value specifies that  the Started Event occurs after the analog data, and a negative delay  value specifies that the Started Event occurs before the analog data.  The default value is zero, which will align the Started event with the analog output.
    You can specify the units of the delay value by setting the NIFGEN_ATTR_STARTED_EVENT_DELAY attribute.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Started:Advanced:Delay Value**
            - C Attribute: **NIFGEN_ATTR_STARTED_EVENT_DELAY**

.. py:attribute:: started_event_delay_units

    Specifies the units applied to the value of the NIFGEN_ATTR_STARTED_EVENT_DELAY
    attribute.  Valid units are seconds and sample clock periods.

    The following table lists the characteristics of this property.

    +----------------+------------------------------+
    | Characteristic | Value                        |
    +================+==============================+
    | Datatype       | enums.StartedEventDelayUnits |
    +----------------+------------------------------+
    | Permissions    | read-write                   |
    +----------------+------------------------------+
    | Channel Based  | False                        |
    +----------------+------------------------------+
    | Resettable     | Yes                          |
    +----------------+------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Started:Advanced:Delay Units**
            - C Attribute: **NIFGEN_ATTR_STARTED_EVENT_DELAY_UNITS**

.. py:attribute:: started_event_latched_status

    Specifies the latched status of the Started Event.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | bool      |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Started:Advanced:Latched Status**
            - C Attribute: **NIFGEN_ATTR_STARTED_EVENT_LATCHED_STATUS**

.. py:attribute:: started_event_level_active_level

    Specifies the output polarity of the Started Event.

    The following table lists the characteristics of this property.

    +----------------+-------------------------------+
    | Characteristic | Value                         |
    +================+===============================+
    | Datatype       | enums.StartedEventActiveLevel |
    +----------------+-------------------------------+
    | Permissions    | read-write                    |
    +----------------+-------------------------------+
    | Channel Based  | False                         |
    +----------------+-------------------------------+
    | Resettable     | Yes                           |
    +----------------+-------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Started:Level:Active Level**
            - C Attribute: **NIFGEN_ATTR_STARTED_EVENT_LEVEL_ACTIVE_LEVEL**

.. py:attribute:: started_event_output_behavior

    Specifies the output behavior for the Started Event.

    The following table lists the characteristics of this property.

    +----------------+----------------------------------+
    | Characteristic | Value                            |
    +================+==================================+
    | Datatype       | enums.StartedEventOutputBehavior |
    +----------------+----------------------------------+
    | Permissions    | read-write                       |
    +----------------+----------------------------------+
    | Channel Based  | False                            |
    +----------------+----------------------------------+
    | Resettable     | Yes                              |
    +----------------+----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Started:Output Behavior**
            - C Attribute: **NIFGEN_ATTR_STARTED_EVENT_OUTPUT_BEHAVIOR**

.. py:attribute:: started_event_output_terminal

    Specifies the destination terminal for the Started Event.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Started:Output Terminal**
            - C Attribute: **NIFGEN_ATTR_STARTED_EVENT_OUTPUT_TERMINAL**

.. py:attribute:: started_event_pulse_polarity

    Specifies the output polarity of the Started Event.

    The following table lists the characteristics of this property.

    +----------------+---------------------------------+
    | Characteristic | Value                           |
    +================+=================================+
    | Datatype       | enums.StartedEventPulsePolarity |
    +----------------+---------------------------------+
    | Permissions    | read-write                      |
    +----------------+---------------------------------+
    | Channel Based  | False                           |
    +----------------+---------------------------------+
    | Resettable     | Yes                             |
    +----------------+---------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Started:Pulse:Polarity**
            - C Attribute: **NIFGEN_ATTR_STARTED_EVENT_PULSE_POLARITY**

.. py:attribute:: started_event_pulse_width

    Specifies the pulse width for the Started Event.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Started:Pulse:Width Value**
            - C Attribute: **NIFGEN_ATTR_STARTED_EVENT_PULSE_WIDTH**

.. py:attribute:: started_event_pulse_width_units

    Specifies the pulse width units for the Started Event.

    The following table lists the characteristics of this property.

    +----------------+-----------------------------------+
    | Characteristic | Value                             |
    +================+===================================+
    | Datatype       | enums.StartedEventPulseWidthUnits |
    +----------------+-----------------------------------+
    | Permissions    | read-write                        |
    +----------------+-----------------------------------+
    | Channel Based  | False                             |
    +----------------+-----------------------------------+
    | Resettable     | Yes                               |
    +----------------+-----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Started:Pulse:Width Units**
            - C Attribute: **NIFGEN_ATTR_STARTED_EVENT_PULSE_WIDTH_UNITS**

.. py:attribute:: start_trigger_type

    Specifies whether you want the Start trigger to be a Digital Edge, or Software trigger. You can also choose None as the value for this attribute.

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | enums.StartTriggerType |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | False                  |
    +----------------+------------------------+
    | Resettable     | Yes                    |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Start:Trigger Type**
            - C Attribute: **NIFGEN_ATTR_START_TRIGGER_TYPE**

.. py:attribute:: streaming_space_available_in_waveform

    Indicates the space available (in samples) in the streaming waveform for writing new data. During generation, this available space may be in multiple locations with, for example, part of the available space at the end of the streaming waveform and the rest at the beginning. In this situation, writing a block of waveform data the size of the  total space available in the streaming waveform causes NI-FGEN to return an error, as  NI-FGEN will not wrap the data from the end of the waveform to the beginning and cannot write data past the end of the waveform buffer.
    To avoid writing data past the end of the waveform, write new data to the waveform in a fixed size that is an integer divisor of the total size of the streaming waveform.
    Used in conjunction with the NIFGEN_ATTR_STREAMING_WAVEFORM_HANDLE or NIFGEN_ATTR_STREAMING_WAVEFORM_NAME attributes.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Streaming:Space Available in Streaming Waveform**
            - C Attribute: **NIFGEN_ATTR_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM**

.. py:attribute:: streaming_waveform_handle

    Specifies the waveform handle of the waveform used to continuously stream data during generation. This attribute defaults to -1 when no streaming waveform is specified.
    Used in conjunction with NIFGEN_ATTR_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Streaming:Streaming Waveform Handle**
            - C Attribute: **NIFGEN_ATTR_STREAMING_WAVEFORM_HANDLE**

.. py:attribute:: streaming_waveform_name

    Specifies the name of the waveform used to continuously stream data during generation. This attribute defaults to // when no streaming waveform is specified.
    Use in conjunction with NIFGEN_ATTR_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Streaming:Streaming Waveform Name**
            - C Attribute: **NIFGEN_ATTR_STREAMING_WAVEFORM_NAME**

.. py:attribute:: streaming_write_timeout

    Specifies the maximum amount of time allowed to complete a streaming write operation.

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | datetime.timedelta |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | Yes                |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Streaming:Streaming Write Timeout**
            - C Attribute: **NIFGEN_ATTR_STREAMING_WRITE_TIMEOUT**

.. py:attribute:: supported_instrument_models

    Returns a model code of the device. For NI-FGEN versions that support more than one device, this  attribute contains a comma-separated list of supported device  models.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | str       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models**
            - C Attribute: **NIFGEN_ATTR_SUPPORTED_INSTRUMENT_MODELS**

.. py:attribute:: synchronization

    Specify the source of the synchronization signal that you want to use.

    The following table lists the characteristics of this property.

    +----------------+-----------------------------+
    | Characteristic | Value                       |
    +================+=============================+
    | Datatype       | enums.SynchronizationSource |
    +----------------+-----------------------------+
    | Permissions    | read-write                  |
    +----------------+-----------------------------+
    | Channel Based  | False                       |
    +----------------+-----------------------------+
    | Resettable     | No                          |
    +----------------+-----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:5401/5411/5431:Synchronization Source**
            - C Attribute: **NIFGEN_ATTR_SYNCHRONIZATION**

.. py:attribute:: sync_duty_cycle_high

    Controls the duty cycle of the square wave the signal generator  produces on the SYNC out line.  Specify this attribute as a  percentage of the time the square wave is high in each cycle.
    Units: Percentage of time the waveform is high

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Standard Function:Sync Duty Cycle High**
            - C Attribute: **NIFGEN_ATTR_SYNC_DUTY_CYCLE_HIGH**

.. py:attribute:: sync_out_output_terminal

    Specifies the terminal to which to export the SYNC OUT signal. This attribute is not supported for all devices.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Standard Function:Sync Out Output Terminal**
            - C Attribute: **NIFGEN_ATTR_SYNC_OUT_OUTPUT_TERMINAL**

.. py:attribute:: terminal_configuration

    Specifies whether gain and offset values will be analyzed based on single-ended or differential operation.

    The following table lists the characteristics of this property.

    +----------------+-----------------------------+
    | Characteristic | Value                       |
    +================+=============================+
    | Datatype       | enums.TerminalConfiguration |
    +----------------+-----------------------------+
    | Permissions    | read-write                  |
    +----------------+-----------------------------+
    | Channel Based  | False                       |
    +----------------+-----------------------------+
    | Resettable     | Yes                         |
    +----------------+-----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Terminal Configuration**
            - C Attribute: **NIFGEN_ATTR_TERMINAL_CONFIGURATION**

.. py:attribute:: trigger_mode

    Controls the trigger mode.

    The following table lists the characteristics of this property.

    +----------------+-------------------+
    | Characteristic | Value             |
    +================+===================+
    | Datatype       | enums.TriggerMode |
    +----------------+-------------------+
    | Permissions    | read-write        |
    +----------------+-------------------+
    | Channel Based  | False             |
    +----------------+-------------------+
    | Resettable     | No                |
    +----------------+-------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Trigger Mode**
            - C Attribute: **NIFGEN_ATTR_TRIGGER_MODE**

.. py:attribute:: trigger_source

    Controls which trigger source the signal generator uses.
    After you call the niFgen_InitiateGeneration function, the signal generator waits for the trigger that you specify in the triggerSource parameter. After the signal generator receives a trigger, it produces the number of cycles that you specify in the NIFGEN_ATTR_CYCLE_COUNT attribute.
    This attribute is also the source for the trigger in the other trigger modes as specified by the NIFGEN_ATTR_TRIGGER_MODE attribute.

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | enums.TriggerSource |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | Yes                 |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:5401/5411/5431:Trigger Source**
            - C Attribute: **NIFGEN_ATTR_TRIGGER_SOURCE**

.. py:attribute:: video_waveform_type

    Selects which waveform type that the NI 5431 generates. Setting this attribute ensures that the crystal is set to the proper frequency.

    The following table lists the characteristics of this property.

    +----------------+-------------------------+
    | Characteristic | Value                   |
    +================+=========================+
    | Datatype       | enums.VideoWaveformType |
    +----------------+-------------------------+
    | Permissions    | read-write              |
    +----------------+-------------------------+
    | Channel Based  | False                   |
    +----------------+-------------------------+
    | Resettable     | No                      |
    +----------------+-------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:5401/5411/5431:Video Waveform Type**
            - C Attribute: **NIFGEN_ATTR_VIDEO_WAVEFORM_TYPE**

.. py:attribute:: wait_behavior

    Specifies the behavior of the output while waiting for a script trigger or during a wait instruction.  The output can be configured to hold the last generated voltage before waiting or jump to the Wait Value.

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | enums.WaitBehavior |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | Yes                |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Advanced:Wait Behavior**
            - C Attribute: **NIFGEN_ATTR_WAIT_BEHAVIOR**

.. py:attribute:: wait_value

    Specifies the value to generate while waiting.  The Wait Behavior must be configured to jump to this value.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | Yes        |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Advanced:Wait Value**
            - C Attribute: **NIFGEN_ATTR_WAIT_VALUE**

.. py:attribute:: waveform_quantum

    The size of each arbitrary waveform must be a multiple of a quantum value. This attribute returns the quantum value that the signal generator allows.
    For example, when this attribute returns a value of 8, all waveform sizes must be a multiple of 8. Typically, this value is constant for the signal generator.

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | False     |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Capabilities:Waveform Quantum**
            - C Attribute: **NIFGEN_ATTR_WAVEFORM_QUANTUM**


