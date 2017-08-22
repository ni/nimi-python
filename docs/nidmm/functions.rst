NI-DMM Functions
================

.. py:currentmodule:: nidmm

.. function:: _abort()

    Aborts a previously initiated measurement and returns the DMM to the
    Idle state.

    


.. function:: _clear_error()

    Clears the error information for the current execution thread and the
    IVI session you specify. If you pass VI\_NULL for the
    **Instrument\_Handle** parameter, this function clears the error
    information only for the current execution thread.

    


.. function:: clear_interchange_warnings()

    Clears the list of current interchange warnings.

    


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

.. function:: configure_adc_calibration(adc_calibration)

    For the NI 4080/4081/4082 and NI 4070/4071/4072, allows the DMM to
    compensate for gain drift since the last external calibration or
    self-calibration. When **ADC\_Calibration** is ON, the DMM measures an
    internal reference to calculate the correct gain for the measurement.
    When **ADC\_Calibration** is OFF, the DMM does not compensate for
    changes to the gain.

    


    :param adc_calibration:


        Specifies the **ADC\_Calibration** setting. The driver sets
        :py:data:`nidmm.ADC\_CALIBRATION` to this value.
        NIDMM\_VAL\_ADC\_CALIBRATION\_ON enables **ADC\_Calibration**.
        NIDMM\_VAL\_ADC\_CALIBRATION\_OFF disables **ADC\_Calibration**. If you
        set the value to NIDMM\_VAL\_ADC\_CALIBRATION\_AUTO, the driver
        determines whether to enable **ADC\_Calibration** based on the
        measurement function and resolution that you configure. If you configure
        the NI 4080/4081/4082 or NI 4070/4071/4072 for a 6½–digit and greater
        resolution DC measurement, the driver enables ADC Calibration. For all
        other measurement configurations, the driver disables
        **ADC\_Calibration**.

        +----------------------------------------------+-------+---------------------------------------------------------------------------------------------------+
        | Name                                         | Value | Description                                                                                       |
        +==============================================+=======+===================================================================================================+
        | NIDMM\_VAL\_ADC\_CALIBRATION\_AUTO (default) | -1.0  | The DMM enables or disables **ADC\_Calibration** based on the configured function and resolution. |
        +----------------------------------------------+-------+---------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_ADC\_CALIBRATION\_OFF            | 0     | The DMM does not compensate for changes to the gain.                                              |
        +----------------------------------------------+-------+---------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_ADC\_CALIBRATION\_ON             | 1     | The DMM measures an internal reference to calculate the correct gain for the measurement.         |
        +----------------------------------------------+-------+---------------------------------------------------------------------------------------------------+

    :type adc_calibration: :py:data:`nidmm.ADCCalibration`

.. function:: configure_auto_zero_mode(auto_zero_mode)

    Configures the DMM for **Auto\_Zero\_Mode**. When **Auto\_Zero\_Mode**
    is ON, the DMM internally disconnects the input signal and takes a zero
    reading. It then subtracts the zero reading from the measurement. This
    prevents offset voltages present on the input circuitry of the DMM from
    affecting measurement accuracy. When **Auto\_Zero\_Mode** is OFF, the
    DMM does not compensate for zero reading offset.

    


    :param auto_zero_mode:


        Specifies the **auto\_zero\_mode**. NI-DMM sets the
        :py:data:`nidmm.AUTO\_ZERO` attribute to this value.

        ON enables **auto\_zero\_mode** for each measurement. ONCE enables
        **auto\_zero\_mode** before the next measurement. The
        **auto\_zero\_mode** value is stored and used in subsequent measurements
        until the device is reconfigured.

        OFF disables **auto\_zero\_mode**. If you set this parameter to AUTO,
        NI-DMM determines whether to enable Auto Zero based on the measurement
        function that you configure. If you configure the NI 4080/4081/4082 or
        the NI 4070/4071/4072 for a 6½–digit and greater resolution DC
        measurement, NI-DMM sets **auto\_zero\_mode** to ON.

        For all other DC measurement configurations on the NI 4080/4081/4082 or
        the NI 4070/4071/4072, NI-DMM sets **auto\_zero\_mode** to ONCE. For all
        AC measurements or waveform acquisitions on the NI 4080/4081/4082 or the
        NI 4070/4071/4072, NI-DMM sets **auto\_zero\_mode** to OFF. For NI 4060,
        **auto\_zero\_mode** is set to OFF when AUTO is selected.

        For NI 4065 devices, **auto\_zero\_mode** is always ON.
        **auto\_zero\_mode** is an integral part of the signal measurement phase
        and adds no extra time to the overall measurement.

        +----------------------------------------+----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_AUTO\_ZERO\_AUTO (default) | -1 | NI-DMM chooses the Auto Zero setting based on the configured function and resolution.                                                                                                                      |
        +----------------------------------------+----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_AUTO\_ZERO\_OFF            | 0  | Disables Auto Zero.                                                                                                                                                                                        |
        +----------------------------------------+----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_AUTO\_ZERO\_ON             | 1  | The DMM internally disconnects the input signal following each measurement and takes a zero reading. It then subtracts the zero reading from the preceding reading.                                        |
        +----------------------------------------+----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_AUTO\_ZERO\_ONCE           | 2  | The DMM internally disconnects the input signal following the first measurement and takes a zero reading. It then subtracts the zero reading from the preceding reading and each measurement that follows. |
        +----------------------------------------+----+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: The NI 4060/4065 does *not* support this setting.

    :type auto_zero_mode: :py:data:`nidmm.AutoZero`

.. function:: configure_cable_comp_type(cable_comp_type)

    For the NI 4082 and NI 4072 only, sets the
    :py:data:`nidmm.CABLE\_COMP\_TYPE` attribute for the current
    capacitance/inductance mode range.

    


    :param cable_comp_type:


        Specifies the type of cable compensation that is used for the current
        range.

        

    :type cable_comp_type: :py:data:`nidmm.CableCompensationType`

.. function:: configure_current_source(current_source)

    The NI 4050 and NI 4060 are not supported. Configures the
    **Current\_Source** for diode measurements.

    


    :param current_source:


        Specifies the **current\_source** provided during diode measurements.
        For valid ranges, refer to the device sections for your device. The
        driver sets :py:data:`nidmm.CURRENT\_SOURCE` to this value.

        +-----------------------------------+--------+---------------------------------------------------+
        | NIDMM\_VAL\_1\_MICROAMP           | 1 µA   | NI 4080/4081/4082 and NI 4070/4071/4072           |
        +-----------------------------------+--------+---------------------------------------------------+
        | NIDMM\_VAL\_10\_MICROAMP          | 10 µA  | NI 4080/4081/4082 and NI 4070/4071/4072 only      |
        +-----------------------------------+--------+---------------------------------------------------+
        | NIDMM\_VAL\_100\_MICROAMP         | 100 µA | NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 |
        +-----------------------------------+--------+---------------------------------------------------+
        | NIDMM\_VAL\_1\_MILLIAMP (default) | 1 mA   | NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065 |
        +-----------------------------------+--------+---------------------------------------------------+

    :type current_source: :py:data:`nidmm.CurrentSource`

