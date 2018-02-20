niscope.Session properties
==========================

.. py:currentmodule:: niscope.Session

.. py:attribute:: _5102_adjust_pretrigger_samples

    When set to true and the digitizer is set to master, the number of pretrigger samples  and total samples are adjusted to be able to synchronize a master and slave 5102.

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

.. py:attribute:: _5v_out_output_terminal

    Specifies the destination for the 5 Volt signal.
    Consult your device documentation for a specific list of valid destinations.

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

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | datetime.timedelta |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Clocking:Advanced:Absolute Sample Clock Offset**
            - C Attribute: **NISCOPE_ATTR_ABSOLUTE_SAMPLE_CLOCK_OFFSET**

.. py:attribute:: accessory_gain

    Returns the calibration gain for the current device configuration.
    **Related topics:**
    `NI 5122/5124/5142
    Calibration <digitizers.chm::/5122_Calibration.html>`__



    .. note:: This property is only supported by the NI PXI-5900 differential
        amplifier.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        accessory_gain.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        accessory_gain.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].accessory_gain = var
            var = session['0,1'].accessory_gain

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
            - C Attribute: **NISCOPE_ATTR_ACCESSORY_GAIN**

.. py:attribute:: accessory_offset

    Returns the calibration offset for the current device configuration.
    **Related topics:**
    `NI 5122/5124/5142
    Calibration <digitizers.chm::/5122_Calibration.html>`__



    .. note:: This property is supported only by the NI PXI-5900 differential
        amplifier.


    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        accessory_offset.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        accessory_offset.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].accessory_offset = var
            var = session['0,1'].accessory_offset

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
            - C Attribute: **NISCOPE_ATTR_ACCESSORY_OFFSET**

.. py:attribute:: acquisition_start_time

    Specifies the length of time from the trigger event to the first point in  the waveform record in seconds.  If the value is positive, the first point  in the waveform record occurs after the trigger event (same as specifying  :py:data:`niscope.Session.trigger_delay_time`).  If the value is negative, the first point  in the waveform record occurs before the trigger event (same as specifying  :py:data:`niscope.Session.horz_record_ref_position`).

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
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Horizontal:Advanced:Acquisition Start Time**
            - C Attribute: **NISCOPE_ATTR_ACQUISITION_START_TIME**

.. py:attribute:: acquisition_type

    Specifies how the digitizer acquires data and fills the waveform record.

    The following table lists the characteristics of this property.

    +----------------+-----------------------+
    | Characteristic | Value                 |
    +================+=======================+
    | Datatype       | enums.AcquisitionType |
    +----------------+-----------------------+
    | Permissions    | read-write            |
    +----------------+-----------------------+
    | Channel Based  | False                 |
    +----------------+-----------------------+
    | Resettable     | No                    |
    +----------------+-----------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Acquisition:Acquisition Type**
            - C Attribute: **NISCOPE_ATTR_ACQUISITION_TYPE**

.. py:attribute:: acq_arm_source

    Specifies the source the digitizer monitors for a start (acquisition arm) trigger.   When the start trigger is received, the digitizer begins acquiring pretrigger  samples.
    Valid Values:
    :py:data:`~niscope.NISCOPE_VAL_IMMEDIATE`     ('VAL_IMMEDIATE')    - Triggers immediately
    :py:data:`~niscope.NISCOPE_VAL_RTSI_0`        ('VAL_RTSI_0')       - RTSI 0
    :py:data:`~niscope.NISCOPE_VAL_RTSI_1`        ('VAL_RTSI_1')       - RTSI 1
    :py:data:`~niscope.NISCOPE_VAL_RTSI_2`        ('VAL_RTSI_2')       - RTSI 2
    :py:data:`~niscope.NISCOPE_VAL_RTSI_3`        ('VAL_RTSI_3')       - RTSI 3
    :py:data:`~niscope.NISCOPE_VAL_RTSI_4`        ('VAL_RTSI_4')       - RTSI 4
    :py:data:`~niscope.NISCOPE_VAL_RTSI_5`        ('VAL_RTSI_5')       - RTSI 5
    :py:data:`~niscope.NISCOPE_VAL_RTSI_6`        ('VAL_RTSI_6')       - RTSI 6
    :py:data:`~niscope.NISCOPE_VAL_PFI_0`         ('VAL_PFI_0')        - PFI 0
    :py:data:`~niscope.NISCOPE_VAL_PFI_1`         ('VAL_PFI_1')        - PFI 1
    :py:data:`~niscope.NISCOPE_VAL_PFI_2`         ('VAL_PFI_2')        - PFI 2
    :py:data:`~niscope.NISCOPE_VAL_PXI_STAR`      ('VAL_PXI_STAR')     - PXI Star Trigger

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

    Specifies the source the digitizer monitors for an advance trigger.   When the advance trigger is received, the digitizer begins acquiring pretrigger  samples.

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

.. py:attribute:: allow_more_records_than_memory

    Indicates whether more records can be configured with :py:meth:`niscope.Session.configure_horizontal_timing`  than fit in the onboard memory. If this attribute is set to VI_TRUE, it is necessary  to fetch records while the acquisition is in progress.  Eventually, some of  the records will be overwritten.  An error is returned from the fetch function  if you attempt to fetch a record that has been overwritten.

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

.. py:attribute:: arm_ref_trig_src

    Specifies the source the digitizer monitors for an arm reference trigger.   When the arm reference trigger is received, the digitizer begins looking for a  reference (stop) trigger from the user-configured trigger source.

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

    Returns the number of samples (:py:data:`niscope.Session.points_done`) that have been acquired but not fetched  for the record specified by :py:data:`niscope.Session.fetch_record_number`.

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

    Enables the bandpass filter on the specificed channel.  The default value is FALSE.




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

    Indicates the bit width of the binary data in the acquired waveform.  Useful for determining which Binary Fetch function to use. Compare to :py:data:`niscope.Session.resolution`.
    To configure the device to store samples with a lower resolution that the native, set this attribute to the desired binary width.
    This can be useful for streaming at faster speeds at the cost of resolution. The least significant bits will be lost with this configuration.
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

.. py:attribute:: cache

    Specifies whether to cache the value of attributes.  When caching is  enabled, the instrument driver keeps track of the current instrument  settings and avoids sending redundant commands to the instrument.  Thus,  you can significantly increase execution speed.
    The instrument driver can choose to always cache or to never cache  particular attributes regardless of the setting of this attribute.
    The default value is VI_TRUE.   Use :py:meth:`niscope.Session._init_with_options`  to override this value.

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

.. py:attribute:: channel_count

    Indicates the number of channels that the specific instrument driver  supports.
    For channel-based properties, the IVI engine maintains a separate cache value for each channel.

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
    Valid Values:
    VI_TRUE  (1) - Acquire data on this channel
    VI_FALSE (0) - Don't acquire data on this channel




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        channel_enabled.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        channel_enabled.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].channel_enabled = var
            var = session['0,1'].channel_enabled

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

            - LabVIEW Property: **Vertical:Channel Enabled**
            - C Attribute: **NISCOPE_ATTR_CHANNEL_ENABLED**

