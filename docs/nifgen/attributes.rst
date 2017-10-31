nifgen.Session properties
=========================

.. py:currentmodule:: nifgen

.. py:attribute:: all_marker_events_latched_status

    Returns a bit field of the latched status of all Marker Events. Set this
    property to 0 to clear the latched status of all Marker Events.

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

    Specifies the mask to apply to the analog output data. The masked data
    is replaced with the data in the `Analog Static
    Value <pniFgen_AnalogStaticValue.html>`__ property.

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

    Specifies whether the signal generator applies an analog filter to the
    output signal. Set this property to TRUE to enable the filter. This
    property is valid in Arbitrary Waveform, Arbitrary Sequence, and Script
    output modes. You also can use this property in Standard Function and
    Frequency List output modes for user-defined waveforms.

    **Default Value**: FALSE

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

    Specifies the analog signal path. The main path allows the user to
    configure gain, offset, analog filter status, output impedance, and
    output enable.

    The direct path presents a much smaller gain range, and you cannot
    adjust offset or the filter status. The direct path provides a smaller
    output range but lower distortion. The main path has two amplifier
    options, high and low gain. Setting this value to
    **NIFGEN\_VAL\_MAIN\_ANALOG\_PATH** allows NI-FGEN to choose the
    amplifier based on the user-specified gain.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

    The following table lists the characteristics of this property.

    +----------------+-----------------------+
    | Characteristic | Value                 |
    +================+=======================+
    | Datatype       | :py:data:`AnalogPath` |
    +----------------+-----------------------+
    | Permissions    | read-write            |
    +----------------+-----------------------+
    | Channel Based  | False                 |
    +----------------+-----------------------+
    | Resettable     | Yes                   |
    +----------------+-----------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Analog Path**
            - C Attribute: **NIFGEN_ATTR_ANALOG_PATH**

.. py:attribute:: analog_static_value

    Specifies the static value that replaces data masked by the `Analog Data
    Mask <pniFgen_AnalogDataMask.html>`__ property.

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

    Specifies the factor by which the signal generator scales the arbitrary
    waveform data. When you create arbitrary waveforms, you must first
    normalize the data points to the range -1.0 to +1.0. Use this property
    to scale the arbitrary waveform to other ranges.

    For example, when you set this property to 2.0, the output signal ranges
    from -2.0 V to +2.0 V.

    Use this property when the `Output Mode <pniFgen_OutputMode.html>`__
    property is set to **NIFGEN\_VAL\_OUTPUT\_ARB** or
    **NIFGEN\_VAL\_OUTPUT\_SEQ**.

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

    Specifies the position for a marker to be asserted in the arbitrary
    waveform.

    Use this property when the `Output Mode <pniFgen_OutputMode.html>`__
    property is set to **NIFGEN\_VAL\_OUTPUT\_ARB**. Use the `niFgen Export
    Signal <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Export_Signal.html')>`__
    VI to export the marker signal.

    **Default Value**: -1

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

    Specifies the value the signal generator adds to the arbitrary waveform
    data. When you create arbitrary waveforms, you must first normalize the
    data points to the range -1.0 to +1.0. Use this property to shift the
    arbitrary waveform range.

    For example, when you set this property to 1.0, the output signal ranges
    from 0.0 V to 2.0 V.

    Use this property when the `Output Mode <pniFgen_OutputMode.html>`__
    property is set to **NIFGEN\_VAL\_OUTPUT\_ARB** or
    **NIFGEN\_VAL\_OUTPUT\_SEQ**.

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

    Specifies the number of times to repeat the arbitrary waveform when the
    **Trigger Mode** parameter in the `niFgen Configure Trigger
    Mode <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Configure_Trigger_Mode.html')>`__
    VI is set to **Single** or **Stepped**.

    This property is ignored if the **Trigger Mode** parameter is set to
    **Continuous** or **Burst**. Use this property when the `Output
    Mode <pniFgen_OutputMode.html>`__ property is set to
    **NIFGEN\_VAL\_OUTPUT\_ARB**.

    When used during
    `streaming <javascript:LaunchHelp('SigGenHelp.chm::/streaming.html')>`__
    operations, this property specifies the number of times to repeat the
    streaming waveform (the onboard memory allocated for streaming).

    **Default Value**: 1

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

    Specifies the rate, in samples per second, at which the signal generator
    generates the points in arbitrary waveforms.

    Use this property when the `Output Mode <pniFgen_OutputMode.html>`__
    property is set to **NIFGEN\_VAL\_OUTPUT\_ARB** or
    **NIFGEN\_VAL\_OUTPUT\_SEQ**.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Selects which sequence the signal generator produces. You can create
    multiple sequences using the `niFgen Create Arbitrary
    Sequence <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Create_Arbitrary_Sequence.html')>`__
    VI.

    The niFgen Create Arbitrary Sequence VI returns a **Sequence Handle**
    that you use to identify the particular sequence. To configure the
    signal generator to produce a particular sequence, set this property to
    the **Sequence Handle** value. Use this property when the `Output
    Mode <pniFgen_OutputMode.html>`__ property is set to
    **NIFGEN\_VAL\_OUTPUT\_SEQ**.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Selects which arbitrary waveform the signal generator produces. You can
    create multiple arbitrary waveforms using the `niFgen Create
    Waveform <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Create_Waveform_poly.html')>`__
    VI.

    The `niFgen Create
    Waveform <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Create_Waveform_poly.html')>`__
    VI, `niFgen Allocate
    Waveform <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Allocate_Waveform.html')>`__
    VI, and similar VIs return a **Waveform Handle** that you use to
    identify the particular waveform. To configure the signal generator to
    produce a particular waveform, set this property to the **Waveform
    Handle** value.

    Use this property only when the `Output
    Mode <pniFgen_OutputMode.html>`__ property is set to
    **NIFGEN\_VAL\_OUTPUT\_ARB**.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Controls the specified auxiliary power pin. Setting this property to
    TRUE energizes the auxiliary power when the session is committed. When
    this property is FALSE, the power pin of the connector outputs no power.

    **Default Value**: FALSE

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

    Returns the bus type of the signal generator.

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | :py:data:`BusType` |
    +----------------+--------------------+
    | Permissions    | read only          |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Bus Type**
            - C Attribute: **NIFGEN_ATTR_BUS_TYPE**

.. py:attribute:: cache

    Specifies whether to cache the value of properties.

    When caching is enabled (TRUE), NI-FGEN keeps track of the current
    instrument settings and avoids sending redundant commands to the
    instrument. Thus, you can significantly increase execution speed.
    NI-FGEN can choose always to cache or never to cache particular
    properties regardless of the setting of this property. Use the `niFgen
    Initialize With
    Options <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize_With_Options.html')>`__
    VI to override this value.

    **Default Value**: TRUE

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

    Specifies the input of the calibration ADC. The ADC can take a reading
    from several inputs: the analog output, a 2.5 V reference, and ground.
    The latter two inputs are used to calibrate the ADC itself.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | :py:data:`CalADCInput` |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | False                  |
    +----------------+------------------------+
    | Resettable     | Yes                    |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:Calibration:Cal ADC Input**
            - C Attribute: **NIFGEN_ATTR_CAL_ADC_INPUT**

.. py:attribute:: channel_count

    Returns the number of channels that NI-FGEN supports. For each property
    for which IVI\_VAL\_MULTI\_CHANNEL is set, the IVI engine maintains a
    separate cache value for each channel.

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
            - C Attribute: **NIFGEN_ATTR_CHANNEL_COUNT**

.. py:attribute:: channel_delay

    Specifies the delay to apply to the analog output of the channel
    specified by the `Active Channel <pniFgen_ActiveChannel.html>`__
    property.

    You can use the output delay to configure the timing relationship
    between channels on a multichannel device. Values for this property can
    be zero or positive. A value of zero indicates that the channels are
    aligned. A positive value delays the analog output by the specified
    number of seconds.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Specifies the Sample Clock mode for the signal generator.

    For signal generators that support it, this property allows switching
    the Sample Clock to a high-resolution clocking mode. When in divide-down
    sampling mode, the sample rate can be set only to certain frequencies,
    based on dividing down the Sample Clock. However, in high-resolution
    mode, the sample rate may be set to any value.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

    The following table lists the characteristics of this property.

    +----------------+----------------------+
    | Characteristic | Value                |
    +================+======================+
    | Datatype       | :py:data:`ClockMode` |
    +----------------+----------------------+
    | Permissions    | read-write           |
    +----------------+----------------------+
    | Channel Based  | False                |
    +----------------+----------------------+
    | Resettable     | Yes                  |
    +----------------+----------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Sample Clock:Mode**
            - C Attribute: **NIFGEN_ATTR_CLOCK_MODE**

.. py:attribute:: common_mode_offset

    Specifies the value the signal generator adds to or subtracts from the
    arbitrary waveform data. This property applies only when set the
    `Terminal Configuration <pniFgen_TerminalConfiguration.html>`__ property
    to **Differential**. Common-mode offset is applied to the signals
    generated at each differential output terminal.

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

    Specifies the output polarity of the Data Marker Event. Refer to `Data
    Marker
    Events <javascript:LaunchHelp('SigGenHelp.chm::/events_data_markers.html')>`__
    topic for more information about Data Marker Event polarity.

    The following table lists the characteristics of this property.

    +----------------+-----------------------------------------+
    | Characteristic | Value                                   |
    +================+=========================================+
    | Datatype       | :py:data:`DataMarkerEventLevelPolarity` |
    +----------------+-----------------------------------------+
    | Permissions    | read-write                              |
    +----------------+-----------------------------------------+
    | Channel Based  | False                                   |
    +----------------+-----------------------------------------+
    | Resettable     | Yes                                     |
    +----------------+-----------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Data Marker:Level:Active Level**
            - C Attribute: **NIFGEN_ATTR_DATA_MARKER_EVENT_LEVEL_POLARITY**

