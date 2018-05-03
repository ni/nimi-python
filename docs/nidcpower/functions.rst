nidcpower.Session methods
=========================

.. py:currentmodule:: nidcpower.Session

.. py:method:: abort()

    Transitions the NI-DCPower session from the Running state to the
    Committed state. If a sequence is running, it is stopped. Any
    configuration methods called after this method are not applied until
    the :py:meth:`nidcpower.Session._initiate` method is called. If power output is enabled
    when you call the :py:meth:`nidcpower.Session.abort` method, the output channels remain
    in their current state and continue providing power.

    Use the :py:meth:`nidcpower.Session.ConfigureOutputEnabled` method to disable power
    output on a per channel basis. Use the :py:meth:`nidcpower.Session.reset` method to
    disable output on all channels.

    Refer to the `Programming
    States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
    the *NI DC Power Supplies and SMUs Help* for information about the
    specific NI-DCPower software states.

    **Related Topics:**

    `Programming
    States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

    

    .. note:: One or more of the referenced methods are not in the Python API for this driver.



.. py:method:: commit()

    Applies previously configured settings to the device. Calling this
    method moves the NI-DCPower session from the Uncommitted state into
    the Committed state. After calling this method, modifying any
    property reverts the NI-DCPower session to the Uncommitted state. Use
    the :py:meth:`nidcpower.Session._initiate` method to transition to the Running state.
    Refer to the `Programming
    States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
    the *NI DC Power Supplies and SMUs Help* for details about the specific
    NI-DCPower software states.

    **Related Topics:**

    `Programming
    States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__

    



.. py:method:: configure_aperture_time(aperture_time, units=nidcpower.ApertureTimeUnits.SECONDS)

    Configures the aperture time on the specified channel(s).

    The supported values depend on the **units**. Refer to the *Aperture
    Time* topic for your device in the *NI DC Power Supplies and SMUs Help*
    for more information. In general, devices support discrete
    **apertureTime** values, and if you configure **apertureTime** to some
    unsupported value, NI-DCPower coerces it up to the next supported value.

    Refer to the *Measurement Configuration and Timing* or *DC Noise
    Rejection* topic for your device in the *NI DC Power Supplies and SMUs
    Help* for more information about how to configure your measurements.

    **Related Topics:**

    `Aperture Time <REPLACE_DRIVER_SPECIFIC_URL_1(aperture)>`__

    

    .. note:: This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].configure_aperture_time(aperture_time, units=nidcpower.ApertureTimeUnits.SECONDS)


    :param aperture_time:


        Specifies the aperture time. Refer to the *Aperture Time* topic for your
        device in the *NI DC Power Supplies and SMUs Help* for more information.

        


    :type aperture_time: float
    :param units:


        Specifies the units for **apertureTime**.
        **Defined Values**:

        +------------------------------------------------------------------+------------------------------+
        | :py:data:`~nidcpower.ApertureTimeUnits.SECONDS` (1028)           | Specifies seconds.           |
        +------------------------------------------------------------------+------------------------------+
        | :py:data:`~nidcpower.ApertureTimeUnits.POWER_LINE_CYCLES` (1029) | Specifies Power Line Cycles. |
        +------------------------------------------------------------------+------------------------------+


    :type units: :py:data:`nidcpower.ApertureTimeUnits`