.. py:attribute:: channel_terminal_configuration

    Specifies the terminal configuration for the channel.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        channel_terminal_configuration.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        channel_terminal_configuration.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].channel_terminal_configuration = var
            var = session['0,1'].channel_terminal_configuration

    The following table lists the characteristics of this property.

    +----------------+-----------------------------+
    | Characteristic | Value                       |
    +================+=============================+
    | Datatype       | enums.TerminalConfiguration |
    +----------------+-----------------------------+
    | Permissions    | read-write                  |
    +----------------+-----------------------------+
    | Channel Based  | True                        |
    +----------------+-----------------------------+
    | Resettable     | No                          |
    +----------------+-----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Vertical:Channel Terminal Configuration**
            - C Attribute: **NISCOPE_ATTR_CHANNEL_TERMINAL_CONFIGURATION**

.. py:attribute:: clock_sync_pulse_source

    For the NI 5102, specifies the line on which the sample clock is sent or received. For the NI 5112/5620/5621/5911,  specifies the line on which the one-time sync pulse is sent or received. This line should be the same for all devices to be synchronized.

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

.. py:attribute:: data_transfer_block_size

    Specifies the maximum number of samples to transfer at one time from the device to host memory. Increasing this number should result in better fetching performance because the driver does not need to restart the transfers as often. However, increasing this number may also increase the amount of page-locked memory required from the system.

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

    This property specifies the maximum bandwidth that the device is allowed to consume.

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

    This property specifies the size of (read request|memory write) data payload. Due to alignment of the data buffers, the hardware may not always generate a packet of this size.

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

    The frequency at which the DDC block frequency translates the input data.
    Default Value: 10 MHz




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

    The way in which data is processed by the DDC block.
    Valid Values:
    Real (0)
    Complex (1)
    Default Value: Complex

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
    | Resettable     | No                       |
    +----------------+--------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Onboard Signal Processing:DDC:Data Processing Mode**
            - C Attribute: **NISCOPE_ATTR_DDC_DATA_PROCESSING_MODE**

.. py:attribute:: ddc_enabled

    Enables/disables the Digital Down Converter (DDC) block of the digitizer.  When the DDC block is disabled, all DDC-related properties are disabled and  have no effect on the acquired signal.
    Default Value: VI_FALSE




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

    Enables/disables frequency translating the data around the user-selected center  frequency down to baseband.
    Default Value: VI_TRUE




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

    The I center frequency phase in degrees at the first point of the acquisition.
    Default Value: 0




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

    The Q center frequency phase in degrees at the first point of the acquisition.  Use this attribute only when :py:data:`niscope.Session.ddc_data_processing_mode` is set to Complex.
    Default Value: 90




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

    Indicates the channel that is the input of the Q path of the DDC.
    Default Value: The channel that the attribute is configured off of.




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

    Returns the temperature of the device in degrees Celsius from the onboard sensor.

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

    Applies gain to the specified channel in hardware before any onboard processing.
    Valid Values:
    -1.5 to 1.5




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

    Applies offset to the specified channel in hardware before any onboard processing.
    Valid Values:
    -1.5 to 1.5 V




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

.. py:attribute:: dither_enabled

    Enables or Disables the analog dither on the device.  The default value is FALSE.
    Using dither can improve the spectral performance of the device by reducing the effects of quantization.  However, adding dither increases the power level to the ADC, so you may need to either decrease the signal level or increase your vertical range.




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

.. py:attribute:: driver_setup

    This attribute indicates the Driver Setup string that the user  specified when initializing the driver.
    Some cases exist where the end-user must specify instrument driver  options at initialization.  An example of this is specifying  a particular instrument model from among a family of instruments  that the driver supports.  This is useful when using simulation.   The end-user can specify driver-specific options through  the DriverSetup keyword in the optionsString parameter in  :py:meth:`niscope.Session._init_with_options`, or through the IVI Configuration Utility.
    If the user does not specify a Driver Setup string, this attribute returns an empty string.

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

            - C Attribute: **NISCOPE_ATTR_DRIVER_SETUP**

.. py:attribute:: enable_dc_restore

    Restores the video-triggered data retrieved by the digitizer to the video signal's zero reference point.
    Valid Values:
    VI_TRUE - Enable DC restore
    VI_FALSE - Disable DC restore

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

.. py:attribute:: enable_time_interleaved_sampling

    Specifies whether the digitizer acquires the waveform using multiple ADCs for the channel  enabling a higher maximum real-time sampling rate.
    Valid Values:
    VI_TRUE  (1) - Use multiple interleaved ADCs on this channel
    VI_FALSE (0) - Use only this channel's ADC to acquire data for this channel




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        enable_time_interleaved_sampling.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        enable_time_interleaved_sampling.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].enable_time_interleaved_sampling = var
            var = session['0,1'].enable_time_interleaved_sampling

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

            - LabVIEW Property: **Horizontal:Enable Time Interleaved Sampling**
            - C Attribute: **NISCOPE_ATTR_ENABLE_TIME_INTERLEAVED_SAMPLING**

.. py:attribute:: end_of_acquisition_event_output_terminal

    Specifies the destination for the End of Acquisition Event.    When this event is asserted, the digitizer has completed sampling for all records.
    Consult your device documentation for a specific list of valid destinations.

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

    Specifies the destination for the End of Record Event.    When this event is asserted, the digitizer has completed sampling for the current record.
    Consult your device documentation for a specific list of valid destinations.

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

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | datetime.timedelta |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:End of Record to Advance Trigger Holdoff**
            - C Attribute: **NISCOPE_ATTR_END_OF_RECORD_TO_ADVANCE_TRIGGER_HOLDOFF**

.. py:attribute:: equalization_filter_enabled

    Enables the onboard signal processing FIR block. This block is connected directly to the input signal.  This filter is designed to compensate the input signal for artifacts introduced to the signal outside  of the digitizer. However, since this is a generic FIR filter any coefficients are valid.  Coefficients  should be between +1 and -1 in value.




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

    Returns the number of coefficients that the FIR filter can accept.  This filter is designed  to compensate the input signal for artifacts introduced to the signal outside of the digitizer.   However, since this is a generic FIR filter any coefficients are valid.  Coefficients should be  between +1 and -1 in value.




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

    Specifies the destination to export the advance trigger.   When the advance trigger is received, the digitizer begins acquiring  samples for the Nth record.
    Consult your device documentation for a specific list of valid destinations.

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

    Specifies the destination export for the reference (stop) trigger.
    Consult your device documentation for a specific list of valid destinations.

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

