niscope.Session methods
=======================

.. py:currentmodule:: niscope

.. function:: abort()

    Aborts an acquisition and returns the digitizer to the Idle state. Call
    this function if the digitizer times out waiting for a trigger.

    



.. function:: acquisition_status()

    Returns status information about the acquisition to the **status**
    output parameter.

    



    :rtype: :py:data:`niscope.AcquisitionStatus`
    :return:


            Returns whether the acquisition is complete, in progress, or unknown.

            **Defined Values**

            NISCOPE\_VAL\_ACQ\_COMPLETE

            NISCOPE\_VAL\_ACQ\_IN\_PROGRESS

            NISCOPE\_VAL\_ACQ\_STATUS\_UNKNOWN

            



.. function:: add_waveform_processing(meas_function)

    Adds one measurement to the list of processing steps that are completed
    before the measurement. The processing is added on a per channel basis,
    and the processing measurements are completed in the same order they are
    registered. All measurement library parameters—the attributes starting
    with :py:data:`niscope.MEAS`—are cached at the time of registering the
    processing, and this set of parameters is used during the processing
    step. The processing measurements are streamed, so the result of the
    first processing step is used as the input for the next step. The
    processing is done before any other measurements.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].add_waveform_processing(meas_function)


    :param meas_function:


        The `array
        measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
        to add.

        


    :type meas_function: :py:data:`niscope.ArrayMeasurement`

.. function:: auto_setup()

    Automatically configures the instrument. When you call this function,
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

    +--------------------+
    | **General**        |
    +--------------------+
    | Acquisition mode   |
    +--------------------+
    | Reference clock    |
    +--------------------+
    | **Vertical**       |
    +--------------------+
    | Vertical coupling  |
    +--------------------+
    | Vertical bandwidth |
    +--------------------+
    | Vertical range     |
    +--------------------+
    | Vertical offset    |
    +--------------------+
    | Probe attenuation  |
    +--------------------+
    | Input impedance    |
    +--------------------+
    | **Horizontal**     |
    +--------------------+
    | Sample rate        |
    +--------------------+
    | Min record length  |
    +--------------------+
    | Enforce realtime   |
    +--------------------+
    | Number of Records  |
    +--------------------+
    | **Triggering**     |
    +--------------------+
    | Trigger type       |
    +--------------------+
    | Trigger channel    |
    +--------------------+
    | Trigger slope      |
    +--------------------+
    | Trigger coupling   |
    +--------------------+
    | Reference position |
    +--------------------+
    | Trigger level      |
    +--------------------+
    | Trigger delay      |
    +--------------------+
    | Trigger holdoff    |
    +--------------------+
    | Trigger output     |
    +--------------------+



.. function:: cal_self_calibrate(option=niscope.Option.SELF_CALIBRATE_ALL_CHANNELS)

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
    :py:func:`niscope.CalEnd` is called with **action** set to
    NISCOPE\_VAL\_ACTION\_STORE and no errors occur.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].cal_self_calibrate(option=niscope.Option.SELF_CALIBRATE_ALL_CHANNELS)


    :param option:


        The calibration option. Use VI\_NULL for a normal self-calibration
        operation or NISCOPE\_VAL\_CAL\_RESTORE\_EXTERNAL\_CALIBRATION to
        restore the previous calibration.

        


    :type option: :py:data:`niscope.Option`

.. function:: clear_waveform_measurement_stats(clearable_measurement_function=niscope.ClearableMeasurement.ALL_MEASUREMENTS)

    Clears the waveform stats on the channel and measurement you specify. If
    you want to clear all of the measurements, use
    NISCOPE\_VAL\_ALL\_MEASUREMENTS in the **clearableMeasurementFunction**
    parameter.

    Every time a measurement is called, the statistics information is
    updated, including the min, max, mean, standard deviation, and number of
    updates. This information is fetched with
    :py:func:`niscope.fetch_measurement_stats`. The multi-acquisition array measurements
    are also cleared with this function.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].clear_waveform_measurement_stats(clearable_measurement_function=niscope.ClearableMeasurement.ALL_MEASUREMENTS)


    :param clearable_measurement_function:


        The `scalar
        measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
        or `array
        measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
        to clear the stats for.

        


    :type clearable_measurement_function: :py:data:`niscope.ClearableMeasurement`

.. function:: clear_waveform_processing()

    Clears the list of processing steps assigned to the given channel. The
    processing is added using the :py:func:`niscope.add_waveform_processing` function,
    where the processing steps are completed in the same order in which they
    are registered. The processing measurements are streamed, so the result
    of the first processing step is used as the input for the next step. The
    processing is also done before any other measurements.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].clear_waveform_processing()


.. function:: commit()

    Commits to hardware all the parameter settings associated with the task.
    Use this function if you want a parameter change to be immediately
    reflected in the hardware. This function is not supported for
    Traditional NI-DAQ (Legacy) devices.

    



.. function:: configure_chan_characteristics(input_impedance, max_input_frequency)

    Configures the attributes that control the electrical characteristics of
    the channel—the input impedance and the bandwidth.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].configure_chan_characteristics(input_impedance, max_input_frequency)


    :param input_impedance:


        The input impedance for the channel; NI-SCOPE sets
        :py:data:`niscope.INPUT\_IMPEDANCE` to this value.

        


    :type input_impedance: :py:data:`niscope.InputImpedance`
    :param max_input_frequency:


        The bandwidth for the channel; NI-SCOPE sets
        :py:data:`niscope.MAX\_INPUT\_FREQUENCY` to this value. Pass 0 for this
        value to use the hardware default bandwidth. Pass –1 for this value to
        achieve full bandwidth.

        


    :type max_input_frequency: float

.. function:: configure_equalization_filter_coefficients(coefficients)

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

            session['0,1'].configure_equalization_filter_coefficients(coefficients)


    :param coefficients:


        The custom coefficients for the equalization FIR filter on the device.
        These coefficients should be between +1 and –1. You can obtain the
        number of coefficients from the
        `:py:data:`niscope.EQUALIZATION\_NUM\_COEFFICIENTS` <cviNISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS.html>`__
        attribute. The
        `:py:data:`niscope.EQUALIZATION\_FILTER\_ENABLED` <cviNISCOPE_ATTR_EQUALIZATION_FILTER_ENABLED.html>`__
        attribute must be set to TRUE to enable the filter.

        


    :type coefficients: list of float

.. function:: configure_horizontal_timing(min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime)

    Configures the common properties of the horizontal subsystem for a
    multirecord acquisition in terms of minimum sample rate.

    



    :param min_sample_rate:


        The sampling rate for the acquisition. Refer to
        :py:data:`niscope.MIN\_SAMPLE\_RATE` for more information.

        


    :type min_sample_rate: float
    :param min_num_pts:


        The minimum number of points you need in the record for each channel;
        call :py:func:`niscope.ActualRecordLength` to obtain the actual record length
        used.

        Valid Values: Greater than 1; limited by available memory

        


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

        Default value: VI\_TRUE

        **Defined Values**

        VI\_TRUE—Allow real-time acquisitions only

        VI\_FALSE—Allow real-time and equivalent-time acquisitions

        


    :type enforce_realtime: bool

.. function:: configure_ref_levels(low=10.0, mid=50.0, high=90.0)

    This function is included for compliance with the IviScope Class
    Specification.

    Configures the reference levels for all channels of the digitizer. The
    levels may be set on a per channel basis by setting
    :py:data:`niscope.MEAS\_CHAN\_HIGH\_REF\_LEVEL`,
    :py:data:`niscope.MEAS\_CHAN\_LOW\_REF\_LEVEL`, and
    :py:data:`niscope.MEAS\_CHAN\_MID\_REF\_LEVEL`

    This function configures the reference levels for waveform measurements.
    Call this function before calling :py:func:`niscope.fetch_measurement` to take a
    rise time, fall time, width negative, width positive, duty cycle
    negative, or duty cycle positive measurement.

    



    :param low:


        Pass the low reference you want the digitizer to use for waveform
        measurements.

        Units: Either a percentage or voltage based on
        :py:data:`niscope.MEAS\_REF\_LEVEL\_UNITS`. A percentage is calculated with
        the voltage low and voltage high measurements representing 0% and 100%,
        respectively.

        Default Value: 10.0

        


    :type low: float
    :param mid:


        Pass the mid reference you want the digitizer to use for waveform
        measurements.

        Units: Either a percentage or voltage based on
        :py:data:`niscope.MEAS\_REF\_LEVEL\_UNITS`. A percentage is calculated with
        the voltage low and voltage high measurements representing 0% and 100%,
        respectively.

        Default Value: 50.0

        


    :type mid: float
    :param high:


        Pass the high reference you want the digitizer to use for waveform
        measurements.

        Units: Either a percentage or voltage based on
        :py:data:`niscope.MEAS\_REF\_LEVEL\_UNITS`. A percentage is calculated with
        the voltage low and voltage high measurements representing 0% and 100%,
        respectively.

        Default Value: 90.0

        


    :type high: float

.. function:: configure_trigger_digital(trigger_source, slope=niscope.TriggerSlope.POSITIVE, holdoff=0.0, delay=0.0)

    Configures the common properties of a digital trigger.

    When you initiate an acquisition, the digitizer waits for the start
    trigger, which is configured through the :py:data:`niscope.ACQ\_ARM\_SOURCE`
    (Start Trigger Source) attribute. The default is immediate. Upon
    receiving the start trigger the digitizer begins sampling pretrigger
    points. After the digitizer finishes sampling pretrigger points, the
    digitizer waits for a reference (stop) trigger that you specify with a
    function such as this one. Upon receiving the reference trigger the
    digitizer finishes the acquisition after completing posttrigger
    sampling. With each Configure Trigger function, you specify
    configuration parameters such as the trigger source and the amount of
    trigger delay.

    

    .. note:: For multirecord acquisitions, all records after the first record are
        started by using the Advance Trigger Source. The default is immediate.

        You can adjust the amount of pre-trigger and post-trigger samples using
        the reference position parameter on the
        :py:func:`niscope.configure_horizontal_timing` function. The default is half of the
        record length.

        Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.

        Digital triggering is not supported in RIS mode.



    :param trigger_source:


        Specifies the trigger source. Refer to :py:data:`niscope.TRIGGER\_SOURCE`
        for defined values.

        


    :type trigger_source: string
    :param slope:


        Specifies whether you want a rising edge or a falling edge to trigger
        the digitizer. Refer to :py:data:`niscope.TRIGGER\_SLOPE` for more
        information.

        


    :type slope: :py:data:`niscope.TriggerSlope`
    :param holdoff:


        The length of time the digitizer waits after detecting a trigger before
        enabling NI-SCOPE to detect another trigger. Refer to
        :py:data:`niscope.TRIGGER\_HOLDOFF` for more information.

        


    :type holdoff: float
    :param delay:


        How long the digitizer waits after receiving the trigger to start
        acquiring data. Refer to :py:data:`niscope.TRIGGER\_DELAY\_TIME` for more
        information.

        


    :type delay: float

.. function:: configure_trigger_edge(trigger_source, trigger_coupling, level=0.0, slope=niscope.TriggerSlope.POSITIVE, holdoff=0.0, delay=0.0)

    Configures common properties for analog edge triggering.

    When you initiate an acquisition, the digitizer waits for the start
    trigger, which is configured through the :py:data:`niscope.ACQ\_ARM\_SOURCE`
    (Start Trigger Source) attribute. The default is immediate. Upon
    receiving the start trigger the digitizer begins sampling pretrigger
    points. After the digitizer finishes sampling pretrigger points, the
    digitizer waits for a reference (stop) trigger that you specify with a
    function such as this one. Upon receiving the reference trigger the
    digitizer finishes the acquisition after completing posttrigger
    sampling. With each Configure Trigger function, you specify
    configuration parameters such as the trigger source and the amount of
    trigger delay.

    

    .. note:: Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.



    :param trigger_source:


        Specifies the trigger source. Refer to :py:data:`niscope.TRIGGER\_SOURCE`
        for defined values.

        


    :type trigger_source: string
    :param trigger_coupling:


        Applies coupling and filtering options to the trigger signal. Refer to
        :py:data:`niscope.TRIGGER\_COUPLING` for more information.

        


    :type trigger_coupling: :py:data:`niscope.TriggerCoupling`
    :param level:


        The voltage threshold for the trigger. Refer to
        :py:data:`niscope.TRIGGER\_LEVEL` for more information.

        


    :type level: float
    :param slope:


        Specifies whether you want a rising edge or a falling edge to trigger
        the digitizer. Refer to :py:data:`niscope.TRIGGER\_SLOPE` for more
        information.

        


    :type slope: :py:data:`niscope.TriggerSlope`
    :param holdoff:


        The length of time the digitizer waits after detecting a trigger before
        enabling NI-SCOPE to detect another trigger. Refer to
        :py:data:`niscope.TRIGGER\_HOLDOFF` for more information.

        


    :type holdoff: float
    :param delay:


        How long the digitizer waits after receiving the trigger to start
        acquiring data. Refer to :py:data:`niscope.TRIGGER\_DELAY\_TIME` for more
        information.

        


    :type delay: float

.. function:: configure_trigger_hysteresis(trigger_source, trigger_coupling, level=0.0, hysteresis=0.05, slope=niscope.TriggerSlope.POSITIVE, holdoff=0.0, delay=0.0)

    Configures common properties for analog hysteresis triggering. This kind
    of trigger specifies an additional value, specified in the
    **hysteresis** parameter, that a signal must pass through before a
    trigger can occur. This additional value acts as a kind of buffer zone
    that keeps noise from triggering an acquisition.

    When you initiate an acquisition, the digitizer waits for the start
    trigger, which is configured through the
    :py:data:`niscope.ACQ\_ARM\_SOURCE`. The default is immediate. Upon
    receiving the start trigger the digitizer begins sampling pretrigger
    points. After the digitizer finishes sampling pretrigger points, the
    digitizer waits for a reference (stop) trigger that you specify with a
    function such as this one. Upon receiving the reference trigger the
    digitizer finishes the acquisition after completing posttrigger
    sampling. With each Configure Trigger function, you specify
    configuration parameters such as the trigger source and the amount of
    trigger delay.

    

    .. note:: Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.



    :param trigger_source:


        Specifies the trigger source. Refer to :py:data:`niscope.TRIGGER\_SOURCE`
        for defined values.

        


    :type trigger_source: string
    :param trigger_coupling:


        Applies coupling and filtering options to the trigger signal. Refer to
        :py:data:`niscope.TRIGGER\_COUPLING` for more information.

        


    :type trigger_coupling: :py:data:`niscope.TriggerCoupling`
    :param level:


        The voltage threshold for the trigger. Refer to
        :py:data:`niscope.TRIGGER\_LEVEL` for more information.

        


    :type level: float
    :param hysteresis:


        The size of the hysteresis window on either side of the **level** in
        volts; the digitizer triggers when the trigger signal passes through the
        hysteresis value you specify with this parameter, has the slope you
        specify with **slope**, and passes through the **level**. Refer to
        :py:data:`niscope.TRIGGER\_HYSTERESIS` for defined values.

        


    :type hysteresis: float
    :param slope:


        Specifies whether you want a rising edge or a falling edge to trigger
        the digitizer. Refer to :py:data:`niscope.TRIGGER\_SLOPE` for more
        information.

        


    :type slope: :py:data:`niscope.TriggerSlope`
    :param holdoff:


        The length of time the digitizer waits after detecting a trigger before
        enabling NI-SCOPE to detect another trigger. Refer to
        :py:data:`niscope.TRIGGER\_HOLDOFF` for more information.

        


    :type holdoff: float
    :param delay:


        How long the digitizer waits after receiving the trigger to start
        acquiring data. Refer to :py:data:`niscope.TRIGGER\_DELAY\_TIME` for more
        information.

        


    :type delay: float

.. function:: configure_trigger_immediate()

    Configures common properties for immediate triggering. Immediate
    triggering means the digitizer triggers itself.

    When you initiate an acquisition, the digitizer waits for a trigger. You
    specify the type of trigger that the digitizer waits for with a
    Configure Trigger function, such as :py:func:`niscope.configure_trigger_immediate`.

    



.. function:: configure_trigger_software(holdoff=0.0, delay=0.0)

    Configures common properties for software triggering.

    When you initiate an acquisition, the digitizer waits for the start
    trigger, which is configured through the :py:data:`niscope.ACQ\_ARM\_SOURCE`
    (Start Trigger Source) attribute. The default is immediate. Upon
    receiving the start trigger the digitizer begins sampling pretrigger
    points. After the digitizer finishes sampling pretrigger points, the
    digitizer waits for a reference (stop) trigger that you specify with a
    function such as this one. Upon receiving the reference trigger the
    digitizer finishes the acquisition after completing posttrigger
    sampling. With each Configure Trigger function, you specify
    configuration parameters such as the trigger source and the amount of
    trigger delay.

    To trigger the acquisition, use :py:func:`niscope.send_software_trigger_edge`.

    

    .. note:: Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.



    :param holdoff:


        The length of time the digitizer waits after detecting a trigger before
        enabling NI-SCOPE to detect another trigger. Refer to
        :py:data:`niscope.TRIGGER\_HOLDOFF` for more information.

        


    :type holdoff: float
    :param delay:


        How long the digitizer waits after receiving the trigger to start
        acquiring data. Refer to :py:data:`niscope.TRIGGER\_DELAY\_TIME` for more
        information.

        


    :type delay: float

.. function:: configure_trigger_video(trigger_source, signal_format, event, polarity, trigger_coupling, enable_dc_restore=False, line_number=1, holdoff=0.0, delay=0.0)

    Configures the common properties for video triggering, including the
    signal format, TV event, line number, polarity, and enable DC restore. A
    video trigger occurs when the digitizer finds a valid video signal sync.

    When you initiate an acquisition, the digitizer waits for the start
    trigger, which is configured through the :py:data:`niscope.ACQ\_ARM\_SOURCE`
    (Start Trigger Source) attribute. The default is immediate. Upon
    receiving the start trigger the digitizer begins sampling pretrigger
    points. After the digitizer finishes sampling pretrigger points, the
    digitizer waits for a reference (stop) trigger that you specify with a
    function such as this one. Upon receiving the reference trigger the
    digitizer finishes the acquisition after completing posttrigger
    sampling. With each Configure Trigger function, you specify
    configuration parameters such as the trigger source and the amount of
    trigger delay.

    

    .. note:: Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.



    :param trigger_source:


        Specifies the trigger source. Refer to :py:data:`niscope.TRIGGER\_SOURCE`
        for defined values.

        


    :type trigger_source: string
    :param signal_format:


        Specifies the type of video signal sync the digitizer should look for.
        Refer to :py:data:`niscope.TV\_TRIGGER\_SIGNAL\_FORMAT` for more
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
        :py:data:`niscope.TRIGGER\_COUPLING` for more information.

        


    :type trigger_coupling: :py:data:`niscope.TriggerCoupling`
    :param enable_dc_restore:


        Offsets each video line so the clamping level (the portion of the video
        line between the end of the color burst and the beginning of the active
        image) is moved to zero volt. Refer to
        :py:data:`niscope.ENABLE\_DC\_RESTORE` for defined values.

        


    :type enable_dc_restore: bool
    :param line_number:


        Selects the line number to trigger on. The line number range covers an
        entire frame and is referenced as shown on `Vertical Blanking and
        Synchronization
        Signal <REPLACE_DRIVER_SPECIFIC_URL_1(gray_scale_image)>`__. Refer to
        :py:data:`niscope.TV\_TRIGGER\_LINE\_NUMBER` for more information.

        Default value: 1

        


    :type line_number: int
    :param holdoff:


        The length of time the digitizer waits after detecting a trigger before
        enabling NI-SCOPE to detect another trigger. Refer to
        :py:data:`niscope.TRIGGER\_HOLDOFF` for more information.

        


    :type holdoff: float
    :param delay:


        How long the digitizer waits after receiving the trigger to start
        acquiring data. Refer to :py:data:`niscope.TRIGGER\_DELAY\_TIME` for more
        information.

        


    :type delay: float

.. function:: configure_trigger_window(trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff=0.0, delay=0.0)

    Configures common properties for analog window triggering. A window
    trigger occurs when a signal enters or leaves a window you specify with
    the **high level** or **low level** parameters.

    When you initiate an acquisition, the digitizer waits for the start
    trigger, which is configured through the :py:data:`niscope.ACQ\_ARM\_SOURCE`
    (Start Trigger Source) attribute. The default is immediate. Upon
    receiving the start trigger the digitizer begins sampling pretrigger
    points. After the digitizer finishes sampling pretrigger points, the
    digitizer waits for a reference (stop) trigger that you specify with a
    function such as this one. Upon receiving the reference trigger the
    digitizer finishes the acquisition after completing posttrigger
    sampling. With each Configure Trigger function, you specify
    configuration parameters such as the trigger source and the amount of
    trigger delay.

    To trigger the acquisition, use :py:func:`niscope.send_software_trigger_edge`.

    

    .. note:: Some features are not supported by all digitizers. Refer to `Features
        Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.



    :param trigger_source:


        Specifies the trigger source. Refer to :py:data:`niscope.TRIGGER\_SOURCE`
        for defined values.

        


    :type trigger_source: string
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
        :py:data:`niscope.TRIGGER\_COUPLING` for more information.

        


    :type trigger_coupling: :py:data:`niscope.TriggerCoupling`
    :param holdoff:


        The length of time the digitizer waits after detecting a trigger before
        enabling NI-SCOPE to detect another trigger. Refer to
        :py:data:`niscope.TRIGGER\_HOLDOFF` for more information.

        


    :type holdoff: float
    :param delay:


        How long the digitizer waits after receiving the trigger to start
        acquiring data. Refer to :py:data:`niscope.TRIGGER\_DELAY\_TIME` for more
        information.

        


    :type delay: float

