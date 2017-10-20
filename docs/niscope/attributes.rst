niscope.Session properties
==========================

.. py:currentmodule:: niscope

.. py:attribute:: 5102_adjust_pretrigger_samples

    When set to TRUE and the digitizer is set to master, the number of
    pretrigger samples and total number of samples are adjusted to enable
    synchronizing a master and slave NI 5102.

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

            - LabVIEW Property: **Horizontal:Advanced:5102 Adjust Pretrigger Samples**
            - C Attribute: **NISCOPE_ATTR_5102_ADJUST_PRETRIGGER_SAMPLES**

.. py:attribute:: 5v_out_output_terminal

    Specifies the destination for the 5 Volt power signal. Refer to the
    device specifications document for a list of valid destinations.

    **Defined Values**

    VAL\_RTSI\_0

    VAL\_RTSI\_1

    VAL\_RTSI\_2

    VAL\_RTSI\_3

    VAL\_RTSI\_4

    VAL\_RTSI\_5

    VAL\_RTSI\_6

    VAL\_PFI\_0

    VAL\_PFI\_1

    VAL\_PFI\_2

    VAL\_PXI\_STAR



    .. note:: This property is supported only for NI 5152/5153/5154 devices.

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

            - LabVIEW Property: **Synchronization:5 Volt Power:Output Terminal**
            - C Attribute: **NISCOPE_ATTR_5V_OUT_OUTPUT_TERMINAL**

.. py:attribute:: absolute_sample_clock_offset

    Gets or sets the absolute time offset of the sample clock relative to
    the reference clock in terms of seconds.



    .. note:: Configures the sample clock relationship with respect to the reference
        clock. This parameter is factored into NI-TClk adjustments and is
        typically used to improve the repeatability of NI-TClk Synchronization.
        When this parameter is read, the currently programmed value is returned.
        The range of the absolute sample clock offset is [-.5 sample clock
        periods, .5 sample clock periods]. The default absolute sample clock
        offset is 0s.

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

            - LabVIEW Property: **Clocking:Advanced:Absolute Sample Clock Offset**
            - C Attribute: **NISCOPE_ATTR_ABSOLUTE_SAMPLE_CLOCK_OFFSET**

.. py:attribute:: acquisition_start_time

    Specifies the length of time (in seconds) from the trigger event to the
    first point in the waveform record.

    If the value is positive, the first point in the waveform record occurs
    after the trigger event (same as specifying a trigger delay). If the
    value is negative, the first point in the waveform record occurs before
    the trigger event (same as specifying Reference Position).

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

            - LabVIEW Property: **Horizontal:Advanced:Acquisition Start Time**
            - C Attribute: **NISCOPE_ATTR_ACQUISITION_START_TIME**

.. py:attribute:: acquisition_type

    Specifies how the digitizer acquires data and fills the waveform record.



    .. note:: Acquisition type DDC applies to the NI 5620/5621 only. To use DDC mode
        in the NI 5142 and NI 5622, leave acquisition type set to Normal and set
        `DDC Enabled <pniScope_DDCEnabled.html>`__ to TRUE.

    The following table lists the characteristics of this property.

    +----------------+----------------------------+
    | Characteristic | Value                      |
    +================+============================+
    | Datatype       | :py:data:`AcquisitionType` |
    +----------------+----------------------------+
    | Permissions    | read-write                 |
    +----------------+----------------------------+
    | Channel Based  | False                      |
    +----------------+----------------------------+
    | Resettable     | No                         |
    +----------------+----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Acquisition:Acquisition Type**
            - C Attribute: **NISCOPE_ATTR_ACQUISITION_TYPE**

.. py:attribute:: acq_arm_source

    Specifies the source the digitizer monitors for an acquisition arm
    trigger. When an acquisition arm trigger is received, the digitizer
    begins acquiring pretrigger samples.

    **Defined Values**

    VAL\_IMMEDIATE

    VAL\_RTSI\_0

    VAL\_RTSI\_1

    VAL\_RTSI\_2

    VAL\_RTSI\_3

    VAL\_RTSI\_4

    VAL\_RTSI\_5

    VAL\_RTSI\_6

    VAL\_PFI\_0

    VAL\_PFI\_1

    VAL\_PFI\_2

    VAL\_PXI\_STAR

    VAL\_SW\_TRIG\_FUNC

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

            - LabVIEW Property: **Synchronization:Start Trigger (Acq. Arm):Source**
            - C Attribute: **NISCOPE_ATTR_ACQ_ARM_SOURCE**

.. py:attribute:: adv_trig_src

    Specifies the source the digitizer monitors for an advance trigger. When
    the advance trigger is received, the digitizer begins acquiring
    pretrigger samples for the next record.

    **Defined Values**

    VAL\_IMMEDIATE

    VAL\_RTSI\_0

    VAL\_RTSI\_1

    VAL\_RTSI\_2

    VAL\_RTSI\_3

    VAL\_RTSI\_4

    VAL\_RTSI\_5

    VAL\_RTSI\_6

    VAL\_PFI\_0

    VAL\_PFI\_1

    VAL\_PFI\_2

    VAL\_PXI\_STAR

    VAL\_SW\_TRIG\_FUNC

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

            - LabVIEW Property: **Synchronization:Advance Trigger:Source**
            - C Attribute: **NISCOPE_ATTR_ADV_TRIG_SRC**

.. py:attribute:: agc_average_control

    Averages the `AGC <Digitizers.chm::/Glossary.html#AGC>`__ values. The
    default value is Mean.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        agc_average_control.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        agc_average_control.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].agc_average_control = var
            var = session['0,1'].agc_average_control

    The following table lists the characteristics of this property.

    +----------------+------------------------------+
    | Characteristic | Value                        |
    +================+==============================+
    | Datatype       | :py:data:`AGCAverageControl` |
    +----------------+------------------------------+
    | Permissions    | read-write                   |
    +----------------+------------------------------+
    | Channel Based  | True                         |
    +----------------+------------------------------+
    | Resettable     | No                           |
    +----------------+------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):AGC:Average Control**
            - C Attribute: **NISCOPE_ATTR_AGC_AVERAGE_CONTROL**

.. py:attribute:: agc_loop_gain_0_exponent

    Along with the `AGC Loop Gain 0
    Mantissa <pniScope_AGCLoopGain0Mantissa.html>`__ property, sets the loop
    gain for the `AGC <Digitizers.chm::/Glossary.html#AGC>`__. The default
    value is 0.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        agc_loop_gain_0_exponent.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        agc_loop_gain_0_exponent.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].agc_loop_gain_0_exponent = var
            var = session['0,1'].agc_loop_gain_0_exponent

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):AGC:Loop Gain 0 Exponent**
            - C Attribute: **NISCOPE_ATTR_AGC_LOOP_GAIN_0_EXPONENT**

.. py:attribute:: agc_loop_gain_0_mantissa

    Along with the `AGC Loop Gain 0
    Exponent <pniScope_AGCLoopGain0Exponent.html>`__ property, sets the loop
    gain for the `AGC <Digitizers.chm::/Glossary.html#AGC>`__. The default
    value is 0.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        agc_loop_gain_0_mantissa.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        agc_loop_gain_0_mantissa.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].agc_loop_gain_0_mantissa = var
            var = session['0,1'].agc_loop_gain_0_mantissa

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):AGC:Loop Gain 0 Mantissa**
            - C Attribute: **NISCOPE_ATTR_AGC_LOOP_GAIN_0_MANTISSA**

.. py:attribute:: agc_loop_gain_1_exponent

    Along with `AGC Loop Gain 1
    Mantissa <pniScope_AGCLoopGain1Mantissa.html>`__ property, sets the loop
    gain for the `AGC <Digitizers.chm::/Glossary.html#AGC>`__. The default
    value is 0.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        agc_loop_gain_1_exponent.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        agc_loop_gain_1_exponent.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].agc_loop_gain_1_exponent = var
            var = session['0,1'].agc_loop_gain_1_exponent

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):AGC:Loop Gain 1 Exponent**
            - C Attribute: **NISCOPE_ATTR_AGC_LOOP_GAIN_1_EXPONENT**

.. py:attribute:: agc_loop_gain_1_mantissa

    Along with `AGC Loop Gain 1
    Exponent <pniScope_AGCLoopGain1Exponent.html>`__ property, sets the loop
    gain for the `AGC <Digitizers.chm::/Glossary.html#AGC>`__. The default
    value is 0.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        agc_loop_gain_1_mantissa.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        agc_loop_gain_1_mantissa.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].agc_loop_gain_1_mantissa = var
            var = session['0,1'].agc_loop_gain_1_mantissa

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):AGC:Loop Gain 1 Mantissa**
            - C Attribute: **NISCOPE_ATTR_AGC_LOOP_GAIN_1_MANTISSA**

.. py:attribute:: agc_lower_gain_limit

    Sets the minimum gain and maximum signal levels in the
    `AGC <Digitizers.chm::/Glossary.html#AGC>`__. The default value is
    6.020600.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        agc_lower_gain_limit.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        agc_lower_gain_limit.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].agc_lower_gain_limit = var
            var = session['0,1'].agc_lower_gain_limit

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):AGC:Lower Gain Limit**
            - C Attribute: **NISCOPE_ATTR_AGC_LOWER_GAIN_LIMIT**

.. py:attribute:: agc_threshold

    Sets the gain error in the `AGC <Digitizers.chm::/Glossary.html#AGC>`__.
    The default value is 0x034D.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        agc_threshold.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        agc_threshold.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].agc_threshold = var
            var = session['0,1'].agc_threshold

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):AGC:Threshold**
            - C Attribute: **NISCOPE_ATTR_AGC_THRESHOLD**

.. py:attribute:: agc_upper_gain_limit

    Sets the maximum gain and minimum signal levels in the
    `AGC <Digitizers.chm::/Glossary.html#AGC>`__. The default value is
    6.020600.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        agc_upper_gain_limit.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        agc_upper_gain_limit.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].agc_upper_gain_limit = var
            var = session['0,1'].agc_upper_gain_limit

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):AGC:Upper Gain Limit**
            - C Attribute: **NISCOPE_ATTR_AGC_UPPER_GAIN_LIMIT**

.. py:attribute:: allow_more_records_than_memory

    Allows you to acquire more records than fit in onboard memory.

    TRUE—Enables NI-SCOPE to fetch more records than fit in memory

    FALSE—Disables NI-SCOPE from fetching more records than fit in memory

    **Related topics:**

    `Time Interleaved
    Sampling <digitizers.chm::/TimeInterleavedSampling.html>`__



    .. note:: The property can be used only in digitizers that support continuous
        acquisition. Refer to `Features Supported by
        Device <Digitizers.chm::/Features_Supported_Main.html>`__ to find out if
        your digitizer supports continuous acquisition.

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

            - LabVIEW Property: **Horizontal:Enable Records > Memory**
            - C Attribute: **NISCOPE_ATTR_ALLOW_MORE_RECORDS_THAN_MEMORY**

.. py:attribute:: aout_parallel_output_source

    Specifies the source for the AOUT parallel output from the
    `DDC <Digitizers.chm::/Glossary.html#DDC>`__. The default is I Data.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        aout_parallel_output_source.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        aout_parallel_output_source.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].aout_parallel_output_source = var
            var = session['0,1'].aout_parallel_output_source

    The following table lists the characteristics of this property.

    +----------------+-------------------------------------+
    | Characteristic | Value                               |
    +================+=====================================+
    | Datatype       | :py:data:`AOUTParallelOutputSource` |
    +----------------+-------------------------------------+
    | Permissions    | read-write                          |
    +----------------+-------------------------------------+
    | Channel Based  | True                                |
    +----------------+-------------------------------------+
    | Resettable     | No                                  |
    +----------------+-------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Output Configuration:Parallel:AOUT Source**
            - C Attribute: **NISCOPE_ATTR_AOUT_PARALLEL_OUTPUT_SOURCE**

.. py:attribute:: arm_ref_trig_src

    Specifies the source the digitizer monitors for an arm reference
    trigger. When the arm reference trigger is received, the digitizer
    begins searching for the reference (stop) trigger from the
    user-configured trigger source.

    **Defined Values**

    VAL\_IMMEDIATE

    VAL\_RTSI\_0

    VAL\_RTSI\_1

    VAL\_RTSI\_2

    VAL\_RTSI\_3

    VAL\_RTSI\_4

    VAL\_RTSI\_5

    VAL\_RTSI\_6

    VAL\_PFI\_0

    VAL\_PFI\_1

    VAL\_PFI\_2

    VAL\_PXI\_STAR

    VAL\_SW\_TRIG\_FUNC

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

            - LabVIEW Property: **Synchronization:Arm Reference Trigger:Source**
            - C Attribute: **NISCOPE_ATTR_ARM_REF_TRIG_SRC**

.. py:attribute:: backlog

    Specifies the number of points acquired that have not been fetched yet.

    **Related topics:**

    `Fetching Data <digitizers.chm::/Fetching_Data.html>`__

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

            - LabVIEW Property: **Fetch:Fetch Backlog**
            - C Attribute: **NISCOPE_ATTR_BACKLOG**

.. py:attribute:: bandpass_filter_enabled

    Enables the bandpass filter on the specified channel. For the NI
    PXIe-5622, set the value to TRUE to enable the IF filtered path 50MHz
    bandpass filter centered at 187MHz. The default value is FALSE.

    **Related topics:**

    `Bandwidth <digitizers.chm::/Analog_Bandwidth.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        bandpass_filter_enabled.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        bandpass_filter_enabled.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].bandpass_filter_enabled = var
            var = session['0,1'].bandpass_filter_enabled

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Vertical:Advanced:Bandpass Filter Enabled**
            - C Attribute: **NISCOPE_ATTR_BANDPASS_FILTER_ENABLED**

.. py:attribute:: binary_sample_width

    Indicates the bit width of the binary data in the acquired waveform,
    which can help you determine which Binary Fetch to use.

    To configure the device to store samples with a lower resolution than
    the native, set this property to the desired binary width. This
    configuration can be useful for streaming at faster speeds, but at the
    cost of resolution. The least significant bits are lost with this
    configuration. Compare to the `Resolution <pniScope_Resolution.html>`__
    property.

    Valid Values: 8, 16, 32

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

            - LabVIEW Property: **Acquisition:Binary Sample Width**
            - C Attribute: **NISCOPE_ATTR_BINARY_SAMPLE_WIDTH**

.. py:attribute:: bout_parallel_output_source

    Specifies the source for the BOUT parallel output from the
    `DDC <Digitizers.chm::/Glossary.html#DDC>`__. The default is Q Data.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        bout_parallel_output_source.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        bout_parallel_output_source.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].bout_parallel_output_source = var
            var = session['0,1'].bout_parallel_output_source

    The following table lists the characteristics of this property.

    +----------------+-------------------------------------+
    | Characteristic | Value                               |
    +================+=====================================+
    | Datatype       | :py:data:`BOUTParallelOutputSource` |
    +----------------+-------------------------------------+
    | Permissions    | read-write                          |
    +----------------+-------------------------------------+
    | Channel Based  | True                                |
    +----------------+-------------------------------------+
    | Resettable     | No                                  |
    +----------------+-------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Output Configuration:Parallel:BOUT Source**
            - C Attribute: **NISCOPE_ATTR_BOUT_PARALLEL_OUTPUT_SOURCE**

.. py:attribute:: cache

    Specifies whether to cache the value of properties. When caching is
    enabled, the instrument driver keeps track of the current instrument
    settings and avoids sending redundant commands to the instrument. Thus,
    you can significantly increase execution speed. The instrument driver
    can choose always to cache or never to cache particular properties,
    regardless of the setting of this property. The default value is TRUE.
    Use `niScope Initialize with
    Options <scopeviref.chm::/niScope_Initialize_With_Options.html>`__ to
    override this value.

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

            - LabVIEW Property: **Inherent IVI Attributes:User Options:Cache**
            - C Attribute: **NISCOPE_ATTR_CACHE**

.. py:attribute:: carrier_nco_center_frequency

    Controls the frequency of the timing NCO. The default value is
    0X8000000.

    Specifies the timing NCO center frequency in binary format as follows:

    N = ( *:sub:`out`* / *F\ :sub:`resampler`* ) & 2\ :sup:`32`

    where *F\ :sub:`out`* is the output frequency and *F\ :sub:`resampler`*
    is the resampled frequency.

    The value is transferred to the active register during the next initiate
    acquisition operation.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        carrier_nco_center_frequency.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        carrier_nco_center_frequency.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].carrier_nco_center_frequency = var
            var = session['0,1'].carrier_nco_center_frequency

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Carrier Mixer:NCO Center Frequency**
            - C Attribute: **NISCOPE_ATTR_CARRIER_NCO_CENTER_FREQUENCY**

.. py:attribute:: carrier_phase_offset

    Offsets the phase of the timing NCO in binary format. The value is
    transferred to the active register during the next initiate acquisition.
    The default value is 0.

    Valid Range: 0 to 6.283185307179586476925286766558




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        carrier_phase_offset.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        carrier_phase_offset.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].carrier_phase_offset = var
            var = session['0,1'].carrier_phase_offset

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Carrier Mixer:Phase Offset**
            - C Attribute: **NISCOPE_ATTR_CARRIER_PHASE_OFFSET**

.. py:attribute:: channel_count

    Indicates the number of channels that the specific instrument driver
    supports. For channel based properties, the IVI engine maintains a
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

            - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Channel Count**
            - C Attribute: **NISCOPE_ATTR_CHANNEL_COUNT**

.. py:attribute:: channel_enabled

    Specifies whether the digitizer acquires a waveform for the channel.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        channel_enabled.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        channel_enabled.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].channel_enabled = var
            var = session['0,1'].channel_enabled

    The following table lists the characteristics of this property.

    +----------------+----------------------------------+
    | Characteristic | Value                            |
    +================+==================================+
    | Datatype       | :py:data:`BoolEnableDisableChan` |
    +----------------+----------------------------------+
    | Permissions    | read-write                       |
    +----------------+----------------------------------+
    | Channel Based  | True                             |
    +----------------+----------------------------------+
    | Resettable     | No                               |
    +----------------+----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Vertical:Channel Enabled**
            - C Attribute: **NISCOPE_ATTR_CHANNEL_ENABLED**