.. py:attribute:: exported_start_trigger_output_terminal

    Specifies the destination to export the Start trigger.   When the start trigger is received, the digitizer begins acquiring  samples.
    Consult your device documentation for a specific list of valid destinations.

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

    Set to VI_TRUE to retrieve one array with alternating values on the NI 5620/5621.  For example, this attribute can be used to retrieve a single array with I and Q interleaved  instead of two separate arrays. If set to VI_TRUE, the resulting array will be twice the size of the actual record length.

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

    Enables/disables interleaving of the I and Q data.  When disabled, the traditional  :py:meth:`niscope.Session._fetch`() functions will return the I waveform for each acquisition followed by  the Q waveform.  When enabled, the I and Q  data are interleaved into a single waveform.  In the interleaving case, you must  allocate twice as many elements in the array as number of samples being fetched (since each  sample contains an I and a Q component).
    Default Value: VI_TRUE

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

            - LabVIEW Property: **Onboard Signal Processing:DDC:Fetch Interleaved IQ Data**
            - C Attribute: **NISCOPE_ATTR_FETCH_INTERLEAVED_IQ_DATA**

.. py:attribute:: fetch_meas_num_samples

    Number of samples to fetch when performing a measurement. Use -1 to fetch the actual record length.
    Default Value: -1

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

    Number of records to fetch. Use -1 to fetch all configured records.
    Default Value: -1

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

    Offset in samples to start fetching data within each record. The offset is applied relative to  :py:data:`niscope.Session.fetch_relative_to`.The offset can be positive or negative.
    Default Value: 0

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

    Zero-based index of the first record to fetch.  Use NISCOPE_FETCH_NUM_RECORDS to set the number of records to fetch.
    Default Value: 0.

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

    Position to start fetching within one record.
    Default Value: :py:data:`~niscope.FetchRelativeTo.PRETRIGGER`

    The following table lists the characteristics of this property.

    +----------------+-----------------------+
    | Characteristic | Value                 |
    +================+=======================+
    | Datatype       | enums.FetchRelativeTo |
    +----------------+-----------------------+
    | Permissions    | read-write            |
    +----------------+-----------------------+
    | Channel Based  | False                 |
    +----------------+-----------------------+
    | Resettable     | No                    |
    +----------------+-----------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Fetch:Fetch Relative To**
            - C Attribute: **NISCOPE_ATTR_FETCH_RELATIVE_TO**

.. py:attribute:: flex_fir_antialias_filter_type

    The NI 5922 flexible-resolution digitizer uses an onboard FIR lowpass antialias filter.
    Use this attribute to select from several types of filters to achieve desired filtering characteristics.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        flex_fir_antialias_filter_type.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        flex_fir_antialias_filter_type.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].flex_fir_antialias_filter_type = var
            var = session['0,1'].flex_fir_antialias_filter_type

    The following table lists the characteristics of this property.

    +----------------+----------------------------------+
    | Characteristic | Value                            |
    +================+==================================+
    | Datatype       | enums.FlexFIRAntialiasFilterType |
    +----------------+----------------------------------+
    | Permissions    | read-write                       |
    +----------------+----------------------------------+
    | Channel Based  | True                             |
    +----------------+----------------------------------+
    | Resettable     | No                               |
    +----------------+----------------------------------+

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

    Enables the onboard signal processing block that resamples the input waveform to the user desired sample rate.  The default value is FALSE.

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

    A string that contains a comma-separated list of class extension groups that this driver implements.

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

    Indicates whether the digitizer enforces real-time measurements  or allows equivalent-time measurements.

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

            - LabVIEW Property: **Horizontal:Enforce Realtime**
            - C Attribute: **NISCOPE_ATTR_HORZ_ENFORCE_REALTIME**

.. py:attribute:: horz_min_num_pts

    Specifies the minimum number of points you require in the waveform record for each channel.  NI-SCOPE uses the value you specify to configure the record length that the digitizer uses  for waveform acquisition. :py:data:`niscope.Session.horz_record_length` returns the actual record length.
    Valid Values: 1 - available onboard memory

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

    Specifies the number of records to acquire. Can be used for multi-record acquisition  and single-record acquisitions. Setting this to 1 indicates a single-record acquisition.

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

    Returns the actual number of points the digitizer acquires for each channel.  The value is equal to or greater than the minimum number of points you specify with  :py:data:`niscope.Session.horz_min_num_pts`.
    Allocate a ViReal64 array of this size or greater to pass as the WaveformArray parameter of  the Read and Fetch functions. This attribute is only valid after a call to the one of the  Configure Horizontal functions.

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

    Specifies the position of the Reference Event in the waveform record.  When the digitizer detects a trigger, it waits the length of time the  :py:data:`niscope.Session.trigger_delay_time` attribute specifies. The event that occurs when  the delay time elapses is the Reference Event. The Reference Event is relative to the  start of the record and is a percentage of the record length. For example, the value 50.0  corresponds to the center of the waveform record and 0.0 corresponds to the first element in the waveform record.
    Valid Values: 0.0 - 100.0

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

    Returns the effective sample rate using the current configuration. The units are samples per second.  This attribute is only valid after a call to the one of the Configure Horizontal functions.
    Units: Hertz (Samples / Second)

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

    Specifies the length of time that corresponds to the record length.
    Units: Seconds

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
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Horizontal:Advanced:Time Per Record**
            - C Attribute: **NISCOPE_ATTR_HORZ_TIME_PER_RECORD**

