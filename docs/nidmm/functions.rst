nidmm.Session methods
=====================

.. py:currentmodule:: nidmm.Session

.. py:method:: abort()

    Aborts a previously initiated measurement and returns the DMM to the
    Idle state.

    



.. py:method:: configure_ac_bandwidth(ac_minimum_frequency_hz, ac_maximum_frequency_hz)

    Configures the :py:data:`nidmm.Session.ac_min_freq` and :py:data:`nidmm.Session.ac_max_freq`
    properties, which the DMM uses for AC measurements.

    



    :param ac_minimum_frequency_hz:


        Specifies the minimum expected frequency component of the input signal
        in hertz. This parameter affects the DMM only when you set the
        :py:data:`nidmm.Session.method` property to AC measurements. NI-DMM uses this
        parameter to calculate the proper aperture for the measurement.
        The driver sets the :py:data:`nidmm.Session.ac_min_freq` property to this value.
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
        :py:data:`nidmm.Session.method` property to AC measurements. The driver sets the
        :py:data:`nidmm.Session.ac_max_freq` property to this value. The valid range is 1
        Hz–300 kHz for the NI 4080/4081/4082 and the NI 4070/4071/4072, 10
        Hz–100 Hz for the NI 4065, and 20 Hz–25 kHz for the NI 4050 and NI 4060.

        


    :type ac_maximum_frequency_hz: float