.. py:attribute:: data_marker_event_output_terminal

    Specifies the destination terminal for the Data Marker Event. For a list
    of the terminals available on your device, refer to the Routes topic for
    your device or the **Device Routes** tab in MAX.



    .. note:: NI recommends using a data sample rate of less than 200 MS/s for data
        markers routed to RTSI. Faster sample rates may lead to unwanted
        behavior.

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

    Specifies the number of samples at a time to download to onboard memory.
    This property is useful when the total data to be transferred to onboard
    memory is large.

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

    Specifies the maximum amount of bus bandwidth to use for data transfers.

    The signal generator limits data transfer speeds on the PCI Express bus
    to the value you specify for this property. Set this property to
    optimize bus bandwidth usage for multidevice streaming applications by
    preventing the signal generator from consuming all the available
    bandwidth on a PCI Express link when waveforms are being written to the
    onboard memory of the device.

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

    Specifies the maximum number of concurrent PCI Express read requests the
    signal generator can issue.

    When transferring data from computer memory to device onboard memory
    across the PCI Express bus, the signal generator can issue multiple
    memory reads at the same time. In general, the larger the number of read
    requests, the more efficiently the device uses the bus because the
    multiple read requests keep the data flowing, even in a PCI Express
    topology that has high latency due to PCI Express switches in the data
    path. Most NI devices can issue a large number of read requests
    (typically 8 or 16). By default, this property is set to the highest
    value the signal generator supports.

    If other devices in your system cannot tolerate long data latencies, it
    may be helpful to decrease the number of in-flight read requests the NI
    signal generator issues. This change helps to reduce the amount of data
    the signal generator reads at one time.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Specifies the preferred size of the data field in a PCI Express read
    request packet.

    In general, the larger the packet size, the more efficiently the device
    uses the bus. By default, NI signal generators use the largest packet
    size allowed by the system. However, due to different system
    implementations, some systems may perform better with smaller packet
    sizes.

    Recommended values for this property are powers of two between 64 and
    512.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Specifies the mask to apply to the output on the digital connector. The
    masked data is replaced with the data in the `Digital Static
    Value <pniFgen_DigitalStaticValue.html>`__ property.

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

    Specifies the active edge for the Script Trigger. This property is used
    when the `Script Trigger Type <pniFgen_ScriptTriggerType.html>`__
    property is set to **Digital Edge**.

    The following table lists the characteristics of this property.

    +----------------+-----------------------------------------+
    | Characteristic | Value                                   |
    +================+=========================================+
    | Datatype       | :py:data:`ScriptTriggerDigitalEdgeEdge` |
    +----------------+-----------------------------------------+
    | Permissions    | read-write                              |
    +----------------+-----------------------------------------+
    | Channel Based  | False                                   |
    +----------------+-----------------------------------------+
    | Resettable     | Yes                                     |
    +----------------+-----------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Script:Digital Edge:Edge**
            - C Attribute: **NIFGEN_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE**

.. py:attribute:: digital_edge_script_trigger_source

    Specifies the source terminal for the Script Trigger. This property is
    used when the `Script Trigger Type <pniFgen_ScriptTriggerType.html>`__
    property is set to **Digital Edge**.

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

    Specifies the active edge for the Start Trigger. This property is used
    only when the `Start Trigger Type <pniFgen_StartTriggerType.html>`__
    property is set to **Digital Edge**.

    The following table lists the characteristics of this property.

    +----------------+----------------------------------------+
    | Characteristic | Value                                  |
    +================+========================================+
    | Datatype       | :py:data:`StartTriggerDigitalEdgeEdge` |
    +----------------+----------------------------------------+
    | Permissions    | read-write                             |
    +----------------+----------------------------------------+
    | Channel Based  | False                                  |
    +----------------+----------------------------------------+
    | Resettable     | Yes                                    |
    +----------------+----------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Start:Digital Edge:Edge**
            - C Attribute: **NIFGEN_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE**

.. py:attribute:: digital_edge_start_trigger_source

    Specifies the source terminal for the Start Trigger. This property is
    used only when the `Start Trigger
    Type <pniFgen_StartTriggerType.html>`__ property is set to **Digital
    Edge**.

    You can specify any valid source terminal for this property. Valid
    sources can be found in the Routes topic for your device or in
    Measurement & Automation Explorer under the **Device Routes** tab.

    Source terminals can be specified in two ways. If your device is named
    Dev1 and your terminal is PFI0, then the terminal can be specified as a
    fully qualified terminal name, "/Dev1/PFI0". You can also specify the
    terminal using PFI 0.

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

    Specifies whether the signal generator applies a digital filter to the
    output signal. Set this property to TRUE to use a digital filter. This
    property is valid in Arbitrary Waveform, Arbitrary Sequence, and Script
    output modes. You also can use this property in Standard Function and
    Frequency List output modes for user-defined waveforms.

    **Default Value**: FALSE

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

    Specifies the interpolation factor when the `Digital Filter
    Enabled <pniFgen_DigitalFilterEnabled.html>`__ property is set to TRUE.

    **Valid Values**: 2, 4, and 8



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Specifies a factor by which the signal generator digitally multiplies
    generated data before converting it to an analog signal in the DAC. For
    a digital gain greater than 1.0, the product of digital gain times the
    generated data must be inside the range ±1.0, assuming floating point
    data. If the product exceeds these limits, the signal generator clips
    the output signal, and an error results.

    Some signal generators support both digital gain and analog gain,
    specified with the `Amplitude <pniFgen_Amplitude.html>`__ property or
    `Arbitrary Waveform Gain <pniFgen_ArbitraryWaveformGain.html>`__
    property. Digital gain can be changed during generation without the
    glitches that may occur when changing analog gains, because of relay
    switching. However, the DAC output resolution is a function of analog
    gain, so only analog gain makes full use of the resolution of the DAC.

    **Default Value**: 1

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

    Specifies the active level for the Script Trigger. This property is used
    when the `Script Trigger Type <pniFgen_ScriptTriggerType.html>`__
    property is set to **Digital Level**.

    The following table lists the characteristics of this property.

    +----------------+-------------------------------------------------+
    | Characteristic | Value                                           |
    +================+=================================================+
    | Datatype       | :py:data:`ScriptTriggerDigitalLevelActiveLevel` |
    +----------------+-------------------------------------------------+
    | Permissions    | read-write                                      |
    +----------------+-------------------------------------------------+
    | Channel Based  | False                                           |
    +----------------+-------------------------------------------------+
    | Resettable     | Yes                                             |
    +----------------+-------------------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Script:Digital Level:Active Level**
            - C Attribute: **NIFGEN_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL**

.. py:attribute:: digital_level_script_trigger_source

    Specifies the source terminal for the Script Trigger. This property is
    used when the `Script Trigger Type <pniFgen_ScriptTriggerType.html>`__
    property is set to **Digital Level**.

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

    Specifies whether the signal generator generates a digital pattern
    corresponding to the output signal. Set this property to TRUE to
    generate a digital pattern.

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

    Specifies the static value that replaces data masked by the `Digital
    Data Mask <pniFgen_DigitalDataMask.html>`__ property.

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

    Enables the device for Direct DMA writes.

    When enabled, all `niFgen Create
    Waveform <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Create_Waveform_poly.html')>`__
    VI and `niFgen Write
    Waveform <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Write_Waveform_poly.html')>`__
    VI calls that are given a data address in the Direct DMA window download
    data residing on the Direct DMA device to the instrument onboard memory.

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

    Specifies the window address (beginning of window) of the waveform data
    source. This window address is specified by your Direct DMA-compatible
    data source.

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

    Specifies the size of the memory window provided by your Direct
    DMA-compatible data source.

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

    Specifies the amount of delay applied to a Done Event with respect to
    the analog output of the signal generator.

    A positive delay value indicates that the Done Event occurs after the
    analog data, while a negative delay value indicates that the Done Event
    occurs before the analog data. A value of zero aligns the Done Event
    with the analog output.

    You can specify the units of the delay value by setting the `Delay
    Units <pniFgen_DoneEventDelayUnits.html>`__ property.

    **Default Value**: 0

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

    Specifies the units used for the `Done Event Delay
    Value <pniFgen_DoneEventDelayValue.html>`__ property.

    The following table lists the characteristics of this property.

    +----------------+--------------------------------+
    | Characteristic | Value                          |
    +================+================================+
    | Datatype       | :py:data:`DoneEventDelayUnits` |
    +----------------+--------------------------------+
    | Permissions    | read-write                     |
    +----------------+--------------------------------+
    | Channel Based  | False                          |
    +----------------+--------------------------------+
    | Resettable     | Yes                            |
    +----------------+--------------------------------+

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

    +----------------+---------------------------------+
    | Characteristic | Value                           |
    +================+=================================+
    | Datatype       | :py:data:`DoneEventActiveLevel` |
    +----------------+---------------------------------+
    | Permissions    | read-write                      |
    +----------------+---------------------------------+
    | Channel Based  | False                           |
    +----------------+---------------------------------+
    | Resettable     | Yes                             |
    +----------------+---------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Done:Level:Active Level**
            - C Attribute: **NIFGEN_ATTR_DONE_EVENT_LEVEL_ACTIVE_LEVEL**

.. py:attribute:: done_event_output_behavior

    Specifies the output behavior for the Done Event.

    The following table lists the characteristics of this property.

    +----------------+------------------------------------+
    | Characteristic | Value                              |
    +================+====================================+
    | Datatype       | :py:data:`DoneEventOutputBehavior` |
    +----------------+------------------------------------+
    | Permissions    | read-write                         |
    +----------------+------------------------------------+
    | Channel Based  | False                              |
    +----------------+------------------------------------+
    | Resettable     | Yes                                |
    +----------------+------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Done:Output Behavior**
            - C Attribute: **NIFGEN_ATTR_DONE_EVENT_OUTPUT_BEHAVIOR**

