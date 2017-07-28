NI-DMM Session
==============

.. py:module:: nidmm

.. py:class:: Session

   An NI-DMM session to a National Instruments Digital Multimeter


   :var absolute_resolution: 
      Specifies the measurement resolution in absolute units. Setting this
      property to higher values increases the measurement accuracy. Setting
      this property to lower values increases the measurement speed.
   :vartype absolute_resolution: ViReal64
   :var adc_calibration: 
      For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the ADC
      calibration mode.
   :vartype adc_calibration: :py:data:`ADCCalibration`
   :var aperture_time: 
      Specifies the measurement aperture time for the current configuration.
      Aperture time is specified in units set by the Aperture Time Units
      property. To override the default aperture, set this property to the
      desired aperture time after calling niDMM Config Measurement . To return
      to the default, set this property to Aperture Time Auto (-1).
   :vartype aperture_time: ViReal64
   :var aperture_time_units: 
      Specifies the units of aperture time for the current configuration.
   :vartype aperture_time_units: :py:data:`ApertureTimeUnits`
   :var auto_range_value: 
      Specifies the value of the range. If auto ranging is enabled, shows the
      actual value of the active range. The value of this property is set
      during a read operation.
   :vartype auto_range_value: ViReal64
   :var auto_zero: 
      Specifies the AutoZero mode. This property is not supported for the NI
      4050.
   :vartype auto_zero: :py:data:`AutoZero`
   :var buffer_size: 
      Specifies the size in samples of the internal data buffer. Maximum size
      is 134,217,727 (0X7FFFFFF) samples. When set to Auto (-1), NI-DMM
      chooses the buffer size.
   :vartype buffer_size: ViInt32
   :var cable_compensation_type: 
      For the NI 4081 and NI 4072 only, specifies the type of cable
      compensation that is applied to the current capacitance or inductance
      measurement for the current range.
   :vartype cable_compensation_type: :py:data:`CableCompensationType`
   :var cache: 
      Specifies whether to cache the value of properties. When caching is
      enabled, the instrument driver keeps track of the current instrument
      settings and avoids sending redundant commands to the instrument. Thus,
      it significantly increases execution speed. The instrument driver can
      choose to always cache or to never cache particular properties
      regardless of the setting of this property. The default value is TRUE
      (1). Use niDMM Initialize With Options to override the default setting.
   :vartype cache: ViBoolean
   :var channel_count: 
      Indicates the number of channels that the specific instrument driver
      supports. For each property for which the IVI\_VAL\_MULTI\_CHANNEL flag
      property is set, the IVI engine maintains a separate cache value for
      each channel.
   :vartype channel_count: ViInt32
   :var conductance: 
      For the NI 4082 and NI 4072 only, specifies the active part
      (conductance) of the open cable compensation. The valid range is any
      real number >0. The default value (-1.0) indicates that compensation has
      not taken place.
   :vartype conductance: ViReal64
   :var current_source: 
      Specifies the current source provided during diode measurements.

      The NI 4050 and NI 4060 are not supported.
   :vartype current_source: :py:data:`CurrentSource`
   :var dc_bias: 
      For the NI 4082 and NI 4072 only, controls the available DC bias for
      capacitance measurements.
   :vartype dc_bias: :py:data:`DCBias`
   :var dc_noise_rejection: 
      Specifies the DC noise rejection mode.
   :vartype dc_noise_rejection: :py:data:`DCNoiseRejection`
   :var digits_resolution: 
      Specifies the measurement resolution in digits. Setting this property to
      higher values increases the measurement accuracy. Setting this property
      to lower values increases the measurement speed.
   :vartype digits_resolution: :py:data:`DigitsResolution`
   :var driver_setup: 
      This property indicates the Driver Setup string that the user specified
      when initializing the driver. Some cases exist where the end-user must
      specify instrument driver options at initialization time. An example of
      this is specifying a particular instrument model from among a family of
      instruments that the driver supports. This is useful when using
      simulation. The end-user can specify driver-specific options through the
      Driver Setup keyword in the Option String parameter in niDMM Initialize
      With Options . If the user does not specify a Driver Setup string, this
      property returns an empty string.
   :vartype driver_setup: ViString
   :var engine_major_version: 
      The major version number of the IVI engine.
   :vartype engine_major_version: ViInt32
   :var engine_minor_version: 
      The minor version number of the IVI engine.
   :vartype engine_minor_version: ViInt32
   :var engine_revision: 
      A string that contains additional version information about the IVI
      engine.
   :vartype engine_revision: ViString
   :var error_elaboration: 
      An optional string that contains additional information concerning the
      primary error condition.
   :vartype error_elaboration: ViString
   :var frequency_voltage_auto_range_value: 
      For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the value of
      the frequency voltage range. If auto ranging is enabled, shows the
      actual value of the active frequency voltage range. If not Auto Ranging,
      the value is the same as that of the Frequency Voltage Range property.
   :vartype frequency_voltage_auto_range_value: ViReal64
   :var frequency_voltage_range: 
      For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the maximum
      amplitude of the input signal for frequency measurements.
   :vartype frequency_voltage_range: ViReal64
   :var function: 
      Specifies the measurement function. If you are setting this property
      directly, you must also set the Operation Mode property, which controls
      whether the DMM takes standard single or multipoint measurements, or
      acquires a waveform. If you are programming properties directly, you
      must set the Operation Mode property before setting other configuration
      properties. If the Operation Mode property is set to Waveform Mode, the
      only valid function types are Waveform Voltage and Waveform Current. Set
      the Operation Mode property to IVIDMM Mode to set all other function
      values.
   :vartype function: :py:data:`Function`
   :var group_capabilities: 
      A string containing the capabilities and extension groups supported by
      the specific driver.
   :vartype group_capabilities: ViString
   :var idquery_response: 
      A string containing the type of instrument used in the current session.
   :vartype idquery_response: ViString
   :var input_resistance: 
      Specifies the input resistance of the instrument.
   :vartype input_resistance: :py:data:`InputResistance`
   :var instrument_firmware_revision: 
      A string containing the instrument firmware revision number.
   :vartype instrument_firmware_revision: ViString
   :var instrument_manufacturer: 
      A string containing the manufacturer of the instrument.
   :vartype instrument_manufacturer: ViString
   :var instrument_model: 
      A string containing the instrument model.
   :vartype instrument_model: ViString
   :var instrument_product_id: 
      The PCI product ID.
   :vartype instrument_product_id: ViInt32
   :var instrument_serial_number: 
      A string containing the serial number of the instrument. This property
      corresponds to the serial number label that is attached to most
      products.
   :vartype instrument_serial_number: ViString
   :var interchange_check: 
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
   :vartype interchange_check: ViBoolean
   :var io_resource_descriptor: 
      A string containing the resource descriptor of the instrument.
   :vartype io_resource_descriptor: ViString
   :var latency: 
      Specifies the number of measurements transferred at a time from the
      instrument to an internal buffer. When set to Auto (-1), NI-DMM chooses
      the transfer size.
   :vartype latency: ViInt32
   :var lc_calculation_model: 
      For the NI 4082 and NI 4072 only, specifies the type of algorithm that
      the measurement processing uses for capacitance and inductance
      measurements.
   :vartype lc_calculation_model: :py:data:`LCCalculationModel`
   :var logical_name: 
      A string containing the logical name of the instrument.
   :vartype logical_name: ViString
   :var max_frequency: 
      Specifies the maximum frequency component of the input signal for AC
      measurements. This property is used only for error checking and verifies
      that the value of this parameter is less than the maximum frequency of
      the device. This property affects the DMM only when you set the Function
      property to AC measurements.
   :vartype max_frequency: ViReal64
   :var measurement_completdest: 
      Specifies the destination of the measurement complete (MC) signal.

      To determine which values are supported by each device, refer to the
      LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.
   :vartype measurement_completdest: :py:data:`MeasurementCompleteDest`
   :var measurement_destination_slope: 
      Specifies the polarity of the generated measurement complete signal.
   :vartype measurement_destination_slope: :py:data:`MeasurementDestinationSlope`
   :var min_frequency: 
      Specifies the minimum frequency component of the input signal for AC
      measurements. This property affects the DMM only when you set the
      Function property to AC measurements. The valid range is 1 Hz-300 kHz
      for the NI 4080/4081/4082 and NI 4070/4071/4072, 10 Hz-100 Hz for the NI
      4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.
   :vartype min_frequency: ViReal64
   :var number_of_averages: 
      Specifies the number of averages to perform in a measurement. For the NI
      4080/4081/4082 and NI 4070/4071/4072, applies only when the aperture
      time is not set to Auto and Auto Zero is ON. The Number of Averages
      Property will be ignored otherwise. The default is 4 for 7 1/2 digits;
      otherwise, the default is 1.

      The NI 4050 and NI 4060 are not supported.
   :vartype number_of_averages: ViInt32
   :var number_of_lc_measurements_to_average: 
      For the NI 4082 and NI 4072 only, specifies the number of LC
      measurements that are averaged to produce one reading.
   :vartype number_of_lc_measurements_to_average: ViInt32
   :var offset_compensated_ohms: 
      For the NI 4080/4081/4082 and NI 4070/4071/4072, enables or disables
      offset compensated ohms.
   :vartype offset_compensated_ohms: :py:data:`OffsetCompensatedOhms`
   :var operation_mode: 
      Specifies how the DMM acquires data.

      .. note::
         The NI 4050 and NI 4060 are not supported.

      When you call niDMM Config Measurement , NI-DMM sets this property to
      IVIDMM Mode. When you call niDMM Configure Waveform Acquisition , NI-DMM
      sets this property to Waveform Mode. If you are programming properties
      directly, you must set this property before setting other configuration
      properties.
   :vartype operation_mode: :py:data:`OperationMode`
   :var powerline_frequency: 
      Specifies the powerline frequency. The NI 4060 and NI 4050 use this
      value to select an aperture time to reject powerline noise by selecting
      the appropriate internal sample clock and filter. The NI 4065, NI
      4070/4071/4072, and NI 4080/4081/4082 use this value to select timebases
      for setting the Aperture Time property in powerline cycles.
   :vartype powerline_frequency: :py:data:`PowerlineFrequency`
   :var primary_error: 
      A code that describes the first error that occurred since the last call
      to niDMM Get Error for the session. The value follows the VXIplug&play
      conventions. A negative value describes an error condition. A positive
      value describes a warning condition. A zero indicates that no error or
      warning occurred. The error and warning values can be status codes
      defined by IVI, VISA, class drivers, or specific drivers.
   :vartype primary_error: ViInt32
   :var query_instrument_status: 
      Specifies whether the instrument driver queries the instrument status
      after each operation. Querying the instrument status is very useful for
      debugging. After the user program is validated, this property can be set
      to FALSE (0) to disable status checking and maximize performance. The
      instrument driver can choose to ignore status checking for particular
      properties regardless of the setting of this property. The default value
      is TRUE (1). Use niDMM Initialize With Options to override the default
      setting.
   :vartype query_instrument_status: ViBoolean
   :var range: 
      Specifies the measurement range. Use positive values to represent the
      absolute value of the maximum expected measurement. The value is in
      units appropriate for the current value of the Function property. For
      example, if the Function property is set to DC Volts, the units are
      volts.
   :vartype range: ViReal64
   :var range_check: 
      Specifies whether to validate property values and VI parameters. If
      enabled, the instrument driver validates the parameter values passed to
      driver VIs. Range checking parameters is very useful for debugging.
      After the user program is validated, you can set this property to FALSE
      (0) to disable range checking and maximize performance. The default
      value is TRUE (1). Use niDMM Initialize With Options to override the
      default setting.
   :vartype range_check: ViBoolean
   :var reactance: 
      For the NI 4082 and NI 4072 only, represents the reactive part
      (reactance) of the short cable compensation. The valid range is any real
      number >0. The default value (-1) indicates that compensation has not
      taken place.
   :vartype reactance: ViReal64
   :var record_value_coercions: 
      Specifies whether the IVI engine keeps a list of the value coercions it
      makes for ViInt32 and ViReal64 properties. The default value is FALSE
      (0). Use niDMM Initialize With Options to override the default setting.
      Use niDMM Get Next Coercion Record to extract and delete the oldest
      coercion record from the list.
   :vartype record_value_coercions: ViBoolean
   :var resistance: 
      For the NI 4082 and NI 4072 only, represents the active part
      (resistance) of the short cable compensation. The valid range is any
      real number >0. The default value (-1) indicates that compensation has
      not taken place.
   :vartype resistance: ViReal64
   :var rtd_a: 
      Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the
      **RTD Type property** is set to Custom.
   :vartype rtd_a: ViReal64
   :var rtd_b: 
      Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the
      **RTD Type property** is set to Custom.
   :vartype rtd_b: ViReal64
   :var rtd_c: 
      Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the
      **RTD Type property** is set to Custom.
   :vartype rtd_c: ViReal64
   :var rtd_resistance: 
      Specifies the RTD resistance at 0 degrees Celsius.
   :vartype rtd_resistance: ViReal64
   :var rtd_type: 
      Specifies the RTD type.
   :vartype rtd_type: :py:data:`RTDType`
   :var sample_count: 
      Specifies the number of measurements the DMM takes each time it receives
      a trigger in a multiple point acquisition. Setting Sample Count to 0 on
      the NI 4050 and NI 4060 causes the device to take continuous
      measurements. Otherwise, setting Sample Count to 0 causes the
      conditional statement "Measurements equal to Sample Count" to always
      evaluate to False, and causes the DMM to continue taking measurements in
      the inner loop.
   :vartype sample_count: ViInt32
   :var sample_delay_mode: 
      For the NI 4060 only, specifies a delay interval after a sample trigger.
   :vartype sample_delay_mode: ViInt32
   :var sample_interval: 
      Specifies the amount of time in seconds the DMM waits between
      measurement cycles. This property only applies when the Sample Trigger
      property is set to INTERVAL. The default value (-1) ensures that the DMM
      settles for a recommended time, which is the same as using an immediate
      trigger.
   :vartype sample_interval: ViReal64
   :var sample_trigger: 
      Specifies the sample trigger source.

      To determine which values are supported by each device, refer to the
      LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.
   :vartype sample_trigger: :py:data:`SampleTrigger`
   :var sample_trig_slope: 
      Specifies the edge of the signal from the specified sample trigger
      source on which the DMM is triggered.
   :vartype sample_trig_slope: :py:data:`SampleTrigSlope`
   :var secondary_error: 
      An optional code that provides additional information concerning the
      primary error condition. The error and warning values can be status
      codes defined by IVI, VISA, class drivers, or specific drivers. Zero
      indicates no additional information.
   :vartype secondary_error: ViInt32
   :var settle_time: 
      Specifies the settling time in seconds. Use this property to override
      the default settling time. To return to the default, set this property
      to Auto (-1).
   :vartype settle_time: ViReal64
   :var shunt_value: 
      For the NI 4050 only, specifies the shunt resistance value.
   :vartype shunt_value: ViReal64
   :var simulate: 
      Specifies whether to simulate instrument driver I/O operations. If
      simulation is enabled, instrument driver functions perform range
      checking and call IVI Get and Set VIs, but they do not perform
      instrument I/O. For output parameters that represent instrument data,
      the instrument driver VIs return calculated values. The default value is
      FALSE (0). Use niDMM Initialize With Options to override the default
      setting.
   :vartype simulate: ViBoolean
   :var specific_driver_class_spec_major_version: 
      The major version number of the class specification for the specific
      driver.
   :vartype specific_driver_class_spec_major_version: ViInt32
   :var specific_driver_class_spec_minor_version: 
      The minor version number of the class specification for the specific
      driver.
   :vartype specific_driver_class_spec_minor_version: ViInt32
   :var specific_driver_description: 
      A string containing a description of the specific driver.
   :vartype specific_driver_description: ViString
   :var specific_driver_major_version: 
      Returns the major version number of this instrument driver.
   :vartype specific_driver_major_version: ViInt32
   :var specific_driver_minor_version: 
      Returns the minor version number of this instrument driver.
   :vartype specific_driver_minor_version: ViInt32
   :var specific_driver_prefix: 
      The prefix for the specific instrument driver. The name of each
      user-callable VI in this driver starts with this prefix. The prefix can
      be up to a maximum of eight characters.
   :vartype specific_driver_prefix: ViString
   :var specific_driver_revision: 
      A string that contains additional version information about this
      instrument driver.
   :vartype specific_driver_revision: ViString
   :var specific_driver_vendor: 
      A string containing the vendor of the specific driver.
   :vartype specific_driver_vendor: ViString
   :var supported_instrument_models: 
      A string containing the instrument models supported by the specific
      driver.
   :vartype supported_instrument_models: ViString
   :var susceptance: 
      For the NI 4082 and NI 4072 only, specifies the reactive part
      (susceptance) of the open cable compensation. The valid range is any
      real number >0. The default value (-1.0) indicates that compensation has
      not taken place.
   :vartype susceptance: ViReal64
   :var tc_fixed_ref_junction: 
      Specifies the value of the fixed reference junction temperature for a
      thermocouple in degrees Celsius.
   :vartype tc_fixed_ref_junction: ViReal64
   :var tc_ref_junction_type: 
      Specifies the thermocouple reference junction type.
   :vartype tc_ref_junction_type: :py:data:`ThermocoupleReferenceJunctionType`
   :var thermistor_a: 
      Specifies the Steinhart-Hart A coefficient for thermistor scaling when
      the **Thermistor Type property** is set to Custom.
   :vartype thermistor_a: ViReal64
   :var thermistor_b: 
      Specifies the Steinhart-Hart B coefficient for thermistor scaling when
      the **Thermistor Type property** is set to Custom.
   :vartype thermistor_b: ViReal64
   :var thermistor_c: 
      Specifies the Steinhart-Hart C coefficient for thermistor scaling when
      the **Thermistor Type property** is set to Custom.
   :vartype thermistor_c: ViReal64
   :var thermistor_type: 
      Specifies the thermistor type.
   :vartype thermistor_type: :py:data:`ThermistorType`
   :var thermocouple_type: 
      Specifies the thermocouple type.
   :vartype thermocouple_type: :py:data:`ThermocoupleType`
   :var transducer_type: 
      Specifies the transducer type.
   :vartype transducer_type: :py:data:`TransducerType`
   :var trigger_count: 
      Specifies the number of triggers the DMM receives before returning to
      the Idle state. This property can be set to any positive ViInt32 value
      for the NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082.

      The NI 4050/4060 only support this property being set to 1.

      Refer to Multiple Point Acquisitions in the *NI Digital Multimeters
      Help* for more information.
   :vartype trigger_count: ViInt32
   :var trigger_delay: 
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
   :vartype trigger_delay: ViReal64
   :var trigger_slope: 
      Specifies the edge of the signal from the specified trigger source on
      which the DMM is triggered.
   :vartype trigger_slope: :py:data:`TriggerSlope`
   :var trigger_source: 
      Specifies the trigger source. When niDMM Initiate is called, the DMM
      waits for the trigger specified with this property. After it receives
      the trigger, the DMM waits the length of time specified with the Trigger
      Delay property. The DMM then takes a measurement.

      To determine which values are supported by each device, refer to the
      LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.
   :vartype trigger_source: :py:data:`TriggerSource`
   :var waveform_coupling: 
      For the NI 4080/4081/4082 and NI 4070/4071/4072 only, specifies the
      coupling during a waveform acquisition.
   :vartype waveform_coupling: :py:data:`WaveformCoupling`
   :var waveform_points: 
      For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the number of
      points to acquire in a waveform acquisition.
   :vartype waveform_points: ViInt32
   :var waveform_rate: 
      Specifies the rate of the waveform acquisition in samples per second
      (S/s). The valid rate is calculated by dividing 1,800,000 by an integer
      divisor, and the rate falls between 10 and 1,800,000 samples per second.
      The waveform rate is coerced upwards to the next valid rate. The default
      value is 1,800,000 samples per second. Not supported by NI 4065.
   :vartype waveform_rate: ViReal64