.. py:attribute:: channel_terminal_configuration

    Specifies how the digitizer configures the channel terminal.

    **Related topics:**

    `NI 5922 Channel Terminal
    Configuration <digitizers.chm::/5922_Chan_Terminal_Configuration.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        channel_terminal_configuration.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        channel_terminal_configuration.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].channel_terminal_configuration = var
            var = session['0,1'].channel_terminal_configuration

    The following table lists the characteristics of this property.

    +----------------+----------------------------------+
    | Characteristic | Value                            |
    +================+==================================+
    | Datatype       | :py:data:`TerminalConfiguration` |
    +----------------+----------------------------------+
    | Permissions    | read-write                       |
    +----------------+----------------------------------+
    | Channel Based  | True                             |
    +----------------+----------------------------------+
    | Resettable     | No                               |
    +----------------+----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Vertical:Channel Terminal Configuration**
            - C Attribute: **NISCOPE_ATTR_CHANNEL_TERMINAL_CONFIGURATION**

.. py:attribute:: cic_decimation

    Controls the decimation in the CIC filter. The CIC filter reduces the
    sample rate of a wideband signal to a rate that other filters in the DDC
    can process. The default value is 4.

    Valid Range: 4 to 32




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        cic_decimation.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        cic_decimation.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].cic_decimation = var
            var = session['0,1'].cic_decimation

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):CIC Filter:Decimation**
            - C Attribute: **NISCOPE_ATTR_CIC_DECIMATION**

.. py:attribute:: cic_shift_gain

    Controls the shift gain at the input to the CIC filter. The CIC filter
    reduces the sample rate of a wideband signal to a rate that other
    filters in the DDC can process. The default value is 0.

    Valid Range: 0 to 15




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        cic_shift_gain.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        cic_shift_gain.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].cic_shift_gain = var
            var = session['0,1'].cic_shift_gain

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):CIC Filter:Shift Gain**
            - C Attribute: **NISCOPE_ATTR_CIC_SHIFT_GAIN**

.. py:attribute:: clock_sync_pulse_source

    For the NI 5102, specifies the line on which the sample clock is sent or
    received. For the NI 5112/5620/5621, specifies the line on which the
    one-time sync pulse is sent or received.

    This line should be the same for all devices to be synchronized.

    **Defined Values**

    VAL\_NO\_SOURCE

    VAL\_RTSI\_0

    VAL\_RTSI\_1

    VAL\_RTSI\_2

    VAL\_RTSI\_3

    VAL\_RTSI\_4

    VAL\_RTSI\_5

    VAL\_RTSI\_6

    VAL\_PFI\_1

    VAL\_PFI\_2

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

            - LabVIEW Property: **Clocking:Clock Sync Pulse Source**
            - C Attribute: **NISCOPE_ATTR_CLOCK_SYNC_PULSE_SOURCE**

.. py:attribute:: combined_decimation

    Returns the combined `DDC <Digitizers.chm::/Glossary.html#DDC>`__
    decimation.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        combined_decimation.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        combined_decimation.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].combined_decimation = var
            var = session['0,1'].combined_decimation

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | True      |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Combined Decimation**
            - C Attribute: **NISCOPE_ATTR_COMBINED_DECIMATION**

.. py:attribute:: coordinate_converter_input

    Selects the source for the input to the coordinate converter, either the
    HB filter or the Programmable FIR. the default value is Programmable
    FIR.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        coordinate_converter_input.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        coordinate_converter_input.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].coordinate_converter_input = var
            var = session['0,1'].coordinate_converter_input

    The following table lists the characteristics of this property.

    +----------------+-------------------------------------+
    | Characteristic | Value                               |
    +================+=====================================+
    | Datatype       | :py:data:`CoordinateConverterInput` |
    +----------------+-------------------------------------+
    | Permissions    | read-write                          |
    +----------------+-------------------------------------+
    | Channel Based  | True                                |
    +----------------+-------------------------------------+
    | Resettable     | No                                  |
    +----------------+-------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Coordinate Converter Input**
            - C Attribute: **NISCOPE_ATTR_COORDINATE_CONVERTER_INPUT**

.. py:attribute:: data_transfer_block_size

    Specifies the maximum number of samples to transfer at one time from the
    device to host memory. Increasing this number should result in better
    fetching performance because the driver does not need to restart the
    transfers as often. However, increasing this number may also increase
    the amount of page-locked memory required from the system.

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

            - LabVIEW Property: **Fetch:Data Transfer Block Size**
            - C Attribute: **NISCOPE_ATTR_DATA_TRANSFER_BLOCK_SIZE**

.. py:attribute:: data_transfer_maximum_bandwidth

    Specifies the maximum bandwidth that the device is allowed to consume.
    The NI device limits itself to transfer fewer bytes per second on the
    PCIe bus than the value you specify for this property.

    **Related topics:**

    `Bandwidth <digitizers.chm::/Analog_Bandwidth.html>`__

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

            - LabVIEW Property: **Fetch:Advanced:Maximum Bandwidth**
            - C Attribute: **NISCOPE_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH**

.. py:attribute:: data_transfer_preferred_packet_size

    Specifies the preferred size of the data field in the PCI Express
    packet. In general, the larger the packet size, the more efficiently the
    device uses the bus. However, some systems, because of their
    implementation, perform better with smaller packet sizes. The value of
    this property must be a power of two (64, 128, ... , 512).

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

            - LabVIEW Property: **Fetch:Advanced:Preferred Packet Size**
            - C Attribute: **NISCOPE_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE**

.. py:attribute:: ddc_center_frequency

    The frequency at which the `DDC <Digitizers.chm::/Glossary.html#DDC>`__
    block frequency translates the input data. The default value is 10 MHz.

    **Valid Values**

    0 - (0.5 × Sample Clock Timebase Rate for digitizer)



    .. note:: This property can be used only with high-speed digitizers that support
        onboard signal processing (OSP). NI-SCOPE returns an error if you use
        this property with a device that does not support OSP.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        ddc_center_frequency.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        ddc_center_frequency.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].ddc_center_frequency = var
            var = session['0,1'].ddc_center_frequency

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Onboard Signal Processing:DDC:Center Frequency**
            - C Attribute: **NISCOPE_ATTR_DDC_CENTER_FREQUENCY**

.. py:attribute:: ddc_data_processing_mode

    The way in which data is processed by the DDC block. The default value
    is Complex.



    .. note:: This property can be used only with high-speed digitizers that support
        onboard signal processing (OSP). NI-SCOPE returns an error if you use
        this property with a device that does not support OSP.

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
    | Resettable     | No                            |
    +----------------+-------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Onboard Signal Processing:DDC:Data Processing Mode**
            - C Attribute: **NISCOPE_ATTR_DDC_DATA_PROCESSING_MODE**

.. py:attribute:: ddc_direct_register_address

    Used for directly accessing the
    `DDC <Digitizers.chm::/Glossary.html#DDC>`__ registers.

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

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:DDC Direct Register Address**
            - C Attribute: **NISCOPE_ATTR_DDC_DIRECT_REGISTER_ADDRESS**

.. py:attribute:: ddc_direct_register_data

    Used for directly accessing the
    `DDC <Digitizers.chm::/Glossary.html#DDC>`__ registers. The default
    value is 0.

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

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:DDC Direct Register Data**
            - C Attribute: **NISCOPE_ATTR_DDC_DIRECT_REGISTER_DATA**

.. py:attribute:: ddc_enabled

    Enables/disables the digital downconverter (DDC) block of the digitizer.
    When the DDC block is disabled, all DDC-related properties are disabled
    and have no effect on the acquired signal. The default value is FALSE.



    .. note:: This property can be used only with high-speed digitizers that support
        onboard signal processing (OSP). NI-SCOPE returns an error if you use
        this property with a device that does not support OSP. For NI 5620/5621
        digitizers, use `Enable DDC <pniScope_EnableDDC.html>`__.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        ddc_enabled.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        ddc_enabled.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].ddc_enabled = var
            var = session['0,1'].ddc_enabled

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Onboard Signal Processing:DDC:DDC Enabled**
            - C Attribute: **NISCOPE_ATTR_DDC_ENABLED**

.. py:attribute:: ddc_frequency_translation_enabled

    Enables/disables frequency translating the data around the user-selected
    center frequency down to baseband. The default value is TRUE.



    .. note:: This property can be used only with high-speed digitizers that support
        onboard signal processing (OSP). NI-SCOPE returns an error if you use
        this property with a device that does not support OSP.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        ddc_frequency_translation_enabled.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        ddc_frequency_translation_enabled.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].ddc_frequency_translation_enabled = var
            var = session['0,1'].ddc_frequency_translation_enabled

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Onboard Signal Processing:DDC:Frequency Translation Enabled**
            - C Attribute: **NISCOPE_ATTR_DDC_FREQUENCY_TRANSLATION_ENABLED**

.. py:attribute:: ddc_frequency_translation_phase_i

    The I oscillator phase in degrees at the first point acquired. The
    default value is 0.

    **Valid Values**

    -360 to 360



    .. note:: This property can be used only with high-speed digitizers that support
        onboard signal processing (OSP). NI-SCOPE returns an error if you use
        this property with a device that does not support OSP.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        ddc_frequency_translation_phase_i.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        ddc_frequency_translation_phase_i.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].ddc_frequency_translation_phase_i = var
            var = session['0,1'].ddc_frequency_translation_phase_i

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Onboard Signal Processing:DDC:Signal Adjustments:Frequency Translation:Frequency Translation Phase I**
            - C Attribute: **NISCOPE_ATTR_DDC_FREQUENCY_TRANSLATION_PHASE_I**

.. py:attribute:: ddc_frequency_translation_phase_q

    The Q oscillator phase in degrees at the first point acquired. Use this
    property only when the `Data Processing
    Mode <pniScope_DataProcessingMode.html>`__ property is set to Complex.
    The default value is 90.

    **Valid Values**

    -360 to 360



    .. note:: This property can be used only with high-speed digitizers that support
        onboard signal processing (OSP). NI-SCOPE returns an error if you use
        this property with a device that does not support OSP.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        ddc_frequency_translation_phase_q.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        ddc_frequency_translation_phase_q.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].ddc_frequency_translation_phase_q = var
            var = session['0,1'].ddc_frequency_translation_phase_q

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Onboard Signal Processing:DDC:Signal Adjustments:Frequency Translation:Frequency Translation Phase Q**
            - C Attribute: **NISCOPE_ATTR_DDC_FREQUENCY_TRANSLATION_PHASE_Q**

.. py:attribute:: ddc_q_source

    Specifies the channel that is the input to the Q data stream of the
    `DDC <Digitizers.chm::/Glossary.html#DDC>`__. The default value is the
    channel to which the property is registered.

    Valid Values: All valid channels for the device.



    .. note:: This property can be used only with high-speed digitizers that support
        onboard signal processing (OSP). NI-SCOPE returns an error if you use
        this property with a device that does not support OSP.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        ddc_q_source.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        ddc_q_source.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].ddc_q_source = var
            var = session['0,1'].ddc_q_source

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Onboard Signal Processing:DDC:Q Source**
            - C Attribute: **NISCOPE_ATTR_DDC_Q_SOURCE**

.. py:attribute:: delay_before_initiate

    Specifies a delay in seconds that is used by `:py:func:`niscope.Initiate`
    Acquisition <scopeviref.chm::/niScope_Initiate_Acquisition.html>`__ to
    allow additional delay between programming of the vertical range,
    trigger level, DDC, and the start of the acquisition. This property is
    supported only on the NI 5112 and the NI 5620/5621. The default value is
    0.0.

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

            - LabVIEW Property: **Acquisition:Delay before Initiate**
            - C Attribute: **NISCOPE_ATTR_DELAY_BEFORE_INITIATE**

.. py:attribute:: device_number

    Indicates the device number associated with the current session.

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

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Device Number**
            - C Attribute: **NISCOPE_ATTR_DEVICE_NUMBER**

.. py:attribute:: device_temperature

    Returns the temperature of the device in degrees Celsius from the
    onboard sensor.

    **Related topics:**

    `Thermal Shutdown <digitizers.chm::/Thermal_Shutdown.html>`__ `PXI/PXIe
    Chassis Cooling <digitizers.chm::/chassis_with_PXIe.html>`__

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

            - LabVIEW Property: **Device:Temperature**
            - C Attribute: **NISCOPE_ATTR_DEVICE_TEMPERATURE**

.. py:attribute:: digital_gain

    Applies gain to the specified channel in hardware before any onboard
    signal processing occurs. The default value is 1.

    The output of the digital gain/offset block is as follows:

    (*ADC value* × *digital gain*) + *digital offset*

    Units: Unitless

    Valid Values: -1.5 to 1.5

    **Related topics:**

    `NI 5622 Onboard Signal Processing
    (OSP) <digitizers.chm::/5622_OSP_diagram.html>`__



    .. note:: This property can be used only with high-speed digitizers that support
        onboard signal processing (OSP). NI-SCOPE returns an error if you use
        this property with a device that does not support OSP.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        digital_gain.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        digital_gain.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].digital_gain = var
            var = session['0,1'].digital_gain

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Vertical:Advanced:Digital Gain**
            - C Attribute: **NISCOPE_ATTR_DIGITAL_GAIN**

.. py:attribute:: digital_offset

    Applies offset to the specified channel in hardware before any onboard
    signal processing occurs. The default value is 0.

    Units: Volts

    **Valid Values**

    ±(Vertical Range × 0.4)

    The output of the digital gain/offset block is as follows:

    (*ADC value* × *digital gain*) + *digital offset*

    **Related topics:**

    `NI 5622 Onboard Signal Processing
    (OSP) <digitizers.chm::/5622_OSP_diagram.html>`__



    .. note:: This property can be used only with high-speed digitizers that support
        onboard signal processing (OSP). NI-SCOPE returns an error if you use
        this property with a device that does not support OSP.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        digital_offset.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        digital_offset.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].digital_offset = var
            var = session['0,1'].digital_offset

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Vertical:Advanced:Digital Offset**
            - C Attribute: **NISCOPE_ATTR_DIGITAL_OFFSET**

.. py:attribute:: discr._enable

    Enables or disables the discriminator. If set to TRUE, frequency
    discriminator is enabled. The default value is FALSE.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        discr._enable.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        discr._enable.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].discr._enable = var
            var = session['0,1'].discr._enable

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:Enable**
            - C Attribute: **NISCOPE_ATTR_DISCR._ENABLE**

.. py:attribute:: discriminator_delay

    Sets the number of delays in the discriminator. The default value is 1.

    Valid Range: 1 to 8




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        discriminator_delay.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        discriminator_delay.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].discriminator_delay = var
            var = session['0,1'].discriminator_delay

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:Delay**
            - C Attribute: **NISCOPE_ATTR_DISCRIMINATOR_DELAY**

.. py:attribute:: discriminator_fir_decimation

    Sets the amount of decimation. The default value is 1.

    Valid Range: 1 to 8




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        discriminator_fir_decimation.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        discriminator_fir_decimation.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].discriminator_fir_decimation = var
            var = session['0,1'].discriminator_fir_decimation

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:FIR Decimation**
            - C Attribute: **NISCOPE_ATTR_DISCRIMINATOR_FIR_DECIMATION**

.. py:attribute:: discriminator_fir_input_source

    Sets the discriminator FIR input source to Phase, Magnitude, or
    Resampler. The default value is Phase.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        discriminator_fir_input_source.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        discriminator_fir_input_source.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].discriminator_fir_input_source = var
            var = session['0,1'].discriminator_fir_input_source

    The following table lists the characteristics of this property.

    +----------------+----------------------------------------+
    | Characteristic | Value                                  |
    +================+========================================+
    | Datatype       | :py:data:`DiscriminatorFIRInputSource` |
    +----------------+----------------------------------------+
    | Permissions    | read-write                             |
    +----------------+----------------------------------------+
    | Channel Based  | True                                   |
    +----------------+----------------------------------------+
    | Resettable     | No                                     |
    +----------------+----------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:FIR Input Source**
            - C Attribute: **NISCOPE_ATTR_DISCRIMINATOR_FIR_INPUT_SOURCE**

.. py:attribute:: discriminator_fir_symmetry

    Sets the discriminator FIR symmetry to symmetric or asymmetric. The
    default value is Symmetric.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        discriminator_fir_symmetry.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        discriminator_fir_symmetry.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].discriminator_fir_symmetry = var
            var = session['0,1'].discriminator_fir_symmetry

    The following table lists the characteristics of this property.

    +----------------+-------------------------------------+
    | Characteristic | Value                               |
    +================+=====================================+
    | Datatype       | :py:data:`DiscriminatorFIRSymmetry` |
    +----------------+-------------------------------------+
    | Permissions    | read-write                          |
    +----------------+-------------------------------------+
    | Channel Based  | True                                |
    +----------------+-------------------------------------+
    | Resettable     | No                                  |
    +----------------+-------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:FIR Symmetry**
            - C Attribute: **NISCOPE_ATTR_DISCRIMINATOR_FIR_SYMMETRY**

.. py:attribute:: discriminator_fir_symmetry_type

    Sets the discriminator FIR symmetry type to even or odd. The default
    value is even.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        discriminator_fir_symmetry_type.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        discriminator_fir_symmetry_type.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].discriminator_fir_symmetry_type = var
            var = session['0,1'].discriminator_fir_symmetry_type

    The following table lists the characteristics of this property.

    +----------------+-----------------------------------------+
    | Characteristic | Value                                   |
    +================+=========================================+
    | Datatype       | :py:data:`DiscriminatorFIRSymmetryType` |
    +----------------+-----------------------------------------+
    | Permissions    | read-write                              |
    +----------------+-----------------------------------------+
    | Channel Based  | True                                    |
    +----------------+-----------------------------------------+
    | Resettable     | No                                      |
    +----------------+-----------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:FIR Symmetry Type**
            - C Attribute: **NISCOPE_ATTR_DISCRIMINATOR_FIR_SYMMETRY_TYPE**

.. py:attribute:: discriminator_fir_taps

    Sets the discriminator FIR number of taps. The default value is 1.

    Valid Range: 1 to 63




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        discriminator_fir_taps.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        discriminator_fir_taps.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].discriminator_fir_taps = var
            var = session['0,1'].discriminator_fir_taps

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:FIR Taps**
            - C Attribute: **NISCOPE_ATTR_DISCRIMINATOR_FIR_TAPS**

.. py:attribute:: discriminator_phase_multiplier

    Programs the coordinate converter to multiply the phase output by 1, 2,
    4, or 8. Multiplying the phase output removes phase modulation before
    the frequency is measured. The default value is 0.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        discriminator_phase_multiplier.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        discriminator_phase_multiplier.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].discriminator_phase_multiplier = var
            var = session['0,1'].discriminator_phase_multiplier

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:Phase Multiplier**
            - C Attribute: **NISCOPE_ATTR_DISCRIMINATOR_PHASE_MULTIPLIER**