.. py:attribute:: done_event_output_terminal

    Specifies the destination terminal for the Done Event. For a list of the
    terminals available on your device, refer to the Routes topic for your
    device or the **Device Routes** tab in MAX.

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

    +----------------+-----------------------------------+
    | Characteristic | Value                             |
    +================+===================================+
    | Datatype       | :py:data:`DoneEventPulsePolarity` |
    +----------------+-----------------------------------+
    | Permissions    | read-write                        |
    +----------------+-----------------------------------+
    | Channel Based  | False                             |
    +----------------+-----------------------------------+
    | Resettable     | Yes                               |
    +----------------+-----------------------------------+

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

    +----------------+-------------------------------------+
    | Characteristic | Value                               |
    +================+=====================================+
    | Datatype       | :py:data:`DoneEventPulseWidthUnits` |
    +----------------+-------------------------------------+
    | Permissions    | read-write                          |
    +----------------+-------------------------------------+
    | Channel Based  | False                               |
    +----------------+-------------------------------------+
    | Resettable     | Yes                                 |
    +----------------+-------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Done:Pulse:Width Units**
            - C Attribute: **NIFGEN_ATTR_DONE_EVENT_PULSE_WIDTH_UNITS**

.. py:attribute:: exported_onboard_reference_clock_output_terminal

    Specifies the terminal at which to export the onboard Reference Clock.

    For a list of the terminals available on your device, refer to the
    Routes topic for your device or the **Device Routes** tab in MAX.

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

    Specifies the terminal at which to export the Reference Clock.

    For a list of the terminals available on your device, refer to the
    Routes topic for your device or the **Device Routes** tab in MAX.

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

    Specifies the factor by which to divide the update (Sample) Clock before
    it is exported.

    To export the Sample Clock, use the `niFgen Export
    Signal <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Export_Signal.html')>`__
    VI or the `Exported Sample Clock Output
    Terminal <pniFgen_ExportedSampleClockOutputTerminal.html>`__ property.

    **Valid Values**: 1 to 4,096

    **Default Value**: 1



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Specifies the terminal at which to export the Sample Clock. If you
    specify a divisor with the `Exported Sample Clock
    Divisor <pniFgen_ExportedSampleClockDivisor.html>`__ property, the
    Sample Clock exported with this property is the value of the Sample
    Clock after it is divided-down.

    For a list of the terminals available on your device, refer to the
    Routes topic for your device or the **Device Routes** tab in MAX.



    .. note:: The signal generator must not be in the Generating state when you change
        this property. To change the device configuration, call the `niFgen
        Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Specifies the factor by which to divide the device clock (Sample Clock
    timebase) before it is exported.

    To export the Sample Clock timebase, use the `niFgen Export
    Signal <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Export_Signal.html')>`__
    VI or the `Exported Sample Clock Timebase Output
    Terminal <pniFgen_ExportedSampleClockTimebaseOutputTerminal.html>`__
    property.

    **Valid Values**: 1 to 4,194,304



    .. note:: Not all devices support a divisor value of 1.

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

    Specifies the terminal at which to export the Sample Clock Timebase.

    For a list of the terminals available on your device, refer to the
    Routes topic for your device or the **Device Routes** tab in MAX.

    If you specify a divisor with the `Exported Sample Clock Timebase
    Divisor <pniFgen_ExportedSampleClockTimebaseDivisor.html>`__ property,
    the Sample Clock timebase exported with the Exported Sample Clock
    Timebase Output Terminal property is the value of the Sample Clock
    timebase after it is divided down.



    .. note:: The signal generator must not be in the Generating state when you change
        this property. To change the device configuration, call the `niFgen
        Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Specifies the output terminal for the exported Script Trigger.

    Setting this property to an empty string means that when you commit the
    session, the signal is removed from that terminal and, if possible, the
    terminal is tristated.

    For a list of the terminals available on your device, refer to the
    Routes topic for your device or the **Device Routes** tab in MAX.

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

    Specifies the destination terminal for exporting the Start Trigger.

    For a list of the terminals available on your device, refer to the
    Routes topic for your device or the **Device Routes** tab in MAX.

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

    Specifies the external clock delay binary value.

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

    Specifies a multiplication factor to use to obtain a desired sample rate
    from an external Sample Clock.

    The resulting sample rate is equal to this factor multiplied by the
    external Sample Clock rate. You can use this property to generate
    samples at a rate higher than your external clock rate. When using this
    property, you do not need to explicitly set the external clock rate.

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

    Specifies the maximum number of samples to transfer at one time from the
    device to host memory. This property is used in conjunction with the
    `niFgen Create Waveform From
    File <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Create_Waveform_poly.html')>`__
    VI and the `niFgen Write Waveform From
    File <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Write_Waveform_poly.html')>`__
    VI.

    If the requested value is not evenly divisible by the required
    increment, this property is coerced up to the next 64-sample increment
    (32-sample increment for complex samples).

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

    Specifies the filter correction frequency of the analog filter. This
    property can correct for the ripples in the analog filter frequency
    response at the frequency specified.

    When using the Standard Waveform output mode, this property should be
    set to the same frequency as the standard waveform. To disable filter
    correction, set this property to 0.

    **Units**: hertz (Hz)

    **Default Value**: 0

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

    Specify a value of TRUE to enable flatness correction. When flatness
    correction is enabled, the signal generator applies a flatness
    correction factor to the generated sine wave to ensure the same output
    power level at all frequencies.

    Set this property to FALSE when performing flatness calibration.

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

    Returns the quantum that all durations must be a multiple of in a
    frequency list.

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

    Sets which frequency list the signal generator produces. You create a
    frequency list using the `niFgen Create Frequency
    List <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Create_Frequency_List.html')>`__
    VI. The niFgen Create Frequency List VI returns a handle that you use to
    identify the list.

    **Default Value**: None



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Controls the amplitude of the standard waveform that the signal
    generator produces. This value is the amplitude at the output terminal.

    For example, to produce a waveform ranging from -5.00 V to +5.00 V, set
    Amplitude property to 10.00 V.

    **Units**: volts peak-to-peak (Vpk-pk)

    **Default Value**: None



    .. note:: This parameter does not affect signal generator behavior when you set
        the `Waveform <pniFgen_Waveform.html>`__ property to
        **NIFGEN\_VAL\_WFM\_DC**.

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

    Contains the number of samples used in the standard function waveform
    buffer.

    This property is valid only on devices that implement Standard Function
    output mode in software, and it is read-only for all other devices.



    .. note:: Refer to the `Standard Function
        Mode <javascript:LaunchHelp('SigGenHelp.chm::/Function_Generation_Mode.html')>`__
        topic in the *NI Signal Generators Help* for more information about the
        implementation of Standard Function output mode on your device.

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

    Controls the DC offset of the standard waveform that the signal
    generator produces.

    This value is the offset at the output terminal. The value is the offset
    from ground to the center of the waveform you specify with the
    `Waveform <pniFgen_Waveform.html>`__ property.

    For example, to configure a waveform with an amplitude of 10.00 V to
    range from 0.00 V to +10.00 V, set this property to 5.00 V.

    **Units**: volts (V)

    **Default Value**: None

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

    Specifies the duty cycle of the square wave the signal generator is
    producing. Specify this property as a percentage of the time the square
    wave is high in a cycle.

    **Units**: Percentage of time the waveform is high

    **Default Value**: 50%



    .. note:: This parameter only affects signal generator behavior when you set the
        `Waveform <pniFgen_Waveform.html>`__ property to
        **NIFGEN\_VAL\_WFM\_SQUARE**.

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

    Controls the frequency of the standard waveform that the signal
    generator produces.

    **Units**: hertz (Hz)

    **Default Value**: None



    .. note:: This parameter does not affect signal generator behavior when you set
        the `Waveform <pniFgen_Waveform.html>`__ property to
        **NIFGEN\_VAL\_WFM\_DC**. For **NIFGEN\_VAL\_WFM\_SINE** , the range is
        between 0 MHz and 16 MHz, but the range is between 0 MHz and 1 MHz for
        all other waveforms.

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

    Sets the maximum number of samples that can be used in the standard
    function waveform buffer. Increasing this value may increase the quality
    of the waveform but may also increase the amount of time required to
    change the waveform while running.

    This property is valid only on devices that implement Standard Function
    output mode in software, and it is read-only for all other devices.



    .. note:: Refer to the `Standard Function
        Mode <javascript:LaunchHelp('SigGenHelp.chm::/Function_Generation_Mode.html')>`__
        topic in the *NI Signal Generators Help* for more information about the
        implementation of Standard Function output mode on your device.

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

    Controls horizontal offset of the standard waveform the signal generator
    produces. Specify this property in degrees of one waveform cycle.

    A start phase of 180 degrees means output generation begins halfway
    through the waveform. A start phase of 360 degrees offsets the output by
    an entire waveform cycle, which is identical to a start phase of 0
    degrees.

    **Units**: Degrees of one cycle

    **Default Value**: None



    .. note:: This property does not affect signal generator behavior when you set the
        `Waveform <pniFgen_Waveform.html>`__ property to
        **NIFGEN\_VAL\_WFM\_DC**.

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

    Specifies which standard waveform the signal generator produces. Use
    this property only when the `Output Mode <pniFgen_OutputMode.html>`__
    property is set to **NIFGEN\_VAL\_OUTPUT\_FUNC**.

    **Default Value**: **NIFGEN\_VAL\_WFM\_DC**

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | :py:data:`Waveform` |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Standard Function:Waveform**
            - C Attribute: **NIFGEN_ATTR_FUNC_WAVEFORM**

