niscope.Session methods
=======================

.. py:currentmodule:: niscope.Session

.. py:method:: abort()

    Aborts an acquisition and returns the digitizer to the Idle state. Call
    this method if the digitizer times out waiting for a trigger.

    



.. py:method:: acquisition_status()

    Returns status information about the acquisition to the **status**
    output parameter.

    



    :rtype: :py:data:`niscope.AcquisitionStatus`
    :return:


            Returns whether the acquisition is complete, in progress, or unknown.

            **Defined Values**

            :py:data:`~niscope.AcquisitionStatus.COMPLETE`

            :py:data:`~niscope.AcquisitionStatus.IN_PROGRESS`

            :py:data:`~niscope.AcquisitionStatus.STATUS_UNKNOWN`

            



.. py:method:: auto_setup()

    Automatically configures the instrument. When you call this method,
    the digitizer senses the input signal and automatically configures many
    of the instrument settings. If a signal is detected on a channel, the
    driver chooses the smallest available vertical range that is larger than
    the signal range. For example, if the signal is a 1.2 V\ :sub:`pk-pk`
    sine wave, and the device supports 1 V and 2 V vertical ranges, the
    driver will choose the 2 V vertical range for that channel.

    If no signal is found on any analog input channel, a warning is
    returned, and all channels are enabled. A channel is considered to have
    a signal present if the signal is at least 10% of the smallest vertical
    range available for that channel.

    The following settings are changed:

    +--------------------+-----------------------------------------------+
    | **General**        |                                               |
    +--------------------+-----------------------------------------------+
    | Acquisition mode   | Normal                                        |
    +--------------------+-----------------------------------------------+
    | Reference clock    | Internal                                      |
    +--------------------+-----------------------------------------------+
    | **Vertical**       |                                               |
    +--------------------+-----------------------------------------------+
    | Vertical coupling  | AC (DC for NI 5621)                           |
    +--------------------+-----------------------------------------------+
    | Vertical bandwidth | Full                                          |
    +--------------------+-----------------------------------------------+
    | Vertical range     | Changed by auto setup                         |
    +--------------------+-----------------------------------------------+
    | Vertical offset    | 0 V                                           |
    +--------------------+-----------------------------------------------+
    | Probe attenuation  | Unchanged by auto setup                       |
    +--------------------+-----------------------------------------------+
    | Input impedance    | Unchanged by auto setup                       |
    +--------------------+-----------------------------------------------+
    | **Horizontal**     |                                               |
    +--------------------+-----------------------------------------------+
    | Sample rate        | Changed by auto setup                         |
    +--------------------+-----------------------------------------------+
    | Min record length  | Changed by auto setup                         |
    +--------------------+-----------------------------------------------+
    | Enforce realtime   | True                                          |
    +--------------------+-----------------------------------------------+
    | Number of Records  | Changed to 1                                  |
    +--------------------+-----------------------------------------------+
    | **Triggering**     |                                               |
    +--------------------+-----------------------------------------------+
    | Trigger type       | Edge if signal present, otherwise immediate   |
    +--------------------+-----------------------------------------------+
    | Trigger channel    | Lowest numbered channel with a signal present |
    +--------------------+-----------------------------------------------+
    | Trigger slope      | Positive                                      |
    +--------------------+-----------------------------------------------+
    | Trigger coupling   | DC                                            |
    +--------------------+-----------------------------------------------+
    | Reference position | 50%                                           |
    +--------------------+-----------------------------------------------+
    | Trigger level      | 50% of signal on trigger channel              |
    +--------------------+-----------------------------------------------+
    | Trigger delay      | 0                                             |
    +--------------------+-----------------------------------------------+
    | Trigger holdoff    | 0                                             |
    +--------------------+-----------------------------------------------+
    | Trigger output     | None                                          |
    +--------------------+-----------------------------------------------+



.. py:method:: commit()

    Commits to hardware all the parameter settings associated with the task.
    Use this method if you want a parameter change to be immediately
    reflected in the hardware. This method is not supported for
    Traditional NI-DAQ (Legacy) devices.

    