.. function:: configure_vertical(range, coupling, offset=0.0, probe_attenuation=1.0, enabled=True)

    Configures the most commonly configured attributes of the digitizer
    vertical subsystem, such as the range, offset, coupling, probe
    attenuation, and the channel.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].configure_vertical(range, coupling, offset=0.0, probe_attenuation=1.0, enabled=True)


    :param range:


        Specifies the vertical range Refer to :py:data:`niscope.VERTICAL\_RANGE` for
        more information.

        


    :type range: float
    :param coupling:


        Specifies how to couple the input signal. Refer to
        :py:data:`niscope.VERTICAL\_COUPLING` for more information.

        


    :type coupling: :py:data:`niscope.VerticalCoupling`
    :param offset:


        Specifies the vertical offset. Refer to :py:data:`niscope.VERTICAL\_OFFSET`
        for more information.

        


    :type offset: float
    :param probe_attenuation:


        Specifies the probe attenuation. Refer to
        :py:data:`niscope.PROBE\_ATTENUATION` for valid values.

        


    :type probe_attenuation: float
    :param enabled:


        Specifies whether the channel is enabled for acquisition. Refer to
        :py:data:`niscope.CHANNEL\_ENABLED` for more information.

        


    :type enabled: bool

.. function:: disable()

    Aborts any current operation, opens data channel relays, and releases
    RTSI and PFI lines.

    