.. py:attribute:: gain_dac_value

    Specifies the value programmed to the Gain DAC. The value should be
    treated as an unsigned, right-justified number.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Returns a comma-separated list of class-extension groups that NI-FGEN
    implements.

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

    Specifies the behavior of the output during the Idle state.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

    The following table lists the characteristics of this property.

    +----------------+-------------------------+
    | Characteristic | Value                   |
    +================+=========================+
    | Datatype       | :py:data:`IdleBehavior` |
    +----------------+-------------------------+
    | Permissions    | read-write              |
    +----------------+-------------------------+
    | Channel Based  | False                   |
    +----------------+-------------------------+
    | Resettable     | Yes                     |
    +----------------+-------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Advanced:Idle Behavior**
            - C Attribute: **NIFGEN_ATTR_IDLE_BEHAVIOR**

.. py:attribute:: idle_value

    Specifies the value to generate in the Idle state. You must set the
    `Idle Behavior <pniFgen_IdleBehavior.html>`__ property to **Jump To
    Value** to use this property.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

.. py:attribute:: instrument_firmware_revision

    Returns the firmware revision information for the instrument you are
    currently using.

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

    Returns the name of the instrument manufacturer you are currently using.

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

    Returns the model number or name of the instrument that you are
    currently using.

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

    Specifies whether to perform interchangeability checking and log
    interchangeability warnings when you call VIs. Set this property to TRUE
    to enable interchangeability checking.

    Interchangeability warnings indicate that using your application with a
    different instrument might cause different behavior. Interchangeability
    checking examines the properties in a capability group only if you
    specify a value for at least one property within that group.
    Interchangeability warnings can occur when a property affects the
    behavior of the instrument and you have not set that property or the
    property has been invalidated since you set it.

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

    Returns the resource descriptor NI-FGEN uses to identify the physical
    device.

    If you initialize NI-FGEN with a logical name, this property contains
    the resource descriptor that corresponds to the entry in the IVI
    Configuration utility.

    If you initialize NI-FGEN with the resource descriptor, this property
    contains that value.

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

    Specifies the load impedance connected to the analog output of the
    channel.

    If the load impedance is set to -1.0, NI-FGEN matches the load impedance
    to the `Output Impedance <pniFgen_OutputImpedance.html>`__ property
    value. NI-FGEN compensates to give the desired peak-to-peak voltage
    amplitude or arbitrary gain (relative to 1 V).



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Returns the logical name you specified when opening the current IVI
    session.

    You may pass a logical name to the `niFgen
    Initialize <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize.html')>`__
    VI or the `niFgen Initialize With
    Options <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize_With_Options.html')>`__
    VI. The IVI Configuration utility must contain an entry for the logical
    name. The logical name entry refers to a virtual instrument section in
    the IVI Configuration file. The virtual instrument section specifies a
    physical device and initial user options.

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

.. py:attribute:: marker_events_count

    Returns the number of markers supported by the device. Use this property
    when the `Output Mode <pniFgen_OutputMode.html>`__ property is set to
    **NIFGEN\_VAL\_OUTPUT\_SCRIPT**.

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

    Specifies the amount of delay applied to a Marker Event with respect to
    the analog output of the signal generator.

    A positive delay value indicates that the Marker Event occurs after the
    analog data, while a negative delay value indicates that the Marker
    Event occurs before the analog data. The default value is zero, which
    aligns the Marker Event with the analog output.

    You can specify the units of the delay value using the `Marker Event
    Delay Units <pniFgen_MarkerEventDelayUnits.html>`__ property.

    **Default Value**: 0

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

    Specifies the units used for the `Marker Event Delay
    Value <pniFgen_MarkerEventDelayValue.html>`__ property.

    The following table lists the characteristics of this property.

    +----------------+----------------------------------+
    | Characteristic | Value                            |
    +================+==================================+
    | Datatype       | :py:data:`MarkerEventDelayUnits` |
    +----------------+----------------------------------+
    | Permissions    | read-write                       |
    +----------------+----------------------------------+
    | Channel Based  | False                            |
    +----------------+----------------------------------+
    | Resettable     | Yes                              |
    +----------------+----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Marker:Advanced:Delay Units**
            - C Attribute: **NIFGEN_ATTR_MARKER_EVENT_DELAY_UNITS**

.. py:attribute:: marker_event_latched_status

    Specifies the latched status of the specified Marker Event. Set this
    property to FALSE to clear the latched status of the Marker Event.

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

    Returns TRUE if the status of the specified Marker Event is live, and
    FALSE otherwise.

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

    +----------------+--------------------------------------+
    | Characteristic | Value                                |
    +================+======================================+
    | Datatype       | :py:data:`MarkerEventOutputBehavior` |
    +----------------+--------------------------------------+
    | Permissions    | read-write                           |
    +----------------+--------------------------------------+
    | Channel Based  | False                                |
    +----------------+--------------------------------------+
    | Resettable     | Yes                                  |
    +----------------+--------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Marker:Output Behavior**
            - C Attribute: **NIFGEN_ATTR_MARKER_EVENT_OUTPUT_BEHAVIOR**

.. py:attribute:: marker_event_output_terminal

    Specifies the destination terminal for the Marker Event.

    For a list of the terminals available on your device, refer to the
    Routes topic for your device or the **Device Routes** tab in MAX.

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

    +----------------+-------------------------------------+
    | Characteristic | Value                               |
    +================+=====================================+
    | Datatype       | :py:data:`MarkerEventPulsePolarity` |
    +----------------+-------------------------------------+
    | Permissions    | read-write                          |
    +----------------+-------------------------------------+
    | Channel Based  | False                               |
    +----------------+-------------------------------------+
    | Resettable     | Yes                                 |
    +----------------+-------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Marker:Pulse:Polarity**
            - C Attribute: **NIFGEN_ATTR_MARKER_EVENT_PULSE_POLARITY**

.. py:attribute:: marker_event_pulse_width

    Specifies the pulse width value of the Marker Event. Set the units for
    the values with the `Marker Event Pulse Width
    Units <pniFgen_MarkerEventPulseWidthUnits.html>`__ property.

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

    Specifies the pulse width units of the Marker Event.

    The following table lists the characteristics of this property.

    +----------------+---------------------------------------+
    | Characteristic | Value                                 |
    +================+=======================================+
    | Datatype       | :py:data:`MarkerEventPulseWidthUnits` |
    +----------------+---------------------------------------+
    | Permissions    | read-write                            |
    +----------------+---------------------------------------+
    | Channel Based  | False                                 |
    +----------------+---------------------------------------+
    | Resettable     | Yes                                   |
    +----------------+---------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Marker:Pulse:Width Units**
            - C Attribute: **NIFGEN_ATTR_MARKER_EVENT_PULSE_WIDTH_UNITS**

.. py:attribute:: marker_event_toggle_initial_state

    Specifies the initial state of the Marker Event.

    The following table lists the characteristics of this property.

    +----------------+------------------------------------------+
    | Characteristic | Value                                    |
    +================+==========================================+
    | Datatype       | :py:data:`MarkerEventToggleInitialState` |
    +----------------+------------------------------------------+
    | Permissions    | read-write                               |
    +----------------+------------------------------------------+
    | Channel Based  | False                                    |
    +----------------+------------------------------------------+
    | Resettable     | Yes                                      |
    +----------------+------------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Marker:Toggle:Initial State**
            - C Attribute: **NIFGEN_ATTR_MARKER_EVENT_TOGGLE_INITIAL_STATE**

.. py:attribute:: max_freq_list_duration

    Returns the maximum duration, in seconds, of any one step in the
    frequency list.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Returns the maximum number of steps that can be in a frequency list.

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

    Returns the maximum number of times the signal generator can repeat a
    waveform in a sequence. Typically, this value is constant for the signal
    generator.

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

    Returns the maximum number of frequency lists that the signal generator
    allows.

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

    Returns the maximum number of arbitrary sequences the signal generator
    allows.

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

    Returns the maximum number of arbitrary waveforms that the signal
    generator allows. On some signal generators, this value may vary with
    remaining onboard memory.

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

    Returns the maximum number of arbitrary waveforms the signal generator
    allows in a sequence.

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

    Returns the maximum number of points the signal generator allows in an
    arbitrary waveform. On some signal generators, this value may vary with
    remaining onboard memory.

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

    Returns the amount of memory in bytes on the signal generator.

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

.. py:attribute:: min_freq_list_duration

    Returns the minimum duration, in seconds, of any one step in a frequency
    list.

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

    Returns the minimum number of frequency lists that the signal generator
    allows.

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

    Returns the minimum number of arbitrary waveforms the signal generator
    allows in a sequence. Typically, this value is constant for the signal
    generator.

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

    Returns the minimum number of points the signal generator allows in an
    arbitrary waveform. Typically, this value is constant for the signal
    generator.



    .. note:: In some cases, you may need to supply a larger waveform than the value
        specified by this property. Refer to the "Features Supported" topic for
        your device in the *NI Signal Generators Help* for a table of minimum
        waveform sizes.

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

    Returns the revision letter of the module you are using.

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