.. py:method:: configure_chan_characteristics(input_impedance, max_input_frequency)

    Configures the properties that control the electrical characteristics of
    the channel—the input impedance and the bandwidth.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].configure_chan_characteristics(input_impedance, max_input_frequency)


    :param input_impedance:


        The input impedance for the channel; NI-SCOPE sets
        :py:data:`niscope.Session.input_impedance` to this value.

        


    :type input_impedance: float
    :param max_input_frequency:


        The bandwidth for the channel; NI-SCOPE sets
        :py:data:`niscope.Session.max_input_frequency` to this value. Pass 0 for this
        value to use the hardware default bandwidth. Pass –1 for this value to
        achieve full bandwidth.

        


    :type max_input_frequency: float

.. py:method:: configure_equalization_filter_coefficients(coefficients)

    Configures the custom coefficients for the equalization FIR filter on
    the device. This filter is designed to compensate the input signal for
    artifacts introduced to the signal outside of the digitizer. Because
    this filter is a generic FIR filter, any coefficients are valid.
    Coefficient values should be between +1 and –1.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].configure_equalization_filter_coefficients(coefficients)


    :param coefficients:


        The custom coefficients for the equalization FIR filter on the device.
        These coefficients should be between +1 and –1. You can obtain the
        number of coefficients from the
        `:py:data:`niscope.Session.equalization_num_coefficients` <cvi:py:data:`niscope.Session.equalization_num_coefficients`.html>`__
        property. The
        `:py:data:`niscope.Session.equalization_filter_enabled` <cvi:py:data:`niscope.Session.equalization_filter_enabled`.html>`__
        property must be set to TRUE to enable the filter.

        


    :type coefficients: list of float

.. py:method:: configure_horizontal_timing(min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime)

    Configures the common properties of the horizontal subsystem for a
    multirecord acquisition in terms of minimum sample rate.

    



    :param min_sample_rate:


        The sampling rate for the acquisition. Refer to
        :py:data:`niscope.Session.min_sample_rate` for more information.

        


    :type min_sample_rate: float
    :param min_num_pts:


        The minimum number of points you need in the record for each channel;
        call :py:meth:`niscope.Session.ActualRecordLength` to obtain the actual record length
        used.

        Valid Values: Greater than 1; limited by available memory

        

        .. note:: One or more of the referenced methods are not in the Python API for this driver.


    :type min_num_pts: int
    :param ref_position:


        The position of the Reference Event in the waveform record specified as
        a percentage.

        


    :type ref_position: float
    :param num_records:


        The number of records to acquire

        


    :type num_records: int
    :param enforce_realtime:


        Indicates whether the digitizer enforces real-time measurements or
        allows equivalent-time (RIS) measurements; not all digitizers support
        RIS—refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Default value: True

        **Defined Values**

        True—Allow real-time acquisitions only

        False—Allow real-time and equivalent-time acquisitions

        


    :type enforce_realtime: bool

.. py:method:: configure_trigger_digital(trigger_source, slope=niscope.TriggerSlope.POSITIVE, holdoff=datetime.timedelta(seconds=0.0), delay=datetime.timedelta(seconds=0.0))

    Configures the common properties of a digital trigger.

    When you initiate an acquisition, the digitizer waits for the start
    trigger, which is configured through the :py:data:`niscope.Session.acq_arm_source`
    (Start Trigger Source) property. The default is immediate. Upon
    receiving the start trigger the digitizer begins sampling pretrigger
    points. After the digitizer finishes sampling pretrigger points, the
    digitizer waits for a reference (stop) trigger that you specify with a
    method such as this one. Upon receiving the reference trigger the
    digitizer finishes the acquisition after completing posttrigger
    sampling. With each Configure Trigger method, you specify
    configuration parameters such as the trigger source and the amount of
    trigger delay.

    

    .. note:: For multirecord acquisitions, all records after the first record are
        started by using the Advance Trigger Source. The default is immediate.

        You can adjust the amount of pre-trigger and post-trigger samples using
        the reference position parameter on the
        :py:meth:`niscope.Session.configure_horizontal_timing` method. The default is half of the
        record length.

        Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Digital triggering is not supported in RIS mode.



    :param trigger_source:


        Specifies the trigger source. Refer to :py:data:`niscope.Session.trigger_source`
        for defined values.

        


    :type trigger_source: str
    :param slope:


        Specifies whether you want a rising edge or a falling edge to trigger
        the digitizer. Refer to :py:data:`niscope.Session.trigger_slope` for more
        information.

        


    :type slope: :py:data:`niscope.TriggerSlope`
    :param holdoff:


        The length of time the digitizer waits after detecting a trigger before
        enabling NI-SCOPE to detect another trigger. Refer to
        :py:data:`niscope.Session.trigger_holdoff` for more information.

        


    :type holdoff: float in seconds or datetime.timedelta
    :param delay:


        How long the digitizer waits after receiving the trigger to start
        acquiring data. Refer to :py:data:`niscope.Session.trigger_delay_time` for more
        information.

        


    :type delay: float in seconds or datetime.timedelta