.. py:method:: configure_digital_edge_measure_trigger(input_terminal, edge=nidcpower.DigitalEdge.RISING)

    Configures the Measure trigger for digital edge triggering.

    

    .. note:: This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :param input_terminal:


        Specifies the input terminal for the digital edge Measure trigger.

        You can specify any valid input terminal for this method. Valid
        terminals are listed in MAX under the **Device Routes** tab. For
        PXIe-4162/4163, refer to the Signal Routing topic for the device to
        determine which routes are available. This information is not available
        on a Device Routes tab in MAX.

        Input terminals can be specified in one of two ways. If the device is
        named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
        with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
        shortened terminal name, PXI_Trig0. The input terminal can also be a
        terminal from another device. For example, you can set the input
        terminal on Dev1 to be /Dev2/SourceCompleteEvent.

        


    :type input_terminal: str
    :param edge:


        Specifies whether to configure the Measure trigger to assert on the
        rising or falling edge.
        **Defined Values:**

        +--------------------------------------------------+----------------------------------------------------------------+
        | :py:data:`~nidcpower.DigitalEdge.RISING` (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
        +--------------------------------------------------+----------------------------------------------------------------+
        | :py:data:`~nidcpower.DigitalEdge.FALLING` (1017) | Asserts the trigger on the falling edge of the digital signal. |
        +--------------------------------------------------+----------------------------------------------------------------+


    :type edge: :py:data:`nidcpower.DigitalEdge`

.. py:method:: configure_digital_edge_pulse_trigger(input_terminal, edge=nidcpower.DigitalEdge.RISING)

    Configures the Pulse trigger for digital edge triggering.

    

    .. note:: This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :param input_terminal:


        Specifies the input terminal for the digital edge Pulse trigger.

        You can specify any valid input terminal for this method. Valid
        terminals are listed in MAX under the **Device Routes** tab.

        Input terminals can be specified in one of two ways. If the device is
        named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
        with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
        shortened terminal name, PXI_Trig0. The input terminal can also be a
        terminal from another device. For example, you can set the input
        terminal on Dev1 to be /Dev2/SourceCompleteEvent.

        


    :type input_terminal: str
    :param edge:


        Specifies whether to configure the Pulse trigger to assert on the rising
        or falling edge.
        **Defined Values:**

        +--------------------------------------------------+----------------------------------------------------------------+
        | :py:data:`~nidcpower.DigitalEdge.RISING` (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
        +--------------------------------------------------+----------------------------------------------------------------+
        | :py:data:`~nidcpower.DigitalEdge.FALLING` (1017) | Asserts the trigger on the falling edge of the digital signal. |
        +--------------------------------------------------+----------------------------------------------------------------+


    :type edge: :py:data:`nidcpower.DigitalEdge`

.. py:method:: configure_digital_edge_sequence_advance_trigger(input_terminal, edge=nidcpower.DigitalEdge.RISING)

    Configures the Sequence Advance trigger for digital edge triggering.

    

    .. note:: This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :param input_terminal:


        Specifies the input terminal for the digital edge Sequence Advance
        trigger.

        You can specify any valid input terminal for this method. Valid
        terminals are listed in MAX under the **Device Routes** tab. For
        PXIe-4162/4163, refer to the Signal Routing topic for the device to
        determine which routes are available. This information is not available
        on a Device Routes tab in MAX.

        Input terminals can be specified in one of two ways. If the device is
        named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
        with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
        shortened terminal name, PXI_Trig0. The input terminal can also be a
        terminal from another device. For example, you can set the input
        terminal on Dev1 to be /Dev2/SourceCompleteEvent.

        


    :type input_terminal: str
    :param edge:


        Specifies whether to configure the Sequence Advance trigger to assert on
        the rising or falling edge.
        **Defined Values:**

        +--------------------------------------------------+----------------------------------------------------------------+
        | :py:data:`~nidcpower.DigitalEdge.RISING` (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
        +--------------------------------------------------+----------------------------------------------------------------+
        | :py:data:`~nidcpower.DigitalEdge.FALLING` (1017) | Asserts the trigger on the falling edge of the digital signal. |
        +--------------------------------------------------+----------------------------------------------------------------+


    :type edge: :py:data:`nidcpower.DigitalEdge`

.. py:method:: configure_digital_edge_source_trigger(input_terminal, edge=nidcpower.DigitalEdge.RISING)

    Configures the Source trigger for digital edge triggering.

    

    .. note:: This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :param input_terminal:


        Specifies the input terminal for the digital edge Source trigger.

        You can specify any valid input terminal for this method. Valid
        terminals are listed in MAX under the **Device Routes** tab. For
        PXIe-4162/4163, refer to the Signal Routing topic for the device to
        determine which routes are available. This information is not available
        on a Device Routes tab in MAX.

        Input terminals can be specified in one of two ways. If the device is
        named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
        with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
        shortened terminal name, PXI_Trig0. The input terminal can also be a
        terminal from another device. For example, you can set the input
        terminal on Dev1 to be /Dev2/SourceCompleteEvent.

        


    :type input_terminal: str
    :param edge:


        Specifies whether to configure the Source trigger to assert on the
        rising or falling edge.
        **Defined Values:**

        +--------------------------------------------------+----------------------------------------------------------------+
        | :py:data:`~nidcpower.DigitalEdge.RISING` (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
        +--------------------------------------------------+----------------------------------------------------------------+
        | :py:data:`~nidcpower.DigitalEdge.FALLING` (1017) | Asserts the trigger on the falling edge of the digital signal. |
        +--------------------------------------------------+----------------------------------------------------------------+


    :type edge: :py:data:`nidcpower.DigitalEdge`

.. py:method:: configure_digital_edge_start_trigger(input_terminal, edge=nidcpower.DigitalEdge.RISING)

    Configures the Start trigger for digital edge triggering.

    

    .. note:: This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :param input_terminal:


        Specifies the input terminal for the digital edge Start trigger.

        You can specify any valid input terminal for this method. Valid
        terminals are listed in MAX under the **Device Routes** tab. For
        PXIe-4162/4163, refer to the Signal Routing topic for the device to
        determine which routes are available. This information is not available
        on a Device Routes tab in MAX.

        Input terminals can be specified in one of two ways. If the device is
        named Dev1 and your terminal is PXI_Trig0, you can specify the terminal
        with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the
        shortened terminal name, PXI_Trig0. The input terminal can also be a
        terminal from another device. For example, you can set the input
        terminal on Dev1 to be /Dev2/SourceCompleteEvent.

        


    :type input_terminal: str
    :param edge:


        Specifies whether to configure the Start trigger to assert on the rising
        or falling edge.
        **Defined Values:**

        +--------------------------------------------------+----------------------------------------------------------------+
        | :py:data:`~nidcpower.DigitalEdge.RISING` (1016)  | Asserts the trigger on the rising edge of the digital signal.  |
        +--------------------------------------------------+----------------------------------------------------------------+
        | :py:data:`~nidcpower.DigitalEdge.FALLING` (1017) | Asserts the trigger on the falling edge of the digital signal. |
        +--------------------------------------------------+----------------------------------------------------------------+


    :type edge: :py:data:`nidcpower.DigitalEdge`

.. py:method:: disable()

    This method performs the same actions as the :py:meth:`nidcpower.Session.reset`
    method, except that this method also immediately sets the
    :py:data:`nidcpower.Session.output_enabled` property to False.

    This method opens the output relay on devices that have an output
    relay.

    



.. py:method:: export_signal(signal, output_terminal, signal_identifier="")

    Routes signals (triggers and events) to the output terminal you specify.
    The route is created when the session is :py:meth:`nidcpower.Session.commit`.

    **Related Topics:**

    `Triggers <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__

    

    .. note:: This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :param signal:


        Specifies which trigger or event to export.
        **Defined Values:**

        +-----------------------------------------------------------------------------+------------------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.SOURCE_COMPLETE_EVENT` (1030)             | Exports the Source Complete event.             |
        +-----------------------------------------------------------------------------+------------------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.MEASURE_COMPLETE_EVENT` (1031)            | Exports the Measure Complete event.            |
        +-----------------------------------------------------------------------------+------------------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.SEQUENCE_ITERATION_COMPLETE_EVENT` (1032) | Exports the Sequence Iteration Complete event. |
        +-----------------------------------------------------------------------------+------------------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.SEQUENCE_ENGINE_DONE_EVENT` (1033)        | Exports the Sequence Engine Done event.        |
        +-----------------------------------------------------------------------------+------------------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.PULSE_COMPLETE_EVENT` (1051)              | Exports the Pulse Complete event.              |
        +-----------------------------------------------------------------------------+------------------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.READY_FOR_PULSE_TRIGGER_EVENT` (1052)     | Exports the Ready Pulse Trigger event.         |
        +-----------------------------------------------------------------------------+------------------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.START_TRIGGER` (1034)                     | Exports the Start trigger.                     |
        +-----------------------------------------------------------------------------+------------------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.SOURCE_TRIGGER` (1035)                    | Exports the Source trigger.                    |
        +-----------------------------------------------------------------------------+------------------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.MEASURE_TRIGGER` (1036)                   | Exports the Measure trigger.                   |
        +-----------------------------------------------------------------------------+------------------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.SEQUENCE_ADVANCE_TRIGGER` (1037)          | Exports the Sequence Advance trigger.          |
        +-----------------------------------------------------------------------------+------------------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.PULSE_TRIGGER` (1053)                     | Exports the Pulse trigger.                     |
        +-----------------------------------------------------------------------------+------------------------------------------------+


    :type signal: :py:data:`nidcpower.ExportSignal`
    :param output_terminal:


        Specifies where to export the selected signal.
        **Relative Terminals**:

        +-------------+----------------------+
        | ""          | Do not export signal |
        +-------------+----------------------+
        | "PXI_Trig0" | PXI trigger line 0   |
        +-------------+----------------------+
        | "PXI_Trig1" | PXI trigger line 1   |
        +-------------+----------------------+
        | "PXI_Trig2" | PXI trigger line 2   |
        +-------------+----------------------+
        | "PXI_Trig3" | PXI trigger line 3   |
        +-------------+----------------------+
        | "PXI_Trig4" | PXI trigger line 4   |
        +-------------+----------------------+
        | "PXI_Trig5" | PXI trigger line 5   |
        +-------------+----------------------+
        | "PXI_Trig6" | PXI trigger line 6   |
        +-------------+----------------------+
        | "PXI_Trig7" | PXI trigger line 7   |
        +-------------+----------------------+


    :type output_terminal: str
    :param signal_identifier:


        Reserved for future use. Pass in an empty string for this parameter.

        


    :type signal_identifier: str

.. py:method:: fetch_multiple(count, timeout=datetime.timedelta(seconds=1.0))

    Returns a list of named tuples (Measurement) that were
    previously taken and are stored in the NI-DCPower buffer. This method
    should not be used when the :py:data:`nidcpower.Session.measure_when` property is
    set to :py:data:`~nidcpower.MeasureWhen.ON_DEMAND`. You must first call
    :py:meth:`nidcpower.Session._initiate` before calling this method.

    Fields in Measurement:

    - **voltage** (float)
    - **current** (float)
    - **in_compliance** (bool)

    

    .. note:: This method is not supported on all devices. Refer to `Supported Methods by Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm, supportedfunctions)>`__ for more information about supported devices.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].fetch_multiple(count, timeout=datetime.timedelta(seconds=1.0))


    :param count:


        Specifies the number of measurements to fetch.

        


    :type count: int
    :param timeout:


        Specifies the maximum time allowed for this method to complete. If the method does not complete within this time interval, NI-DCPower returns an error.

        

        .. note:: When setting the timeout interval, ensure you take into account any triggers so that the timeout interval is long enough for your application.


    :type timeout: float in seconds or datetime.timedelta

    :rtype: list of Measurement
    :return:


            List of named tuples with fields:

            - **voltage** (float)
            - **current** (float)
            - **in_compliance** (bool)

            



.. py:method:: get_channel_name(index)

    Retrieves the output **channelName** that corresponds to the requested
    **index**. Use the :py:data:`nidcpower.Session.channel_count` property to
    determine the upper bound of valid values for **index**.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].get_channel_name(index)


    :param index:


        Specifies which output channel name to return. The index values begin at
        1.

        


    :type index: int

.. py:method:: get_ext_cal_last_date_and_time()

    Returns the date and time of the last successful calibration.

    



    :rtype: datetime.datetime
    :return:


            Indicates date and time of the last calibration.

            



.. py:method:: get_ext_cal_last_temp()

    Returns the onboard **temperature** of the device, in degrees Celsius,
    during the last successful external calibration.

    



    :rtype: float
    :return:


            Returns the onboard **temperature** of the device, in degrees Celsius,
            during the last successful external calibration.

            



.. py:method:: get_ext_cal_recommended_interval()

    Returns the recommended maximum interval, in **months**, between
    external calibrations.

    



    :rtype: datetime.timedelta
    :return:


            Specifies the recommended maximum interval, in **months**, between
            external calibrations.

            



.. py:method:: get_self_cal_last_date_and_time()

    Returns the date and time of the oldest successful self-calibration from among the channels in the session.

    

    .. note:: This method is not supported on all devices.



    :rtype: datetime.datetime
    :return:


            Returns the date and time the device was last calibrated.

            



.. py:method:: get_self_cal_last_temp()

    Returns the onboard temperature of the device, in degrees Celsius,
    during the oldest successful self-calibration from among the channels in
    the session.

    For example, if you have a session using channels 1 and 2, and you
    perform a self-calibration on channel 1 with a device temperature of 25
    degrees Celsius at 2:00, and a self-calibration was performed on channel
    2 at 27 degrees Celsius at 3:00 on the same day, this method returns
    25 for the **temperature** parameter.

    

    .. note:: This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :rtype: float
    :return:


            Returns the onboard **temperature** of the device, in degrees Celsius,
            during the oldest successful calibration.

            



.. py:method:: lock_session(caller_has_lock=None)

    | Obtains a multithread lock on the device session. Before doing so, the
      software waits until all other execution threads release their locks
      on the device session.
    | Other threads may have obtained a lock on this session for the
      following reasons:

    -  The application called the :py:meth:`nidcpower.Session.lock_session` method.
    -  A call to NI-DCPower locked the session.
    -  A call to the IVI engine locked the session.
    -  After a call to the :py:meth:`nidcpower.Session.lock_session` method returns
       successfully, no other threads can access the device session until
       you call the :py:meth:`nidcpower.Session.unlock_session` method.
    -  Use the :py:meth:`nidcpower.Session.lock_session` method and the
       :py:meth:`nidcpower.Session.unlock_session` method around a sequence of calls to
       instrument driver methods if you require that the device retain its
       settings through the end of the sequence.

    You can safely make nested calls to the :py:meth:`nidcpower.Session.lock_session` method
    within the same thread. To completely unlock the session, you must
    balance each call to the :py:meth:`nidcpower.Session.lock_session` method with a call to
    the :py:meth:`nidcpower.Session.unlock_session` method. If, however, you use
    **Caller_Has_Lock** in all calls to the :py:meth:`nidcpower.Session.lock_session` and
    :py:meth:`nidcpower.Session.unlock_session` method within a method, the IVI Library
    locks the session only once within the method regardless of the number
    of calls you make to the :py:meth:`nidcpower.Session.lock_session` method. This behavior
    allows you to call the :py:meth:`nidcpower.Session.unlock_session` method just once at
    the end of the method.





    :param caller_has_lock:


        This parameter is optional. If you do not want to use this parameter, pass None.

        Use this parameter in complex methods to keep track of whether you
        obtain a lock and therefore need to unlock the session. Pass False to the initial
        lock_session call and store the return value into a variable. Pass in the variable as well
        as putting the return value into the same variable for each call to lock_session or
        unlock_session.




    :type caller_has_lock: bool

    :rtype: bool
    :return:


            This parameter is optional. If you do not want to use this parameter, pass None.

            Use this parameter in complex methods to keep track of whether you
            obtain a lock and therefore need to unlock the session. Pass False to the initial
            lock_session call and store the return value into a variable. Pass in the variable as well
            as putting the return value into the same variable for each call to lock_session or
            unlock_session.




.. py:method:: measure(measurement_type)

    Returns the measured value of either the voltage or current on the
    specified output channel. Each call to this method blocks other
    method calls until the hardware returns the **measurement**. To
    measure multiple output channels, use the :py:meth:`nidcpower.Session.measure_multiple`
    method.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].measure(measurement_type)


    :param measurement_type:


        Specifies whether a voltage or current value is measured.
        **Defined Values**:

        +----------------------------------------------------+------------------------------+
        | :py:data:`~nidcpower.MeasurementTypes.VOLTAGE` (1) | The device measures voltage. |
        +----------------------------------------------------+------------------------------+
        | :py:data:`~nidcpower.MeasurementTypes.CURRENT` (0) | The device measures current. |
        +----------------------------------------------------+------------------------------+


    :type measurement_type: :py:data:`nidcpower.MeasurementTypes`

    :rtype: float
    :return:


            Returns the value of the measurement, either in volts for voltage or
            amps for current.

            



.. py:method:: measure_multiple()

    Returns a list of named tuples (Measurement) containing the measured voltage
    and current values on the specified output channel(s). Each call to this method
    blocks other method calls until the measurements are returned from the device.
    The order of the measurements returned in the array corresponds to the order
    on the specified output channel(s).

    Fields in Measurement:

    - **voltage** (float)
    - **current** (float)
    - **in_compliance** (bool) - Always None

    

    .. note:: This method is not supported on all devices. Refer to `Supported Methods by Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm, supportedfunctions)>`__ for more information about supported devices.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].measure_multiple()


    :rtype: list of Measurement
    :return:


            List of named tuples with fields:

            - **voltage** (float)
            - **current** (float)
            - **in_compliance** (bool) - Always None

            