.. py:method:: configure_measurement_absolute(measurement_function, range, resolution_absolute)

    Configures the common properties of the measurement. These properties
    include :py:data:`nidmm.Session.method`, :py:data:`nidmm.Session.range`, and
    :py:data:`nidmm.Session.resolution_absolute`.

    



    :param measurement_function:


        Specifies the **measurement_function** used to acquire the measurement.
        The driver sets :py:data:`nidmm.Session.method` to this value.

        


    :type measurement_function: :py:data:`nidmm.Function`
    :param range:


        Specifies the **range** for the method specified in the
        **Measurement_Function** parameter. When frequency is specified in the
        **Measurement_Function** parameter, you must supply the minimum
        frequency expected in the **range** parameter. For example, you must
        type in 100 Hz if you are measuring 101 Hz or higher.
        For all other methods, you must supply a **range** that exceeds the
        value that you are measuring. For example, you must type in 10 V if you
        are measuring 9 V. **range** values are coerced up to the closest input
        **range**. Refer to the `Devices
        Overview <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/devices/>`__ for a list of valid
        ranges. The driver sets :py:data:`nidmm.Session.range` to this value. The default is
        0.02 V.

        +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ON`   | -1.0 | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                                                  |
        +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_OFF`  | -2.0 | NI-DMM sets the Range to the current :py:data:`nidmm.Session.auto_range_value` and uses this range for all subsequent measurements until the measurement configuration is changed.                               |
        +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ONCE` | -3.0 | NI-DMM performs an Auto Range before acquiring the measurement. The :py:data:`nidmm.Session.auto_range_value` is stored and used for all subsequent measurements until the measurement configuration is changed. |
        +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
            trigger and sample trigger are set to IMMEDIATE.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type range: float
    :param resolution_absolute:


        Specifies the absolute resolution for the measurement. NI-DMM sets
        :py:data:`nidmm.Session.resolution_absolute` to this value. This parameter is
        ignored when the **Range** parameter is set to
        :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ON` (-1.0) or :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ONCE`
        (-3.0). The default is 0.001 V.

        

        .. note:: NI-DMM ignores this parameter for capacitance and inductance
            measurements on the NI 4072. To achieve better resolution for such
            measurements, use the :py:data:`nidmm.Session.lc_number_meas_to_average`
            property.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type resolution_absolute: float

.. py:method:: configure_measurement_digits(measurement_function, range, resolution_digits)

    Configures the common properties of the measurement. These properties
    include :py:data:`nidmm.Session.method`, :py:data:`nidmm.Session.range`, and
    :py:data:`nidmm.Session.resolution_digits`.

    



    :param measurement_function:


        Specifies the **measurement_function** used to acquire the measurement.
        The driver sets :py:data:`nidmm.Session.method` to this value.

        


    :type measurement_function: :py:data:`nidmm.Function`
    :param range:


        Specifies the range for the method specified in the
        **Measurement_Function** parameter. When frequency is specified in the
        **Measurement_Function** parameter, you must supply the minimum
        frequency expected in the **range** parameter. For example, you must
        type in 100 Hz if you are measuring 101 Hz or higher.
        For all other methods, you must supply a range that exceeds the value
        that you are measuring. For example, you must type in 10 V if you are
        measuring 9 V. range values are coerced up to the closest input range.
        Refer to the `Devices
        Overview <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/devices/>`__ for a list of valid
        ranges. The driver sets :py:data:`nidmm.Session.range` to this value. The default is
        0.02 V.

        +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ON`   | -1.0 | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                                                  |
        +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_OFF`  | -2.0 | NI-DMM sets the Range to the current :py:data:`nidmm.Session.auto_range_value` and uses this range for all subsequent measurements until the measurement configuration is changed.                               |
        +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
        | :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ONCE` | -3.0 | NI-DMM performs an Auto Range before acquiring the measurement. The :py:data:`nidmm.Session.auto_range_value` is stored and used for all subsequent measurements until the measurement configuration is changed. |
        +---------------------------------------------+------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

        .. note:: The NI 4050, NI 4060, and NI 4065 only support Auto Range when the
            trigger and sample trigger are set to IMMEDIATE.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type range: float
    :param resolution_digits:


        Specifies the resolution of the measurement in digits. The driver sets
        the `Devices Overview <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/devices/>`__ for a
        list of valid ranges. The driver sets :py:data:`nidmm.Session.resolution_digits`
        property to this value. This parameter is ignored when the **Range**
        parameter is set to :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ON` (-1.0) or
        :py:data:`~nidmm.NIDMM_VAL_AUTO_RANGE_ONCE` (-3.0). The default is 5½.

        

        .. note:: NI-DMM ignores this parameter for capacitance and inductance
            measurements on the NI 4072. To achieve better resolution for such
            measurements, use the :py:data:`nidmm.Session.lc_number_meas_to_average`
            property.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type resolution_digits: float

.. py:method:: configure_multi_point(trigger_count, sample_count, sample_trigger=nidmm.SampleTrigger.IMMEDIATE, sample_interval=datetime.timedelta(seconds=-1))

    Configures the properties for multipoint measurements. These properties
    include :py:data:`nidmm.Session.trigger_count`, :py:data:`nidmm.Session.sample_count`,
    :py:data:`nidmm.Session.sample_trigger`, and :py:data:`nidmm.Session.sample_interval`.

    For continuous acquisitions, set :py:data:`nidmm.Session.trigger_count` or
    :py:data:`nidmm.Session.sample_count` to zero. For more information, refer to
    `Multiple Point
    Acquisitions <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/multi_point/>`__,
    `Triggering <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/trigger/>`__, and `Using
    Switches <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/switch_selection/>`__.

    



    :param trigger_count:


        Sets the number of triggers you want the DMM to receive before returning
        to the Idle state. The driver sets :py:data:`nidmm.Session.trigger_count` to this
        value. The default value is 1.

        


    :type trigger_count: int
    :param sample_count:


        Sets the number of measurements the DMM makes in each measurement
        sequence initiated by a trigger. The driver sets
        :py:data:`nidmm.Session.sample_count` to this value. The default value is 1.

        


    :type sample_count: int
    :param sample_trigger:


        Specifies the **sample_trigger** source you want to use. The driver
        sets :py:data:`nidmm.Session.sample_trigger` to this value. The default is
        Immediate.

        

        .. note:: To determine which values are supported by each device, refer to the
            `LabWindows/CVI Trigger
            Routing <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/cvitrigger_routing/>`__ section.


    :type sample_trigger: :py:data:`nidmm.SampleTrigger`
    :param sample_interval:


        Sets the amount of time in seconds the DMM waits between measurement
        cycles. The driver sets :py:data:`nidmm.Session.sample_interval` to this value.
        Specify a sample interval to add settling time between measurement
        cycles or to decrease the measurement rate. **sample_interval** only
        applies when the **Sample_Trigger** is set to INTERVAL.

        On the NI 4060, the **sample_interval** value is used as the settling
        time. When sample interval is set to 0, the DMM does not settle between
        measurement cycles. The NI 4065 and NI 4070/4071/4072 use the value
        specified in **sample_interval** as additional delay. The default value
        (-1) ensures that the DMM settles for a recommended time. This is the
        same as using an Immediate trigger.

        

        .. note:: This property is not used on the NI 4080/4081/4082 and the NI 4050.


    :type sample_interval: float

.. py:method:: configure_open_cable_comp_values(conductance, susceptance)

    For the NI 4082 and NI 4072 only, configures the
    :py:data:`nidmm.Session.open_cable_comp_conductance` and
    :py:data:`nidmm.Session.open_cable_comp_susceptance` properties.

    



    :param conductance:


        Specifies the open cable compensation **conductance**.

        


    :type conductance: float
    :param susceptance:


        Specifies the open cable compensation **susceptance**.

        


    :type susceptance: float

.. py:method:: configure_power_line_frequency(power_line_frequency_hz)

    Specifies the powerline frequency.

    



    :param power_line_frequency_hz:


        **Powerline Frequency** specifies the powerline frequency in hertz.
        NI-DMM sets the Powerline Frequency property to this value.

        


    :type power_line_frequency_hz: float

.. py:method:: configure_rtd_custom(rtd_a, rtd_b, rtd_c)

    Configures the A, B, and C parameters for a custom RTD.

    



    :param rtd_a:


        Specifies the Callendar-Van Dusen A coefficient for RTD scaling when RTD
        Type parameter is set to Custom in the :py:meth:`nidmm.Session.configure_rtd_type` method.
        The default is 3.9083e-3 (Pt3851)

        


    :type rtd_a: float
    :param rtd_b:


        Specifies the Callendar-Van Dusen B coefficient for RTD scaling when RTD
        Type parameter is set to Custom in the :py:meth:`nidmm.Session.configure_rtd_type` method.
        The default is -5.775e-7 (Pt3851).

        


    :type rtd_b: float
    :param rtd_c:


        Specifies the Callendar-Van Dusen C coefficient for RTD scaling when RTD
        Type parameter is set to Custom in the :py:meth:`nidmm.Session.configure_rtd_type` method.
        The default is -4.183e-12 (Pt3851).

        


    :type rtd_c: float

.. py:method:: configure_rtd_type(rtd_type, rtd_resistance)

    Configures the RTD Type and RTD Resistance parameters for an RTD.

    



    :param rtd_type:


        Specifies the type of RTD used to measure the temperature resistance.
        NI-DMM uses this value to set the RTD Type property. The default is
        :py:data:`~nidmm.RTDType.PT3851`.

        +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
        | Enum                             | Standards                                     | Material | TCR (α) | Typical R\ :sub:`0` (Ω) | Notes                                                                         |                               |
        +==================================+===============================================+==========+=========+=========================+===============================================================================+===============================+
        | Callendar-Van Dusen Coefficient  |                                               |          |         |                         |                                                                               |                               |
        +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
        | :py:data:`~nidmm.RTDType.PT3851` | IEC-751 DIN 43760 BS 1904 ASTM-E1137 EN-60751 | Platinum | .003851 | 100 Ω 1000 Ω            | A = 3.9083 × 10\ :sup:`–3` B = –5.775×10:sup:`–7` C = –4.183×10:sup:`–12`     | Most common RTDs              |
        +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
        | :py:data:`~nidmm.RTDType.PT3750` | Low-cost vendor compliant RTD\*               | Platinum | .003750 | 1000 Ω                  | A = 3.81 × 10\ :sup:`–3` B = –6.02×10:sup:`–7` C = –6.0×10:sup:`–12`          | Low-cost RTD                  |
        +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
        | :py:data:`~nidmm.RTDType.PT3916` | JISC 1604                                     | Platinum | .003916 | 100 Ω                   | A = 3.9739 × 10\ :sup:`–3` B = –5.870×10:sup:`–7` C = –4.4 ×10\ :sup:`–12`    | Used in primarily in Japan    |
        +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
        | :py:data:`~nidmm.RTDType.PT3920` | US Industrial Standard D-100 American         | Platinum | .003920 | 100 Ω                   | A = 3.9787 × 10\ :sup:`–3` B = –5.8686×10:sup:`–7` C = –4.167 ×10\ :sup:`–12` | Low-cost RTD                  |
        +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
        | :py:data:`~nidmm.RTDType.PT3911` | US Industrial Standard American               | Platinum | .003911 | 100 Ω                   | A = 3.9692 × 10\ :sup:`–3` B = –5.8495×10:sup:`–7` C = –4.233 ×10\ :sup:`–12` | Low-cost RTD                  |
        +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
        | :py:data:`~nidmm.RTDType.PT3928` | ITS-90                                        | Platinum | .003928 | 100 Ω                   | A = 3.9888 × 10\ :sup:`–3` B = –5.915×10:sup:`–7` C = –3.85 ×10\ :sup:`–12`   | The definition of temperature |
        +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+
        | \*No standard. Check the TCR.    |                                               |          |         |                         |                                                                               |                               |
        +----------------------------------+-----------------------------------------------+----------+---------+-------------------------+-------------------------------------------------------------------------------+-------------------------------+


    :type rtd_type: :py:data:`nidmm.RTDType`
    :param rtd_resistance:


        Specifies the RTD resistance in ohms at 0 °C. NI-DMM uses this value to
        set the RTD Resistance property. The default is 100 (Ω).

        


    :type rtd_resistance: float

.. py:method:: configure_short_cable_comp_values(resistance, reactance)

    For the NI 4082 and NI 4072 only, configures the
    :py:data:`nidmm.Session.short_cable_comp_resistance` and
    :py:data:`nidmm.Session.short_cable_comp_reactance` properties.

    



    :param resistance:


        Specifies the short cable compensation **resistance**.

        


    :type resistance: float
    :param reactance:


        Specifies the short cable compensation **reactance**.

        


    :type reactance: float

.. py:method:: configure_thermistor_custom(thermistor_a, thermistor_b, thermistor_c)

    Configures the A, B, and C parameters for a custom thermistor.

    



    :param thermistor_a:


        Specifies the Steinhart-Hart A coefficient for thermistor scaling when
        Thermistor Type is set to Custom in the :py:meth:`nidmm.Session.ConfigureThermistorType`
        method. The default is 1.0295e-3 (44006).

        

        .. note:: One or more of the referenced methods are not in the Python API for this driver.


    :type thermistor_a: float
    :param thermistor_b:


        Specifies the Steinhart-Hart B coefficient for thermistor scaling when
        Thermistor Type is set to Custom in the :py:meth:`nidmm.Session.ConfigureThermistorType`
        method. The default is 2.391e-4 (44006).

        

        .. note:: One or more of the referenced methods are not in the Python API for this driver.


    :type thermistor_b: float
    :param thermistor_c:


        Specifies the Steinhart-Hart C coefficient for thermistor scaling when
        Thermistor Type is set to Custom in the :py:meth:`nidmm.Session.ConfigureThermistorType`
        method. The default is 1.568e-7 (44006).

        

        .. note:: One or more of the referenced methods are not in the Python API for this driver.


    :type thermistor_c: float

.. py:method:: configure_thermocouple(thermocouple_type, reference_junction_type=nidmm.ThermocoupleReferenceJunctionType.FIXED)

    Configures the thermocouple type and reference junction type for a
    chosen thermocouple.

    



    :param thermocouple_type:


        Specifies the type of thermocouple used to measure the temperature.
        NI-DMM uses this value to set the Thermocouple Type property. The
        default is :py:data:`~nidmm.ThermocoupleType.J`.

        +--------------------------------------+---------------------+
        | :py:data:`~nidmm.ThermocoupleType.B` | Thermocouple type B |
        +--------------------------------------+---------------------+
        | :py:data:`~nidmm.ThermocoupleType.E` | Thermocouple type E |
        +--------------------------------------+---------------------+
        | :py:data:`~nidmm.ThermocoupleType.J` | Thermocouple type J |
        +--------------------------------------+---------------------+
        | :py:data:`~nidmm.ThermocoupleType.K` | Thermocouple type K |
        +--------------------------------------+---------------------+
        | :py:data:`~nidmm.ThermocoupleType.N` | Thermocouple type N |
        +--------------------------------------+---------------------+
        | :py:data:`~nidmm.ThermocoupleType.R` | Thermocouple type R |
        +--------------------------------------+---------------------+
        | :py:data:`~nidmm.ThermocoupleType.S` | Thermocouple type S |
        +--------------------------------------+---------------------+
        | :py:data:`~nidmm.ThermocoupleType.T` | Thermocouple type T |
        +--------------------------------------+---------------------+


    :type thermocouple_type: :py:data:`nidmm.ThermocoupleType`
    :param reference_junction_type:


        Specifies the type of reference junction to be used in the reference
        junction compensation of a thermocouple measurement. NI-DMM uses this
        value to set the Reference Junction Type property. The only supported
        value is :py:data:`~nidmm.NIDMM_VAL_TEMP_REF_JUNC_FIXED`.

        

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type reference_junction_type: :py:data:`nidmm.ThermocoupleReferenceJunctionType`

.. py:method:: configure_trigger(trigger_source, trigger_delay=datetime.timedelta(seconds=-1))

    Configures the DMM **Trigger_Source** and **Trigger_Delay**. Refer to
    `Triggering <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/trigger/>`__ and `Using
    Switches <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/switch_selection/>`__ for more
    information.

    



    :param trigger_source:


        Specifies the **trigger_source** that initiates the acquisition. The
        driver sets :py:data:`nidmm.Session.trigger_source` to this value. Software
        configures the DMM to wait until :py:meth:`nidmm.Session.send_software_trigger` is called
        before triggering the DMM.

        

        .. note:: To determine which values are supported by each device, refer to the
            `LabWindows/CVI Trigger
            Routing <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/cvitrigger_routing/>`__ section.


    :type trigger_source: :py:data:`nidmm.TriggerSource`
    :param trigger_delay:


        Specifies the time that the DMM waits after it has received a trigger
        before taking a measurement. The driver sets the
        :py:data:`nidmm.Session.trigger_delay` property to this value. By default,
        **trigger_delay** is :py:data:`~nidmm.NIDMM_VAL_AUTO_DELAY` (-1), which means the DMM
        waits an appropriate settling time before taking the measurement. On the
        NI 4060, if you set **trigger_delay** to 0, the DMM does not settle
        before taking the measurement. The NI 4065 and NI 4070/4071/4072 use the
        value specified in **trigger_delay** as additional settling time.

        

        .. note:: When using the NI 4050, **Trigger_Delay** must be set to
            :py:data:`~nidmm.NIDMM_VAL_AUTO_DELAY` (-1).

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type trigger_delay: float

.. py:method:: configure_waveform_acquisition(measurement_function, range, rate, waveform_points)

    Configures the DMM for waveform acquisitions. This feature is supported
    on the NI 4080/4081/4082 and the NI 4070/4071/4072.

    



    :param measurement_function:


        Specifies the **measurement_function** used in a waveform acquisition.
        The driver sets :py:data:`nidmm.Session.method` to this value.

        +-----------------------------------------------------+------+------------------+
        | :py:data:`~nidmm.Method.WAVEFORM_VOLTAGE` (default) | 1003 | Voltage Waveform |
        +-----------------------------------------------------+------+------------------+
        | :py:data:`~nidmm.Method.WAVEFORM_CURRENT`           | 1004 | Current Waveform |
        +-----------------------------------------------------+------+------------------+


    :type measurement_function: :py:data:`nidmm.Function`
    :param range:


        Specifies the expected maximum amplitude of the input signal and sets
        the **range** for the **Measurement_Function**. NI-DMM sets
        :py:data:`nidmm.Session.range` to this value. **range** values are coerced up to the
        closest input **range**. The default is 10.0.

        For valid ranges refer to the topics in
        `Devices <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/devices/>`__.

        Auto-ranging is not supported during waveform acquisitions.

        


    :type range: float
    :param rate:


        Specifies the **rate** of the acquisition in samples per second. NI-DMM
        sets :py:data:`nidmm.Session.waveform_rate` to this value.

        The valid **Range** is 10.0–1,800,000 S/s. **rate** values are coerced
        to the closest integer divisor of 1,800,000. The default value is
        1,800,000.

        


    :type rate: float
    :param waveform_points:


        Specifies the number of points to acquire before the waveform
        acquisition completes. NI-DMM sets :py:data:`nidmm.Session.waveform_points` to this
        value.

        To calculate the maximum and minimum number of waveform points that you
        can acquire in one acquisition, refer to the `Waveform Acquisition
        Measurement Cycle <http://zone.ni.com/reference/en-XX/help/370384T-01/dmm/waveform_cycle/>`__.

        The default value is 500.

        


    :type waveform_points: int

