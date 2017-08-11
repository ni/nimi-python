NI-DMM Functions
================

.. py:currentmodule:: nidmm


.. function:: _abort()

    Aborts a previously initiated measurement and returns the DMM to the
    Idle state.


.. function:: _clear_error()

    Clears the error information for the current execution thread and the
    IVI session you specify. If you pass VI\_NULL for the
    **vi** parameter, this function clears the error
    information only for the current execution thread.


.. function:: clear_interchange_warnings()

    Clears the list of current interchange warnings.


.. function:: configure_ac_bandwidth(ac_minimum_frequency_hz, ac_maximum_frequency_hz)

    Configures the :py:data:`nidmm.ac_min_freq` and :py:data:`nidmm.ac_max_freq`
    attributes, which the DMM uses for AC measurements.

    :param ac_minimum_frequency_hz: 
        Specifies the minimum expected frequency component of the input signal
        in hertz. This parameter affects the DMM only when you set the
        :py:data:`nidmm.function` attribute to AC measurements. NI-DMM uses this
        parameter to calculate the proper aperture for the measurement.
        The driver sets the :py:data:`nidmm.ac_min_freq` attribute to this value.
        The valid range is 1 Hz–300 kHz for the NI 4080/4081/4082 and the NI
        4070/4071/4072, 10 Hz–100 Hz for the NI 4065, and 20 Hz–25 kHz for the
        NI 4050 and NI 4060.

    :type ac_minimum_frequency_hz: ViReal64
    :param ac_maximum_frequency_hz: 
        Specifies the maximum expected frequency component of the input signal
        in hertz within the device limits. This parameter is used only for error
        checking and verifies that the value of this parameter is less than the
        maximum frequency of the device.

        This parameter affects the DMM only when you set the
        :py:data:`nidmm.function` attribute to AC measurements. The driver sets the
        :py:data:`nidmm.ac_max_freq` attribute to this value. The valid range is 1
        Hz–300 kHz for the NI 4080/4081/4082 and the NI 4070/4071/4072, 10
        Hz–100 Hz for the NI 4065, and 20 Hz–25 kHz for the NI 4050 and NI 4060.

    :type ac_maximum_frequency_hz: ViReal64


.. function:: configure_adc_calibration(adc_calibration)

    For the NI 4080/4081/4082 and NI 4070/4071/4072, allows the DMM to
    compensate for gain drift since the last external calibration or
    self-calibration. When **ADC\_Calibration** is ON, the DMM measures an
    internal reference to calculate the correct gain for the measurement.
    When **ADC\_Calibration** is OFF, the DMM does not compensate for
    changes to the gain.

    :param adc_calibration: 
        Specifies the **ADC\_Calibration** setting. The driver sets
        :py:data:`nidmm.adc_calibration` to this value.
        NIDMM\_VAL\_ADC\_CALIBRATION\_ON enables **ADC\_Calibration**.
        NIDMM\_VAL\_ADC\_CALIBRATION\_OFF disables **ADC\_Calibration**. If you
        set the value to NIDMM\_VAL\_ADC\_CALIBRATION\_AUTO, the driver
        determines whether to enable **ADC\_Calibration** based on the
        measurement function and resolution that you configure. If you configure
        the NI 4080/4081/4082 or NI 4070/4071/4072 for a 6½–digit and greater
        resolution DC measurement, the driver enables ADC Calibration. For all
        other measurement configurations, the driver disables
        **ADC\_Calibration**.

        +------------------------------------------------+---------+-----------------------------------------------------------------------------------------------------+
        | Name                                           | Value   | Description                                                                                         |
        +================================================+=========+=====================================================================================================+
        | NIDMM\_VAL\_ADC\_CALIBRATION\_AUTO (default)   | -1.0    | The DMM enables or disables **ADC\_Calibration** based on the configured function and resolution.   |
        +------------------------------------------------+---------+-----------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_ADC\_CALIBRATION\_OFF              |  0      | The DMM does not compensate for changes to the gain.                                                |
        +------------------------------------------------+---------+-----------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_ADC\_CALIBRATION\_ON               |  1      | The DMM measures an internal reference to calculate the correct gain for the measurement.           |
        +------------------------------------------------+---------+-----------------------------------------------------------------------------------------------------+

    :type adc_calibration: :py:data:`nidmm.ADCCalibration`


.. function:: configure_auto_zero_mode(auto_zero_mode)

    Configures the DMM for **auto_zero_mode**. When **auto_zero_mode**
    is ON, the DMM internally disconnects the input signal and takes a zero
    reading. It then subtracts the zero reading from the measurement. This
    prevents offset voltages present on the input circuitry of the DMM from
    affecting measurement accuracy. When **auto_zero_mode** is OFF, the
    DMM does not compensate for zero reading offset.

    :param auto_zero_mode: 
        Specifies the **auto\_zero\_mode**. NI-DMM sets the
        :py:data:`nidmm.auto_zero` attribute to this value.

        ON enables **auto\_zero\_mode** for each measurement. ONCE enables
        **auto\_zero\_mode** before the next measurement. The
        **auto\_zero\_mode** value is stored and used in subsequent measurements
        until the device is reconfigured.

        OFF disables **auto\_zero\_mode**. If you set this parameter to AUTO,
        NI-DMM determines whether to enable Auto Zero based on the measurement
        function that you configure. If you configure the NI 4080/4081/4082 or
        the NI 4070/4071/4072 for a 6½–digit and greater resolution DC
        measurement, NI-DMM sets **auto\_zero\_mode** to ON.

        For all other DC measurement configurations on the NI 4080/4081/4082 or
        the NI 4070/4071/4072, NI-DMM sets **auto\_zero\_mode** to ONCE. For all
        AC measurements or waveform acquisitions on the NI 4080/4081/4082 or the
        NI 4070/4071/4072, NI-DMM sets **auto\_zero\_mode** to OFF. For NI 4060,
        **auto\_zero\_mode** is set to OFF when AUTO is selected.

        For NI 4065 devices, **auto\_zero\_mode** is always ON.
        **auto\_zero\_mode** is an integral part of the signal measurement phase
        and adds no extra time to the overall measurement.


        .. note:: The NI 4060/4065 does *not* support this setting.
    :type auto_zero_mode: :py:data:`nidmm.AutoZero`


.. function:: configure_cable_comp_type(cable_comp_type)

    For the NI 4082 and NI 4072 only, sets the
    :py:data:`nidmm.CABLE\_COMP\_TYPE` attribute for the current
    capacitance/inductance mode range.

    :param cable_comp_type: 
        Specifies the type of cable compensation that is used for the current
        range.

    :type cable_comp_type: :py:data:`nidmm.CableCompensationType`