.. py:method:: configure_trigger_edge(trigger_source, trigger_coupling, level=0.0, slope=niscope.TriggerSlope.POSITIVE, holdoff=datetime.timedelta(seconds=0.0), delay=datetime.timedelta(seconds=0.0))

    Configures common properties for analog edge triggering.

    When you initiate an acquisition, the digitizer waits for the start
    trigger, which is configured through the :py:data:`niscope.Session.acq_arm_source`
    (Start Trigger Source) property. The default is immediate. Upon
    receiving the start trigger the digitizer begins sampling pretrigger
    points. After the digitizer finishes sampling pretrigger points, the
    digitizer waits for a reference (stop) trigger that you specify with a
    method such as this one. Upon receiving the reference trigger the
    digitizer finishes the acquisition after completing posttrigger
    sampling. With each Configure Trigger method, you specify
    configuration parameters such as the trigger source and the amount of
    trigger delay.

    

    .. note:: Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.



    :param trigger_source:


        Specifies the trigger source. Refer to :py:data:`niscope.Session.trigger_source`
        for defined values.

        


    :type trigger_source: str
    :param trigger_coupling:


        Applies coupling and filtering options to the trigger signal. Refer to
        :py:data:`niscope.Session.trigger_coupling` for more information.

        


    :type trigger_coupling: :py:data:`niscope.TriggerCoupling`
    :param level:


        The voltage threshold for the trigger. Refer to
        :py:data:`niscope.Session.trigger_level` for more information.

        


    :type level: float
    :param slope:


        Specifies whether you want a rising edge or a falling edge to trigger
        the digitizer. Refer to :py:data:`niscope.Session.trigger_slope` for more
        information.

        


    :type slope: :py:data:`niscope.TriggerSlope`
    :param holdoff:


        The length of time the digitizer waits after detecting a trigger before
        enabling NI-SCOPE to detect another trigger. Refer to
        :py:data:`niscope.Session.trigger_holdoff` for more information.

        


    :type holdoff: float in seconds or datetime.timedelta
    :param delay:


        How long the digitizer waits after receiving the trigger to start
        acquiring data. Refer to :py:data:`niscope.Session.trigger_delay_time` for more
        information.

        


    :type delay: float in seconds or datetime.timedelta