.. py:method:: disable()

    Places the instrument in a quiescent state where it has minimal or no
    impact on the system to which it is connected. If a measurement is in
    progress when this method is called, the measurement is aborted.

    



.. py:method:: fetch(maximum_time=datetime.timedelta(milliseconds=-1))

    Returns the value from a previously initiated measurement. You must call
    :py:meth:`nidmm.Session._initiate` before calling this method.

    



    :param maximum_time:


        Specifies the **maximum_time** allowed for this method to complete in
        milliseconds. If the method does not complete within this time
        interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
        error code. This may happen if an external trigger has not been
        received, or if the specified timeout is not long enough for the
        acquisition to complete.

        The valid range is 0–86400000. The default value is
        :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
        automatically.

        

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type maximum_time: int

    :rtype: float
    :return:


            The measured value returned from the DMM.

            



.. py:method:: fetch_multi_point(array_size, maximum_time=datetime.timedelta(milliseconds=-1))

    Returns an array of values from a previously initiated multipoint
    measurement. The number of measurements the DMM makes is determined by
    the values you specify for the **Trigger_Count** and **Sample_Count**
    parameters of :py:meth:`nidmm.Session.configure_multi_point`. You must first call
    :py:meth:`nidmm.Session._initiate` to initiate a measurement before calling this method.

    



    :param array_size:


        Specifies the number of measurements to acquire. The maximum number of
        measurements for a finite acquisition is the (**Trigger Count** x
        **Sample Count**) parameters in :py:meth:`nidmm.Session.configure_multi_point`.

        For continuous acquisitions, up to 100,000 points can be returned at
        once. The number of measurements can be a subset. The valid range is any
        positive ViInt32. The default value is 1.

        


    :type array_size: int
    :param maximum_time:


        Specifies the **maximum_time** allowed for this method to complete in
        milliseconds. If the method does not complete within this time
        interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
        error code. This may happen if an external trigger has not been
        received, or if the specified timeout is not long enough for the
        acquisition to complete.

        The valid range is 0–86400000. The default value is
        :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
        automatically.

        

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type maximum_time: int

    :rtype: tuple (reading_array, actual_number_of_points)

        WHERE

        reading_array (array.array("d")): 


            An array of measurement values.

            

            .. note:: The size of the **Reading_Array** must be at least the size that you
                specify for the **Array_Size** parameter.


        actual_number_of_points (int): 


            Indicates the number of measured values actually retrieved from the DMM.

            



