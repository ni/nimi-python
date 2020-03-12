.. py:module:: niscope

Session
=======

.. py:class:: Session(self, resource_name, id_query=False, reset_device=False, options={})

    

    Performs the following initialization actions:

    -  Creates a new IVI instrument driver and optionally sets the initial
       state of the following session properties: Range Check, Cache,
       Simulate, Record Value Coercions
    -  Opens a session to the specified device using the interface and
       address you specify for the **resourceName**
    -  Resets the digitizer to a known state if **resetDevice** is set to
       True
    -  Queries the instrument ID and verifies that it is valid for this
       instrument driver if the **IDQuery** is set to True
    -  Returns an instrument handle that you use to identify the instrument
       in all subsequent instrument driver method calls

    



    :param resource_name:
        

        .. caution:: Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
            However, all IVI names, such as logical names, are case-sensitive. If
            you use logical names, driver session names, or virtual names in your
            program, you must make sure that the name you use matches the name in
            the IVI Configuration Store file exactly, without any variations in the
            case of the characters.

        | Specifies the resource name of the device to initialize

        For Traditional NI-DAQ devices, the syntax is DAQ::\ *n*, where *n* is
        the device number assigned by MAX, as shown in Example 1.

        For NI-DAQmx devices, the syntax is just the device name specified in
        MAX, as shown in Example 2. Typical default names for NI-DAQmx devices
        in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by
        right-clicking on the name in MAX and entering a new name.

        An alternate syntax for NI-DAQmx devices consists of DAQ::NI-DAQmx
        device name, as shown in Example 3. This naming convention allows for
        the use of an NI-DAQmx device in an application that was originally
        designed for a Traditional NI-DAQ device. For example, if the
        application expects DAQ::1, you can rename the NI-DAQmx device to 1 in
        MAX and pass in DAQ::1 for the resource name, as shown in Example 4.

        If you use the DAQ::\ *n* syntax and an NI-DAQmx device name already
        exists with that same name, the NI-DAQmx device is matched first.

        You can also pass in the name of an IVI logical name or an IVI virtual
        name configured with the IVI Configuration utility, as shown in Example
        5. A logical name identifies a particular virtual instrument. A virtual
        name identifies a specific device and specifies the initial settings for
        the session.

        +---------+--------------------------------------+--------------------------------------------------+
        | Example | Device Type                          | Syntax                                           |
        +=========+======================================+==================================================+
        | 1       | Traditional NI-DAQ device            | DAQ::1 (1 = device number)                       |
        +---------+--------------------------------------+--------------------------------------------------+
        | 2       | NI-DAQmx device                      | myDAQmxDevice (myDAQmxDevice = device name)      |
        +---------+--------------------------------------+--------------------------------------------------+
        | 3       | NI-DAQmx device                      | DAQ::myDAQmxDevice (myDAQmxDevice = device name) |
        +---------+--------------------------------------+--------------------------------------------------+
        | 4       | NI-DAQmx device                      | DAQ::2 (2 = device name)                         |
        +---------+--------------------------------------+--------------------------------------------------+
        | 5       | IVI logical name or IVI virtual name | myLogicalName (myLogicalName = name)             |
        +---------+--------------------------------------+--------------------------------------------------+


    :type resource_name: str

    :param id_query:
        

        Specify whether to perform an ID query.

        When you set this parameter to True, NI-SCOPE verifies that the
        device you initialize is a type that it supports.

        When you set this parameter to False, the method initializes the
        device without performing an ID query.

        **Defined Values**

        | True—Perform ID query
        | False—Skip ID query

        **Default Value**: True

        


    :type id_query: bool

    :param reset_device:
        

        Specify whether to reset the device during the initialization process.

        Default Value: True

        **Defined Values**

        True (1)—Reset device

        False (0)—Do not reset device

        

        .. note:: For the NI 5112, repeatedly resetting the device may cause excessive
            wear on the electromechanical relays. Refer to `NI 5112
            Electromechanical Relays <REPLACE_DRIVER_SPECIFIC_URL_1(5112_relays)>`__
            for recommended programming practices.


    :type reset_device: bool

    :param options:
        

        Specifies the initial value of certain properties for the session. The
        syntax for **options** is a dictionary of properties with an assigned
        value. For example:

        { 'simulate': False }

        You do not have to specify a value for all the properties. If you do not
        specify a value for a property, the default value is used.

        Advanced Example:
        { 'simulate': True, 'driver_setup': { 'Model': '<model number>',  'BoardType': '<type>' } }

        +-------------------------+---------+
        | Property                | Default |
        +=========================+=========+
        | range_check             | True    |
        +-------------------------+---------+
        | query_instrument_status | False   |
        +-------------------------+---------+
        | cache                   | True    |
        +-------------------------+---------+
        | simulate                | False   |
        +-------------------------+---------+
        | record_value_coersions  | False   |
        +-------------------------+---------+
        | driver_setup            | {}      |
        +-------------------------+---------+


    :type options: dict


Methods
=======

abort
-----

    .. py:currentmodule:: niscope.Session

    .. py:method:: abort()

            Aborts an acquisition and returns the digitizer to the Idle state. Call
            this method if the digitizer times out waiting for a trigger.

            



acquisition_status
------------------

    .. py:currentmodule:: niscope.Session

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

                    



auto_setup
----------

    .. py:currentmodule:: niscope.Session

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



close
-----

    .. py:currentmodule:: niscope.Session

    .. py:method:: close()

            When you are finished using an instrument driver session, you must call
            this method to perform the following actions:

            -  Closes the instrument I/O session.
            -  Destroys the IVI session and all of its properties.
            -  Deallocates any memory resources used by the IVI session.

            

            .. note:: This method is not needed when using the session context manager



commit
------

    .. py:currentmodule:: niscope.Session

    .. py:method:: commit()

            Commits to hardware all the parameter settings associated with the task.
            Use this method if you want a parameter change to be immediately
            reflected in the hardware. This method is not supported for
            Traditional NI-DAQ (Legacy) devices.

            



configure_chan_characteristics
------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_chan_characteristics(input_impedance, max_input_frequency)

            Configures the properties that control the electrical characteristics of
            the channel—the input impedance and the bandwidth.

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                niscope.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                niscope.Session repeated capabilities container, and calling this method on the result.


            :param input_impedance:


                The input impedance for the channel; NI-SCOPE sets
                :py:attr:`niscope.Session.input_impedance` to this value.

                


            :type input_impedance: float
            :param max_input_frequency:


                The bandwidth for the channel; NI-SCOPE sets
                :py:attr:`niscope.Session.max_input_frequency` to this value. Pass 0 for this
                value to use the hardware default bandwidth. Pass –1 for this value to
                achieve full bandwidth.

                


            :type max_input_frequency: float

configure_equalization_filter_coefficients
------------------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_equalization_filter_coefficients(coefficients)

            Configures the custom coefficients for the equalization FIR filter on
            the device. This filter is designed to compensate the input signal for
            artifacts introduced to the signal outside of the digitizer. Because
            this filter is a generic FIR filter, any coefficients are valid.
            Coefficient values should be between +1 and –1.

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                niscope.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                niscope.Session repeated capabilities container, and calling this method on the result.


            :param coefficients:


                The custom coefficients for the equalization FIR filter on the device.
                These coefficients should be between +1 and –1. You can obtain the
                number of coefficients from the
                `:py:attr:`niscope.Session.equalization_num_coefficients` <cvi:py:attr:`niscope.Session.equalization_num_coefficients`.html>`__
                property. The
                `:py:attr:`niscope.Session.equalization_filter_enabled` <cvi:py:attr:`niscope.Session.equalization_filter_enabled`.html>`__
                property must be set to TRUE to enable the filter.

                


            :type coefficients: list of float

configure_horizontal_timing
---------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_horizontal_timing(min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime)

            Configures the common properties of the horizontal subsystem for a
            multirecord acquisition in terms of minimum sample rate.

            



            :param min_sample_rate:


                The sampling rate for the acquisition. Refer to
                :py:attr:`niscope.Session.min_sample_rate` for more information.

                


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

configure_trigger_digital
-------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_trigger_digital(trigger_source, slope=niscope.TriggerSlope.POSITIVE, holdoff=datetime.timedelta(seconds=0.0), delay=datetime.timedelta(seconds=0.0))

            Configures the common properties of a digital trigger.

            When you initiate an acquisition, the digitizer waits for the start
            trigger, which is configured through the :py:attr:`niscope.Session.acq_arm_source`
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


                Specifies the trigger source. Refer to :py:attr:`niscope.Session.trigger_source`
                for defined values.

                


            :type trigger_source: str
            :param slope:


                Specifies whether you want a rising edge or a falling edge to trigger
                the digitizer. Refer to :py:attr:`niscope.Session.trigger_slope` for more
                information.

                


            :type slope: :py:data:`niscope.TriggerSlope`
            :param holdoff:


                The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                :py:attr:`niscope.Session.trigger_holdoff` for more information.

                


            :type holdoff: float in seconds or datetime.timedelta
            :param delay:


                How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to :py:attr:`niscope.Session.trigger_delay_time` for more
                information.

                


            :type delay: float in seconds or datetime.timedelta

configure_trigger_edge
----------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_trigger_edge(trigger_source, level, trigger_coupling, slope=niscope.TriggerSlope.POSITIVE, holdoff=datetime.timedelta(seconds=0.0), delay=datetime.timedelta(seconds=0.0))

            Configures common properties for analog edge triggering.

            When you initiate an acquisition, the digitizer waits for the start
            trigger, which is configured through the :py:attr:`niscope.Session.acq_arm_source`
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


                Specifies the trigger source. Refer to :py:attr:`niscope.Session.trigger_source`
                for defined values.

                


            :type trigger_source: str
            :param level:


                The voltage threshold for the trigger. Refer to
                :py:attr:`niscope.Session.trigger_level` for more information.

                


            :type level: float
            :param trigger_coupling:


                Applies coupling and filtering options to the trigger signal. Refer to
                :py:attr:`niscope.Session.trigger_coupling` for more information.

                


            :type trigger_coupling: :py:data:`niscope.TriggerCoupling`
            :param slope:


                Specifies whether you want a rising edge or a falling edge to trigger
                the digitizer. Refer to :py:attr:`niscope.Session.trigger_slope` for more
                information.

                


            :type slope: :py:data:`niscope.TriggerSlope`
            :param holdoff:


                The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                :py:attr:`niscope.Session.trigger_holdoff` for more information.

                


            :type holdoff: float in seconds or datetime.timedelta
            :param delay:


                How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to :py:attr:`niscope.Session.trigger_delay_time` for more
                information.

                


            :type delay: float in seconds or datetime.timedelta