.. py:attribute:: input_clock_source

    Specifies the input source for the PLL reference clock (the 1 MHz to 20 MHz clock on the NI 5122, the 10 MHz clock  for the NI 5112/5620/5621/5911) to which the digitizer will be phase-locked; for the NI 5102, this is the source  of the board clock.

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

    Specifies the input impedance for the channel in Ohms.




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

    A string that contains the firmware revision information  for the instrument you are currently using.

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

    A string that contains the name of the instrument manufacturer.

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

    NI-SCOPE does not generate interchange warnings and therefore ignores this attribute.

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

    Indicates the resource descriptor the driver uses to identify the physical device.  If you initialize the driver with a logical name, this attribute contains the resource descriptor  that corresponds to the entry in the IVI Configuration utility.
    If you initialize the instrument driver with the resource descriptor, this attribute contains that  value.You can pass a logical name to :py:meth:`niscope.Session.Init` or :py:meth:`niscope.Session._init_with_options`. The IVI Configuration  utility must contain an entry for the logical name. The logical name entry refers to a virtual  instrument section in the IVI Configuration file. The virtual instrument section specifies a physical  device and initial user options.

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

    A string containing the logical name you specified when opening the current IVI session.  You can pass a logical name to :py:meth:`niscope.Session.Init` or :py:meth:`niscope.Session._init_with_options`. The IVI Configuration  utility must contain an entry for the logical name. The logical name entry refers to a virtual  instrument section in the IVI Configuration file. The virtual instrument section specifies a physical  device and initial user options.

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

    Specifies whether you want the device to be a master or a slave. The master typically originates  the trigger signal and clock sync pulse. For a standalone device, set this attribute to VI_FALSE.

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

    Specifies the bandwidth of the channel. Express this value as the frequency at which the input  circuitry attenuates the input signal by 3 dB. The units are hertz.
    Defined Values:
    :py:data:`~niscope.NISCOPE_VAL_BANDWIDTH_FULL` (-1.0)
    :py:data:`~niscope.NISCOPE_VAL_BANDWIDTH_DEVICE_DEFAULT` (0.0)
    :py:data:`~niscope.NISCOPE_VAL_20MHZ_BANDWIDTH` (20000000.0)
    :py:data:`~niscope.NISCOPE_VAL_100MHZ_BANDWIDTH` (100000000.0)
    :py:data:`~niscope.NISCOPE_VAL_20MHZ_MAX_INPUT_FREQUENCY` (20000000.0)
    :py:data:`~niscope.NISCOPE_VAL_100MHZ_MAX_INPUT_FREQUENCY` (100000000.0)




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

    Returns the maximum real time sample rate in Hz.

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

    Returns the maximum sample rate in RIS mode in Hz.

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

    Every element of an array is multiplied by this scalar value during the Array Gain measurement.  Refer to :py:data:`~niscope.NISCOPE_VAL_ARRAY_GAIN` for more information.
    Default: 1.0




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

    Every element of an array is added to this scalar value during the Array Offset measurement. Refer to :py:data:`~niscope.NISCOPE_VAL_ARRAY_OFFSET` for more information.
    Default: 0.0




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

    Stores the high reference level used in many scalar measurements. Different channels may have different reference  levels. Do not use the IVI-defined, nonchannel-based attributes such as :py:data:`niscope.Session.MEAS_HIGH_REF` if you use  this attribute to set various channels to different values.
    Default: 90%




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

    Stores the low reference level used in many scalar measurements. Different channels  may have different reference levels. Do not use the IVI-defined, nonchannel-based attributes such as  :py:data:`niscope.Session.MEAS_LOW_REF` if you use this attribute to set various channels to different values.
    Default: 10%




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

    Stores the mid reference level used in many scalar measurements. Different channels  may have different reference levels. Do not use the IVI-defined, nonchannel-based attributes such as  :py:data:`niscope.Session.MEAS_MID_REF` if you use this attribute to set various channels to different values.
    Default: 50%




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

    The center frequency in hertz for filters of type bandpass and bandstop. The width of the filter is specified by :py:data:`niscope.Session.meas_filter_width`, where the cutoff frequencies are the center ± width.
    Default: 1.0e6 Hz




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

    Specifies the cutoff frequency in hertz for filters of type lowpass and highpass. The cutoff frequency definition varies depending on the filter.
    Default: 1.0e6 Hz




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

    Specifies the order of an IIR filter. All positive integers are valid.
    Default: 2

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

    Specifies the amount of ripple in the passband in units of decibels (positive values). Used only for Chebyshev filters. The more ripple allowed gives a sharper cutoff for a given filter order.
    Default: 0.1 dB

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

    Defines the number of taps (coefficients) for an FIR filter.
    Default: 25

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

    The percentage (0 - 100%) of the IIR filtered waveform to eliminate from the beginning of the waveform. This allows eliminating the transient portion of the waveform that is undefined due to the assumptions necessary at the boundary condition.
    Default: 20.0%




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

    Specifies the type of filter, for both IIR and FIR filters. The allowed values are the following:
    ·  :py:data:`~niscope.NISCOPE_VAL_MEAS_LOWPASS`
    ·  :py:data:`~niscope.NISCOPE_VAL_MEAS_HIGHPASS`
    ·  :py:data:`~niscope.NISCOPE_VAL_MEAS_BANDPASS`
    ·  :py:data:`~niscope.NISCOPE_VAL_MEAS_BANDSTOP`
    Default: :py:data:`~niscope.NISCOPE_VAL_MEAS_LOWPASS`

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
    | Resettable     | No               |
    +----------------+------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Filter:Type**
            - C Attribute: **NISCOPE_ATTR_MEAS_FILTER_TYPE**

.. py:attribute:: meas_filter_width

    Specifies the width of bandpass and bandstop type filters in hertz. The cutoff frequencies occur at :py:data:`niscope.Session.meas_filter_center_freq` ± one-half width.
    Default: 1.0e3 Hz

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

    Specifies the FIR window type. The possible choices are:
    :py:data:`~niscope.NISCOPE_VAL_NONE`
    :py:data:`~niscope.NISCOPE_VAL_HANNING_WINDOW`
    :py:data:`~niscope.NISCOPE_VAL_HAMMING_WINDOW`
    :py:data:`~niscope.NISCOPE_VAL_TRIANGLE_WINDOW`
    :py:data:`~niscope.NISCOPE_VAL_FLAT_TOP_WINDOW`
    :py:data:`~niscope.NISCOPE_VAL_BLACKMAN_WINDOW`
    The symmetric windows are applied to the FIR filter coefficients to limit passband ripple in FIR filters.
    Default: :py:data:`~niscope.NISCOPE_VAL_NONE`




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_fir_filter_window.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_fir_filter_window.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_fir_filter_window = var
            var = session['0,1'].meas_fir_filter_window

    The following table lists the characteristics of this property.

    +----------------+-----------------------+
    | Characteristic | Value                 |
    +================+=======================+
    | Datatype       | enums.FIRFilterWindow |
    +----------------+-----------------------+
    | Permissions    | read-write            |
    +----------------+-----------------------+
    | Channel Based  | True                  |
    +----------------+-----------------------+
    | Resettable     | No                    |
    +----------------+-----------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Filter:FIR Window**
            - C Attribute: **NISCOPE_ATTR_MEAS_FIR_FILTER_WINDOW**

.. py:attribute:: meas_hysteresis_percent

    Digital hysteresis that is used in several of the scalar waveform measurements. This attribute specifies the percentage of the full-scale vertical range for the hysteresis window size.
    Default: 2%




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

    The new number of points for polynomial interpolation is the sampling factor times the input number of points. For example, if you acquire 1,000 points with the digitizer and set this attribute to 2.5, calling :py:meth:`niscope.Session.FetchWaveformMeasurementArray` with the :py:data:`~niscope.NISCOPE_VAL_POLYNOMIAL_INTERPOLATION` measurement resamples the waveform to 2,500 points.
    Default: 2.0




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

    Specifies the size (that is, the number of bins) in the last acquisition histogram. This histogram is used to determine several scalar measurements, most importantly voltage low and voltage high.
    Default: 256




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

    Specifies the second channel for two-channel measurements, such as :py:data:`~niscope.NISCOPE_VAL_ADD_CHANNELS`. If processing steps are registered with this channel, the processing is done before the waveform is used in a two-channel measurement.
    Default: '0'




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

    Specifies the method used to map percentage reference units to voltages for the reference. Possible values are:
    :py:data:`~niscope.NISCOPE_VAL_MEAS_LOW_HIGH`
    :py:data:`~niscope.NISCOPE_VAL_MEAS_MIN_MAX`
    :py:data:`~niscope.NISCOPE_VAL_MEAS_BASE_TOP`
    Default: :py:data:`~niscope.NISCOPE_VAL_MEAS_BASE_TOP`




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_percentage_method.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_percentage_method.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_percentage_method = var
            var = session['0,1'].meas_percentage_method

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | enums.PercentageMethod |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | True                   |
    +----------------+------------------------+
    | Resettable     | No                     |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Reference Levels:Percentage Units Method**
            - C Attribute: **NISCOPE_ATTR_MEAS_PERCENTAGE_METHOD**