.. py:method:: fetch_waveform(array_size, maximum_time=datetime.timedelta(milliseconds=-1))

    For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of
    values from a previously initiated waveform acquisition. You must call
    :py:meth:`nidmm.Session._initiate` before calling this method.

    



    :param array_size:


        Specifies the number of waveform points to return. You specify the total
        number of points that the DMM acquires in the **Waveform Points**
        parameter of :py:meth:`nidmm.Session.configure_waveform_acquisition`. The default value is
        1.

        


    :type array_size: int
    :param maximum_time:


        Specifies the **maximum_time** allowed for this method to complete in
        milliseconds. If the method does not complete within this time
        interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
        error code. This may happen if an external trigger has not been
        received, or if the specified timeout is not long enough for the
        acquisition to complete.

        The valid range is 0–86400000. The default value is
        :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
        automatically.

        

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type maximum_time: int

    :rtype: tuple (waveform_array, actual_number_of_points)

        WHERE

        waveform_array (array.array("d")): 


            **Waveform Array** is an array of measurement values stored in waveform
            data type.

            


        actual_number_of_points (int): 


            Indicates the number of measured values actually retrieved from the DMM.

            



.. py:method:: fetch_waveform_into(array_size, maximum_time=datetime.timedelta(milliseconds=-1))

    For the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of
    values from a previously initiated waveform acquisition. You must call
    :py:meth:`nidmm.Session._initiate` before calling this method.

    



    :param waveform_array:


        **Waveform Array** is an array of measurement values stored in waveform
        data type.

        


    :type waveform_array: numpy.array(dtype=numpy.float64)
    :param maximum_time:


        Specifies the **maximum_time** allowed for this method to complete in
        milliseconds. If the method does not complete within this time
        interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
        error code. This may happen if an external trigger has not been
        received, or if the specified timeout is not long enough for the
        acquisition to complete.

        The valid range is 0–86400000. The default value is
        :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
        automatically.

        

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type maximum_time: int

    :rtype: tuple (waveform_array, actual_number_of_points)

        WHERE

        waveform_array (numpy.array(dtype=numpy.float64)): 


            **Waveform Array** is an array of measurement values stored in waveform
            data type.

            


        actual_number_of_points (int): 


            Indicates the number of measured values actually retrieved from the DMM.

            