.. function:: export_signal(signal, output_terminal, signal_identifier='None')

    Configures the digitizer to generate a signal that other devices can
    detect when configured for digital triggering or sharing clocks. The
    **signal** parameter specifies what condition causes the digitizer to
    generate the signal. The **outputTerminal** parameter specifies where to
    send the signal on the hardware (such as a PFI connector or RTSI line).

    In cases where multiple instances of a particular signal exist, use the
    **signalIdentifier** input to specify which instance to control. For
    normal signals, only one instance exists and you should leave this
    parameter set to the empty string. You can call this function multiple
    times and set each available line to a different signal.

    To unprogram a specific line on device, call this function with the
    signal you no longer want to export and set **outputTerminal** to
    NISCOPE\_VAL\_NONE.

    

    .. note:: This function replaces :py:func:`niscope.ConfigureTriggerOutput`.



    :param signal:


        signal (clock, trigger, or event) to export.

        **Defined Values**

        +-------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
        | NISCOPE\_VAL\_REF\_TRIGGER                | (1)   | Generate a pulse when detecting the Stop/Reference trigger.                                     |
        +-------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
        | NISCOPE\_VAL\_START\_TRIGGER              | (2)   | Generate a pulse when detecting a Start trigger.                                                |
        +-------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
        | NISCOPE\_VAL\_END\_OF\_ACQUISITION\_EVENT | (3)   | Generate a pulse when the acquisition finishes.                                                 |
        +-------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
        | NISCOPE\_VAL\_END\_OF\_RECORD\_EVENT      | (4)   | Generate a pulse at the end of the record.                                                      |
        +-------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
        | NISCOPE\_VAL\_ADVANCE\_TRIGGER            | (5)   | Generate a pulse when detecting an Advance trigger.                                             |
        +-------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
        | NISCOPE\_VAL\_READY\_FOR\_ADVANCE\_EVENT  | (6)   | Asserts when the digitizer is ready to advance to the next record.                              |
        +-------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
        | NISCOPE\_VAL\_READY\_FOR\_START\_EVENT    | (7)   | Asserts when the digitizer is initiated and ready to accept a Start trigger and begin sampling. |
        +-------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
        | NISCOPE\_VAL\_READY\_FOR\_REF\_EVENT      | (10)  | Asserts when the digitizer is ready to accept a Reference trigger.                              |
        +-------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
        | NISCOPE\_VAL\_REF\_CLOCK                  | (100) | Export the Reference clock for the digitizer to the specified terminal.                         |
        +-------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
        | NISCOPE\_VAL\_SAMPLE\_CLOCK               | (101) | Export the Sample clock for the digitizer to the specified terminal.                            |
        +-------------------------------------------+-------+-------------------------------------------------------------------------------------------------+
        | NISCOPE\_VAL\_5V\_OUT                     | (13)  | Exports a 5 V power supply.                                                                     |
        +-------------------------------------------+-------+-------------------------------------------------------------------------------------------------+


    :type signal: :py:data:`niscope.ExportableSignals`
    :param output_terminal:


        Identifies the hardware signal line on which the digital pulse is
        generated.

        **Defined Values**

        +-------------------------+--------------------+
        | NISCOPE\_VAL\_RTSI\_0   | ("VAL\_RTSI\_0")   |
        +-------------------------+--------------------+
        | NISCOPE\_VAL\_RTSI\_1   | ("VAL\_RTSI\_1")   |
        +-------------------------+--------------------+
        | NISCOPE\_VAL\_RTSI\_2   | ("VAL\_RTSI\_2")   |
        +-------------------------+--------------------+
        | NISCOPE\_VAL\_RTSI\_3   | ("VAL\_RTSI\_3")   |
        +-------------------------+--------------------+
        | NISCOPE\_VAL\_RTSI\_4   | ("VAL\_RTSI\_4")   |
        +-------------------------+--------------------+
        | NISCOPE\_VAL\_RTSI\_5   | ("VAL\_RTSI\_5")   |
        +-------------------------+--------------------+
        | NISCOPE\_VAL\_RTSI\_6   | ("VAL\_RTSI\_6")   |
        +-------------------------+--------------------+
        | NISCOPE\_VAL\_RTSI\_7   | ("VAL\_RTSI\_7")   |
        +-------------------------+--------------------+
        | NISCOPE\_VAL\_PXI\_STAR | ("VAL\_PXI\_STAR") |
        +-------------------------+--------------------+
        | NISCOPE\_VAL\_PFI\_0    | ("VAL\_PFI\_0")    |
        +-------------------------+--------------------+
        | NISCOPE\_VAL\_PFI\_1    | ("VAL\_PFI\_1")    |
        +-------------------------+--------------------+
        | NISCOPE\_VAL\_PFI\_2    | ("VAL\_PFI\_2")    |
        +-------------------------+--------------------+
        | NISCOPE\_VAL\_CLK\_OUT  | ("VAL\_CLK\_OUT")  |
        +-------------------------+--------------------+


    :type output_terminal: string
    :param signal_identifier:


        Describes the signal being exported.

        


    :type signal_identifier: string