.. py:attribute:: dither_enabled

    Enables or disables the analog dither on the device. Using dither can
    improve the spectral performance of the device by reducing the effects
    of quantization. However, adding dither increases the power level to the
    ADC, so you may need to either decrease the signal level or increase the
    vertical range. The default value is FALSE.

    **Related topics:**

    `NI 5620/5621 Signal
    Conditioning <digitizers.chm::/562x_Signal_Cond.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        dither_enabled.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        dither_enabled.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].dither_enabled = var
            var = session['0,1'].dither_enabled

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Vertical:Advanced:Dither Enabled**
            - C Attribute: **NISCOPE_ATTR_DITHER_ENABLED**

.. py:attribute:: enable_dc_restore

    Restores the video-triggered data retrieved by the digitizer to the
    video signal's zero reference point. The default value is FALSE.

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

            - LabVIEW Property: **Triggering:Trigger Video:Enable DC Restore**
            - C Attribute: **NISCOPE_ATTR_ENABLE_DC_RESTORE**

.. py:attribute:: enable_ddc

    Disables programming the DDC when set to FALSE. The default value is
    TRUE.

    This property is supported for NI 5620/5621 digitizers only. For NI
    5142/5622 digitizers, use the `DDC Enabled <pniScope_DDCEnabled.html>`__
    property.

    Custom programming of the DDC using NI-SCOPE property nodes is not
    supported by National Instruments.

    National Instruments supports using the DDC only when the Modulation
    Toolkit and/or Spectral Measurements Toolkit are used, because they make
    use of the DDC automatically (that is, without user intervention) when
    configuration settings allow.

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

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Enable DDC**
            - C Attribute: **NISCOPE_ATTR_ENABLE_DDC**

.. py:attribute:: enable_dither

    Applies dither at the input of the ADC. Set this property to TRUE to
    enable dither. The default value is FALSE.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        enable_dither.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        enable_dither.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].enable_dither = var
            var = session['0,1'].enable_dither

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Enable Dither**
            - C Attribute: **NISCOPE_ATTR_ENABLE_DITHER**

.. py:attribute:: enable_time_interleaved_sampling

    Extends the maximum sample rate on the specified Active Channel for some
    devices that support Time Interleaved Sampling (TIS). TIS enables the
    device to use multiple ADCs to sample the same waveform at a higher
    effective real-time rate. NI 5152/5153/5154 devices fully support
    Read/Write ability for this property. For other devices that use TIS
    mode, such as the NI 5185/5186, this property is Read Only.

    **Related topics:**

    `Time Interleaved
    Sampling <digitizers.chm::/TimeInterleavedSampling.html>`__ `Configuring
    the Horizontal
    Settings <digitizers.chm::/Configuring_Horizontal.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        enable_time_interleaved_sampling.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        enable_time_interleaved_sampling.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].enable_time_interleaved_sampling = var
            var = session['0,1'].enable_time_interleaved_sampling

    The following table lists the characteristics of this property.

    +----------------+---------------------------------+
    | Characteristic | Value                           |
    +================+=================================+
    | Datatype       | :py:data:`BoolEnableDisableTIS` |
    +----------------+---------------------------------+
    | Permissions    | read-write                      |
    +----------------+---------------------------------+
    | Channel Based  | True                            |
    +----------------+---------------------------------+
    | Resettable     | No                              |
    +----------------+---------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Horizontal:Enable Time Interleaved Sampling**
            - C Attribute: **NISCOPE_ATTR_ENABLE_TIME_INTERLEAVED_SAMPLING**

.. py:attribute:: end_of_acquisition_event_output_terminal

    Specifies the destination for the End of Acquisition event. When this
    event is asserted, the digitizer has completed sampling all records.
    Refer to the device specifications document for a list of valid
    destinations.

    **Defined Values**

    VAL\_RTSI\_0

    VAL\_RTSI\_1

    VAL\_RTSI\_2

    VAL\_RTSI\_3

    VAL\_RTSI\_4

    VAL\_RTSI\_5

    VAL\_RTSI\_6

    VAL\_PFI\_0

    VAL\_PFI\_1

    VAL\_PFI\_2

    VAL\_PXI\_STAR

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

            - LabVIEW Property: **Synchronization:End of Acquisition:Output Terminal**
            - C Attribute: **NISCOPE_ATTR_END_OF_ACQUISITION_EVENT_OUTPUT_TERMINAL**

.. py:attribute:: end_of_record_event_output_terminal

    Specifies the destination for the End of Record event. When this event
    is asserted, the digitizer has completed sampling a record. Refer to the
    device specifications document for a list of valid destinations.

    **Defined Values**

    VAL\_RTSI\_0

    VAL\_RTSI\_1

    VAL\_RTSI\_2

    VAL\_RTSI\_3

    VAL\_RTSI\_4

    VAL\_RTSI\_5

    VAL\_RTSI\_6

    VAL\_PFI\_0

    VAL\_PFI\_1

    VAL\_PFI\_2

    VAL\_PXI\_STAR

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

            - LabVIEW Property: **Synchronization:End of Record:Output Terminal**
            - C Attribute: **NISCOPE_ATTR_END_OF_RECORD_EVENT_OUTPUT_TERMINAL**

.. py:attribute:: end_of_record_to_advance_trigger_holdoff

    End of Record to Advance Trigger Holdoff is the length of time (in
    seconds) that a device waits between the completion of one record and
    the acquisition of pre-trigger samples for the next record. During this
    time, the acquisition engine state delays the transition to the Wait for
    Advance Trigger state, and will not store samples in onboard memory,
    accept an Advance Trigger, or trigger on the input signal..

    **Supported Devices**: NI 5185/5186

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

            - LabVIEW Property: **Triggering:End of Record to Advance Trigger Holdoff**
            - C Attribute: **NISCOPE_ATTR_END_OF_RECORD_TO_ADVANCE_TRIGGER_HOLDOFF**

.. py:attribute:: equalization_filter_enabled

    Enables the onboard signal processing equalization FIR block, which is
    connected directly to the input signal. The equalization filter is
    designed to compensate the input signal for artifacts introduced to the
    signal outside of the digitizer. Because this filter is a generic FIR
    filter, any coefficients are valid. Coefficient values should be between
    +1 and -1. The default value is FALSE.



    .. note:: This property can be used only with high-speed digitizers that support
        onboard signal processing (OSP). NI-SCOPE returns an error if you use
        this property with a device that does not support OSP.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        equalization_filter_enabled.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        equalization_filter_enabled.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].equalization_filter_enabled = var
            var = session['0,1'].equalization_filter_enabled

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Onboard Signal Processing:Equalization:Equalization Filter Enabled**
            - C Attribute: **NISCOPE_ATTR_EQUALIZATION_FILTER_ENABLED**

.. py:attribute:: equalization_num_coefficients

    Returns the number of coefficients that the equalization FIR filter can
    accept. This filter is designed to compensate the input signal for
    artifacts introduced to the signal outside of the digitizer. Because
    this filter is a generic FIR filter, any coefficients are valid.
    Coefficient values should be between +1 and -1.



    .. note:: This property can be used only with high-speed digitizers that support
        onboard signal processing (OSP). NI-SCOPE returns an error if you use
        this property with a device that does not support OSP.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        equalization_num_coefficients.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        equalization_num_coefficients.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].equalization_num_coefficients = var
            var = session['0,1'].equalization_num_coefficients

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | int       |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | True      |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Onboard Signal Processing:Equalization:Equalization Num Coefficients**
            - C Attribute: **NISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS**

.. py:attribute:: exported_advance_trigger_output_terminal

    Specifies the destination for the advance trigger. When the advance
    trigger is received, the digitizer begins acquiring pretrigger samples.

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

            - LabVIEW Property: **Synchronization:Advance Trigger:Output Terminal**
            - C Attribute: **NISCOPE_ATTR_EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL**

.. py:attribute:: exported_ref_trigger_output_terminal

    Specifies the destination to export the Reference (Stop) Trigger Refer
    to the device specifications document for a list of valid destinations.

    **Defined Values**

    VAL\_EXTERNAL

    VAL\_RTSI\_0

    VAL\_RTSI\_1

    VAL\_RTSI\_2

    VAL\_RTSI\_3

    VAL\_RTSI\_4

    VAL\_RTSI\_5

    VAL\_RTSI\_6

    VAL\_PFI\_0

    VAL\_PFI\_1

    VAL\_PFI\_2

    VAL\_PXI\_STAR

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

            - LabVIEW Property: **Triggering:Trigger Output Terminal**
            - C Attribute: **NISCOPE_ATTR_EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL**

.. py:attribute:: exported_sample_clock_output_terminal

    Exports the sample clock to a specified terminal. This property is not
    supported by all digitizers.

    The full sample clock rate can be exported to the CLK\_OUT connector. If
    decimating, the divided down sample clock rate can be exported to any of
    the valid destinations.

    **Defined Values**

    VAL\_CLK\_OUT

    VAL\_RTSI\_0

    VAL\_RTSI\_1

    VAL\_RTSI\_2

    VAL\_RTSI\_3

    VAL\_RTSI\_4

    VAL\_RTSI\_5

    VAL\_RTSI\_6

    VAL\_PXI\_STAR

    VAL\_PFI\_0

    VAL\_PFI\_1

    VAL\_PFI\_2

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

            - LabVIEW Property: **Clocking:Exported Sample Clock Output Terminal**
            - C Attribute: **NISCOPE_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL**

.. py:attribute:: exported_start_trigger_output_terminal

    Specifies the destination to export the Start trigger. When the start
    trigger is received, the digitizer begins acquiring data. Refer to the
    device specifications document for a list of valid destinations.

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

            - LabVIEW Property: **Synchronization:Start Trigger (Acq. Arm):Output Terminal**
            - C Attribute: **NISCOPE_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL**

.. py:attribute:: fetch_interleaved_data

    Set to TRUE to retrieve one array with alternating values on the NI
    5620/5621. This property can be used to retrieve a single array with I
    and Q interleaved instead of two separate arrays. If set to TRUE, the
    resulting array is twice the size of the actual record length. The
    default value is FALSE.

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

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Fetch Interleaved Data**
            - C Attribute: **NISCOPE_ATTR_FETCH_INTERLEAVED_DATA**

.. py:attribute:: fetch_interleaved_iq_data

    Specifies whether a fetch call retrieves a single waveform with I and Q
    interleaved, or two separate waveforms. If enabled, the number of
    elements returned by scalar fetch types (such as 16-bit integer) is
    twice the requested number of samples. If disabled during DDC
    acquisitions in Complex mode, two noninterleaved arrays of data are
    returned per channel, per record.



    .. note:: This property can be used only with high-speed digitizers that support
        onboard signal processing (OSP). NI-SCOPE returns an error if you use
        this property with a device that does not support OSP.

    The following table lists the characteristics of this property.

    +----------------+--------------------------------+
    | Characteristic | Value                          |
    +================+================================+
    | Datatype       | :py:data:`BoolEnableDisableIQ` |
    +----------------+--------------------------------+
    | Permissions    | read-write                     |
    +----------------+--------------------------------+
    | Channel Based  | False                          |
    +----------------+--------------------------------+
    | Resettable     | No                             |
    +----------------+--------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Onboard Signal Processing:DDC:Fetch Interleaved IQ Data**
            - C Attribute: **NISCOPE_ATTR_FETCH_INTERLEAVED_IQ_DATA**

.. py:attribute:: fetch_meas_num_samples

    Determines the number of samples to fetch from a digitizer when
    performing a measurement. -1 means fetch all samples from the `Fetch
    Offset <pniScope_FetchOffset.html>`__ property to the end of the current
    record. The default value is -1.

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

            - LabVIEW Property: **Fetch:Fetch Meas Num Samples**
            - C Attribute: **NISCOPE_ATTR_FETCH_MEAS_NUM_SAMPLES**

.. py:attribute:: fetch_num_records

    Fetches multiple records. If you want to fetch all records from the
    record you specify in the `Fetch Record
    Number <pniScope_FetchRecordNumber.html>`__ property to the last record
    configured, use -1. The default value is -1.

    **Related topics:**

    `Making Multiple-Record
    Acquisitions <digitizers.chm::/Making_Multiple-Record_Acquisitions.html>`__
    `Fetching Multiple-Record
    Acquisitions <digitizers.chm::/Fetching_Multiple-Record_Acquisitions.html>`__

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

            - LabVIEW Property: **Fetch:Fetch Number of Records**
            - C Attribute: **NISCOPE_ATTR_FETCH_NUM_RECORDS**

.. py:attribute:: fetch_offset

    Sets the offset in samples; the samples returned also depend on the
    `Fetch Relative To <pniScope_FetchRelativeTo.html>`__ property. The
    default value is 0.

    Valid Values: All integers

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

            - LabVIEW Property: **Fetch:Fetch Offset**
            - C Attribute: **NISCOPE_ATTR_FETCH_OFFSET**

.. py:attribute:: fetch_record_number

    Sets the record to fetch. The record is from a channel you specify. The
    default value is 0.

    Valid Values: Values greater than or equal to 0

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

            - LabVIEW Property: **Fetch:Fetch Record Number**
            - C Attribute: **NISCOPE_ATTR_FETCH_RECORD_NUMBER**

.. py:attribute:: fetch_relative_to

    Specifies which point in the acquired waveform is the first to be
    fetched. This property specifies what the 'Fetch Offset' is relative to.

    The following table lists the characteristics of this property.

    +----------------+----------------------------+
    | Characteristic | Value                      |
    +================+============================+
    | Datatype       | :py:data:`FetchRelativeTo` |
    +----------------+----------------------------+
    | Permissions    | read-write                 |
    +----------------+----------------------------+
    | Channel Based  | False                      |
    +----------------+----------------------------+
    | Resettable     | No                         |
    +----------------+----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Fetch:Fetch Relative To**
            - C Attribute: **NISCOPE_ATTR_FETCH_RELATIVE_TO**

.. py:attribute:: flex_fir_antialias_filter_type

    The NI 5922 flexible-resolution digitizer uses an onboard FIR lowpass
    antialias filter. Use this property to select from several types of
    filters to achieve desired filtering characteristics. For most
    applications, the default value of this property is recommended. The
    other available filters are useful for optimizing settling time
    measurements of step responses. The default value is 48 Tap Standard.

    **Related topics:**

    `Aliasing <digitizers.chm::/Aliasing.html>`__ `FIR
    Filters <digitizers.chm::/FIR_Filters.html>`__



    .. note:: Settling time values refer to the FIR filter only and do not take into
        account settling time caused by the analog front end. Refer to the *NI
        PXI-5922 Specifications* for combined digital and analog settling times.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        flex_fir_antialias_filter_type.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        flex_fir_antialias_filter_type.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].flex_fir_antialias_filter_type = var
            var = session['0,1'].flex_fir_antialias_filter_type

    The following table lists the characteristics of this property.

    +----------------+---------------------------------------+
    | Characteristic | Value                                 |
    +================+=======================================+
    | Datatype       | :py:data:`FlexFIRAntialiasFilterType` |
    +----------------+---------------------------------------+
    | Permissions    | read-write                            |
    +----------------+---------------------------------------+
    | Channel Based  | True                                  |
    +----------------+---------------------------------------+
    | Resettable     | No                                    |
    +----------------+---------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Vertical:Advanced:Flex FIR Antialias Filter Type**
            - C Attribute: **NISCOPE_ATTR_FLEX_FIR_ANTIALIAS_FILTER_TYPE**

.. py:attribute:: fpga_bitfile_path

    Gets the absolute file path to the bitfile loaded on the FPGA.



    .. note:: Gets the absolute file path to the bitfile loaded on the FPGA.

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

            - LabVIEW Property: **Device:FPGA Bitfile Path**
            - C Attribute: **NISCOPE_ATTR_FPGA_BITFILE_PATH**

.. py:attribute:: fractional_resample_enabled

    Enables the onboard signal processing block that resamples the input
    waveform to the user desired sample rate. The default value is FALSE.



    .. note:: This property can be used only with high-speed digitizers that support
        onboard signal processing (OSP). NI-SCOPE returns an error if you use
        this property with a device that does not support OSP.

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

            - LabVIEW Property: **Onboard Signal Processing:Fractional Resample:Fractional Resample Enabled**
            - C Attribute: **NISCOPE_ATTR_FRACTIONAL_RESAMPLE_ENABLED**

.. py:attribute:: group_capabilities

    A string that contains a comma-separated list of class-extension groups
    that this driver implements.

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

            - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities**
            - C Attribute: **NISCOPE_ATTR_GROUP_CAPABILITIES**

.. py:attribute:: halfband_filter_1_enable

    Enables halfband filter 1. If TRUE, filter is enabled. The default is
    TRUE.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        halfband_filter_1_enable.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        halfband_filter_1_enable.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].halfband_filter_1_enable = var
            var = session['0,1'].halfband_filter_1_enable

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):HalfBand Filter:Filter 1 Enable**
            - C Attribute: **NISCOPE_ATTR_HALFBAND_FILTER_1_ENABLE**

.. py:attribute:: halfband_filter_2_enable

    Enables halfband filter 2. If TRUE, filter is enabled. The default is
    FALSE.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        halfband_filter_2_enable.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        halfband_filter_2_enable.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].halfband_filter_2_enable = var
            var = session['0,1'].halfband_filter_2_enable

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):HalfBand Filter:Filter 2 Enable**
            - C Attribute: **NISCOPE_ATTR_HALFBAND_FILTER_2_ENABLE**

.. py:attribute:: halfband_filter_3_enable

    Enables halfband filter 3. If TRUE, filter is enabled. The default is
    FALSE.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        halfband_filter_3_enable.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        halfband_filter_3_enable.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].halfband_filter_3_enable = var
            var = session['0,1'].halfband_filter_3_enable

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):HalfBand Filter:Filter 3 Enable**
            - C Attribute: **NISCOPE_ATTR_HALFBAND_FILTER_3_ENABLE**

.. py:attribute:: halfband_filter_4_enable

    Enables halfband filter 4. If TRUE, filter is enabled. The default is
    FALSE.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        halfband_filter_4_enable.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        halfband_filter_4_enable.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].halfband_filter_4_enable = var
            var = session['0,1'].halfband_filter_4_enable

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):HalfBand Filter:Filter 4 Enable**
            - C Attribute: **NISCOPE_ATTR_HALFBAND_FILTER_4_ENABLE**

.. py:attribute:: halfband_filter_5_enable

    Enables halfband filter 5. If TRUE, filter is enabled. The default is
    FALSE.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        halfband_filter_5_enable.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        halfband_filter_5_enable.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].halfband_filter_5_enable = var
            var = session['0,1'].halfband_filter_5_enable

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):HalfBand Filter:Filter 5 Enable**
            - C Attribute: **NISCOPE_ATTR_HALFBAND_FILTER_5_ENABLE**

.. py:attribute:: halfband_filter_bypass

    Enables or bypasses the halfband filters. If set to TRUE, halfband
    filters are bypassed. The default is TRUE.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        halfband_filter_bypass.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        halfband_filter_bypass.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].halfband_filter_bypass = var
            var = session['0,1'].halfband_filter_bypass

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):HalfBand Filter:Bypass**
            - C Attribute: **NISCOPE_ATTR_HALFBAND_FILTER_BYPASS**

.. py:attribute:: high_pass_filter_frequency

    Specifies the frequency for the highpass filter in Hz. The device uses
    one of the valid values listed below. If an invalid value is specified,
    no coercion occurs. The default value is 0.

    **(PXIe-5164) Valid Values:**

    0 90 450

    **Related topics:**

    `Digital Filtering <digitizers.chm::/Digital_Filtering_Overview.html>`__

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

            - LabVIEW Property: **Vertical:Advanced:High Pass Filter Frequency**
            - C Attribute: **NISCOPE_ATTR_HIGH_PASS_FILTER_FREQUENCY**

