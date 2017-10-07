nidmm.Session methods
=====================

.. py:currentmodule:: nidmm

.. function:: configure_ac_bandwidth(ac_minimum_frequency_hz, ac_maximum_frequency_hz)

    Configures the :py:data:`nidmm.AC\_MIN\_FREQ` and :py:data:`nidmm.AC\_MAX\_FREQ`
    attributes, which the DMM uses for AC measurements.

    


    :param ac_minimum_frequency_hz:


        Specifies the minimum expected frequency component of the input signal
        in hertz. This parameter affects the DMM only when you set the
        :py:data:`nidmm.function` attribute to AC measurements. NI-DMM uses this
        parameter to calculate the proper aperture for the measurement.
        The driver sets the :py:data:`nidmm.AC\_MIN\_FREQ` attribute to this value.
        The valid range is 1 Hz–300 kHz for the NI 4080/4081/4082 and the NI
        4070/4071/4072, 10 Hz–100 Hz for the NI 4065, and 20 Hz–25 kHz for the
        NI 4050 and NI 4060.

        

    :type ac_minimum_frequency_hz: float
    :param ac_maximum_frequency_hz:


        Specifies the maximum expected frequency component of the input signal
        in hertz within the device limits. This parameter is used only for error
        checking and verifies that the value of this parameter is less than the
        maximum frequency of the device.

        This parameter affects the DMM only when you set the
        :py:data:`nidmm.function` attribute to AC measurements. The driver sets the
        :py:data:`nidmm.AC\_MAX\_FREQ` attribute to this value. The valid range is 1
        Hz–300 kHz for the NI 4080/4081/4082 and the NI 4070/4071/4072, 10
        Hz–100 Hz for the NI 4065, and 20 Hz–25 kHz for the NI 4050 and NI 4060.

        

    :type ac_maximum_frequency_hz: float

.. function:: configure_measurement_absolute(measurement_function, range, resolution_absolute)

    Configures the common attributes of the measurement. These attributes
    include :py:data:`nidmm.function`, :py:data:`nidmm.range`, and
    :py:data:`nidmm.RESOLUTION\_ABSOLUTE`.

    


    :param measurement_function:


        Specifies the **measurement\_function** used to acquire the measurement.
        The driver sets :py:data:`nidmm.function` to this value.

        

    :type measurement_function: :py:data:`nidmm.Function`
    :param range:


        Specifies the **range** for the function specified in the
        **Measurement\_Function** parameter. When frequency is specified in the
        **Measurement\_Function** parameter, you must supply the minimum
        frequency expected in the **range** parameter. For example, you must
        type in 100 Hz if you are measuring 101 Hz or higher.
        For all other functions, you must supply a **range** that exceeds the
        value that you are measuring. For example, you must type in 10 V if you
        are measuring 9 V. **range** values are coerced up to the closest input
        **range**. Refer to the `Devices
        Overview <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/devices/>`__
        for a list of valid ranges. The driver sets :py:data:`nidmm.range` to this
        value. The default is 0.02 V.

        +-------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_AUTO\_RANGE\_ON   | -1.0 | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                                            |
        +-------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_AUTO\_RANGE\_OFF  | -2.0 | NI-DMM sets the Range to the current :py:data:`nidmm.AUTO\_RANGE\_VALUE` and uses this range for all subsequent measurements until the measurement configuration is changed.                               |
        +-------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_AUTO\_RANGE\_ONCE | -3.0 | NI-DMM performs an Auto Range before acquiring the measurement. The :py:data:`nidmm.AUTO\_RANGE\_VALUE` is stored and used for all subsequent measurements until the measurement configuration is changed. |
        +-------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
            trigger and sample trigger are set to IMMEDIATE.

    :type range: float
    :param resolution_absolute:


        Specifies the absolute resolution for the measurement. NI-DMM sets
        :py:data:`nidmm.RESOLUTION\_ABSOLUTE` to this value. This parameter is
        ignored when the **Range** parameter is set to
        NIDMM\_VAL\_AUTO\_RANGE\_ON (-1.0) or NIDMM\_VAL\_AUTO\_RANGE\_ONCE
        (-3.0). The default is 0.001 V.

        

        .. note:: NI-DMM ignores this parameter for capacitance and inductance
            measurements on the NI 4072. To achieve better resolution for such
            measurements, use the :py:data:`nidmm.LC\_NUMBER\_MEAS\_TO\_AVERAGE`
            attribute.

    :type resolution_absolute: float