.. py:method:: configure_trigger_hysteresis(trigger_source, trigger_coupling, level=0.0, hysteresis=0.05, slope=niscope.TriggerSlope.POSITIVE, holdoff=datetime.timedelta(seconds=0.0), delay=datetime.timedelta(seconds=0.0))

    Configures common properties for analog hysteresis triggering. This kind
    of trigger specifies an additional value, specified in the
    **hysteresis** parameter, that a signal must pass through before a
    trigger can occur. This additional value acts as a kind of buffer zone
    that keeps noise from triggering an acquisition.

    When you initiate an acquisition, the digitizer waits for the start
    trigger, which is configured through the
    :py:data:`niscope.Session.acq_arm_source`. The default is immediate. Upon
    receiving the start trigger the digitizer begins sampling pretrigger
    points. After the digitizer finishes sampling pretrigger points, the
    digitizer waits for a reference (stop) trigger that you specify with a
    method such as this one. Upon receiving the reference trigger the
    digitizer finishes the acquisition after completing posttrigger
    sampling. With each Configure Trigger method, you specify
    configuration parameters such as the trigger source and the amount of
    trigger delay.

    

    .. note:: Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.



    :param trigger_source:


        Specifies the trigger source. Refer to :py:data:`niscope.Session.trigger_source`
        for defined values.

        


    :type trigger_source: str
    :param trigger_coupling:


        Applies coupling and filtering options to the trigger signal. Refer to
        :py:data:`niscope.Session.trigger_coupling` for more information.

        


    :type trigger_coupling: :py:data:`niscope.TriggerCoupling`
    :param level:


        The voltage threshold for the trigger. Refer to
        :py:data:`niscope.Session.trigger_level` for more information.

        


    :type level: float
    :param hysteresis:


        The size of the hysteresis window on either side of the **level** in
        volts; the digitizer triggers when the trigger signal passes through the
        hysteresis value you specify with this parameter, has the slope you
        specify with **slope**, and passes through the **level**. Refer to
        :py:data:`niscope.Session.trigger_hysteresis` for defined values.

        


    :type hysteresis: float
    :param slope:


        Specifies whether you want a rising edge or a falling edge to trigger
        the digitizer. Refer to :py:data:`niscope.Session.trigger_slope` for more
        information.

        


    :type slope: :py:data:`niscope.TriggerSlope`
    :param holdoff:


        The length of time the digitizer waits after detecting a trigger before
        enabling NI-SCOPE to detect another trigger. Refer to
        :py:data:`niscope.Session.trigger_holdoff` for more information.

        


    :type holdoff: float in seconds or datetime.timedelta
    :param delay:


        How long the digitizer waits after receiving the trigger to start
        acquiring data. Refer to :py:data:`niscope.Session.trigger_delay_time` for more
        information.

        


    :type delay: float in seconds or datetime.timedelta

.. py:method:: configure_trigger_immediate()

    Configures common properties for immediate triggering. Immediate
    triggering means the digitizer triggers itself.

    When you initiate an acquisition, the digitizer waits for a trigger. You
    specify the type of trigger that the digitizer waits for with a
    Configure Trigger method, such as :py:meth:`niscope.Session.configure_trigger_immediate`.

    



.. py:method:: configure_trigger_software(holdoff=datetime.timedelta(seconds=0.0), delay=datetime.timedelta(seconds=0.0))

    Configures common properties for software triggering.

    When you initiate an acquisition, the digitizer waits for the start
    trigger, which is configured through the :py:data:`niscope.Session.acq_arm_source`
    (Start Trigger Source) property. The default is immediate. Upon
    receiving the start trigger the digitizer begins sampling pretrigger
    points. After the digitizer finishes sampling pretrigger points, the
    digitizer waits for a reference (stop) trigger that you specify with a
    method such as this one. Upon receiving the reference trigger the
    digitizer finishes the acquisition after completing posttrigger
    sampling. With each Configure Trigger method, you specify
    configuration parameters such as the trigger source and the amount of
    trigger delay.

    To trigger the acquisition, use :py:meth:`niscope.Session.send_software_trigger_edge`.

    

    .. note:: Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.



    :param holdoff:


        The length of time the digitizer waits after detecting a trigger before
        enabling NI-SCOPE to detect another trigger. Refer to
        :py:data:`niscope.Session.trigger_holdoff` for more information.

        


    :type holdoff: float in seconds or datetime.timedelta
    :param delay:


        How long the digitizer waits after receiving the trigger to start
        acquiring data. Refer to :py:data:`niscope.Session.trigger_delay_time` for more
        information.

        


    :type delay: float in seconds or datetime.timedelta