.. function:: configure_current_source(current_source)

    The NI 4050 and NI 4060 are not supported. Configures the
    **current_source** for diode measurements.

    :param current_source: 
        Specifies the **current\_source** provided during diode measurements.
        For valid ranges, refer to the device sections for your device. The
        driver sets :py:data:`nidmm.current_source` to this value.

        +-------------------------------------+----------+-----------------------------------------------------+
        | NIDMM\_VAL\_1\_MICROAMP             | 1 µA     | NI 4080/4081/4082 and NI 4070/4071/4072             |
        +-------------------------------------+----------+-----------------------------------------------------+
        | NIDMM\_VAL\_10\_MICROAMP            | 10 µA    | NI 4080/4081/4082 and NI 4070/4071/4072 only        |
        +-------------------------------------+----------+-----------------------------------------------------+
        | NIDMM\_VAL\_100\_MICROAMP           | 100 µA   | NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065   |
        +-------------------------------------+----------+-----------------------------------------------------+
        | NIDMM\_VAL\_1\_MILLIAMP (default)   | 1 mA     | NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065   |
        +-------------------------------------+----------+-----------------------------------------------------+

    :type current_source: :py:data:`nidmm.CurrentSource`


.. function:: configure_fixed_ref_junction(fixed_reference_junction)

    Configures the fixed reference junction temperature for a thermocouple
    with a fixed reference junction type.

    :param fixed_reference_junction: 
        Specifies the reference junction temperature when a fixed reference
        junction is used to take a thermocouple measurement. The units are
        degrees Celsius. NI-DMM uses this value to set the Fixed Reference
        Junction property. The default is 25.00 (°C).

    :type fixed_reference_junction: ViReal64


.. function:: configure_frequency_voltage_range(voltage_range)

    For the NI 4080/4081/4082 and the NI 4070/4071/4072 only, specifies the
    expected maximum amplitude of the input signal for frequency and period
    measurements.

    :param voltage_range: 
        Sets the expected maximum amplitude of the input signal. Refer to the
        `NI 4080 <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4080_functional_overview/>`__,
        `NI 4081 <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4081_functional_overview/>`__,
        `NI 4072 <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4082/>`__,
        `NI 4070 <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4070_functional_overview/>`__,
        `NI 4071 <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4071_functional_overview/>`__,
        and
        `NI 4072 <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/4072/>`__
        sections for a list of valid values. NI-DMM sets
        :py:data:`nidmm.FREQ\_VOLTAGE\_RANGE` to this value. The minimum
        peak-to-peak signal amplitude that can be detected is 10% of the
        specified **voltage\_range**.

        +-----------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------+
        | Name                                    | Value   | Description                                                                                                                        |
        +=========================================+=========+====================================================================================================================================+
        | NIDMM\_VAL\_AUTO\_RANGE\_ON (default)   | -1.0    | Configures the DMM to take an Auto Range measurement to calculate the voltage range before each frequency or period measurement.   |
        +-----------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_AUTO\_RANGE\_OFF            | -2.0    | Disables Auto Ranging. The driver sets the voltage range to the last calculated voltage range.                                     |
        +-----------------------------------------+---------+------------------------------------------------------------------------------------------------------------------------------------+

    :type voltage_range: ViReal64


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

        +--------------------------+-----+------------------------+------------------------------------------------------------------+
        | Rising Edge              | 0   | NIDMM\_VAL\_POSITIVE   | The driver triggers on the rising edge of the trigger signal.    |
        +--------------------------+-----+------------------------+------------------------------------------------------------------+
        | Falling Edge (default)   | 1   | NIDMM\_VAL\_NEGATIVE   | The driver triggers on the falling edge of the trigger signal.   |
        +--------------------------+-----+------------------------+------------------------------------------------------------------+

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

        +---------------------------------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_AUTO\_RANGE\_ON     | -1.0   | NI-DMM performs an Auto range before acquiring the measurement.                                                                                                                                          |
        +---------------------------------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_AUTO\_RANGE\_OFF    | -2.0   | NI-DMM sets the range to the current :py:data:`nidmm.auto_range_value` and uses this range                                                                                                                 |
        |                                 |        | for all subsequent measurements until the measurement configuration is changed.                                                                                                                          |
        +---------------------------------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_AUTO\_RANGE\_ONCE   | -3.0   | NI-DMM performs an Auto range before acquiring the measurement. The :py:data:`nidmm.auto_range_value` is stored and used for all subsequent measurements until the measurement configuration is changed.   |
        +---------------------------------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


        .. note:: The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
            trigger and sample trigger are set to IMMEDIATE.
    :type range: ViReal64
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
    :type resolution_absolute: ViReal64


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

        +---------------------------------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_AUTO\_RANGE\_ON     | -1.0   | NI-DMM performs an Auto range before acquiring the measurement.                                                                                                                                          |
        +---------------------------------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_AUTO\_RANGE\_OFF    | -2.0   | NI-DMM sets the range to the current :py:data:`nidmm.auto_range_value` and uses this range                                                                                                                 |
        |                                 |        | for all subsequent measurements until the measurement configuration is changed.                                                                                                                          |
        +---------------------------------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | NIDMM\_VAL\_AUTO\_RANGE\_ONCE   | -3.0   | NI-DMM performs an Auto range before acquiring the measurement. The :py:data:`nidmm.auto_range_value` is stored and used for all subsequent measurements until the measurement configuration is changed.   |
        +---------------------------------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


        .. note:: The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
            trigger and sample trigger are set to IMMEDIATE.
    :type range: ViReal64
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
            measurements on the NI 4072. To achieve better resolution for such
            measurements, use the :py:data:`nidmm.LC\_NUMBER\_MEAS\_TO\_AVERAGE`
            attribute.
    :type resolution_digits: ViReal64


.. function:: configure_multi_point(trigger_count, sample_count, sample_trigger, sample_interval)

    Configures the attributes for multipoint measurements. These attributes
    include :py:data:`nidmm.trigger_count`, :py:data:`nidmm.sample_count`,
    :py:data:`nidmm.sample_trigger`, and :py:data:`nidmm.sample_interval`.

    :param trigger_count: 
        Sets the number of triggers you want the DMM to receive before returning
        to the Idle state. The driver sets :py:data:`nidmm.trigger_count` to this
        value. The default value is 1.

    :type trigger_count: ViInt32
    :param sample_count: 
        Sets the number of measurements the DMM makes in each measurement
        sequence initiated by a trigger. The driver sets
        :py:data:`nidmm.sample_count` to this value. The default value is 1.

    :type sample_count: ViInt32
    :param sample_trigger: 
        Specifies the **sample\_trigger** source you want to use. The driver
        sets :py:data:`nidmm.sample_trigger` to this value. The default is
        Immediate.


        .. note:: To determine which values are supported by each device, refer to the
            `LabWindows/CVI Trigger
            Routing <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/cvitrigger_routing/>`__
            section.
    :type sample_trigger: :py:data:`nidmm.SampleTrigger`
    :param sample_interval: 
        Sets the amount of time in seconds the DMM waits between measurement
        cycles. The driver sets :py:data:`nidmm.sample_interval` to this value.
        Specify a sample interval to add settling time between measurement
        cycles or to decrease the measurement rate. **sample\_interval** only
        applies when the **Sample\_Trigger** is set to INTERVAL.

        On the NI 4060, the **sample\_interval** value is used as the settling
        time. When sample interval is set to 0, the DMM does not settle between
        measurement cycles. The NI 4065 and NI 4070/4071/4072 use the value
        specified in **sample\_interval** as additional delay. The default value
        (-1) ensures that the DMM settles for a recommended time. This is the
        same as using an Immediate trigger.


        .. note:: This attribute is not used on the NI 4080/4081/4082 and the NI 4050.
    :type sample_interval: ViReal64