.. py:attribute:: horz_enforce_realtime

    Indicates whether the digitizer enforces real-time measurements or
    allows equivalent-time measurements.

    **Related topics:**

    `Sampling Methods <digitizers.chm::/Sampling_Methods.html>`__ `Real-Time
    Sampling <digitizers.chm::/Real-Time_Sampling.html>`__

    The following table lists the characteristics of this property.

    +----------------+--------------------------------------+
    | Characteristic | Value                                |
    +================+======================================+
    | Datatype       | :py:data:`BoolEnableDisableRealtime` |
    +----------------+--------------------------------------+
    | Permissions    | read-write                           |
    +----------------+--------------------------------------+
    | Channel Based  | False                                |
    +----------------+--------------------------------------+
    | Resettable     | No                                   |
    +----------------+--------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Horizontal:Enforce Realtime**
            - C Attribute: **NISCOPE_ATTR_HORZ_ENFORCE_REALTIME**

.. py:attribute:: horz_min_num_pts

    Specifies the minimum number of points you require in the waveform
    record for each channel.

    NI-SCOPE uses the value you specify to configure the record length that
    the digitizer uses for waveform acquisition. The `Actual Record
    Length <pniScope_ActualRecordLength.html>`__ property returns the actual
    record length.

    **Related topics:**

    `Record Length <digitizers.chm::/Record_Length.html>`__ `Sample
    Rate <digitizers.chm::/Sample_Rate.html>`__

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

            - LabVIEW Property: **Horizontal:Min Number of Points**
            - C Attribute: **NISCOPE_ATTR_HORZ_MIN_NUM_PTS**

.. py:attribute:: horz_num_records

    Specify the number of records to acquire.

    **Related topics:**

    `Making Multiple-Record
    Acquisitions <digitizers.chm::/Making_Multiple-Record_Acquisitions.html>`__
    `Fetching Multiple-Record
    Acquisitions <digitizers.chm::/Fetching_Multiple-Record_Acquisitions.html>`__

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

            - LabVIEW Property: **Horizontal:Number of Records**
            - C Attribute: **NISCOPE_ATTR_HORZ_NUM_RECORDS**

.. py:attribute:: horz_record_length

    Returns the actual number of points the digitizer acquires for each
    channel. The value is equal to or greater than the value you specify in
    the `niScope Configure Horizontal
    Timing <scopeviref.chm::/niScope_Configure_Horizontal_Timing.html>`__
    VI.

    Valid Values: 1 to the maximum memory size

    `Record Length <digitizers.chm::/Record_Length.html>`__ `Coercions of
    Horizontal Parameters <digitizers.chm::/Horizontal_Parameters.html>`__

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

            - LabVIEW Property: **Horizontal:Actual Record Length**
            - C Attribute: **NISCOPE_ATTR_HORZ_RECORD_LENGTH**

.. py:attribute:: horz_record_ref_position

    Specifies the position of the Reference Event in the waveform record as
    a percentage of the record.

    When the digitizer detects a trigger, it waits the length of time the
    `Trigger Delay <pniScope_TriggerDelay.html>`__ property specifies. The
    event that occurs when the delay time elapses is the Reference Event.
    The Reference Event is relative to the start of the record and is a
    percentage of the record length. For example, the value 50.0 corresponds
    to the center of the waveform record and 0.0 corresponds to the first
    element in the waveform record.

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

            - LabVIEW Property: **Horizontal:Reference Position**
            - C Attribute: **NISCOPE_ATTR_HORZ_RECORD_REF_POSITION**

.. py:attribute:: horz_sample_rate

    Returns the actual sample rate used for the acquisition.

    Units: hertz (Samples / Second)

    **Related topics:**

    `Sample Clock <digitizers.chm::/Sample_Clock.html>`__

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

            - LabVIEW Property: **Horizontal:Actual Sample Rate**
            - C Attribute: **NISCOPE_ATTR_HORZ_SAMPLE_RATE**

.. py:attribute:: horz_time_per_record

    Specifies the length of time (in seconds) that corresponds to the record
    length. This attribute is invalid when the device is configured to use
    an external sample clock timebase. This attribute is also invalid when a
    DDC is enabled. When both the Time Per Record Property and the `Min
    Sample Rate <pniScope_MinSampleRate.html>`__ Property are set, the
    attribute that was set first is ignored.

    **Related topics:**

    `Record Length <digitizers.chm::/Record_Length.html>`__ `Sample
    Rate <digitizers.chm::/Sample_Rate.html>`__

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

            - LabVIEW Property: **Horizontal:Advanced:Time Per Record**
            - C Attribute: **NISCOPE_ATTR_HORZ_TIME_PER_RECORD**

.. py:attribute:: input_clock_source

    Specifies the input source for the PLL reference clock for all boards
    except the NI 5102. For the NI 5102 this property is the source of the
    board clock.

    **Defined Values**

    VAL\_NO\_SOURCE

    VAL\_PFI\_0

    VAL\_PFI\_1

    VAL\_PFI\_2

    VAL\_PXI\_CLOCK

    VAL\_CLK\_IN

    VAL\_EXTERNAL

    VAL\_RTSI\_CLOCK

    **Related topics:**

    `Reference Clock/Phase-Lock
    Loop <digitizers.chm::/Reference_Clock.html>`__

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

            - LabVIEW Property: **Clocking:Reference (Input) Clock Source**
            - C Attribute: **NISCOPE_ATTR_INPUT_CLOCK_SOURCE**

.. py:attribute:: input_impedance

    Specifies the input impedance for the channel in ohms.

    **Defined Values**

    50 Ohm

    1 M Ohm

    **Related topics:**

    `Impedance and Impedance
    Matching <digitizers.chm::/Impedance_and_Impedance_Matching.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        input_impedance.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        input_impedance.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].input_impedance = var
            var = session['0,1'].input_impedance

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Vertical:Input Impedance**
            - C Attribute: **NISCOPE_ATTR_INPUT_IMPEDANCE**

.. py:attribute:: instrument_firmware_revision

    A string that contains the firmware revision information for the current
    instrument.

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

            - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Firmware Revision**
            - C Attribute: **NISCOPE_ATTR_INSTRUMENT_FIRMWARE_REVISION**

.. py:attribute:: instrument_manufacturer

    A string that contains the name of the instrument manufacturer, for
    example, "National Instruments".

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

            - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Manufacturer**
            - C Attribute: **NISCOPE_ATTR_INSTRUMENT_MANUFACTURER**

.. py:attribute:: instrument_model

    A string that contains the model number of the current instrument.

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

            - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Model**
            - C Attribute: **NISCOPE_ATTR_INSTRUMENT_MODEL**

.. py:attribute:: interchange_check

    Specifies whether to perform interchangeability checking and log
    interchangeability warnings when you call VIs. Interchangeability
    warnings indicate that using your application with a different
    instrument might cause different behavior.

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

            - LabVIEW Property: **Inherent IVI Attributes:User Options:Interchange Check**
            - C Attribute: **NISCOPE_ATTR_INTERCHANGE_CHECK**

.. py:attribute:: interleaving_offset_correction_enabled

    Enables the interleaving offset correction on the specified channel. The
    default value is TRUE.

    **Related topics:**

    `Timed Interleaved
    Sampling <digitizers.chm::/TimeInterleavedSampling.html>`__



    .. note:: If disabled, warranted specifications are not guaranteed.

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

            - LabVIEW Property: **Vertical:Advanced:Interleaving Offset Correction Enabled**
            - C Attribute: **NISCOPE_ATTR_INTERLEAVING_OFFSET_CORRECTION_ENABLED**

.. py:attribute:: io_resource_descriptor

    Indicates the resource descriptor the driver uses to identify the
    physical device. If you initialize the driver with a logical name, this
    property contains the resource descriptor that corresponds to the entry
    in the IVI Configuration utility. If you initialize the instrument
    driver with the resource descriptor, this property contains that value.

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

            - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Resource Descriptor**
            - C Attribute: **NISCOPE_ATTR_IO_RESOURCE_DESCRIPTOR**

.. py:attribute:: logical_name

    A string that contains the logical name you specified when opening the
    current IVI session.

    You can pass a logical name to `niScope
    Initialize <scopeviref.chm::/niScope_Initialize.html>`__ or `niScope
    Initialize with
    Options <scopeviref.chm::/niScope_Initialize_With_Options.html>`__. The
    IVI Configuration utility must contain an entry for the logical name.
    The logical name entry refers to a virtual instrument section in the IVI
    Configuration file. The virtual instrument section specifies a physical
    device and initial user options.

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

            - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Logical Name**
            - C Attribute: **NISCOPE_ATTR_LOGICAL_NAME**

.. py:attribute:: master_enable

    Specifies whether the device is a master or a slave.

    The master device is typically the originator of the trigger signal and
    clock sync pulse. For a stand-alone device, set this property to FALSE.

    **Valid Range**

    TRUE—Master

    FALSE—Slave

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

            - LabVIEW Property: **Synchronization:Master Enable**
            - C Attribute: **NISCOPE_ATTR_MASTER_ENABLE**

.. py:attribute:: max_input_frequency

    Specifies the bandwidth of the channel in hertz. Express this value as
    the frequency at which the input circuitry attenuates the input signal
    by 3 dB.

    Special Values:

    (-1) Full bandwidth

    (0) Device default

    **Related topics:**

    `Bandwidth <digitizers.chm::/Analog_Bandwidth.html>`__ `Probes and Their
    Effects <digitizers.chm::/Probes.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        max_input_frequency.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        max_input_frequency.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].max_input_frequency = var
            var = session['0,1'].max_input_frequency

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Vertical:Maximum Input Frequency**
            - C Attribute: **NISCOPE_ATTR_MAX_INPUT_FREQUENCY**

.. py:attribute:: max_real_time_sampling_rate

    Returns the maximum real-time sample rate in hertz.

    **Related topics:**

    `Sampling Methods <digitizers.chm::/Sampling_Methods.html>`__ `Real-Time
    Sampling <digitizers.chm::/Real-Time_Sampling.html>`__

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

            - LabVIEW Property: **Horizontal:Maximum Real Time Sample Rate**
            - C Attribute: **NISCOPE_ATTR_MAX_REAL_TIME_SAMPLING_RATE**

.. py:attribute:: max_ris_rate

    Returns the maximum RIS sampling rate in hertz.

    **Related topics:**

    `Sampling Methods <digitizers.chm::/Sampling_Methods.html>`__
    `Equivalent-Time Sampling and Random Interleaved
    Sampling <digitizers.chm::/ris.html>`__

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

            - LabVIEW Property: **Horizontal:Maximum RIS Rate**
            - C Attribute: **NISCOPE_ATTR_MAX_RIS_RATE**

.. py:attribute:: meas_array_gain

    Every element of an array is multiplied by this scalar value during the
    array gain measurement. The default value is 1.0.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_array_gain.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_array_gain.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_array_gain = var
            var = session['0,1'].meas_array_gain

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Array Gain**
            - C Attribute: **NISCOPE_ATTR_MEAS_ARRAY_GAIN**

.. py:attribute:: meas_array_offset

    Every element of an array is added to this scalar value during the array
    offset measurement. The default value is 0.0.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_array_offset.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_array_offset.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_array_offset = var
            var = session['0,1'].meas_array_offset

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Array Offset**
            - C Attribute: **NISCOPE_ATTR_MEAS_ARRAY_OFFSET**

.. py:attribute:: meas_chan_high_ref_level

    Specifies the high reference level used in many scalar measurements. The
    default value is 90%.

    Units: Percentage of the signal based on the selected `Percentage Units
    Method <pniScope_PercentageMethod.html>`__ property.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_chan_high_ref_level.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_chan_high_ref_level.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_chan_high_ref_level = var
            var = session['0,1'].meas_chan_high_ref_level

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Reference Levels:Channel Based High Ref Level**
            - C Attribute: **NISCOPE_ATTR_MEAS_CHAN_HIGH_REF_LEVEL**

.. py:attribute:: meas_chan_low_ref_level

    Specifies the low reference level used in many scalar measurements. The
    default value is 10.0%.

    Units: Percentage of the signal based on the selected `Percentage Units
    Method <pniScope_PercentageMethod.html>`__ property.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_chan_low_ref_level.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_chan_low_ref_level.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_chan_low_ref_level = var
            var = session['0,1'].meas_chan_low_ref_level

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Reference Levels:Channel Based Low Ref Level**
            - C Attribute: **NISCOPE_ATTR_MEAS_CHAN_LOW_REF_LEVEL**

.. py:attribute:: meas_chan_mid_ref_level

    Specifies the mid reference level used in many scalar measurements. The
    default value is 50%.

    Units: Percentage of the signal based on the selected `Percentage Units
    Method <pniScope_PercentageMethod.html>`__ property.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_chan_mid_ref_level.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_chan_mid_ref_level.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_chan_mid_ref_level = var
            var = session['0,1'].meas_chan_mid_ref_level

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Reference Levels:Channel Based Mid Ref Level**
            - C Attribute: **NISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL**

.. py:attribute:: meas_filter_center_freq

    The center frequency in hertz for filters of type bandpass and bandstop.
    The width of the filter is specified by Filter Width, where the cutoff
    frequencies are the center width. The default value is 1.0e6 Hz.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_filter_center_freq.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_filter_center_freq.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_filter_center_freq = var
            var = session['0,1'].meas_filter_center_freq

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Filter:Center Frequency**
            - C Attribute: **NISCOPE_ATTR_MEAS_FILTER_CENTER_FREQ**

.. py:attribute:: meas_filter_cutoff_freq

    Specifies the cutoff frequency in hertz for filters of type lowpass and
    highpass. The cutoff frequency definition varies depending on the
    filter. The default value is 1.0e6 Hz.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_filter_cutoff_freq.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_filter_cutoff_freq.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_filter_cutoff_freq = var
            var = session['0,1'].meas_filter_cutoff_freq

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Filter:Cutoff Frequency**
            - C Attribute: **NISCOPE_ATTR_MEAS_FILTER_CUTOFF_FREQ**

.. py:attribute:: meas_filter_order

    Specifies the order of the infinite impulse response filter. The default
    value is 2.

    Valid Values: >0

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

            - LabVIEW Property: **Waveform Measurement:Filter:IIR Order**
            - C Attribute: **NISCOPE_ATTR_MEAS_FILTER_ORDER**

.. py:attribute:: meas_filter_ripple

    Specifies the amount of passband ripple (in dB) for Chebyshev filters.
    More ripple gives a sharper cutoff for a given filter order. The default
    value is 0.1.

    Valid Values: >0.0

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

            - LabVIEW Property: **Waveform Measurement:Filter:Ripple**
            - C Attribute: **NISCOPE_ATTR_MEAS_FILTER_RIPPLE**

.. py:attribute:: meas_filter_taps

    Specifies the number of taps for the finite impulse response filter.
    This value must be odd if the filter type is highpass or bandstop.
    Otherwise, the magnitude response goes to zero as the frequency goes to
    half the sampling rate. The default value is 25.

    Valid Values: >0

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

            - LabVIEW Property: **Waveform Measurement:Filter:FIR Taps**
            - C Attribute: **NISCOPE_ATTR_MEAS_FILTER_TAPS**

.. py:attribute:: meas_filter_transient_waveform_percent

    The percentage (0 - 100%) of the infinite impulse response (IIR)
    filtered waveform to eliminate from the beginning of the waveform. This
    action allows eliminating the transient portion of the waveform that is
    undefined due to the assumptions necessary at the boundary condition.
    The default value is 20.0%.

    Valid Range: 0.0 - 100.0%




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_filter_transient_waveform_percent.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_filter_transient_waveform_percent.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_filter_transient_waveform_percent = var
            var = session['0,1'].meas_filter_transient_waveform_percent

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Filter:Percent Waveform Transient**
            - C Attribute: **NISCOPE_ATTR_MEAS_FILTER_TRANSIENT_WAVEFORM_PERCENT**

.. py:attribute:: meas_filter_type

    Specifies the type of digital filter. The default value is lowpass.

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
    | Resettable     | No                    |
    +----------------+-----------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Filter:Type**
            - C Attribute: **NISCOPE_ATTR_MEAS_FILTER_TYPE**

.. py:attribute:: meas_filter_width

    Specifies the width (in Hz) of a bandpass or bandstop filter. The cutoff
    frequencies are the (center frequency property ± 0.5 × filter width).
    The default value is 1.0e3.

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

            - LabVIEW Property: **Waveform Measurement:Filter:Width**
            - C Attribute: **NISCOPE_ATTR_MEAS_FILTER_WIDTH**

.. py:attribute:: meas_fir_filter_window

    Specifies the FIR window type. The symmetric windows are applied to the
    FIR filter coefficients to limit passband ripple in FIR filters. The
    default value is None (0).




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_fir_filter_window.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_fir_filter_window.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_fir_filter_window = var
            var = session['0,1'].meas_fir_filter_window

    The following table lists the characteristics of this property.

    +----------------+----------------------------+
    | Characteristic | Value                      |
    +================+============================+
    | Datatype       | :py:data:`FIRFilterWindow` |
    +----------------+----------------------------+
    | Permissions    | read-write                 |
    +----------------+----------------------------+
    | Channel Based  | True                       |
    +----------------+----------------------------+
    | Resettable     | No                         |
    +----------------+----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Filter:FIR Window**
            - C Attribute: **NISCOPE_ATTR_MEAS_FIR_FILTER_WINDOW**

.. py:attribute:: meas_hysteresis_percent

    Digital hysteresis that is used in several of the scalar waveform
    measurements. This property specifies the percentage of the full-scale
    vertical range for the hysteresis window size. The default value is 2%.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_hysteresis_percent.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_hysteresis_percent.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_hysteresis_percent = var
            var = session['0,1'].meas_hysteresis_percent

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Hysteresis Percent**
            - C Attribute: **NISCOPE_ATTR_MEAS_HYSTERESIS_PERCENT**

.. py:attribute:: meas_interpolation_sampling_factor

    The new number of points for polynomial interpolation is the sampling
    factor times the input number of points. The default value is 0.0.

    For example, if you acquire 1,000 points with the digitizer and set this
    property to 2.5, calling the `niScope Fetch Measurement
    (poly) <scopeviref.chm::/niScope_Fetch_Measurement_(poly).html>`__ VI
    (Measurement Scalar DBL instance), with the Polynomial Interpolation
    measurement resamples the waveform to 2,500 points.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_interpolation_sampling_factor.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_interpolation_sampling_factor.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_interpolation_sampling_factor = var
            var = session['0,1'].meas_interpolation_sampling_factor

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Interpolation:Sampling Factor**
            - C Attribute: **NISCOPE_ATTR_MEAS_INTERPOLATION_SAMPLING_FACTOR**