.. function:: configure_fixed_ref_junction(fixed_reference_junction)

    Configures the fixed reference junction temperature for a thermocouple
    with a fixed reference junction type.

    


    :param fixed_reference_junction:


        Specifies the reference junction temperature when a fixed reference
        junction is used to take a thermocouple measurement. The units are
        degrees Celsius. NI-DMM uses this value to set the Fixed Reference
        Junction property. The default is 25.00 (°C).

        

    :type fixed_reference_junction: float

.. function:: configure_frequency_voltage_range(voltage_range)

    For the NI 4080/4081/4082 and the NI 4070/4071/4072 only, specifies the
    expected maximum amplitude of the input signal for frequency and period
    measurements.

    


    :param voltage_range:


        Sets the expected maximum amplitude of the input signal. Refer to the
        `NI 4080 <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4080_functional_overview/>`__,
        `NI 4081 <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4081_functional_overview/>`__,
        `NI 4072 <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4082/>`__,
        `NI 4070 <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4070_functional_overview/>`__,
        `NI 4071 <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4071_functional_overview/>`__,
        and
        `NI 4072 <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4072/>`__
        sections for a list of valid values. NI-DMM sets
        :py:data:`nidmm.FREQ\_VOLTAGE\_RANGE` to this value. The minimum
        peak-to-peak signal amplitude that can be detected is 10% of the
        specified **voltage\_range**.

        +---------------------------------------+-------+----------------------------------------------------------------------------------------------------------------------------------+
        | Name                                  | Value | Description                                                                                                                      |
        +=======================================+=======+==================================================================================================================================+
        | NIDMM\_VAL\_AUTO\_RANGE\_ON (default) | -1.0  | Configures the DMM to take an Auto Range measurement to calculate the voltage range before each frequency or period measurement. |
        +---------------------------------------+-------+----------------------------------------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_AUTO\_RANGE\_OFF          | -2.0  | Disables Auto Ranging. The driver sets the voltage range to the last calculated voltage range.                                   |
        +---------------------------------------+-------+----------------------------------------------------------------------------------------------------------------------------------+

    :type voltage_range: float

.. function:: configure_meas_complete_dest(meas_complete_destination)

    Specifies the destination of the DMM Measurement Complete (MC) signal.
    Refer to
    `Triggering <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/trigger/>`__
    for more information.

    


    :param meas_complete_destination:


        Specifies the destination of the Measurement Complete signal. This
        signal is issued when the DMM completes a single measurement. The driver
        sets the :py:data:`nidmm.MEAS\_COMPLETE\_DEST` attribute to this value. This
        signal is commonly referred to as Voltmeter Complete.

        

        .. note:: To determine which values are supported by each device, refer to the
            `LabWindows/CVI Trigger
            Routing <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/cvitrigger_routing/>`__
            section.

    :type meas_complete_destination: :py:data:`nidmm.MeasurementCompleteDest`

.. function:: configure_meas_complete_slope(meas_complete_slope)

    Sets the Measurement Complete signal to either rising edge (positive) or
    falling edge (negative) polarity.

    


    :param meas_complete_slope:


        Specifies the polarity of the signal that is generated. The driver sets
        :py:data:`nidmm.MEAS\_DEST\_SLOPE` to this value.

        +------------------------+---+----------------------+----------------------------------------------------------------+
        | Rising Edge            | 0 | NIDMM\_VAL\_POSITIVE | The driver triggers on the rising edge of the trigger signal.  |
        +------------------------+---+----------------------+----------------------------------------------------------------+
        | Falling Edge (default) | 1 | NIDMM\_VAL\_NEGATIVE | The driver triggers on the falling edge of the trigger signal. |
        +------------------------+---+----------------------+----------------------------------------------------------------+

    :type meas_complete_slope: :py:data:`nidmm.Slope`

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

.. function:: configure_multi_point(trigger_count, sample_count, sample_trigger, sample_interval)

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

.. function:: configure_offset_comp_ohms(offset_comp_ohms)

    For NI 4080/4081/4082 and NI 4070/4071/4072, allows the DMM to
    compensate for voltage offsets in resistance measurements. When
    **Offset\_Comp\_Ohms** is enabled, the DMM measures the resistance twice
    (once with the current source on and again with it turned off). Any
    voltage offset present in both measurements is cancelled out.
    **Offset\_Comp\_Ohms** is useful when measuring resistance values less
    than 10 KΩ.

    


    :param offset_comp_ohms:


        Enables or disables **offset\_comp\_ohms**. The driver sets
        :py:data:`nidmm.OFFSET\_COMP\_OHMS` to this value.

        +-----------------------------------------------+-------+--------------------------------------+
        | Name                                          | Value | Description                          |
        +===============================================+=======+======================================+
        | NIDMM\_VAL\_OFFSET\_COMP\_OHMS\_OFF (default) | 0     | Off disables **Offset\_Comp\_Ohms**. |
        +-----------------------------------------------+-------+--------------------------------------+
        | NIDMM\_VAL\_OFFSET\_COMP\_OHMS\_ON            | 1     | On enables **Offset\_Comp\_Ohms**.   |
        +-----------------------------------------------+-------+--------------------------------------+

    :type offset_comp_ohms: :py:data:`nidmm.OffsetCompensatedOhms`

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

    :type rtd_type: int
    :param rtd_resistance:


        Specifies the RTD resistance in ohms at 0 °C. NI-DMM uses this value to
        set the RTD Resistance property. The default is 100 (Ω).

        

    :type rtd_resistance: float

.. function:: configure_sample_trigger_slope(sample_trigger_slope)

    Sets the :py:data:`nidmm.SAMPLE\_TRIGGER\_SLOPE` to either rising edge
    (positive) or falling edge (negative) polarity.

    


    :param sample_trigger_slope:


        Specifies the polarity of the Trigger signal on which the measurement is
        triggered for values of either NIDMM\_VAL\_POSITIVE or
        NIDMM\_VAL\_NEGATIVE. The driver sets
        :py:data:`nidmm.SAMPLE\_TRIGGER\_SLOPE` to this value.

        +------------------------+---+----------------------+----------------------------------------------------------------+
        | Rising Edge            | 0 | NIDMM\_VAL\_POSITIVE | The driver triggers on the rising edge of the trigger signal.  |
        +------------------------+---+----------------------+----------------------------------------------------------------+
        | Falling Edge (default) | 1 | NIDMM\_VAL\_NEGATIVE | The driver triggers on the falling edge of the trigger signal. |
        +------------------------+---+----------------------+----------------------------------------------------------------+

    :type sample_trigger_slope: :py:data:`nidmm.Slope`

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

.. function:: configure_thermistor_type(thermistor_type)

    Configures the thermistor type.

    


    :param thermistor_type:


        Specifies the type of thermistor used to measure the temperature. NI-DMM
        uses this value to set the Thermistor Type property. The default is
        NIDMM\_VAL\_TEMP\_THERMISTOR\_44006.

        +--------------------+--------------------+--------------------+--------------------+
        | **Defined Values** | **Thermistor       | **Value**          | **25 °C            |
        |                    | Type**             |                    | Resistance**       |
        +--------------------+--------------------+--------------------+--------------------+
        | NIDMM\_VAL\_TEMP\_ | Custom             | 0                  | —                  |
        | THERMISTOR\_CUSTOM |                    |                    |                    |
        +--------------------+--------------------+--------------------+--------------------+
        | NIDMM\_VAL\_TEMP\_ | 44004              | 1                  | 2.25 kΩ            |
        | THERMISTOR\_44004  |                    |                    |                    |
        +--------------------+--------------------+--------------------+--------------------+
        | NIDMM\_VAL\_TEMP\_ | 44006              | 2                  | 10 kΩ              |
        | THERMISTOR\_44006  |                    |                    |                    |
        +--------------------+--------------------+--------------------+--------------------+
        | NIDMM\_VAL\_TEMP\_ | 44007              | 3                  | 5 kΩ               |
        | THERMISTOR\_44007  |                    |                    |                    |
        +--------------------+--------------------+--------------------+--------------------+

        

    :type thermistor_type: :py:data:`nidmm.TemperatureThermistorType`