.. py:method:: get_aperture_time_info()

    Returns the DMM **Aperture_Time** and **Aperture_Time_Units**.

    



    :rtype: tuple (aperture_time, aperture_time_units)

        WHERE

        aperture_time (float): 


            Specifies the amount of time the DMM digitizes the input signal for a
            single measurement. This parameter does not include settling time.
            Returns the value of the :py:data:`nidmm.Session.aperture_time` property. The
            units of this property depend on the value of the
            :py:data:`nidmm.Session.aperture_time_units` property.
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
            seconds. Returns the value of the :py:data:`nidmm.Session.aperture_time_units`
            property.

            +-------------------------------------------------------+---+------------------+
            | :py:data:`~nidmm.ApertureTimeUnits.SECONDS`           | 0 | Seconds          |
            +-------------------------------------------------------+---+------------------+
            | :py:data:`~nidmm.ApertureTimeUnits.POWER_LINE_CYCLES` | 1 | Powerline Cycles |
            +-------------------------------------------------------+---+------------------+



.. py:method:: get_auto_range_value()

    Returns the **Actual_Range** that the DMM is using, even when Auto
    Range is off.

    



    :rtype: float
    :return:


            Indicates the **actual_range** the DMM is using. Returns the value of
            the :py:data:`nidmm.Session.auto_range_value` property. The units of the returned
            value depend on the method.

            