.. py:attribute:: meas_last_acq_histogram_size

    Specifies the size (that is, the number of bins) in the last acquisition
    histogram. This histogram is used to determine several scalar
    measurements, most importantly voltage low and voltage high. The default
    value is 256.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_last_acq_histogram_size.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_last_acq_histogram_size.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_last_acq_histogram_size = var
            var = session['0,1'].meas_last_acq_histogram_size

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Last Acq. Histogram Size**
            - C Attribute: **NISCOPE_ATTR_MEAS_LAST_ACQ_HISTOGRAM_SIZE**

.. py:attribute:: meas_other_channel

    Specifies the second channel for two-channel measurements, such as `Add
    Channels <Digitizers.chm::/Add_Channels.html>`__. If processing steps
    are registered with this channel, the processing happens before the
    waveform is used in a two-channel measurement. The default value is 0.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_other_channel.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_other_channel.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_other_channel = var
            var = session['0,1'].meas_other_channel

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | str        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Other Channel**
            - C Attribute: **NISCOPE_ATTR_MEAS_OTHER_CHANNEL**

.. py:attribute:: meas_percentage_method

    Specifies the method used to map percentage reference units to voltages.
    The default value is BaseTop.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_percentage_method.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_percentage_method.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_percentage_method = var
            var = session['0,1'].meas_percentage_method

    The following table lists the characteristics of this property.

    +----------------+-----------------------------+
    | Characteristic | Value                       |
    +================+=============================+
    | Datatype       | :py:data:`PercentageMethod` |
    +----------------+-----------------------------+
    | Permissions    | read-write                  |
    +----------------+-----------------------------+
    | Channel Based  | True                        |
    +----------------+-----------------------------+
    | Resettable     | No                          |
    +----------------+-----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Reference Levels:Percentage Units Method**
            - C Attribute: **NISCOPE_ATTR_MEAS_PERCENTAGE_METHOD**

.. py:attribute:: meas_polynomial_interpolation_order

    Specifies the order of the polynomial used during the polynomial
    interpolation array measurement. For example, an order of 1 is linear
    interpolation whereas an order of 2 specifies parabolic interpolation.
    Any positive integer is valid. The default value is 1 (linear
    interpolation).

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

            - LabVIEW Property: **Waveform Measurement:Interpolation:Polynomial Interpolation Order**
            - C Attribute: **NISCOPE_ATTR_MEAS_POLYNOMIAL_INTERPOLATION_ORDER**

.. py:attribute:: meas_ref_level_units

    Specifies the units for the waveform measurement reference levels.

    If you choose percentage, the measurement routine uses the `Percentage
    Method <pniScope_PercentageMethod.html>`__ property to map the
    percentage values to voltages. If you choose voltage units, you can set
    the voltage thresholds directly and avoid extra calculations.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_ref_level_units.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_ref_level_units.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_ref_level_units = var
            var = session['0,1'].meas_ref_level_units

    The following table lists the characteristics of this property.

    +----------------+---------------------------+
    | Characteristic | Value                     |
    +================+===========================+
    | Datatype       | :py:data:`Ref.LevelUnits` |
    +----------------+---------------------------+
    | Permissions    | read-write                |
    +----------------+---------------------------+
    | Channel Based  | True                      |
    +----------------+---------------------------+
    | Resettable     | No                        |
    +----------------+---------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Reference Levels:Units**
            - C Attribute: **NISCOPE_ATTR_MEAS_REF_LEVEL_UNITS**

.. py:attribute:: meas_time_histogram_high_time

    Specifies the maximum time limit (in seconds) of the Multi-Acquisition
    time histogram, where the time is in seconds relative to the trigger
    position. Only points in the waveform between the low and high time
    limits are included in the histogram. The default value is 5.0e-4 .

    This value is used during the first time histogram measurement, and it
    is not updated until you call `niScope Clear Waveform Measurement
    Stats <scopeviref.chm::/niScope_Clear_Waveform_Measurement_Stats.html>`__.

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

            - LabVIEW Property: **Waveform Measurement:Time Histogram:High Time**
            - C Attribute: **NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_HIGH_TIME**

.. py:attribute:: meas_time_histogram_high_volts

    Specifies the high voltage limit for the Multi-Acquisition time
    histogram. Only points in the waveform between the low and high voltage
    limits are included in the histogram. The default value is 10.0 V.

    This value is used during the first time histogram measurement, and it
    is not updated until you call `niScope Clear Waveform Measurement
    Stats <scopeviref.chm::/niScope_Clear_Waveform_Measurement_Stats.html>`__.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_time_histogram_high_volts.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_time_histogram_high_volts.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_time_histogram_high_volts = var
            var = session['0,1'].meas_time_histogram_high_volts

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Time Histogram:High Volts**
            - C Attribute: **NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_HIGH_VOLTS**

.. py:attribute:: meas_time_histogram_low_time

    Specifies the minimum time limit (in seconds) of the multi-acquisition
    time histogram, where the time is in seconds relative to the trigger
    position. Only points in the waveform between the low and high time
    limits are included in the histogram. The default value is -5.0e-4 .

    This value is used during the first time histogram measurement, and it
    is not updated until you call `niScope Clear Waveform Measurement
    Stats <scopeviref.chm::/niScope_Clear_Waveform_Measurement_Stats.html>`__.

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

            - LabVIEW Property: **Waveform Measurement:Time Histogram:Low Time**
            - C Attribute: **NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_LOW_TIME**

.. py:attribute:: meas_time_histogram_low_volts

    Specifies the low voltage limit for the multi-acquisition time
    histogram. Only points in the waveform between the low and high voltage
    limits are included in the histogram. The default value is -10.0.

    This value is used during the first running time histogram measurement,
    and it is not updated until you call `niScope Clear Waveform Measurement
    Stats <scopeviref.chm::/niScope_Clear_Waveform_Measurement_Stats.html>`__.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_time_histogram_low_volts.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_time_histogram_low_volts.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_time_histogram_low_volts = var
            var = session['0,1'].meas_time_histogram_low_volts

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Time Histogram:Low Volts**
            - C Attribute: **NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_LOW_VOLTS**

.. py:attribute:: meas_time_histogram_size

    Determines the multiple acquisition time histogram size. The size is set
    during the first call to a time histogram measurement after you clear
    the measurement history with `niScope Clear Waveform Measurement
    Stats <scopeviref.chm::/niScope_Clear_Waveform_Measurement_Stats.html>`__.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_time_histogram_size.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_time_histogram_size.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_time_histogram_size = var
            var = session['0,1'].meas_time_histogram_size

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Time Histogram:Size**
            - C Attribute: **NISCOPE_ATTR_MEAS_TIME_HISTOGRAM_SIZE**

.. py:attribute:: meas_voltage_histogram_high_volts

    Specifies the maximum voltage value in the running voltage histogram.
    The default value is 10.0.

    This value is used during the first running voltage histogram
    measurement, and it is not updated until you call `niScope Clear
    Waveform Measurement
    Stats <scopeviref.chm::/niScope_Clear_Waveform_Measurement_Stats.html>`__.

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

            - LabVIEW Property: **Waveform Measurement:Voltage Histogram:High Volts**
            - C Attribute: **NISCOPE_ATTR_MEAS_VOLTAGE_HISTOGRAM_HIGH_VOLTS**

.. py:attribute:: meas_voltage_histogram_low_volts

    Specifies the minimum voltage value in the running voltage histogram.
    The default value is -10.0.

    This value is used during the first running voltage histogram
    measurement, and it is not updated until you call `niScope Clear
    Waveform Measurement
    Stats <scopeviref.chm::/niScope_Clear_Waveform_Measurement_Stats.html>`__.

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

            - LabVIEW Property: **Waveform Measurement:Voltage Histogram:Low Volts**
            - C Attribute: **NISCOPE_ATTR_MEAS_VOLTAGE_HISTOGRAM_LOW_VOLTS**

.. py:attribute:: meas_voltage_histogram_size

    Specifies the number of bins in the running voltage histogram. The
    default value is 256.

    This value is used during the first running voltage histogram
    measurement, and it is not updated until you call `niScope Clear
    Waveform Measurement
    Stats <scopeviref.chm::/niScope_Clear_Waveform_Measurement_Stats.html>`__.

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

            - LabVIEW Property: **Waveform Measurement:Voltage Histogram:Size**
            - C Attribute: **NISCOPE_ATTR_MEAS_VOLTAGE_HISTOGRAM_SIZE**

.. py:attribute:: min_sample_rate

    Specifies the sampling rate (in Samples/second) for the acquisition.
    This attribute is invalid when the device is configured to use an
    external sample clock timebase. When a DDC is enabled, this attribute
    specifices the IQ rate. When both the `Time Per
    Record <pniScope_TimePerRecord.html>`__ Property and the Min Sample Rate
    Property are set, the attribute that was set first is ignored.

    Valid Values: The combination of sampling rate and minimum record length
    must allow the digitizer to sample at a valid sampling rate for the
    acquisition type specified in the `niScope Configure
    Acquisition <scopeviref.chm::/niScope_Configure_Acquisition.html>`__ VI
    and not require more memory than the onboard memory module allows.

    `Sample Rate <digitizers.chm::/Sample_Rate.html>`__ `Coercions of
    Horizontal Parameters <digitizers.chm::/Horizontal_Parameters.html>`__

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

            - LabVIEW Property: **Horizontal:Min Sample Rate**
            - C Attribute: **NISCOPE_ATTR_MIN_SAMPLE_RATE**

.. py:attribute:: mux_mode_register

    

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

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Mux Mode**
            - C Attribute: **NISCOPE_ATTR_MUX_MODE_REGISTER**

.. py:attribute:: onboard_memory_size

    Returns the total combined amount of onboard memory for all channels in
    bytes.

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

            - LabVIEW Property: **Horizontal:Memory Size**
            - C Attribute: **NISCOPE_ATTR_ONBOARD_MEMORY_SIZE**

.. py:attribute:: oscillator_phase_dac_value

    Gets or sets the binary phase DAC value that controls the delay added to
    the Phase Locked Loop (PLL) of the sample clock. The default value is "
    ".



    .. note:: If this value is set, sample clock adjustments and TClk cannot do any
        subsample adjustment of the timebase sample clock.

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

            - LabVIEW Property: **Clocking:Advanced:Oscillator Phase DAC Value**
            - C Attribute: **NISCOPE_ATTR_OSCILLATOR_PHASE_DAC_VALUE**

.. py:attribute:: output_clock_source

    Specifies the output source for the 10 MHz clock to which another
    digitizer's sample clock can be phased-locked.

    The NI 5102 uses a 20 MHz system clock.

    **Defined Values**

    None

    VAL\_RTSI\_CLOCK

    VAL\_PFI\_0

    VAL\_PFI\_1

    VAL\_PFI\_2

    VAL\_CLK\_OUT

    VAL\_RTSI\_0

    VAL\_RTSI\_1

    VAL\_RTSI\_2

    VAL\_RTSI\_3

    VAL\_RTSI\_4

    VAL\_RTSI\_5

    VAL\_RTSI\_6

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

            - LabVIEW Property: **Clocking:Output Clock Source**
            - C Attribute: **NISCOPE_ATTR_OUTPUT_CLOCK_SOURCE**

.. py:attribute:: overflow_error_reporting

    Configures error reporting when the onboard signal processing block
    detects an overflow in any of its stages. Overflows lead to clipping of
    the waveform. The default value is Warning.

    The following table lists the characteristics of this property.

    +----------------+-----------------------------------+
    | Characteristic | Value                             |
    +================+===================================+
    | Datatype       | :py:data:`OverflowErrorReporting` |
    +----------------+-----------------------------------+
    | Permissions    | read-write                        |
    +----------------+-----------------------------------+
    | Channel Based  | False                             |
    +----------------+-----------------------------------+
    | Resettable     | No                                |
    +----------------+-----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Onboard Signal Processing:OSP Overflow Error Reporting**
            - C Attribute: **NISCOPE_ATTR_OVERFLOW_ERROR_REPORTING**

.. py:attribute:: p2p_channels_to_stream

    Specifies which channels will be written to a peer-to-peer endpoint. If
    multiple channels are specified, they will be interleaved by sample.
    This property is endpoint-based. The default value is 0.



    .. note:: This property must either be unused or set to all enabled channels on NI
        5160/5162 digitizers.

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

            - LabVIEW Property: **Peer-to-Peer:Channels to Stream**
            - C Attribute: **NISCOPE_ATTR_P2P_CHANNELS_TO_STREAM**

.. py:attribute:: p2p_data_trans_permission_addr

    Returns the address of a hardware register used to grant permission for
    the peer-to-peer endpoint to write data to another peer. The type of
    this address is determined by the `Data Transfer Permission Address
    Type <pniScope_P2PDataTransferPermissionAddressType.html>`__ property.
    Permission is granted in bytes and the register is additive. This
    property is endpoint-based.



    .. note:: This property can be used only with high-speed digitizers that support
        peer-to-peer streaming.

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

            - LabVIEW Property: **Peer-to-Peer:Manual:Configuration:Data Transfer Permission Address**
            - C Attribute: **NISCOPE_ATTR_P2P_DATA_TRANS_PERMISSION_ADDR**

.. py:attribute:: p2p_data_trans_permission_addr_type

    Specifies the type of address returned to the user from the `Data
    Transfer Permission
    Address <pniScope_P2PDataTransferPermissionAddress.html>`__ property.
    This property is endpoint-based.



    .. note:: This property can be used only with high-speed digitizers that support
        peer-to-peer streaming.

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | :py:data:`AddressType` |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | False                  |
    +----------------+------------------------+
    | Resettable     | No                     |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Peer-to-Peer:Manual:Configuration:Data Transfer Permission Address Type**
            - C Attribute: **NISCOPE_ATTR_P2P_DATA_TRANS_PERMISSION_ADDR_TYPE**

.. py:attribute:: p2p_destination_window_addr

    Specifies the destination for data written by the peer-to-peer endpoint.
    The type of this address is specified by the `Destination Window Address
    Type <pniScope_P2PDestinationWindowAddressType.html>`__ property. This
    property is endpoint-based.

    **Valid Values**

    A valid, non-NULL, physical or virtual address.



    .. note:: This property can be used only with high-speed digitizers that support
        peer-to-peer streaming.

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

            - LabVIEW Property: **Peer-to-Peer:Manual:Configuration:Destination Window Address**
            - C Attribute: **NISCOPE_ATTR_P2P_DESTINATION_WINDOW_ADDR**

.. py:attribute:: p2p_destination_window_addr_type

    Specifies the type of the `Destination Window
    Address <pniScope_P2PDestinationWindowAddress.html>`__ property. This
    property is endpoint-based.



    .. note:: This property can be used only with high-speed digitizers that support
        peer-to-peer streaming.

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | :py:data:`AddressType` |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | False                  |
    +----------------+------------------------+
    | Resettable     | No                     |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Peer-to-Peer:Manual:Configuration:Destination Window Address Type**
            - C Attribute: **NISCOPE_ATTR_P2P_DESTINATION_WINDOW_ADDR_TYPE**

.. py:attribute:: p2p_destination_window_size

    Specifies the size, in bytes, of the destination window determined by
    the `Destination Window
    Address <pniScope_P2PDestinationWindowAddress.html>`__ and `Destination
    Window Address Type <pniScope_P2PDestinationWindowAddressType.html>`__
    properties. This property is endpoint-based.



    .. note:: This property can be used only with high-speed digitizers that support
        peer-to-peer streaming.

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

            - LabVIEW Property: **Peer-to-Peer:Manual:Configuration:Destination Window Size**
            - C Attribute: **NISCOPE_ATTR_P2P_DESTINATION_WINDOW_SIZE**

.. py:attribute:: p2p_enabled

    Specifies whether the digitizer writes data to the peer-to-peer
    endpoint. This property is endpoint-based.



    .. note:: This property can be used only with high-speed digitizers that support
        peer-to-peer streaming.

    The following table lists the characteristics of this property.

    +----------------+------------------------------+
    | Characteristic | Value                        |
    +================+==============================+
    | Datatype       | :py:data:`BoolEnableDisable` |
    +----------------+------------------------------+
    | Permissions    | read-write                   |
    +----------------+------------------------------+
    | Channel Based  | False                        |
    +----------------+------------------------------+
    | Resettable     | No                           |
    +----------------+------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Peer-to-Peer:P2P Enabled**
            - C Attribute: **NISCOPE_ATTR_P2P_ENABLED**

.. py:attribute:: p2p_endpoint_overflow

    Returns TRUE if the peer-to-peer endpoint has overflowed. Reset the
    endpoint to clear the overflow condition. This property is
    endpoint-based.



    .. note:: This property can be used only with high-speed digitizers that support
        peer-to-peer streaming.

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

            - LabVIEW Property: **Peer-to-Peer:Endpoint Overflow**
            - C Attribute: **NISCOPE_ATTR_P2P_ENDPOINT_OVERFLOW**

.. py:attribute:: p2p_endpoint_size

    Returns the size, in samples, of the peer-to-peer endpoint. This
    property is endpoint-based.



    .. note:: This property can be used only with high-speed digitizers that support
        peer-to-peer streaming.

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

            - LabVIEW Property: **Peer-to-Peer:Endpoint Size**
            - C Attribute: **NISCOPE_ATTR_P2P_ENDPOINT_SIZE**

.. py:attribute:: p2p_fifo_endpoint_count

    Returns the number of FIFO-based peer-to-peer endpoints this device
    supports.



    .. note:: This property can be used only with high-speed digitizers that support
        peer-to-peer streaming.

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

            - LabVIEW Property: **Peer-to-Peer:FIFO Endpoint Count**
            - C Attribute: **NISCOPE_ATTR_P2P_FIFO_ENDPOINT_COUNT**

.. py:attribute:: p2p_manual_configuration_enabled

    Enables and disables manual configuration of a peer-to-peer endpoint.
    These attributes cannot be used if an endpoint is being configured by
    NI-P2P, or a resource reservation error will result. This property is
    endpoint-based.



    .. note:: This property can be used only with high-speed digitizers that support
        peer-to-peer streaming.

    The following table lists the characteristics of this property.

    +----------------+------------------------------+
    | Characteristic | Value                        |
    +================+==============================+
    | Datatype       | :py:data:`BoolEnableDisable` |
    +----------------+------------------------------+
    | Permissions    | read-write                   |
    +----------------+------------------------------+
    | Channel Based  | False                        |
    +----------------+------------------------------+
    | Resettable     | No                           |
    +----------------+------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Peer-to-Peer:Manual:Manual Configuration Enabled**
            - C Attribute: **NISCOPE_ATTR_P2P_MANUAL_CONFIGURATION_ENABLED**

.. py:attribute:: p2p_most_samples_avail_in_endpoint

    Returns the most number of samples available to stream from a
    peer-to-peer endpoint since the last time this property was read. This
    property is endpoint-based.



    .. note:: This property can be used only with high-speed digitizers that support
        peer-to-peer streaming.

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

            - LabVIEW Property: **Peer-to-Peer:Most Samples Available in Endpoint**
            - C Attribute: **NISCOPE_ATTR_P2P_MOST_SAMPLES_AVAIL_IN_ENDPOINT**