.. function:: configure_offset_comp_ohms(offset_comp_ohms)

    For NI 4080/4081/4082 and NI 4070/4071/4072, allows the DMM to
    compensate for voltage offsets in resistance measurements. When
    **offset_comp_ohms** is enabled, the DMM measures the resistance twice
    (once with the current source on and again with it turned off). Any
    voltage offset present in both measurements is cancelled out.
    **offset_comp_ohms** is useful when measuring resistance values less
    than 10 KΩ.

    :param offset_comp_ohms: 
        Enables or disables **offset\_comp\_ohms**. The driver sets
        :py:data:`nidmm.OFFSET\_COMP\_OHMS` to this value.

        +-------------------------------------------------+---------+------------------------------------------+
        | Name                                            | Value   | Description                              |
        +=================================================+=========+==========================================+
        | NIDMM\_VAL\_OFFSET\_COMP\_OHMS\_OFF (default)   | 0       | Off disables \ **offset\_comp\_ohms**.   |
        +-------------------------------------------------+---------+------------------------------------------+
        | NIDMM\_VAL\_OFFSET\_COMP\_OHMS\_ON              | 1       | On enables **offset\_comp\_ohms**.       |
        +-------------------------------------------------+---------+------------------------------------------+

    :type offset_comp_ohms: :py:data:`nidmm.OffsetCompensatedOhms`


.. function:: configure_open_cable_comp_values(conductance, susceptance)

    For the NI 4082 and NI 4072 only, configures the
    :py:data:`nidmm.OPEN\_CABLE\_COMP\_CONDUCTANCE` and
    :py:data:`nidmm.OPEN\_CABLE\_COMP\_SUSCEPTANCE` attributes.

    :param conductance: 
        Specifies the open cable compensation **conductance**.

    :type conductance: ViReal64
    :param susceptance: 
        Specifies the open cable compensation **susceptance**.

    :type susceptance: ViReal64


.. function:: configure_power_line_frequency(power_line_frequency_hz)

    Specifies the powerline frequency.

    :param power_line_frequency_hz: 
        **Powerline Frequency** specifies the powerline frequency in hertz.
        NI-DMM sets the Powerline Frequency property to this value.

    :type power_line_frequency_hz: ViReal64


.. function:: configure_rtd_custom(rtd_a, rtd_b, rtd_c)

    Configures the A, B, and C parameters for a custom RTD.

    :param rtd_a: 
        Specifies the Callendar-Van Dusen A coefficient for RTD scaling when RTD
        Type parameter is set to Custom in the niDMM\_ConfigureRTDType function.
        The default is 3.9083e-3 (Pt3851)

    :type rtd_a: ViReal64
    :param rtd_b: 
        Specifies the Callendar-Van Dusen B coefficient for RTD scaling when RTD
        Type parameter is set to Custom in the niDMM\_ConfigureRTDType function.
        The default is -5.775e-7 (Pt3851).

    :type rtd_b: ViReal64
    :param rtd_c: 
        Specifies the Callendar-Van Dusen C coefficient for RTD scaling when RTD
        Type parameter is set to Custom in the niDMM\_ConfigureRTDType function.
        The default is -4.183e-12 (Pt3851).

    :type rtd_c: ViReal64


.. function:: configure_rtd_type(rtd_type, rtd_resistance)

    Configures the RTD Type and RTD Resistance parameters for an RTD.

    :param rtd_type: 
        Specifies the type of RTD used to measure the temperature resistance.
        NI-DMM uses this value to set the RTD Type property. The default is
        NIDMM\_VAL\_TEMP\_RTD\_PT3851.
        Enum
        Standards
        Material
        TCR (α)
        Typical R\ :sub:`0` (Ω)
        Callendar-Van Dusen Coefficient
        Notes
        NIDMM\_VAL\_TEMP\_RTD\_PT3851
        IEC-751
        DIN 43760
        BS 1904
        ASTM-E1137
        EN-60751
        Platinum
        .003851
        100 Ω
        1000 Ω
        A = 3.9083 × 10\ :sup:`–3`
        B = –5.775×10:sup:`–7`
        C = –4.183×10:sup:`–12`
        Most common RTDs
        NIDMM\_VAL\_TEMP\_RTD\_PT3750
        Low-cost vendor compliant RTD\*
        Platinum
        .003750
        1000 Ω
        A = 3.81 × 10\ :sup:`–3`
        B = –6.02×10:sup:`–7`
        C = –6.0×10:sup:`–12`
        Low-cost RTD
        NIDMM\_VAL\_TEMP\_RTD\_PT3916
        JISC 1604
        Platinum
        .003916
        100 Ω
        A = 3.9739 × 10\ :sup:`–3`
        B = –5.870×10:sup:`–7`
        C = –4.4 ×10\ :sup:`–12`
        Used in primarily in Japan
        NIDMM\_VAL\_TEMP\_RTD\_PT3920
        US Industrial Standard D-100
        American
        Platinum
        .003920
        100 Ω
        A = 3.9787 × 10\ :sup:`–3`
        B = –5.8686×10:sup:`–7`
        C = –4.167 ×10\ :sup:`–12`
        Low-cost RTD
        NIDMM\_VAL\_TEMP\_RTD\_PT3911
        US Industrial Standard
        American
        Platinum
        .003911
        100 Ω
        A = 3.9692 × 10\ :sup:`–3`
        B = –5.8495×10:sup:`–7`
        C = –4.233 ×10\ :sup:`–12`
        Low-cost RTD
        NIDMM\_VAL\_TEMP\_RTD\_PT3928
        ITS-90
        Platinum
        .003928
        100 Ω
        A = 3.9888 × 10\ :sup:`–3`
        B = –5.915×10:sup:`–7`
        C = –3.85 ×10\ :sup:`–12`
        The definition of temperature
        \*No standard. Check the TCR.

    :type rtd_type: ViInt32
    :param rtd_resistance: 
        Specifies the RTD resistance in ohms at 0 °C. NI-DMM uses this value to
        set the RTD Resistance property. The default is 100 (Ω).

    :type rtd_resistance: ViReal64


.. function:: configure_sample_trigger_slope(sample_trigger_slope)

    Sets the :py:data:`nidmm.SAMPLE\_TRIGGER\_SLOPE` to either rising edge
    (positive) or falling edge (negative) polarity.

    :param sample_trigger_slope: 
        Specifies the polarity of the Trigger signal on which the measurement is
        triggered for values of either NIDMM\_VAL\_POSITIVE or
        NIDMM\_VAL\_NEGATIVE. The driver sets
        :py:data:`nidmm.SAMPLE\_TRIGGER\_SLOPE` to this value.

        +--------------------------+-----+------------------------+------------------------------------------------------------------+
        | Rising Edge              | 0   | NIDMM\_VAL\_POSITIVE   | The driver triggers on the rising edge of the trigger signal.    |
        +--------------------------+-----+------------------------+------------------------------------------------------------------+
        | Falling Edge (default)   | 1   | NIDMM\_VAL\_NEGATIVE   | The driver triggers on the falling edge of the trigger signal.   |
        +--------------------------+-----+------------------------+------------------------------------------------------------------+

    :type sample_trigger_slope: :py:data:`nidmm.Slope`