.. function:: configure_measurement_digits(measurement_function, range, resolution_digits)

    Configures the common attributes of the measurement. These attributes
    include :py:data:`nidmm.function`, :py:data:`nidmm.range`, and
    :py:data:`nidmm.RESOLUTION\_DIGITS`.

    


    :param measurement_function:


        Specifies the **measurement\_function** used to acquire the measurement.
        The driver sets :py:data:`nidmm.function` to this value.

        

    :type measurement_function: :py:data:`nidmm.Function`
    :param range:


        Specifies the range for the function specified in the
        **Measurement\_Function** parameter. When frequency is specified in the
        **Measurement\_Function** parameter, you must supply the minimum
        frequency expected in the **range** parameter. For example, you must
        type in 100 Hz if you are measuring 101 Hz or higher.
        For all other functions, you must supply a range that exceeds the value
        that you are measuring. For example, you must type in 10 V if you are
        measuring 9 V. range values are coerced up to the closest input range.
        Refer to the `Devices
        Overview <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/devices/>`__
        for a list of valid ranges. The driver sets :py:data:`nidmm.range` to this
        value. The default is 0.02 V.

        +-------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_AUTO\_RANGE\_ON   | -1.0 | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                                            |
        +-------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_AUTO\_RANGE\_OFF  | -2.0 | NI-DMM sets the Range to the current :py:data:`nidmm.AUTO\_RANGE\_VALUE` and uses this range for all subsequent measurements until the measurement configuration is changed.                               |
        +-------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_AUTO\_RANGE\_ONCE | -3.0 | NI-DMM performs an Auto Range before acquiring the measurement. The :py:data:`nidmm.AUTO\_RANGE\_VALUE` is stored and used for all subsequent measurements until the measurement configuration is changed. |
        +-------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
            trigger and sample trigger are set to IMMEDIATE.

    :type range: float
    :param resolution_digits:


        Specifies the resolution of the measurement in digits. The driver sets
        the `Devices
        Overview <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/devices/>`__
        for a list of valid ranges. The driver sets
        :py:data:`nidmm.RESOLUTION\_DIGITS` attribute to this value. This parameter
        is ignored when the **Range** parameter is set to
        NIDMM\_VAL\_AUTO\_RANGE\_ON (-1.0) or NIDMM\_VAL\_AUTO\_RANGE\_ONCE
        (-3.0). The default is 5½.

        

        .. note:: NI-DMM ignores this parameter for capacitance and inductance
            measurements on the NI 4072. To achieve better resolution for such
            measurements, use the :py:data:`nidmm.LC\_NUMBER\_MEAS\_TO\_AVERAGE`
            attribute.

    :type resolution_digits: float

.. function:: configure_multi_point(trigger_count, sample_count, sample_trigger=nidmm.SampleTrigger.IMMEDIATE, sample_interval=-1)

    Configures the attributes for multipoint measurements. These attributes
    include :py:data:`nidmm.TRIGGER\_COUNT`, :py:data:`nidmm.SAMPLE\_COUNT`,
    :py:data:`nidmm.SAMPLE\_TRIGGER`, and :py:data:`nidmm.SAMPLE\_INTERVAL`.

    For continuous acquisitions, set :py:data:`nidmm.TRIGGER\_COUNT` or
    :py:data:`nidmm.SAMPLE\_COUNT` to zero. For more information, refer to
    `Multiple Point
    Acquisitions <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/multi_point/>`__,
    `Triggering <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/trigger/>`__,
    and `Using
    Switches <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/switch_selection/>`__.

    


    :param trigger_count:


        Sets the number of triggers you want the DMM to receive before returning
        to the Idle state. The driver sets :py:data:`nidmm.TRIGGER\_COUNT` to this
        value. The default value is 1.

        

    :type trigger_count: int
    :param sample_count:


        Sets the number of measurements the DMM makes in each measurement
        sequence initiated by a trigger. The driver sets
        :py:data:`nidmm.SAMPLE\_COUNT` to this value. The default value is 1.

        

    :type sample_count: int
    :param sample_trigger:


        Specifies the **sample\_trigger** source you want to use. The driver
        sets :py:data:`nidmm.SAMPLE\_TRIGGER` to this value. The default is
        Immediate.

        

        .. note:: To determine which values are supported by each device, refer to the
            `LabWindows/CVI Trigger
            Routing <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/cvitrigger_routing/>`__
            section.

    :type sample_trigger: :py:data:`nidmm.SampleTrigger`
    :param sample_interval:


        Sets the amount of time in seconds the DMM waits between measurement
        cycles. The driver sets :py:data:`nidmm.SAMPLE\_INTERVAL` to this value.
        Specify a sample interval to add settling time between measurement
        cycles or to decrease the measurement rate. **sample\_interval** only
        applies when the **Sample\_Trigger** is set to INTERVAL.

        On the NI 4060, the **sample\_interval** value is used as the settling
        time. When sample interval is set to 0, the DMM does not settle between
        measurement cycles. The NI 4065 and NI 4070/4071/4072 use the value
        specified in **sample\_interval** as additional delay. The default value
        (-1) ensures that the DMM settles for a recommended time. This is the
        same as using an Immediate trigger.

        

        .. note:: This attribute is not used on the NI 4080/4081/4082 and the NI 4050.

    :type sample_interval: float