.. function:: configure_thermocouple(thermocouple_type, reference_junction_type)

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

        

    :type reference_junction_type: int

.. function:: configure_transducer_type(transducer_type)

    Configures the transducer type.

    


    :param transducer_type:


        Specifies the type of device used to measure the temperature. NI-DMM
        uses this value to set the Transducer Type property. The default is
        NIDMM\_VAL\_THERMOCOUPLE.

        +--------------------------+--------------+
        | NIDMM\_VAL\_2\_WIRE\_RTD | 2-wire RTD   |
        +--------------------------+--------------+
        | NIDMM\_VAL\_4\_WIRE\_RTD | 4-wire RTD   |
        +--------------------------+--------------+
        | NIDMM\_VAL\_THERMISTOR   | Thermistor   |
        +--------------------------+--------------+
        | NIDMM\_VAL\_THERMOCOUPLE | Thermocouple |
        +--------------------------+--------------+

    :type transducer_type: :py:data:`nidmm.TemperatureTransducerType`

.. function:: configure_trigger(trigger_source, trigger_delay)

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

.. function:: configure_trigger_slope(trigger_slope)

    Sets the :py:data:`nidmm.TRIGGER\_SLOPE` attribute to either rising edge
    (positive) or falling edge (negative) polarity.

    


    :param trigger_slope:


        Specifies the polarity of the trigger signal on which the measurement is
        triggered for values of either NIDMM\_VAL\_POSITIVE or
        NIDMM\_VAL\_NEGATIVE. The driver sets the :py:data:`nidmm.TRIGGER\_SLOPE`
        attribute to this value.

        +--------------------------------+---+----------------------------------------------------------------+
        | NIDMM\_VAL\_POSITIVE           | 0 | The driver triggers on the rising edge of the trigger signal.  |
        +--------------------------------+---+----------------------------------------------------------------+
        | NIDMM\_VAL\_NEGATIVE (default) | 1 | The driver triggers on the falling edge of the trigger signal. |
        +--------------------------------+---+----------------------------------------------------------------+

    :type trigger_slope: :py:data:`nidmm.Slope`

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

.. function:: configure_waveform_coupling(waveform_coupling)

    For the NI 4080/4081/4082 and the NI 4070/4071/4072, configures
    instrument coupling for voltage waveforms.

    


    :param waveform_coupling:


        Selects DC or AC coupling. The driver sets
        :py:data:`nidmm.WAVEFORM\_COUPLING` to this value.

        +----------------------------------------------+-------+-------------+
        | Name                                         | Value | Description |
        +==============================================+=======+=============+
        | NIDMM\_VAL\_WAVEFORM\_COUPLING\_AC           | 0     | AC coupling |
        +----------------------------------------------+-------+-------------+
        | NIDMM\_VAL\_WAVEFORM\_COUPLING\_DC (default) | 1     | DC coupling |
        +----------------------------------------------+-------+-------------+

    :type waveform_coupling: :py:data:`nidmm.WaveformCouplingMode`

.. function:: disable()

    Places the instrument in a quiescent state where it has minimal or no
    impact on the system to which it is connected. If a measurement is in
    progress when this function is called, the measurement is aborted.

    


.. function:: fetch(maximum_time, reading)

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

    :rtype: ViReal64


            The measured value returned from the DMM.

            


.. function:: fetch_multi_point(maximum_time, array_size, reading_array, actual_number_of_points)

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

        reading_array (ViReal64): 


            An array of measurement values.

            

            .. note:: The size of the **Reading\_Array** must be at least the size that you
                specify for the **Array\_Size** parameter.

        actual_number_of_points (ViInt32): 


            Indicates the number of measured values actually retrieved from the DMM.

            


.. function:: fetch_waveform(maximum_time, array_size, waveform_array, actual_number_of_points)

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

        waveform_array (ViReal64): 


            **Waveform Array** is an array of measurement values stored in waveform
            data type.

            

        actual_number_of_points (ViInt32): 


            Indicates the number of measured values actually retrieved from the DMM.

            


.. function:: format_meas_absolute(measurement_function, range, resolution, measurement, mode_string, range_string, data_string)

    Formats the **Measurement** to the proper number of displayed digits
    according to the **Measurement\_Function**, **Range**, and
    **Resolution**. Returns the formatted data, range, and mode strings.

    


    :param measurement_function:


        Specifies the **measurement\_function** used to acquire the measurement.
        The driver sets :py:data:`nidmm.function` to this value.

        

    :type measurement_function: int
    :param range:


        Specifies the :py:data:`nidmm.range` used to acquire the **Measurement**.

        

    :type range: float
    :param resolution:


        Specifies the :py:data:`nidmm.RESOLUTION\_ABSOLUTE` of the **Measurement**.

        

    :type resolution: float
    :param measurement:


        Specifies the measured value returned from the DMM.

        

    :type measurement: float

    :rtype: tuple (mode_string, range_string, data_string)

        WHERE

        mode_string (ViChar): 


            Returns a string containing the units of the **Measurement** mode.

            

        range_string (ViChar): 


            Returns the :py:data:`nidmm.range` of the **Measurement**, formatted into a
            string with the correct number of display digits.

            

        data_string (ViChar): 


            Returns the **Measurement**, formatted according to the
            :py:data:`nidmm.function`, :py:data:`nidmm.range`, and
            :py:data:`nidmm.RESOLUTION\_ABSOLUTE`.

            


.. function:: get_aperture_time_info(aperture_time, aperture_time_units)

    Returns the DMM **Aperture\_Time** and **Aperture\_Time\_Units**.

    


    :rtype: tuple (aperture_time, aperture_time_units)

        WHERE

        aperture_time (ViReal64): 


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

            

        aperture_time_units (enums.ApertureTimeUnits): 


            Indicates the units of aperture time as powerline cycles (PLCs) or
            seconds. Returns the value of the :py:data:`nidmm.APERTURE\_TIME\_UNITS`
            attribute.

            +---------------------------------+---+------------------+
            | NIDMM\_VAL\_SECONDS             | 0 | Seconds          |
            +---------------------------------+---+------------------+
            | NIDMM\_VAL\_POWER\_LINE\_CYCLES | 1 | Powerline Cycles |
            +---------------------------------+---+------------------+


.. function:: _get_attribute_vi_boolean(channel_name, attribute_id, attribute_value)

    Queries the value of a ViBoolean attribute. You can use this function to
    get the values of instrument-specific attributes and inherent IVI
    attributes.

    If the attribute represents an instrument state, this function performs
    instrument I/O in the following cases:

    -  State caching is disabled for the entire session or for the
       particular attribute.
    -  State caching is enabled, and the currently cached value is invalid.

    


    :param channel_name:


        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int

    :rtype: ViBoolean


            Returns the current value of the attribute. Pass the address of a
            ViBoolean variable.

            