.. function:: configure_short_cable_comp_values(resistance, reactance)

    For the NI 4082 and NI 4072 only, configures the
    :py:data:`nidmm.SHORT\_CABLE\_COMP\_RESISTANCE` and
    :py:data:`nidmm.SHORT\_CABLE\_COMP\_REACTANCE` attributes.

    :param resistance: 
        Specifies the short cable compensation **resistance**.

    :type resistance: ViReal64
    :param reactance: 
        Specifies the short cable compensation **reactance**.

    :type reactance: ViReal64


.. function:: configure_thermistor_custom(thermistor_a, thermistor_b, thermistor_c)

    Configures the A, B, and C parameters for a custom thermistor.

    :param thermistor_a: 
        Specifies the Steinhart-Hart A coefficient for thermistor scaling when
        Thermistor Type is set to Custom in the niDMM\_ConfigureThermistorType
        function. The default is 1.0295e-3 (44006).

    :type thermistor_a: ViReal64
    :param thermistor_b: 
        Specifies the Steinhart-Hart B coefficient for thermistor scaling when
        Thermistor Type is set to Custom in the niDMM\_ConfigureThermistorType
        function. The default is 2.391e-4 (44006).

    :type thermistor_b: ViReal64
    :param thermistor_c: 
        Specifies the Steinhart-Hart C coefficient for thermistor scaling when
        Thermistor Type is set to Custom in the niDMM\_ConfigureThermistorType
        function. The default is 1.568e-7 (44006).

    :type thermistor_c: ViReal64


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

        +---------------------------+-----------------------+
        | NIDMM\_VAL\_TEMP\_TC\_B   | Thermocouple type B   |
        +---------------------------+-----------------------+
        | NIDMM\_VAL\_TEMP\_TC\_E   | Thermocouple type E   |
        +---------------------------+-----------------------+
        | NIDMM\_VAL\_TEMP\_TC\_J   | Thermocouple type J   |
        +---------------------------+-----------------------+
        | NIDMM\_VAL\_TEMP\_TC\_K   | Thermocouple type K   |
        +---------------------------+-----------------------+
        | NIDMM\_VAL\_TEMP\_TC\_N   | Thermocouple type N   |
        +---------------------------+-----------------------+
        | NIDMM\_VAL\_TEMP\_TC\_R   | Thermocouple type R   |
        +---------------------------+-----------------------+
        | NIDMM\_VAL\_TEMP\_TC\_S   | Thermocouple type S   |
        +---------------------------+-----------------------+
        | NIDMM\_VAL\_TEMP\_TC\_T   | Thermocouple type T   |
        +---------------------------+-----------------------+

    :type thermocouple_type: ViInt32
    :param reference_junction_type: 
        Specifies the type of reference junction to be used in the reference
        junction compensation of a thermocouple measurement. NI-DMM uses this
        value to set the Reference Junction Type property. The only supported
        value is NIDMM\_VAL\_TEMP\_REF\_JUNC\_FIXED.

    :type reference_junction_type: ViInt32


.. function:: configure_transducer_type(transducer_type)

    Configures the transducer type.

    :param transducer_type: 
        Specifies the type of device used to measure the temperature. NI-DMM
        uses this value to set the Transducer Type property. The default is
        NIDMM\_VAL\_THERMOCOUPLE.

        +----------------------------+----------------+
        | NIDMM\_VAL\_2\_WIRE\_RTD   | 2-wire RTD     |
        +----------------------------+----------------+
        | NIDMM\_VAL\_4\_WIRE\_RTD   | 4-wire RTD     |
        +----------------------------+----------------+
        | NIDMM\_VAL\_THERMISTOR     | Thermistor     |
        +----------------------------+----------------+
        | NIDMM\_VAL\_THERMOCOUPLE   | Thermocouple   |
        +----------------------------+----------------+

    :type transducer_type: :py:data:`nidmm.TemperatureTransducerType`


.. function:: configure_trigger(trigger_source, trigger_delay)

    Configures the DMM **trigger_source** and **trigger_delay**. Refer to
    `Triggering <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/trigger/>`__
    and `Using
    Switches <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/switch_selection/>`__
    for more information.

    :param trigger_source: 
        Specifies the **trigger\_source** that initiates the acquisition. The
        driver sets :py:data:`nidmm.trigger_source` to this value. Software
        configures the DMM to wait until niDMM\_SendSoftwareTrigger is called
        before triggering the DMM.


        .. note:: To determine which values are supported by each device, refer to the
            `LabWindows/CVI Trigger
            Routing <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/cvitrigger_routing/>`__
            section.
    :type trigger_source: :py:data:`nidmm.TriggerSource`
    :param trigger_delay: 
        Specifies the time that the DMM waits after it has received a trigger
        before taking a measurement. The driver sets the
        :py:data:`nidmm.trigger_delay` attribute to this value. By default,
        **trigger\_delay** is NIDMM\_VAL\_AUTO\_DELAY (-1), which means the DMM
        waits an appropriate settling time before taking the measurement. On the
        NI 4060, if you set **trigger\_delay** to 0, the DMM does not settle
        before taking the measurement. The NI 4065 and NI 4070/4071/4072 use the
        value specified in **trigger\_delay** as additional settling time.


        .. note:: When using the NI 4050, **Trigger\_Delay** must be set to
            NIDMM\_VAL\_AUTO\_DELAY (-1).
    :type trigger_delay: ViReal64


.. function:: configure_trigger_slope(trigger_slope)

    Sets the :py:data:`nidmm.trigger_slope` attribute to either rising edge
    (positive) or falling edge (negative) polarity.

    :param trigger_slope: 
        Specifies the polarity of the trigger signal on which the measurement is
        triggered for values of either NIDMM\_VAL\_POSITIVE or
        NIDMM\_VAL\_NEGATIVE. The driver sets the :py:data:`nidmm.trigger_slope`
        attribute to this value.

        +----------------------------------+-----+------------------------------------------------------------------+
        | NIDMM\_VAL\_POSITIVE             | 0   | The driver triggers on the rising edge of the trigger signal.    |
        +----------------------------------+-----+------------------------------------------------------------------+
        | NIDMM\_VAL\_NEGATIVE (default)   | 1   | The driver triggers on the falling edge of the trigger signal.   |
        +----------------------------------+-----+------------------------------------------------------------------+

    :type trigger_slope: :py:data:`nidmm.Slope`