.. py:attribute:: p2p_notify_message_push_addr

    Specifies the address to push the `Message Push
    Value <pniScope_P2PMessagePushValue.html>`__ to on the event specified
    by the `Push Message On <pniScope_P2PPushMessageOn.html>`__ property.
    This property is endpoint-based.



    .. note:: This property can be used only with high-speed digitizers that support
        peer-to-peer streaming.

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

            - LabVIEW Property: **Peer-to-Peer:Manual:Notification:Message Push Address**
            - C Attribute: **NISCOPE_ATTR_P2P_NOTIFY_MESSAGE_PUSH_ADDR**

.. py:attribute:: p2p_notify_message_push_addr_type

    Specifies the type of the `Message Push
    Address <pniScope_P2PMessagePushAddress.html>`__ property. This property
    is endpoint-based.



    .. note:: This property can be used only with high-speed digitizers that support
        peer-to-peer streaming.

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | :py:data:`AddressType` |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | False                  |
    +----------------+------------------------+
    | Resettable     | No                     |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Peer-to-Peer:Manual:Notification:Message Push Address Type**
            - C Attribute: **NISCOPE_ATTR_P2P_NOTIFY_MESSAGE_PUSH_ADDR_TYPE**

.. py:attribute:: p2p_notify_message_push_value

    Specifies the value to be pushed to the `Message Push
    Address <pniScope_P2PMessagePushAddress.html>`__ property on the event
    specified in the `Push Message On <pniScope_P2PPushMessageOn.html>`__
    property. This property is endpoint-based.



    .. note:: This property can be used only with high-speed digitizers that support
        peer-to-peer streaming.

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

            - LabVIEW Property: **Peer-to-Peer:Manual:Notification:Message Push Value**
            - C Attribute: **NISCOPE_ATTR_P2P_NOTIFY_MESSAGE_PUSH_VALUE**

.. py:attribute:: p2p_notify_push_message_on

    Specifies the event to push the `Message Push
    Value <pniScope_P2PMessagePushValue.html>`__ property to the `Message
    Push Address <pniScope_P2PMessagePushAddress.html>`__ property.
    Specifying Done will push the message when the acquisition has
    completed. This property is endpoint-based.



    .. note:: This property can be used only with high-speed digitizers that support
        peer-to-peer streaming.

    The following table lists the characteristics of this property.

    +----------------+-----------------------------+
    | Characteristic | Value                       |
    +================+=============================+
    | Datatype       | :py:data:`NotificationType` |
    +----------------+-----------------------------+
    | Permissions    | read-write                  |
    +----------------+-----------------------------+
    | Channel Based  | False                       |
    +----------------+-----------------------------+
    | Resettable     | No                          |
    +----------------+-----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Peer-to-Peer:Manual:Notification:Push Message On**
            - C Attribute: **NISCOPE_ATTR_P2P_NOTIFY_PUSH_MESSAGE_ON**

.. py:attribute:: p2p_onboard_memory_enabled

    Specifies whether the digitizer writes data to onboard memory when a
    peer-to-peer endpoint is enabled.



    .. note:: This property is not supported on NI 5160/5162 digitizers.

    The following table lists the characteristics of this property.

    +----------------+------------------------------+
    | Characteristic | Value                        |
    +================+==============================+
    | Datatype       | :py:data:`BoolEnableDisable` |
    +----------------+------------------------------+
    | Permissions    | read-write                   |
    +----------------+------------------------------+
    | Channel Based  | False                        |
    +----------------+------------------------------+
    | Resettable     | No                           |
    +----------------+------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Peer-to-Peer:Onboard Memory Enabled**
            - C Attribute: **NISCOPE_ATTR_P2P_ONBOARD_MEMORY_ENABLED**

.. py:attribute:: p2p_samples_avail_in_endpoint

    Returns the current number of samples available to stream from a
    peer-to-peer endpoint. This property is endpoint-based.



    .. note:: This property can be used only with high-speed digitizers that support
        peer-to-peer streaming.

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

            - LabVIEW Property: **Peer-to-Peer:Samples Available In Endpoint**
            - C Attribute: **NISCOPE_ATTR_P2P_SAMPLES_AVAIL_IN_ENDPOINT**

.. py:attribute:: p2p_samples_transferred

    Returns the number of samples transferred through the peer-to-peer
    endpoint since the endpoint was last reset. This property is
    endpoint-based.



    .. note:: This property can be used only with high-speed digitizers that support
        peer-to-peer streaming.

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

            - LabVIEW Property: **Peer-to-Peer:Samples Transferred**
            - C Attribute: **NISCOPE_ATTR_P2P_SAMPLES_TRANSFERRED**

.. py:attribute:: p2p_samples_transferred_per_record

    Returns the number of samples transferred per record when you set the
    `Stream Relative To <pniScope_P2PStreamRelativeTo.html>`__ property to
    **Reference Trigger** or **Sync Trigger**.



    .. note:: This property is only supported on NI 5160/5162 digitizers.

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

            - LabVIEW Property: **Peer-to-Peer:Samples Transferred Per Record**
            - C Attribute: **NISCOPE_ATTR_P2P_SAMPLES_TRANSFERRED_PER_RECORD**

.. py:attribute:: p2p_stream_relative_to

    Determines which trigger peer-to-peer data is streamed relative to. The
    default value is **Start Trigger**.



    .. note:: On the NI 5122/5622, only **Start Trigger** is valid for this property.

    The following table lists the characteristics of this property.

    +----------------+----------------------------------+
    | Characteristic | Value                            |
    +================+==================================+
    | Datatype       | :py:data:`StreamingPositionType` |
    +----------------+----------------------------------+
    | Permissions    | read-write                       |
    +----------------+----------------------------------+
    | Channel Based  | False                            |
    +----------------+----------------------------------+
    | Resettable     | No                               |
    +----------------+----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Peer-to-Peer:Stream Relative To**
            - C Attribute: **NISCOPE_ATTR_P2P_STREAM_RELATIVE_TO**

.. py:attribute:: pll_lock_status

    If TRUE, the PLL has remained locked to the external reference clock
    since it was last checked. If FALSE, the PLL has become unlocked from
    the external reference clock since it was last checked.

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

            - LabVIEW Property: **Clocking:PLL Lock Status**
            - C Attribute: **NISCOPE_ATTR_PLL_LOCK_STATUS**

.. py:attribute:: points_done

    Actual number of samples acquired since the last fetch, relative to the
    configured value for `Fetch Relative
    To <pniScope_FetchRelativeTo.html>`__, including `Fetch
    Offset <pniScope_FetchOffset.html>`__, and for the current configured
    `Fetch Record Number <pniScope_FetchRecordNumber.html>`__.

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

            - LabVIEW Property: **Fetch:Points Done**
            - C Attribute: **NISCOPE_ATTR_POINTS_DONE**

.. py:attribute:: probe_attenuation

    Specifies the probe attenuation for the input channel. For example, for
    a 10:1 probe, you would set this property to 10.0.

    **Related topics:**

    `Probes and Their Effects <digitizers.chm::/Probes.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        probe_attenuation.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        probe_attenuation.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].probe_attenuation = var
            var = session['0,1'].probe_attenuation

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Vertical:Probe Attenuation**
            - C Attribute: **NISCOPE_ATTR_PROBE_ATTENUATION**

.. py:attribute:: prog._fir_filter_decimation

    Specifies the programmable FIR filter decimation. The default value is
    1.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        prog._fir_filter_decimation.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        prog._fir_filter_decimation.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].prog._fir_filter_decimation = var
            var = session['0,1'].prog._fir_filter_decimation

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Programmable FIR Filter:Decimation**
            - C Attribute: **NISCOPE_ATTR_PROG._FIR_FILTER_DECIMATION**

.. py:attribute:: prog._fir_filter_realcomplex

    Sets either a Complex filter or a dual Real filter. The default value is
    Real.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        prog._fir_filter_realcomplex.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        prog._fir_filter_realcomplex.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].prog._fir_filter_realcomplex = var
            var = session['0,1'].prog._fir_filter_realcomplex

    The following table lists the characteristics of this property.

    +----------------+---------------------------------------+
    | Characteristic | Value                                 |
    +================+=======================================+
    | Datatype       | :py:data:`Prog.FIRFilterReal/Complex` |
    +----------------+---------------------------------------+
    | Permissions    | read-write                            |
    +----------------+---------------------------------------+
    | Channel Based  | True                                  |
    +----------------+---------------------------------------+
    | Resettable     | No                                    |
    +----------------+---------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Programmable FIR Filter:Real/Complex**
            - C Attribute: **NISCOPE_ATTR_PROG._FIR_FILTER_REALCOMPLEX**

.. py:attribute:: prog._fir_filter_symmetry

    Sets either a Symmetric or Asymmetric filter. The default value is
    Symmetric.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        prog._fir_filter_symmetry.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        prog._fir_filter_symmetry.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].prog._fir_filter_symmetry = var
            var = session['0,1'].prog._fir_filter_symmetry

    The following table lists the characteristics of this property.

    +----------------+-----------------------------------+
    | Characteristic | Value                             |
    +================+===================================+
    | Datatype       | :py:data:`Prog.FIRFilterSymmetry` |
    +----------------+-----------------------------------+
    | Permissions    | read-write                        |
    +----------------+-----------------------------------+
    | Channel Based  | True                              |
    +----------------+-----------------------------------+
    | Resettable     | No                                |
    +----------------+-----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Programmable FIR Filter:Symmetry**
            - C Attribute: **NISCOPE_ATTR_PROG._FIR_FILTER_SYMMETRY**

.. py:attribute:: prog._fir_filter_symmetry_type

    Sets either even or odd symmetry. The default value is Even.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        prog._fir_filter_symmetry_type.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        prog._fir_filter_symmetry_type.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].prog._fir_filter_symmetry_type = var
            var = session['0,1'].prog._fir_filter_symmetry_type

    The following table lists the characteristics of this property.

    +----------------+---------------------------------------+
    | Characteristic | Value                                 |
    +================+=======================================+
    | Datatype       | :py:data:`Prog.FIRFilterSymmetryType` |
    +----------------+---------------------------------------+
    | Permissions    | read-write                            |
    +----------------+---------------------------------------+
    | Channel Based  | True                                  |
    +----------------+---------------------------------------+
    | Resettable     | No                                    |
    +----------------+---------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Programmable FIR Filter:Symmetry Type**
            - C Attribute: **NISCOPE_ATTR_PROG._FIR_FILTER_SYMMETRY_TYPE**

.. py:attribute:: prog._fir_filter_taps

    Defines the number of taps (in other words, coefficients) for a FIR
    filter. The default value is 25.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        prog._fir_filter_taps.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        prog._fir_filter_taps.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].prog._fir_filter_taps = var
            var = session['0,1'].prog._fir_filter_taps

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Programmable FIR Filter:Taps**
            - C Attribute: **NISCOPE_ATTR_PROG._FIR_FILTER_TAPS**

.. py:attribute:: query_instrument_status

    Specifies whether the instrument driver queries the instrument status
    after each operation. Querying the instrument status is very useful for
    debugging. After you validate your program, you can set this property to
    FALSE to disable status checking and maximize performance. The
    instrument driver can choose to ignore status checking for particular
    properties regardless of the setting of this property. The default value
    is TRUE. Use `niScope Initialize with
    Options <scopeviref.chm::/niScope_Initialize_With_Options.html>`__ to
    override this value.

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

            - LabVIEW Property: **Inherent IVI Attributes:User Options:Query Instrument Status**
            - C Attribute: **NISCOPE_ATTR_QUERY_INSTRUMENT_STATUS**

.. py:attribute:: q_input_to_coord._converter

    Either enables or zeros out the Q input to coordinate converter. The
    default value is I and Q.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        q_input_to_coord._converter.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        q_input_to_coord._converter.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].q_input_to_coord._converter = var
            var = session['0,1'].q_input_to_coord._converter

    The following table lists the characteristics of this property.

    +----------------+------------------------------------+
    | Characteristic | Value                              |
    +================+====================================+
    | Datatype       | :py:data:`QInputtoCoord.Converter` |
    +----------------+------------------------------------+
    | Permissions    | read-write                         |
    +----------------+------------------------------------+
    | Channel Based  | True                               |
    +----------------+------------------------------------+
    | Resettable     | No                                 |
    +----------------+------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Q Input to Coord. Converter**
            - C Attribute: **NISCOPE_ATTR_Q_INPUT_TO_COORD._CONVERTER**

.. py:attribute:: range_check

    Specifies whether to validate property values and function parameters.
    If enabled, the instrument driver validates the parameter values that
    you pass to driver functions. Range checking parameters is very useful
    for debugging. After you validate your program, you can set this
    property to FALSE to disable range checking and maximize performance.
    The default value is TRUE. Use `niScope Initialize with
    Options <scopeviref.chm::/niScope_Initialize_With_Options.html>`__ to
    override this value.

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

            - LabVIEW Property: **Inherent IVI Attributes:User Options:Range Check**
            - C Attribute: **NISCOPE_ATTR_RANGE_CHECK**

.. py:attribute:: ready_for_advance_event_output_terminal

    Specifies the destination for the advance trigger. When the advance
    trigger is received, the digitizer begins acquiring pretrigger samples.

    **Defined Values**

    VAL\_RTSI\_0

    VAL\_RTSI\_1

    VAL\_RTSI\_2

    VAL\_RTSI\_3

    VAL\_RTSI\_4

    VAL\_RTSI\_5

    VAL\_RTSI\_6

    VAL\_PFI\_0

    VAL\_PFI\_1

    VAL\_PFI\_2

    VAL\_PXI\_STAR

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

            - LabVIEW Property: **Synchronization:Ready for Advance:Output Terminal**
            - C Attribute: **NISCOPE_ATTR_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL**

.. py:attribute:: ready_for_ref_event_output_terminal

    Specifies the destination for the Ready for Reference Event. When this
    event is asserted, the digitizer is ready to receive a reference
    trigger. Refer to the device-specific documentation in the *NI
    High-Speed Digitizers Help* for a list of valid destinations for your
    device.

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

            - LabVIEW Property: **Synchronization:Ready for Reference:Output Terminal**
            - C Attribute: **NISCOPE_ATTR_READY_FOR_REF_EVENT_OUTPUT_TERMINAL**

.. py:attribute:: ready_for_start_event_output_terminal

    Specifies the destination to export the Start trigger. When the start
    trigger is received, the digitizer begins acquiring data. Refer to the
    device specifications document for a list of valid destinations.

    **Defined Values**

    VAL\_RTSI\_0

    VAL\_RTSI\_1

    VAL\_RTSI\_2

    VAL\_RTSI\_3

    VAL\_RTSI\_4

    VAL\_RTSI\_5

    VAL\_RTSI\_6

    VAL\_PFI\_0

    VAL\_PFI\_1

    VAL\_PFI\_2

    VAL\_PXI\_STAR

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

            - LabVIEW Property: **Synchronization:Ready for Start:Output Terminal**
            - C Attribute: **NISCOPE_ATTR_READY_FOR_START_EVENT_OUTPUT_TERMINAL**

.. py:attribute:: records_done

    Returns the number of records your digitizer has acquired.

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

            - LabVIEW Property: **Fetch:Records Done**
            - C Attribute: **NISCOPE_ATTR_RECORDS_DONE**

.. py:attribute:: record_arm_source

    Specifies the source for the record arm. This property is only
    applicable to Traditional NI-DAQ (Legacy) devices. For SMC-based or USB
    devices, use the Synchronization:Advance Trigger:Source Property.

    **Defined Values**

    VAL\_IMMEDIATE

    VAL\_RTSI\_0

    VAL\_RTSI\_1

    VAL\_RTSI\_2

    VAL\_RTSI\_3

    VAL\_RTSI\_4

    VAL\_RTSI\_5

    VAL\_RTSI\_6

    VAL\_PFI\_0

    VAL\_PFI\_1

    VAL\_PFI\_2

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

            - LabVIEW Property: **Synchronization:Record Arm Source**
            - C Attribute: **NISCOPE_ATTR_RECORD_ARM_SOURCE**

.. py:attribute:: record_coercions

    Specifies whether the IVI engine keeps a list of the value coercions it
    makes for ViInt32 and DBL properties. The default value is FALSE. Use
    `niScope Initialize with
    Options <scopeviref.chm::/niScope_Initialize_With_Options.html>`__ to
    override this value.

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

            - LabVIEW Property: **Inherent IVI Attributes:User Options:Record Value Coercions**
            - C Attribute: **NISCOPE_ATTR_RECORD_COERCIONS**

.. py:attribute:: ref_clk_rate

    If `Reference Clock Source <pniScope_ReferenceClockSource.html>`__ is an
    external source, specifies the frequency (in hertz) of the input clock
    (reference clock) to which the internal sample clock timebase is
    synchronized.

    **Related topics:**

    `Reference Clock/Phase-Lock
    Loop <digitizers.chm::/Reference_Clock.html>`__



    .. note:: Refer to `Features Supported by
        Device <Digitizers.chm::/Features_Supported_Main.html>`__ for valid
        values.

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

            - LabVIEW Property: **Clocking:Reference Clock Rate**
            - C Attribute: **NISCOPE_ATTR_REF_CLK_RATE**

.. py:attribute:: ref_trigger_detector_location

    Specifies which reference trigger detection circuitry to use on the
    device.



    .. note:: This property can be used only with high-speed digitizers that support
        onboard signal processing (OSP). NI-SCOPE returns an error if you use
        this property with a device that does not support OSP.

    The following table lists the characteristics of this property.

    +----------------+---------------------------------------+
    | Characteristic | Value                                 |
    +================+=======================================+
    | Datatype       | :py:data:`RefTriggerDetectorLocation` |
    +----------------+---------------------------------------+
    | Permissions    | read-write                            |
    +----------------+---------------------------------------+
    | Channel Based  | False                                 |
    +----------------+---------------------------------------+
    | Resettable     | No                                    |
    +----------------+---------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Onboard Signal Processing:Ref Trigger Detection Location**
            - C Attribute: **NISCOPE_ATTR_REF_TRIGGER_DETECTOR_LOCATION**

.. py:attribute:: ref_trigger_minimum_quiet_time

    Specifies the amount of time (in seconds) the trigger circuit must not
    detect a signal above the `trigger level <pniScope_TriggerLevel.html>`__
    (or below the trigger level if the trigger slope is negative) before the
    trigger is armed. This property is useful for triggering at the
    beginning of signal bursts instead of in the middle of signal bursts.
    The default value is 0.

    **Valid Values**

    Any value greater than or equal to 0.



    .. note:: This property can be used only with high-speed digitizers that support
        onboard signal processing (OSP). NI-SCOPE returns an error if you use
        this property with a device that does not support OSP.

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

            - LabVIEW Property: **Triggering:Onboard Signal Processing:Ref Trigger Min Quiet Time**
            - C Attribute: **NISCOPE_ATTR_REF_TRIGGER_MINIMUM_QUIET_TIME**

.. py:attribute:: ref_trig_tdc_enable

    Specifies that the digitizer should record the trigger position
    precisely using time-digital conversion (TDC).

    **Related topics:**

    `TDC <digitizers.chm::/TDC.html>`__

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

            - LabVIEW Property: **Horizontal:Advanced:Enable TDC**
            - C Attribute: **NISCOPE_ATTR_REF_TRIG_TDC_ENABLE**

.. py:attribute:: resampler_bypass

    Either enables or bypasses the resampler filter in the DDC. The
    resampler is a polyphase filter that allows the output sample rate to
    have a non-integer relationship to the input sample rate. In essence, it
    acts as a fixed interpolation filter followed by an NCO controlled
    decimator. The default value is TRUE.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        resampler_bypass.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        resampler_bypass.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].resampler_bypass = var
            var = session['0,1'].resampler_bypass

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Resampler:Bypass**
            - C Attribute: **NISCOPE_ATTR_RESAMPLER_BYPASS**

.. py:attribute:: resampler_filter_mode

    Selects the resampling filter mode.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        resampler_filter_mode.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        resampler_filter_mode.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].resampler_filter_mode = var
            var = session['0,1'].resampler_filter_mode

    The following table lists the characteristics of this property.

    +----------------+--------------------------------+
    | Characteristic | Value                          |
    +================+================================+
    | Datatype       | :py:data:`ResamplerFilterMode` |
    +----------------+--------------------------------+
    | Permissions    | read-write                     |
    +----------------+--------------------------------+
    | Channel Based  | True                           |
    +----------------+--------------------------------+
    | Resettable     | No                             |
    +----------------+--------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Resampler:Filter Mode**
            - C Attribute: **NISCOPE_ATTR_RESAMPLER_FILTER_MODE**

.. py:attribute:: resampler_nco_divide

    Divides down the
    `resampler <Digitizers.chm::/Glossary.html#resampler>`__ NCO output by
    the value loaded into the register plus one. The default value is 2.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        resampler_nco_divide.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        resampler_nco_divide.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].resampler_nco_divide = var
            var = session['0,1'].resampler_nco_divide

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Resampler:NCO Divide**
            - C Attribute: **NISCOPE_ATTR_RESAMPLER_NCO_DIVIDE**