.. py:method:: query_in_compliance()

    Queries the specified output device to determine if it is operating at
    the `compliance <REPLACE_DRIVER_SPECIFIC_URL_2(compliance)>`__ limit.

    The compliance limit is the current limit when the output method is
    set to :py:data:`~nidcpower.OutputFunction.DC_VOLTAGE`. If the output is operating at the
    compliance limit, the output reaches the current limit before the
    desired voltage level. Refer to the :py:meth:`nidcpower.Session.ConfigureOutputFunction`
    method and the :py:meth:`nidcpower.Session.ConfigureCurrentLimit` method for more
    information about output method and current limit, respectively.

    The compliance limit is the voltage limit when the output method is
    set to :py:data:`~nidcpower.OutputFunction.DC_CURRENT`. If the output is operating at the
    compliance limit, the output reaches the voltage limit before the
    desired current level. Refer to the :py:meth:`nidcpower.Session.ConfigureOutputFunction`
    method and the :py:meth:`nidcpower.Session.ConfigureVoltageLimit` method for more
    information about output method and voltage limit, respectively.

    **Related Topics:**

    `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__

    

    .. note:: One or more of the referenced methods are not in the Python API for this driver.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].query_in_compliance()


    :rtype: bool
    :return:


            Returns whether the device output channel is in compliance.

            



.. py:method:: query_max_current_limit(voltage_level)

    Queries the maximum current limit on an output channel if the output
    channel is set to the specified **voltageLevel**.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].query_max_current_limit(voltage_level)


    :param voltage_level:


        Specifies the voltage level to use when calculating the
        **maxCurrentLimit**.

        


    :type voltage_level: float

    :rtype: float
    :return:


            Returns the maximum current limit that can be set with the specified
            **voltageLevel**.

            



.. py:method:: query_max_voltage_level(current_limit)

    Queries the maximum voltage level on an output channel if the output
    channel is set to the specified **currentLimit**.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].query_max_voltage_level(current_limit)


    :param current_limit:


        Specifies the current limit to use when calculating the
        **maxVoltageLevel**.

        


    :type current_limit: float

    :rtype: float
    :return:


            Returns the maximum voltage level that can be set on an output channel
            with the specified **currentLimit**.

            



.. py:method:: query_min_current_limit(voltage_level)

    Queries the minimum current limit on an output channel if the output
    channel is set to the specified **voltageLevel**.

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].query_min_current_limit(voltage_level)


    :param voltage_level:


        Specifies the voltage level to use when calculating the
        **minCurrentLimit**.

        


    :type voltage_level: float

    :rtype: float
    :return:


            Returns the minimum current limit that can be set on an output channel
            with the specified **voltageLevel**.

            



.. py:method:: query_output_state(output_state)

    Queries the specified output channel to determine if the output channel
    is currently in the state specified by **outputState**.

    **Related Topics:**

    `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__

    


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].query_output_state(output_state)


    :param output_state:


        Specifies the output state of the output channel that is being queried.
        **Defined Values**:

        +------------------------------------------------+-------------------------------------------------------------------+
        | :py:data:`~nidcpower.OutputStates.VOLTAGE` (0) | The device maintains a constant voltage by adjusting the current. |
        +------------------------------------------------+-------------------------------------------------------------------+
        | :py:data:`~nidcpower.OutputStates.CURRENT` (1) | The device maintains a constant current by adjusting the voltage. |
        +------------------------------------------------+-------------------------------------------------------------------+


    :type output_state: :py:data:`nidcpower.OutputStates`

    :rtype: bool
    :return:


            Returns whether the device output channel is in the specified output
            state.

            