.. function:: fetch_array_measurement(array_meas_function, meas_wfm_size, timeout=5.0)

    Obtains a waveform from the digitizer and returns the specified
    measurement array. This function may return multiple waveforms depending
    on the number of channels, the acquisition type, and the number of
    records you specify.

    

    .. note:: Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].fetch_array_measurement(array_meas_function, meas_wfm_size, timeout=5.0)


    :param array_meas_function:


        The `array
        measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
        to perform.

        


    :type array_meas_function: :py:data:`niscope.ArrayMeasurement`
    :param timeout:


        The time to wait in seconds for data to be acquired; using 0 for this
        parameter tells NI-SCOPE to fetch whatever is currently available. Using
        -1 for this parameter implies infinite timeout.

        


    :type timeout: float

    :rtype: tuple (meas_wfm, wfm_info)

        WHERE

        meas_wfm (list of float): 


            Returns an array whose length is the number of waveforms times
            **measWfmSize**; call :py:func:`niscope._actual_num_wfms` to determine the number of
            waveforms; call :py:func:`niscope._actual_meas_wfm_size` to determine the size of each
            waveform.

            NI-SCOPE returns this data sequentially, so all record 0 waveforms are
            first. For example, with channel list of 0, 1, you would have the
            following index values:

            index 0 = record 0, channel 0

            index *x* = record 0, channel 1

            index 2\ *x* = record 1, channel 0

            index 3\ *x* = record 1, channel 1

            Where *x* = the record length

            


        wfm_info (list of WaveformInfo): 


            Returns an array of structures with the following timing and scaling
            information about each waveform:

            -  **relativeInitialX**—the time (in seconds) from the trigger to the
               first sample in the fetched waveform
            -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
               sample. This timestamp is comparable between records and
               acquisitions; devices that do not support this parameter use 0 for
               this output.
            -  **xIncrement**—the time between points in the acquired waveform in
               seconds
            -  **actualSamples**—the actual number of samples fetched and placed in
               the waveform array
            -  **gain**—the gain factor of the given channel; useful for scaling
               binary data with the following formula:

            voltage = binary data × gain factor + offset

            -  **offset**—the offset factor of the given channel; useful for scaling
               binary data with the following formula:

            voltage = binary data × gain factor + offset

            Call :py:func:`niscope._actual_num_wfms` to determine the size of this array.

            



.. function:: fetch_into(num_samples, wfm, timeout=5.0)

    Returns the waveform from a previously initiated acquisition that the
    digitizer acquires for the specified channel. This function returns
    scaled voltage waveforms.

    This function may return multiple waveforms depending on the number of
    channels, the acquisition type, and the number of records you specify.

    

    .. note:: You can use :py:func:`niscope.read` instead of this function. :py:func:`niscope.read`
        starts an acquisition on all enabled channels, waits for the acquisition
        to complete, and returns the waveform for the specified channel.

        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].fetch(num_samples, wfm, timeout=5.0)


    :param num_samples:


        The maximum number of samples to fetch for each waveform. If the
        acquisition finishes with fewer points than requested, some devices
        return partial data if the acquisition finished, was aborted, or a
        timeout of 0 was used. If it fails to complete within the timeout
        period, the function returns an error.

        


    :type num_samples: int
    :param wfm:


        Returns an array whose length is the **numSamples** times number of
        waveforms. Call :py:func:`niscope.ActualNumwfms` to determine the number of
        waveforms.

        NI-SCOPE returns this data sequentially, so all record 0 waveforms are
        first. For example, with a channel list of 0,1, you would have the
        following index values:

        index 0 = record 0, channel 0

        index *x* = record 0, channel 1

        index 2\ *x* = record 1, channel 0

        index 3\ *x* = record 1, channel 1

        Where *x* = the record length

        


    :type wfm: list of float
    :param timeout:


        The time to wait in seconds for data to be acquired; using 0 for this
        parameter tells NI-SCOPE to fetch whatever is currently available. Using
        -1 for this parameter implies infinite timeout.

        


    :type timeout: float

    :rtype: list of WaveformInfo
    :return:


            Returns an array of structures with the following timing and scaling
            information about each waveform:

            -  **relativeInitialX**—the time (in seconds) from the trigger to the
            first sample in the fetched waveform
            -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
            sample. This timestamp is comparable between records and
            acquisitions; devices that do not support this parameter use 0 for
            this output.
            -  **xIncrement**—the time between points in the acquired waveform in
            seconds
            -  **actualSamples**—the actual number of samples fetched and placed in
            the waveform array
            -  **gain**—the gain factor of the given channel; useful for scaling
            binary data with the following formula:

            voltage = binary data × gain factor + offset

            -  **offset**—the offset factor of the given channel; useful for scaling
            binary data with the following formula:

            voltage = binary data × gain factor + offset

            Call :py:func:`niscope._actual_num_wfms` to determine the size of this array.

            



.. function:: fetch(num_samples, timeout=5.0)

    Returns the waveform from a previously initiated acquisition that the
    digitizer acquires for the specified channel. This function returns
    scaled voltage waveforms.

    This function may return multiple waveforms depending on the number of
    channels, the acquisition type, and the number of records you specify.

    

    .. note:: You can use :py:func:`niscope.read` instead of this function. :py:func:`niscope.read`
        starts an acquisition on all enabled channels, waits for the acquisition
        to complete, and returns the waveform for the specified channel.

        Some functionality, such as time stamping, is not supported in all
        digitizers. Refer to `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].fetch(num_samples, timeout=5.0)


    :param num_samples:


        The maximum number of samples to fetch for each waveform. If the
        acquisition finishes with fewer points than requested, some devices
        return partial data if the acquisition finished, was aborted, or a
        timeout of 0 was used. If it fails to complete within the timeout
        period, the function returns an error.

        


    :type num_samples: int
    :param timeout:


        The time to wait in seconds for data to be acquired; using 0 for this
        parameter tells NI-SCOPE to fetch whatever is currently available. Using
        -1 for this parameter implies infinite timeout.

        


    :type timeout: float

    :rtype: tuple (wfm, wfm_info)

        WHERE

        wfm (list of float): 


            Returns an array whose length is the **numSamples** times number of
            waveforms. Call :py:func:`niscope.ActualNumwfms` to determine the number of
            waveforms.

            NI-SCOPE returns this data sequentially, so all record 0 waveforms are
            first. For example, with a channel list of 0,1, you would have the
            following index values:

            index 0 = record 0, channel 0

            index *x* = record 0, channel 1

            index 2\ *x* = record 1, channel 0

            index 3\ *x* = record 1, channel 1

            Where *x* = the record length

            


        wfm_info (list of WaveformInfo): 


            Returns an array of structures with the following timing and scaling
            information about each waveform:

            -  **relativeInitialX**—the time (in seconds) from the trigger to the
            first sample in the fetched waveform
            -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
            sample. This timestamp is comparable between records and
            acquisitions; devices that do not support this parameter use 0 for
            this output.
            -  **xIncrement**—the time between points in the acquired waveform in
            seconds
            -  **actualSamples**—the actual number of samples fetched and placed in
            the waveform array
            -  **gain**—the gain factor of the given channel; useful for scaling
            binary data with the following formula:

            voltage = binary data × gain factor + offset

            -  **offset**—the offset factor of the given channel; useful for scaling
            binary data with the following formula:

            voltage = binary data × gain factor + offset

            Call :py:func:`niscope._actual_num_wfms` to determine the size of this array.

            