.. function:: configure_waveform_acquisition(measurement_function, range, rate, waveform_points)

    Configures the DMM for waveform acquisitions. This feature is supported
    on the NI 4080/4081/4082 and the NI 4070/4071/4072.

    :param measurement_function: 
        Specifies the **measurement\_function** used in a waveform acquisition.
        The driver sets :py:data:`nidmm.function` to this value.

        +-------------------------------------------+--------+--------------------+
        | NIDMM\_VAL\_WAVEFORM\_VOLTAGE (default)   | 1003   | Voltage Waveform   |
        +-------------------------------------------+--------+--------------------+
        | NIDMM\_VAL\_WAVEFORM\_CURRENT             | 1004   | Current Waveform   |
        +-------------------------------------------+--------+--------------------+

    :type measurement_function: :py:data:`nidmm.Function`
    :param range: 
        Specifies the expected maximum amplitude of the input signal and sets
        the **range** for the **Measurement\_Function**. NI-DMM sets
        :py:data:`nidmm.range` to this value. **range** values are coerced up to the
        closest input **range**. The default is 10.0.

        For valid ranges refer to the topics in
        `Devices <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/devices/>`__.

        Auto-ranging is not supported during waveform acquisitions.

    :type range: ViReal64
    :param rate: 
        Specifies the **rate** of the acquisition in samples per second. NI-DMM
        sets :py:data:`nidmm.waveform_rate` to this value.

        The valid **Range** is 10.0–1,800,000 S/s. **rate** values are coerced
        to the closest integer divisor of 1,800,000. The default value is
        1,800,000.

    :type rate: ViReal64
    :param waveform_points: 
        Specifies the number of points to acquire before the waveform
        acquisition completes. NI-DMM sets :py:data:`nidmm.waveform_points` to this
        value.

        To calculate the maximum and minimum number of waveform points that you
        can acquire in one acquisition, refer to the `Waveform Acquisition
        Measurement
        Cycle <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/waveform_cycle/>`__.

        The default value is 500.

    :type waveform_points: ViInt32


.. function:: configure_waveform_coupling(waveform_coupling)

    For the NI 4080/4081/4082 and the NI 4070/4071/4072, configures
    instrument coupling for voltage waveforms.

    :param waveform_coupling: 
        Selects DC or AC coupling. The driver sets
        :py:data:`nidmm.waveform_coupling` to this value.

        +------------------------------------------------+---------+---------------+
        | Name                                           | Value   | Description   |
        +================================================+=========+===============+
        | NIDMM\_VAL\_WAVEFORM\_COUPLING\_AC             | 0       | AC coupling   |
        +------------------------------------------------+---------+---------------+
        | NIDMM\_VAL\_WAVEFORM\_COUPLING\_DC (default)   | 1       | DC coupling   |
        +------------------------------------------------+---------+---------------+

    :type waveform_coupling: :py:data:`nidmm.WaveformCouplingMode`


.. function:: disable()

    Places the instrument in a quiescent state where it has minimal or no
    impact on the system to which it is connected. If a measurement is in
    progress when this function is called, the measurement is aborted.


.. function:: fetch(maximum_time, reading)

    Returns the value from a previously initiated measurement. You must call
    niDMM\_Initiate before calling this function.

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

    :type maximum_time: ViInt32

    :rtype: ViReal64


.. function:: fetch_multi_point(maximum_time, array_size, reading_array, actual_number_of_points)

    Returns an array of values from a previously initiated multipoint
    measurement. The number of measurements the DMM makes is determined by
    the values you specify for the **Trigger\_Count** and **Sample\_Count**
    parameters of niDMM\_ConfigureMultiPoint. You must first call
    niDMM\_Initiate to initiate a measurement before calling this function.

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

    :type maximum_time: ViInt32
    :param array_size: 
        Specifies the number of measurements to acquire. The maximum number of
        measurements for a finite acquisition is the (**Trigger Count** x
        **Sample Count**) parameters in niDMM\_ConfigureMultiPoint.

        For continuous acquisitions, up to 100,000 points can be returned at
        once. The number of measurements can be a subset. The valid range is any
        positive ViInt32. The default value is 1.

    :type array_size: ViInt32

    :rtype: tuple (reading_array, actual_number_of_points)

        WHERE

        reading_array (ViReal64): 
            An array of measurement values.


        .. note:: The size of the **Reading\_Array** must be at least the size that you
            specify for the **Array\_Size** parameter.
        actual_number_of_points (ViInt32): 
            Indicates the number of measured values actually retrieved from the DMM.



.. function:: fetch_waveform(maximum_time, array_size, waveform_array, actual_number_of_points)

    For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of
    values from a previously initiated waveform acquisition. You must call
    niDMM\_Initiate before calling this function.

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

    :type maximum_time: ViInt32
    :param array_size: 
        Specifies the number of waveform points to return. You specify the total
        number of points that the DMM acquires in the **Waveform Points**
        parameter of niDMM\_ConfigureWaveformAcquisition. The default value is
        1.

    :type array_size: ViInt32

    :rtype: tuple (waveform_array, actual_number_of_points)

        WHERE

        waveform_array (ViReal64): 
            **Waveform Array** is an array of measurement values stored in waveform
            data type.

        actual_number_of_points (ViInt32): 
            Indicates the number of measured values actually retrieved from the DMM.



.. function:: format_meas_absolute(measurement_function, range, resolution, measurement, mode_string, range_string, data_string)

    Formats the **measurement** to the proper number of displayed digits
    according to the **measurement\_Function**, **range**, and
    **resolution**. Returns the formatted data, range, and mode strings.

    :param measurement_function: 
        Specifies the **measurement\_function** used to acquire the measurement.
        The driver sets :py:data:`nidmm.function` to this value.

    :type measurement_function: ViInt32
    :param range: 
        Specifies the :py:data:`nidmm.range` used to acquire the **Measurement**.

    :type range: ViReal64
    :param resolution: 
        Specifies the :py:data:`nidmm.RESOLUTION\_ABSOLUTE` of the **Measurement**.

    :type resolution: ViReal64
    :param measurement: 
        Specifies the measured value returned from the DMM.

    :type measurement: ViReal64

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

    Returns the DMM **aperture_time** and **aperture_time\_Units**.

    :rtype: tuple (aperture_time, aperture_time_units)

        WHERE

        aperture_time (ViReal64): 
            Specifies the amount of time the DMM digitizes the input signal for a
            single measurement. This parameter does not include settling time.
            Returns the value of the :py:data:`nidmm.aperture_time` attribute. The
            units of this attribute depend on the value of the
            :py:data:`nidmm.aperture_time_units` attribute.
            On the NI 4070/4071/4072, the minimum aperture time is 8.89 µs, and the
            maximum aperture time is 149 s. Any number of powerline cycles (PLCs)
            within the minimum and maximum ranges is allowed on the
            NI 4070/4071/4072.
            On the NI 4065 the minimum aperture time is 333 µs, and the maximum
            aperture time is 78.2 s. If setting the number of averages directly, the
            total measurement time is aperture time X the number of averages, which
            must be less than 72.8 s. The aperture times allowed are 333 µs, 667 µs,
            or multiples of 1.11 ms—for example 1.11 ms, 2.22 ms, 3.33 ms, and so
            on. If you set an aperture time other than 333 µs, 667 µs, or multiples
            of 1.11 ms, the value will be coerced up to the next supported aperture
            time.
            On the NI 4060, when the powerline frequency is 60, the PLCs allowed are
            1 PLC, 6 PLC, 12 PLC, and 120 PLC. When the powerline frequency is 50,
            the PLCs allowed are 1 PLC, 5 PLC, 10 PLC, and 100 PLC.

        aperture_time_units (enums.ApertureTimeUnits): 
            Indicates the units of aperture time as powerline cycles (PLCs) or
            seconds. Returns the value of the :py:data:`nidmm.aperture_time_units`
            attribute.

            +-----------------------------------+-----+--------------------+
            | NIDMM\_VAL\_SECONDS               | 0   | Seconds            |
            +-----------------------------------+-----+--------------------+
            | NIDMM\_VAL\_POWER\_LINE\_CYCLES   | 1   | Powerline Cycles   |
            +-----------------------------------+-----+--------------------+