.. function:: _get_attribute_vi_int32(channel_name, attribute_id, attribute_value)

    Queries the value of a ViInt32 attribute. You can use this function to
    get the values of instrument-specific attributes and inherent IVI
    attributes.

    If the attribute represents an instrument state, this function performs
    instrument I/O in the following cases:

    -  State caching is disabled for the entire session or for the
       particular attribute.
    -  State caching is enabled, and the currently cached value is invalid.

    


    :param channel_name:


        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int

    :rtype: ViInt32


            Returns the current value of the attribute. Pass the address of a
            ViInt32 variable.

            


.. function:: _get_attribute_vi_real64(channel_name, attribute_id, attribute_value)

    Queries the value of a ViReal64 attribute. You can use this function to
    get the values of instrument-specific attributes and inherent IVI
    attributes.

    If the attribute represents an instrument state, this function performs
    instrument I/O in the following cases:

    -  State caching is disabled for the entire session or for the
       particular attribute.
    -  State caching is enabled, and the currently cached value is invalid.

    


    :param channel_name:


        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int

    :rtype: ViReal64


            Returns the current value of the attribute. Pass the address of a
            ViReal64 variable.

            


.. function:: _get_attribute_vi_session(channel_name, attribute_id, attribute_value)

    Queries the value of a ViSession attribute. You can use this function to
    get the values of instrument-specific attributes and inherent IVI
    attributes.

    If the attribute represents an instrument state, this function performs
    instrument I/O in the following cases:

    -  State caching is disabled for the entire session or for the
       particular attribute.
    -  State caching is enabled, and the currently cached value is invalid.

    


    :param channel_name:


        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int

    :rtype: ViSession


            Returns the current value of the attribute. Pass the address of a
            ViSession variable.

            


.. function:: _get_attribute_vi_string(channel_name, attribute_id, buffer_size, attribute_value)

    Queries the value of a ViString attribute. You can use this function to
    get the values of instrument-specific attributes and inherent IVI
    attributes.

    If the attribute represents an instrument state, this function performs
    instrument I/O in the following cases:

    -  State caching is disabled for the entire session or for the
       particular attribute.
    -  State caching is enabled, and the currently cached value is invalid.
       You must provide a ViChar array to serve as a buffer for the value.
       You pass the number of bytes in the buffer as the Array Size
       parameter.

    


    :param channel_name:


        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int
    :param buffer_size:


        Pass the number of bytes in the ViChar array you specify for the
        **Attribute\_Value** parameter.

        If the current value of the attribute, including the terminating NULL
        byte, contains more bytes that you indicate in this parameter, the
        function copies **buffer\_size**—1 bytes into the buffer, places an
        ASCII NUL byte at the end of the buffer, and returns the buffer size you
        must pass to get the entire value. For example, if the value is "123456"
        and the **buffer\_size** is 4, the function places "123" into the buffer
        and returns 7.

        If you pass a negative number, the function copies the value to the
        buffer regardless of the number of bytes in the value. If you pass 0,
        you can pass VI\_NULL for the **Attribute\_Value** buffer parameter.

        

    :type buffer_size: int

.. function:: get_auto_range_value(actual_range)

    Returns the **Actual\_Range** that the DMM is using, even when Auto
    Range is off.

    


    :rtype: ViReal64


            Indicates the **actual\_range** the DMM is using. Returns the value of
            the :py:data:`nidmm.AUTO\_RANGE\_VALUE` attribute. The units of the returned
            value depend on the function.

            


.. function:: get_cal_count(cal_type, count)

    Returns the calibration **Count** for the specified type of calibration.

    

    .. note:: The NI 4050, NI 4060, and NI 4080/4081/4082 are not supported.


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

    :rtype: ViInt32


            The number of times calibration has been performed.

            


.. function:: get_cal_date_and_time(cal_type, month, day, year, hour, minute)

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

        month (ViInt32): 


            Indicates the **month** of the last calibration.

            

        day (ViInt32): 


            Indicates the **day** of the last calibration.

            

        year (ViInt32): 


            Indicates the **year** of the last calibration.

            

        hour (ViInt32): 


            Indicates the **hour** of the last calibration.

            

        minute (ViInt32): 


            Indicates the **minute** of the last calibration.

            


.. function:: get_channel_name(index, buffer_size, channel_string)

    Returns the **Channel\_String** that is in the channel table at an
    **Index** you specify. Not applicable to National Instruments DMMs.
    Included for compliance with the *IviDmm Class Specification*.

    


    :param index:


        A 1–based **index** into the channel table.

        

    :type index: int
    :param buffer_size:


        Passes the number of bytes in the ViChar array you specify for the
        **Channel\_String** parameter. If the next **Channel\_String**,
        including the terminating NULL byte, contains more bytes than you
        indicate in this parameter, the function copies
        **buffer\_size** –1 bytes into the buffer, places an ASCII NULL byte at
        the end of the buffer, and returns the buffer size you must pass to get
        the entire value.

        For example, if the value is "123456" and the **buffer\_size** is 4, the
        function places "123" into the buffer and returns 7. If you pass a
        negative number, the function copies the value to the buffer regardless
        of the number of bytes in the value. If you pass 0, you can pass
        VI\_NULL for the **Channel\_String** buffer parameter. The default value
        is None.

        

    :type buffer_size: int

    :rtype: ViChar


            Returns the **channel\_string** that is in the channel table at the
            **Index** you specify. Do not modify the contents of the
            **channel\_string**.

            


.. function:: get_dev_temp(options, temperature)

    Returns the current **Temperature** of the device.

    

    .. note:: The NI 4050 and NI 4060 are not supported.


    :param options:


        Reserved.

        

    :type options: str

    :rtype: ViReal64


            Returns the current **temperature** of the device.

            


.. function:: _get_error(error_code, buffer_size, description)

    Returns the error information associated with the
    **Instrument\_Handle**. This function retrieves and then clears the
    error information for the session. If you leave the
    **Instrument\_Handle** unwired, this function retrieves and then clears
    the error information for the process.

    


    :param buffer_size:


        Passes the number of bytes in the ViChar array you specify for the
        **Description** parameter. If the error description, including the
        terminating NULL byte, contains more bytes than you indicate in this
        parameter, the function copies **buffer\_size** –1 bytes into the
        buffer, places an ASCII NULL byte at the end of the buffer, and returns
        the **buffer\_size** you must pass to get the entire value.

        For example, if the value is "123456" and the **buffer\_size** is 4, the
        function places "123" into the buffer and returns 7. If you pass a
        negative number, the function copies the value to the buffer regardless
        of the number of bytes in the value. If you pass 0, you can pass
        VI\_NULL for the **Description** buffer parameter. The default value is
        None.

        

    :type buffer_size: int

    :rtype: ViStatus


            Returns the **error\_code** for the session or execution thread. If you
            pass 0 for the **Buffer\_Size**, you can pass VI\_NULL for this
            parameter.

            