.. py:attribute:: resampler_output_pulse_delay

    Programs the delay between output samples when interpolating. These
    outputs can be delayed from 2 to 255 clocks. The default value is 16.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        resampler_output_pulse_delay.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        resampler_output_pulse_delay.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].resampler_output_pulse_delay = var
            var = session['0,1'].resampler_output_pulse_delay

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Resampler:Output Pulse Delay**
            - C Attribute: **NISCOPE_ATTR_RESAMPLER_OUTPUT_PULSE_DELAY**

.. py:attribute:: resampler_reference_divide

    Divides down the reference clock by the value loaded into the register
    plus one. Load with a value that is one less than the desired period.
    The default value is 2.

    **Related topics:**

    `Reference Clock/Phase-Lock
    Loop <digitizers.chm::/Reference_Clock.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        resampler_reference_divide.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        resampler_reference_divide.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].resampler_reference_divide = var
            var = session['0,1'].resampler_reference_divide

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Resampler:Reference Divide**
            - C Attribute: **NISCOPE_ATTR_RESAMPLER_REFERENCE_DIVIDE**

.. py:attribute:: resolution

    Indicates the actual resolution in bits of valid data (as opposed to
    padding bits) in the acquired waveform. Compare to the `Binary Sample
    Width <pniScope_BinarySampleWidth.html>`__ property.

    Valid Values: 8 to 32

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

            - LabVIEW Property: **Acquisition:Resolution**
            - C Attribute: **NISCOPE_ATTR_RESOLUTION**

.. py:attribute:: ris_in_auto_setup_enable

    Indicates whether the digitizer should use RIS sample rates when
    searching for a frequency in autosetup.

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

            - LabVIEW Property: **Acquisition:Advanced:Enable RIS in Auto Setup**
            - C Attribute: **NISCOPE_ATTR_RIS_IN_AUTO_SETUP_ENABLE**

.. py:attribute:: ris_method

    Specifies the algorithm for random-interleaved sampling, which is used
    if the sample rate exceeds the `Max Realtime Sample
    Rate <pniScope_MaximumRealtimeSampleRate.html>`__.

    The following table lists the characteristics of this property.

    +----------------+----------------------+
    | Characteristic | Value                |
    +================+======================+
    | Datatype       | :py:data:`RISMethod` |
    +----------------+----------------------+
    | Permissions    | read-write           |
    +----------------+----------------------+
    | Channel Based  | False                |
    +----------------+----------------------+
    | Resettable     | No                   |
    +----------------+----------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Horizontal:RIS Method**
            - C Attribute: **NISCOPE_ATTR_RIS_METHOD**

.. py:attribute:: ris_num_averages

    Specifies the number of averages in each RIS bin.

    Averaging is useful in RIS because the trigger times are not evenly
    spaced, so adjacent points in the reconstructed waveform cannot be
    accurately spaced. By averaging, the errors in both time and voltage are
    smoothed, minimizing the noise in the reconstructed waveform.

    Valid Values: Greater than or equal to 0

    **Related topics:**

    `Sampling Methods <digitizers.chm::/Sampling_Methods.html>`__
    `Equivalent-Time Sampling and Random Interleaved
    Sampling <digitizers.chm::/ris.html>`__

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

            - LabVIEW Property: **Horizontal:RIS Num Avg**
            - C Attribute: **NISCOPE_ATTR_RIS_NUM_AVERAGES**

.. py:attribute:: sample_mode

    Returns the sample mode the digitizer is currently using.

    **Defined Values**

    Real Time (0)

    Equivalent Time (1)

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

            - LabVIEW Property: **Acquisition:Sample Mode**
            - C Attribute: **NISCOPE_ATTR_SAMPLE_MODE**

.. py:attribute:: samp_clk_timebase_div

    If `Sample Clock Timebase
    Source <pniScope_SampleClockTimebaseSource.html>`__ is an external
    source, specifies the ratio between the sample clock timebase rate and
    the actual sample rate, which can be slower.

    **Related topics:**

    `Sample Clock <digitizers.chm::/Sample_Clock.html>`__

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

            - LabVIEW Property: **Clocking:Sample Clock Timebase Divisor**
            - C Attribute: **NISCOPE_ATTR_SAMP_CLK_TIMEBASE_DIV**

.. py:attribute:: samp_clk_timebase_mult

    If `Sample Clock Timebase
    Source <pniScope_SampleClockTimebaseSource.html>`__ is an external
    source, this property specifies the ratio between the `Sample Clock
    Timebase Rate <pniScope_SampleClockTimebaseRate.html>`__ and the actual
    sample rate, which can be higher. This property can be used in
    conjunction with the `Sample Clock Timebase Divisor
    Property <pniscope_SampleClockTimebaseDivisor.html>`__.

    Some devices use multiple ADCs to sample the same channel at an
    effective sample rate that is greater than the specified clock rate.
    When providing an external sample clock use this property to indicate
    when you want a higher sample rate. Valid values for this property vary
    by device and current configuration.

    **Related topics:**

    `Sample Clock <digitizers.chm::/Sample_Clock.html>`__

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

            - LabVIEW Property: **Clocking:Sample Clock Timebase Multiplier**
            - C Attribute: **NISCOPE_ATTR_SAMP_CLK_TIMEBASE_MULT**

.. py:attribute:: samp_clk_timebase_rate

    Specifies the frequency in hertz of the external clock used as the
    timebase source if the `Sample Clock Timebase
    Source <pniScope_SampleClockTimebaseSource.html>`__ is an external
    source.

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

            - LabVIEW Property: **Clocking:Sample Clock Timebase Rate**
            - C Attribute: **NISCOPE_ATTR_SAMP_CLK_TIMEBASE_RATE**

.. py:attribute:: samp_clk_timebase_src

    Specifies the source of the sample clock timebase, which is the timebase
    used to control waveform sampling.

    The actual sample rate may be the timebase itself or a scaled version of
    the timebase, depending on the `Min Sample
    Rate <pniScope_MinSampleRate.html>`__ property (for internal sources) or
    the `Sample Clock Timebase
    Divisor <pniScope_SampleClockTimebaseDivisor.html>`__ and `Sample Clock
    Timebase Multiplier <pniScope_SampleClockTimebaseMultiplier.html>`__
    properties (for external sources).

    **Defined Values**

    VAL\_CLK\_IN

    VAL\_PXI\_STAR

    VAL\_PFI\_0

    VAL\_PFI\_1

    VAL\_NO\_SOURCE

    **Related topics:**

    `Sample Clock <digitizers.chm::/Sample_Clock.html>`__

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

            - LabVIEW Property: **Clocking:Sample Clock Timebase Source**
            - C Attribute: **NISCOPE_ATTR_SAMP_CLK_TIMEBASE_SRC**

.. py:attribute:: serial_dac_cal_voltage

    

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

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Serial DAC Cal Voltage**
            - C Attribute: **NISCOPE_ATTR_SERIAL_DAC_CAL_VOLTAGE**

.. py:attribute:: serial_number

    Returns the serial number of the device.

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

            - LabVIEW Property: **Device:Serial Number**
            - C Attribute: **NISCOPE_ATTR_SERIAL_NUMBER**

.. py:attribute:: signal_cond_gain

    Returns the calibration gain for the current device configuration.

    **Related topics:**

    `NI 5122/5124/5142
    Calibration <digitizers.chm::/5122_Calibration.html>`__



    .. note:: This property is only supported by the NI PXI-5900 differential
        amplifier.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        signal_cond_gain.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        signal_cond_gain.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].signal_cond_gain = var
            var = session['0,1'].signal_cond_gain

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | float     |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | True      |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device:Accessory:Gain**
            - C Attribute: **NISCOPE_ATTR_SIGNAL_COND_GAIN**

.. py:attribute:: signal_cond_offset

    Returns the calibration offset for the current device configuration.

    **Related topics:**

    `NI 5122/5124/5142
    Calibration <digitizers.chm::/5122_Calibration.html>`__



    .. note:: This property is supported only by the NI PXI-5900 differential
        amplifier.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        signal_cond_offset.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        signal_cond_offset.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].signal_cond_offset = var
            var = session['0,1'].signal_cond_offset

    The following table lists the characteristics of this property.

    +----------------+-----------+
    | Characteristic | Value     |
    +================+===========+
    | Datatype       | float     |
    +----------------+-----------+
    | Permissions    | read only |
    +----------------+-----------+
    | Channel Based  | True      |
    +----------------+-----------+
    | Resettable     | No        |
    +----------------+-----------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device:Accessory:Offset**
            - C Attribute: **NISCOPE_ATTR_SIGNAL_COND_OFFSET**

.. py:attribute:: simulate

    Specifies whether to simulate instrument driver I/O operations. The
    default value is FALSE. Use `niScope Initialize with
    Options <scopeviref.chm::/niScope_Initialize_With_Options.html>`__ to
    override this value.

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

            - LabVIEW Property: **Inherent IVI Attributes:User Options:Simulate**
            - C Attribute: **NISCOPE_ATTR_SIMULATE**

.. py:attribute:: slave_trigger_delay

    Specifies the delay in seconds for the trigger from the master to the
    slave.

    This value adjusts the **initial X** value of the slave digitizer to
    correct for the propagation delay between the master trigger output and
    slave trigger input.

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

            - LabVIEW Property: **Synchronization:Trigger Calibration Delay:Slave Trigger Delay**
            - C Attribute: **NISCOPE_ATTR_SLAVE_TRIGGER_DELAY**

.. py:attribute:: specific_driver_class_spec_major_version

    The major version number of the class specification with which this
    driver is compliant.

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

            - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Class Specification Major Version**
            - C Attribute: **NISCOPE_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION**

.. py:attribute:: specific_driver_class_spec_minor_version

    The minor version number of the class specification with which this
    driver is compliant.

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

            - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Class Specification Minor Version**
            - C Attribute: **NISCOPE_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION**

.. py:attribute:: specific_driver_description

    A string that contains the description of the instrument.

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

            - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Description**
            - C Attribute: **NISCOPE_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

.. py:attribute:: specific_driver_prefix

    A string that contains the prefix for the instrument driver. The name of
    each user-callable function in this driver starts with this prefix.

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

            - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Driver Prefix**
            - C Attribute: **NISCOPE_ATTR_SPECIFIC_DRIVER_PREFIX**

.. py:attribute:: specific_driver_revision

    The string that contains additional version information about this
    instrument driver.

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

            - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Revision**
            - C Attribute: **NISCOPE_ATTR_SPECIFIC_DRIVER_REVISION**

.. py:attribute:: specific_driver_vendor

    A string that contains the name of the vendor that supplies this driver,
    for example, "National Instruments".

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

            - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Driver Vendor**
            - C Attribute: **NISCOPE_ATTR_SPECIFIC_DRIVER_VENDOR**

.. py:attribute:: start_to_ref_trigger_holdoff

    Pass the length of time (in seconds) you want the digitizer to wait
    after it starts acquiring data until the digitizer enables the trigger
    system to detect a reference (stop) trigger.

    Valid Values: 0.0 - 171.8




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        start_to_ref_trigger_holdoff.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        start_to_ref_trigger_holdoff.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].start_to_ref_trigger_holdoff = var
            var = session['0,1'].start_to_ref_trigger_holdoff

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Start To Ref Trigger Holdoff**
            - C Attribute: **NISCOPE_ATTR_START_TO_REF_TRIGGER_HOLDOFF**

.. py:attribute:: supported_instrument_models

    A string that contains a comma-separated list of the instrument model
    numbers supported by this driver.

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

            - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models**
            - C Attribute: **NISCOPE_ATTR_SUPPORTED_INSTRUMENT_MODELS**

.. py:attribute:: syncout_clk_select

    Source for Syncout CLK. The default value is CLK IN.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        syncout_clk_select.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        syncout_clk_select.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].syncout_clk_select = var
            var = session['0,1'].syncout_clk_select

    The following table lists the characteristics of this property.

    +----------------+-----------------------------+
    | Characteristic | Value                       |
    +================+=============================+
    | Datatype       | :py:data:`SyncoutCLKSelect` |
    +----------------+-----------------------------+
    | Permissions    | read-write                  |
    +----------------+-----------------------------+
    | Channel Based  | True                        |
    +----------------+-----------------------------+
    | Resettable     | No                          |
    +----------------+-----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Syncout CLK Select**
            - C Attribute: **NISCOPE_ATTR_SYNCOUT_CLK_SELECT**

.. py:attribute:: test_mode_sincos

    Enables the special test mode where the carrier NCO outputs are set to
    0x7FFF. The default is FALSE.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        test_mode_sincos.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        test_mode_sincos.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].test_mode_sincos = var
            var = session['0,1'].test_mode_sincos

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Test Mode Sin/Cos**
            - C Attribute: **NISCOPE_ATTR_TEST_MODE_SINCOS**

.. py:attribute:: timing_nco_center_freq.

    Controls the frequency of the timing NCO. Specifies the timing NCO
    center frequency in binary format:

    *N = (F:sub:`out` / F\ :sub:`resampler`) & 2\ :sup:`32`*

    where *F\ :sub:`out`* is the output frequency and *F\ :sub:`resampler`*
    is the resampled frequency.

    The value is transferred to the active register during the next initiate
    acquisition operation. The default value is 0X8000000.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        timing_nco_center_freq..Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        timing_nco_center_freq..Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].timing_nco_center_freq. = var
            var = session['0,1'].timing_nco_center_freq.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Timing NCO:Center Frequency**
            - C Attribute: **NISCOPE_ATTR_TIMING_NCO_CENTER_FREQ.**

.. py:attribute:: timing_nco_clear_phase_accum.

    If FALSE, enables the accumulator in the `timing
    NCO <Digitizers.chm::/Glossary.html#timingNCO>`__. If TRUE, zeros out
    feedback in the accumulator. The default value is FALSE.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        timing_nco_clear_phase_accum..Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        timing_nco_clear_phase_accum..Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].timing_nco_clear_phase_accum. = var
            var = session['0,1'].timing_nco_clear_phase_accum.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Timing NCO:Clear Phase Accum.**
            - C Attribute: **NISCOPE_ATTR_TIMING_NCO_CLEAR_PHASE_ACCUM.**

.. py:attribute:: timing_nco_enable_offset_freq.

    If TRUE, enables offset frequency in the `timing
    NCO <Digitizers.chm::/Glossary.html#timingNCO>`__. If FALSE, applies no
    offset frequency. The default value is FALSE.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        timing_nco_enable_offset_freq..Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        timing_nco_enable_offset_freq..Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].timing_nco_enable_offset_freq. = var
            var = session['0,1'].timing_nco_enable_offset_freq.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Timing NCO:Enable Offset Freq.**
            - C Attribute: **NISCOPE_ATTR_TIMING_NCO_ENABLE_OFFSET_FREQ.**

.. py:attribute:: timing_nco_freq._offset_bits

    Specifies the number of offset bits in the `timing
    NCO <Digitizers.chm::/Glossary.html#timingNCO>`__. The default value is
    8 bits.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        timing_nco_freq._offset_bits.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        timing_nco_freq._offset_bits.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].timing_nco_freq._offset_bits = var
            var = session['0,1'].timing_nco_freq._offset_bits

    The following table lists the characteristics of this property.

    +----------------+-------------------------------------+
    | Characteristic | Value                               |
    +================+=====================================+
    | Datatype       | :py:data:`TimingNCOFreq.OffsetBits` |
    +----------------+-------------------------------------+
    | Permissions    | read-write                          |
    +----------------+-------------------------------------+
    | Channel Based  | True                                |
    +----------------+-------------------------------------+
    | Resettable     | No                                  |
    +----------------+-------------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Timing NCO:Frequency Offset Bits**
            - C Attribute: **NISCOPE_ATTR_TIMING_NCO_FREQ._OFFSET_BITS**

.. py:attribute:: timing_nco_phase_accum._load_on_update

    When TRUE, updates the `timing
    NCO <Digitizers.chm::/Glossary.html#timingNCO>`__ frequency to zero the
    feedback of the phase accumulator as well as update the phase and
    frequency. The default value is TRUE.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        timing_nco_phase_accum._load_on_update.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        timing_nco_phase_accum._load_on_update.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].timing_nco_phase_accum._load_on_update = var
            var = session['0,1'].timing_nco_phase_accum._load_on_update

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | bool       |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Timing NCO:Phase Accum. Load on Update**
            - C Attribute: **NISCOPE_ATTR_TIMING_NCO_PHASE_ACCUM._LOAD_ON_UPDATE**