.. py:method:: read_current_temperature()

    Returns the current onboard **temperature**, in degrees Celsius, of the
    device.

    



    :rtype: float
    :return:


            Returns the onboard **temperature**, in degrees Celsius, of the device.

            



.. py:method:: reset()

    Resets the device to a known state. This method disables power
    generation, resets session properties to their default values, commits
    the session properties, and leaves the session in the Uncommitted state.
    Refer to the `Programming
    States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
    more information about NI-DCPower software states.

    



.. py:method:: reset_device()

    Resets the device to a known state. The method disables power
    generation, resets session properties to their default values, clears
    errors such as overtemperature and unexpected loss of auxiliary power,
    commits the session properties, and leaves the session in the
    Uncommitted state. This method also performs a hard reset on the
    device and driver software. This method has the same functionality as
    using reset in Measurement & Automation Explorer. Refer to the
    `Programming
    States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for
    more information about NI-DCPower software states.

    This will also open the output relay on devices that have an output
    relay.

    



.. py:method:: reset_with_defaults()

    Resets the device to a known state. This method disables power
    generation, resets session properties to their default values, commits
    the session properties, and leaves the session in the
    `Running <javascript:LaunchHelp('NI_DC_Power_Supplies_Help.chm::/programmingStates.html#running')>`__
    state. In addition to exhibiting the behavior of the :py:meth:`nidcpower.Session.reset`
    method, this method can assign user-defined default values for
    configurable properties from the IVI configuration.

    