.. function:: fetch_measurement(scalar_meas_function, timeout=5.0)

    Fetches a waveform from the digitizer and performs the specified
    waveform measurement. Refer to `Using Fetch
    Functions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
    more information.

    Many of the measurements use the low, mid, and high reference levels.
    You configure the low, mid, and high references by using
    :py:data:`niscope.MEAS\_CHAN\_LOW\_REF\_LEVEL`,
    :py:data:`niscope.MEAS\_CHAN\_MID\_REF\_LEVEL`, and
    :py:data:`niscope.MEAS\_CHAN\_HIGH\_REF\_LEVEL` to set each channel
    differently.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].fetch_measurement(scalar_meas_function, timeout=5.0)


    :param scalar_meas_function:


        The `scalar
        measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
        to be performed.

        


    :type scalar_meas_function: :py:data:`niscope.ScalarMeasurement`
    :param timeout:


        The time to wait in seconds for data to be acquired; using 0 for this
        parameter tells NI-SCOPE to fetch whatever is currently available. Using
        -1 for this parameter implies infinite timeout.

        


    :type timeout: float

    :rtype: list of float
    :return:


            Contains an array of all measurements acquired; call
            :py:func:`niscope._actual_num_wfms` to determine the array length.

            



.. function:: fetch_measurement_stats(scalar_meas_function, timeout=5.0)

    Obtains a waveform measurement and returns the measurement value. This
    function may return multiple statistical results depending on the number
    of channels, the acquisition type, and the number of records you
    specify.

    You specify a particular measurement type, such as rise time, frequency,
    or voltage peak-to-peak. The waveform on which the digitizer calculates
    the waveform measurement is from an acquisition that you previously
    initiated. The statistics for the specified measurement function are
    returned, where the statistics are updated once every acquisition when
    the specified measurement is fetched by any of the Fetch Measurement
    functions. If a Fetch Measurement function has not been called, this
    function fetches the data on which to perform the measurement. The
    statistics are cleared by calling
    :py:func:`niscope.clear_waveform_measurement_stats`. Refer to `Using Fetch
    Functions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
    more information on incorporating fetch functions in your application.

    Many of the measurements use the low, mid, and high reference levels.
    You configure the low, mid, and high references with
    :py:data:`niscope.MEAS\_CHAN\_LOW\_REF\_LEVEL`,
    :py:data:`niscope.MEAS\_CHAN\_MID\_REF\_LEVEL`, and
    :py:data:`niscope.MEAS\_CHAN\_HIGH\_REF\_LEVEL` to set each channel
    differently.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].fetch_measurement_stats(scalar_meas_function, timeout=5.0)


    :param scalar_meas_function:


        The `scalar
        measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
        to be performed on each fetched waveform.

        


    :type scalar_meas_function: :py:data:`niscope.ScalarMeasurement`
    :param timeout:


        The time to wait in seconds for data to be acquired; using 0 for this
        parameter tells NI-SCOPE to fetch whatever is currently available. Using
        -1 for this parameter implies infinite timeout.

        


    :type timeout: float

    :rtype: tuple (result, mean, stdev, min, max, num_in_stats)

        WHERE

        result (list of float): 


            Returns the resulting measurement

            


        mean (list of float): 


            Returns the mean scalar value, which is obtained by averaging each
            :py:func:`niscope.fetch_measurement_stats` call.

            


        stdev (list of float): 


            Returns the standard deviation of the most recent **numInStats**
            measurements.

            


        min (list of float): 


            Returns the smallest scalar value acquired (the minimum of the
            **numInStats** measurements).

            


        max (list of float): 


            Returns the largest scalar value acquired (the maximum of the
            **numInStats** measurements).

            


        num_in_stats (list of int): 


            Returns the number of times :py:func:`niscope.fetch_measurement_stats` has been
            called.

            