configure_trigger_hysteresis
----------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_trigger_hysteresis(trigger_source, level, hysteresis, trigger_coupling, slope=niscope.TriggerSlope.POSITIVE, holdoff=datetime.timedelta(seconds=0.0), delay=datetime.timedelta(seconds=0.0))

            Configures common properties for analog hysteresis triggering. This kind
            of trigger specifies an additional value, specified in the
            **hysteresis** parameter, that a signal must pass through before a
            trigger can occur. This additional value acts as a kind of buffer zone
            that keeps noise from triggering an acquisition.

            When you initiate an acquisition, the digitizer waits for the start
            trigger, which is configured through the
            :py:attr:`niscope.Session.acq_arm_source`. The default is immediate. Upon
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


                Specifies the trigger source. Refer to :py:attr:`niscope.Session.trigger_source`
                for defined values.

                


            :type trigger_source: str
            :param level:


                The voltage threshold for the trigger. Refer to
                :py:attr:`niscope.Session.trigger_level` for more information.

                


            :type level: float
            :param hysteresis:


                The size of the hysteresis window on either side of the **level** in
                volts; the digitizer triggers when the trigger signal passes through the
                hysteresis value you specify with this parameter, has the slope you
                specify with **slope**, and passes through the **level**. Refer to
                :py:attr:`niscope.Session.trigger_hysteresis` for defined values.

                


            :type hysteresis: float
            :param trigger_coupling:


                Applies coupling and filtering options to the trigger signal. Refer to
                :py:attr:`niscope.Session.trigger_coupling` for more information.

                


            :type trigger_coupling: :py:data:`niscope.TriggerCoupling`
            :param slope:


                Specifies whether you want a rising edge or a falling edge to trigger
                the digitizer. Refer to :py:attr:`niscope.Session.trigger_slope` for more
                information.

                


            :type slope: :py:data:`niscope.TriggerSlope`
            :param holdoff:


                The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                :py:attr:`niscope.Session.trigger_holdoff` for more information.

                


            :type holdoff: float in seconds or datetime.timedelta
            :param delay:


                How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to :py:attr:`niscope.Session.trigger_delay_time` for more
                information.

                


            :type delay: float in seconds or datetime.timedelta

configure_trigger_immediate
---------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_trigger_immediate()

            Configures common properties for immediate triggering. Immediate
            triggering means the digitizer triggers itself.

            When you initiate an acquisition, the digitizer waits for a trigger. You
            specify the type of trigger that the digitizer waits for with a
            Configure Trigger method, such as :py:meth:`niscope.Session.configure_trigger_immediate`.

            



configure_trigger_software
--------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_trigger_software(holdoff=datetime.timedelta(seconds=0.0), delay=datetime.timedelta(seconds=0.0))

            Configures common properties for software triggering.

            When you initiate an acquisition, the digitizer waits for the start
            trigger, which is configured through the :py:attr:`niscope.Session.acq_arm_source`
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
                :py:attr:`niscope.Session.trigger_holdoff` for more information.

                


            :type holdoff: float in seconds or datetime.timedelta
            :param delay:


                How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to :py:attr:`niscope.Session.trigger_delay_time` for more
                information.

                


            :type delay: float in seconds or datetime.timedelta

configure_trigger_video
-----------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_trigger_video(trigger_source, signal_format, event, polarity, trigger_coupling, enable_dc_restore=False, line_number=1, holdoff=datetime.timedelta(seconds=0.0), delay=datetime.timedelta(seconds=0.0))

            Configures the common properties for video triggering, including the
            signal format, TV event, line number, polarity, and enable DC restore. A
            video trigger occurs when the digitizer finds a valid video signal sync.

            When you initiate an acquisition, the digitizer waits for the start
            trigger, which is configured through the :py:attr:`niscope.Session.acq_arm_source`
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


                Specifies the trigger source. Refer to :py:attr:`niscope.Session.trigger_source`
                for defined values.

                


            :type trigger_source: str
            :param signal_format:


                Specifies the type of video signal sync the digitizer should look for.
                Refer to :py:attr:`niscope.Session.tv_trigger_signal_format` for more
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
                :py:attr:`niscope.Session.trigger_coupling` for more information.

                


            :type trigger_coupling: :py:data:`niscope.TriggerCoupling`
            :param enable_dc_restore:


                Offsets each video line so the clamping level (the portion of the video
                line between the end of the color burst and the beginning of the active
                image) is moved to zero volt. Refer to
                :py:attr:`niscope.Session.enable_dc_restore` for defined values.

                


            :type enable_dc_restore: bool
            :param line_number:


                Selects the line number to trigger on. The line number range covers an
                entire frame and is referenced as shown on `Vertical Blanking and
                Synchronization
                Signal <REPLACE_DRIVER_SPECIFIC_URL_1(gray_scale_image)>`__. Refer to
                :py:attr:`niscope.Session.tv_trigger_line_number` for more information.

                Default value: 1

                


            :type line_number: int
            :param holdoff:


                The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                :py:attr:`niscope.Session.trigger_holdoff` for more information.

                


            :type holdoff: float in seconds or datetime.timedelta
            :param delay:


                How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to :py:attr:`niscope.Session.trigger_delay_time` for more
                information.

                


            :type delay: float in seconds or datetime.timedelta

configure_trigger_window
------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_trigger_window(trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff=datetime.timedelta(seconds=0.0), delay=datetime.timedelta(seconds=0.0))

            Configures common properties for analog window triggering. A window
            trigger occurs when a signal enters or leaves a window you specify with
            the **high level** or **low level** parameters.

            When you initiate an acquisition, the digitizer waits for the start
            trigger, which is configured through the :py:attr:`niscope.Session.acq_arm_source`
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

            

            .. note:: Some features are not supported by all digitizers.



            :param trigger_source:


                Specifies the trigger source. Refer to :py:attr:`niscope.Session.trigger_source`
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
                :py:attr:`niscope.Session.trigger_coupling` for more information.

                


            :type trigger_coupling: :py:data:`niscope.TriggerCoupling`
            :param holdoff:


                The length of time the digitizer waits after detecting a trigger before
                enabling NI-SCOPE to detect another trigger. Refer to
                :py:attr:`niscope.Session.trigger_holdoff` for more information.

                


            :type holdoff: float in seconds or datetime.timedelta
            :param delay:


                How long the digitizer waits after receiving the trigger to start
                acquiring data. Refer to :py:attr:`niscope.Session.trigger_delay_time` for more
                information.

                


            :type delay: float in seconds or datetime.timedelta

configure_vertical
------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: configure_vertical(range, coupling, offset=0.0, probe_attenuation=1.0, enabled=True)

            Configures the most commonly configured properties of the digitizer
            vertical subsystem, such as the range, offset, coupling, probe
            attenuation, and the channel.

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                niscope.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                niscope.Session repeated capabilities container, and calling this method on the result.


            :param range:


                Specifies the vertical range Refer to :py:attr:`niscope.Session.vertical_range` for
                more information.

                


            :type range: float
            :param coupling:


                Specifies how to couple the input signal. Refer to
                :py:attr:`niscope.Session.vertical_coupling` for more information.

                


            :type coupling: :py:data:`niscope.VerticalCoupling`
            :param offset:


                Specifies the vertical offset. Refer to :py:attr:`niscope.Session.vertical_offset`
                for more information.

                


            :type offset: float
            :param probe_attenuation:


                Specifies the probe attenuation. Refer to
                :py:attr:`niscope.Session.probe_attenuation` for valid values.

                


            :type probe_attenuation: float
            :param enabled:


                Specifies whether the channel is enabled for acquisition. Refer to
                :py:attr:`niscope.Session.channel_enabled` for more information.

                


            :type enabled: bool

disable
-------

    .. py:currentmodule:: niscope.Session

    .. py:method:: disable()

            Aborts any current operation, opens data channel relays, and releases
            RTSI and PFI lines.

            



export_attribute_configuration_buffer
-------------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: export_attribute_configuration_buffer()

            Exports the property configuration of the session to a configuration
            buffer.

            You can export and import session property configurations only between
            devices with identical model numbers, channel counts, and onboard memory
            sizes.

            This method verifies that the properties you have configured for the
            session are valid. If the configuration is invalid, NI‑SCOPE returns an
            error.

            **Related Topics:**

            `Properties and Property
            Methods <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__

            `Setting Properties Before Reading
            Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

            



            :rtype: bytes
            :return:


                    Specifies the byte array buffer to be populated with the exported
                    property configuration.

                    



export_attribute_configuration_file
-----------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: export_attribute_configuration_file(file_path)

            Exports the property configuration of the session to the specified
            file.

            You can export and import session property configurations only between
            devices with identical model numbers, channel counts, and onboard memory
            sizes.

            This method verifies that the properties you have configured for the
            session are valid. If the configuration is invalid, NI‑SCOPE returns an
            error.

            **Related Topics:**

            `Properties and Property
            Methods <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__

            `Setting Properties Before Reading
            Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

            



            :param file_path:


                Specifies the absolute path to the file to contain the exported
                property configuration. If you specify an empty or relative path, this
                method returns an error.
                **Default file extension:** .niscopeconfig

                


            :type file_path: str

fetch
-----

    .. py:currentmodule:: niscope.Session

    .. py:method:: fetch(num_samples=None, relative_to=niscope.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=datetime.timedelta(seconds=5.0))

            Returns the waveform from a previously initiated acquisition that the
            digitizer acquires for the specified channel. This method returns
            scaled voltage waveforms.

            This method may return multiple waveforms depending on the number of
            channels, the acquisition type, and the number of records you specify.

            

            .. note:: Some functionality, such as time stamping, is not supported in all digitizers.


            .. tip:: This method requires repeated capabilities. If called directly on the
                niscope.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                niscope.Session repeated capabilities container, and calling this method on the result.


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

                


            :type timeout: float in seconds or datetime.timedelta

            :rtype: list of WaveformInfo
            :return:


                    Returns a list of class instances with the following timing and scaling information about each waveform:

                    -  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform
                    -  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
                    -  **x_increment** (float) the time between points in the acquired waveform in seconds
                    -  **channel** (str) channel name this waveform was acquired from
                    -  **record** (int) record number of this waveform
                    -  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:

                        .. math::

                            voltage = binary data * gain factor + offset

                    -  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:

                        .. math::

                            voltage = binary data * gain factor + offset

                    - **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired

                    