.. function:: _get_error_message(error_code, buffer_size, error_message)

    Returns the **Error\_Message** as a user-readable string for the
    provided **Error\_Code**. Calling this function with a **Buffer\_Size**
    of 0 returns the size needed for the **Error\_Message**.

    


    :param error_code:


        The error code returned from the instrument for which you want to get a
        user-readable string.

        

    :type error_code: int
    :param buffer_size:


        Specifies the number of bytes allocated for the **Error\_Message**
        ViChar array. If the error description that this function returns
        (including terminating NULL byte) is larger than you indicated in
        **buffer\_size**, the error description will be truncated to fit. If you
        pass 0 for **buffer\_size**, the function returns the buffer size needed
        for **Error\_Message**.

        

    :type buffer_size: int

.. function:: get_last_cal_temp(cal_type, temperature)

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

    :rtype: ViReal64


            Returns the **temperature** during the last calibration.

            


.. function:: get_measurement_period(period)

    Returns the measurement **Period**, which is the amount of time it takes
    to complete one measurement with the current configuration. Use this
    function right before you begin acquiring data—after you have completely
    configured the measurement and after all configuration functions have
    been called.

    


    :rtype: ViReal64


            Returns the number of seconds it takes to make one measurement.

            The first measurement in a multipoint acquisition requires additional
            settling time. This function does not include this additional time or
            any :py:data:`nidmm.TRIGGER\_DELAY` associated with the first measurement.
            Time required for internal measurements, such as
            :py:data:`nidmm.AUTO\_ZERO`, is included.

            


.. function:: get_next_coercion_record(buffer_size, coercion_record)

    This function returns the coercion information associated with the IVI
    session, and it retrieves and clears the oldest instance in which NI-DMM
    coerced a value you specified to another value.

    If you set :py:data:`nidmm.RECORD\_COERCIONS` to VI\_TRUE (1), NI-DMM keeps
    a list of all coercions it makes on ViInt32 or ViReal64 values that you
    pass to NI-DMM functions. Use this function to retrieve information from
    that list.

    


    :param buffer_size:


        Passes the number of bytes in the ViChar array you specify for the
        **Coercion\_Record** parameter. If the next coercion record string,
        including the terminating NULL byte, contains more bytes than you
        indicate in this parameter, the function copies **buffer\_size** – 1
        bytes into the buffer, places an ASCII NULL byte at the end of the
        buffer, and returns the buffer size you must pass to get the entire
        value.

        For example, if the value is "123456" and the **buffer\_size** is 4, the
        function places "123" into the buffer and returns 7. If you pass a
        negative number, the function copies the value to the buffer regardless
        of the number of bytes in the value.

        If you pass 0, you can pass VI\_NULL for the **Coercion\_Record** buffer
        parameter.

        The default value is None.

        

    :type buffer_size: int

    :rtype: ViChar


            Returns the next **coercion\_record** for the IVI session.

            If there are no coercions records, the function returns an empty string.
            The buffer must contain at least as many elements as the value you
            specify with the **Buffer\_Size** parameter.

            


.. function:: get_next_interchange_warning(buffer_size, interchange_warning)

    This function returns the interchangeability warnings associated with
    the IVI session. It retrieves and clears the oldest instance in which
    the class driver recorded an interchangeability warning.
    Interchangeability warnings indicate that using your application with a
    different instrument might cause different behavior.

    The driver performs interchangeability checking when
    :py:data:`nidmm.INTERCHANGE\_CHECK` is set to VI\_TRUE (1). The function
    returns an empty string in the **Interchange\_Warning** parameter if no
    interchangeability warnings remain for the session. In general, the
    instrument driver generates interchangeability warnings when an
    attribute that affects the behavior of the instrument is in a state that
    you did not specify.

    


    :param buffer_size:


        Passes the number of bytes in the ViChar array you specify for the
        **Interchange\_Warning** parameter. If the next interchangeability
        warning string, including the terminating NULL byte, contains more bytes
        than you indicate in this parameter, the function copies
        **buffer\_size** –1 bytes into the buffer, places an ASCII NULL byte at
        the end of the buffer, and returns the buffer size you must pass to get
        the entire value.

        For example, if the value is "123456" and the **buffer\_size** is 4, the
        function places "123" into the buffer and returns 7. If you pass a
        negative number, the function copies the value to the buffer regardless
        of the number of bytes in the value. If you pass 0, you can pass
        VI\_NULL for the **Interchange\_Warning** buffer parameter. The default
        value is None.

        

    :type buffer_size: int

.. function:: get_self_cal_supported(self_cal_supported)

    Returns a Boolean value that expresses whether or not the DMM that you
    are using can perform self-calibration.

    


    :rtype: ViBoolean


            Returns whether Self Cal is supported for the device specified by the
            given session.

            +-----------+---+-------------------------------------------------------------+
            | VI\_TRUE  | 1 | The DMM that you are using can perform self-calibration.    |
            +-----------+---+-------------------------------------------------------------+
            | VI\_FALSE | 0 | The DMM that you are using cannot perform self-calibration. |
            +-----------+---+-------------------------------------------------------------+


.. function:: _init_with_options(resource_name, id_query, reset_device, option_string)

    This function completes the following tasks:

    -  Creates a new IVI instrument driver session and, optionally, sets the
       initial state of the following session attributes:
       :py:data:`nidmm.RANGE\_CHECK`, :py:data:`nidmm.QUERY\_INSTR\_STATUS`,
       :py:data:`nidmm.cache`, :py:data:`nidmm.simulate`,
       :py:data:`nidmm.RECORD\_COERCIONS`.
    -  Opens a session to the device you specify for the **Resource\_Name**
       parameter. If the **ID\_Query** parameter is set to VI\_TRUE, this
       function queries the instrument ID and checks that it is valid for
       this instrument driver.
    -  If the **Reset\_Device** parameter is set to VI\_TRUE, this function
       resets the instrument to a known state. Sends initialization commands
       to set the instrument to the state necessary for the operation of the
       instrument driver.
    -  Returns a ViSession handle that you use to identify the instrument in
       all subsequent instrument driver function calls.

    


    :param resource_name:


        .. caution:: All IVI names for the **Resource\_Name**, such as logical names or
            virtual names, are case-sensitive. If you use logical names, driver
            session names, or virtual names in your program, you must make sure that
            the name you use matches the name in the IVI Configuration Store file
            exactly, without any variations in the case of the characters in the
            name.

        | Contains the **resource\_name** of the device to initialize. The
          **resource\_name** is assigned in Measurement & Automation Explorer
          (MAX). Refer to `Related
          Documentation <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/related_documentation/>`__
          for the *NI Digital Multimeters Getting Started Guide* for more
          information about configuring and testing the DMM in MAX.
        | Valid Syntax:

        -  NI-DAQmx name
        -  DAQ::NI-DAQmx name[::INSTR]
        -  DAQ::Traditional NI-DAQ device number[::INSTR]
        -  IVI logical name

        

    :type resource_name: str
    :param id_query:


        Verifies that the device you initialize is one that the driver supports.
        NI-DMM automatically performs this query, so setting this parameter is
        not necessary.
        Defined Values:

        +--------------------+---+------------------+
        | VI\_TRUE (default) | 1 | Perform ID Query |
        +--------------------+---+------------------+
        | VI\_FALSE          | 0 | Skip ID Query    |
        +--------------------+---+------------------+

    :type id_query: bool
    :param reset_device:


        Specifies whether to reset the instrument during the initialization
        procedure.
        Defined Values:

        +--------------------+---+--------------+
        | VI\_TRUE (default) | 1 | Reset Device |
        +--------------------+---+--------------+
        | VI\_FALSE          | 0 | Don't Reset  |
        +--------------------+---+--------------+

    :type reset_device: bool
    :param option_string:


        | Sets the initial value of certain attributes for the session. The
          following table specifies the attribute name, attribute constant, and
          default value for each attribute that you can use in this parameter:

        The format of this string is, "AttributeName=Value." To set multiple
        attributes, separate their assignments with a comma.

        If you pass NULL or an empty string for this parameter, the session uses
        the default values for the attributes. You can override the default
        values by assigning a value explicitly in an **option\_string**
        parameter. You do not have to specify all of the attributes and may
        leave any of them out (those left out use the default value).

        Refer to `Simulating NI Digital
        Multimeters <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/simulation/>`__
        for more information.

        +------------------+---------------------------------------+-------------------+----+
        | Check            | :py:data:`nidmm.RANGE\_CHECK`         | VI\_TRUE          | 1  |
        +------------------+---------------------------------------+-------------------+----+
        | QueryInstrStatus | :py:data:`nidmm.QUERY\_INSTR\_STATUS` | VI\_FALSE         | 0  |
        +------------------+---------------------------------------+-------------------+----+
        | Cache            | :py:data:`nidmm.cache`                | VI\_TRUE          | 1  |
        +------------------+---------------------------------------+-------------------+----+
        | Simulate         | :py:data:`nidmm.simulate`             | VI\_FALSE         | 0  |
        +------------------+---------------------------------------+-------------------+----+
        | RecordCoercions  | :py:data:`nidmm.RECORD\_COERCIONS`    | VI\_FALSE         | 0  |
        +------------------+---------------------------------------+-------------------+----+
        | DriverSetup      | :py:data:`nidmm.DRIVER\_SETUP`        | "" (empty string) | "" |
        +------------------+---------------------------------------+-------------------+----+

    :type option_string: str

    :rtype: ViSession


            Returns a ViSession handle that you use to identify the instrument in
            all subsequent instrument driver function calls.

            


