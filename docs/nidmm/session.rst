NI-DMM Session
==============

.. py:module:: nidmm

.. py:class:: Session

   An NI-DMM session to a National Instruments Digital Multimeter


   :var absolute_resolution: 
   :vartype absolute_resolution: ViReal64
   :var adc_calibration: 
   :vartype adc_calibration: :py:data:`ADCCalibration`
   :var aperture_time: 
   :vartype aperture_time: ViReal64
   :var aperture_time_units: 
   :vartype aperture_time_units: :py:data:`ApertureTimeUnits`
   :var auto_range_value: 
   :vartype auto_range_value: ViReal64
   :var auto_zero: 
   :vartype auto_zero: :py:data:`AutoZero`
   :var buffer_size: 
   :vartype buffer_size: ViInt32
   :var cable_compensation_type: 
   :vartype cable_compensation_type: :py:data:`CableCompensationType`
   :var cache: 
   :vartype cache: ViBoolean
   :var channel_count: 
   :vartype channel_count: ViInt32
   :var conductance: 
   :vartype conductance: ViReal64
   :var current_source: 
   :vartype current_source: :py:data:`CurrentSource`
   :var dc_bias: 
   :vartype dc_bias: :py:data:`DCBias`
   :var dc_noise_rejection: 
   :vartype dc_noise_rejection: :py:data:`DCNoiseRejection`
   :var digits_resolution: 
   :vartype digits_resolution: :py:data:`DigitsResolution`
   :var driver_setup: 
   :vartype driver_setup: ViString
   :var engine_major_version: 
   :vartype engine_major_version: ViInt32
   :var engine_minor_version: 
   :vartype engine_minor_version: ViInt32
   :var engine_revision: 
   :vartype engine_revision: ViString
   :var error_elaboration: 
   :vartype error_elaboration: ViString
   :var frequency_voltage_auto_range_value: 
   :vartype frequency_voltage_auto_range_value: ViReal64
   :var frequency_voltage_range: 
   :vartype frequency_voltage_range: ViReal64
   :var function: 
   :vartype function: :py:data:`Function`
   :var group_capabilities: 
   :vartype group_capabilities: ViString
   :var idquery_response: 
   :vartype idquery_response: ViString
   :var input_resistance: 
   :vartype input_resistance: :py:data:`InputResistance`
   :var instrument_firmware_revision: 
   :vartype instrument_firmware_revision: ViString
   :var instrument_manufacturer: 
   :vartype instrument_manufacturer: ViString
   :var instrument_model: 
   :vartype instrument_model: ViString
   :var instrument_product_id: 
   :vartype instrument_product_id: ViInt32
   :var instrument_serial_number: 
   :vartype instrument_serial_number: ViString
   :var interchange_check: 
   :vartype interchange_check: ViBoolean
   :var io_resource_descriptor: 
   :vartype io_resource_descriptor: ViString
   :var latency: 
   :vartype latency: ViInt32
   :var lc_calculation_model: 
   :vartype lc_calculation_model: :py:data:`LCCalculationModel`
   :var logical_name: 
   :vartype logical_name: ViString
   :var max_frequency: 
   :vartype max_frequency: ViReal64
   :var measurement_completdest: 
   :vartype measurement_completdest: :py:data:`MeasurementCompleteDest`
   :var measurement_destination_slope: 
   :vartype measurement_destination_slope: :py:data:`MeasurementDestinationSlope`
   :var min_frequency: 
   :vartype min_frequency: ViReal64
   :var number_of_averages: 
   :vartype number_of_averages: ViInt32
   :var number_of_lc_measurements_to_average: 
   :vartype number_of_lc_measurements_to_average: ViInt32
   :var offset_compensated_ohms: 
   :vartype offset_compensated_ohms: :py:data:`OffsetCompensatedOhms`
   :var operation_mode: 
   :vartype operation_mode: :py:data:`OperationMode`
   :var powerline_frequency: 
   :vartype powerline_frequency: :py:data:`PowerlineFrequency`
   :var primary_error: 
   :vartype primary_error: ViInt32
   :var query_instrument_status: 
   :vartype query_instrument_status: ViBoolean
   :var range: 
   :vartype range: ViReal64
   :var range_check: 
   :vartype range_check: ViBoolean
   :var reactance: 
   :vartype reactance: ViReal64
   :var record_value_coercions: 
   :vartype record_value_coercions: ViBoolean
   :var resistance: 
   :vartype resistance: ViReal64
   :var rtd_a: 
   :vartype rtd_a: ViReal64
   :var rtd_b: 
   :vartype rtd_b: ViReal64
   :var rtd_c: 
   :vartype rtd_c: ViReal64
   :var rtd_resistance: 
   :vartype rtd_resistance: ViReal64
   :var rtd_type: 
   :vartype rtd_type: :py:data:`RTDType`
   :var sample_count: 
   :vartype sample_count: ViInt32
   :var sample_delay_mode: 
   :vartype sample_delay_mode: ViInt32
   :var sample_interval: 
   :vartype sample_interval: ViReal64
   :var sample_trigger: 
   :vartype sample_trigger: :py:data:`SampleTrigger`
   :var sample_trig_slope: 
   :vartype sample_trig_slope: :py:data:`SampleTrigSlope`
   :var secondary_error: 
   :vartype secondary_error: ViInt32
   :var settle_time: 
   :vartype settle_time: ViReal64
   :var shunt_value: 
   :vartype shunt_value: ViReal64
   :var simulate: 
   :vartype simulate: ViBoolean
   :var specific_driver_class_spec_major_version: 
   :vartype specific_driver_class_spec_major_version: ViInt32
   :var specific_driver_class_spec_minor_version: 
   :vartype specific_driver_class_spec_minor_version: ViInt32
   :var specific_driver_description: 
   :vartype specific_driver_description: ViString
   :var specific_driver_major_version: 
   :vartype specific_driver_major_version: ViInt32
   :var specific_driver_minor_version: 
   :vartype specific_driver_minor_version: ViInt32
   :var specific_driver_prefix: 
   :vartype specific_driver_prefix: ViString
   :var specific_driver_revision: 
   :vartype specific_driver_revision: ViString
   :var specific_driver_vendor: 
   :vartype specific_driver_vendor: ViString
   :var supported_instrument_models: 
   :vartype supported_instrument_models: ViString
   :var susceptance: 
   :vartype susceptance: ViReal64
   :var tc_fixed_ref_junction: 
   :vartype tc_fixed_ref_junction: ViReal64
   :var tc_ref_junction_type: 
   :vartype tc_ref_junction_type: :py:data:`ThermocoupleReferenceJunctionType`
   :var thermistor_a: 
   :vartype thermistor_a: ViReal64
   :var thermistor_b: 
   :vartype thermistor_b: ViReal64
   :var thermistor_c: 
   :vartype thermistor_c: ViReal64
   :var thermistor_type: 
   :vartype thermistor_type: :py:data:`ThermistorType`
   :var thermocouple_type: 
   :vartype thermocouple_type: :py:data:`ThermocoupleType`
   :var transducer_type: 
   :vartype transducer_type: :py:data:`TransducerType`
   :var trigger_count: 
   :vartype trigger_count: ViInt32
   :var trigger_delay: 
   :vartype trigger_delay: ViReal64
   :var trigger_slope: 
   :vartype trigger_slope: :py:data:`TriggerSlope`
   :var trigger_source: 
   :vartype trigger_source: :py:data:`TriggerSource`
   :var waveform_coupling: 
   :vartype waveform_coupling: :py:data:`WaveformCoupling`
   :var waveform_points: 
   :vartype waveform_points: ViInt32
   :var waveform_rate: 
   :vartype waveform_rate: ViReal64