fetch_into
----------

    .. py:currentmodule:: niscope.Session

    .. py:method:: fetch_into(waveform, relative_to=niscope.FetchRelativeTo.PRETRIGGER, offset=0, record_number=0, num_records=None, timeout=datetime.timedelta(seconds=5.0))

            Returns the waveform from a previously initiated acquisition that the
            digitizer acquires for the specified channel. This method returns
            scaled voltage waveforms.

            This method may return multiple waveforms depending on the number of
            channels, the acquisition type, and the number of records you specify.

            

            .. note:: Some functionality, such as time stamping, is not supported in all digitizers.


            .. tip:: This method requires repeated capabilities. If called directly on the
                niscope.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                niscope.Session repeated capabilities container, and calling this method on the result.


            :param waveform:


                numpy array of the appropriate type and size that should be acquired as a 1D array. Size should be **num_samples** times number of waveforms. Call :py:meth:`niscope.Session._actual_num_wfms` to determine the number of waveforms.

                Types supported are

                - `numpy.float64`
                - `numpy.int8`
                - `numpy.in16`
                - `numpy.int32`

                Example:

                .. code-block:: python

                    waveform = numpy.ndarray(num_samples * session.actual_num_wfms(), dtype=numpy.float64)
                    wfm_info = session['0,1'].fetch_into(waveform, timeout=5.0)

                


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

                


            :type timeout: float in seconds or datetime.timedelta

            :rtype: list of WaveformInfo
            :return:


                    Returns a list of class instances with the following timing and scaling information about each waveform:

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

                    



get_equalization_filter_coefficients
------------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: get_equalization_filter_coefficients()

            Retrieves the custom coefficients for the equalization FIR filter on the device. This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should be between +1 and –1.

            


            .. tip:: This method requires repeated capabilities. If called directly on the
                niscope.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                niscope.Session repeated capabilities container, and calling this method on the result.


import_attribute_configuration_buffer
-------------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: import_attribute_configuration_buffer(configuration)

            Imports a property configuration to the session from the specified
            configuration buffer.

            You can export and import session property configurations only between
            devices with identical model numbers, channel counts, and onboard memory
            sizes.

            **Related Topics:**

            `Properties and Property
            Methods <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__

            `Setting Properties Before Reading
            Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

            

            .. note:: You cannot call this method while the session is in a running state,
                such as while acquiring a signal.



            :param configuration:


                Specifies the byte array buffer that contains the property
                configuration to import.

                


            :type configuration: bytes