.. py:method:: get_cal_date_and_time(cal_type)

    Returns the date and time of the last calibration performed.

    

    .. note:: The NI 4050 and NI 4060 are not supported.



    :param cal_type:


        Specifies the type of calibration performed (external or self-calibration).

        +-----------------------------------------------------+---+----------------------+
        | :py:data:`~nidmm.NIDMM_VAL_INTERNAL_AREA` (default) | 0 | Self-Calibration     |
        +-----------------------------------------------------+---+----------------------+
        | :py:data:`~nidmm.NIDMM_VAL_EXTERNAL_AREA`           | 1 | External Calibration |
        +-----------------------------------------------------+---+----------------------+

        .. note:: The NI 4065 does not support self-calibration.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type cal_type: int

    :rtype: datetime.datetime
    :return:


            Indicates date and time of the last calibration.

            



.. py:method:: get_dev_temp(options="")

    Returns the current **Temperature** of the device.

    

    .. note:: The NI 4050 and NI 4060 are not supported.



    :param options:


        Reserved.

        


    :type options: str

    :rtype: float
    :return:


            Returns the current **temperature** of the device.

            



.. py:method:: get_ext_cal_recommended_interval()

    Returns the recommended interval between external recalibration in
    **Months**.

    

    .. note:: The NI 4050 and NI 4060 are not supported.



    :rtype: int
    :return:


            Returns the recommended number of **months** between external
            calibrations.

            



