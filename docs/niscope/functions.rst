niscope.Session methods
=======================

.. py:currentmodule:: niscope

.. function:: acquisition_status()

    Returns status information about the acquisition to the **status**
    output parameter.

    



    :rtype: int
    :return:


            Returns whether the acquisition is complete, in progress, or unknown.

            **Defined Values**

            NISCOPE\_VAL\_ACQ\_COMPLETE

            NISCOPE\_VAL\_ACQ\_IN\_PROGRESS

            NISCOPE\_VAL\_ACQ\_STATUS\_UNKNOWN

            



.. function:: actual_meas_wfm_size(array_meas_function)

    Returns the total available size of an array measurement acquisition.

    



    :param array_meas_function:


        The `array
        measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
        to perform.

        


    :type array_meas_function: int

    :rtype: int
    :return:


            Returns the size (in number of samples) of the resulting analysis
            waveform.

            



.. function:: actual_num_wfms()

    Helps you to declare appropriately sized waveforms. NI-SCOPE handles the
    channel list parsing for you.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].actual_num_wfms()


    :rtype: int
    :return:


            Returns the number of records times the number of channels; if you are
            operating in DDC mode (NI 5620/5621 only), this value is multiplied by
            two.

            



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

        


    :type meas_function: int

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



.. function:: cal_self_calibrate(option)

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

            session['0,1'].cal_self_calibrate(option)


    :param option:


        The calibration option. Use VI\_NULL for a normal self-calibration
        operation or NISCOPE\_VAL\_CAL\_RESTORE\_EXTERNAL\_CALIBRATION to
        restore the previous calibration.

        


    :type option: int

.. function:: clear_waveform_measurement_stats(clearable_measurement_function)

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

            session['0,1'].clear_waveform_measurement_stats(clearable_measurement_function)


    :param clearable_measurement_function:


        The `scalar
        measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
        or `array
        measurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__
        to clear the stats for.

        


    :type clearable_measurement_function: int

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

        


    :type input_impedance: float
    :param max_input_frequency:


        The bandwidth for the channel; NI-SCOPE sets
        :py:data:`niscope.MAX\_INPUT\_FREQUENCY` to this value. Pass 0 for this
        value to use the hardware default bandwidth. Pass –1 for this value to
        achieve full bandwidth.

        


    :type max_input_frequency: float

.. function:: configure_equalization_filter_coefficients(number_of_coefficients, coefficients)

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

            session['0,1'].configure_equalization_filter_coefficients(number_of_coefficients, coefficients)


    :param number_of_coefficients:


        The number of coefficients being passed in the **coefficients** array.

        


    :type number_of_coefficients: int
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

.. function:: configure_ref_levels(low, mid, high)

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

.. function:: configure_tv_trigger_line_number(line_number)

    This function is included for compliance with the IviScope Class
    Specification.

    Configures the TV line upon which the instrument triggers. The line
    number is absolute and not relative to the field of the TV signal.

    This function affects instrument behavior only if the trigger type is
    set to NISCOPE\_VAL\_TV\_TRIGGER and the TV trigger event is set to
    NISCOPE\_VAL\_TV\_EVENT\_LINE\_NUMBER. Call
    :py:func:`niscope.configure_tv_trigger_source` to set the TV trigger event before
    calling this function.

    



    :param line_number:


        Specify the line number of the signal you want to trigger off of. The
        valid ranges of the attribute depend on the signal format configured.

        Default Value: 1

        +---------------------------+--------------+
        | Signal Format             | Line Numbers |
        +===========================+==============+
        | M-NTSC, 480i, 480p        | 1 to 525     |
        +---------------------------+--------------+
        | BG/PAL, SECAM, 576i, 576p | 1 to 625     |
        +---------------------------+--------------+
        | 720p                      | 1 to 750     |
        +---------------------------+--------------+
        | 1080i,1080p               | 1 to 1,125   |
        +---------------------------+--------------+


    :type line_number: int

.. function:: configure_tv_trigger_source(source, signal_format, event, polarity)

    Configures the instrument for TV triggering. It configures the TV signal
    format, the event, and the signal polarity.

    This function affects instrument behavior only if the trigger type is
    NISCOPE\_VAL\_TV\_TRIGGER. Set the trigger type and trigger coupling
    before calling this function.

    

    .. note:: This function is included for compliance with the IviScope Class
        Specification.



    :param source:


        Pass the source you want the digitizer to monitor for a trigger.

        Defined Values

        | "0"—Channel 0
        | "1"—Channel 1
        | NISCOPE\_VAL\_EXTERNAL—Analog External Trigger Input

        


    :type source: string
    :param signal_format:


        Specifies the Video/TV signal format.

        Defined Values

        | NISCOPE\_VAL\_NTSC (1)
        | NISCOPE\_VAL\_PAL (2)
        | NISCOPE\_VAL\_SECAM (3)

        


    :type signal_format: int
    :param event:


        Video/TV event to trigger off of.

        Defined Values

        | NISCOPE\_VAL\_TV\_EVENT\_FIELD1 (1)—trigger on field 1 of the signal
        | NISCOPE\_VAL\_TV\_EVENT\_FIELD2 (2)—trigger on field 2 of the signal
        | NISCOPE\_VAL\_TV\_EVENT\_ANY\_FIELD (3)—trigger on the first field
          acquired
        | NISCOPE\_VAL\_TV\_EVENT\_ANY\_LINE (4)—trigger on the first line
          acquired
        | NISCOPE\_VAL\_TV\_EVENT\_LINE\_NUMBER (5)—trigger on a specific line
          of a video signal. Valid values vary depending on the signal format
          configured.

        


    :type event: int
    :param polarity:


        | Specifies the polarity of the video signal to trigger off of.

        Defined Values

        | NISCOPE\_VAL\_TV\_POSITIVE (1)
        | NISCOPE\_VAL\_TV\_NEGATIVE (2)

        


    :type polarity: int

.. function:: configure_trigger(trigger_type, holdoff)

    Configures the common attributes of the trigger subsystem.

    When you use :py:func:`niscope.read_waveform`, the instrument waits for a trigger.
    You specify the type of trigger for which the instrument waits with the
    Trigger Type parameter.

    If the instrument requires multiple waveform acquisitions to build a
    complete waveform, it waits for the length of time you specify with the
    **holdoff** parameter to elapse since the previous trigger. The
    instrument then waits for the next trigger.

    

    .. note:: This function is included for compliance with the IviScope Class
        Specification.



    :param trigger_type:


        Specifies the type of trigger for which the digitizer will wait.

        


    :type trigger_type: int
    :param holdoff:


        The length of time the digitizer waits after detecting a trigger before
        enabling NI-SCOPE to detect another trigger. Refer to
        :py:data:`niscope.TRIGGER\_HOLDOFF` for more information.

        


    :type holdoff: float

.. function:: configure_trigger_coupling(coupling)

    Sets the trigger coupling attribute.

    

    .. note:: This function is included for compliance with the IviScope Class
        Specification.



    :param coupling:


        Specify how you want the instrument to couple the trigger signal.

        Defined Values

         NISCOPE\_VAL\_AC (0)

         NISCOPE\_VAL\_DC (1)

        NISCOPE\_VAL\_HF\_REJECT (2)

        NISCOPE\_VAL\_LF\_REJECT (3)

        NISCOPE\_VAL\_AC\_PLUS\_HF\_REJECT (1001)

        


    :type coupling: int

.. function:: configure_trigger_digital(trigger_source, slope, holdoff, delay)

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

        


    :type slope: int
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

.. function:: configure_trigger_edge(trigger_source, level, slope, trigger_coupling, holdoff, delay)

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
    :param level:


        The voltage threshold for the trigger. Refer to
        :py:data:`niscope.TRIGGER\_LEVEL` for more information.

        


    :type level: float
    :param slope:


        Specifies whether you want a rising edge or a falling edge to trigger
        the digitizer. Refer to :py:data:`niscope.TRIGGER\_SLOPE` for more
        information.

        


    :type slope: int
    :param trigger_coupling:


        Applies coupling and filtering options to the trigger signal. Refer to
        :py:data:`niscope.TRIGGER\_COUPLING` for more information.

        


    :type trigger_coupling: int
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

.. function:: configure_trigger_hysteresis(trigger_source, level, hysteresis, slope, trigger_coupling, holdoff, delay)

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

        


    :type slope: int
    :param trigger_coupling:


        Applies coupling and filtering options to the trigger signal. Refer to
        :py:data:`niscope.TRIGGER\_COUPLING` for more information.

        


    :type trigger_coupling: int
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

    



.. function:: configure_trigger_output(trigger_event, trigger_output)

    Configures the digitizer to generate a signal pulse that other
    digitizers can detect when configured for digital triggering.

    For Traditional NI-DAQ devices, exported signals are still present in
    the route after the session is closed. You must clear the route before
    closing the session, or call :py:func:`niscope.reset`.

    To clear the route, call this function again and route
    NISCOPE\_VAL\_NONE to the line that you had exported. For example, if
    you originally called this function with the trigger event
    NISCOPE\_VAL\_STOP\_TRIGGER\_EVENT routed to the trigger output
    NISCOPE\_VAL\_RTSI\_0, you would call this function again with
    NISCOPE\_VAL\_NONE routed to NISCOPE\_VAL\_RTSI\_0 to clear the route.

    

    .. note:: This function is obsolete. Consider using :py:func:`niscope.export_signal`
        instead.



    :param trigger_event:


        Specifies the condition in which this device generates a digital pulse.

        


    :type trigger_event: int
    :param trigger_output:


        Specifies the hardware signal line on which the digital pulse is
        generated.

        **Valid Values**

        | NISCOPE\_VAL\_NO\_EVENT
        | NISCOPE\_VAL\_STOP\_TRIGGER\_EVENT
        | NISCOPE\_VAL\_START\_TRIGGER\_EVENT
        | NISCOPE\_VAL\_END\_OF\_ACQUISITION\_EVENT
        | NISCOPE\_VAL\_END\_OF\_RECORD\_EVENT

        


    :type trigger_output: string

.. function:: configure_trigger_software(holdoff, delay)

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

.. function:: configure_trigger_video(trigger_source, enable_dc_restore, signal_format, event, line_number, polarity, trigger_coupling, holdoff, delay)

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
    :param enable_dc_restore:


        Offsets each video line so the clamping level (the portion of the video
        line between the end of the color burst and the beginning of the active
        image) is moved to zero volt. Refer to
        :py:data:`niscope.ENABLE\_DC\_RESTORE` for defined values.

        


    :type enable_dc_restore: bool
    :param signal_format:


        Specifies the type of video signal sync the digitizer should look for.
        Refer to :py:data:`niscope.TV\_TRIGGER\_SIGNAL\_FORMAT` for more
        information.

        


    :type signal_format: int
    :param event:


        Specifies the TV event you want to trigger on. You can trigger on a
        specific or on the next coming line or field of the signal.

        


    :type event: int
    :param line_number:


        Selects the line number to trigger on. The line number range covers an
        entire frame and is referenced as shown on `Vertical Blanking and
        Synchronization
        Signal <REPLACE_DRIVER_SPECIFIC_URL_1(gray_scale_image)>`__. Refer to
        :py:data:`niscope.TV\_TRIGGER\_LINE\_NUMBER` for more information.

        Default value: 1

        


    :type line_number: int
    :param polarity:


        Specifies the polarity of the video signal sync.

        


    :type polarity: int
    :param trigger_coupling:


        Applies coupling and filtering options to the trigger signal. Refer to
        :py:data:`niscope.TRIGGER\_COUPLING` for more information.

        


    :type trigger_coupling: int
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

.. function:: configure_trigger_window(trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff, delay)

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

        


    :type window_mode: int
    :param trigger_coupling:


        Applies coupling and filtering options to the trigger signal. Refer to
        :py:data:`niscope.TRIGGER\_COUPLING` for more information.

        


    :type trigger_coupling: int
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

.. function:: configure_vertical(range, offset, coupling, probe_attenuation, enabled)

    Configures the most commonly configured attributes of the digitizer
    vertical subsystem, such as the range, offset, coupling, probe
    attenuation, and the channel.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].configure_vertical(range, offset, coupling, probe_attenuation, enabled)


    :param range:


        Specifies the vertical range Refer to :py:data:`niscope.VERTICAL\_RANGE` for
        more information.

        


    :type range: float
    :param offset:


        Specifies the vertical offset. Refer to :py:data:`niscope.VERTICAL\_OFFSET`
        for more information.

        


    :type offset: float
    :param coupling:


        Specifies how to couple the input signal. Refer to
        :py:data:`niscope.VERTICAL\_COUPLING` for more information.

        


    :type coupling: int
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

    



.. function:: export_signal(signal, signal_identifier, output_terminal)

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

    

    .. note:: This function replaces :py:func:`niscope.configure_trigger_output`.



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


    :type signal: int
    :param signal_identifier:


        Describes the signal being exported.

        


    :type signal_identifier: string
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

.. function:: fetch_measurement(timeout, scalar_meas_function)

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

            session['0,1'].fetch_measurement(timeout, scalar_meas_function)


    :param timeout:


        The time to wait in seconds for data to be acquired; using 0 for this
        parameter tells NI-SCOPE to fetch whatever is currently available. Using
        -1 for this parameter implies infinite timeout.

        


    :type timeout: float
    :param scalar_meas_function:


        The `scalar
        measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
        to be performed.

        


    :type scalar_meas_function: int

    :rtype: list of float
    :return:


            Contains an array of all measurements acquired; call
            :py:func:`niscope.actual_num_wfms` to determine the array length.

            