.. function:: get_equalization_filter_coefficients(number_of_coefficients)

    Retrieves the custom coefficients for the equalization FIR filter on the
    device. This filter is designed to compensate the input signal for
    artifacts introduced to the signal outside of the digitizer. Because
    this filter is a generic FIR filter, any coefficients are valid.
    Coefficient values should be between +1 and –1.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].get_equalization_filter_coefficients(number_of_coefficients)


    :param number_of_coefficients:


        The number of coefficients being passed in the **coefficients** array.

        


    :type number_of_coefficients: int

    :rtype: list of float
    :return:


            The custom coefficients for the equalization FIR filter on the device.
            These coefficients should be between +1 and –1. You can obtain the
            number of coefficients from the
            `:py:data:`niscope.EQUALIZATION\_NUM\_COEFFICIENTS` <cviNISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS.html>`__
            attribute.

            



.. function:: probe_compensation_signal_start()

    Starts the 1 kHz square wave output on PFI 1 for probe compensation.

    



.. function:: probe_compensation_signal_stop()

    Stops the 1 kHz square wave output on PFI 1 for probe compensation.

    



.. function:: read(num_samples, timeout=5.0)

    Initiates an acquisition, waits for it to complete, and retrieves the
    data. The process is similar to calling :py:func:`niscope._initiate_acquisition`,
    :py:func:`niscope.acquisition_status`, and :py:func:`niscope._fetch_double`. The only difference is
    that with :py:func:`niscope.read`, you enable all channels specified with
    **channelList** before the acquisition; in the other method, you enable
    the channels with :py:func:`niscope.configure_vertical`.

    This function may return multiple waveforms depending on the number of
    channels, the acquisition type, and the number of records you specify.

    

    .. note:: Some functionality is not supported in all digitizers. Refer to
        `Features Supported by
        Device <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for
        more information.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].read(num_samples, timeout=5.0)


    :param num_samples:


        The maximum number of samples to fetch for each waveform. If the
        acquisition finishes with fewer points than requested, some devices
        return partial data if the acquisition finished, was aborted, or a
        timeout of 0 was used. If it fails to complete within the timeout
        period, the function returns an error.

        


    :type num_samples: int
    :param timeout:


        The time to wait in seconds for data to be acquired; using 0 for this
        parameter tells NI-SCOPE to fetch whatever is currently available. Using
        -1 for this parameter implies infinite timeout.

        


    :type timeout: float

    :rtype: tuple (wfm, wfm_info)

        WHERE

        wfm (list of float): 


            Returns an array whose length is the **numSamples** times number of
            waveforms. Call :py:func:`niscope.ActualNumwfms` to determine the number of
            waveforms.

            NI-SCOPE returns this data sequentially, so all record 0 waveforms are
            first. For example, with a channel list of 0,1, you would have the
            following index values:

            index 0 = record 0, channel 0

            index *x* = record 0, channel 1

            index 2\ *x* = record 1, channel 0

            index 3\ *x* = record 1, channel 1

            Where *x* = the record length

            


        wfm_info (list of WaveformInfo): 


            Returns an array of structures with the following timing and scaling
            information about each waveform:

            -  **relativeInitialX**—the time (in seconds) from the trigger to the
               first sample in the fetched waveform
            -  **absoluteInitialX**—timestamp (in seconds) of the first fetched
               sample. This timestamp is comparable between records and
               acquisitions; devices that do not support this parameter use 0 for
               this output.
            -  **xIncrement**—the time between points in the acquired waveform in
               seconds
            -  **actualSamples**—the actual number of samples fetched and placed in
               the waveform array
            -  **gain**—the gain factor of the given channel; useful for scaling
               binary data with the following formula:

            voltage = binary data × gain factor + offset

            -  **offset**—the offset factor of the given channel; useful for scaling
               binary data with the following formula:

            voltage = binary data × gain factor + offset

            Call :py:func:`niscope._actual_num_wfms` to determine the size of this array.

            



.. function:: read_measurement(scalar_meas_function, timeout=5.0)

    Initiates an acquisition, waits for it to complete, and performs the
    specified waveform measurement for a single channel and record or for
    multiple channels and records.

    Refer to `Using Fetch
    Functions <REPLACE_DRIVER_SPECIFIC_URL_1(using_fetch_functions)>`__ for
    more information.

    Many of the measurements use the low, mid, and high reference levels.
    You configure the low, mid, and high references by using
    :py:data:`niscope.MEAS\_CHAN\_LOW\_REF\_LEVEL`,
    :py:data:`niscope.MEAS\_CHAN\_MID\_REF\_LEVEL`, and
    :py:data:`niscope.MEAS\_CHAN\_HIGH\_REF\_LEVEL` to set each channel
    differently.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].read_measurement(scalar_meas_function, timeout=5.0)


    :param scalar_meas_function:


        The `scalar
        measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
        to be performed

        


    :type scalar_meas_function: :py:data:`niscope.ScalarMeasurement`
    :param timeout:


        The time to wait in seconds for data to be acquired; using 0 for this
        parameter tells NI-SCOPE to fetch whatever is currently available. Using
        -1 for this parameter implies infinite timeout.

        


    :type timeout: float

    :rtype: list of float
    :return:


            Contains an array of all measurements acquired. Call
            :py:func:`niscope._actual_num_wfms` to determine the array length.

            