.. py:attribute:: offset_dac_value

    Specifies the value programmed to the Offset DAC. The value should be
    treated as an unsigned, right-justified number.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Specifies the value programmed to the Oscillator DAC. The value should
    be treated as an unsigned, right-justified number.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Specifies the oscillator phase DAC value.

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

    Enables (TRUE) or disables (FALSE) generation of the carrier.

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

    Specifies the frequency of the generated carrier.

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

    Specifies the I carrier phase, in degrees, at the first point of the
    generated signal.

    **Default Value**: 0.0

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

    Specifies the Q carrier phase, in degrees, at the first point of the
    generated signal. This property is used only when the `Data Processing
    Mode <pniFgen_DataProcessingMode.html>`__ property is set to
    **Complex**.

    **Default Value**: -90.0

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

    Enables (TRUE) or disables (FALSE) the CIC filter.



    .. note:: You must set the CIC Filter Enabled and `FIR Filter
        Enabled <pniFgen_FIRFilterEnabled.html>`__ properties to the same value.

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

    Specifies the gain applied at the final stage of the CIC filter. This
    property is commonly used to compensate for attenuation in the FIR
    filter. If you set the `FIR Filter Type <pniFgen_FilterType.html>`__ to
    a value other than **Custom**, NI-FGEN calculates the CIC gain to
    achieve unity gain between the FIR and CIC filters. Setting this
    property overrides the value set by NI-FGEN.

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

    Specifies the interpolation factor for the CIC filter. If you do not set
    this value, NI-FGEN calculates the appropriate value based on the value
    of the `IQ Rate <pniFgen_IQRate.html>`__ property.

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

    Adjusts for OSP filter group delay when aligning analog outputs and
    events in OSP mode. If you set this property to TRUE, event outputs
    align more closely with the analog output. The analog output also aligns
    more closely between two devices synchronized using NI-TClk.



    .. note:: Group delay is the delay that occurs as a result of passing through a
        FIR filter. At a low I/Q rate, the group delay can become so large that
        some devices may not be able to align the events with the output. In
        this case, you must increase the I/Q rate or disable this property.

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

    Controls the way that data is processed by the OSP block.



    .. note:: When using the NI 5450/5451 with I/Q rates higher than 200 MS/s, NI-FGEN
        restricts this property value to Complex.

    The following table lists the characteristics of this property.

    +----------------+-------------------------------+
    | Characteristic | Value                         |
    +================+===============================+
    | Datatype       | :py:data:`DataProcessingMode` |
    +----------------+-------------------------------+
    | Permissions    | read-write                    |
    +----------------+-------------------------------+
    | Channel Based  | False                         |
    +----------------+-------------------------------+
    | Resettable     | Yes                           |
    +----------------+-------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:Data Processing Mode**
            - C Attribute: **NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE**

.. py:attribute:: osp_enabled

    Enables (TRUE) or disables (FALSE) the OSP block of the signal
    generator. When the OSP block is disabled, all OSP-related properties
    are disabled and have no effect on the generated signal.

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

    Specify TRUE to enables the FIR filter. Specify FALSE to disable the FIR
    filter.



    .. note:: You must set the `CIC Filter Enabled <pniFgen_CICFilterEnabled.html>`__
        property and the FIR Filter Enabled property to the same value.

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

    Specifies the passband value to use when calculating the FIR filter
    coefficients. The FIR filter is designed to be flat to passband × I/Q
    rate. This property is used only when the `Filter
    Type <pniFgen_FilterType.html>`__ property is set to **Flat**.

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

    Specifies the BT value to use when calculating the pulse-shaping FIR
    filter coefficients. The BT value is the product of the -3 dB bandwidth
    and the symbol period. This property is used only when the `Filter
    Type <pniFgen_FilterType.html>`__ property is set to **Gaussian**.

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

    Specifies the interpolation factor for the FIR filter. If you do not set
    this value, NI-FGEN calculates the appropriate value based on the value
    of the `IQ Rate <pniFgen_IQRate.html>`__ property.

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

    Specifies the alpha value to use when calculating the pulse-shaping FIR
    filter coefficients. This property is used only when the `Filter
    Type <pniFgen_FilterType.html>`__ property is set to **Raised Cosine**.

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

    Specifies the alpha value to use when calculating the pulse-shaping FIR
    filter coefficients. This property is used only when the `Filter
    Type <pniFgen_FilterType.html>`__ property is set to **Root Raised
    Cosine**.

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

    Specifies the pulse-shaping filter type for the FIR filter.

    The following table lists the characteristics of this property.

    +----------------+-----------------------+
    | Characteristic | Value                 |
    +================+=======================+
    | Datatype       | :py:data:`FilterType` |
    +----------------+-----------------------+
    | Permissions    | read-write            |
    +----------------+-----------------------+
    | Channel Based  | False                 |
    +----------------+-----------------------+
    | Resettable     | Yes                   |
    +----------------+-----------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Filter Type**
            - C Attribute: **NIFGEN_ATTR_OSP_FIR_FILTER_TYPE**

.. py:attribute:: osp_frequency_shift

    Specifies the amount of frequency shift applied to the baseband signal.



    .. note:: When using the NI 5450/5451 with I/Q rates higher than 200 MS/s, NI-FGEN
        restricts this property value to 0.

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

    Specifies the generation mode of the OSP, which determines the type of
    data contained in the output signal.

    For more information about the OSP modes your device supports, refer to
    `Devices <javascript:LaunchHelp('SigGenHelp.chm::/device_specific.html')>`__
    section of the *NI Signal Generators Help*.



    .. note:: When using the NI 5450/5451 with I/Q rates higher than 200 MS/s, NI-FGEN
        restricts this property value to BaseBand.

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | :py:data:`OSPMode` |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | Yes                |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:OSP Mode**
            - C Attribute: **NIFGEN_ATTR_OSP_MODE**

.. py:attribute:: osp_overflow_error_reporting

    Configures error reporting when the OSP block detects an overflow in any
    of its stages. Overflows lead to waveform clipping.

    You can use the `OSP Overflow Status <pniFgen_OSPOverflowStatus.html>`__
    property to query for overflow conditions regardless of the setting of
    the OSP Overflow Error Reporting property. The device continues to
    generate after an overflow regardless of the setting of the OSP Overflow
    Error Reporting property.

    The following table lists the characteristics of this property.

    +----------------+--------------------------------------+
    | Characteristic | Value                                |
    +================+======================================+
    | Datatype       | :py:data:`OSPOverflowErrorReporting` |
    +----------------+--------------------------------------+
    | Permissions    | read-write                           |
    +----------------+--------------------------------------+
    | Channel Based  | False                                |
    +----------------+--------------------------------------+
    | Resettable     | Yes                                  |
    +----------------+--------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Onboard Signal Processing:Advanced:OSP Overflow Error Reporting**
            - C Attribute: **NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING**

.. py:attribute:: osp_overflow_status

    Returns a bit field of the overflow status in any stage of the OSP
    block. This property is functional regardless of the value for the `OSP
    Overflow Error Reporting <pniFgen_OSPOverflowErrorReporting.html>`__
    property.

    Set this property to 0 to clear the current OSP overflow status.

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

    Specifies the digital gain to apply to the I data stream before any
    filtering by the OSP block.

    **Valid Values**: -2.0 to 2.0

    **Default Value**: 1.0

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

    Specifies the digital gain to apply to the Q data stream before any
    filtering by the OSP block. This property is used only when the `Data
    Processing Mode <pniFgen_DataProcessingMode.html>`__ property is set to
    **Complex**.

    **Valid Values**: -2.0 to 2.0

    **Default Value**: 1.0

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

    Specifies the digital offset to apply to the I data stream. This offset
    is applied after the prefilter gain and before any filtering.

    **Valid Values**: -1.0 to 1.0

    **Default Value**: 0.9

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

    Specifies the digital offset to apply to the Q data stream. This offset
    is applied after the prefilter gain and before any filtering. This
    property is only used when the `Data Processing
    Mode <pniFgen_DataProcessingMode.html>`__ property is set to
    **Complex**.

    **Valid Values**: -1.0 to 1.0

    **Default Value**: 0.0

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

    Specifies whether the signal that the signal generator produces appears
    at the output connector.

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

    Specifies the output impedance of the signal generator at the output
    connector. NI signal generators have an output impedance of 50 ohms and
    an optional 75 ohms on select modules.

    If the `Load Impedance <pniFgen_LoadImpedance.html>`__ property value
    matches the output impedance, the voltage at the signal output connector
    is at the necessary level. The voltage at the signal output connector
    varies with load output impedance, up to doubling the voltage for a
    high-impedance load.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Specifies the output mode the signal generator uses. The output mode you
    specify determines which VIs and properties you use to configure the
    waveform the signal generator produces.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

    The following table lists the characteristics of this property.

    +----------------+-----------------------+
    | Characteristic | Value                 |
    +================+=======================+
    | Datatype       | :py:data:`OutputMode` |
    +----------------+-----------------------+
    | Permissions    | read-write            |
    +----------------+-----------------------+
    | Channel Based  | False                 |
    +----------------+-----------------------+
    | Resettable     | No                    |
    +----------------+-----------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Output Mode**
            - C Attribute: **NIFGEN_ATTR_OUTPUT_MODE**

.. py:attribute:: p2p_data_transfer_permission_address

    Indicates the address in the writer peer to which the signal generator
    sends data transfer permission credits. This property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.



    .. note:: You can use this property only when the `Manual Configuration
        Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
        TRUE.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | write only |
    +----------------+------------+
    | Channel Based  | False      |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Peer-to-Peer:Manual:Configuration:Data Transfer Permission Address**
            - C Attribute: **NIFGEN_ATTR_P2P_DATA_TRANSFER_PERMISSION_ADDRESS**

.. py:attribute:: p2p_data_transfer_permission_address_type

    Specifies the type of address for the `Data Transfer Permission
    Address <pniFgen_DataTransferPermissionAddress.html>`__ property. This
    property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

    **Default Value**: **Virtual**



    .. note:: You can only use this property when the `Manual Configuration
        Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
        TRUE.

    The following table lists the characteristics of this property.

    +----------------+---------------------------+
    | Characteristic | Value                     |
    +================+===========================+
    | Datatype       | :py:data:`P2PAddressType` |
    +----------------+---------------------------+
    | Permissions    | read-write                |
    +----------------+---------------------------+
    | Channel Based  | False                     |
    +----------------+---------------------------+
    | Resettable     | No                        |
    +----------------+---------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Peer-to-Peer:Manual:Configuration:Data Transfer Permission Address Type**
            - C Attribute: **NIFGEN_ATTR_P2P_DATA_TRANSFER_PERMISSION_ADDRESS_TYPE**