.. function:: fetch_measurement_stats(timeout, scalar_meas_function)

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

            session['0,1'].fetch_measurement_stats(timeout, scalar_meas_function)


    :param timeout:


        The time to wait in seconds for data to be acquired; using 0 for this
        parameter tells NI-SCOPE to fetch whatever is currently available. Using
        -1 for this parameter implies infinite timeout.

        


    :type timeout: float
    :param scalar_meas_function:


        The `scalar
        measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
        to be performed on each fetched waveform.

        


    :type scalar_meas_function: int

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

            



.. function:: fetch_waveform(channel, waveform_size)

    Returns the waveform from a previously initiated acquisition that the
    digitizer acquires for the channel you specify.

    :py:func:`niscope._initiate_acquisition` starts an acquisition on the channels that
    you enable with :py:func:`niscope.configure_vertical`. The digitizer acquires
    waveforms for the enabled channels concurrently. You use
    :py:func:`niscope.acquisition_status` to determine when the acquisition is
    complete. You must call this function separately for each enabled
    channel to obtain the waveforms.

    You can call :py:func:`niscope.read_waveform` instead of
    :py:func:`niscope._initiate_acquisition`. :py:func:`niscope.read_waveform` starts an
    acquisition on all enabled channels, waits for the acquisition to
    complete, and returns the waveform for the channel you specify. Call
    this function to obtain the waveforms for each of the remaining
    channels.

    

    .. note:: This function is included for compliance with the IviScope Class
        Specification.



    :param channel:


        The channel to configure. For more information, refer to `channel String
        Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.

        Default Value: "0"

        


    :type channel: string
    :param waveform_size:


        The number of elements to insert into the **waveform** array.

        


    :type waveform_size: int

    :rtype: tuple (waveform, actual_points, initial_x, x_increment)

        WHERE

        waveform (list of float): 


            Returns the waveform that the digitizer acquires.

            Units: volts

            | Notes:
            | If the digitizer cannot sample a point in the waveform, this function
              returns an error.

            


        actual_points (int): 


            Indicates the actual number of points the function placed in the
            **waveform** array.

            


        initial_x (float): 


            Indicates the time of the first point in the **waveform** array relative
            to the Reference Position.

            Units: seconds

            For example, if the digitizer acquires the first point in the
            **waveform** array 1 second before the trigger, this parameter returns
            the value –1.0. If the acquisition of the first point occurs at the same
            time as the trigger, this parameter returns the value 0.0.

            


        x_increment (float): 


            Indicates the length of time between points in the **waveform** array.

            Units: seconds

            