.. function:: configure_open_cable_comp_values(conductance, susceptance)

    For the NI 4082 and NI 4072 only, configures the
    :py:data:`nidmm.OPEN\_CABLE\_COMP\_CONDUCTANCE` and
    :py:data:`nidmm.OPEN\_CABLE\_COMP\_SUSCEPTANCE` attributes.

    


    :param conductance:


        Specifies the open cable compensation **conductance**.

        

    :type conductance: float
    :param susceptance:


        Specifies the open cable compensation **susceptance**.

        

    :type susceptance: float

.. function:: configure_power_line_frequency(power_line_frequency_hz)

    Specifies the powerline frequency.

    


    :param power_line_frequency_hz:


        **Powerline Frequency** specifies the powerline frequency in hertz.
        NI-DMM sets the Powerline Frequency property to this value.

        

    :type power_line_frequency_hz: float

.. function:: configure_rtd_custom(rtd_a, rtd_b, rtd_c)

    Configures the A, B, and C parameters for a custom RTD.

    


    :param rtd_a:


        Specifies the Callendar-Van Dusen A coefficient for RTD scaling when RTD
        Type parameter is set to Custom in the :py:func:`nidmm.configure_rtd_type` function.
        The default is 3.9083e-3 (Pt3851)

        

    :type rtd_a: float
    :param rtd_b:


        Specifies the Callendar-Van Dusen B coefficient for RTD scaling when RTD
        Type parameter is set to Custom in the :py:func:`nidmm.configure_rtd_type` function.
        The default is -5.775e-7 (Pt3851).

        

    :type rtd_b: float
    :param rtd_c:


        Specifies the Callendar-Van Dusen C coefficient for RTD scaling when RTD
        Type parameter is set to Custom in the :py:func:`nidmm.configure_rtd_type` function.
        The default is -4.183e-12 (Pt3851).

        

    :type rtd_c: float

.. function:: configure_rtd_type(rtd_type, rtd_resistance)

    Configures the RTD Type and RTD Resistance parameters for an RTD.

    


    :param rtd_type:


        Specifies the type of RTD used to measure the temperature resistance.
        NI-DMM uses this value to set the RTD Type property. The default is
        NIDMM\_VAL\_TEMP\_RTD\_PT3851.

        +---------------------------------+
        | Enum                            |
        +=================================+
        | Callendar-Van Dusen Coefficient |
        +---------------------------------+
        | NIDMM\_VAL\_TEMP\_RTD\_PT3851   |
        +---------------------------------+
        | NIDMM\_VAL\_TEMP\_RTD\_PT3750   |
        +---------------------------------+
        | NIDMM\_VAL\_TEMP\_RTD\_PT3916   |
        +---------------------------------+
        | NIDMM\_VAL\_TEMP\_RTD\_PT3920   |
        +---------------------------------+
        | NIDMM\_VAL\_TEMP\_RTD\_PT3911   |
        +---------------------------------+
        | NIDMM\_VAL\_TEMP\_RTD\_PT3928   |
        +---------------------------------+
        | \*No standard. Check the TCR.   |
        +---------------------------------+

    :type rtd_type: :py:data:`nidmm.RTDType`
    :param rtd_resistance:


        Specifies the RTD resistance in ohms at 0 °C. NI-DMM uses this value to
        set the RTD Resistance property. The default is 100 (Ω).

        

    :type rtd_resistance: float

.. function:: configure_short_cable_comp_values(resistance, reactance)

    For the NI 4082 and NI 4072 only, configures the
    :py:data:`nidmm.SHORT\_CABLE\_COMP\_RESISTANCE` and
    :py:data:`nidmm.SHORT\_CABLE\_COMP\_REACTANCE` attributes.

    


    :param resistance:


        Specifies the short cable compensation **resistance**.

        

    :type resistance: float
    :param reactance:


        Specifies the short cable compensation **reactance**.

        

    :type reactance: float

.. function:: configure_thermistor_custom(thermistor_a, thermistor_b, thermistor_c)

    Configures the A, B, and C parameters for a custom thermistor.

    


    :param thermistor_a:


        Specifies the Steinhart-Hart A coefficient for thermistor scaling when
        Thermistor Type is set to Custom in the :py:func:`nidmm.configure_thermistor_type`
        function. The default is 1.0295e-3 (44006).

        

    :type thermistor_a: float
    :param thermistor_b:


        Specifies the Steinhart-Hart B coefficient for thermistor scaling when
        Thermistor Type is set to Custom in the :py:func:`nidmm.configure_thermistor_type`
        function. The default is 2.391e-4 (44006).

        

    :type thermistor_b: float
    :param thermistor_c:


        Specifies the Steinhart-Hart C coefficient for thermistor scaling when
        Thermistor Type is set to Custom in the :py:func:`nidmm.configure_thermistor_type`
        function. The default is 1.568e-7 (44006).

        

    :type thermistor_c: float