.. function:: _initiate()

    Initiates an acquisition. After you call this function, the DMM leaves
    the Idle state and enters the Wait-for-Trigger state. If trigger is set
    to Immediate mode, the DMM begins acquiring measurement data. Use
    :py:func:`nidmm.fetch`, :py:func:`nidmm.fetch_multi_point`, or :py:func:`nidmm.fetch_waveform` to
    retrieve the measurement data.

    


.. function:: is_over_range(measurement_value, is_over_range)

    Takes a **Measurement\_Value** and determines if the value is a valid
    measurement or a value indicating that an overrange condition occurred.

    


    :param measurement_value:


        The measured value returned from the DMM.

        

        .. note:: If an overrange condition occurs, the **Measurement\_Value** contains
            an IEEE-defined NaN (Not a Number) value.

    :type measurement_value: float

    :rtype: ViBoolean


            Returns whether the measurement value is a valid measurement or an
            overrange condition.

            +-----------+---+-----------------------------------------------------------+
            | VI\_TRUE  | 1 | The value indicates that an overrange condition occurred. |
            +-----------+---+-----------------------------------------------------------+
            | VI\_FALSE | 0 | The value is a valid measurement.                         |
            +-----------+---+-----------------------------------------------------------+


.. function:: is_under_range(measurement_value, is_under_range)

    Takes a **Measurement\_Value** and determines if the value is a valid
    measurement or a value indicating that an underrange condition occurred.

    


    :param measurement_value:


        The measured value returned from the DMM.

        

        .. note:: If an overrange condition occurs, the **Measurement\_Value** contains
            an IEEE-defined NaN (Not a Number) value.

    :type measurement_value: float

    :rtype: ViBoolean


            Returns whether the **Measurement\_Value** is a valid measurement or an
            underrange condition.

            +-----------+---+------------------------------------------------------------+
            | VI\_TRUE  | 1 | The value indicates that an underrange condition occurred. |
            +-----------+---+------------------------------------------------------------+
            | VI\_FALSE | 0 | The value is a valid measurement.                          |
            +-----------+---+------------------------------------------------------------+