.. py:attribute:: p2p_data_transfer_permission_initial_credits

    Specifies the initial amount of data, in samples per channel, that the
    writer peer is allowed to transfer over the bus into the configured
    endpoint when the peer-to-peer data stream is enabled. If you do not set
    this property and the endpoint is empty, credits equal to the full size
    of the endpoint are issued to the writer peer. If data has been written
    to the endpoint using the `niFgen Write P2P Endpoint
    I16 <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Write_P2P_Endpoint_I16.html')>`__
    VI prior to enabling the stream, credits equal to the remaining space
    available in the endpoint are issued to the writer peer. This property
    is coerced up by NI-FGEN to 8-byte boundaries.

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

            - LabVIEW Property: **Arbitrary Waveform:Peer-to-Peer:Data Transfer Permission Initial Credits**
            - C Attribute: **NIFGEN_ATTR_P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS**

.. py:attribute:: p2p_data_transfer_permission_interval

    Specifies the interval, in samples per channel, at which the signal
    generator issues credits to allow the writer peer to transfer data over
    the bus into the configured endpoint. Refer to the `Flow
    Control <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Flow_Control.html')>`__
    topic in the *NI Signal Generators Help* for more information. This
    property is coerced up by NI-FGEN to the nearest 128-byte boundary. This
    property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

    **Default Value**: 1,024

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

            - LabVIEW Property: **Arbitrary Waveform:Peer-to-Peer:Data Transfer Permission Interval**
            - C Attribute: **NIFGEN_ATTR_P2P_DATA_TRANSFER_PERMISSION_INTERVAL**

.. py:attribute:: p2p_destination_channels

    Specifies which channels are written to by a peer-to-peer endpoint. If
    multiple channels are specified, data is deinterleaved to each channel.
    Channels are configured using the `niFgen Configure
    Channels <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Configure_Channels.html')>`__
    VI. This property is `endpoint
    based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

    **Default Value**: "" (empty string), all channels are configured

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

            - LabVIEW Property: **Arbitrary Waveform:Peer-to-Peer:Destination Channels**
            - C Attribute: **NIFGEN_ATTR_P2P_DESTINATION_CHANNELS**

.. py:attribute:: p2p_done_notification_address

    Returns the signal generator address to which the writer peer sends the
    `Done Notification Value <pniFgen_DoneNotificationValue.html>`__. This
    property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.
    Refer to the `Stopping a Peer-to-Peer
    Generation <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Stopping_Generation.html')>`__
    topic in the *NI Signal Generators Help* for more information about
    using Done Notifications.



    .. note:: You can only use this property when the `Manual Configuration
        Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
        TRUE.

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

            - LabVIEW Property: **Arbitrary Waveform:Peer-to-Peer:Manual:Notification:Done Notification Address**
            - C Attribute: **NIFGEN_ATTR_P2P_DONE_NOTIFICATION_ADDRESS**

.. py:attribute:: p2p_done_notification_address_type

    Specifies the address type of the `Done Notification
    Address <pniFgen_DoneNotificationAddress.html>`__ property. This
    property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.
    Refer to the `Stopping a Peer-to-Peer
    Generation <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Stopping_Generation.html')>`__
    topic in the *NI Signal Generators Help* for more information about
    using Done Notifications.

    Default Value: **Virtual**



    .. note:: You can only use this property when the `Manual Configuration
        Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
        TRUE.

    The following table lists the characteristics of this property.

    +----------------+---------------------------+
    | Characteristic | Value                     |
    +================+===========================+
    | Datatype       | :py:data:`P2PAddressType` |
    +----------------+---------------------------+
    | Permissions    | read-write                |
    +----------------+---------------------------+
    | Channel Based  | False                     |
    +----------------+---------------------------+
    | Resettable     | No                        |
    +----------------+---------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Peer-to-Peer:Manual:Notification:Done Notification Address Type**
            - C Attribute: **NIFGEN_ATTR_P2P_DONE_NOTIFICATION_ADDRESS_TYPE**

.. py:attribute:: p2p_done_notification_value

    Returns the value the writer peer writes to the address specified by the
    `Done Notification Address <pniFgen_DoneNotificationAddress.html>`__
    property. This property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.
    Refer to the `Stopping a Peer-to-Peer
    Generation <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Stopping_Generation.html')>`__
    topic in the *NI Signal Generators Help* for more information about
    using Done Notifications.



    .. note:: You can only use this property when the `Manual Configuration
        Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
        TRUE.

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

            - LabVIEW Property: **Arbitrary Waveform:Peer-to-Peer:Manual:Notification:Done Notification Value**
            - C Attribute: **NIFGEN_ATTR_P2P_DONE_NOTIFICATION_VALUE**

.. py:attribute:: p2p_enabled

    Specifies whether the signal generator reads data from the peer-to-peer
    endpoint (TRUE) instead of reading it from the onboard memory. This
    property is `endpoint
    based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

    **Default Value**: FALSE

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

            - LabVIEW Property: **Arbitrary Waveform:Peer-to-Peer:P2P Enabled**
            - C Attribute: **NIFGEN_ATTR_P2P_ENABLED**

.. py:attribute:: p2p_endpoint_count

    Returns the number of peer-to-peer FIFO endpoints supported by the
    device.

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

            - LabVIEW Property: **Arbitrary Waveform:Peer-to-Peer:Endpoint Count**
            - C Attribute: **NIFGEN_ATTR_P2P_ENDPOINT_COUNT**

.. py:attribute:: p2p_endpoint_fullness_start_trigger_level

    Specifies the number of samples the endpoint needs to receive before the
    signal generator starts generation. This property applies only when the
    `Start Trigger Type <pniFgen_StartTriggerType.html>`__ property is set
    to **P2P Endpoint Fullness**. Refer to the `Flow
    Control <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Flow_Control.html')>`__
    topic in the *NI Signal Generators Help* for more information about
    peer-to-peer operations. This property is coerced down to 8-byte
    boundaries.



    .. note:: Due to an additional internal FIFO in the signal generator, the writer
        peer actually must write 2,304 bytes more than the quantity of data
        specified by this property to satisfy the trigger level.

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

.. py:attribute:: p2p_endpoint_size

    Returns the size, in samples per channel, of the peer-to-peer endpoint.
    This property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

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

            - LabVIEW Property: **Arbitrary Waveform:Peer-to-Peer:Endpoint Size**
            - C Attribute: **NIFGEN_ATTR_P2P_ENDPOINT_SIZE**

.. py:attribute:: p2p_endpoint_window_address

    Returns the signal generator address where endpoint data is sent by the
    writer peer. The type of this address is specified by the `Endpoint
    Window Address Type <pniFgen_EndpointWindowAddressType.html>`__
    property. This property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.



    .. note:: You can only use this property when the `Manual Configuration
        Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
        TRUE.

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

            - LabVIEW Property: **Arbitrary Waveform:Peer-to-Peer:Manual:Configuration:Endpoint Window Address**
            - C Attribute: **NIFGEN_ATTR_P2P_ENDPOINT_WINDOW_ADDRESS**

.. py:attribute:: p2p_endpoint_window_address_type

    Specifies the type of the `Endpoint Window
    Address <pniFgen_EndpointWindowAddress.html>`__ property. This property
    is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

    **Default Value**: **Virtual**



    .. note:: You can only use this property when the `Manual Configuration
        Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
        TRUE.

    The following table lists the characteristics of this property.

    +----------------+---------------------------+
    | Characteristic | Value                     |
    +================+===========================+
    | Datatype       | :py:data:`P2PAddressType` |
    +----------------+---------------------------+
    | Permissions    | read-write                |
    +----------------+---------------------------+
    | Channel Based  | False                     |
    +----------------+---------------------------+
    | Resettable     | No                        |
    +----------------+---------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Arbitrary Waveform:Peer-to-Peer:Manual:Configuration:Endpoint Window Address Type**
            - C Attribute: **NIFGEN_ATTR_P2P_ENDPOINT_WINDOW_ADDRESS_TYPE**