.. function:: fetch_waveform_measurement(channel, meas_function)

    Configure the appropriate reference levels before calling this function.
    You can configure the low, mid, and high references by setting the
    following attributes:

    | :py:data:`niscope.MEAS\_HIGH\_REF`
    | :py:data:`niscope.MEAS\_LOW\_REF`
    | :py:data:`niscope.MEAS\_MID\_REF`

    

    .. note:: This function is included for compliance with the IviScope Class
        Specification.

        You can use :py:func:`niscope.read_waveform_measurement` instead of this function.
        :py:func:`niscope.read_waveform_measurement` starts an acquisition on all enabled
        channels, waits for the acquisition to complete, obtains a waveform
        measurement on the specified channel, and returns the waveform for the
        specified channel. Call this function separately to obtain any other
        waveform measurements on a specific channel.



    :param channel:


        The channel to configure. For more information, refer to `channel String
        Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.

        Default Value: "0"

        


    :type channel: string
    :param meas_function:


        Characteristic of the acquired waveform to be measured.

        


    :type meas_function: int

    :rtype: float
    :return:


            The measured value.

            



.. function:: get_channel_name(index, buffer_size)

    Returns the channel string that is in the channel table at an index you
    specify. Not applicable to National Instruments digitizers.

    

    .. note:: This function is included for compliance with the IviScope Class
        Specification.



    :param index:


        A 1-based index into the channel table.

        


    :type index: int
    :param buffer_size:


        Passes the number of bytes in the ViChar array you specify for the
        **description** parameter.

        If the error description, including the terminating NULL byte, contains
        more bytes than you indicate in this parameter, the function copies
        BufferSize - 1 bytes into the buffer, places an ASCII NULL byte at the
        end of the buffer, and returns the buffer size you must pass to get the
        entire value. For example, if the value is "123456" and the Buffer Size
        is 4, the function places "123" into the buffer and returns 7.

        If you pass a negative number, the function copies the value to the
        buffer regardless of the number of bytes in the value.

        


    :type buffer_size: int

    :rtype: string
    :return:


            Returns the channel string that is in the channel table at the index you
            specify. Do not modify the contents of the channel string.

            



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

            



.. function:: get_error_message(error_code, buffer__size)

    Returns the error code from an NI-SCOPE function as a user-readable
    string. Use VI\_NULL as the default instrument handle.

    You must call this function twice. For the first call, set
    **bufferSize** to 0 to prevent the function from populating the error
    message. Instead, the function returns the size of the error string. Use
    the returned size to create a buffer, then call the function again,
    passing in the new buffer and setting **bufferSize** equal to the size
    that was returned in the first function call.

    



    :param error_code:


        The error code that is returned from any of the instrument driver
        functions.

        


    :type error_code: int
    :param buffer__size:


        The number of characters you specify for the **errorMessage** parameter.

        


    :type buffer__size: int

    :rtype: string
    :return:


            Returns a char buffer that will be populated with the error message. It
            should be at least as large as the buffer size.

            



.. function:: get_frequency_response(buffer_size, frequencies, amplitudes, phases)

    Gets the frequency response of the digitizer for the current
    configurations of the channel attributes. Not all digitizers support
    this function.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        niscope.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niscope.Session instance, and calling this method on the result.:

        .. code:: python

            session['0,1'].get_frequency_response(buffer_size, frequencies, amplitudes, phases)


    :param buffer_size:


        The array size for the frequencies, amplitudes, and phases arrays that
        you pass in to the other parameters.

        To determine the sizes of the buffers to allocate for the frequencies,
        amplitudes, and phases arrays, pass a value of 0 to the **buffer\_size**
        parameter and a value of NULL to the **frequencies** parameter. In this
        case, the value returned by the **numberOfFrequencies** parameter is the
        size of the arrays necessary to hold the frequencies, amplitudes, and
        phases. Allocate three arrays of this size, then call this function
        again (with correct **buffer\_size** parameter) to retrieve the actual
        values.

        


    :type buffer_size: int
    :param frequencies:


        The array of frequencies that corresponds with the amplitude and phase
        response of the device.

        


    :type frequencies: list of float
    :param amplitudes:


        The array of amplitudes that correspond with the magnitude response of
        the device.

        


    :type amplitudes: list of float
    :param phases:


        The array of phases that correspond with the phase response of the
        device.

        


    :type phases: list of float

    :rtype: int
    :return:


            Returns the number of frequencies in the returned spectrum.

            



.. function:: get_stream_endpoint_handle(stream_name)

    Returns a writer endpoint that can be used with NI-P2P to configure a
    peer-to-peer stream with a digitizer endpoint.

    -  `Peer-to-Peer Streaming <digitizers.chm::/5160_P2P.html>`__

    



    :param stream_name:


        The stream endpoint FIFO to configure. Refer to the device-specific
        documentation for peer-to-peer streaming in the *High-Speed Digitizers
        Help* for more information.

        


    :type stream_name: string

    :rtype: int
    :return:


            Returns a reference to a peer-to-peer writer FIFO that can be used to
            create a peer-to-peer streaming session.

            



.. function:: is_invalid_wfm_element(element_value)

    Determines whether a value you pass from the waveform array is invalid.
    After the read and fetch waveform functions execute, each element in the
    waveform array contains either a voltage or a value indicating that the
    instrument could not sample a voltage.

    

    .. note:: This function is included for compliance with the IviScope Class
        Specification.



    :param element_value:


        Pass one of the values from the waveform array returned by the read and
        fetch waveform functions.

        


    :type element_value: float

    :rtype: bool
    :return:


            Returns whether the element value is a valid voltage or a value
            indicating that the digitizer could not sample a voltage.

            Return values:

            | VI\_TRUE—The element value indicates that the instrument could not
              sample the voltage.
            | VI\_FALSE—The element value is a valid voltage.

            



.. function:: probe_compensation_signal_start()

    Starts the 1 kHz square wave output on PFI 1 for probe compensation.

    



.. function:: probe_compensation_signal_stop()

    Stops the 1 kHz square wave output on PFI 1 for probe compensation.

    



.. function:: read_measurement(timeout, scalar_meas_function)

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

            session['0,1'].read_measurement(timeout, scalar_meas_function)


    :param timeout:


        The time to wait in seconds for data to be acquired; using 0 for this
        parameter tells NI-SCOPE to fetch whatever is currently available. Using
        -1 for this parameter implies infinite timeout.

        


    :type timeout: float
    :param scalar_meas_function:


        The `scalar
        measurement <REPLACE_DRIVER_SPECIFIC_URL_2(scalar_measurements_refs)>`__
        to be performed

        


    :type scalar_meas_function: int

    :rtype: list of float
    :return:


            Contains an array of all measurements acquired. Call
            :py:func:`niscope.actual_num_wfms` to determine the array length.

            



.. function:: read_waveform(channel, waveform_size, max_time)

    Initiates an acquisition on the channels that you enable with
    :py:func:`niscope.configure_vertical`. This function then waits for the acquisition
    to complete and returns the waveform for the channel you specify. Call
    :py:func:`niscope.fetch_waveform` to obtain the waveforms for each of the remaining
    enabled channels without initiating another acquisition.

    Use :py:func:`niscope.ActualRecordLength` to determine the required size for the
    **waveform** array.

    

    .. note:: This function is included for compliance with the IviScope Class
        Specification.



    :param channel:


        The channel to configure. For more information, refer to `channel String
        Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.

        Default Value: "0"

        


    :type channel: string
    :param waveform_size:


        The number of elements to insert into the **waveform** array.

        


    :type waveform_size: int
    :param max_time:


        Pass the maximum length of time in which to allow the read waveform
        operation to complete.

        If the operation does not complete within this time interval, the
        function returns the NISCOPE\_ERROR\_MAX\_TIME\_EXCEEDED error code.
        When this occurs, you can call :py:func:`niscope._abort` to cancel the read
        waveform operation and return the digitizer to the idle state.

        Units: milliseconds

        | Other Defined Values
        | NISCOPE\_VAL\_MAX\_TIME\_NONE
        | NISCOPE\_VAL\_MAX\_TIME\_INFINITE

        


    :type max_time: int

    :rtype: tuple (waveform, actual_points, initial_x, x_increment)

        WHERE

        waveform (list of float): 


            Returns the waveform that the digitizer acquires.
            Units: volts

            


        actual_points (int): 


            Indicates the actual number of points the function placed in the
            **waveform** array.

            


        initial_x (float): 


            Indicates the time of the first point in the **waveform** array relative
            to the Reference Position.

            Units: seconds

            For example, if the digitizer acquires the first point in the
            **waveform** array 1 second before the trigger, this parameter returns
            the value –1.0. If the acquisition of the first point occurs at the same
            time as the trigger, this parameter returns the value 0.0.

            


        x_increment (float): 


            Indicates the length of time between points in the **waveform** array.

            Units: seconds

            