.. py:attribute:: meas_polynomial_interpolation_order

    Specifies the polynomial order used for the polynomial interpolation measurement. For example, an order of 1 is linear interpolation whereas an order of 2 specifies parabolic interpolation. Any positive integer is valid.
    Default: 1

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

    Specifies the units of the reference levels.
    :py:data:`~niscope.NISCOPE_VAL_MEAS_VOLTAGE`--Specifies that the reference levels are given in units of volts
    :py:data:`~niscope.NISCOPE_VAL_MEAS_PERCENTAGE`--Percentage units, where the measurements voltage low and voltage high represent 0% and 100%, respectively.
    Default: :py:data:`~niscope.NISCOPE_VAL_MEAS_PERCENTAGE`




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        meas_ref_level_units.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        meas_ref_level_units.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].meas_ref_level_units = var
            var = session['0,1'].meas_ref_level_units

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | enums.RefLevelUnits |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | True                |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Waveform Measurement:Reference Levels:Units**
            - C Attribute: **NISCOPE_ATTR_MEAS_REF_LEVEL_UNITS**

.. py:attribute:: meas_time_histogram_high_time

    Specifies the highest time value included in the multiple acquisition time histogram. The units are always seconds.
    Default: 5.0e-4 seconds

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

    Specifies the highest voltage value included in the multiple-acquisition time histogram. The units are always volts.
    Default: 10.0 V




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

    Specifies the lowest time value included in the multiple-acquisition time histogram. The units are always seconds.
    Default: -5.0e-4 seconds

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

    Specifies the lowest voltage value included in the multiple acquisition time histogram. The units are always volts.
    Default: -10.0 V




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

    Determines the multiple acquisition voltage histogram size. The size is set during the first call to a time histogram measurement after clearing the measurement history with :py:meth:`niscope.Session.clear_waveform_measurement_stats`.
    Default: 256




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

    Specifies the highest voltage value included in the multiple acquisition voltage histogram. The units are always volts.
    Default: 10.0 V

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

    Specifies the lowest voltage value included in the multiple-acquisition voltage histogram. The units are always volts.
    Default: -10.0 V

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

    Determines the multiple acquisition voltage histogram size. The size is set the first time a voltage histogram measurement is called after clearing the measurement history with the function :py:meth:`niscope.Session.clear_waveform_measurement_stats`.
    Default: 256

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

    Specify the sampling rate for the acquisition in Samples per second.
    Valid Values:
    The combination of sampling rate and min record length must allow the  digitizer to sample at a valid sampling rate for the acquisition type specified  in :py:meth:`niscope.Session.ConfigureAcquisition` and not require more memory than the  onboard memory module allows.

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

    Returns the total combined amount of onboard memory for all channels in bytes.

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

    Gets or sets the binary phase DAC value that controls the delay added to the Phase Locked Loop (PLL) of the sample clock.



    .. note:: if this value is set, sample clock adjust and TClk will not be able to do any sub-sample adjustment of the timebase sample clock.

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

    Specifies the output source for the 10 MHz clock to which another digitizer's sample clock can be phased-locked.

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

    Configures error reporting when the DDC block detects an overflow in any of its  stages. Overflows lead to clipping of the waveform.
    Valid Values:
    Warning (0)
    Error (1)
    Disabled (2)
    Default Value: Warning

    The following table lists the characteristics of this property.

    +----------------+------------------------------+
    | Characteristic | Value                        |
    +================+==============================+
    | Datatype       | enums.OverflowErrorReporting |
    +----------------+------------------------------+
    | Permissions    | read-write                   |
    +----------------+------------------------------+
    | Channel Based  | False                        |
    +----------------+------------------------------+
    | Resettable     | No                           |
    +----------------+------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Onboard Signal Processing:OSP Overflow Error Reporting**
            - C Attribute: **NISCOPE_ATTR_OVERFLOW_ERROR_REPORTING**

.. py:attribute:: pll_lock_status

    If TRUE, the PLL has remained locked to the external reference clock since it was last checked. If FALSE,  the PLL has become unlocked from the external reference clock since it was last checked.

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

    Actual number of samples acquired in the record specified by :py:data:`niscope.Session.fetch_record_number` from the :py:data:`niscope.Session.fetch_relative_to` and :py:data:`niscope.Session.fetch_offset` attributes.

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

.. py:attribute:: poll_interval

    Specifies the poll interval in milliseconds to use during RIS acquisitions to check  whether the acquisition is complete.

    The following table lists the characteristics of this property.

    +----------------+------------+
    | Characteristic | Value      |
    +================+============+
    | Datatype       | int        |
    +----------------+------------+
    | Permissions    | read-write |
    +----------------+------------+
    | Channel Based  |          0 |
    +----------------+------------+
    | Resettable     |          0 |
    +----------------+------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - C Attribute: **NISCOPE_ATTR_POLL_INTERVAL**

.. py:attribute:: probe_attenuation

    Specifies the probe attenuation for the input channel. For example, for a 10:1 probe,  set this attribute to 10.0.
    Valid Values:
    Any positive real number. Typical values are 1, 10, and 100.




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

.. py:attribute:: range_check

    Specifies whether to validate attribute values and function parameters.   If enabled, the instrument driver validates the parameters values that you  pass to driver functions.  Range checking parameters is very useful for  debugging.  After you validate your program, you can set this attribute to  VI_FALSE to disable range checking and maximize performance.
    The default value is VI_TRUE.   Use the :py:meth:`niscope.Session._init_with_options`  function to override this value.

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

    Specifies the destination for the Ready for Advance Event.    When this event is asserted, the digitizer is ready to receive an advance trigger.
    Consult your device documentation for a specific list of valid destinations.

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

    Specifies the destination for the Ready for Reference Event.   When this event is asserted, the digitizer is ready to receive a reference trigger.
    Consult your device documentation for a specific list of valid destinations.

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

    Specifies the destination for the Ready for Start Event.   When this event is asserted, the digitizer is ready to receive a start trigger.
    Consult your device documentation for a specific list of valid destinations.

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

    Specifies the number of records that have been completely acquired.

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

    Specifies the record arm source.

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

    Specifies whether the IVI engine keeps a list of the value coercions it  makes for ViInt32 and ViReal64 attributes.  You call  Ivi_GetNextCoercionInfo to extract and delete the oldest coercion record  from the list.
    The default value is VI_FALSE.   Use the :py:meth:`niscope.Session._init_with_options`  function to override this value.

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

    If :py:data:`niscope.Session.input_clock_source` is an external source, this attribute specifies the frequency of the input,  or reference clock, to which the internal sample clock timebase is synchronized. The frequency is in hertz.

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

    Indicates which analog compare circuitry to use on the device.

    The following table lists the characteristics of this property.

    +----------------+----------------------------------+
    | Characteristic | Value                            |
    +================+==================================+
    | Datatype       | enums.RefTriggerDetectorLocation |
    +----------------+----------------------------------+
    | Permissions    | read-write                       |
    +----------------+----------------------------------+
    | Channel Based  | False                            |
    +----------------+----------------------------------+
    | Resettable     | No                               |
    +----------------+----------------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Onboard Signal Processing:Ref Trigger Detection Location**
            - C Attribute: **NISCOPE_ATTR_REF_TRIGGER_DETECTOR_LOCATION**