.. function:: configure_thermocouple(thermocouple_type, reference_junction_type=nidmm.ThermocoupleReferenceJunctionType.FIXED)

    Configures the thermocouple type and reference junction type for a
    chosen thermocouple.

    


    :param thermocouple_type:


        Specifies the type of thermocouple used to measure the temperature.
        NI-DMM uses this value to set the Thermocouple Type property. The
        default is NIDMM\_VAL\_TEMP\_TC\_J.

        +-------------------------+---------------------+
        | NIDMM\_VAL\_TEMP\_TC\_B | Thermocouple type B |
        +-------------------------+---------------------+
        | NIDMM\_VAL\_TEMP\_TC\_E | Thermocouple type E |
        +-------------------------+---------------------+
        | NIDMM\_VAL\_TEMP\_TC\_J | Thermocouple type J |
        +-------------------------+---------------------+
        | NIDMM\_VAL\_TEMP\_TC\_K | Thermocouple type K |
        +-------------------------+---------------------+
        | NIDMM\_VAL\_TEMP\_TC\_N | Thermocouple type N |
        +-------------------------+---------------------+
        | NIDMM\_VAL\_TEMP\_TC\_R | Thermocouple type R |
        +-------------------------+---------------------+
        | NIDMM\_VAL\_TEMP\_TC\_S | Thermocouple type S |
        +-------------------------+---------------------+
        | NIDMM\_VAL\_TEMP\_TC\_T | Thermocouple type T |
        +-------------------------+---------------------+

    :type thermocouple_type: :py:data:`nidmm.ThermocoupleType`
    :param reference_junction_type:


        Specifies the type of reference junction to be used in the reference
        junction compensation of a thermocouple measurement. NI-DMM uses this
        value to set the Reference Junction Type property. The only supported
        value is NIDMM\_VAL\_TEMP\_REF\_JUNC\_FIXED.

        

    :type reference_junction_type: :py:data:`nidmm.ThermocoupleReferenceJunctionType`

.. function:: configure_trigger(trigger_source, trigger_delay=-1)

    Configures the DMM **Trigger\_Source** and **Trigger\_Delay**. Refer to
    `Triggering <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/trigger/>`__
    and `Using
    Switches <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/switch_selection/>`__
    for more information.

    


    :param trigger_source:


        Specifies the **trigger\_source** that initiates the acquisition. The
        driver sets :py:data:`nidmm.TRIGGER\_SOURCE` to this value. Software
        configures the DMM to wait until :py:func:`nidmm.send_software_trigger` is called
        before triggering the DMM.

        

        .. note:: To determine which values are supported by each device, refer to the
            `LabWindows/CVI Trigger
            Routing <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/cvitrigger_routing/>`__
            section.

    :type trigger_source: :py:data:`nidmm.TriggerSource`
    :param trigger_delay:


        Specifies the time that the DMM waits after it has received a trigger
        before taking a measurement. The driver sets the
        :py:data:`nidmm.TRIGGER\_DELAY` attribute to this value. By default,
        **trigger\_delay** is NIDMM\_VAL\_AUTO\_DELAY (-1), which means the DMM
        waits an appropriate settling time before taking the measurement. On the
        NI 4060, if you set **trigger\_delay** to 0, the DMM does not settle
        before taking the measurement. The NI 4065 and NI 4070/4071/4072 use the
        value specified in **trigger\_delay** as additional settling time.

        

        .. note:: When using the NI 4050, **Trigger\_Delay** must be set to
            NIDMM\_VAL\_AUTO\_DELAY (-1).

    :type trigger_delay: float

.. function:: configure_waveform_acquisition(measurement_function, range, rate, waveform_points)

    Configures the DMM for waveform acquisitions. This feature is supported
    on the NI 4080/4081/4082 and the NI 4070/4071/4072.

    


    :param measurement_function:


        Specifies the **measurement\_function** used in a waveform acquisition.
        The driver sets :py:data:`nidmm.function` to this value.

        +-----------------------------------------+------+------------------+
        | NIDMM\_VAL\_WAVEFORM\_VOLTAGE (default) | 1003 | Voltage Waveform |
        +-----------------------------------------+------+------------------+
        | NIDMM\_VAL\_WAVEFORM\_CURRENT           | 1004 | Current Waveform |
        +-----------------------------------------+------+------------------+

    :type measurement_function: :py:data:`nidmm.Function`
    :param range:


        Specifies the expected maximum amplitude of the input signal and sets
        the **range** for the **Measurement\_Function**. NI-DMM sets
        :py:data:`nidmm.range` to this value. **range** values are coerced up to the
        closest input **range**. The default is 10.0.

        For valid ranges refer to the topics in
        `Devices <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/devices/>`__.

        Auto-ranging is not supported during waveform acquisitions.

        

    :type range: float
    :param rate:


        Specifies the **rate** of the acquisition in samples per second. NI-DMM
        sets :py:data:`nidmm.WAVEFORM\_RATE` to this value.

        The valid **Range** is 10.0–1,800,000 S/s. **rate** values are coerced
        to the closest integer divisor of 1,800,000. The default value is
        1,800,000.

        

    :type rate: float
    :param waveform_points:


        Specifies the number of points to acquire before the waveform
        acquisition completes. NI-DMM sets :py:data:`nidmm.WAVEFORM\_POINTS` to this
        value.

        To calculate the maximum and minimum number of waveform points that you
        can acquire in one acquisition, refer to the `Waveform Acquisition
        Measurement
        Cycle <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/waveform_cycle/>`__.

        The default value is 500.

        

    :type waveform_points: int