.. py:method:: configure_trigger_video(trigger_source, signal_format, event, polarity, trigger_coupling, enable_dc_restore=False, line_number=1, holdoff=datetime.timedelta(seconds=0.0), delay=datetime.timedelta(seconds=0.0))

    Configures the common properties for video triggering, including the
    signal format, TV event, line number, polarity, and enable DC restore. A
    video trigger occurs when the digitizer finds a valid video signal sync.

    When you initiate an acquisition, the digitizer waits for the start
    trigger, which is configured through the :py:data:`niscope.Session.acq_arm_source`
    (Start Trigger Source) property. The default is immediate. Upon
    receiving the start trigger the digitizer begins sampling pretrigger
    points. After the digitizer finishes sampling pretrigger points, the
    digitizer waits for a reference (stop) trigger that you specify with a
    method such as this one. Upon receiving the reference trigger the
    digitizer finishes the acquisition after completing posttrigger
    sampling. With each Configure Trigger method, you specify
    configuration parameters such as the trigger source and the amount of
    trigger delay.

    

    .. note:: Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.



    :param trigger_source:


        Specifies the trigger source. Refer to :py:data:`niscope.Session.trigger_source`
        for defined values.

        


    :type trigger_source: str
    :param signal_format:


        Specifies the type of video signal sync the digitizer should look for.
        Refer to :py:data:`niscope.Session.tv_trigger_signal_format` for more
        information.

        


    :type signal_format: :py:data:`niscope.VideoSignalFormat`
    :param event:


        Specifies the TV event you want to trigger on. You can trigger on a
        specific or on the next coming line or field of the signal.

        


    :type event: :py:data:`niscope.VideoTriggerEvent`
    :param polarity:


        Specifies the polarity of the video signal sync.

        


    :type polarity: :py:data:`niscope.VideoPolarity`
    :param trigger_coupling:


        Applies coupling and filtering options to the trigger signal. Refer to
        :py:data:`niscope.Session.trigger_coupling` for more information.

        


    :type trigger_coupling: :py:data:`niscope.TriggerCoupling`
    :param enable_dc_restore:


        Offsets each video line so the clamping level (the portion of the video
        line between the end of the color burst and the beginning of the active
        image) is moved to zero volt. Refer to
        :py:data:`niscope.Session.enable_dc_restore` for defined values.

        


    :type enable_dc_restore: bool
    :param line_number:


        Selects the line number to trigger on. The line number range covers an
        entire frame and is referenced as shown on `Vertical Blanking and
        Synchronization
        Signal <REPLACE_DRIVER_SPECIFIC_URL_1(gray_scale_image)>`__. Refer to
        :py:data:`niscope.Session.tv_trigger_line_number` for more information.

        Default value: 1

        


    :type line_number: int
    :param holdoff:


        The length of time the digitizer waits after detecting a trigger before
        enabling NI-SCOPE to detect another trigger. Refer to
        :py:data:`niscope.Session.trigger_holdoff` for more information.

        


    :type holdoff: float in seconds or datetime.timedelta
    :param delay:


        How long the digitizer waits after receiving the trigger to start
        acquiring data. Refer to :py:data:`niscope.Session.trigger_delay_time` for more
        information.

        


    :type delay: float in seconds or datetime.timedelta

.. py:method:: configure_trigger_window(trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff=datetime.timedelta(seconds=0.0), delay=datetime.timedelta(seconds=0.0))

    Configures common properties for analog window triggering. A window
    trigger occurs when a signal enters or leaves a window you specify with
    the **high level** or **low level** parameters.

    When you initiate an acquisition, the digitizer waits for the start
    trigger, which is configured through the :py:data:`niscope.Session.acq_arm_source`
    (Start Trigger Source) property. The default is immediate. Upon
    receiving the start trigger the digitizer begins sampling pretrigger
    points. After the digitizer finishes sampling pretrigger points, the
    digitizer waits for a reference (stop) trigger that you specify with a
    method such as this one. Upon receiving the reference trigger the
    digitizer finishes the acquisition after completing posttrigger
    sampling. With each Configure Trigger method, you specify
    configuration parameters such as the trigger source and the amount of
    trigger delay.

    To trigger the acquisition, use :py:meth:`niscope.Session.send_software_trigger_edge`.

    

    .. note:: Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.



    :param trigger_source:


        Specifies the trigger source. Refer to :py:data:`niscope.Session.trigger_source`
        for defined values.

        


    :type trigger_source: str
    :param low_level:


        Passes the voltage threshold you want the digitizer to use for low
        triggering.

        


    :type low_level: float
    :param high_level:


        Passes the voltage threshold you want the digitizer to use for high
        triggering.

        


    :type high_level: float
    :param window_mode:


        Specifies whether you want the trigger to occur when the signal enters
        or leaves a window.

        


    :type window_mode: :py:data:`niscope.TriggerWindowMode`
    :param trigger_coupling:


        Applies coupling and filtering options to the trigger signal. Refer to
        :py:data:`niscope.Session.trigger_coupling` for more information.

        


    :type trigger_coupling: :py:data:`niscope.TriggerCoupling`
    :param holdoff:


        The length of time the digitizer waits after detecting a trigger before
        enabling NI-SCOPE to detect another trigger. Refer to
        :py:data:`niscope.Session.trigger_holdoff` for more information.

        


    :type holdoff: float in seconds or datetime.timedelta
    :param delay:


        How long the digitizer waits after receiving the trigger to start
        acquiring data. Refer to :py:data:`niscope.Session.trigger_delay_time` for more
        information.

        


    :type delay: float in seconds or datetime.timedelta