.. function:: _lock_session(caller_has_lock)

    This function obtains a multithread lock on the instrument session.
    Before it does so, it waits until all other execution threads have
    released their locks on the instrument session.

    Other threads might have obtained a lock on this session in the
    following ways:

    -  The user application called this function.
    -  A call to the instrument driver locked the session.
    -  A call to the IVI Library locked the session.

    After your call to this function returns successfully, no other threads
    can access the instrument session until you call :py:func:`nidmm._unlock_session`.

    Use this function and :py:func:`nidmm._unlock_session` around a sequence of calls to
    instrument driver functions if you require that the instrument retain
    its settings through the end of the sequence. You can safely make nested
    calls to this function within the same thread.

    To completely unlock the session, you must balance each call to this
    function with a call to :py:func:`nidmm._unlock_session`. If, however, you use the
    **Caller\_Has\_Lock** parameter in all calls to this function and
    :py:func:`nidmm._unlock_session` within a function, the IVI Library locks the
    session only once within the function regardless of the number of calls
    you make to this function. This feature allows you to call
    :py:func:`nidmm._unlock_session` just once at the end of the function.

    


    :rtype: ViBoolean


            This parameter serves as a convenience. If you do not want to use this
            parameter, pass VI\_NULL. Use this parameter in complex functions to
            keep track of whether you obtain a lock and, therefore, need to unlock
            the session. To use this parameter, complete the following steps:

            #. Pass the address of a local ViBoolean variable.
            #. In the declaration of the local variable, initialize it to VI\_FALSE
               (0).
            #. Pass the address of the same local variable to any other calls you
               make to this function or :py:func:`nidmm._unlock_session` in the same function.

            The parameter is an input/output parameter. This function and
            :py:func:`nidmm._unlock_session` each inspect the current value and take the
            following actions:

            If the value is VI\_TRUE (1), this function does not lock the session
            again. If the value is VI\_FALSE, this function obtains the lock and
            sets the value of the parameter to VI\_TRUE.

            If the value is VI\_FALSE, :py:func:`nidmm._unlock_session` does not attempt to
            unlock the session. If the value is VI\_TRUE, :py:func:`nidmm._unlock_session`
            releases the lock and sets the value of the parameter to VI\_FALSE.
            Thus, you can, call :py:func:`nidmm._unlock_session` at the end of your function
            without worrying about whether you actually have the lock.

            **Example**

            ViStatus TestFunc (ViSession vi, ViInt32 flags)

            {

            | ViStatus error = VI\_SUCCESS;
            | ViBoolean haveLock = VI\_FALSE;
            | if (flags & BIT\_1)

            | {
            | viCheckErr( NIDMM\_LockSession(vi, &haveLock;));
            | viCheckErr( TakeAction1(vi));
            | if (flags & BIT\_2)

            {

            viCheckErr( NIDMM\_UnlockSession(vi, &haveLock;));

            viCheckErr( TakeAction2(vi));

            viCheckErr( NIDMM\_LockSession(vi, &haveLock;);

            }

            if (flags & BIT\_3)

            viCheckErr( TakeAction3(vi));

            }

            Error:

            /\*

            At this point, you cannot really be sure that you have the lock.
            Fortunately, the haveLock variable takes care of that for you.

            \*/

            :py:func:`nidmm._unlock_session`(vi, &haveLock;);

            return error;

            }

            


.. function:: perform_open_cable_comp(conductance, susceptance)

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

        conductance (ViReal64): 


            **conductance** is the measured value of open cable compensation
            **conductance**.

            

        susceptance (ViReal64): 


            **susceptance** is the measured value of open cable compensation
            **susceptance**.

            


.. function:: perform_short_cable_comp(resistance, reactance)

    Performs the short cable compensation measurements for the current
    capacitance/inductance range, and returns short cable compensation
    **Resistance** and **Reactance** values. You can use the return values
    of this function as inputs to :py:func:`nidmm.configure_short_cable_comp_values`.

    This function returns an error if the value of the :py:data:`nidmm.function`
    attribute is not set to NIDMM\_VAL\_CAPACITANCE (1005) or
    NIDMM\_VAL\_INDUCTANCE (1006).

    


    :rtype: tuple (resistance, reactance)

        WHERE

        resistance (ViReal64): 


            **resistance** is the measured value of short cable compensation
            **resistance**.

            

        reactance (ViReal64): 


            **reactance** is the measured value of short cable compensation
            **reactance**.

            


.. function:: read(maximum_time, reading)

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

    :rtype: ViReal64


            The measured value returned from the DMM.

            


.. function:: read_multi_point(maximum_time, array_size, reading_array, actual_number_of_points)

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

        reading_array (ViReal64): 


            An array of measurement values.

            

            .. note:: The size of the **Reading\_Array** must be at least the size that you
                specify for the **Array\_Size** parameter.

        actual_number_of_points (ViInt32): 


            Indicates the number of measured values actually retrieved from the DMM.

            


.. function:: read_status(acquisition_backlog, acquisition_status)

    Returns measurement backlog and acquisition status. Use this function to
    determine how many measurements are available before calling
    :py:func:`nidmm.fetch`, :py:func:`nidmm.fetch_multi_point`, or :py:func:`nidmm.fetch_waveform`.

    

    .. note:: The NI 4050 is not supported.


    :rtype: tuple (acquisition_backlog, acquisition_status)

        WHERE

        acquisition_backlog (ViInt32): 


            The number of measurements available to be read. If the backlog
            continues to increase, data is eventually overwritten, resulting in an
            error.

            

            .. note:: On the NI 4060, the **Backlog** does not increase when autoranging. On
                the NI 4065, the **Backlog** does not increase when Range is set to AUTO
                RANGE ON (-1), or before the first point is fetched when Range is set to
                AUTO RANGE ONCE (-3). These behaviors are due to the autorange model of
                the devices.

        acquisition_status (enums.AcquisitionStatus): 


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


.. function:: read_waveform(maximum_time, array_size, waveform_array, actual_number_of_points)

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

        waveform_array (ViReal64): 


            An array of measurement values.

            

            .. note:: The size of the **Waveform\_Array** must be at least the size that you
                specify for the **Array\_Size** parameter.

        actual_number_of_points (ViInt32): 


            Indicates the number of measured values actually retrieved from the DMM.

            


.. function:: reset_interchange_check()

    When developing a complex test system that consists of multiple test
    modules, it is generally a good idea to design the test modules so that
    they can run in any order. To do so requires ensuring that each test
    module completely configures the state of each instrument it uses.

    If a particular test module does not completely configure the state of
    an instrument, the state of the instrument depends on the configuration
    from a previously executed test module. If you execute the test modules
    in a different order, the behavior of the instrument and therefore the
    entire test module is likely to change. This change in behavior is
    generally instrument specific and represents an interchangeability
    problem. You can use this function to test for such cases. After you
    call this function, the interchangeability checking algorithms in NI-DMM
    ignore all previous configuration operations. By calling this function
    at the beginning of a test module, you can determine whether the test
    module has dependencies on the operation of previously executed test
    modules.

    This function does not clear the interchangeability warnings from the
    list of previously recorded interchangeability warnings. If you want to
    guarantee that :py:func:`nidmm.get_next_interchange_warning` only returns those
    interchangeability warnings that are generated after calling this
    function, you must clear the list of interchangeability warnings. You
    can clear the interchangeability warnings list by repeatedly calling
    :py:func:`nidmm.get_next_interchange_warning` until no more interchangeability
    warnings are returned. If you are not interested in the content of those
    warnings, you can call :py:func:`nidmm.clear_interchange_warnings`.

    


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

    


.. function:: _set_attribute_vi_boolean(channel_name, attribute_id, attribute_value)

    This function sets the value of a ViBoolean attribute.

    This is a low-level function that you can use to set the values of
    instrument-specific attributes and inherent IVI attributes.

    If the attribute represents an instrument state, this function performs
    instrument I/O in the following cases:

    -  State caching is disabled for the entire session or for the
       particular attribute.
    -  State caching is enabled, and the currently cached value is invalid
       or is different than the value you specify.

    This instrument driver contains high-level functions that set most of
    the instrument attributes. It is best to use the high-level driver
    functions as much as possible. They handle order dependencies and
    multithread locking for you. In addition, they perform status checking
    only after setting all of the attributes.

    In contrast, when you set multiple attributes using the SetAttribute
    functions, the functions check the instrument status after each call.
    Also, when state caching is enabled, the high-level functions that
    configure multiple attributes perform instrument I/O only for the
    attributes whose value you change. Thus, you can safely call the
    high-level functions without the penalty of redundant instrument I/O.

    


    :param channel_name:


        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int
    :param attribute_value:


        Pass the value that you want to set the attribute to.

        

    :type attribute_value: bool

.. function:: _set_attribute_vi_int32(channel_name, attribute_id, attribute_value)

    This function sets the value of a ViInt32 attribute.

    This is a low-level function that you can use to set the values of
    instrument-specific attributes and inherent IVI attributes.

    If the attribute represents an instrument state, this function performs
    instrument I/O in the following cases:

    -  State caching is disabled for the entire session or for the
       particular attribute.
    -  State caching is enabled, and the currently cached value is invalid
       or is different than the value you specify.

    This instrument driver contains high-level functions that set most of
    the instrument attributes. It is best to use the high-level driver
    functions as much as possible. They handle order dependencies and
    multithread locking for you. In addition, they perform status checking
    only after setting all of the attributes.

    In contrast, when you set multiple attributes using the SetAttribute
    functions, the functions check the instrument status after each call.
    Also, when state caching is enabled, the high-level functions that
    configure multiple attributes perform instrument I/O only for the
    attributes whose value you change. Thus, you can safely call the
    high-level functions without the penalty of redundant instrument I/O.

    


    :param channel_name:


        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int
    :param attribute_value:


        Pass the value that you want to set the attribute to.

        

    :type attribute_value: int

.. function:: _set_attribute_vi_real64(channel_name, attribute_id, attribute_value)

    This function sets the value of a ViReal64 attribute.

    This is a low-level function that you can use to set the values of
    instrument-specific attributes and inherent IVI attributes.

    If the attribute represents an instrument state, this function performs
    instrument I/O in the following cases:

    -  State caching is disabled for the entire session or for the
       particular attribute.
    -  State caching is enabled, and the currently cached value is invalid
       or is different than the value you specify.

    This instrument driver contains high-level functions that set most of
    the instrument attributes. It is best to use the high-level driver
    functions as much as possible. They handle order dependencies and
    multithread locking for you. In addition, they perform status checking
    only after setting all of the attributes.

    In contrast, when you set multiple attributes using the SetAttribute
    functions, the functions check the instrument status after each call.
    Also, when state caching is enabled, the high-level functions that
    configure multiple attributes perform instrument I/O only for the
    attributes whose value you change. Thus, you can safely call the
    high-level functions without the penalty of redundant instrument I/O.

    


    :param channel_name:


        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int
    :param attribute_value:


        Pass the value that you want to set the attribute to.

        

    :type attribute_value: float

.. function:: _set_attribute_vi_session(channel_name, attribute_id, attribute_value)

    This function sets the value of a ViSession attribute.

    This is a low-level function that you can use to set the values of
    instrument-specific attributes and inherent IVI attributes.

    If the attribute represents an instrument state, this function performs
    instrument I/O in the following cases:

    -  State caching is disabled for the entire session or for the
       particular attribute.
    -  State caching is enabled, and the currently cached value is invalid
       or is different than the value you specify.

    


    :param channel_name:


        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int
    :param attribute_value:


        Pass the value that you want to set the attribute to.

        

    :type attribute_value: int

.. function:: _set_attribute_vi_string(channel_name, attribute_id, attribute_value)

    This function sets the value of a ViString attribute.

    This is a low-level function that you can use to set the values of
    instrument-specific attributes and inherent IVI attributes.

    If the attribute represents an instrument state, this function performs
    instrument I/O in the following cases:

    -  State caching is disabled for the entire session or for the
       particular attribute.
    -  State caching is enabled, and the currently cached value is invalid
       or is different than the value you specify.

    This instrument driver contains high-level functions that set most of
    the instrument attributes. It is best to use the high-level driver
    functions as much as possible. They handle order dependencies and
    multithread locking for you. In addition, they perform status checking
    only after setting all of the attributes.

    In contrast, when you set multiple attributes using the SetAttribute
    functions, the functions check the instrument status after each call.
    Also, when state caching is enabled, the high-level functions that
    configure multiple attributes perform instrument I/O only for the
    attributes whose value you change. Thus, you can safely call the
    high-level functions without the penalty of redundant instrument I/O.

    


    :param channel_name:


        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

        

    :type channel_name: str
    :param attribute_id:


        Pass the ID of an attribute.

        

    :type attribute_id: int
    :param attribute_value:


        Pass the value that you want to set the attribute to.

        

    :type attribute_value: str

.. function:: _unlock_session(caller_has_lock)

    This function releases a lock that you acquired on an instrument session
    using :py:func:`nidmm._lock_session`. Refer to :py:func:`nidmm._lock_session` for additional
    information on session locks.

    


    :rtype: ViBoolean


            This parameter serves as a convenience. If you do not want to use this
            parameter, pass VI\_NULL.

            Use this parameter in complex functions to keep track of whether you
            obtain a lock and, therefore, need to unlock the session.

            To use this parameter, complete the following steps:

            #. Pass the address of a local ViBoolean variable.
            #. In the declaration of the local variable, initialize it to VI\_FALSE
               (0).
            #. Pass the address of the same local variable to any other calls you
               make to :py:func:`nidmm._lock_session` or this function in the same function.

            The parameter is an input/output parameter. :py:func:`nidmm._lock_session` and this
            function each inspect the current value and take the following actions:

            If the value is VI\_TRUE (1), :py:func:`nidmm._lock_session` does not lock the
            session again. If the value is VI\_FALSE, :py:func:`nidmm._lock_session` obtains the
            lock and sets the value of the parameter to VI\_TRUE.

            If the value is VI\_FALSE, this function does not attempt to unlock the
            session. If the value is VI\_TRUE, this function releases the lock and
            sets the value of the parameter to VI\_FALSE. Thus, you can, call this
            function at the end of your function without worrying about whether you
            actually have the lock.

            **Example**

            ViStatus TestFunc (ViSession vi, ViInt32 flags)

            {

            ViStatus error = VI\_SUCCESS;

            ViBoolean haveLock = VI\_FALSE;

            if (flags & BIT\_1)

            {

            viCheckErr( NIDMM\_LockSession(vi, &haveLock;));

            viCheckErr( TakeAction1(vi));

            if (flags & BIT\_2)

            {

            viCheckErr( NIDMM\_UnlockSession(vi, &haveLock;));

            viCheckErr( TakeAction2(vi));

            viCheckErr( NIDMM\_LockSession(vi, &haveLock;);

            }

            if (flags & BIT\_3)

            viCheckErr( TakeAction3(vi));

            }

            Error:

            /\*

            At this point, you cannot really be sure that you have the lock.
            Fortunately, the haveLock variable takes care of that for you.

            \*/

            :py:func:`nidmm._unlock_session`(vi, &haveLock;);

            return error;

            }

            


.. function:: _close()

    Closes the specified session and deallocates resources that it reserved.

    


.. function:: error_message(error_code, error_message)

    Takes the **Error\_Code** returned by the instrument driver functions,
    interprets it, and returns it as a user-readable string.

    


    :param error_code:


        The **error\_code** returned from the instrument. The default is 0,
        indicating VI\_SUCCESS.

        

    :type error_code: int

    :rtype: ViChar


            The error information formatted into a string.

            


.. function:: error_query(error_code, error_message)

    Reads an **Error\_Code** and message from the DMM error queue. National
    Instruments DMMs do not contain an error queue. Errors are reported as
    they occur. Therefore, this function does not detect errors; it is
    included for compliance with the *IviDmm Class Specification*.

    


    :rtype: tuple (error_code, error_message)

        WHERE

        error_code (ViStatus): 


            The **error\_code** returned from the instrument.

            The default value is VI\_SUCCESS (0).

            

        error_message (ViChar): 


            Formats the **Error\_Code** into a user-readable message string.

            

            .. note:: The array must contain at least 256 elements ViChar[256].


.. function:: reset()

    Resets the instrument to a known state and sends initialization commands
    to the instrument. The initialization commands set instrument settings
    to the state necessary for the operation of the instrument driver.

    


.. function:: revision_query(instrument_driver_revision, firmware_revision)

    Returns the revision numbers of the instrument driver and instrument
    firmware.

    


    :rtype: tuple (instrument_driver_revision, firmware_revision)

        WHERE

        instrument_driver_revision (ViChar): 


            Returns a string containing the instrument driver software revision
            numbers.

            

            .. note:: The array must contain at least 256 elements ViChar[256].

        firmware_revision (ViChar): 


            Returns a string containing the instrument **firmware\_revision**
            numbers.

            

            .. note:: The array must contain at least 256 elements ViChar[256].


.. function:: self_test(self_test_result, self_test_message)

    Performs a self-test on the DMM to ensure that the DMM is functioning
    properly. Self-test does not calibrate the DMM.

    

    .. note:: This function calls :py:func:`nidmm.reset`, and any configurations previous to
        the call will be lost. All attributes will be set to their default
        values after the call returns.


    :rtype: tuple (self_test_result, self_test_message)

        WHERE

        self_test_result (ViInt16): 


            Contains the value returned from the instrument self-test. Zero
            indicates success.

            On the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that
            you should check the fuse and replace it, if necessary.

            

            .. note:: Self-test does not check the fuse on the NI 4065, NI 4071, and
                NI 4081. Hence, even if the fuse is blown on the device, self-test does
                not return error code 1013.

        self_test_message (ViChar): 


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

            