.. function:: disable()

    Places the instrument in a quiescent state where it has minimal or no
    impact on the system to which it is connected. If a measurement is in
    progress when this function is called, the measurement is aborted.

    


.. function:: fetch(maximum_time=-1)

    Returns the value from a previously initiated measurement. You must call
    :py:func:`nidmm._initiate` before calling this function.

    


    :param maximum_time:


        Specifies the **maximum\_time** allowed for this function to complete in
        milliseconds. If the function does not complete within this time
        interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
        error code. This may happen if an external trigger has not been
        received, or if the specified timeout is not long enough for the
        acquisition to complete.

        The valid range is 0–86400000. The default value is
        NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
        automatically.

        

    :type maximum_time: int

    :rtype: float
    :return:


            The measured value returned from the DMM.

            


.. function:: fetch_multi_point(array_size, maximum_time=-1)

    Returns an array of values from a previously initiated multipoint
    measurement. The number of measurements the DMM makes is determined by
    the values you specify for the **Trigger\_Count** and **Sample\_Count**
    parameters of :py:func:`nidmm.configure_multi_point`. You must first call
    :py:func:`nidmm._initiate` to initiate a measurement before calling this function.

    


    :param maximum_time:


        Specifies the **maximum\_time** allowed for this function to complete in
        milliseconds. If the function does not complete within this time
        interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
        error code. This may happen if an external trigger has not been
        received, or if the specified timeout is not long enough for the
        acquisition to complete.

        The valid range is 0–86400000. The default value is
        NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
        automatically.

        

    :type maximum_time: int
    :param array_size:


        Specifies the number of measurements to acquire. The maximum number of
        measurements for a finite acquisition is the (**Trigger Count** x
        **Sample Count**) parameters in :py:func:`nidmm.configure_multi_point`.

        For continuous acquisitions, up to 100,000 points can be returned at
        once. The number of measurements can be a subset. The valid range is any
        positive ViInt32. The default value is 1.

        

    :type array_size: int

    :rtype: tuple (reading_array, actual_number_of_points)

        WHERE

        reading_array (list of float): 


            An array of measurement values.

            

            .. note:: The size of the **Reading\_Array** must be at least the size that you
                specify for the **Array\_Size** parameter.

        actual_number_of_points (int): 


            Indicates the number of measured values actually retrieved from the DMM.

            


.. function:: fetch_waveform(array_size, maximum_time=-1)

    For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of
    values from a previously initiated waveform acquisition. You must call
    :py:func:`nidmm._initiate` before calling this function.

    


    :param maximum_time:


        Specifies the **maximum\_time** allowed for this function to complete in
        milliseconds. If the function does not complete within this time
        interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
        error code. This may happen if an external trigger has not been
        received, or if the specified timeout is not long enough for the
        acquisition to complete.

        The valid range is 0–86400000. The default value is
        NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
        automatically.

        

    :type maximum_time: int
    :param array_size:


        Specifies the number of waveform points to return. You specify the total
        number of points that the DMM acquires in the **Waveform Points**
        parameter of :py:func:`nidmm.configure_waveform_acquisition`. The default value is
        1.

        

    :type array_size: int

    :rtype: tuple (waveform_array, actual_number_of_points)

        WHERE

        waveform_array (list of float): 


            **Waveform Array** is an array of measurement values stored in waveform
            data type.

            

        actual_number_of_points (int): 


            Indicates the number of measured values actually retrieved from the DMM.

            