.. py:attribute:: p2p_endpoint_window_size

    Returns the size, in bytes, of the endpoint window. The endpoint window
    is also described by the `Endpoint Window
    Address <pniFgen_EndpointWindowAddress.html>`__ property and the
    `Endpoint Window Address
    Type <pniFgen_EndpointWindowAddressType.html>`__ property. This property
    is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.



    .. note:: You can only use this property when the `Manual Configuration
        Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
        TRUE.

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

            - LabVIEW Property: **Arbitrary Waveform:Peer-to-Peer:Manual:Configuration:Endpoint Window Size**
            - C Attribute: **NIFGEN_ATTR_P2P_ENDPOINT_WINDOW_SIZE**

.. py:attribute:: p2p_manual_configuration_enabled

    Enables (TRUE) or disables (FALSE) manual configuration for a
    peer-to-peer endpoint. Enabling this property disables automatic NI-P2P
    stream manager flow control and Done Notifications.

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

            - LabVIEW Property: **Arbitrary Waveform:Peer-to-Peer:Manual:Manual Configuration Enabled**
            - C Attribute: **NIFGEN_ATTR_P2P_MANUAL_CONFIGURATION_ENABLED**

.. py:attribute:: p2p_most_space_available_in_endpoint

    Returns the largest number of samples per channel available in the
    endpoint since this property was last read. This property can be used to
    determine how much endpoint space to use as a buffer against PCI Express
    bus traffic latencies by reading the property and keeping track of the
    largest value returned. This property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

    If you want to minimize the latency for data to move through the
    endpoint and be generated by the signal generator, use the `Data
    Transfer Permission Initial
    Credits <pniFgen_DataTransferPermissionInitialCredits.html>`__ property
    to grant fewer initial credits than the default of the entire endpoint
    size.

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

            - LabVIEW Property: **Arbitrary Waveform:Peer-to-Peer:Most Space Available In Endpoint**
            - C Attribute: **NIFGEN_ATTR_P2P_MOST_SPACE_AVAILABLE_IN_ENDPOINT**

.. py:attribute:: p2p_space_available_in_endpoint

    Returns the current space available in the endpoint in samples per
    channel. You can use this property when priming the endpoint with
    initial data through the `niFgen Write P2P Endpoint
    I16 <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Write_P2P_Endpoint_I16.html')>`__
    VI to determine how many samples you can write. You also can use this
    property to characterize the performance and measure the latency of the
    peer-to-peer stream as data moves across the bus. This property is
    `endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

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

            - LabVIEW Property: **Arbitrary Waveform:Peer-to-Peer:Space Available In Endpoint**
            - C Attribute: **NIFGEN_ATTR_P2P_SPACE_AVAILABLE_IN_ENDPOINT**

.. py:attribute:: pci_dma_optimizations_enabled

    Controls whether NI-FGEN allows performance optimizations for DMA
    transfers. This property is only valid for PCI and PXI SMC-based
    devices. This property is enabled (TRUE) by default, and NI recommends
    leaving it enabled.

    **Default Value**: TRUE



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Specifies the amount of post-amplifier attenuation to apply to the
    signal, in dB.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Specifies the amount of preamplifier attenuation to apply to the signal,
    in dB.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Specifies whether to validate property values and VI parameters. Set
    this property to TRUE to enable range-checking.

    If enabled, in some cases, NI-FGEN does extra validation of parameter
    values that you pass to NI-FGEN VIs. Range checking parameters is useful
    for debugging. After you validate your program, you can set this
    property to FALSE to disable range checking and maximize performance.

    Use the `niFgen Initialize With
    Options <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize_With_Options.html')>`__
    VI to override the value of this property.

    **Default Value**: TRUE

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

    +----------------+------------------------------------------+
    | Characteristic | Value                                    |
    +================+==========================================+
    | Datatype       | :py:data:`ReadyForStartEventActiveLevel` |
    +----------------+------------------------------------------+
    | Permissions    | read-write                               |
    +----------------+------------------------------------------+
    | Channel Based  | False                                    |
    +----------------+------------------------------------------+
    | Resettable     | Yes                                      |
    +----------------+------------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Ready For Start:Level:Active Level**
            - C Attribute: **NIFGEN_ATTR_READY_FOR_START_EVENT_LEVEL_ACTIVE_LEVEL**

.. py:attribute:: ready_for_start_event_live_status

    Returns TRUE if the status of the specified Ready for Start Event is
    live, and FALSE otherwise.

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

    Specifies the destination terminal for the Ready for Start Event. For a
    list of the terminals available on your device, refer to the Routes
    topic for your device or the **Device Routes** tab in MAX.

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

    Specifies whether the IVI engine keeps a list of the value coercions it
    makes for ViInt32 and ViReal64 properties. Set this property to TRUE to
    record the coercions. Use the `niFgen Initialize With
    Options <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize_With_Options.html')>`__
    VI to override this value.

    **Default Value**: FALSE

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

    Specifies the Reference Clock source used by the signal generator.

    The signal generator derives the frequencies and sample rates that it
    uses to generate waveforms from the source you specify. For example,
    when you set this property to **Clock In**, the signal generator uses
    the signal it receives at its CLK In front panel connector as its
    Reference Clock.



    .. note:: The signal generator must not be in the Generating state when you change
        this property. To change the device configuration, call the `niFgen
        Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

    The following table lists the characteristics of this property.

    +----------------+---------------------------------+
    | Characteristic | Value                           |
    +================+=================================+
    | Datatype       | :py:data:`ReferenceClockSource` |
    +----------------+---------------------------------+
    | Permissions    | read-write                      |
    +----------------+---------------------------------+
    | Channel Based  | False                           |
    +----------------+---------------------------------+
    | Resettable     | Yes                             |
    +----------------+---------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Reference Clock:Source**
            - C Attribute: **NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE**

.. py:attribute:: ref_clock_frequency

    Specifies the Reference Clock frequency. The signal generator uses the
    Reference Clock to derive frequencies and sample rates when generating
    output.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Specifies the delay in seconds to apply to an external Sample Clock.
    This property is useful when trying to align the output of two devices.



    .. note:: For the NI 5421, absolute delay can only be applied when an external
        Sample Clock is used.

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

    Specifies the Sample Clock source.



    .. note:: The signal generator must not be in the Generating state when you change
        this property. To change the device configuration, call the `niFgen
        Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

    The following table lists the characteristics of this property.

    +----------------+------------------------------+
    | Characteristic | Value                        |
    +================+==============================+
    | Datatype       | :py:data:`SampleClockSource` |
    +----------------+------------------------------+
    | Permissions    | read-write                   |
    +----------------+------------------------------+
    | Channel Based  | False                        |
    +----------------+------------------------------+
    | Resettable     | Yes                          |
    +----------------+------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Sample Clock:Source**
            - C Attribute: **NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE**

.. py:attribute:: sample_clock_timebase_rate

    Specifies the Sample Clock Timebase rate. This property applies only to
    external Sample Clock timebases.



    .. note:: The signal generator must not be in the Generating state when you change
        this property. To change the device configuration, call the `niFgen
        Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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



    .. note:: The signal generator must not be in the Generating state when you change
        this property. To change the device configuration, call the `niFgen
        Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

    The following table lists the characteristics of this property.

    +----------------+--------------------------------------+
    | Characteristic | Value                                |
    +================+======================================+
    | Datatype       | :py:data:`SampleClockTimebaseSource` |
    +----------------+--------------------------------------+
    | Permissions    | read-write                           |
    +----------------+--------------------------------------+
    | Channel Based  | False                                |
    +----------------+--------------------------------------+
    | Resettable     | Yes                                  |
    +----------------+--------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocks:Sample Clock Timebase:Source**
            - C Attribute: **NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_SOURCE**

.. py:attribute:: script_to_generate

    Specifies which script the signal generator uses. To configure the
    signal generator to run a particular script, set this property to the
    name of the script.

    Use the `niFgen Write
    Script <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Write_Script.html')>`__
    VI to create multiple scripts. Use this property when the `Output
    Mode <pniFgen_OutputMode.html>`__ property is set to
    **NIFGEN\_VAL\_OUTPUT\_SCRIPT**.



    .. note:: The signal generator must not be in the Generating state when you change
        this property. To change the device configuration, call the `niFgen
        Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Returns the number of Script Triggers supported by the device. Use this
    property when the `Output Mode <pniFgen_OutputMode.html>`__ property is
    set to **NIFGEN\_VAL\_OUTPUT\_SCRIPT**.

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

    Specifies the Script trigger type. Depending upon the value of this
    property, additional properties may be needed to fully configure the
    trigger.

    The following table lists the characteristics of this property.

    +----------------+------------------------------+
    | Characteristic | Value                        |
    +================+==============================+
    | Datatype       | :py:data:`ScriptTriggerType` |
    +----------------+------------------------------+
    | Permissions    | read-write                   |
    +----------------+------------------------------+
    | Channel Based  | False                        |
    +----------------+------------------------------+
    | Resettable     | Yes                          |
    +----------------+------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Script:Trigger Type**
            - C Attribute: **NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE**

.. py:attribute:: serial_number

    Returns the serial number of the signal generator.

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

    Specifies whether or not to simulate NI-FGEN I/O operations. Set this
    property to TRUE to enable simulation.

    If simulation is enabled, NI-FGEN VIs perform range checking and can get
    and set properties, but they do not perform instrument I/O. For output
    parameters that represent instrument data, NI-FGEN VIs return calculated
    values.

    Use the `niFgen Initialize With
    Options <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize_With_Options.html')>`__
    VI to override the value of this property.

    **Default Value**: FALSE

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

    Returns the major version number of the class specification with which
    NI-FGEN is compliant.

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

    Returns the minor version number of the class specification with which
    NI-FGEN is compliant.

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

    Contains a brief description of the specific driver.

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

.. py:attribute:: specific_driver_vendor

    Contains the name of the vendor that supplies NI-FGEN.

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

    Specifies the amount of delay applied to a Started Event with respect to
    the analog output of the signal generator.

    A positive delay value indicates that the Started Event occurs after the
    analog data, while a negative delay value indicates that the Started
    Event occurs before the analog data. The default value is zero, which
    aligns the Started Event with the analog output.

    You can specify the units of the delay value by setting the `Started
    Event Delay Units <pniFgen_StartedEventDelayUnits.html>`__ property.

    **Default Value**: 0

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

    Specifies the units used for the `Started Event Delay
    Value <pniFgen_StartedEventDelayValue.html>`__ property.

    The following table lists the characteristics of this property.

    +----------------+-----------------------------------+
    | Characteristic | Value                             |
    +================+===================================+
    | Datatype       | :py:data:`StartedEventDelayUnits` |
    +----------------+-----------------------------------+
    | Permissions    | read-write                        |
    +----------------+-----------------------------------+
    | Channel Based  | False                             |
    +----------------+-----------------------------------+
    | Resettable     | Yes                               |
    +----------------+-----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Started:Advanced:Delay Units**
            - C Attribute: **NIFGEN_ATTR_STARTED_EVENT_DELAY_UNITS**

.. py:attribute:: started_event_latched_status

    Returns the latched status of the specified Started Event.

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

    +----------------+------------------------------------+
    | Characteristic | Value                              |
    +================+====================================+
    | Datatype       | :py:data:`StartedEventActiveLevel` |
    +----------------+------------------------------------+
    | Permissions    | read-write                         |
    +----------------+------------------------------------+
    | Channel Based  | False                              |
    +----------------+------------------------------------+
    | Resettable     | Yes                                |
    +----------------+------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Started:Level:Active Level**
            - C Attribute: **NIFGEN_ATTR_STARTED_EVENT_LEVEL_ACTIVE_LEVEL**