import_attribute_configuration_file
-----------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: import_attribute_configuration_file(file_path)

            Imports a property configuration to the session from the specified
            file.

            You can export and import session property configurations only between
            devices with identical model numbers, channel counts, and onboard memory
            sizes.

            **Related Topics:**

            `Properties and Property
            Methods <REPLACE_DRIVER_SPECIFIC_URL_1(attributes_and_attribute_functions)>`__

            `Setting Properties Before Reading
            Properties <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__

            

            .. note:: You cannot call this method while the session is in a running state,
                such as while acquiring a signal.



            :param file_path:


                Specifies the absolute path to the file containing the property
                configuration to import. If you specify an empty or relative path, this
                method returns an error.
                **Default File Extension:** .niscopeconfig

                


            :type file_path: str

initiate
--------

    .. py:currentmodule:: niscope.Session

    .. py:method:: initiate()

            Initiates a waveform acquisition.

            After calling this method, the digitizer leaves the Idle state and
            waits for a trigger. The digitizer acquires a waveform for each channel
            you enable with :py:meth:`niscope.Session.configure_vertical`.

            

            .. note:: This method will return a Python context manager that will initiate on entering and abort on exit.



lock
----

    .. py:currentmodule:: niscope.Session

.. py:method:: lock()

    Obtains a multithread lock on the device session. Before doing so, the
    software waits until all other execution threads release their locks
    on the device session.

    Other threads may have obtained a lock on this session for the
    following reasons:

        -  The application called the :py:meth:`niscope.Session.lock` method.
        -  A call to NI-SCOPE locked the session.
        -  After a call to the :py:meth:`niscope.Session.lock` method returns
           successfully, no other threads can access the device session until
           you call the :py:meth:`niscope.Session.unlock` method or exit out of the with block when using
           lock context manager.
        -  Use the :py:meth:`niscope.Session.lock` method and the
           :py:meth:`niscope.Session.unlock` method around a sequence of calls to
           instrument driver methods if you require that the device retain its
           settings through the end of the sequence.

    You can safely make nested calls to the :py:meth:`niscope.Session.lock` method
    within the same thread. To completely unlock the session, you must
    balance each call to the :py:meth:`niscope.Session.lock` method with a call to
    the :py:meth:`niscope.Session.unlock` method.

    One method for ensuring there are the same number of unlock method calls as there is lock calls
    is to use lock as a context manager

        .. code:: python

            with niscope.Session('dev1') as session:
                with session.lock():
                    # Calls to session within a single lock context

        The first `with` block ensures the session is closed regardless of any exceptions raised

        The second `with` block ensures that unlock is called regardless of any exceptions raised

    :rtype: context manager
    :return:
        When used in a `with` statement, :py:meth:`niscope.Session.lock` acts as
        a context manager and unlock will be called when the `with` block is exited


probe_compensation_signal_start
-------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: probe_compensation_signal_start()

            Starts the 1 kHz square wave output on PFI 1 for probe compensation.

            



probe_compensation_signal_stop
------------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: probe_compensation_signal_stop()

            Stops the 1 kHz square wave output on PFI 1 for probe compensation.

            



read
----

    .. py:currentmodule:: niscope.Session

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


            .. tip:: This method requires repeated capabilities. If called directly on the
                niscope.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                niscope.Session repeated capabilities container, and calling this method on the result.


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

                


            :type timeout: float in seconds or datetime.timedelta

            :rtype: list of WaveformInfo
            :return:


                    Returns a list of class instances with the following timing and scaling information about each waveform:

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

                    



reset
-----

    .. py:currentmodule:: niscope.Session

    .. py:method:: reset()

            Stops the acquisition, releases routes, and all session properties are
            reset to their `default
            states <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cviattribute_defaults)>`__.

            



reset_device
------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: reset_device()

            Performs a hard reset of the device. Acquisition stops, all routes are
            released, RTSI and PFI lines are tristated, hardware is configured to
            its default state, and all session properties are reset to their default
            state.

            -  `Thermal Shutdown <digitizers.chm::/Thermal_Shutdown.html>`__

            



reset_with_defaults
-------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: reset_with_defaults()

            Performs a software reset of the device, returning it to the default
            state and applying any initial default settings from the IVI
            Configuration Store.

            



self_cal
--------

    .. py:currentmodule:: niscope.Session

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


            .. tip:: This method requires repeated capabilities. If called directly on the
                niscope.Session object, then the method will use all repeated capabilities in the session.
                You can specify a subset of repeated capabilities using the Python index notation on an
                niscope.Session repeated capabilities container, and calling this method on the result.


            :param option:


                The calibration option. Use VI_NULL for a normal self-calibration
                operation or :py:data:`~niscope.NISCOPE_VAL_CAL_RESTORE_EXTERNAL_CALIBRATION` to
                restore the previous calibration.

                

                .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


            :type option: :py:data:`niscope.Option`

self_test
---------

    .. py:currentmodule:: niscope.Session

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



send_software_trigger_edge
--------------------------

    .. py:currentmodule:: niscope.Session

    .. py:method:: send_software_trigger_edge(which_trigger)

            Sends the selected trigger to the digitizer. Call this method if you
            called :py:meth:`niscope.Session.configure_trigger_software` when you want the Reference
            trigger to occur. You can also call this method to override a misused
            edge, digital, or hysteresis trigger. If you have configured
            :py:attr:`niscope.Session.acq_arm_source`, :py:attr:`niscope.Session.arm_ref_trig_src`, or
            :py:attr:`niscope.Session.adv_trig_src`, call this method when you want to send
            the corresponding trigger to the digitizer.

            



            :param which_trigger:


                Specifies the type of trigger to send to the digitizer.

                **Defined Values**

                | :py:data:`~niscope.WhichTrigger.START` (0L)
                |  :py:data:`~niscope.WhichTrigger.ARM_REFERENCE` (1L)
                | :py:data:`~niscope.WhichTrigger.REFERENCE` (2L)
                | :py:data:`~niscope.WhichTrigger.ADVANCE` (3L)

                


            :type which_trigger: :py:data:`niscope.WhichTrigger`

unlock
------

    .. py:currentmodule:: niscope.Session

.. py:method:: unlock()

    Releases a lock that you acquired on an device session using
    :py:meth:`niscope.Session.lock`. Refer to :py:meth:`niscope.Session.unlock` for additional
    information on session locks.




Properties
==========

absolute_sample_clock_offset
----------------------------

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

            +----------------+----------------------------------------+
            | Characteristic | Value                                  |
            +================+========================================+
            | Datatype       | float in seconds or datetime.timedelta |
            +----------------+----------------------------------------+
            | Permissions    | read-write                             |
            +----------------+----------------------------------------+
            | Channel Based  | No                                     |
            +----------------+----------------------------------------+
            | Resettable     | Yes                                    |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Advanced:Absolute Sample Clock Offset**
                - C Attribute: **NISCOPE_ATTR_ABSOLUTE_SAMPLE_CLOCK_OFFSET**

acquisition_start_time
----------------------

    .. py:attribute:: acquisition_start_time

        Specifies the length of time from the trigger event to the first point in the waveform record in seconds.  If the value is positive, the first point in the waveform record occurs after the trigger event (same as specifying :py:attr:`niscope.Session.trigger_delay_time`).  If the value is negative, the first point in the waveform record occurs before the trigger event (same as specifying :py:attr:`niscope.Session.horz_record_ref_position`).

        The following table lists the characteristics of this property.

            +----------------+----------------------------------------+
            | Characteristic | Value                                  |
            +================+========================================+
            | Datatype       | float in seconds or datetime.timedelta |
            +----------------+----------------------------------------+
            | Permissions    | read-write                             |
            +----------------+----------------------------------------+
            | Channel Based  | No                                     |
            +----------------+----------------------------------------+
            | Resettable     | Yes                                    |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Advanced:Acquisition Start Time**
                - C Attribute: **NISCOPE_ATTR_ACQUISITION_START_TIME**

acquisition_type
----------------

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
            | Channel Based  | No                    |
            +----------------+-----------------------+
            | Resettable     | Yes                   |
            +----------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Acquisition Type**
                - C Attribute: **NISCOPE_ATTR_ACQUISITION_TYPE**

acq_arm_source
--------------

    .. py:attribute:: acq_arm_source

        Specifies the source the digitizer monitors for a start (acquisition arm) trigger.  When the start trigger is received, the digitizer begins acquiring pretrigger samples.
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



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Start Trigger (Acq. Arm):Source**
                - C Attribute: **NISCOPE_ATTR_ACQ_ARM_SOURCE**

adv_trig_src
------------

    .. py:attribute:: adv_trig_src

        Specifies the source the digitizer monitors for an advance trigger.  When the advance trigger is received, the digitizer begins acquiring pretrigger samples.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Advance Trigger:Source**
                - C Attribute: **NISCOPE_ATTR_ADV_TRIG_SRC**

allow_more_records_than_memory
------------------------------

    .. py:attribute:: allow_more_records_than_memory

        Indicates whether more records can be configured with :py:meth:`niscope.Session.configure_horizontal_timing` than fit in the onboard memory. If this property is set to True, it is necessary to fetch records while the acquisition is in progress.  Eventually, some of the records will be overwritten.  An error is returned from the fetch method if you attempt to fetch a record that has been overwritten.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Enable Records > Memory**
                - C Attribute: **NISCOPE_ATTR_ALLOW_MORE_RECORDS_THAN_MEMORY**

arm_ref_trig_src
----------------

    .. py:attribute:: arm_ref_trig_src

        Specifies the source the digitizer monitors for an arm reference trigger.  When the arm reference trigger is received, the digitizer begins looking for a reference (stop) trigger from the user-configured trigger source.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Arm Reference Trigger:Source**
                - C Attribute: **NISCOPE_ATTR_ARM_REF_TRIG_SRC**

backlog
-------

    .. py:attribute:: backlog

        Returns the number of samples (:py:attr:`niscope.Session.points_done`) that have been acquired but not fetched for the record specified by :py:attr:`niscope.Session.fetch_record_number`.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Fetch:Fetch Backlog**
                - C Attribute: **NISCOPE_ATTR_BACKLOG**

bandpass_filter_enabled
-----------------------

    .. py:attribute:: bandpass_filter_enabled

        Enables the bandpass filter on the specificed channel.  The default value is FALSE.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:Bandpass Filter Enabled**
                - C Attribute: **NISCOPE_ATTR_BANDPASS_FILTER_ENABLED**

binary_sample_width
-------------------

    .. py:attribute:: binary_sample_width

        Indicates the bit width of the binary data in the acquired waveform.  Useful for determining which Binary Fetch method to use. Compare to :py:attr:`niscope.Session.resolution`.
        To configure the device to store samples with a lower resolution that the native, set this property to the desired binary width.
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
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Binary Sample Width**
                - C Attribute: **NISCOPE_ATTR_BINARY_SAMPLE_WIDTH**

cable_sense_mode
----------------

    .. py:attribute:: cable_sense_mode

        Specifies whether and how the oscilloscope is configured to generate a CableSense signal on the specified channels when the :py:meth:`niscope.Session.CableSenseSignalStart` method is called.

        Device-Specific Behavior:
            PXIe-5160/5162
                - The value of this property must be identical across all channels whose input impedance is set to 50 ohms.
                - If this property is set to a value other than :py:data:`~niscope.CableSenseMode.DISABLED` for any channel(s), the input impedance of all channels for which this property is set to :py:data:`~niscope.CableSenseMode.DISABLED` must be set to 1 M Ohm.

        +-----------------------+
        | **Supported Devices** |
        +-----------------------+
        | PXIe-5110             |
        +-----------------------+
        | PXIe-5111             |
        +-----------------------+
        | PXIe-5113             |
        +-----------------------+
        | PXIe-5160             |
        +-----------------------+
        | PXIe-5162             |
        +-----------------------+

        .. note:: the input impedance of the channel(s) to convey the CableSense signal must be set to 50 ohms.

        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +----------------+----------------------+
            | Characteristic | Value                |
            +================+======================+
            | Datatype       | enums.CableSenseMode |
            +----------------+----------------------+
            | Permissions    | read-write           |
            +----------------+----------------------+
            | Channel Based  | No                   |
            +----------------+----------------------+
            | Resettable     | Yes                  |
            +----------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_CABLE_SENSE_MODE**

cable_sense_signal_enable
-------------------------

    .. py:attribute:: cable_sense_signal_enable

        TBD

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_CABLE_SENSE_SIGNAL_ENABLE**

cable_sense_voltage
-------------------

    .. py:attribute:: cable_sense_voltage

        Returns the voltage of the CableSense signal that is written to the EEPROM of the oscilloscope during factory calibration.

        +-----------------------+
        | **Supported Devices** |
        +-----------------------+
        | PXIe-5110             |
        +-----------------------+
        | PXIe-5111             |
        +-----------------------+
        | PXIe-5113             |
        +-----------------------+
        | PXIe-5160             |
        +-----------------------+
        | PXIe-5162             |
        +-----------------------+

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_CABLE_SENSE_VOLTAGE**

channel_count
-------------

    .. py:attribute:: channel_count

        Indicates the number of channels that the specific instrument driver supports.
        For channel-based properties, the IVI engine maintains a separate cache value for each channel.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Channel Count**
                - C Attribute: **NISCOPE_ATTR_CHANNEL_COUNT**

channel_enabled
---------------

    .. py:attribute:: channel_enabled

        Specifies whether the digitizer acquires a waveform for the channel.
        Valid Values:
        True  (1) - Acquire data on this channel
        False (0) - Don't acquire data on this channel




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Channel Enabled**
                - C Attribute: **NISCOPE_ATTR_CHANNEL_ENABLED**

channel_terminal_configuration
------------------------------

    .. py:attribute:: channel_terminal_configuration

        Specifies the terminal configuration for the channel.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------------------------+
            | Characteristic | Value                       |
            +================+=============================+
            | Datatype       | enums.TerminalConfiguration |
            +----------------+-----------------------------+
            | Permissions    | read-write                  |
            +----------------+-----------------------------+
            | Channel Based  | Yes                         |
            +----------------+-----------------------------+
            | Resettable     | Yes                         |
            +----------------+-----------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Channel Terminal Configuration**
                - C Attribute: **NISCOPE_ATTR_CHANNEL_TERMINAL_CONFIGURATION**

data_transfer_block_size
------------------------

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
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Fetch:Data Transfer Block Size**
                - C Attribute: **NISCOPE_ATTR_DATA_TRANSFER_BLOCK_SIZE**

data_transfer_maximum_bandwidth
-------------------------------

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
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Fetch:Advanced:Maximum Bandwidth**
                - C Attribute: **NISCOPE_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH**

data_transfer_preferred_packet_size
-----------------------------------

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
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Fetch:Advanced:Preferred Packet Size**
                - C Attribute: **NISCOPE_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE**

device_temperature
------------------

    .. py:attribute:: device_temperature

        Returns the temperature of the device in degrees Celsius from the onboard sensor.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device:Temperature**
                - C Attribute: **NISCOPE_ATTR_DEVICE_TEMPERATURE**

enabled_channels
----------------

    .. py:attribute:: enabled_channels

        Returns a comma-separated list of the channels enabled for the session in ascending order.

        If no channels are enabled, this property returns an empty string, "".
        If all channels are enabled, this property enumerates all of the channels.

        Because this property returns channels in ascending order, but the order in which you specify channels for the input is important, the value of this property may not necessarily reflect the order in which NI-SCOPE performs certain actions.

        Refer to Channel String Syntax in the NI High-Speed Digitizers Help for more information on the effects of channel order in NI-SCOPE.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_ENABLED_CHANNELS**

enable_dc_restore
-----------------

    .. py:attribute:: enable_dc_restore

        Restores the video-triggered data retrieved by the digitizer to the video signal's zero reference point.
        Valid Values:
        True - Enable DC restore
        False - Disable DC restore

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Video:Enable DC Restore**
                - C Attribute: **NISCOPE_ATTR_ENABLE_DC_RESTORE**

enable_time_interleaved_sampling
--------------------------------

    .. py:attribute:: enable_time_interleaved_sampling

        Specifies whether the digitizer acquires the waveform using multiple ADCs for the channel enabling a higher maximum real-time sampling rate.
        Valid Values:
        True  (1) - Use multiple interleaved ADCs on this channel
        False (0) - Use only this channel's ADC to acquire data for this channel




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Enable Time Interleaved Sampling**
                - C Attribute: **NISCOPE_ATTR_ENABLE_TIME_INTERLEAVED_SAMPLING**

end_of_acquisition_event_output_terminal
----------------------------------------

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
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:End of Acquisition:Output Terminal**
                - C Attribute: **NISCOPE_ATTR_END_OF_ACQUISITION_EVENT_OUTPUT_TERMINAL**

end_of_record_event_output_terminal
-----------------------------------

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
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:End of Record:Output Terminal**
                - C Attribute: **NISCOPE_ATTR_END_OF_RECORD_EVENT_OUTPUT_TERMINAL**

end_of_record_to_advance_trigger_holdoff
----------------------------------------

    .. py:attribute:: end_of_record_to_advance_trigger_holdoff

        End of Record to Advance Trigger Holdoff is the length of time (in
        seconds) that a device waits between the completion of one record and
        the acquisition of pre-trigger samples for the next record. During this
        time, the acquisition engine state delays the transition to the Wait for
        Advance Trigger state, and will not store samples in onboard memory,
        accept an Advance Trigger, or trigger on the input signal..
        **Supported Devices**: NI 5185/5186

        The following table lists the characteristics of this property.

            +----------------+----------------------------------------+
            | Characteristic | Value                                  |
            +================+========================================+
            | Datatype       | float in seconds or datetime.timedelta |
            +----------------+----------------------------------------+
            | Permissions    | read-write                             |
            +----------------+----------------------------------------+
            | Channel Based  | No                                     |
            +----------------+----------------------------------------+
            | Resettable     | Yes                                    |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:End of Record to Advance Trigger Holdoff**
                - C Attribute: **NISCOPE_ATTR_END_OF_RECORD_TO_ADVANCE_TRIGGER_HOLDOFF**

equalization_filter_enabled
---------------------------

    .. py:attribute:: equalization_filter_enabled

        Enables the onboard signal processing FIR block. This block is connected directly to the input signal.  This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. However, since this is a generic FIR filter any coefficients are valid.  Coefficients should be between +1 and -1 in value.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Onboard Signal Processing:Equalization:Equalization Filter Enabled**
                - C Attribute: **NISCOPE_ATTR_EQUALIZATION_FILTER_ENABLED**

equalization_num_coefficients
-----------------------------

    .. py:attribute:: equalization_num_coefficients

        Returns the number of coefficients that the FIR filter can accept.  This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer.  However, since this is a generic FIR filter any coefficients are valid.  Coefficients should be between +1 and -1 in value.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Onboard Signal Processing:Equalization:Equalization Num Coefficients**
                - C Attribute: **NISCOPE_ATTR_EQUALIZATION_NUM_COEFFICIENTS**

exported_advance_trigger_output_terminal
----------------------------------------

    .. py:attribute:: exported_advance_trigger_output_terminal

        Specifies the destination to export the advance trigger.  When the advance trigger is received, the digitizer begins acquiring samples for the Nth record.
        Consult your device documentation for a specific list of valid destinations.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Advance Trigger:Output Terminal**
                - C Attribute: **NISCOPE_ATTR_EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL**

exported_ref_trigger_output_terminal
------------------------------------

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
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Output Terminal**
                - C Attribute: **NISCOPE_ATTR_EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL**

exported_start_trigger_output_terminal
--------------------------------------

    .. py:attribute:: exported_start_trigger_output_terminal

        Specifies the destination to export the Start trigger.  When the start trigger is received, the digitizer begins acquiring samples.
        Consult your device documentation for a specific list of valid destinations.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Start Trigger (Acq. Arm):Output Terminal**
                - C Attribute: **NISCOPE_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL**

flex_fir_antialias_filter_type
------------------------------

    .. py:attribute:: flex_fir_antialias_filter_type

        The NI 5922 flexible-resolution digitizer uses an onboard FIR lowpass antialias filter.
        Use this property to select from several types of filters to achieve desired filtering characteristics.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+----------------------------------+
            | Characteristic | Value                            |
            +================+==================================+
            | Datatype       | enums.FlexFIRAntialiasFilterType |
            +----------------+----------------------------------+
            | Permissions    | read-write                       |
            +----------------+----------------------------------+
            | Channel Based  | Yes                              |
            +----------------+----------------------------------+
            | Resettable     | Yes                              |
            +----------------+----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:Flex FIR Antialias Filter Type**
                - C Attribute: **NISCOPE_ATTR_FLEX_FIR_ANTIALIAS_FILTER_TYPE**

fpga_bitfile_path
-----------------

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
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device:FPGA Bitfile Path**
                - C Attribute: **NISCOPE_ATTR_FPGA_BITFILE_PATH**

glitch_condition
----------------

    .. py:attribute:: glitch_condition

        Specifies whether the oscilloscope triggers on pulses of duration less than or greater than the value specified by the :py:attr:`niscope.Session.glitch_width` property.

        The following table lists the characteristics of this property.

            +----------------+-----------------------+
            | Characteristic | Value                 |
            +================+=======================+
            | Datatype       | enums.GlitchCondition |
            +----------------+-----------------------+
            | Permissions    | read-write            |
            +----------------+-----------------------+
            | Channel Based  | No                    |
            +----------------+-----------------------+
            | Resettable     | Yes                   |
            +----------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_GLITCH_CONDITION**

glitch_polarity
---------------

    .. py:attribute:: glitch_polarity

        Specifies the polarity of pulses that trigger the oscilloscope for glitch triggering.

        The following table lists the characteristics of this property.

            +----------------+----------------------+
            | Characteristic | Value                |
            +================+======================+
            | Datatype       | enums.GlitchPolarity |
            +----------------+----------------------+
            | Permissions    | read-write           |
            +----------------+----------------------+
            | Channel Based  | No                   |
            +----------------+----------------------+
            | Resettable     | Yes                  |
            +----------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_GLITCH_POLARITY**

glitch_width
------------

    .. py:attribute:: glitch_width

        Specifies the glitch duration, in seconds.

        The oscilloscope triggers when it detects of pulse of duration either less than or greater than this value depending on the value of the :py:attr:`niscope.Session.glitch_condition` property.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_GLITCH_WIDTH**

high_pass_filter_frequency
--------------------------

    .. py:attribute:: high_pass_filter_frequency

        Specifies the frequency for the highpass filter in Hz. The device uses
        one of the valid values listed below. If an invalid value is specified,
        no coercion occurs. The default value is 0.
        **(PXIe-5164) Valid Values:**
        0 90 450
        **Related topics:**
        `Digital Filtering <digitizers.chm::/Digital_Filtering_Overview.html>`__




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:High Pass Filter Frequency**
                - C Attribute: **NISCOPE_ATTR_HIGH_PASS_FILTER_FREQUENCY**

horz_enforce_realtime
---------------------

    .. py:attribute:: horz_enforce_realtime

        Indicates whether the digitizer enforces real-time measurements or allows equivalent-time measurements.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Enforce Realtime**
                - C Attribute: **NISCOPE_ATTR_HORZ_ENFORCE_REALTIME**

horz_min_num_pts
----------------

    .. py:attribute:: horz_min_num_pts

        Specifies the minimum number of points you require in the waveform record for each channel.  NI-SCOPE uses the value you specify to configure the record length that the digitizer uses for waveform acquisition. :py:attr:`niscope.Session.horz_record_length` returns the actual record length.
        Valid Values: 1 - available onboard memory

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Min Number of Points**
                - C Attribute: **NISCOPE_ATTR_HORZ_MIN_NUM_PTS**

horz_num_records
----------------

    .. py:attribute:: horz_num_records

        Specifies the number of records to acquire. Can be used for multi-record acquisition and single-record acquisitions. Setting this to 1 indicates a single-record acquisition.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Number of Records**
                - C Attribute: **NISCOPE_ATTR_HORZ_NUM_RECORDS**

horz_record_length
------------------

    .. py:attribute:: horz_record_length

        Returns the actual number of points the digitizer acquires for each channel.  The value is equal to or greater than the minimum number of points you specify with :py:attr:`niscope.Session.horz_min_num_pts`.
        Allocate a ViReal64 array of this size or greater to pass as the WaveformArray parameter of the Read and Fetch methods. This property is only valid after a call to the one of the Configure Horizontal methods.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Actual Record Length**
                - C Attribute: **NISCOPE_ATTR_HORZ_RECORD_LENGTH**

horz_record_ref_position
------------------------

    .. py:attribute:: horz_record_ref_position

        Specifies the position of the Reference Event in the waveform record.  When the digitizer detects a trigger, it waits the length of time the :py:attr:`niscope.Session.trigger_delay_time` property specifies. The event that occurs when the delay time elapses is the Reference Event. The Reference Event is relative to the start of the record and is a percentage of the record length. For example, the value 50.0 corresponds to the center of the waveform record and 0.0 corresponds to the first element in the waveform record.
        Valid Values: 0.0 - 100.0

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Reference Position**
                - C Attribute: **NISCOPE_ATTR_HORZ_RECORD_REF_POSITION**

horz_sample_rate
----------------

    .. py:attribute:: horz_sample_rate

        Returns the effective sample rate using the current configuration. The units are samples per second.  This property is only valid after a call to the one of the Configure Horizontal methods.
        Units: Hertz (Samples / Second)

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Actual Sample Rate**
                - C Attribute: **NISCOPE_ATTR_HORZ_SAMPLE_RATE**

horz_time_per_record
--------------------

    .. py:attribute:: horz_time_per_record

        Specifies the length of time that corresponds to the record length.
        Units: Seconds

        The following table lists the characteristics of this property.

            +----------------+----------------------------------------+
            | Characteristic | Value                                  |
            +================+========================================+
            | Datatype       | float in seconds or datetime.timedelta |
            +----------------+----------------------------------------+
            | Permissions    | read-write                             |
            +----------------+----------------------------------------+
            | Channel Based  | No                                     |
            +----------------+----------------------------------------+
            | Resettable     | Yes                                    |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Advanced:Time Per Record**
                - C Attribute: **NISCOPE_ATTR_HORZ_TIME_PER_RECORD**

input_clock_source
------------------

    .. py:attribute:: input_clock_source

        Specifies the input source for the PLL reference clock (the 1 MHz to 20 MHz clock on the NI 5122, the 10 MHz clock for the NI 5112/5620/5621/5911) to which the digitizer will be phase-locked; for the NI 5102, this is the source of the board clock.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Reference (Input) Clock Source**
                - C Attribute: **NISCOPE_ATTR_INPUT_CLOCK_SOURCE**

input_impedance
---------------

    .. py:attribute:: input_impedance

        Specifies the input impedance for the channel in Ohms.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Input Impedance**
                - C Attribute: **NISCOPE_ATTR_INPUT_IMPEDANCE**

instrument_firmware_revision
----------------------------

    .. py:attribute:: instrument_firmware_revision

        A string that contains the firmware revision information for the instrument you are currently using.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Firmware Revision**
                - C Attribute: **NISCOPE_ATTR_INSTRUMENT_FIRMWARE_REVISION**

instrument_manufacturer
-----------------------

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
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Manufacturer**
                - C Attribute: **NISCOPE_ATTR_INSTRUMENT_MANUFACTURER**

instrument_model
----------------

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
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Instrument Identification:Model**
                - C Attribute: **NISCOPE_ATTR_INSTRUMENT_MODEL**

interleaving_offset_correction_enabled
--------------------------------------

    .. py:attribute:: interleaving_offset_correction_enabled

        Enables the interleaving offset correction on the specified channel. The
        default value is TRUE.
        **Related topics:**
        `Timed Interleaved
        Sampling <digitizers.chm::/TimeInterleavedSampling.html>`__



        .. note:: If disabled, warranted specifications are not guaranteed.


        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Advanced:Interleaving Offset Correction Enabled**
                - C Attribute: **NISCOPE_ATTR_INTERLEAVING_OFFSET_CORRECTION_ENABLED**

io_resource_descriptor
----------------------

    .. py:attribute:: io_resource_descriptor

        Indicates the resource descriptor the driver uses to identify the physical device.  If you initialize the driver with a logical name, this property contains the resource descriptor that corresponds to the entry in the IVI Configuration utility.
        If you initialize the instrument driver with the resource descriptor, this property contains that value.You can pass a logical name to :py:meth:`niscope.Session.Init` or :py:meth:`niscope.Session.__init__`. The IVI Configuration utility must contain an entry for the logical name. The logical name entry refers to a virtual instrument section in the IVI Configuration file. The virtual instrument section specifies a physical device and initial user options.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Resource Descriptor**
                - C Attribute: **NISCOPE_ATTR_IO_RESOURCE_DESCRIPTOR**

is_probe_comp_on
----------------

    .. py:attribute:: is_probe_comp_on

        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | bool      |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_IS_PROBE_COMP_ON**

logical_name
------------

    .. py:attribute:: logical_name

        A string containing the logical name you specified when opening the current IVI session.  You can pass a logical name to :py:meth:`niscope.Session.Init` or :py:meth:`niscope.Session.__init__`. The IVI Configuration utility must contain an entry for the logical name. The logical name entry refers to a virtual instrument section in the IVI Configuration file. The virtual instrument section specifies a physical device and initial user options.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Advanced Session Information:Logical Name**
                - C Attribute: **NISCOPE_ATTR_LOGICAL_NAME**

master_enable
-------------

    .. py:attribute:: master_enable

        Specifies whether you want the device to be a master or a slave. The master typically originates the trigger signal and clock sync pulse. For a standalone device, set this property to False.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Master Enable**
                - C Attribute: **NISCOPE_ATTR_MASTER_ENABLE**

max_input_frequency
-------------------

    .. py:attribute:: max_input_frequency

        Specifies the bandwidth of the channel. Express this value as the frequency at which the input circuitry attenuates the input signal by 3 dB. The units are hertz.
        Defined Values:
        :py:data:`~niscope.NISCOPE_VAL_BANDWIDTH_FULL` (-1.0)
        :py:data:`~niscope.NISCOPE_VAL_BANDWIDTH_DEVICE_DEFAULT` (0.0)
        :py:data:`~niscope.NISCOPE_VAL_20MHZ_BANDWIDTH` (20000000.0)
        :py:data:`~niscope.NISCOPE_VAL_100MHZ_BANDWIDTH` (100000000.0)
        :py:data:`~niscope.NISCOPE_VAL_20MHZ_MAX_INPUT_FREQUENCY` (20000000.0)
        :py:data:`~niscope.NISCOPE_VAL_100MHZ_MAX_INPUT_FREQUENCY` (100000000.0)



        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Maximum Input Frequency**
                - C Attribute: **NISCOPE_ATTR_MAX_INPUT_FREQUENCY**

max_real_time_sampling_rate
---------------------------

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
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Maximum Real Time Sample Rate**
                - C Attribute: **NISCOPE_ATTR_MAX_REAL_TIME_SAMPLING_RATE**

max_ris_rate
------------

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
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Maximum RIS Rate**
                - C Attribute: **NISCOPE_ATTR_MAX_RIS_RATE**

min_sample_rate
---------------

    .. py:attribute:: min_sample_rate

        Specify the sampling rate for the acquisition in Samples per second.
        Valid Values:
        The combination of sampling rate and min record length must allow the digitizer to sample at a valid sampling rate for the acquisition type specified in :py:meth:`niscope.Session.ConfigureAcquisition` and not require more memory than the onboard memory module allows.



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Min Sample Rate**
                - C Attribute: **NISCOPE_ATTR_MIN_SAMPLE_RATE**

onboard_memory_size
-------------------

    .. py:attribute:: onboard_memory_size

        Returns the total combined amount of onboard memory for all channels in bytes.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Memory Size**
                - C Attribute: **NISCOPE_ATTR_ONBOARD_MEMORY_SIZE**

output_clock_source
-------------------

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
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Output Clock Source**
                - C Attribute: **NISCOPE_ATTR_OUTPUT_CLOCK_SOURCE**

pll_lock_status
---------------

    .. py:attribute:: pll_lock_status

        If TRUE, the PLL has remained locked to the external reference clock since it was last checked. If FALSE,  the PLL has become unlocked from the external reference clock since it was last checked.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | bool      |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:PLL Lock Status**
                - C Attribute: **NISCOPE_ATTR_PLL_LOCK_STATUS**

points_done
-----------

    .. py:attribute:: points_done

        Actual number of samples acquired in the record specified by :py:attr:`niscope.Session.fetch_record_number` from the :py:attr:`niscope.Session.fetch_relative_to` and :py:attr:`niscope.Session.fetch_offset` properties.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Fetch:Points Done**
                - C Attribute: **NISCOPE_ATTR_POINTS_DONE**

poll_interval
-------------

    .. py:attribute:: poll_interval

        Specifies the poll interval in milliseconds to use during RIS acquisitions to check whether the acquisition is complete.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_POLL_INTERVAL**

probe_attenuation
-----------------

    .. py:attribute:: probe_attenuation

        Specifies the probe attenuation for the input channel. For example, for a 10:1 probe,  set this property to 10.0.
        Valid Values:
        Any positive real number. Typical values are 1, 10, and 100.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Probe Attenuation**
                - C Attribute: **NISCOPE_ATTR_PROBE_ATTENUATION**

ready_for_advance_event_output_terminal
---------------------------------------

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
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Ready for Advance:Output Terminal**
                - C Attribute: **NISCOPE_ATTR_READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL**

ready_for_ref_event_output_terminal
-----------------------------------

    .. py:attribute:: ready_for_ref_event_output_terminal

        Specifies the destination for the Ready for Reference Event.  When this event is asserted, the digitizer is ready to receive a reference trigger.
        Consult your device documentation for a specific list of valid destinations.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Ready for Reference:Output Terminal**
                - C Attribute: **NISCOPE_ATTR_READY_FOR_REF_EVENT_OUTPUT_TERMINAL**

ready_for_start_event_output_terminal
-------------------------------------

    .. py:attribute:: ready_for_start_event_output_terminal

        Specifies the destination for the Ready for Start Event.  When this event is asserted, the digitizer is ready to receive a start trigger.
        Consult your device documentation for a specific list of valid destinations.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Ready for Start:Output Terminal**
                - C Attribute: **NISCOPE_ATTR_READY_FOR_START_EVENT_OUTPUT_TERMINAL**

records_done
------------

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
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Fetch:Records Done**
                - C Attribute: **NISCOPE_ATTR_RECORDS_DONE**

record_arm_source
-----------------

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
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | No         |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Synchronization:Record Arm Source**
                - C Attribute: **NISCOPE_ATTR_RECORD_ARM_SOURCE**

ref_clk_rate
------------

    .. py:attribute:: ref_clk_rate

        If :py:attr:`niscope.Session.input_clock_source` is an external source, this property specifies the frequency of the input,  or reference clock, to which the internal sample clock timebase is synchronized. The frequency is in hertz.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Reference Clock Rate**
                - C Attribute: **NISCOPE_ATTR_REF_CLK_RATE**

ref_trigger_detector_location
-----------------------------

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
            | Channel Based  | No                               |
            +----------------+----------------------------------+
            | Resettable     | Yes                              |
            +----------------+----------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Onboard Signal Processing:Ref Trigger Detection Location**
                - C Attribute: **NISCOPE_ATTR_REF_TRIGGER_DETECTOR_LOCATION**

ref_trigger_minimum_quiet_time
------------------------------

    .. py:attribute:: ref_trigger_minimum_quiet_time

        The amount of time the trigger circuit must not detect a signal above the trigger level before the trigger is armed.  This property is useful for triggering at the beginning and not in the middle of signal bursts.

        The following table lists the characteristics of this property.

            +----------------+----------------------------------------+
            | Characteristic | Value                                  |
            +================+========================================+
            | Datatype       | float in seconds or datetime.timedelta |
            +----------------+----------------------------------------+
            | Permissions    | read-write                             |
            +----------------+----------------------------------------+
            | Channel Based  | No                                     |
            +----------------+----------------------------------------+
            | Resettable     | Yes                                    |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Onboard Signal Processing:Ref Trigger Min Quiet Time**
                - C Attribute: **NISCOPE_ATTR_REF_TRIGGER_MINIMUM_QUIET_TIME**

ref_trig_tdc_enable
-------------------

    .. py:attribute:: ref_trig_tdc_enable

        This property controls whether the TDC is used to compute an accurate trigger.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:Advanced:Enable TDC**
                - C Attribute: **NISCOPE_ATTR_REF_TRIG_TDC_ENABLE**

resolution
----------

    .. py:attribute:: resolution

        Indicates the bit width of valid data (as opposed to padding bits) in the acquired waveform. Compare to :py:attr:`niscope.Session.binary_sample_width`.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | int       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Resolution**
                - C Attribute: **NISCOPE_ATTR_RESOLUTION**

ris_in_auto_setup_enable
------------------------

    .. py:attribute:: ris_in_auto_setup_enable

        Indicates whether the digitizer should use RIS sample rates when searching for a frequency in autosetup.
        Valid Values:
        True  (1) - Use RIS sample rates in autosetup
        False (0) - Do not use RIS sample rates in autosetup

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Advanced:Enable RIS in Auto Setup**
                - C Attribute: **NISCOPE_ATTR_RIS_IN_AUTO_SETUP_ENABLE**

ris_method
----------

    .. py:attribute:: ris_method

        Specifies the algorithm for random-interleaved sampling, which is used if the sample rate exceeds the value of :py:attr:`niscope.Session.max_real_time_sampling_rate`.

        The following table lists the characteristics of this property.

            +----------------+-----------------+
            | Characteristic | Value           |
            +================+=================+
            | Datatype       | enums.RISMethod |
            +----------------+-----------------+
            | Permissions    | read-write      |
            +----------------+-----------------+
            | Channel Based  | No              |
            +----------------+-----------------+
            | Resettable     | Yes             |
            +----------------+-----------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:RIS Method**
                - C Attribute: **NISCOPE_ATTR_RIS_METHOD**

ris_num_averages
----------------

    .. py:attribute:: ris_num_averages

        The number of averages for each bin in an RIS acquisition.  The number of averages times the oversampling factor is the minimum number of real-time acquisitions necessary to reconstruct the RIS waveform.  Averaging is useful in RIS because the trigger times are not evenly spaced, so adjacent points in the reconstructed waveform not be accurately spaced.  By averaging, the errors in both time and voltage are smoothed.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Horizontal:RIS Num Avg**
                - C Attribute: **NISCOPE_ATTR_RIS_NUM_AVERAGES**

runt_high_threshold
-------------------

    .. py:attribute:: runt_high_threshold

        Specifies the higher of two thresholds, in volts, that bound the vertical range to examine for runt pulses.

        The runt threshold that causes the oscilloscope to trigger depends on the runt polarity you select. Refer to the :py:attr:`niscope.Session.runt_polarity` property for more information.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_RUNT_HIGH_THRESHOLD**

runt_low_threshold
------------------

    .. py:attribute:: runt_low_threshold

        Specifies the lower of two thresholds, in volts, that bound the vertical range to examine for runt pulses.

        The runt threshold that causes the oscilloscope to trigger depends on the runt polarity you select. Refer to the :py:attr:`niscope.Session.runt_polarity` property for more information.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_RUNT_LOW_THRESHOLD**

runt_polarity
-------------

    .. py:attribute:: runt_polarity

        Specifies the polarity of pulses that trigger the oscilloscope for runt triggering.

        When set to :py:data:`~niscope.RuntPolarity.POSITIVE`, the oscilloscope triggers when the following conditions are met:
            * The leading edge of a pulse crosses the :py:attr:`niscope.Session.runt_low_threshold` in a positive direction;
            * The trailing edge of the pulse crosses the :py:attr:`niscope.Session.runt_low_threshold` in a negative direction; and
            * No portion of the pulse crosses the :py:attr:`niscope.Session.runt_high_threshold`.

        When set to :py:data:`~niscope.RuntPolarity.NEGATIVE`, the oscilloscope triggers when the following conditions are met:
            * The leading edge of a pulse crosses the :py:attr:`niscope.Session.runt_high_threshold` in a negative direction;
            * The trailing edge of the pulse crosses the :py:attr:`niscope.Session.runt_high_threshold` in a positive direction; and
            * No portion of the pulse crosses the :py:attr:`niscope.Session.runt_low_threshold`.

        When set to :py:data:`~niscope.RuntPolarity.EITHER`, the oscilloscope triggers in either case.

        The following table lists the characteristics of this property.

            +----------------+--------------------+
            | Characteristic | Value              |
            +================+====================+
            | Datatype       | enums.RuntPolarity |
            +----------------+--------------------+
            | Permissions    | read-write         |
            +----------------+--------------------+
            | Channel Based  | No                 |
            +----------------+--------------------+
            | Resettable     | Yes                |
            +----------------+--------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_RUNT_POLARITY**

runt_time_condition
-------------------

    .. py:attribute:: runt_time_condition

        Specifies whether runt triggers are time qualified, and if so, how the oscilloscope triggers in relation to the duration range bounded by the :py:attr:`niscope.Session.runt_time_low_limit` and :py:attr:`niscope.Session.runt_time_high_limit` properties.

        The following table lists the characteristics of this property.

            +----------------+-------------------------+
            | Characteristic | Value                   |
            +================+=========================+
            | Datatype       | enums.RuntTimeCondition |
            +----------------+-------------------------+
            | Permissions    | read-write              |
            +----------------+-------------------------+
            | Channel Based  | No                      |
            +----------------+-------------------------+
            | Resettable     | Yes                     |
            +----------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_RUNT_TIME_CONDITION**

runt_time_high_limit
--------------------

    .. py:attribute:: runt_time_high_limit

        Specifies, in seconds, the high runt threshold time.

        This property sets the upper bound on the duration of runt pulses that may trigger the oscilloscope. The :py:attr:`niscope.Session.runt_time_condition` property determines how the oscilloscope triggers in relation to the runt time limits.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_RUNT_TIME_HIGH_LIMIT**

runt_time_low_limit
-------------------

    .. py:attribute:: runt_time_low_limit

        Specifies, in seconds, the low runt threshold time.

        This property sets the lower bound on the duration of runt pulses that may trigger the oscilloscope. The :py:attr:`niscope.Session.runt_time_condition` property determines how the oscilloscope triggers in relation to the runt time limits.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_RUNT_TIME_LOW_LIMIT**

sample_mode
-----------

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
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Acquisition:Sample Mode**
                - C Attribute: **NISCOPE_ATTR_SAMPLE_MODE**

samp_clk_timebase_div
---------------------

    .. py:attribute:: samp_clk_timebase_div

        If :py:attr:`niscope.Session.samp_clk_timebase_src` is an external source, specifies the ratio between the sample clock timebase rate and the actual sample rate, which can be slower.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Sample Clock Timebase Divisor**
                - C Attribute: **NISCOPE_ATTR_SAMP_CLK_TIMEBASE_DIV**

sample_clock_timebase_multiplier
--------------------------------

    .. py:attribute:: sample_clock_timebase_multiplier

        If :py:attr:`niscope.Session.samp_clk_timebase_src` is an external source, this property specifies the ratio between the :py:attr:`niscope.Session.samp_clk_timebase_rate` and the actual sample rate, which can be higher. This property can be used in conjunction with :py:attr:`niscope.Session.samp_clk_timebase_div`.
        Some devices use multiple ADCs to sample the same channel at an effective sample rate that is greater than the specified clock rate. When providing an external sample clock use this property to indicate when you want a higher sample rate. Valid values for this property vary by device and current configuration.

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
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_SAMP_CLK_TIMEBASE_MULT**

samp_clk_timebase_rate
----------------------

    .. py:attribute:: samp_clk_timebase_rate

        If :py:attr:`niscope.Session.samp_clk_timebase_src` is an external source, specifies the frequency in hertz of the external clock used as the timebase source.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Sample Clock Timebase Rate**
                - C Attribute: **NISCOPE_ATTR_SAMP_CLK_TIMEBASE_RATE**

samp_clk_timebase_src
---------------------

    .. py:attribute:: samp_clk_timebase_src

        Specifies the source of the sample clock timebase, which is the timebase used to control waveform sampling.  The actual sample rate may be the timebase itself or a divided version of the timebase, depending on the :py:attr:`niscope.Session.min_sample_rate` (for internal sources) or the :py:attr:`niscope.Session.samp_clk_timebase_div` (for external sources).

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | str        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Clocking:Sample Clock Timebase Source**
                - C Attribute: **NISCOPE_ATTR_SAMP_CLK_TIMEBASE_SRC**

serial_number
-------------

    .. py:attribute:: serial_number

        Returns the serial number of the device.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Device:Serial Number**
                - C Attribute: **NISCOPE_ATTR_SERIAL_NUMBER**

accessory_gain
--------------

    .. py:attribute:: accessory_gain

        Returns the calibration gain for the current device configuration.

        **Related topics:**
        `NI 5122/5124/5142 Calibration <digitizers.chm::/5122_Calibration.html>`__



        .. note:: This property is supported only by the NI PXI-5900 differential amplifier.


        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_SIGNAL_COND_GAIN**

accessory_offset
----------------

    .. py:attribute:: accessory_offset

        Returns the calibration offset for the current device configuration.

        **Related topics:**
        `NI 5122/5124/5142 Calibration <digitizers.chm::/5122_Calibration.html>`__



        .. note:: This property is supported only by the NI PXI-5900 differential amplifier.


        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | float     |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | Yes       |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_SIGNAL_COND_OFFSET**

simulate
--------

    .. py:attribute:: simulate

        Specifies whether or not to simulate instrument driver I/O operations.  If simulation is enabled, instrument driver methods perform range checking and call Ivi_GetAttribute and Ivi_SetAttribute methods, but they do not perform instrument I/O.  For output parameters that represent instrument data, the instrument driver methods return calculated values.
        The default value is False.  Use the :py:meth:`niscope.Session.__init__` method to override this value.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:User Options:Simulate**
                - C Attribute: **NISCOPE_ATTR_SIMULATE**

specific_driver_description
---------------------------

    .. py:attribute:: specific_driver_description

        A string that contains a brief description of the specific driver

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Description**
                - C Attribute: **NISCOPE_ATTR_SPECIFIC_DRIVER_DESCRIPTION**

specific_driver_revision
------------------------

    .. py:attribute:: specific_driver_revision

        A string that contains additional version information about this instrument driver.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | str       |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Revision**
                - C Attribute: **NISCOPE_ATTR_SPECIFIC_DRIVER_REVISION**

specific_driver_vendor
----------------------

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
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Identification:Driver Vendor**
                - C Attribute: **NISCOPE_ATTR_SPECIFIC_DRIVER_VENDOR**

start_to_ref_trigger_holdoff
----------------------------

    .. py:attribute:: start_to_ref_trigger_holdoff

        Pass the length of time you want the digitizer to wait after it starts acquiring data until the digitizer enables the trigger system to detect a reference (stop) trigger.
        Units: Seconds
        Valid Values: 0.0 - 171.8

        The following table lists the characteristics of this property.

            +----------------+----------------------------------------+
            | Characteristic | Value                                  |
            +================+========================================+
            | Datatype       | float in seconds or datetime.timedelta |
            +----------------+----------------------------------------+
            | Permissions    | read-write                             |
            +----------------+----------------------------------------+
            | Channel Based  | No                                     |
            +----------------+----------------------------------------+
            | Resettable     | Yes                                    |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Start To Ref Trigger Holdoff**
                - C Attribute: **NISCOPE_ATTR_START_TO_REF_TRIGGER_HOLDOFF**

supported_instrument_models
---------------------------

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
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models**
                - C Attribute: **NISCOPE_ATTR_SUPPORTED_INSTRUMENT_MODELS**

trigger_auto_triggered
----------------------

    .. py:attribute:: trigger_auto_triggered

        Specifies if the last acquisition was auto triggered.  You can use the Auto Triggered property to find out if the last acquisition was triggered.

        The following table lists the characteristics of this property.

            +----------------+-----------+
            | Characteristic | Value     |
            +================+===========+
            | Datatype       | bool      |
            +----------------+-----------+
            | Permissions    | read only |
            +----------------+-----------+
            | Channel Based  | No        |
            +----------------+-----------+
            | Resettable     | No        |
            +----------------+-----------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Auto Triggered**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_AUTO_TRIGGERED**

trigger_coupling
----------------

    .. py:attribute:: trigger_coupling

        Specifies how the digitizer couples the trigger source. This property affects instrument operation only when :py:attr:`niscope.Session.trigger_type` is set to :py:data:`~niscope.TriggerType.EDGE`, :py:data:`~niscope.TriggerType.HYSTERESIS`, or :py:data:`~niscope.TriggerType.WINDOW`.

        The following table lists the characteristics of this property.

            +----------------+-----------------------+
            | Characteristic | Value                 |
            +================+=======================+
            | Datatype       | enums.TriggerCoupling |
            +----------------+-----------------------+
            | Permissions    | read-write            |
            +----------------+-----------------------+
            | Channel Based  | No                    |
            +----------------+-----------------------+
            | Resettable     | Yes                   |
            +----------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Coupling**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_COUPLING**

trigger_delay_time
------------------

    .. py:attribute:: trigger_delay_time

        Specifies the trigger delay time in seconds. The trigger delay time is the length of time the digitizer waits after it receives the trigger. The event that occurs when the trigger delay elapses is the Reference Event.
        Valid Values: 0.0 - 171.8

        The following table lists the characteristics of this property.

            +----------------+----------------------------------------+
            | Characteristic | Value                                  |
            +================+========================================+
            | Datatype       | float in seconds or datetime.timedelta |
            +----------------+----------------------------------------+
            | Permissions    | read-write                             |
            +----------------+----------------------------------------+
            | Channel Based  | No                                     |
            +----------------+----------------------------------------+
            | Resettable     | Yes                                    |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Delay**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_DELAY_TIME**

trigger_holdoff
---------------

    .. py:attribute:: trigger_holdoff

        Specifies the length of time (in seconds) the digitizer waits after detecting a trigger before enabling the trigger subsystem to detect another trigger. This property affects instrument operation only when the digitizer requires multiple acquisitions to build a complete waveform. The digitizer requires multiple waveform acquisitions when it uses equivalent-time sampling or when the digitizer is configured for a multi-record acquisition through a call to :py:meth:`niscope.Session.configure_horizontal_timing`.
        Valid Values: 0.0 - 171.8

        The following table lists the characteristics of this property.

            +----------------+----------------------------------------+
            | Characteristic | Value                                  |
            +================+========================================+
            | Datatype       | float in seconds or datetime.timedelta |
            +----------------+----------------------------------------+
            | Permissions    | read-write                             |
            +----------------+----------------------------------------+
            | Channel Based  | No                                     |
            +----------------+----------------------------------------+
            | Resettable     | Yes                                    |
            +----------------+----------------------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Holdoff**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_HOLDOFF**

trigger_hysteresis
------------------

    .. py:attribute:: trigger_hysteresis

        Specifies the size of the hysteresis window on either side of the trigger level.  The digitizer triggers when the trigger signal passes through the threshold you specify with the Trigger Level parameter, has the slope you specify with the Trigger Slope parameter,  and passes through the hysteresis window that you specify with this parameter.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Hysteresis**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_HYSTERESIS**

trigger_impedance
-----------------

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
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Impedance**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_IMPEDANCE**

trigger_level
-------------

    .. py:attribute:: trigger_level

        Specifies the voltage threshold for the trigger subsystem. The units are volts.  This property affects instrument behavior only when the :py:attr:`niscope.Session.trigger_type` is set to :py:data:`~niscope.TriggerType.EDGE`, :py:data:`~niscope.TriggerType.HYSTERESIS`, or :py:data:`~niscope.TriggerType.WINDOW`.
        Valid Values:
        The values of the range and offset parameters in :py:meth:`niscope.Session.configure_vertical` determine the valid range for the trigger level on the channel you use as the Trigger Source. The value you pass for this parameter must meet the following conditions:

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Level**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_LEVEL**

trigger_modifier
----------------

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
            | Channel Based  | No                    |
            +----------------+-----------------------+
            | Resettable     | Yes                   |
            +----------------+-----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Modifier**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_MODIFIER**

trigger_slope
-------------

    .. py:attribute:: trigger_slope

        Specifies if a rising or a falling edge triggers the digitizer.  This property affects instrument operation only when :py:attr:`niscope.Session.trigger_type` is set to :py:data:`~niscope.TriggerType.EDGE`, :py:data:`~niscope.TriggerType.HYSTERESIS`, or :py:data:`~niscope.TriggerType.WINDOW`.

        The following table lists the characteristics of this property.

            +----------------+--------------------+
            | Characteristic | Value              |
            +================+====================+
            | Datatype       | enums.TriggerSlope |
            +----------------+--------------------+
            | Permissions    | read-write         |
            +----------------+--------------------+
            | Channel Based  | No                 |
            +----------------+--------------------+
            | Resettable     | Yes                |
            +----------------+--------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Slope**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_SLOPE**

trigger_source
--------------

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
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Source**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_SOURCE**

trigger_type
------------

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
            | Channel Based  | No                |
            +----------------+-------------------+
            | Resettable     | Yes               |
            +----------------+-------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Type**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_TYPE**

trigger_window_high_level
-------------------------

    .. py:attribute:: trigger_window_high_level

        Pass the upper voltage threshold you want the digitizer to use for window triggering.
        The digitizer triggers when the trigger signal enters or leaves the window you specify with :py:attr:`niscope.Session.trigger_window_low_level` and :py:attr:`niscope.Session.trigger_window_high_level`
        Valid Values:
        The values of the Vertical Range and Vertical Offset parameters in :py:meth:`niscope.Session.configure_vertical` determine the valid range for the High Window Level on the channel you use as the Trigger Source parameter in :py:meth:`niscope.Session.ConfigureTriggerSource`.  The value you pass for this parameter must meet the following conditions.
        High Trigger Level <= Vertical Range/2 + Vertical Offset
        High Trigger Level >= (-Vertical Range/2) + Vertical Offset
        High Trigger Level > Low Trigger Level



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Window:High Level**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_WINDOW_HIGH_LEVEL**

trigger_window_low_level
------------------------

    .. py:attribute:: trigger_window_low_level

        Pass the lower voltage threshold you want the digitizer to use for window triggering.
        The digitizer triggers when the trigger signal enters or leaves the window you specify with :py:attr:`niscope.Session.trigger_window_low_level` and :py:attr:`niscope.Session.trigger_window_high_level`.
        Units: Volts
        Valid Values:
        The values of the Vertical Range and Vertical Offset parameters in :py:meth:`niscope.Session.configure_vertical` determine the valid range for the Low Window Level on the channel you use as the Trigger Source parameter in :py:meth:`niscope.Session.ConfigureTriggerSource`.  The value you pass for this parameter must meet the following conditions.
        Low Trigger Level <= Vertical Range/2 + Vertical Offset
        Low Trigger Level >= (-Vertical Range/2) + Vertical Offset
        Low Trigger Level < High Trigger Level



        .. note:: One or more of the referenced methods are not in the Python API for this driver.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Window:Low Level**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_WINDOW_LOW_LEVEL**

trigger_window_mode
-------------------

    .. py:attribute:: trigger_window_mode

        Specifies whether you want a trigger to occur when the signal enters or leaves the window specified by :py:attr:`niscope.Session.trigger_window_low_level`, or :py:attr:`niscope.Session.trigger_window_high_level`.

        The following table lists the characteristics of this property.

            +----------------+-------------------------+
            | Characteristic | Value                   |
            +================+=========================+
            | Datatype       | enums.TriggerWindowMode |
            +----------------+-------------------------+
            | Permissions    | read-write              |
            +----------------+-------------------------+
            | Channel Based  | No                      |
            +----------------+-------------------------+
            | Resettable     | Yes                     |
            +----------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Window:Window Mode**
                - C Attribute: **NISCOPE_ATTR_TRIGGER_WINDOW_MODE**

tv_trigger_event
----------------

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
            | Channel Based  | No                      |
            +----------------+-------------------------+
            | Resettable     | Yes                     |
            +----------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Video:Event**
                - C Attribute: **NISCOPE_ATTR_TV_TRIGGER_EVENT**

tv_trigger_line_number
----------------------

    .. py:attribute:: tv_trigger_line_number

        Specifies the line on which to trigger, if :py:attr:`niscope.Session.tv_trigger_event` is set to line number. The valid ranges of the property depend on the signal format selected.  M-NTSC has a valid range of 1 to 525.  B/G-PAL, SECAM, 576i, and 576p have a valid range of 1 to 625. 720p has a valid range of 1 to 750. 1080i and 1080p have a valid range of 1125.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | int        |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Video:Line Number**
                - C Attribute: **NISCOPE_ATTR_TV_TRIGGER_LINE_NUMBER**

tv_trigger_polarity
-------------------

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
            | Channel Based  | No                  |
            +----------------+---------------------+
            | Resettable     | Yes                 |
            +----------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Video:Polarity**
                - C Attribute: **NISCOPE_ATTR_TV_TRIGGER_POLARITY**

tv_trigger_signal_format
------------------------

    .. py:attribute:: tv_trigger_signal_format

        Specifies the type of video signal, such as NTSC, PAL, or SECAM.

        The following table lists the characteristics of this property.

            +----------------+-------------------------+
            | Characteristic | Value                   |
            +================+=========================+
            | Datatype       | enums.VideoSignalFormat |
            +----------------+-------------------------+
            | Permissions    | read-write              |
            +----------------+-------------------------+
            | Channel Based  | No                      |
            +----------------+-------------------------+
            | Resettable     | Yes                     |
            +----------------+-------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Triggering:Trigger Video:Signal Format**
                - C Attribute: **NISCOPE_ATTR_TV_TRIGGER_SIGNAL_FORMAT**

use_spec_initial_x
------------------

    .. py:attribute:: use_spec_initial_x

        

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | bool       |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_USE_SPEC_INITIAL_X**

vertical_coupling
-----------------

    .. py:attribute:: vertical_coupling

        Specifies how the digitizer couples the input signal for the channel.  When input coupling changes, the input stage takes a finite amount of time to settle.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+------------------------+
            | Characteristic | Value                  |
            +================+========================+
            | Datatype       | enums.VerticalCoupling |
            +----------------+------------------------+
            | Permissions    | read-write             |
            +----------------+------------------------+
            | Channel Based  | Yes                    |
            +----------------+------------------------+
            | Resettable     | Yes                    |
            +----------------+------------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Vertical Coupling**
                - C Attribute: **NISCOPE_ATTR_VERTICAL_COUPLING**

vertical_offset
---------------

    .. py:attribute:: vertical_offset

        Specifies the location of the center of the range. The value is with respect to ground and is in volts.  For example, to acquire a sine wave that spans between 0.0 and 10.0 V, set this property to 5.0 V.



        .. note:: This property is not supported by all digitizers.Refer to the NI High-Speed Digitizers Help for a list of vertical offsets supported for each device.


        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Vertical Offset**
                - C Attribute: **NISCOPE_ATTR_VERTICAL_OFFSET**

vertical_range
--------------

    .. py:attribute:: vertical_range

        Specifies the absolute value of the input range for a channel in volts.  For example, to acquire a sine wave that spans between -5 and +5 V, set this property to 10.0 V.
        Refer to the NI High-Speed Digitizers Help for a list of supported vertical ranges for each device.  If the specified range is not supported by a device, the value is coerced up to the next valid range.




        .. tip:: This property can use repeated capabilities. If set or get directly on the
            niscope.Session object, then the set/get will use all repeated capabilities in the session.
            You can specify a subset of repeated capabilities using the Python index notation on an
            niscope.Session repeated capabilities container, and calling set/get value on the result.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | Yes        |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - LabVIEW Property: **Vertical:Vertical Range**
                - C Attribute: **NISCOPE_ATTR_VERTICAL_RANGE**

width_condition
---------------

    .. py:attribute:: width_condition

        Specifies whether the oscilloscope triggers on pulses within or outside the duration range bounded by the :py:attr:`niscope.Session.width_low_threshold` and :py:attr:`niscope.Session.width_high_threshold` properties.

        The following table lists the characteristics of this property.

            +----------------+----------------------+
            | Characteristic | Value                |
            +================+======================+
            | Datatype       | enums.WidthCondition |
            +----------------+----------------------+
            | Permissions    | read-write           |
            +----------------+----------------------+
            | Channel Based  | No                   |
            +----------------+----------------------+
            | Resettable     | Yes                  |
            +----------------+----------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_WIDTH_CONDITION**

width_high_threshold
--------------------

    .. py:attribute:: width_high_threshold

        Specifies the high width threshold, in seconds.

        This properties sets the upper bound on the duration range that triggers the oscilloscope. The :py:attr:`niscope.Session.width_condition` property determines how the oscilloscope triggers in relation to the width thresholds.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_WIDTH_HIGH_THRESHOLD**

width_low_threshold
-------------------

    .. py:attribute:: width_low_threshold

        Specifies the low width threshold, in seconds.

        This property sets the lower bound on the duration range that triggers the oscilloscope. The :py:attr:`niscope.Session.width_condition` property determines how the oscilloscope triggers in relation to the width thresholds.

        The following table lists the characteristics of this property.

            +----------------+------------+
            | Characteristic | Value      |
            +================+============+
            | Datatype       | float      |
            +----------------+------------+
            | Permissions    | read-write |
            +----------------+------------+
            | Channel Based  | No         |
            +----------------+------------+
            | Resettable     | Yes        |
            +----------------+------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_WIDTH_LOW_THRESHOLD**

width_polarity
--------------

    .. py:attribute:: width_polarity

        Specifies the polarity of pulses that trigger the oscilloscope for width triggering.

        The following table lists the characteristics of this property.

            +----------------+---------------------+
            | Characteristic | Value               |
            +================+=====================+
            | Datatype       | enums.WidthPolarity |
            +----------------+---------------------+
            | Permissions    | read-write          |
            +----------------+---------------------+
            | Channel Based  | No                  |
            +----------------+---------------------+
            | Resettable     | Yes                 |
            +----------------+---------------------+

        .. tip::
            This property corresponds to the following LabVIEW Property or C Attribute:

                - C Attribute: **NISCOPE_ATTR_WIDTH_POLARITY**


NI-TClk Support
===============

    .. py:attribute:: tclk

        This is used to get and set NI-TClk attributes on the session.

        .. seealso:: See :py:attr:`nitclk.SessionReference` for a complete list of attributes.


.. contents:: Session