.. function:: _get_attribute_vi_boolean(channel_name, attribute_id, attribute_value)

    Queries the value of a ViBoolean attribute. You can use this function to
    get the values of instrument-specific attributes and inherent IVI
    attributes.

    :param channel_name: 
        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

    :type channel_name: ViConstString
    :param attribute_id: 
        Pass the ID of an attribute.

    :type attribute_id: ViAttr

    :rtype: ViBoolean


.. function:: _get_attribute_vi_int32(channel_name, attribute_id, attribute_value)

    Queries the value of a ViInt32 attribute. You can use this function to
    get the values of instrument-specific attributes and inherent IVI
    attributes.

    :param channel_name: 
        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

    :type channel_name: ViConstString
    :param attribute_id: 
        Pass the ID of an attribute.

    :type attribute_id: ViAttr

    :rtype: ViInt32


.. function:: _get_attribute_vi_real64(channel_name, attribute_id, attribute_value)

    Queries the value of a ViReal64 attribute. You can use this function to
    get the values of instrument-specific attributes and inherent IVI
    attributes.

    :param channel_name: 
        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

    :type channel_name: ViConstString
    :param attribute_id: 
        Pass the ID of an attribute.

    :type attribute_id: ViAttr

    :rtype: ViReal64


.. function:: _get_attribute_vi_session(channel_name, attribute_id, attribute_value)

    Queries the value of a ViSession attribute. You can use this function to
    get the values of instrument-specific attributes and inherent IVI
    attributes.

    :param channel_name: 
        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

    :type channel_name: ViConstString
    :param attribute_id: 
        Pass the ID of an attribute.

    :type attribute_id: ViAttr

    :rtype: ViSession


.. function:: _get_attribute_vi_string(channel_name, attribute_id, buffer_size, attribute_value)

    Queries the value of a ViString attribute. You can use this function to
    get the values of instrument-specific attributes and inherent IVI
    attributes.

    :param channel_name: 
        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

    :type channel_name: ViConstString
    :param attribute_id: 
        Pass the ID of an attribute.

    :type attribute_id: ViAttr
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

    :type buffer_size: ViInt32


.. function:: get_auto_range_value(actual_range)

    Returns the **actual_range** that the DMM is using, even when Auto
    Range is off.

    :rtype: ViReal64


.. function:: get_cal_count(cal_type, count)

    Returns the calibration **count** for the specified type of calibration.

    .. note:: The NI 4050, NI 4060, and NI 4080/4081/4082 are not supported.

    :param cal_type: 
        Specifies the type of calibration performed (external or
        self-calibration).


        .. note:: The NI 4065 does not support self-calibration.
    :type cal_type: ViInt32

    :rtype: ViInt32


.. function:: get_cal_date_and_time(cal_type, month, day, year, hour, minute)

    Returns the date and time of the last calibration performed.

    .. note:: The NI 4050 and NI 4060 are not supported.

    :param cal_type: 
        Specifies the type of calibration performed (external or
        self-calibration).


        .. note:: The NI 4065 does not support self-calibration.
    :type cal_type: ViInt32

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

    Returns the **channel_string** that is in the channel table at an
    **index** you specify. Not applicable to National Instruments DMMs.
    Included for compliance with the *IviDmm Class Specification*.

    :param index: 
        A 1–based **index** into the channel table.

    :type index: ViInt32
    :param buffer_size: 
        Passes the number of bytes in the ViChar array you specify for the
        **Channel\_String** parameter. If the next **Channel\_String**,
        including the terminating NULL byte, contains more bytes than you
        indicate in this parameter, the function copies
        **buffer\_size** –1 bytes into the buffer, places an ASCII NULL byte at
        the end of the buffer, and returns the buffer size you must pass to get
        the entire value.

        For example, if the value is "123456" and the **buffer\_size** is 4, the
        function places "123" into the buffer and returns 7. If you pass a
        negative number, the function copies the value to the buffer regardless
        of the number of bytes in the value. If you pass 0, you can pass
        VI\_NULL for the **Channel\_String** buffer parameter. The default value
        is None.

    :type buffer_size: ViInt32

    :rtype: ViChar


.. function:: get_dev_temp(options, temperature)

    Returns the current **temperature** of the device.

    .. note:: The NI 4050 and NI 4060 are not supported.

    :param options: 
        Reserved.

    :type options: ViString

    :rtype: ViReal64


.. function:: _get_error(error_code, buffer_size, description)

    Returns the error information associated with the
    **vi**. This function retrieves and then clears the
    error information for the session. If you leave the
    **vi** unwired, this function retrieves and then clears
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

    :type buffer_size: ViInt32

    :rtype: ViStatus


.. function:: _get_error_message(error_code, buffer_size, error_message)

    Returns the **error_message** as a user-readable string for the
    provided **error_code**. Calling this function with a **Buffer\_Size**
    of 0 returns the size needed for the **error_message**.

    :param error_code: 
        The error code returned from the instrument for which you want to get a
        user-readable string.

    :type error_code: ViStatus
    :param buffer_size: 
        Specifies the number of bytes allocated for the **Error\_Message**
        ViChar array. If the error description that this function returns
        (including terminating NULL byte) is larger than you indicated in
        **buffer\_size**, the error description will be truncated to fit. If you
        pass 0 for **buffer\_size**, the function returns the buffer size needed
        for **Error\_Message**.

    :type buffer_size: ViInt32


.. function:: get_last_cal_temp(cal_type, temperature)

    Returns the **temperature** during the last calibration procedure.

    .. note:: The NI 4050 and NI 4060 are not supported.

    :param cal_type: 
        Specifies the type of calibration performed (external or
        self-calibration).


        .. note:: The NI 4065 does not support self-calibration.
    :type cal_type: ViInt32

    :rtype: ViReal64


.. function:: get_measurement_period(period)

    Returns the measurement **period**, which is the amount of time it takes
    to complete one measurement with the current configuration. Use this
    function right before you begin acquiring data—after you have completely
    configured the measurement and after all configuration functions have
    been called.

    :rtype: ViReal64


.. function:: get_next_coercion_record(buffer_size, coercion_record)

    This function returns the coercion information associated with the IVI
    session, and it retrieves and clears the oldest instance in which NI-DMM
    coerced a value you specified to another value.

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

    :type buffer_size: ViInt32

    :rtype: ViChar