.. py:method:: configure_vertical(range, coupling, offset=0.0, probe_attenuation=1.0, enabled=True)

    Configures the most commonly configured properties of the digitizer
    vertical subsystem, such as the range, offset, coupling, probe
    attenuation, and the channel.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].configure_vertical(range, coupling, offset=0.0, probe_attenuation=1.0, enabled=True)


    :param range:


        Specifies the vertical range Refer to :py:data:`niscope.Session.vertical_range` for
        more information.

        


    :type range: float
    :param coupling:


        Specifies how to couple the input signal. Refer to
        :py:data:`niscope.Session.vertical_coupling` for more information.

        


    :type coupling: :py:data:`niscope.VerticalCoupling`
    :param offset:


        Specifies the vertical offset. Refer to :py:data:`niscope.Session.vertical_offset`
        for more information.

        


    :type offset: float
    :param probe_attenuation:


        Specifies the probe attenuation. Refer to
        :py:data:`niscope.Session.probe_attenuation` for valid values.

        


    :type probe_attenuation: float
    :param enabled:


        Specifies whether the channel is enabled for acquisition. Refer to
        :py:data:`niscope.Session.channel_enabled` for more information.

        


    :type enabled: bool

.. py:method:: disable()

    Aborts any current operation, opens data channel relays, and releases
    RTSI and PFI lines.

    



.. py:method:: fetch(num_samples=None, relative_to=niscope.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=datetime.timedelta(seconds=5.0))

    Returns the waveform from a previously initiated acquisition that the
    digitizer acquires for the specified channel. This method returns
    scaled voltage waveforms.

    This method may return multiple waveforms depending on the number of
    channels, the acquisition type, and the number of records you specify.

    

    .. note:: Some functionality, such as time stamping, is not supported in all digitizers.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].fetch(num_samples=None, relative_to=niscope.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=datetime.timedelta(seconds=5.0))


    :param num_samples:


        The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the method raises.

        


    :type num_samples: int
    :param relative_to:


        Position to start fetching within one record.

        


    :type relative_to: :py:data:`niscope.FetchRelativeTo`
    :param offset:


        Offset in samples to start fetching data within each record. The offset can be positive or negative.

        


    :type offset: int
    :param record_number:


        Zero-based index of the first record to fetch.

        


    :type record_number: int
    :param num_records:


        Number of records to fetch. Use -1 to fetch all configured records.

        


    :type num_records: int
    :param timeout:


        The time to wait for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 seconds for this parameter implies infinite timeout.

        


    :type timeout: float or datetime.timedelta

    :rtype: list of WaveformInfo
    :return:


            Returns an array of classes with the following timing and scaling information about each waveform:

            -  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform
            -  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
            -  **x_increment** (float) the time between points in the acquired waveform in seconds
            -  **channel** (str) channel name this waveform was asquire from
            -  **record** (int) record number of this waveform
            -  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:

                .. math::

                    voltage = binary data * gain factor + offset

            -  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:

                .. math::

                    voltage = binary data * gain factor + offset

            - **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired

            