.. py:attribute:: timing_nco_phase_offset

    Offsets the phase of the `timing
    NCO <Digitizers.chm::/Glossary.html#timingNCO>`__ in binary format. The
    value is transferred to the active register during the next initiate
    acquisition. The default value is 0.

    Valid Range: 0 to 6.283185307179586476925286766558




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        timing_nco_phase_offset.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        timing_nco_phase_offset.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].timing_nco_phase_offset = var
            var = session['0,1'].timing_nco_phase_offset

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Device Specific:IF Digitizer (5620 and 5621):Advanced:Timing NCO:Phase Offset**
            - C Attribute: **NISCOPE_ATTR_TIMING_NCO_PHASE_OFFSET**

.. py:attribute:: trigger_auto_triggered

    Specifies whether the acquisition was triggered automatically. Auto
    triggering occurs if the Trigger Modifier property is set to Auto
    Trigger and no trigger has been received for a certain amount of time.

    **Related topics:**

    `Trigger Types <digitizers.chm::/Trigger_Types.html>`__

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

            - LabVIEW Property: **Triggering:Auto Triggered**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_AUTO_TRIGGERED**

.. py:attribute:: trigger_coupling

    Specifies how the digitizer couples the trigger source.

    This property affects instrument operation only when the `Trigger
    Type <pniScope_TriggerType.html>`__ property is set to Edge, Hysteresis,
    Window, or Video. If the trigger source is an input channel, the
    coupling of that channel is used for the trigger.

    The following table lists the characteristics of this property.

    +----------------+----------------------------+
    | Characteristic | Value                      |
    +================+============================+
    | Datatype       | :py:data:`TriggerCoupling` |
    +----------------+----------------------------+
    | Permissions    | read-write                 |
    +----------------+----------------------------+
    | Channel Based  | False                      |
    +----------------+----------------------------+
    | Resettable     | No                         |
    +----------------+----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Trigger Coupling**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_COUPLING**

.. py:attribute:: trigger_delay_time

    Specifies the trigger delay time in seconds.

    The trigger delay time is the length of time the digitizer waits after
    it receives the trigger. The event that occurs when the trigger delay
    elapses is the Reference Event.

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

            - LabVIEW Property: **Triggering:Trigger Delay**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_DELAY_TIME**

.. py:attribute:: trigger_from_pfi_delay

    A factory-programmed value that specifies the delay in seconds for the
    PFI lines to the trigger input. By itself, this property has no effect
    on the acquired data.

    Depending on how the trigger lines are routed between the master and
    slave digitizers, you can use this value as a starting point to set the
    `Slave Trigger Delay <pniScope_SlaveTriggerDelay.html>`__ property.

    **Related topics:**

    `PFI Lines <digitizers.chm::/PFI_Lines.html>`__

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

            - LabVIEW Property: **Synchronization:Trigger Calibration Delay:Trigger from PFI Delay**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_FROM_PFI_DELAY**

.. py:attribute:: trigger_from_rtsi_delay

    A factory-programmed value that specifies the delay in seconds for the
    RTSI bus to the trigger input. By itself, this property has no effect on
    the acquired data.

    Depending on how the trigger lines are routed between the master and
    slave digitizers, you can use this value as a starting point to set the
    `Slave Trigger Delay <pniScope_SlaveTriggerDelay.html>`__ property.

    **Related topics:**

    `PXI Trigger Lines <digitizers.chm::/PXI_Trigger_Lines.html>`__

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

            - LabVIEW Property: **Synchronization:Trigger Calibration Delay:Trigger from RTSI Delay**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_FROM_RTSI_DELAY**

.. py:attribute:: trigger_from_star_delay

    A factory-programmed value that specifies the delay in seconds for PXI
    Star Trigger line to the trigger input. By itself, this property has no
    effect on the acquired data.

    Depending on how the trigger lines are routed between the master and
    slave digitizers, you can use this value as a starting point to set the
    `Slave Trigger Delay <pniScope_SlaveTriggerDelay.html>`__ property.

    **Related topics:**

    `PXI Star Trigger Line <digitizers.chm::/PXI_Star_Trigger_Line.html>`__

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

            - LabVIEW Property: **Synchronization:Trigger Calibration Delay:Trigger from Star Delay**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_FROM_STAR_DELAY**

.. py:attribute:: trigger_holdoff

    Specifies the length of time the digitizer waits after detecting a
    trigger before enabling the trigger subsystem to detect another trigger.
    The units are seconds.

    This property affects instrument operation only when the digitizer
    requires multiple acquisitions to build a complete waveform. The
    digitizer requires multiple waveform acquisitions when it uses
    equivalent-time sampling or when the digitizer is configured for a
    multirecord acquisition through a call to `niScope Configure Horizontal
    Timing <scopeviref.chm::/niScope_Configure_Horizontal_Timing.html>`__.

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

            - LabVIEW Property: **Triggering:Trigger Holdoff**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_HOLDOFF**

.. py:attribute:: trigger_hysteresis

    Specifies the size of the hysteresis window on either side of the
    trigger level.

    The digitizer triggers when the trigger signal passes through the
    threshold you specify with the Trigger Level parameter, has the slope
    you specify with the Trigger Slope parameter, and passes through the
    hysteresis window that you specify with this parameter.

    Units: Volts

    Min Value: 0

    Max Value for positive trigger slope:

    *Hysteresis - trigger level >= -(vertical range/2) + vertical offset*

    Max value for negative trigger slope:

    *Hysteresis + trigger level <= (vertical range/2) + vertical offset*

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

            - LabVIEW Property: **Triggering:Trigger Hysteresis**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_HYSTERESIS**

.. py:attribute:: trigger_impedance

    Sets the impedance for the trigger channel (NI 5112 only).

    **Defined Values**

    1 M Ohm

    50 Ohm

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

            - LabVIEW Property: **Triggering:Trigger Impedance**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_IMPEDANCE**

.. py:attribute:: trigger_level

    Specifies the voltage threshold for the trigger. The units are volts.

    This property affects instrument behavior only when the `Trigger
    Type <pniScope_TriggerType.html>`__ is set to Edge, Hysteresis, or
    Window.

    The values of the **range** and **offset** parameters in `niScope
    Configure Vertical <scopeviref.chm::/niScope_Configure_Vertical.html>`__
    determine the valid range for the trigger level on the channel you use
    as the **trigger source**. The value you pass for this parameter must
    meet the following conditions:

    *Trigger Level <= Vertical Range/2 + Vertical Offset*

    *Trigger Level >= (-Vertical Range/2) + Vertical Offset*

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

            - LabVIEW Property: **Triggering:Trigger Level**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_LEVEL**

.. py:attribute:: trigger_modifier

    Configures the device to automatically complete an acquisition if a
    trigger has not been received.

    The following table lists the characteristics of this property.

    +----------------+----------------------------+
    | Characteristic | Value                      |
    +================+============================+
    | Datatype       | :py:data:`TriggerModifier` |
    +----------------+----------------------------+
    | Permissions    | read-write                 |
    +----------------+----------------------------+
    | Channel Based  | False                      |
    +----------------+----------------------------+
    | Resettable     | No                         |
    +----------------+----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Trigger Modifier**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_MODIFIER**

.. py:attribute:: trigger_slope

    Specifies whether a rising or a falling edge triggers the digitizer.

    This property affects instrument operation only when the `Trigger
    Type <pniScope_TriggerType.html>`__ property is set to edge, hysteresis,
    window, or video.

    The following table lists the characteristics of this property.

    +----------------+-------------------------+
    | Characteristic | Value                   |
    +================+=========================+
    | Datatype       | :py:data:`TriggerSlope` |
    +----------------+-------------------------+
    | Permissions    | read-write              |
    +----------------+-------------------------+
    | Channel Based  | False                   |
    +----------------+-------------------------+
    | Resettable     | No                      |
    +----------------+-------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Trigger Slope**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_SLOPE**

.. py:attribute:: trigger_source

    Specifies the source the digitizer monitors for the trigger event. The
    value must be selected from one of the following valid values.

    +---------------------+----------------------------------------------+
    | 0..\ *n*            | *n* is the number of channels on the device  |
    +---------------------+----------------------------------------------+
    | VAL\_EXTERNAL       | External TRIG input                          |
    +---------------------+----------------------------------------------+
    | VAL\_IMMEDIATE      | Triggers immediately                         |
    +---------------------+----------------------------------------------+
    | VAL\_RTSI\_0        | RTSI 0                                       |
    +---------------------+----------------------------------------------+
    | VAL\_RTSI\_1        | RTSI 1                                       |
    +---------------------+----------------------------------------------+
    | VAL\_RTSI\_2        | RTSI 2                                       |
    +---------------------+----------------------------------------------+
    | VAL\_RTSI\_3        | RTSI 3                                       |
    +---------------------+----------------------------------------------+
    | VAL\_RTSI\_4        | RTSI 4                                       |
    +---------------------+----------------------------------------------+
    | VAL\_RTSI\_5        | RTSI 5                                       |
    +---------------------+----------------------------------------------+
    | VAL\_RTSI\_6        | RTSI 6                                       |
    +---------------------+----------------------------------------------+
    | VAL\_PFI\_0         | PFI 0                                        |
    +---------------------+----------------------------------------------+
    | VAL\_PFI\_1         | PFI 1                                        |
    +---------------------+----------------------------------------------+
    | VAL\_PFI\_2         | PFI 2                                        |
    +---------------------+----------------------------------------------+
    | VAL\_PXI\_STAR      | PXI Star trigger                             |
    +---------------------+----------------------------------------------+
    | VAL\_SW\_TRIG\_FUNC | Waits for niScope Send Software Trigger Edge |
    +---------------------+----------------------------------------------+

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

            - LabVIEW Property: **Triggering:Trigger Source**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_SOURCE**

.. py:attribute:: trigger_to_pfi_delay

    A factory-programmed value that specifies the delay in seconds for the
    trigger to the PFI lines. By itself, this property has no effect on the
    acquired data.

    Depending on how the trigger lines are routed between the master and
    slave digitizers, you can use this value as a starting point to set the
    `Slave Trigger Delay <pniScope_SlaveTriggerDelay.html>`__ property.

    **Related topics:**

    `PFI Lines <digitizers.chm::/PFI_Lines.html>`__

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

            - LabVIEW Property: **Synchronization:Trigger Calibration Delay:Trigger to PFI Delay**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_TO_PFI_DELAY**

.. py:attribute:: trigger_to_rtsi_delay

    A factory-programmed value that specifies the delay in seconds for the
    trigger to the RTSI bus.

    By itself, this property has no effect on the acquired data. However,
    depending on how the trigger lines are routed between the master and
    slave digitizers, you can use this value as a starting point to set the
    `Slave Trigger Delay <pniScope_SlaveTriggerDelay.html>`__ property.

    **Related topics:**

    `PXI Trigger Lines <digitizers.chm::/PXI_Trigger_Lines.html>`__

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

            - LabVIEW Property: **Synchronization:Trigger Calibration Delay:Trigger to RTSI Delay**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_TO_RTSI_DELAY**

.. py:attribute:: trigger_to_star_delay

    A factory-programmed value that specifies the delay in seconds for the
    trigger to the PXI Star Trigger line.

    By itself, this property has no effect on the acquired data. However,
    depending on how the trigger lines are routed between the master and
    slave boards, you can use this value as a starting point to set the
    `Slave Trigger Delay <pniScope_SlaveTriggerDelay.html>`__ property.

    **Related topics:**

    `PXI Star Trigger Line <digitizers.chm::/PXI_Star_Trigger_Line.html>`__

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

            - LabVIEW Property: **Synchronization:Trigger Calibration Delay:Trigger to Star Delay**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_TO_STAR_DELAY**

.. py:attribute:: trigger_type

    Specifies the type of trigger to use.

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | :py:data:`TriggerType` |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | False                  |
    +----------------+------------------------+
    | Resettable     | No                     |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Trigger Type**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_TYPE**

.. py:attribute:: trigger_window_high_level

    Pass the upper voltage threshold you want the digitizer to use for
    window triggering.

    The digitizer triggers when the trigger signal enters or leaves the
    window you specify with the Trigger Window Low Level property and this
    property.

    The values of the `Vertical Range <pniScope_VerticalRange.html>`__
    property and the `Vertical Offset <pniScope_VerticalOffset.html>`__
    property determine the valid range for the Trigger Window Low Level
    property on the channel you specify with the `Trigger
    Source <pniScope_TriggerSource.html>`__ property.

    The value you pass for this parameter must meet the following
    conditions:

    *High Trigger Level <= Vertical Range/2 + Vertical Offset*

    *High Trigger Level >= (-Vertical Range/2) + Vertical Offset*

    *High Trigger Level > Low Trigger Level*

    **Related topics:**

    `Window Triggers <digitizers.chm::/Window_Triggers.html>`__

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

            - LabVIEW Property: **Triggering:Trigger Window:High Level**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_WINDOW_HIGH_LEVEL**

.. py:attribute:: trigger_window_low_level

    Pass the lower voltage threshold you want the digitizer to use for
    window triggering.

    The digitizer triggers when the trigger signal enters or leaves the
    window you specify with this property and the `Trigger Window High
    Level <pniScope_TriggerWindowHighLevel.html>`__ property.

    The values of the `Vertical Range <pniScope_VerticalRange.html>`__
    property and the `Vertical Offset <pniScope_VerticalOffset.html>`__
    property determine the valid range for this property on the channel you
    specify with the `Trigger Source <pniScope_TriggerSource.html>`__
    property.

    The value you pass for this parameter must meet the following
    conditions:

    *Low Trigger Level <= Vertical Range/2 + Vertical Offset*

    *Low Trigger Level >= (-Vertical Range/2) + Vertical Offset*

    *Low Trigger Level < High Trigger Level*

    **Related topics:**

    `Window Triggers <digitizers.chm::/Window_Triggers.html>`__

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

            - LabVIEW Property: **Triggering:Trigger Window:Low Level**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_WINDOW_LOW_LEVEL**

.. py:attribute:: trigger_window_mode

    Specifies whether to trigger when the signal enters or leaves the window
    specified by the `Trigger Window Low
    Level <pniScope_TriggerWindowLowLevel.html>`__ property or the `Trigger
    Window High Level <pniScope_TriggerWindowHighLevel.html>`__ property.

    **Related topics:**

    `Window Triggers <digitizers.chm::/Window_Triggers.html>`__ `Trigger
    Parameters <digitizers.chm::/Trigger_Parameters.html>`__

    The following table lists the characteristics of this property.

    +----------------+------------------------------+
    | Characteristic | Value                        |
    +================+==============================+
    | Datatype       | :py:data:`TriggerWindowMode` |
    +----------------+------------------------------+
    | Permissions    | read-write                   |
    +----------------+------------------------------+
    | Channel Based  | False                        |
    +----------------+------------------------------+
    | Resettable     | No                           |
    +----------------+------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Trigger Window:Window Mode**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_WINDOW_MODE**

.. py:attribute:: tv_trigger_event

    Specifies the event to trigger on.

    The following table lists the characteristics of this property.

    +----------------+------------------------------+
    | Characteristic | Value                        |
    +================+==============================+
    | Datatype       | :py:data:`VideoTriggerEvent` |
    +----------------+------------------------------+
    | Permissions    | read-write                   |
    +----------------+------------------------------+
    | Channel Based  | False                        |
    +----------------+------------------------------+
    | Resettable     | No                           |
    +----------------+------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Trigger Video:Event**
            - C Attribute: **NISCOPE_ATTR_TV_TRIGGER_EVENT**

.. py:attribute:: tv_trigger_line_number

    Specifies the line number to trigger on.

    This property is only used if the video trigger
    `Event <pniScope_VideoTriggerEvent.html>`__ property is set as Line
    Number. Valid values depend on the video signal format selected.

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

            - LabVIEW Property: **Triggering:Trigger Video:Line Number**
            - C Attribute: **NISCOPE_ATTR_TV_TRIGGER_LINE_NUMBER**

.. py:attribute:: tv_trigger_polarity

    Specifies whether the video signal is positive or negative.

    The following table lists the characteristics of this property.

    +----------------+--------------------------+
    | Characteristic | Value                    |
    +================+==========================+
    | Datatype       | :py:data:`VideoPolarity` |
    +----------------+--------------------------+
    | Permissions    | read-write               |
    +----------------+--------------------------+
    | Channel Based  | False                    |
    +----------------+--------------------------+
    | Resettable     | No                       |
    +----------------+--------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Trigger Video:Polarity**
            - C Attribute: **NISCOPE_ATTR_TV_TRIGGER_POLARITY**

.. py:attribute:: tv_trigger_signal_format

    Specifies the video signal format to use.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        tv_trigger_signal_format.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        tv_trigger_signal_format.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].tv_trigger_signal_format = var
            var = session['0,1'].tv_trigger_signal_format

    The following table lists the characteristics of this property.

    +----------------+------------------------------+
    | Characteristic | Value                        |
    +================+==============================+
    | Datatype       | :py:data:`VideoSignalFormat` |
    +----------------+------------------------------+
    | Permissions    | read-write                   |
    +----------------+------------------------------+
    | Channel Based  | True                         |
    +----------------+------------------------------+
    | Resettable     | No                           |
    +----------------+------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Trigger Video:Signal Format**
            - C Attribute: **NISCOPE_ATTR_TV_TRIGGER_SIGNAL_FORMAT**

.. py:attribute:: vertical_coupling

    Specifies how the digitizer couples the input signal for the channel.
    When you change input coupling, the input stage takes a finite amount of
    time to settle.

    **Related topics:**

    `Input Coupling <digitizers.chm::/Input_Coupling.html>`__




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        vertical_coupling.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        vertical_coupling.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].vertical_coupling = var
            var = session['0,1'].vertical_coupling

    The following table lists the characteristics of this property.

    +----------------+-----------------------------+
    | Characteristic | Value                       |
    +================+=============================+
    | Datatype       | :py:data:`VerticalCoupling` |
    +----------------+-----------------------------+
    | Permissions    | read-write                  |
    +----------------+-----------------------------+
    | Channel Based  | True                        |
    +----------------+-----------------------------+
    | Resettable     | No                          |
    +----------------+-----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Vertical:Vertical Coupling**
            - C Attribute: **NISCOPE_ATTR_VERTICAL_COUPLING**

.. py:attribute:: vertical_offset

    Specifies the location of the center of the range. The value is with
    respect to ground and is in volts. For example, to acquire a sine wave
    that spans between 0.0 and 10.0 V, set this property to 5.0 V. This
    property is not supported by all digitizers.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        vertical_offset.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        vertical_offset.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].vertical_offset = var
            var = session['0,1'].vertical_offset

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Vertical:Vertical Offset**
            - C Attribute: **NISCOPE_ATTR_VERTICAL_OFFSET**

.. py:attribute:: vertical_range

    Specifies the absolute value of the input range for a channel. The units
    are volts. For example, to acquire a sine wave that spans between -5 and
    +5 V, set this property to 10.0 V.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        vertical_range.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        vertical_range.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].vertical_range = var
            var = session['0,1'].vertical_range

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | float      |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  | True       |
    +----------------+------------+
    | Resettable     | No         |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Vertical:Vertical Range**
            - C Attribute: **NISCOPE_ATTR_VERTICAL_RANGE**


