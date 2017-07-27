NI-DMM Session
==============

.. py:module:: nidmm

.. py:class:: Session

   An NI-DMM session to a National Instruments Digital Multimeter


   :ivar ViReal64 absolute_resolution: 
      Specifies the measurement resolution in absolute units. Setting this
      property to higher values increases the measurement accuracy. Setting
      this property to lower values increases the measurement speed.
   :ivar ViString active_channel: 
      Specifies the channel name used to access all subsequent channel-based
      properties in this property node. Set the channel before setting
      channel-based properties. Pass a name that the instrument driver defines
      or a virtual channel name configured in MAX.
   :ivar enums.ADCCalibration adc_calibration: 
      For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the ADC
      calibration mode.
   :ivar ViReal64 aperture_time: 
      Specifies the measurement aperture time for the current configuration.
      Aperture time is specified in units set by the Aperture Time Units
      property. To override the default aperture, set this property to the
      desired aperture time after calling niDMM Config Measurement . To return
      to the default, set this property to Aperture Time Auto (-1).
   :ivar enums.ApertureTimeUnits aperture_time_units: 
      Specifies the units of aperture time for the current configuration.
   :ivar ViReal64 auto_range_value: 
      Specifies the value of the range. If auto ranging is enabled, shows the
      actual value of the active range. The value of this property is set
      during a read operation.
   :ivar enums.AutoZero auto_zero: 
      Specifies the AutoZero mode. This property is not supported for the NI
      4050.
   :ivar ViInt32 buffer_size: 
      Specifies the size in samples of the internal data buffer. Maximum size
      is 134,217,727 (0X7FFFFFF) samples. When set to Auto (-1), NI-DMM
      chooses the buffer size.
   :ivar enums.CableCompensationType cable_compensation_type: 
      For the NI 4081 and NI 4072 only, specifies the type of cable
      compensation that is applied to the current capacitance or inductance
      measurement for the current range.
   :ivar ViBoolean cache: 
      Specifies whether to cache the value of properties. When caching is
      enabled, the instrument driver keeps track of the current instrument
      settings and avoids sending redundant commands to the instrument. Thus,
      it significantly increases execution speed. The instrument driver can
      choose to always cache or to never cache particular properties
      regardless of the setting of this property. The default value is TRUE
      (1). Use niDMM Initialize With Options to override the default setting.
   :ivar ViInt32 channel_count: 
      Indicates the number of channels that the specific instrument driver
      supports. For each property for which the IVI\_VAL\_MULTI\_CHANNEL flag
      property is set, the IVI engine maintains a separate cache value for
      each channel.
   :ivar ViReal64 conductance: 
      For the NI 4082 and NI 4072 only, specifies the active part
      (conductance) of the open cable compensation. The valid range is any
      real number >0. The default value (-1.0) indicates that compensation has
      not taken place.
   :ivar enums.CurrentSource current_source: 
      Specifies the current source provided during diode measurements.

      The NI 4050 and NI 4060 are not supported.
   :ivar enums.DCBias dc_bias: 
      For the NI 4082 and NI 4072 only, controls the available DC bias for
      capacitance measurements.
   :ivar enums.DCNoiseRejection dc_noise_rejection: 
      Specifies the DC noise rejection mode.
   :ivar enums.DigitsResolution digits_resolution: 
      Specifies the measurement resolution in digits. Setting this property to
      higher values increases the measurement accuracy. Setting this property
      to lower values increases the measurement speed.
   :ivar ViString driver_setup: 
      This property indicates the Driver Setup string that the user specified
      when initializing the driver. Some cases exist where the end-user must
      specify instrument driver options at initialization time. An example of
      this is specifying a particular instrument model from among a family of
      instruments that the driver supports. This is useful when using
      simulation. The end-user can specify driver-specific options through the
      Driver Setup keyword in the Option String parameter in niDMM Initialize
      With Options . If the user does not specify a Driver Setup string, this
      property returns an empty string.
   :ivar ViInt32 engine_major_version: 
      The major version number of the IVI engine.
   :ivar ViInt32 engine_minor_version: 
      The minor version number of the IVI engine.
   :ivar ViString engine_revision: 
      A string that contains additional version information about the IVI
      engine.
   :ivar ViString error_elaboration: 
      An optional string that contains additional information concerning the
      primary error condition.
   :ivar ViReal64 frequency_voltage_auto_range_value: 
      For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the value of
      the frequency voltage range. If auto ranging is enabled, shows the
      actual value of the active frequency voltage range. If not Auto Ranging,
      the value is the same as that of the Frequency Voltage Range property.
   :ivar ViReal64 frequency_voltage_range: 
      For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the maximum
      amplitude of the input signal for frequency measurements.
   :ivar enums.Function function: 
      Specifies the measurement function. If you are setting this property
      directly, you must also set the Operation Mode property, which controls
      whether the DMM takes standard single or multipoint measurements, or
      acquires a waveform. If you are programming properties directly, you
      must set the Operation Mode property before setting other configuration
      properties. If the Operation Mode property is set to Waveform Mode, the
      only valid function types are Waveform Voltage and Waveform Current. Set
      the Operation Mode property to IVIDMM Mode to set all other function
      values.
   :ivar ViString group_capabilities: 
      A string containing the capabilities and extension groups supported by
      the specific driver.
   :ivar ViString idquery_response: 
      A string containing the type of instrument used in the current session.
   :ivar enums.InputResistance input_resistance: 
      Specifies the input resistance of the instrument.
   :ivar ViString instrument_firmware_revision: 
      A string containing the instrument firmware revision number.
   :ivar ViString instrument_manufacturer: 
      A string containing the manufacturer of the instrument.
   :ivar ViString instrument_model: 
      A string containing the instrument model.
   :ivar ViInt32 instrument_product_id: 
      The PCI product ID.
   :ivar ViString instrument_serial_number: 
      A string containing the serial number of the instrument. This property
      corresponds to the serial number label that is attached to most
      products.
   :ivar ViBoolean interchange_check: 
      Specifies whether to perform interchangeability checking and log
      interchangeability warnings when you call niDMM VIs. Interchangeability
      warnings indicate that using your application with a different
      instrument might cause different behavior. Use niDMM Get Next
      Interchange Warning to extract interchange warnings. Use niDMM Clear
      Interchange Warnings to clear the list of interchangeability warnings
      without reading them. Interchangeability checking examines the
      properties in a capability group only if you specify a value for at
      least one property within that group. Interchangeability warnings can
      occur when a property affects the behavior of the instrument and you
      have not set that property, or the property has been invalidated since
      you set it.
   :ivar ViString io_resource_descriptor: 
      A string containing the resource descriptor of the instrument.
   :ivar ViInt32 latency: 
      Specifies the number of measurements transferred at a time from the
      instrument to an internal buffer. When set to Auto (-1), NI-DMM chooses
      the transfer size.
   :ivar enums.LCCalculationModel lc_calculation_model: 
      For the NI 4082 and NI 4072 only, specifies the type of algorithm that
      the measurement processing uses for capacitance and inductance
      measurements.
   :ivar ViString logical_name: 
      A string containing the logical name of the instrument.
   :ivar ViReal64 max_frequency: 
      Specifies the maximum frequency component of the input signal for AC
      measurements. This property is used only for error checking and verifies
      that the value of this parameter is less than the maximum frequency of
      the device. This property affects the DMM only when you set the Function
      property to AC measurements.
   :ivar enums.MeasurementCompleteDest measurement_completdest: 
      Specifies the destination of the measurement complete (MC) signal.

      To determine which values are supported by each device, refer to the
      LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.
   :ivar enums.MeasurementDestinationSlope measurement_destination_slope: 
      Specifies the polarity of the generated measurement complete signal.
   :ivar ViReal64 min_frequency: 
      Specifies the minimum frequency component of the input signal for AC
      measurements. This property affects the DMM only when you set the
      Function property to AC measurements. The valid range is 1 Hz-300 kHz
      for the NI 4080/4081/4082 and NI 4070/4071/4072, 10 Hz-100 Hz for the NI
      4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.
   :ivar ViInt32 number_of_averages: 
      Specifies the number of averages to perform in a measurement. For the NI
      4080/4081/4082 and NI 4070/4071/4072, applies only when the aperture
      time is not set to Auto and Auto Zero is ON. The Number of Averages
      Property will be ignored otherwise. The default is 4 for 7 1/2 digits;
      otherwise, the default is 1.

      The NI 4050 and NI 4060 are not supported.
   :ivar ViInt32 number_of_lc_measurements_to_average: 
      For the NI 4082 and NI 4072 only, specifies the number of LC
      measurements that are averaged to produce one reading.
   :ivar enums.OffsetCompensatedOhms offset_compensated_ohms: 
      For the NI 4080/4081/4082 and NI 4070/4071/4072, enables or disables
      offset compensated ohms.
   :ivar enums.OperationMode operation_mode: 
      Specifies how the DMM acquires data.

      .. note::
         The NI 4050 and NI 4060 are not supported.

      When you call niDMM Config Measurement , NI-DMM sets this property to
      IVIDMM Mode. When you call niDMM Configure Waveform Acquisition , NI-DMM
      sets this property to Waveform Mode. If you are programming properties
      directly, you must set this property before setting other configuration
      properties.
   :ivar enums.PowerlineFrequency powerline_frequency: 
      Specifies the powerline frequency. The NI 4060 and NI 4050 use this
      value to select an aperture time to reject powerline noise by selecting
      the appropriate internal sample clock and filter. The NI 4065, NI
      4070/4071/4072, and NI 4080/4081/4082 use this value to select timebases
      for setting the Aperture Time property in powerline cycles.
   :ivar ViInt32 primary_error: 
      A code that describes the first error that occurred since the last call
      to niDMM Get Error for the session. The value follows the VXIplug&play
      conventions. A negative value describes an error condition. A positive
      value describes a warning condition. A zero indicates that no error or
      warning occurred. The error and warning values can be status codes
      defined by IVI, VISA, class drivers, or specific drivers.
   :ivar ViBoolean query_instrument_status: 
      Specifies whether the instrument driver queries the instrument status
      after each operation. Querying the instrument status is very useful for
      debugging. After the user program is validated, this property can be set
      to FALSE (0) to disable status checking and maximize performance. The
      instrument driver can choose to ignore status checking for particular
      properties regardless of the setting of this property. The default value
      is TRUE (1). Use niDMM Initialize With Options to override the default
      setting.
   :ivar ViReal64 range: 
      Specifies the measurement range. Use positive values to represent the
      absolute value of the maximum expected measurement. The value is in
      units appropriate for the current value of the Function property. For
      example, if the Function property is set to DC Volts, the units are
      volts.
   :ivar ViBoolean range_check: 
      Specifies whether to validate property values and VI parameters. If
      enabled, the instrument driver validates the parameter values passed to
      driver VIs. Range checking parameters is very useful for debugging.
      After the user program is validated, you can set this property to FALSE
      (0) to disable range checking and maximize performance. The default
      value is TRUE (1). Use niDMM Initialize With Options to override the
      default setting.
   :ivar ViReal64 reactance: 
      For the NI 4082 and NI 4072 only, represents the reactive part
      (reactance) of the short cable compensation. The valid range is any real
      number >0. The default value (-1) indicates that compensation has not
      taken place.
   :ivar ViBoolean record_value_coercions: 
      Specifies whether the IVI engine keeps a list of the value coercions it
      makes for ViInt32 and ViReal64 properties. The default value is FALSE
      (0). Use niDMM Initialize With Options to override the default setting.
      Use niDMM Get Next Coercion Record to extract and delete the oldest
      coercion record from the list.
   :ivar ViReal64 resistance: 
      For the NI 4082 and NI 4072 only, represents the active part
      (resistance) of the short cable compensation. The valid range is any
      real number >0. The default value (-1) indicates that compensation has
      not taken place.
   :ivar ViReal64 rtd_a: 
      Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the
      **RTD Type property** is set to Custom.
   :ivar ViReal64 rtd_b: 
      Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the
      **RTD Type property** is set to Custom.
   :ivar ViReal64 rtd_c: 
      Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the
      **RTD Type property** is set to Custom.
   :ivar ViReal64 rtd_resistance: 
      Specifies the RTD resistance at 0 degrees Celsius.
   :ivar enums.RTDType rtd_type: 
      Specifies the RTD type.
   :ivar ViInt32 sample_count: 
      Specifies the number of measurements the DMM takes each time it receives
      a trigger in a multiple point acquisition. Setting Sample Count to 0 on
      the NI 4050 and NI 4060 causes the device to take continuous
      measurements. Otherwise, setting Sample Count to 0 causes the
      conditional statement "Measurements equal to Sample Count" to always
      evaluate to False, and causes the DMM to continue taking measurements in
      the inner loop.
   :ivar ViInt32 sample_delay_mode: 
      For the NI 4060 only, specifies a delay interval after a sample trigger.
   :ivar ViReal64 sample_interval: 
      Specifies the amount of time in seconds the DMM waits between
      measurement cycles. This property only applies when the Sample Trigger
      property is set to INTERVAL. The default value (-1) ensures that the DMM
      settles for a recommended time, which is the same as using an immediate
      trigger.
   :ivar enums.SampleTrigger sample_trigger: 
      Specifies the sample trigger source.

      To determine which values are supported by each device, refer to the
      LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.
   :ivar enums.SampleTrigSlope sample_trig_slope: 
      Specifies the edge of the signal from the specified sample trigger
      source on which the DMM is triggered.
   :ivar ViInt32 secondary_error: 
      An optional code that provides additional information concerning the
      primary error condition. The error and warning values can be status
      codes defined by IVI, VISA, class drivers, or specific drivers. Zero
      indicates no additional information.
   :ivar ViReal64 settle_time: 
      Specifies the settling time in seconds. Use this property to override
      the default settling time. To return to the default, set this property
      to Auto (-1).
   :ivar ViReal64 shunt_value: 
      For the NI 4050 only, specifies the shunt resistance value.
   :ivar ViBoolean simulate: 
      Specifies whether to simulate instrument driver I/O operations. If
      simulation is enabled, instrument driver functions perform range
      checking and call IVI Get and Set VIs, but they do not perform
      instrument I/O. For output parameters that represent instrument data,
      the instrument driver VIs return calculated values. The default value is
      FALSE (0). Use niDMM Initialize With Options to override the default
      setting.
   :ivar ViInt32 specific_driver_class_spec_major_version: 
      The major version number of the class specification for the specific
      driver.
   :ivar ViInt32 specific_driver_class_spec_minor_version: 
      The minor version number of the class specification for the specific
      driver.
   :ivar ViString specific_driver_description: 
      A string containing a description of the specific driver.
   :ivar ViInt32 specific_driver_major_version: 
      Returns the major version number of this instrument driver.
   :ivar ViInt32 specific_driver_minor_version: 
      Returns the minor version number of this instrument driver.
   :ivar ViString specific_driver_prefix: 
      The prefix for the specific instrument driver. The name of each
      user-callable VI in this driver starts with this prefix. The prefix can
      be up to a maximum of eight characters.
   :ivar ViString specific_driver_revision: 
      A string that contains additional version information about this
      instrument driver.
   :ivar ViString specific_driver_vendor: 
      A string containing the vendor of the specific driver.
   :ivar ViString supported_instrument_models: 
      A string containing the instrument models supported by the specific
      driver.
   :ivar ViReal64 susceptance: 
      For the NI 4082 and NI 4072 only, specifies the reactive part
      (susceptance) of the open cable compensation. The valid range is any
      real number >0. The default value (-1.0) indicates that compensation has
      not taken place.
   :ivar ViReal64 tc_fixed_ref_junction: 
      Specifies the value of the fixed reference junction temperature for a
      thermocouple in degrees Celsius.
   :ivar enums.ThermocoupleReferenceJunctionType tc_ref_junction_type: 
      Specifies the thermocouple reference junction type.
   :ivar ViReal64 thermistor_a: 
      Specifies the Steinhart-Hart A coefficient for thermistor scaling when
      the **Thermistor Type property** is set to Custom.
   :ivar ViReal64 thermistor_b: 
      Specifies the Steinhart-Hart B coefficient for thermistor scaling when
      the **Thermistor Type property** is set to Custom.
   :ivar ViReal64 thermistor_c: 
      Specifies the Steinhart-Hart C coefficient for thermistor scaling when
      the **Thermistor Type property** is set to Custom.
   :ivar enums.ThermistorType thermistor_type: 
      Specifies the thermistor type.
   :ivar enums.ThermocoupleType thermocouple_type: 
      Specifies the thermocouple type.
   :ivar enums.TransducerType transducer_type: 
      Specifies the transducer type.
   :ivar ViInt32 trigger_count: 
      Specifies the number of triggers the DMM receives before returning to
      the Idle state. This property can be set to any positive ViInt32 value
      for the NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082.

      The NI 4050/4060 only support this property being set to 1.

      Refer to Multiple Point Acquisitions in the *NI Digital Multimeters
      Help* for more information.
   :ivar ViReal64 trigger_delay: 
      Specifies the time (in seconds) that the DMM waits after it has received
      a trigger before taking a measurement. The default value is Auto Delay
      (-1), which means that the DMM waits an appropriate settling time before
      taking the measurement.

      The NI 4080/4081/4082 uses the value specified in this property as
      additional settling time. The valid range for Trigger Delay is Auto
      Delay (-1) or 0.0 - 150.0 seconds, and the onboard timing resolution is
      10.0 ns.

      The NI 4065 and NI 4070/4071/4072 use the value specified in this
      property as additional settling time. For these devices, the valid range
      for Trigger Delay is Auto Delay (-1) or 0.0 - 149.0 seconds and the
      onboard timing resolution is 34.72 ns.

      On the NI 4060, if this property is set to 0, the DMM does not settle
      before taking the measurement. On the NI 4060, the valid range for
      Trigger Delay (-1) is 0.0-12.0 seconds and the onboard timing resolution
      is 100 ms.

      When using the NI 4050, this property must be set to Auto Delay (-1).

      Use positive values to set the trigger delay in seconds.

      Valid Range: Auto Delay (-1.0), 0.0-12.0 seconds (NI 4060 only),
      0.0-149.0 seconds (NI 4065 and NI 4070/4071/4072)

      Default Value: Auto Delay
   :ivar enums.TriggerSlope trigger_slope: 
      Specifies the edge of the signal from the specified trigger source on
      which the DMM is triggered.
   :ivar enums.TriggerSource trigger_source: 
      Specifies the trigger source. When niDMM Initiate is called, the DMM
      waits for the trigger specified with this property. After it receives
      the trigger, the DMM waits the length of time specified with the Trigger
      Delay property. The DMM then takes a measurement.

      To determine which values are supported by each device, refer to the
      LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.
   :ivar enums.WaveformCoupling waveform_coupling: 
      For the NI 4080/4081/4082 and NI 4070/4071/4072 only, specifies the
      coupling during a waveform acquisition.
   :ivar ViInt32 waveform_points: 
      For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the number of
      points to acquire in a waveform acquisition.
   :ivar ViReal64 waveform_rate: 
      Specifies the rate of the waveform acquisition in samples per second
      (S/s). The valid rate is calculated by dividing 1,800,000 by an integer
      divisor, and the rate falls between 10 and 1,800,000 samples per second.
      The waveform rate is coerced upwards to the next valid rate. The default
      value is 1,800,000 samples per second. Not supported by NI 4065.