.. py:method:: fetch_into(waveform, relative_to=niscope.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=datetime.timedelta(seconds=5.0))

    Returns the waveform from a previously initiated acquisition that the
    digitizer acquires for the specified channel. This method returns
    scaled voltage waveforms.

    This method may return multiple waveforms depending on the number of
    channels, the acquisition type, and the number of records you specify.

    

    .. note:: Some functionality, such as time stamping, is not supported in all digitizers.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].fetch(waveform, relative_to=niscope.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=datetime.timedelta(seconds=5.0))


    :param waveform:


        numpy array of the appropriate type and size the should be acquired as a 1D array. Size should be **num_samples** times number of waveforms. Call :py:meth:`niscope.Session._actual_num_wfms` to determine the number of waveforms.

        Types supported are

        - `numpy.float64`
        - `numpy.int8`
        - `numpy.in16`
        - `numpy.int32`

        Example:

        .. code-block:: python

            waveform = numpy.ndarray(num_samples * session.actual_num_wfms(), dtype=numpy.float64)
            wfm_info = session['0,1'].fetch_into(num_samples, waveform, timeout=5.0)

        


    :type waveform: array.array("d")
    :param relative_to:


        Position to start fetching within one record.

        


    :type relative_to: :py:data:`niscope.FetchRelativeTo`
    :param offset:


        Offset in samples to start fetching data within each record.The offset can be positive or negative.

        


    :type offset: int
    :param record_number:


        Zero-based index of the first record to fetch.

        


    :type record_number: int
    :param num_records:


        Number of records to fetch. Use -1 to fetch all configured records.

        


    :type num_records: int
    :param timeout:


        The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout.

        


    :type timeout: float

    :rtype: list of WaveformInfo
    :return:


            Returns an array of classed with the following timing and scaling information about each waveform:

            -  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform
            -  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
            -  **x_increment** (float) the time between points in the acquired waveform in seconds
            -  **channel** (str) channel name this waveform was asquire from
            -  **record** (int) record number of this waveform
            -  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:

                .. math::

                    voltage = binary data * gain factor + offset

            -  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:

                .. math::

                    voltage = binary data * gain factor + offset

            - **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired

            



.. py:method:: get_equalization_filter_coefficients()

    Retrieves the custom coefficients for the equalization FIR filter on the device. This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should be between +1 and –1.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].get_equalization_filter_coefficients()


.. py:method:: probe_compensation_signal_start()

    Starts the 1 kHz square wave output on PFI 1 for probe compensation.

    



.. py:method:: probe_compensation_signal_stop()

    Stops the 1 kHz square wave output on PFI 1 for probe compensation.

    



.. py:method:: read(num_samples=None, relative_to=niscope.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=datetime.timedelta(seconds=5.0))

    Initiates an acquisition, waits for it to complete, and retrieves the
    data. The process is similar to calling :py:meth:`niscope.Session._initiate_acquisition`,
    :py:meth:`niscope.Session.acquisition_status`, and :py:meth:`niscope.Session.fetch`. The only difference is
    that with :py:meth:`niscope.Session.read`, you enable all channels specified with
    **channelList** before the acquisition; in the other method, you enable
    the channels with :py:meth:`niscope.Session.configure_vertical`.

    This method may return multiple waveforms depending on the number of
    channels, the acquisition type, and the number of records you specify.

    

    .. note:: Some functionality, such as time stamping, is not supported in all digitizers.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].read(num_samples=None, relative_to=niscope.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=datetime.timedelta(seconds=5.0))


    :param num_samples:


        The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the method raises.

        


    :type num_samples: int
    :param relative_to:


        Position to start fetching within one record.

        


    :type relative_to: :py:data:`niscope.FetchRelativeTo`
    :param offset:


        Offset in samples to start fetching data within each record. The offset can be positive or negative.

        


    :type offset: int
    :param record_number:


        Zero-based index of the first record to fetch.

        


    :type record_number: int
    :param num_records:


        Number of records to fetch. Use -1 to fetch all configured records.

        


    :type num_records: int
    :param timeout:


        The time to wait for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 seconds for this parameter implies infinite timeout.

        


    :type timeout: float or datetime.timedelta

    :rtype: list of WaveformInfo
    :return:


            Returns an array of classes with the following timing and scaling information about each waveform:

            -  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform
            -  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
            -  **x_increment** (float) the time between points in the acquired waveform in seconds
            -  **channel** (str) channel name this waveform was asquire from
            -  **record** (int) record number of this waveform
            -  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:

                .. math::

                    voltage = binary data * gain factor + offset

            -  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:

                .. math::

                    voltage = binary data * gain factor + offset

            - **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired

            