.. py:method:: self_cal()

    Performs a self-calibration upon the specified channel(s).

    This method disables the output, performs several internal
    calculations, and updates calibration values. The updated calibration
    values are written to the device hardware if the
    :py:data:`nidcpower.Session.self_calibration_persistence` property is set to
    :py:data:`~nidcpower.SelfCalibrationPersistence.WRITE_TO_EEPROM`. Refer to the
    :py:data:`nidcpower.Session.self_calibration_persistence` property topic for more
    information about the settings for this property.

    When calling :py:meth:`nidcpower.Session.self_cal` with the PXIe-4162/4163,
    specify all channels of your PXIe-4162/4163 with the channelName input.
    You cannot self-calibrate a subset of PXIe-4162/4163 channels.

    Refer to the
    `Self-Calibration <REPLACE_DRIVER_SPECIFIC_URL_1(selfcal)>`__ topic for
    more information about this method.

    **Related Topics:**

    `Self-Calibration <REPLACE_DRIVER_SPECIFIC_URL_1(selfcal)>`__

    

    .. note:: This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].self_cal()


.. py:method:: self_test()

    Performs the device self-test routine and returns the test result(s).
    Calling this method implicitly calls the :py:meth:`nidcpower.Session.reset` method.

    When calling :py:meth:`nidcpower.Session.self_test` with the PXIe-4162/4163, specify all
    channels of your PXIe-4162/4163 with the channels input of
    :py:meth:`nidcpower.Session.__init__`. You cannot self test a subset of
    PXIe-4162/4163 channels.

    Raises `SelfTestError` on self test failure. Properties on exception object:

    - code - failure code from driver
    - message - status message from driver

    +----------------+-------------------+
    | Self-Test Code | Description       |
    +================+===================+
    | 0              | Self test passed. |
    +----------------+-------------------+
    | 1              | Self test failed. |
    +----------------+-------------------+