.. function:: read_waveform_measurement(channel, meas_function, max_time)

    Initiates a new waveform acquisition and returns a specified waveform
    measurement from a specific channel.

    This function initiates an acquisition on the channels that you enable
    with the :py:func:`niscope.configure_vertical` function. It then waits for the
    acquisition to complete, obtains a waveform measurement on the channel
    you specify, and returns the measurement value. You specify a particular
    measurement type, such as rise time, frequency, or voltage peak-to-peak.

    You can call the :py:func:`niscope.fetch_waveform_measurement` function separately
    to obtain any other waveform measurement on a specific channel without
    initiating another acquisition.

    You must configure the appropriate reference levels before calling this
    function. Configure the low, mid, and high references by calling
    :py:func:`niscope.configure_ref_levels` or by setting the following attributes:

    | :py:data:`niscope.MEAS\_HIGH\_REF`
    | :py:data:`niscope.MEAS\_LOW\_REF`
    | :py:data:`niscope.MEAS\_MID\_REF`

    

    .. note:: This function is included for compliance with the IviScope Class
        Specification.



    :param channel:


        The channel to configure. For more information, refer to `channel String
        Syntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.

        Default Value: "0"

        


    :type channel: string
    :param meas_function:


        The scalar measurement to perform.

        


    :type meas_function: int
    :param max_time:


        Pass the maximum length of time in which to allow the read waveform
        operation to complete.

        If the operation does not complete within this time interval, the
        function returns the NISCOPE\_ERROR\_MAX\_TIME\_EXCEEDED error code.
        When this occurs, you can call :py:func:`niscope._abort` to cancel the read
        waveform operation and return the digitizer to the idle state.

        Units: milliseconds

        


    :type max_time: int

    :rtype: float
    :return:


            The measured value.

            



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

    



.. function:: sample_rate()

    Returns the effective sample rate, in samples per second, of the
    acquired waveform using the current configuration. Refer to `Coercions
    of Horizontal
    Parameters <REPLACE_DRIVER_SPECIFIC_URL_1(horizontal_parameters)>`__ for
    more information about sample rate coercion.

    



    :rtype: float
    :return:


            Returns the effective sample rate of the acquired waveform the digitizer
            acquires for each channel; the driver returns the value held in the
            :py:data:`niscope.HORZ\_SAMPLE\_RATE` attribute.

            



.. function:: send_sw_trigger()

    Sends a command to trigger the digitizer. Call this function after you
    call :py:func:`niscope.configure_trigger_software`.

    

    .. note:: This function is included for compliance with the IviScope Class
        Specification. Consider using :py:func:`niscope.send_software_trigger_edge` instead.



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

        


    :type which_trigger: int

.. function:: error_handler(error_code)

    Takes the error code returned by NI-SCOPE functions and returns the
    interpretation as a user-readable string.

    

    .. note:: You can pass VI\_NULL as the instrument handle, which is useful to
        interpret errors after :py:func:`niscope.init` has failed.



    :param error_code:


        The error code that is returned from any of the instrument driver
        functions.

        


    :type error_code: int

    :rtype: tuple (error_source, error_description)

        WHERE

        error_source (string): 


            Specifies the function in which the error occurred. You can pass in a
            string no longer than MAX\_FUNCTION\_NAME\_SIZE. If you pass in a valid
            string, this source is included in the **errorDescription** string. For
            example:

            "Error <**errorCode**> at <**errorSource**>"

            If you pass in NULL or an empty string, this parameter is ignored.

            


        error_description (string): 


            Returns the interpreted error code as a user readable message string;
            you must pass a ViChar array at least MAX\_ERROR\_DESCRIPTION bytes in
            length.

            



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

            