.. function:: get_next_interchange_warning(buffer_size, interchange_warning)

    This function returns the interchangeability warnings associated with
    the IVI session. It retrieves and clears the oldest instance in which
    the class driver recorded an interchangeability warning.
    Interchangeability warnings indicate that using your application with a
    different instrument might cause different behavior.

    :param buffer_size: 
        Passes the number of bytes in the ViChar array you specify for the
        **Interchange\_Warning** parameter. If the next interchangeability
        warning string, including the terminating NULL byte, contains more bytes
        than you indicate in this parameter, the function copies
        **buffer\_size** –1 bytes into the buffer, places an ASCII NULL byte at
        the end of the buffer, and returns the buffer size you must pass to get
        the entire value.

        For example, if the value is "123456" and the **buffer\_size** is 4, the
        function places "123" into the buffer and returns 7. If you pass a
        negative number, the function copies the value to the buffer regardless
        of the number of bytes in the value. If you pass 0, you can pass
        VI\_NULL for the **Interchange\_Warning** buffer parameter. The default
        value is None.

    :type buffer_size: ViInt32


.. function:: get_self_cal_supported(self_cal_supported)

    Returns a Boolean value that expresses whether or not the DMM that you
    are using can perform self-calibration.

    :rtype: ViBoolean


.. function:: _init_with_options(resource_name, id_query, reset_device, option_string)

    This function completes the following tasks:

    :param resource_name: 
        | Contains the **resource\_name** of the device to initialize. The
          **resource\_name** is assigned in Measurement & Automation Explorer
          (MAX). Refer to `Related
          Documentation <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/related_documentation/>`__
          for the *NI Digital Multimeters Getting Started Guide* for more
          information about configuring and testing the DMM in MAX.
        | Valid Syntax:

        -  NI-DAQmx name
        -  DAQ::NI-DAQmx name[::INSTR]
        -  DAQ::Traditional NI-DAQ device number[::INSTR]
        -  IVI logical name

        .. caution::   All IVI names for the **resource\_name**, such as logical
        names or virtual names, are case-sensitive. If you use logical names,
        driver session names, or virtual names in your program, you must make
        sure that the name you use matches the name in the IVI Configuration
        Store file exactly, without any variations in the case of the characters
        in the name.

    :type resource_name: ViString
    :param id_query: 
        Verifies that the device you initialize is one that the driver supports.
        NI-DMM automatically performs this query, so setting this parameter is
        not necessary.
        Defined Values:

        +----------------------+-----+--------------------+
        | VI\_TRUE (default)   | 1   | Perform ID Query   |
        +----------------------+-----+--------------------+
        | VI\_FALSE            | 0   | Skip ID Query      |
        +----------------------+-----+--------------------+

    :type id_query: ViBoolean
    :param reset_device: 
        Specifies whether to reset the instrument during the initialization
        procedure.
        Defined Values:

        +----------------------+-----+----------------+
        | VI\_TRUE (default)   | 1   | Reset Device   |
        +----------------------+-----+----------------+
        | VI\_FALSE            | 0   | Don't Reset    |
        +----------------------+-----+----------------+

    :type reset_device: ViBoolean
    :param option_string: 
        | Sets the initial value of certain attributes for the session. The
          following table specifies the attribute name, attribute constant, and
          default value for each attribute that you can use in this parameter:

        +--------------------+-------------------------------------+---------------------+------+
        | Check              | :py:data:`nidmm.range_check`           | VI\_TRUE            | 1    |
        +--------------------+-------------------------------------+---------------------+------+
        | QueryInstrStatus   | :py:data:`nidmm.QUERY\_INSTR\_STATUS`   | VI\_FALSE           | 0    |
        +--------------------+-------------------------------------+---------------------+------+
        | Cache              | :py:data:`nidmm.cache`                  | VI\_TRUE            | 1    |
        +--------------------+-------------------------------------+---------------------+------+
        | Simulate           | :py:data:`nidmm.simulate`               | VI\_FALSE           | 0    |
        +--------------------+-------------------------------------+---------------------+------+
        | RecordCoercions    | :py:data:`nidmm.RECORD\_COERCIONS`      | VI\_FALSE           | 0    |
        +--------------------+-------------------------------------+---------------------+------+
        | DriverSetup        | :py:data:`nidmm.driver_setup`          | "" (empty string)   | ""   |
        +--------------------+-------------------------------------+---------------------+------+

        The format of this string is, "AttributeName=Value." To set multiple
        attributes, separate their assignments with a comma.

        If you pass NULL or an empty string for this parameter, the session uses
        the default values for the attributes. You can override the default
        values by assigning a value explicitly in an **option\_string**
        parameter. You do not have to specify all of the attributes and may
        leave any of them out (those left out use the default value).

        Refer to `Simulating NI Digital
        Multimeters <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/simulation/>`__
        for more information.

    :type option_string: ViString

    :rtype: ViSession


.. function:: _initiate()

    Initiates an acquisition. After you call this function, the DMM leaves
    the Idle state and enters the Wait-for-Trigger state. If trigger is set
    to Immediate mode, the DMM begins acquiring measurement data. Use
    niDMM\_Fetch, niDMM\_FetchMultiPoint, or niDMM\_FetchWaveform to
    retrieve the measurement data.


.. function:: is_over_range(measurement_value, is_over_range)

    Takes a **measurement_value** and determines if the value is a valid
    measurement or a value indicating that an overrange condition occurred.

    :param measurement_value: 
        The measured value returned from the DMM.


        .. note:: If an overrange condition occurs, the **Measurement\_Value** contains
            an IEEE-defined NaN (Not a Number) value.
    :type measurement_value: ViReal64

    :rtype: ViBoolean


.. function:: is_under_range(measurement_value, is_under_range)

    Takes a **measurement_value** and determines if the value is a valid
    measurement or a value indicating that an underrange condition occurred.

    :param measurement_value: 
        The measured value returned from the DMM.


        .. note:: If an overrange condition occurs, the **Measurement\_Value** contains
            an IEEE-defined NaN (Not a Number) value.
    :type measurement_value: ViReal64

    :rtype: ViBoolean


.. function:: _lock_session(caller_has_lock)

    This function obtains a multithread lock on the instrument session.
    Before it does so, it waits until all other execution threads have
    released their locks on the instrument session.

    :rtype: ViBoolean


.. function:: perform_open_cable_comp(conductance, susceptance)

    For the NI 4082 and NI 4072 only, performs the open cable compensation
    measurements for the current capacitance/inductance range, and returns
    open cable compensation **conductance** and **susceptance** values. You
    can use the return values of this function as inputs to
    niDMM\_ConfigureOpenCableCompValues.

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
    **resistance** and **reactance** values. You can use the return values
    of this function as inputs to niDMM\_ConfigureShortCableCompValues.

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

    :type maximum_time: ViInt32

    :rtype: ViReal64