.. py:attribute:: ref_trigger_minimum_quiet_time

    The amount of time the trigger circuit must not detect a signal above the trigger level before  the trigger is armed.  This attribute is useful for triggering at the beginning and not in the  middle of signal bursts.

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
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Onboard Signal Processing:Ref Trigger Min Quiet Time**
            - C Attribute: **NISCOPE_ATTR_REF_TRIGGER_MINIMUM_QUIET_TIME**

.. py:attribute:: ref_trig_tdc_enable

    This attribute controls whether the TDC is used to compute an accurate trigger.

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

.. py:attribute:: resolution

    Indicates the bit width of valid data (as opposed to padding bits) in the acquired waveform. Compare to :py:data:`niscope.Session.binary_sample_width`.

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

    Indicates whether the digitizer should use RIS sample rates when searching for a frequency in autosetup.
    Valid Values:
    VI_TRUE  (1) - Use RIS sample rates in autosetup
    VI_FALSE (0) - Do not use RIS sample rates in autosetup

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

    Specifies the algorithm for random-interleaved sampling, which is used if the sample rate exceeds the  value of :py:data:`niscope.Session.max_real_time_sampling_rate`.

    The following table lists the characteristics of this property.

    +----------------+-----------------+
    | Characteristic | Value           |
    +================+=================+
    | Datatype       | enums.RISMethod |
    +----------------+-----------------+
    | Permissions    | read-write      |
    +----------------+-----------------+
    | Channel Based  | False           |
    +----------------+-----------------+
    | Resettable     | No              |
    +----------------+-----------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Horizontal:RIS Method**
            - C Attribute: **NISCOPE_ATTR_RIS_METHOD**

.. py:attribute:: ris_num_averages

    The number of averages for each bin in an RIS acquisition.  The number of averages  times the oversampling factor is the minimum number of real-time acquisitions  necessary to reconstruct the RIS waveform.  Averaging is useful in RIS because  the trigger times are not evenly spaced, so adjacent points in the reconstructed  waveform not be accurately spaced.  By averaging, the errors in both time and  voltage are smoothed.

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

.. py:attribute:: sample_clock_timebase_multiplier

    If `Sample Clock Timebase
    Source <p:py:meth:`niscope.Session.SampleClockTimebaseSource`.html>`__ is an external
    source, this property specifies the ratio between the `Sample Clock
    Timebase Rate <p:py:meth:`niscope.Session.SampleClockTimebaseRate`.html>`__ and the actual
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
            - C Attribute: **NISCOPE_ATTR_SAMPLE_CLOCK_TIMEBASE_MULTIPLIER**

.. py:attribute:: sample_mode

    Indicates the sample mode the digitizer is currently using.

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

    If :py:data:`niscope.Session.samp_clk_timebase_src` is an external source, specifies the ratio between the sample clock timebase rate and the actual sample rate, which can be slower.

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

.. py:attribute:: samp_clk_timebase_rate

    If :py:data:`niscope.Session.samp_clk_timebase_src` is an external source, specifies the frequency in hertz of the external clock used as the timebase source.

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

    Specifies the source of the sample clock timebase, which is the timebase used to control waveform sampling.  The actual sample rate may be the timebase itself or a divided version of the timebase, depending on the  :py:data:`niscope.Session.min_sample_rate` (for internal sources) or the :py:data:`niscope.Session.samp_clk_timebase_div` (for external sources).

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

.. py:attribute:: simulate

    Specifies whether or not to simulate instrument driver I/O operations.  If  simulation is enabled, instrument driver functions perform range checking  and call Ivi_GetAttribute and Ivi_SetAttribute functions, but they do not  perform instrument I/O.  For output parameters that represent instrument  data, the instrument driver functions return calculated values.
    The default value is VI_FALSE.   Use the :py:meth:`niscope.Session._init_with_options`  function to override this value.

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

    Specifies the delay for the trigger from the master to the slave in seconds.  This value adjusts the initial X value of the slave devices to correct for the  propagation delay between the master trigger output and slave trigger input.

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
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Synchronization:Trigger Calibration Delay:Slave Trigger Delay**
            - C Attribute: **NISCOPE_ATTR_SLAVE_TRIGGER_DELAY**

.. py:attribute:: specific_driver_class_spec_major_version

    The major version number of the class specification with which this driver is compliant.

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

    The minor version number of the class specification with which this driver is compliant.

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

    A string that contains a brief description of the specific  driver

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

.. py:attribute:: specific_driver_revision

    A string that contains additional version information about this  instrument driver.

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

    A string that contains the name of the vendor that supplies this driver.

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

    Pass the length of time you want the digitizer to wait after it starts acquiring  data until the digitizer enables the trigger system to detect a reference (stop) trigger.
    Units: Seconds
    Valid Values: 0.0 - 171.8




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        start_to_ref_trigger_holdoff.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        start_to_ref_trigger_holdoff.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].start_to_ref_trigger_holdoff = var
            var = session['0,1'].start_to_ref_trigger_holdoff

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | datetime.timedelta |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | True               |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Start To Ref Trigger Holdoff**
            - C Attribute: **NISCOPE_ATTR_START_TO_REF_TRIGGER_HOLDOFF**

.. py:attribute:: stream_relative_to

    Determines which trigger peer-to-peer data is streamed relative to. The
    default value is **Start Trigger**.



    .. note:: On the NI 5122/5622, only **Start Trigger** is valid for this property.

    The following table lists the characteristics of this property.

    +----------------+-----------------------------+
    | Characteristic | Value                       |
    +================+=============================+
    | Datatype       | enums.StreamingPositionType |
    +----------------+-----------------------------+
    | Permissions    | read-write                  |
    +----------------+-----------------------------+
    | Channel Based  | False                       |
    +----------------+-----------------------------+
    | Resettable     | No                          |
    +----------------+-----------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Peer-to-Peer:Stream Relative To**
            - C Attribute: **NISCOPE_ATTR_STREAM_RELATIVE_TO**

.. py:attribute:: supported_instrument_models

    A string that contains a comma-separated list of the instrument model numbers supported by this driver.

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

.. py:attribute:: trigger_auto_triggered

    Specifies if the last acquisition was auto triggered.   You can use the Auto Triggered attribute to find out if the last acquisition was triggered.

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

    Specifies how the digitizer couples the trigger source. This attribute affects instrument operation only when  :py:data:`niscope.Session.trigger_type` is set to :py:data:`~niscope.TriggerType.EDGE`, :py:data:`~niscope.TriggerType.HYSTERESIS`, or :py:data:`~niscope.TriggerType.WINDOW`.

    The following table lists the characteristics of this property.

    +----------------+-----------------------+
    | Characteristic | Value                 |
    +================+=======================+
    | Datatype       | enums.TriggerCoupling |
    +----------------+-----------------------+
    | Permissions    | read-write            |
    +----------------+-----------------------+
    | Channel Based  | False                 |
    +----------------+-----------------------+
    | Resettable     | No                    |
    +----------------+-----------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Trigger Coupling**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_COUPLING**