.. py:method:: get_last_cal_temp(cal_type)

    Returns the **Temperature** during the last calibration procedure.

    

    .. note:: The NI 4050 and NI 4060 are not supported.



    :param cal_type:


        Specifies the type of calibration performed (external or
        self-calibration).

        +-----------------------------------------------------+---+----------------------+
        | :py:data:`~nidmm.NIDMM_VAL_INTERNAL_AREA` (default) | 0 | Self-Calibration     |
        +-----------------------------------------------------+---+----------------------+
        | :py:data:`~nidmm.NIDMM_VAL_EXTERNAL_AREA`           | 1 | External Calibration |
        +-----------------------------------------------------+---+----------------------+

        .. note:: The NI 4065 does not support self-calibration.

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type cal_type: int

    :rtype: float
    :return:


            Returns the **temperature** during the last calibration.

            



.. py:method:: get_measurement_period()

    Returns the measurement **Period**, which is the amount of time it takes
    to complete one measurement with the current configuration. Use this
    method right before you begin acquiring data—after you have completely
    configured the measurement and after all configuration methods have
    been called.

    



    :rtype: float
    :return:


            Returns the number of seconds it takes to make one measurement.

            The first measurement in a multipoint acquisition requires additional
            settling time. This method does not include this additional time or
            any :py:data:`nidmm.Session.trigger_delay` associated with the first measurement.
            Time required for internal measurements, such as
            :py:data:`nidmm.Session.auto_zero`, is included.

            



.. py:method:: get_self_cal_supported()

    Returns a Boolean value that expresses whether or not the DMM that you
    are using can perform self-calibration.

    



    :rtype: bool
    :return:


            Returns whether Self Cal is supported for the device specified by the
            given session.

            +-------+---+-------------------------------------------------------------+
            | True  | 1 | The DMM that you are using can perform self-calibration.    |
            +-------+---+-------------------------------------------------------------+
            | False | 0 | The DMM that you are using cannot perform self-calibration. |
            +-------+---+-------------------------------------------------------------+



.. py:method:: perform_open_cable_comp()

    For the NI 4082 and NI 4072 only, performs the open cable compensation
    measurements for the current capacitance/inductance range, and returns
    open cable compensation **Conductance** and **Susceptance** values. You
    can use the return values of this method as inputs to
    :py:meth:`nidmm.Session.configure_open_cable_comp_values`.

    This method returns an error if the value of the :py:data:`nidmm.Session.method`
    property is not set to :py:data:`~nidmm.Method.CAPACITANCE` (1005) or
    :py:data:`~nidmm.Method.INDUCTANCE` (1006).

    



    :rtype: tuple (conductance, susceptance)

        WHERE

        conductance (float): 


            **conductance** is the measured value of open cable compensation
            **conductance**.

            


        susceptance (float): 


            **susceptance** is the measured value of open cable compensation
            **susceptance**.

            



.. py:method:: perform_short_cable_comp()

    Performs the short cable compensation measurements for the current
    capacitance/inductance range, and returns short cable compensation
    **Resistance** and **Reactance** values. You can use the return values
    of this method as inputs to :py:meth:`nidmm.Session.configure_short_cable_comp_values`.

    This method returns an error if the value of the :py:data:`nidmm.Session.method`
    property is not set to :py:data:`~nidmm.Method.CAPACITANCE` (1005) or
    :py:data:`~nidmm.Method.INDUCTANCE` (1006).

    



    :rtype: tuple (resistance, reactance)

        WHERE

        resistance (float): 


            **resistance** is the measured value of short cable compensation
            **resistance**.

            


        reactance (float): 


            **reactance** is the measured value of short cable compensation
            **reactance**.

            



.. py:method:: read(maximum_time=datetime.timedelta(milliseconds=-1))

    Acquires a single measurement and returns the measured value.

    



    :param maximum_time:


        Specifies the **maximum_time** allowed for this method to complete in
        milliseconds. If the method does not complete within this time
        interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
        error code. This may happen if an external trigger has not been
        received, or if the specified timeout is not long enough for the
        acquisition to complete.

        The valid range is 0–86400000. The default value is
        :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
        automatically.

        

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type maximum_time: int

    :rtype: float
    :return:


            The measured value returned from the DMM.

            



.. py:method:: read_multi_point(array_size, maximum_time=datetime.timedelta(milliseconds=-1))

    Acquires multiple measurements and returns an array of measured values.
    The number of measurements the DMM makes is determined by the values you
    specify for the **Trigger_Count** and **Sample_Count** parameters in
    :py:meth:`nidmm.Session.configure_multi_point`.

    



    :param array_size:


        Specifies the number of measurements to acquire. The maximum number of
        measurements for a finite acquisition is the (**Trigger Count** x
        **Sample Count**) parameters in :py:meth:`nidmm.Session.configure_multi_point`.

        For continuous acquisitions, up to 100,000 points can be returned at
        once. The number of measurements can be a subset. The valid range is any
        positive ViInt32. The default value is 1.

        


    :type array_size: int
    :param maximum_time:


        Specifies the **maximum_time** allowed for this method to complete in
        milliseconds. If the method does not complete within this time
        interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
        error code. This may happen if an external trigger has not been
        received, or if the specified timeout is not long enough for the
        acquisition to complete.

        The valid range is 0–86400000. The default value is
        :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
        automatically.

        

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type maximum_time: int

    :rtype: tuple (reading_array, actual_number_of_points)

        WHERE

        reading_array (array.array("d")): 


            An array of measurement values.

            

            .. note:: The size of the **Reading_Array** must be at least the size that you
                specify for the **Array_Size** parameter.


        actual_number_of_points (int): 


            Indicates the number of measured values actually retrieved from the DMM.

            