.. function:: read_multi_point(maximum_time, array_size, reading_array, actual_number_of_points)

    Acquires multiple measurements and returns an array of measured values.
    The number of measurements the DMM makes is determined by the values you
    specify for the **Trigger\_Count** and **Sample\_Count** parameters in
    niDMM\_ConfigureMultiPoint.

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

    :type maximum_time: ViInt32
    :param array_size: 
        Specifies the number of measurements to acquire. The maximum number of
        measurements for a finite acquisition is the (**Trigger Count** x
        **Sample Count**) parameters in niDMM\_ConfigureMultiPoint.

        For continuous acquisitions, up to 100,000 points can be returned at
        once. The number of measurements can be a subset. The valid range is any
        positive ViInt32. The default value is 1.

    :type array_size: ViInt32

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
    niDMM\_Fetch, niDMM\_FetchMultiPoint, or niDMM\_FetchWaveform.

    .. note:: The NI 4050 is not supported.

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

            +-----+------------------------------+
            | 0   | Running                      |
            +-----+------------------------------+
            | 1   | Finished with backlog        |
            +-----+------------------------------+
            | 2   | Finished with no backlog     |
            +-----+------------------------------+
            | 3   | Paused                       |
            +-----+------------------------------+
            | 4   | No acquisition in progress   |
            +-----+------------------------------+



.. function:: read_waveform(maximum_time, array_size, waveform_array, actual_number_of_points)

    For the NI 4080/4081/4082 and the NI 4070/4071/4072, acquires a waveform
    and returns data as an array of values or as a waveform data type. The
    number of elements in the **waveform_array** is determined by the
    values you specify for the **Waveform\_Points** parameter in
    niDMM\_ConfigureWaveformAcquisition.

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

    :type maximum_time: ViInt32
    :param array_size: 
        Specifies the number of waveform points to return. You specify the total
        number of points that the DMM acquires in the **Waveform Points**
        parameter of niDMM\_ConfigureWaveformAcquisition. The default value is
        1.

    :type array_size: ViInt32

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


.. function:: reset_with_defaults()

    Resets the instrument to a known state and sends initialization commands
    to the DMM. The initialization commands set the DMM settings to the
    state necessary for the operation of NI-DMM. All user-defined default
    values associated with a logical name are applied after setting the DMM.


.. function:: self_cal()

    For the NI 4080/4081/4082 and the NI 4070/4071/4072, executes the
    self-calibration routine to maintain measurement accuracy.

    .. note:: This function calls niDMM\_reset, and any configurations previous to
        the call will be lost. All attributes will be set to their default
        values after the call returns.


.. function:: send_software_trigger()

    Sends a command to trigger the DMM. Call this function if you have
    configured either the :py:data:`nidmm.trigger_source` or
    :py:data:`nidmm.sample_trigger` attributes. If the
    :py:data:`nidmm.trigger_source` and/or :py:data:`nidmm.sample_trigger`
    attributes are set to NIDMM\_VAL\_EXTERNAL or NIDMM\_VAL\_TTL\ *n*, you
    can use this function to override the trigger source that you configured
    and trigger the device. The NI 4050 and NI 4060 are not supported.


.. function:: _set_attribute_vi_boolean(channel_name, attribute_id, attribute_value)

    This function sets the value of a ViBoolean attribute.

    :param channel_name: 
        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

    :type channel_name: ViConstString
    :param attribute_id: 
        Pass the ID of an attribute.

    :type attribute_id: ViAttr
    :param attribute_value: 
        Pass the value that you want to set the attribute to.

    :type attribute_value: ViBoolean


.. function:: _set_attribute_vi_int32(channel_name, attribute_id, attribute_value)

    This function sets the value of a ViInt32 attribute.

    :param channel_name: 
        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

    :type channel_name: ViConstString
    :param attribute_id: 
        Pass the ID of an attribute.

    :type attribute_id: ViAttr
    :param attribute_value: 
        Pass the value that you want to set the attribute to.

    :type attribute_value: ViInt32


.. function:: _set_attribute_vi_real64(channel_name, attribute_id, attribute_value)

    This function sets the value of a ViReal64 attribute.

    :param channel_name: 
        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

    :type channel_name: ViConstString
    :param attribute_id: 
        Pass the ID of an attribute.

    :type attribute_id: ViAttr
    :param attribute_value: 
        Pass the value that you want to set the attribute to.

    :type attribute_value: ViReal64


.. function:: _set_attribute_vi_session(channel_name, attribute_id, attribute_value)

    This function sets the value of a ViSession attribute.

    :param channel_name: 
        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

    :type channel_name: ViConstString
    :param attribute_id: 
        Pass the ID of an attribute.

    :type attribute_id: ViAttr
    :param attribute_value: 
        Pass the value that you want to set the attribute to.

    :type attribute_value: ViSession


.. function:: _set_attribute_vi_string(channel_name, attribute_id, attribute_value)

    This function sets the value of a ViString attribute.

    :param channel_name: 
        This parameter is ignored. National Instruments DMMs do not support
        channel names since they only have a single channel. This parameter is
        included in order to support interchangeability and upgradability to
        multiple channel DMMs.

        The default value is " " (an empty string).

    :type channel_name: ViConstString
    :param attribute_id: 
        Pass the ID of an attribute.

    :type attribute_id: ViAttr
    :param attribute_value: 
        Pass the value that you want to set the attribute to.

    :type attribute_value: ViString


.. function:: _unlock_session(caller_has_lock)

    This function releases a lock that you acquired on an instrument session
    using niDMM\_LockSession. Refer to niDMM\_LockSession for additional
    information on session locks.

    :rtype: ViBoolean


.. function:: _close()

    Closes the specified session and deallocates resources that it reserved.


.. function:: error_message(error_code, error_message)

    Takes the **error_code** returned by the instrument driver functions,
    interprets it, and returns it as a user-readable string.

    :param error_code: 
        The **error\_code** returned from the instrument. The default is 0,
        indicating VI\_SUCCESS.

    :type error_code: ViStatus

    :rtype: ViChar


.. function:: error_query(error_code, error_message)

    Reads an **error_code** and message from the DMM error queue. National
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

    .. note:: This function calls niDMM\_reset, and any configurations previous to
        the call will be lost. All attributes will be set to their default
        values after the call returns.

    :rtype: tuple (self_test_result, self_test_message)

        WHERE

        self_test_result (ViInt16): 
            Contains the value returned from the instrument self-test. Zero
            indicates success.

            On the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that
            you should check the fuse and replace it, if necessary.


        .. note:: Self-test does not check the fuse on the NI 4065, NI 4071, and
            NI 4081. Hence, even if the fuse is blown on the device, self-test does
            not return error code 1013.
        self_test_message (ViChar): 
            This parameter contains the string returned from the instrument
            self-test. The array must contain at least 256 elements.

            For the NI 4050 and NI 4060, the error codes returned for self-test
            failures include the following:

            -  NIDMM\_ERROR\_AC\_TEST\_FAILURE
            -  NIDMM\_ERROR\_DC\_TEST\_FAILURE
            -  NIDMM\_ERROR\_RESISTANCE\_TEST\_FAILURE

            These error codes indicate that the DMM should be repaired.

            For the NI 4080/4081/4082 and the NI 4070/4071/4072, the error code
            returned for a self-test failure is NIDMM\_ERROR\_SELF\_TEST\_FAILURE.
            This error code indicates that the DMM should be repaired.