.. py:attribute:: trigger_delay_time

    Specifies the trigger delay time in seconds. The trigger delay time is the length of time the digitizer waits  after it receives the trigger. The event that occurs when the trigger delay elapses is the Reference Event.
    Valid Values: 0.0 - 171.8

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
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Trigger Delay**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_DELAY_TIME**

.. py:attribute:: trigger_from_pfi_delay

    This is a factory-programmed value that specifies the delay for the PFI lines  to the trigger input in seconds.  By itself, this attribute has no effect on  the acquired data.  However, depending on how the trigger lines are routed  between the master and slave devices, you can use this value as a starting  point to set :py:data:`niscope.Session.slave_trigger_delay`.

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | datetime.timedelta |
    +----------------+--------------------+
    | Permissions    | read only          |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Synchronization:Trigger Calibration Delay:Trigger from PFI Delay**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_FROM_PFI_DELAY**

.. py:attribute:: trigger_from_rtsi_delay

    This is a factory-programmed value that specifies the delay for the RTSI bus  to the trigger input in seconds.  By itself, this attribute has no effect on  the acquired data.  However, depending on how the trigger lines are routed  between the master and slave devices, you can use this value as a starting point  to set :py:data:`niscope.Session.slave_trigger_delay`.

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | datetime.timedelta |
    +----------------+--------------------+
    | Permissions    | read only          |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Synchronization:Trigger Calibration Delay:Trigger from RTSI Delay**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_FROM_RTSI_DELAY**

.. py:attribute:: trigger_from_star_delay

    This is a factory-programmed value that specifies the delay for PXI Star  Trigger line to the trigger input in seconds.  By itself, this attribute  has no effect on the acquired data.  However, depending on how the trigger  lines are routed between the master and slave devices, you can use this value  as a starting point to set :py:data:`niscope.Session.slave_trigger_delay`.

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | datetime.timedelta |
    +----------------+--------------------+
    | Permissions    | read only          |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Synchronization:Trigger Calibration Delay:Trigger from Star Delay**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_FROM_STAR_DELAY**

.. py:attribute:: trigger_holdoff

    Specifies the length of time (in seconds) the digitizer waits after detecting a trigger before  enabling the trigger subsystem to detect another trigger. This attribute affects instrument operation  only when the digitizer requires multiple acquisitions to build a complete waveform. The digitizer requires  multiple waveform acquisitions when it uses equivalent-time sampling or when the digitizer is configured for a  multi-record acquisition through a call to :py:meth:`niscope.Session.configure_horizontal_timing`.
    Valid Values: 0.0 - 171.8

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
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Trigger Holdoff**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_HOLDOFF**

.. py:attribute:: trigger_hysteresis

    Specifies the size of the hysteresis window on either side of the trigger level.  The digitizer triggers when the trigger signal passes through the threshold you specify  with the Trigger Level parameter, has the slope you specify with the Trigger Slope parameter,  and passes through the hysteresis window that you specify with this parameter.

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

    Specifies the input impedance for the external analog trigger channel in Ohms.
    Valid Values:
    50      - 50 ohms
    1000000 - 1 mega ohm

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

    Specifies the voltage threshold for the trigger subsystem. The units are volts.  This attribute affects instrument behavior only when the :py:data:`niscope.Session.trigger_type` is set to  :py:data:`~niscope.TriggerType.EDGE`, :py:data:`~niscope.TriggerType.HYSTERESIS`, or :py:data:`~niscope.TriggerType.WINDOW`.
    Valid Values:
    The values of the range and offset parameters in :py:meth:`niscope.Session.configure_vertical` determine the valid range for the trigger level  on the channel you use as the Trigger Source. The value you pass for this parameter must meet the following conditions:

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

    Configures the device to automatically complete an acquisition if a trigger has not been received.
    Valid Values:
    None (1)         - Normal triggering
    Auto Trigger (2) - Auto trigger acquisition if no trigger arrives

    The following table lists the characteristics of this property.

    +----------------+-----------------------+
    | Characteristic | Value                 |
    +================+=======================+
    | Datatype       | enums.TriggerModifier |
    +----------------+-----------------------+
    | Permissions    | read-write            |
    +----------------+-----------------------+
    | Channel Based  | False                 |
    +----------------+-----------------------+
    | Resettable     | No                    |
    +----------------+-----------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Trigger Modifier**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_MODIFIER**

.. py:attribute:: trigger_slope

    Specifies if a rising or a falling edge triggers the digitizer.  This attribute affects instrument operation only when :py:data:`niscope.Session.trigger_type` is set to  :py:data:`~niscope.TriggerType.EDGE`, :py:data:`~niscope.TriggerType.HYSTERESIS`, or :py:data:`~niscope.TriggerType.WINDOW`.

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | enums.TriggerSlope |
    +----------------+--------------------+
    | Permissions    | read-write         |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Trigger Slope**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_SLOPE**

.. py:attribute:: trigger_source

    Specifies the source the digitizer monitors for the trigger event.

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

    This is a factory-programmed value that specifies the delay for the trigger  to the PFI lines in seconds.  By itself, this attribute has no effect on the  acquired data.  However, depending on how the trigger lines are routed between  the master and slave devices, you can use this value as a starting point to set  :py:data:`niscope.Session.slave_trigger_delay`.

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | datetime.timedelta |
    +----------------+--------------------+
    | Permissions    | read only          |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Synchronization:Trigger Calibration Delay:Trigger to PFI Delay**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_TO_PFI_DELAY**

.. py:attribute:: trigger_to_rtsi_delay

    This is a factory-programmed value that specifies the delay for the trigger  to the RTSI bus in seconds.  By itself, this attribute has no effect on the  acquired data.  However, depending on how the trigger lines are routed between  the master and slave devices, you can use this value as a starting point to set   :py:data:`niscope.Session.slave_trigger_delay`.

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | datetime.timedelta |
    +----------------+--------------------+
    | Permissions    | read only          |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Synchronization:Trigger Calibration Delay:Trigger to RTSI Delay**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_TO_RTSI_DELAY**

.. py:attribute:: trigger_to_star_delay

    This is a factory-programmed value that specifies the delay for the trigger  to the PXI Star Trigger line in seconds.  By itself, this attribute has no  effect on the acquired data.  However, depending on how the trigger lines  are routed between the master and slave devices, you can use this value as  a starting point to set :py:data:`niscope.Session.slave_trigger_delay`.

    The following table lists the characteristics of this property.

    +----------------+--------------------+
    | Characteristic | Value              |
    +================+====================+
    | Datatype       | datetime.timedelta |
    +----------------+--------------------+
    | Permissions    | read only          |
    +----------------+--------------------+
    | Channel Based  | False              |
    +----------------+--------------------+
    | Resettable     | No                 |
    +----------------+--------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Synchronization:Trigger Calibration Delay:Trigger to Star Delay**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_TO_STAR_DELAY**