.. py:method:: read_status()

    Returns measurement backlog and acquisition status. Use this method to
    determine how many measurements are available before calling
    :py:meth:`nidmm.Session.fetch`, :py:meth:`nidmm.Session.fetch_multi_point`, or :py:meth:`nidmm.Session.fetch_waveform`.

    

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



.. py:method:: read_waveform(array_size, maximum_time=datetime.timedelta(milliseconds=-1))

    For the NI 4080/4081/4082 and the NI 4070/4071/4072, acquires a waveform
    and returns data as an array of values or as a waveform data type. The
    number of elements in the **Waveform_Array** is determined by the
    values you specify for the **Waveform_Points** parameter in
    :py:meth:`nidmm.Session.configure_waveform_acquisition`.

    



    :param array_size:


        Specifies the number of waveform points to return. You specify the total
        number of points that the DMM acquires in the **Waveform Points**
        parameter of :py:meth:`nidmm.Session.configure_waveform_acquisition`. The default value is
        1.

        


    :type array_size: int
    :param maximum_time:


        Specifies the **maximum_time** allowed for this method to complete in
        milliseconds. If the method does not complete within this time
        interval, the method returns the NIDMM_ERROR_MAX_TIME_EXCEEDED
        error code. This may happen if an external trigger has not been
        received, or if the specified timeout is not long enough for the
        acquisition to complete.

        The valid range is 0–86400000. The default value is
        :py:data:`~nidmm.NIDMM_VAL_TIME_LIMIT_AUTO` (-1). The DMM calculates the timeout
        automatically.

        

        .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


    :type maximum_time: int

    :rtype: tuple (waveform_array, actual_number_of_points)

        WHERE

        waveform_array (array.array("d")): 


            An array of measurement values.

            

            .. note:: The size of the **Waveform_Array** must be at least the size that you
                specify for the **Array_Size** parameter.


        actual_number_of_points (int): 


            Indicates the number of measured values actually retrieved from the DMM.

            



.. py:method:: reset()

    Resets the instrument to a known state and sends initialization commands
    to the instrument. The initialization commands set instrument settings
    to the state necessary for the operation of the instrument driver.

    



.. py:method:: reset_with_defaults()

    Resets the instrument to a known state and sends initialization commands
    to the DMM. The initialization commands set the DMM settings to the
    state necessary for the operation of NI-DMM. All user-defined default
    values associated with a logical name are applied after setting the DMM.

    



.. py:method:: self_cal()

    For the NI 4080/4081/4082 and the NI 4070/4071/4072, executes the
    self-calibration routine to maintain measurement accuracy.

    

    .. note:: This method calls :py:meth:`nidmm.Session.reset`, and any configurations previous to
        the call will be lost. All properties will be set to their default
        values after the call returns.



.. py:method:: self_test()

    Performs a self-test on the DMM to ensure that the DMM is functioning
    properly. Self-test does not calibrate the DMM.

    

    .. note:: This method calls :py:meth:`nidmm.Session.reset`, and any configurations previous to
        the call will be lost. All properties will be set to their default
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


        self_test_message (str): 


            This parameter contains the string returned from the instrument
            self-test. The array must contain at least 256 elements.

            For the NI 4050 and NI 4060, the error codes returned for self-test
            failures include the following:

            -  NIDMM_ERROR_AC_TEST_FAILURE
            -  NIDMM_ERROR_DC_TEST_FAILURE
            -  NIDMM_ERROR_RESISTANCE_TEST_FAILURE

            These error codes indicate that the DMM should be repaired.

            For the NI 4080/4081/4082 and the NI 4070/4071/4072, the error code
            returned for a self-test failure is NIDMM_ERROR_SELF_TEST_FAILURE.
            This error code indicates that the DMM should be repaired.

            



.. py:method:: send_software_trigger()

    Sends a command to trigger the DMM. Call this method if you have
    configured either the :py:data:`nidmm.Session.trigger_source` or
    :py:data:`nidmm.Session.sample_trigger` properties. If the
    :py:data:`nidmm.Session.trigger_source` and/or :py:data:`nidmm.Session.sample_trigger`
    properties are set to :py:data:`~nidmm.NIDMM_VAL_EXTERNAL` or :py:data:`~nidmm.NIDMM_VAL_TTL`\ *n*, you
    can use this method to override the trigger source that you configured
    and trigger the device. The NI 4050 and NI 4060 are not supported.

    

    .. note:: One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.