.. function:: reset_device()

    Performs a hard reset of the device. Acquisition stops, all routes are
    released, RTSI and PFI lines are tristated, hardware is configured to
    its default state, and all session attributes are reset to their default
    state.

    -  `Thermal Shutdown <digitizers.chm::/Thermal_Shutdown.html>`__

    



.. function:: reset_with_defaults()

    Performs a software reset of the device, returning it to the default
    state and applying any initial default settings from the IVI
    Configuration Store.

    



.. function:: send_software_trigger_edge(which_trigger)

    Sends the selected trigger to the digitizer. Call this function if you
    called :py:func:`niscope.configure_trigger_software` when you want the Reference
    trigger to occur. You can also call this function to override a misused
    edge, digital, or hysteresis trigger. If you have configured
    :py:data:`niscope.ACQ\_ARM\_SOURCE`, :py:data:`niscope.ARM\_REF\_TRIG\_SRC`, or
    :py:data:`niscope.ADV\_TRIG\_SRC`, call this function when you want to send
    the corresponding trigger to the digitizer.

    



    :param which_trigger:


        Specifies the type of trigger to send to the digitizer.

        **Defined Values**

        | NISCOPE\_VAL\_SOFTWARE\_TRIGGER\_START (0L)
        |  NISCOPE\_VAL\_SOFTWARE\_TRIGGER\_ARM\_REFERENCE (1L)
        | NISCOPE\_VAL\_SOFTWARE\_TRIGGER\_REFERENCE (2L)
        | NISCOPE\_VAL\_SOFTWARE\_TRIGGER\_ADVANCE (3L)

        


    :type which_trigger: :py:data:`niscope.WhichTrigger`

.. function:: reset()

    Stops the acquisition, releases routes, and all session attributes are
    reset to their `default
    states <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cviattribute_defaults)>`__.

    



.. function:: self_test()

    Runs the instrument self-test routine and returns the test result(s).

    



    :rtype: tuple (self_test_result, self_test_message)

        WHERE

        self_test_result (int): 


            This control contains the value returned from the instrument self-test.

            **Self-Test Code Description**

            0—Self-test passed

            1—Self-test failed

            


        self_test_message (string): 


            Returns the self-test response string from the instrument. Refer to the
            device-specific help topics for an explanation of the string contents;
            you must pass a ViChar array at least IVI\_MAX\_MESSAGE\_BUF\_SIZE bytes
            in length.

            