.. py:attribute:: trigger_type

    Specifies the type of trigger to use.

    The following table lists the characteristics of this property.

    +----------------+-------------------+
    | Characteristic | Value             |
    +================+===================+
    | Datatype       | enums.TriggerType |
    +----------------+-------------------+
    | Permissions    | read-write        |
    +----------------+-------------------+
    | Channel Based  | False             |
    +----------------+-------------------+
    | Resettable     | No                |
    +----------------+-------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Trigger Type**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_TYPE**

.. py:attribute:: trigger_window_high_level

    Pass the upper voltage threshold you want the digitizer to use for  window triggering.
    The digitizer triggers when the trigger signal enters or leaves  the window you specify with :py:data:`niscope.Session.trigger_window_low_level` and :py:data:`niscope.Session.trigger_window_high_level`
    Valid Values:
    The values of the Vertical Range and Vertical Offset parameters in  :py:meth:`niscope.Session.configure_vertical` determine the valid range for the  High Window Level on the channel you use as the Trigger Source parameter  in :py:meth:`niscope.Session.ConfigureTriggerSource`.  The value you pass for this parameter  must meet the following conditions.
    High Trigger Level <= Vertical Range/2 + Vertical Offset
    High Trigger Level >= (-Vertical Range/2) + Vertical Offset
    High Trigger Level > Low Trigger Level

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

    Pass the lower voltage threshold you want the digitizer to use for  window triggering.
    The digitizer triggers when the trigger signal enters or leaves  the window you specify with :py:data:`niscope.Session.trigger_window_low_level` and :py:data:`niscope.Session.trigger_window_high_level`.
    Units: Volts
    Valid Values:
    The values of the Vertical Range and Vertical Offset parameters in  :py:meth:`niscope.Session.configure_vertical` determine the valid range for the  Low Window Level on the channel you use as the Trigger Source parameter  in :py:meth:`niscope.Session.ConfigureTriggerSource`.  The value you pass for this parameter  must meet the following conditions.
    Low Trigger Level <= Vertical Range/2 + Vertical Offset
    Low Trigger Level >= (-Vertical Range/2) + Vertical Offset
    Low Trigger Level < High Trigger Level

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

    Specifies whether you want a trigger to occur when the signal enters or leaves the window specified by  :py:data:`niscope.Session.trigger_window_low_level`, or :py:data:`niscope.Session.trigger_window_high_level`.

    The following table lists the characteristics of this property.

    +----------------+-------------------------+
    | Characteristic | Value                   |
    +================+=========================+
    | Datatype       | enums.TriggerWindowMode |
    +----------------+-------------------------+
    | Permissions    | read-write              |
    +----------------+-------------------------+
    | Channel Based  | False                   |
    +----------------+-------------------------+
    | Resettable     | No                      |
    +----------------+-------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Trigger Window:Window Mode**
            - C Attribute: **NISCOPE_ATTR_TRIGGER_WINDOW_MODE**

.. py:attribute:: tv_trigger_event

    Specifies the condition in the video signal that causes the digitizer to trigger.

    The following table lists the characteristics of this property.

    +----------------+-------------------------+
    | Characteristic | Value                   |
    +================+=========================+
    | Datatype       | enums.VideoTriggerEvent |
    +----------------+-------------------------+
    | Permissions    | read-write              |
    +----------------+-------------------------+
    | Channel Based  | False                   |
    +----------------+-------------------------+
    | Resettable     | No                      |
    +----------------+-------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Trigger Video:Event**
            - C Attribute: **NISCOPE_ATTR_TV_TRIGGER_EVENT**

.. py:attribute:: tv_trigger_line_number

    Specifies the line on which to trigger, if :py:data:`niscope.Session.tv_trigger_event` is set to line number. The  valid ranges of the attribute depend on the signal format selected.  M-NTSC has a valid range of 1 to 525.  B/G-PAL, SECAM, 576i, and 576p have a valid range of  1 to 625. 720p has a valid range of 1 to 750. 1080i and 1080p have a valid range of 1125.

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

    Specifies whether the video signal sync is positive or negative.

    The following table lists the characteristics of this property.

    +----------------+---------------------+
    | Characteristic | Value               |
    +================+=====================+
    | Datatype       | enums.VideoPolarity |
    +----------------+---------------------+
    | Permissions    | read-write          |
    +----------------+---------------------+
    | Channel Based  | False               |
    +----------------+---------------------+
    | Resettable     | No                  |
    +----------------+---------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Trigger Video:Polarity**
            - C Attribute: **NISCOPE_ATTR_TV_TRIGGER_POLARITY**

.. py:attribute:: tv_trigger_signal_format

    Specifies the type of video signal, such as NTSC, PAL, or SECAM.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        tv_trigger_signal_format.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        tv_trigger_signal_format.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].tv_trigger_signal_format = var
            var = session['0,1'].tv_trigger_signal_format

    The following table lists the characteristics of this property.

    +----------------+-------------------------+
    | Characteristic | Value                   |
    +================+=========================+
    | Datatype       | enums.VideoSignalFormat |
    +----------------+-------------------------+
    | Permissions    | read-write              |
    +----------------+-------------------------+
    | Channel Based  | True                    |
    +----------------+-------------------------+
    | Resettable     | No                      |
    +----------------+-------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Triggering:Trigger Video:Signal Format**
            - C Attribute: **NISCOPE_ATTR_TV_TRIGGER_SIGNAL_FORMAT**

.. py:attribute:: vertical_coupling

    Specifies how the digitizer couples the input signal for the channel.  When input coupling changes, the input stage takes a finite amount of time to settle.




    .. tip:: This property can use repeated capabilities (usually channels). If set or get directly on the
        vertical_coupling.Session object, then the set/get will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        vertical_coupling.Session instance, and calling set/get value on the result.:

        .. code:: python

            session['0,1'].vertical_coupling = var
            var = session['0,1'].vertical_coupling

    The following table lists the characteristics of this property.

    +----------------+------------------------+
    | Characteristic | Value                  |
    +================+========================+
    | Datatype       | enums.VerticalCoupling |
    +----------------+------------------------+
    | Permissions    | read-write             |
    +----------------+------------------------+
    | Channel Based  | True                   |
    +----------------+------------------------+
    | Resettable     | No                     |
    +----------------+------------------------+

    .. tip::
        This property corresponds to the following LabVIEW Property or C Attribute:

            - LabVIEW Property: **Vertical:Vertical Coupling**
            - C Attribute: **NISCOPE_ATTR_VERTICAL_COUPLING**

.. py:attribute:: vertical_offset

    Specifies the location of the center of the range. The value is with respect to ground and is in volts.  For example, to acquire a sine wave that spans between 0.0 and 10.0 V, set this attribute to 5.0 V.



    .. note:: This attribute is not supported by all digitizers.Refer to the NI High-Speed Digitizers Help for a list of vertical offsets supported for each device.


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

    Specifies the absolute value of the input range for a channel in volts.  For example, to acquire a sine wave that spans between -5 and +5 V, set this attribute to 10.0 V.
    Refer to the NI High-Speed Digitizers Help for a list of supported vertical ranges for each device.  If the specified range is not supported by a device, the value is coerced  up to the next valid range.




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