.. py:method:: reset()

    Stops the acquisition, releases routes, and all session properties are
    reset to their `default
    states <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cviattribute_defaults)>`__.

    



.. py:method:: reset_device()

    Performs a hard reset of the device. Acquisition stops, all routes are
    released, RTSI and PFI lines are tristated, hardware is configured to
    its default state, and all session properties are reset to their default
    state.

    -  `Thermal Shutdown <digitizers.chm::/Thermal_Shutdown.html>`__

    



.. py:method:: reset_with_defaults()

    Performs a software reset of the device, returning it to the default
    state and applying any initial default settings from the IVI
    Configuration Store.

    



.. py:method:: self_cal(option=niscope.Option.SELF_CALIBRATE_ALL_CHANNELS)

    Self-calibrates most NI digitizers, including all SMC-based devices and
    most Traditional NI-DAQ (Legacy) devices. To verify that your digitizer
    supports self-calibration, refer to `Features Supported by
    Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__.

    For SMC-based digitizers, if the self-calibration is performed
    successfully in a regular session, the calibration constants are
    immediately stored in the self-calibration area of the EEPROM. If the
    self-calibration is performed in an external calibration session, the
    calibration constants take effect immediately for the duration of the
    session. However, they are not stored in the EEPROM until
    :py:meth:`niscope.Session.CalEnd` is called with **action** set to
    :py:data:`~niscope.NISCOPE_VAL_ACTION_STORE` and no errors occur.

    

    .. note:: One or more of the referenced methods are not in the Python API for this driver.

    .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].self_cal(option=niscope.Option.SELF_CALIBRATE_ALL_CHANNELS)


    :param option:


        The calibration option. Use VI_NULL for a normal self-calibration
        operation or :py:data:`~niscope.NISCOPE_VAL_CAL_RESTORE_EXTERNAL_CALIBRATION` to
        restore the previous calibration.

        

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type option: :py:data:`niscope.Option`

.. py:method:: self_test()

    Runs the instrument self-test routine and returns the test result(s). Refer to the
    device-specific help topics for an explanation of the message contents.

    Raises `SelfTestError` on self test failure. Properties on exception object:

    - code - failure code from driver
    - message - status message from driver

    +----------------+------------------+
    | Self-Test Code | Description      |
    +================+==================+
    | 0              | Passed self-test |
    +----------------+------------------+
    | 1              | Self-test failed |
    +----------------+------------------+



.. py:method:: send_software_trigger_edge(which_trigger)

    Sends the selected trigger to the digitizer. Call this method if you
    called :py:meth:`niscope.Session.configure_trigger_software` when you want the Reference
    trigger to occur. You can also call this method to override a misused
    edge, digital, or hysteresis trigger. If you have configured
    :py:data:`niscope.Session.acq_arm_source`, :py:data:`niscope.Session.arm_ref_trig_src`, or
    :py:data:`niscope.Session.adv_trig_src`, call this method when you want to send
    the corresponding trigger to the digitizer.

    



    :param which_trigger:


        Specifies the type of trigger to send to the digitizer.

        **Defined Values**

        | :py:data:`~niscope.WhichTrigger.START` (0L)
        |  :py:data:`~niscope.WhichTrigger.ARM_REFERENCE` (1L)
        | :py:data:`~niscope.WhichTrigger.REFERENCE` (2L)
        | :py:data:`~niscope.WhichTrigger.ADVANCE` (3L)

        


    :type which_trigger: :py:data:`niscope.WhichTrigger`