.. function:: get_aperture_time_info()

    Returns the DMM **Aperture\_Time** and **Aperture\_Time\_Units**.

    


    :rtype: tuple (aperture_time, aperture_time_units)

        WHERE

        aperture_time (float): 


            Specifies the amount of time the DMM digitizes the input signal for a
            single measurement. This parameter does not include settling time.
            Returns the value of the :py:data:`nidmm.APERTURE\_TIME` attribute. The
            units of this attribute depend on the value of the
            :py:data:`nidmm.APERTURE\_TIME\_UNITS` attribute.
            On the NI 4070/4071/4072, the minimum aperture time is 8.89 µs, and the
            maximum aperture time is 149 s. Any number of powerline cycles (PLCs)
            within the minimum and maximum ranges is allowed on the
            NI 4070/4071/4072.
            On the NI 4065 the minimum aperture time is 333 µs, and the maximum
            aperture time is 78.2 s. If setting the number of averages directly, the
            total measurement time is aperture time X the number of averages, which
            must be less than 72.8 s. The aperture times allowed are 333 µs, 667 µs,
            or multiples of 1.11 ms—for example 1.11 ms, 2.22 ms, 3.33 ms, and so
            on. If you set an aperture time other than 333 µs, 667 µs, or multiples
            of 1.11 ms, the value will be coerced up to the next supported aperture
            time.
            On the NI 4060, when the powerline frequency is 60, the PLCs allowed are
            1 PLC, 6 PLC, 12 PLC, and 120 PLC. When the powerline frequency is 50,
            the PLCs allowed are 1 PLC, 5 PLC, 10 PLC, and 100 PLC.

            

        aperture_time_units (:py:data:`nidmm.ApertureTimeUnits`): 


            Indicates the units of aperture time as powerline cycles (PLCs) or
            seconds. Returns the value of the :py:data:`nidmm.APERTURE\_TIME\_UNITS`
            attribute.

            +---------------------------------+---+------------------+
            | NIDMM\_VAL\_SECONDS             | 0 | Seconds          |
            +---------------------------------+---+------------------+
            | NIDMM\_VAL\_POWER\_LINE\_CYCLES | 1 | Powerline Cycles |
            +---------------------------------+---+------------------+


.. function:: get_auto_range_value()

    Returns the **Actual\_Range** that the DMM is using, even when Auto
    Range is off.

    


    :rtype: float
    :return:


            Indicates the **actual\_range** the DMM is using. Returns the value of
            the :py:data:`nidmm.AUTO\_RANGE\_VALUE` attribute. The units of the returned
            value depend on the function.

            


.. function:: get_cal_date_and_time(cal_type)

    Returns the date and time of the last calibration performed.

    

    .. note:: The NI 4050 and NI 4060 are not supported.


    :param cal_type:


        Specifies the type of calibration performed (external or
        self-calibration).

        +--------------------------------------+---+----------------------+
        | NIDMM\_VAL\_INTERNAL\_AREA (default) | 0 | Self-Calibration     |
        +--------------------------------------+---+----------------------+
        | NIDMM\_VAL\_EXTERNAL\_AREA           | 1 | External Calibration |
        +--------------------------------------+---+----------------------+

        .. note:: The NI 4065 does not support self-calibration.

    :type cal_type: int

    :rtype: tuple (month, day, year, hour, minute)

        WHERE

        month (int): 


            Indicates the **month** of the last calibration.

            

        day (int): 


            Indicates the **day** of the last calibration.

            

        year (int): 


            Indicates the **year** of the last calibration.

            

        hour (int): 


            Indicates the **hour** of the last calibration.

            

        minute (int): 


            Indicates the **minute** of the last calibration.

            


.. function:: get_dev_temp(options='')

    Returns the current **Temperature** of the device.

    

    .. note:: The NI 4050 and NI 4060 are not supported.


    :param options:


        Reserved.

        

    :type options: string

    :rtype: float
    :return:


            Returns the current **temperature** of the device.

            


.. function:: get_last_cal_temp(cal_type)

    Returns the **Temperature** during the last calibration procedure.

    

    .. note:: The NI 4050 and NI 4060 are not supported.


    :param cal_type:


        Specifies the type of calibration performed (external or
        self-calibration).

        +--------------------------------------+---+----------------------+
        | NIDMM\_VAL\_INTERNAL\_AREA (default) | 0 | Self-Calibration     |
        +--------------------------------------+---+----------------------+
        | NIDMM\_VAL\_EXTERNAL\_AREA           | 1 | External Calibration |
        +--------------------------------------+---+----------------------+

        .. note:: The NI 4065 does not support self-calibration.

    :type cal_type: int

    :rtype: float
    :return:


            Returns the **temperature** during the last calibration.

            


.. function:: get_measurement_period()

    Returns the measurement **Period**, which is the amount of time it takes
    to complete one measurement with the current configuration. Use this
    function right before you begin acquiring data—after you have completely
    configured the measurement and after all configuration functions have
    been called.

    


    :rtype: float
    :return:


            Returns the number of seconds it takes to make one measurement.

            The first measurement in a multipoint acquisition requires additional
            settling time. This function does not include this additional time or
            any :py:data:`nidmm.TRIGGER\_DELAY` associated with the first measurement.
            Time required for internal measurements, such as
            :py:data:`nidmm.AUTO\_ZERO`, is included.

            


.. function:: get_self_cal_supported()

    Returns a Boolean value that expresses whether or not the DMM that you
    are using can perform self-calibration.

    


    :rtype: bool
    :return:


            Returns whether Self Cal is supported for the device specified by the
            given session.

            +-----------+---+-------------------------------------------------------------+
            | VI\_TRUE  | 1 | The DMM that you are using can perform self-calibration.    |
            +-----------+---+-------------------------------------------------------------+
            | VI\_FALSE | 0 | The DMM that you are using cannot perform self-calibration. |
            +-----------+---+-------------------------------------------------------------+