.. py:attribute:: started_event_output_behavior

    Specifies the output behavior for the Started Event.

    The following table lists the characteristics of this property.

    +----------------+---------------------------------------+
    | Characteristic | Value                                 |
    +================+=======================================+
    | Datatype       | :py:data:`StartedEventOutputBehavior` |
    +----------------+---------------------------------------+
    | Permissions    | read-write                            |
    +----------------+---------------------------------------+
    | Channel Based  | False                                 |
    +----------------+---------------------------------------+
    | Resettable     | Yes                                   |
    +----------------+---------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Started:Output Behavior**
            - C Attribute: **NIFGEN_ATTR_STARTED_EVENT_OUTPUT_BEHAVIOR**

.. py:attribute:: started_event_output_terminal

    Specifies the destination terminal for the Started Event. For a list of
    the terminals available on your device, refer to the Routes topic for
    your device or the **Device Routes** tab in MAX.

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

    +----------------+--------------------------------------+
    | Characteristic | Value                                |
    +================+======================================+
    | Datatype       | :py:data:`StartedEventPulsePolarity` |
    +----------------+--------------------------------------+
    | Permissions    | read-write                           |
    +----------------+--------------------------------------+
    | Channel Based  | False                                |
    +----------------+--------------------------------------+
    | Resettable     | Yes                                  |
    +----------------+--------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Started:Pulse:Polarity**
            - C Attribute: **NIFGEN_ATTR_STARTED_EVENT_PULSE_POLARITY**

.. py:attribute:: started_event_pulse_width

    Specifies the pulse width value for the Started Event.

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

    +----------------+----------------------------------------+
    | Characteristic | Value                                  |
    +================+========================================+
    | Datatype       | :py:data:`StartedEventPulseWidthUnits` |
    +----------------+----------------------------------------+
    | Permissions    | read-write                             |
    +----------------+----------------------------------------+
    | Channel Based  | False                                  |
    +----------------+----------------------------------------+
    | Resettable     | Yes                                    |
    +----------------+----------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Events:Started:Pulse:Width Units**
            - C Attribute: **NIFGEN_ATTR_STARTED_EVENT_PULSE_WIDTH_UNITS**

.. py:attribute:: start_trigger_type

    Specifies the type of Start Trigger you want to use.

    The following table lists the characteristics of this property.

    +----------------+-----------------------------+
    | Characteristic | Value                       |
    +================+=============================+
    | Datatype       | :py:data:`StartTriggerType` |
    +----------------+-----------------------------+
    | Permissions    | read-write                  |
    +----------------+-----------------------------+
    | Channel Based  | False                       |
    +----------------+-----------------------------+
    | Resettable     | Yes                         |
    +----------------+-----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Start:Trigger Type**
            - C Attribute: **NIFGEN_ATTR_START_TRIGGER_TYPE**

.. py:attribute:: streaming_space_available_in_waveform

    Returns the space available in the streaming waveform for writing new
    data.

    Use this property in conjunction with the `Streaming Waveform
    Handle <pniFgen_StreamingWaveformHandle.html>`__ property or the
    `Streaming Waveform Name <pniFgen_StreamingWaveformName.html>`__
    property.

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

    Specifies the waveform handle of the waveform used to continuously
    stream data during generation.

    This property is used in conjunction with the `Space Available in
    Streaming Waveform <pniFgen_SpaceAvailInStreamingWfm.html>`__ property.

    **Default Value**: -1



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Specifies the name of the waveform used to continuously stream data
    during generation. This property defaults to an empty string when no
    streaming waveform is specified.

    Use this property in conjunction with the `Space Available in Streaming
    Waveform <pniFgen_SpaceAvailInStreamingWfm.html>`__ property.

    **Default Value**: ""



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Specifies the maximum amount of time allowed to complete a streaming
    write operation.

    **Units**: seconds (s)

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

            - LabVIEW Property: **Arbitrary Waveform:Data Transfer:Streaming:Streaming Write Timeout**
            - C Attribute: **NIFGEN_ATTR_STREAMING_WRITE_TIMEOUT**

.. py:attribute:: supported_instrument_models

    Returns a model code of the instrument. For drivers that support more
    than one device, this property contains a comma-separated list of
    supported instrument models.

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

    Specifies the source of the synchronization signal to use.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

    The following table lists the characteristics of this property.

    +----------------+----------------------------------+
    | Characteristic | Value                            |
    +================+==================================+
    | Datatype       | :py:data:`SynchronizationSource` |
    +----------------+----------------------------------+
    | Permissions    | read-write                       |
    +----------------+----------------------------------+
    | Channel Based  | False                            |
    +----------------+----------------------------------+
    | Resettable     | No                               |
    +----------------+----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:5401/5411/5431:Synchronization Source**
            - C Attribute: **NIFGEN_ATTR_SYNCHRONIZATION**

.. py:attribute:: sync_duty_cycle_high

    Specifies the duty cycle of the square wave the signal generator
    produces on the SYNC OUT connector. Specify this property as a
    percentage of the time the square wave is high in each cycle.

    **Units**: Percentage of time the waveform is high

    **Default Value**: 50%

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

    Specifies the terminal at which to export the SYNC OUT signal. This
    property is not supported for all devices. For a list of the terminals
    available on your device, refer to the Routes topic for your device or
    the **Device Routes** tab in MAX.

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

    Specifies whether to analyze gain and offset values based on
    single-ended or
    `differential <javascript:LaunchHelp('SigGenHelp.chm::/fund_differential_output.html')>`__
    operation.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

    The following table lists the characteristics of this property.

    +----------------+----------------------------------+
    | Characteristic | Value                            |
    +================+==================================+
    | Datatype       | :py:data:`TerminalConfiguration` |
    +----------------+----------------------------------+
    | Permissions    | read-write                       |
    +----------------+----------------------------------+
    | Channel Based  | False                            |
    +----------------+----------------------------------+
    | Resettable     | Yes                              |
    +----------------+----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Terminal Configuration**
            - C Attribute: **NIFGEN_ATTR_TERMINAL_CONFIGURATION**

.. py:attribute:: trigger_mode

    Controls the trigger mode.

    **Default Value**: **NIFGEN\_VAL\_CONTINUOUS**

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | :py:data:`TriggerMode` |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | False                  |
    +----------------+------------------------+
    | Resettable     | No                     |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggers:Trigger Mode**
            - C Attribute: **NIFGEN_ATTR_TRIGGER_MODE**

.. py:attribute:: trigger_source

    Specifies which trigger source the signal generator uses.

    After you call the `niFgen Initiate
    Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initiate_Generation.html')>`__
    VI, the signal generator waits for the trigger you specify in this
    parameter. After it receives a trigger, the signal generator produces
    the number of cycles you specify in the `Repeat
    Count <pniFgen_ArbWfm.RepeatCount.html>`__ property.

    The value you select for this property is also the source for the
    trigger in the other trigger modes as specified by the `Trigger
    Mode <pniFgen_TriggerMode.html>`__ property.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

    The following table lists the characteristics of this property.

    +----------------+--------------------------+
    | Characteristic | Value                    |
    +================+==========================+
    | Datatype       | :py:data:`TriggerSource` |
    +----------------+--------------------------+
    | Permissions    | read-write               |
    +----------------+--------------------------+
    | Channel Based  | False                    |
    +----------------+--------------------------+
    | Resettable     | Yes                      |
    +----------------+--------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:5401/5411/5431:Trigger Source**
            - C Attribute: **NIFGEN_ATTR_TRIGGER_SOURCE**

.. py:attribute:: video_waveform_type

    Specifies the waveform type the NI 5431 generates. Setting this property
    ensures the oscillator crystal is set to the proper frequency.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

    The following table lists the characteristics of this property.

    +----------------+------------------------------+
    | Characteristic | Value                        |
    +================+==============================+
    | Datatype       | :py:data:`VideoWaveformType` |
    +----------------+------------------------------+
    | Permissions    | read-write                   |
    +----------------+------------------------------+
    | Channel Based  | False                        |
    +----------------+------------------------------+
    | Resettable     | No                           |
    +----------------+------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Instrument:5401/5411/5431:Video Waveform Type**
            - C Attribute: **NIFGEN_ATTR_VIDEO_WAVEFORM_TYPE**

.. py:attribute:: wait_behavior

    Specifies the behavior of the output while waiting for a Script Trigger
    or during a wait instruction.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

    The following table lists the characteristics of this property.

    +----------------+-------------------------+
    | Characteristic | Value                   |
    +================+=========================+
    | Datatype       | :py:data:`WaitBehavior` |
    +----------------+-------------------------+
    | Permissions    | read-write              |
    +----------------+-------------------------+
    | Channel Based  | False                   |
    +----------------+-------------------------+
    | Resettable     | Yes                     |
    +----------------+-------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Output:Advanced:Wait Behavior**
            - C Attribute: **NIFGEN_ATTR_WAIT_BEHAVIOR**

.. py:attribute:: wait_value

    Specifies the value to generate while waiting. You must set the `Wait
    Behavior <pniFgen_WaitBehavior.html>`__ property to **Jump To Value** to
    use this property.



    .. note:: You cannot change this property while the device is generating a
        waveform. If you want to change the device configuration, call the
        `niFgen Abort
        Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
        VI or wait for the generation to complete.

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

    Returns the quantum value the signal generator allows. The size of each
    arbitrary waveform must be a multiple of this quantum value.

    For example, when this property returns a value of 8, all waveform sizes
    must be a multiple of 8. Typically, this value is constant for the
    signal generator.

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