.. py:method:: send_software_edge_trigger(trigger=nidcpower.SendSoftwareEdgeTriggerType.START)

    Asserts the specified trigger. This method can override an external
    edge trigger.

    **Related Topics:**

    `Triggers <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__

    

    .. note:: This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :param trigger:


        Specifies which trigger to assert.
        **Defined Values:**

        +--------------------------------------------------------------------+---------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.START_TRIGGER` (1034)            | Asserts the Start trigger.            |
        +--------------------------------------------------------------------+---------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.SOURCE_TRIGGER` (1035)           | Asserts the Source trigger.           |
        +--------------------------------------------------------------------+---------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.MEASURE_TRIGGER` (1036)          | Asserts the Measure trigger.          |
        +--------------------------------------------------------------------+---------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.SEQUENCE_ADVANCE_TRIGGER` (1037) | Asserts the Sequence Advance trigger. |
        +--------------------------------------------------------------------+---------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.PULSE_TRIGGER` (1053             | Asserts the Pulse trigger.            |
        +--------------------------------------------------------------------+---------------------------------------+


    :type trigger: :py:data:`nidcpower.SendSoftwareEdgeTriggerType`

.. py:method:: set_sequence(values, source_delays)

    Configures a series of voltage or current outputs and corresponding
    source delays. The source mode must be set to
    `Sequence <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ for this
    method to take effect.

    Refer to the `Configuring the Source
    Unit <REPLACE_DRIVER_SPECIFIC_URL_1(configuringthesourceunit)>`__ topic
    in the *NI DC Power Supplies and SMUs Help* for more information about
    how to configure your device.

    Use this method in the Uncommitted or Committed programming states.
    Refer to the `Programming
    States <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in
    the *NI DC Power Supplies and SMUs Help* for more information about
    NI-DCPower programming states.

    

    .. note:: This method is not supported on all devices. Refer to `Supported
        Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.


    .. tip:: This method requires repeated capabilities (usually channels). If called directly on the
        nidcpower.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nidcpower.Session instance, and calling this method on the result.:

        .. code:: python

            session.channels['0,1'].set_sequence(values, source_delays)


    :param values:


        Specifies the series of voltage levels or current levels, depending on
        the configured `output
        method <REPLACE_DRIVER_SPECIFIC_URL_1(programming_output)>`__.
        **Valid values**:
        The valid values for this parameter are defined by the voltage level
        range or current level range.

        


    :type values: list of float
    :param source_delays:


        Specifies the source delay that follows the configuration of each value
        in the sequence.
        **Valid Values**:
        The valid values are between 0 and 167 seconds.

        


    :type source_delays: list of float

.. py:method:: unlock_session(caller_has_lock=None)

    Releases a lock that you acquired on an device session using
    :py:meth:`nidcpower.Session.lock_session`. Refer to :py:meth:`nidcpower.Session.lock_session` for additional
    information on session locks.





    :param caller_has_lock:


        This parameter is optional. If you do not want to use this parameter, pass None.

        Use this parameter in complex methods to keep track of whether you
        obtain a lock and therefore need to unlock the session. Pass False to the initial
        lock_session call and store the return value into a variable. Pass in the variable as well
        as putting the return value into the same variable for each call to lock_session or
        unlock_session.




    :type caller_has_lock: bool

    :rtype: bool
    :return:


            This parameter is optional. If you do not want to use this parameter, pass None.

            Use this parameter in complex methods to keep track of whether you
            obtain a lock and therefore need to unlock the session. Pass False to the initial
            lock_session call and store the return value into a variable. Pass in the variable as well
            as putting the return value into the same variable for each call to lock_session or
            unlock_session.



.. py:method:: wait_for_event(event_id, timeout=datetime.timedelta(seconds=10.0))

    Waits until the device has generated the specified event.

    The session monitors whether each type of event has occurred at least
    once since the last time this method or the :py:meth:`nidcpower.Session._initiate`
    method were called. If an event has only been generated once and you
    call this method successively, the method times out. Individual
    events must be generated between separate calls of this method.

    

    .. note:: Refer to `Supported Methods by
        Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__
        for more information about supported devices.



    :param event_id:


        Specifies which event to wait for.
        **Defined Values:**

        +-----------------------------------------------------------------------------+--------------------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.SOURCE_COMPLETE_EVENT` (1030)             | Waits for the Source Complete event.             |
        +-----------------------------------------------------------------------------+--------------------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.MEASURE_COMPLETE_EVENT` (1031)            | Waits for the Measure Complete event.            |
        +-----------------------------------------------------------------------------+--------------------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.SEQUENCE_ITERATION_COMPLETE_EVENT` (1032) | Waits for the Sequence Iteration Complete event. |
        +-----------------------------------------------------------------------------+--------------------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.SEQUENCE_ENGINE_DONE_EVENT` (1033)        | Waits for the Sequence Engine Done event.        |
        +-----------------------------------------------------------------------------+--------------------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.PULSE_COMPLETE_EVENT` (1051 )             | Waits for the Pulse Complete event.              |
        +-----------------------------------------------------------------------------+--------------------------------------------------+
        | :py:data:`~nidcpower.ExportSignal.READY_FOR_PULSE_TRIGGER_EVENT` (1052)     | Waits for the Ready for Pulse Trigger event.     |
        +-----------------------------------------------------------------------------+--------------------------------------------------+


    :type event_id: :py:data:`nidcpower.Event`
    :param timeout:


        Specifies the maximum time allowed for this method to complete, in
        seconds. If the method does not complete within this time interval,
        NI-DCPower returns an error.

        

        .. note:: When setting the timeout interval, ensure you take into account any
            triggers so that the timeout interval is long enough for your
            application.


    :type timeout: float in seconds or datetime.timedelta