.. function:: perform_open_cable_comp()

    For the NI 4082 and NI 4072 only, performs the open cable compensation
    measurements for the current capacitance/inductance range, and returns
    open cable compensation **Conductance** and **Susceptance** values. You
    can use the return values of this function as inputs to
    :py:func:`nidmm.configure_open_cable_comp_values`.

    This function returns an error if the value of the :py:data:`nidmm.function`
    attribute is not set to NIDMM\_VAL\_CAPACITANCE (1005) or
    NIDMM\_VAL\_INDUCTANCE (1006).

    


    :rtype: tuple (conductance, susceptance)

        WHERE

        conductance (float): 


            **conductance** is the measured value of open cable compensation
            **conductance**.

            

        susceptance (float): 


            **susceptance** is the measured value of open cable compensation
            **susceptance**.

            


.. function:: perform_short_cable_comp()

    Performs the short cable compensation measurements for the current
    capacitance/inductance range, and returns short cable compensation
    **Resistance** and **Reactance** values. You can use the return values
    of this function as inputs to :py:func:`nidmm.configure_short_cable_comp_values`.

    This function returns an error if the value of the :py:data:`nidmm.function`
    attribute is not set to NIDMM\_VAL\_CAPACITANCE (1005) or
    NIDMM\_VAL\_INDUCTANCE (1006).

    


    :rtype: tuple (resistance, reactance)

        WHERE

        resistance (float): 


            **resistance** is the measured value of short cable compensation
            **resistance**.

            

        reactance (float): 


            **reactance** is the measured value of short cable compensation
            **reactance**.

            


.. function:: read(maximum_time=-1)

    Acquires a single measurement and returns the measured value.

    


    :param maximum_time:


        Specifies the **maximum\_time** allowed for this function to complete in
        milliseconds. If the function does not complete within this time
        interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
        error code. This may happen if an external trigger has not been
        received, or if the specified timeout is not long enough for the
        acquisition to complete.

        The valid range is 0–86400000. The default value is
        NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
        automatically.

        

    :type maximum_time: int

    :rtype: float
    :return:


            The measured value returned from the DMM.

            


.. function:: read_multi_point(array_size, maximum_time=-1)

    Acquires multiple measurements and returns an array of measured values.
    The number of measurements the DMM makes is determined by the values you
    specify for the **Trigger\_Count** and **Sample\_Count** parameters in
    :py:func:`nidmm.configure_multi_point`.

    


    :param maximum_time:


        Specifies the **maximum\_time** allowed for this function to complete in
        milliseconds. If the function does not complete within this time
        interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
        error code. This may happen if an external trigger has not been
        received, or if the specified timeout is not long enough for the
        acquisition to complete.

        The valid range is 0–86400000. The default value is
        NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
        automatically.

        

    :type maximum_time: int
    :param array_size:


        Specifies the number of measurements to acquire. The maximum number of
        measurements for a finite acquisition is the (**Trigger Count** x
        **Sample Count**) parameters in :py:func:`nidmm.configure_multi_point`.

        For continuous acquisitions, up to 100,000 points can be returned at
        once. The number of measurements can be a subset. The valid range is any
        positive ViInt32. The default value is 1.

        

    :type array_size: int

    :rtype: tuple (reading_array, actual_number_of_points)

        WHERE

        reading_array (list of float): 


            An array of measurement values.

            

            .. note:: The size of the **Reading\_Array** must be at least the size that you
                specify for the **Array\_Size** parameter.

        actual_number_of_points (int): 


            Indicates the number of measured values actually retrieved from the DMM.

            


.. function:: read_status()

    Returns measurement backlog and acquisition status. Use this function to
    determine how many measurements are available before calling
    :py:func:`nidmm.fetch`, :py:func:`nidmm.fetch_multi_point`, or :py:func:`nidmm.fetch_waveform`.

    

    .. note:: The NI 4050 is not supported.


    :rtype: tuple (acquisition_backlog, acquisition_status)

        WHERE

        acquisition_backlog (int): 


            The number of measurements available to be read. If the backlog
            continues to increase, data is eventually overwritten, resulting in an
            error.

            

            .. note:: On the NI 4060, the **Backlog** does not increase when autoranging. On
                the NI 4065, the **Backlog** does not increase when Range is set to AUTO
                RANGE ON (-1), or before the first point is fetched when Range is set to
                AUTO RANGE ONCE (-3). These behaviors are due to the autorange model of
                the devices.

        acquisition_status (:py:data:`nidmm.AcquisitionStatus`): 


            Indicates status of the acquisition. The following table shows the
            acquisition states:

            +---+----------------------------+
            | 0 | Running                    |
            +---+----------------------------+
            | 1 | Finished with backlog      |
            +---+----------------------------+
            | 2 | Finished with no backlog   |
            +---+----------------------------+
            | 3 | Paused                     |
            +---+----------------------------+
            | 4 | No acquisition in progress |
            +---+----------------------------+


.. function:: read_waveform(array_size, maximum_time=-1)

    For the NI 4080/4081/4082 and the NI 4070/4071/4072, acquires a waveform
    and returns data as an array of values or as a waveform data type. The
    number of elements in the **Waveform\_Array** is determined by the
    values you specify for the **Waveform\_Points** parameter in
    :py:func:`nidmm.configure_waveform_acquisition`.

    


    :param maximum_time:


        Specifies the **maximum\_time** allowed for this function to complete in
        milliseconds. If the function does not complete within this time
        interval, the function returns the NIDMM\_ERROR\_MAX\_TIME\_EXCEEDED
        error code. This may happen if an external trigger has not been
        received, or if the specified timeout is not long enough for the
        acquisition to complete.

        The valid range is 0–86400000. The default value is
        NIDMM\_VAL\_TIME\_LIMIT\_AUTO (-1). The DMM calculates the timeout
        automatically.

        

    :type maximum_time: int
    :param array_size:


        Specifies the number of waveform points to return. You specify the total
        number of points that the DMM acquires in the **Waveform Points**
        parameter of :py:func:`nidmm.configure_waveform_acquisition`. The default value is
        1.

        

    :type array_size: int

    :rtype: tuple (waveform_array, actual_number_of_points)

        WHERE

        waveform_array (list of float): 


            An array of measurement values.

            

            .. note:: The size of the **Waveform\_Array** must be at least the size that you
                specify for the **Array\_Size** parameter.

        actual_number_of_points (int): 


            Indicates the number of measured values actually retrieved from the DMM.

            


.. function:: reset_with_defaults()

    Resets the instrument to a known state and sends initialization commands
    to the DMM. The initialization commands set the DMM settings to the
    state necessary for the operation of NI-DMM. All user-defined default
    values associated with a logical name are applied after setting the DMM.

    


.. function:: self_cal()

    For the NI 4080/4081/4082 and the NI 4070/4071/4072, executes the
    self-calibration routine to maintain measurement accuracy.

    

    .. note:: This function calls :py:func:`nidmm.reset`, and any configurations previous to
        the call will be lost. All attributes will be set to their default
        values after the call returns.


.. function:: send_software_trigger()

    Sends a command to trigger the DMM. Call this function if you have
    configured either the :py:data:`nidmm.TRIGGER\_SOURCE` or
    :py:data:`nidmm.SAMPLE\_TRIGGER` attributes. If the
    :py:data:`nidmm.TRIGGER\_SOURCE` and/or :py:data:`nidmm.SAMPLE\_TRIGGER`
    attributes are set to NIDMM\_VAL\_EXTERNAL or NIDMM\_VAL\_TTL\ *n*, you
    can use this function to override the trigger source that you configured
    and trigger the device. The NI 4050 and NI 4060 are not supported.

    


.. function:: reset()

    Resets the instrument to a known state and sends initialization commands
    to the instrument. The initialization commands set instrument settings
    to the state necessary for the operation of the instrument driver.

    


.. function:: revision_query()

    Returns the revision numbers of the instrument driver and instrument
    firmware.

    


    :rtype: tuple (instrument_driver_revision, firmware_revision)

        WHERE

        instrument_driver_revision (string): 


            Returns a string containing the instrument driver software revision
            numbers.

            

            .. note:: The array must contain at least 256 elements ViChar[256].

        firmware_revision (string): 


            Returns a string containing the instrument **firmware\_revision**
            numbers.

            

            .. note:: The array must contain at least 256 elements ViChar[256].


.. function:: self_test()

    Performs a self-test on the DMM to ensure that the DMM is functioning
    properly. Self-test does not calibrate the DMM.

    

    .. note:: This function calls :py:func:`nidmm.reset`, and any configurations previous to
        the call will be lost. All attributes will be set to their default
        values after the call returns.


    :rtype: tuple (self_test_result, self_test_message)

        WHERE

        self_test_result (int): 


            Contains the value returned from the instrument self-test. Zero
            indicates success.

            On the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that
            you should check the fuse and replace it, if necessary.

            

            .. note:: Self-test does not check the fuse on the NI 4065, NI 4071, and
                NI 4081. Hence, even if the fuse is blown on the device, self-test does
                not return error code 1013.

        self_test_message (string): 


            This parameter contains the string returned from the instrument
            self-test. The array must contain at least 256 elements.

            For the NI 4050 and NI 4060, the error codes returned for self-test
            failures include the following:

            -  NIDMM\_ERROR\_AC\_TEST\_FAILURE
            -  NIDMM\_ERROR\_DC\_TEST\_FAILURE
            -  NIDMM\_ERROR\_RESISTANCE\_TEST\_FAILURE

            These error codes indicate that the DMM should be repaired.

            For the NI 4080/4081/4082 and the NI 4070/4071/4072, the error code
            returned for a self-test failure is NIDMM\_ERROR\_SELF\_TEST\_FAILURE.
            This error code indicates that the DMM should be repaired.

            



