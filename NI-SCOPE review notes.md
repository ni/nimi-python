#NI-SCOPE review notes for addons.

Everything listed here needs to be implemented.

##Buffer sizes

* configure_equalization_filter_coefficients
* get_equalization_filter_coefficients number_of_coefficients should be queried from attribute
* get_frequency_response is ivi dance

##Defaults

* cal_self_calibrate default None or 0 or maybe there's an enum value
* clear_waveform_measurement_stats default to NISCOPE_VAL_ALL_MEASUREMENTS
* configure_vertical offset 0, probe_attenuation 1, enabled True
* fetch_measurement timeout 5.0
* fetch_measurement_stats timeout 5.0
* read_measurement timeout 5.0
* __init__ id_query=False reset_device=False option_string=''
* configure_ref_levels(low 10.0, mid 50.0, high 90.0)
* configure_trigger_digital slope rising, holdoff 0.0, delay 0.0
* configure_trigger_edge level 0.0, slope rising, holdoff 0.0, delay 0.0
* configure_trigger_hysteresis(self, trigger_source, level, hysteresis, slope, trigger_coupling, holdoff, delay):
* configure_trigger_software 0.0 0.0
* configure_trigger_video enable_dc_restore False, line_number 1, holdoff 0.0, delay 0.0
* configure_trigger_window holdoff 0.0, delay 0.0
* export_signal signal_identifier:'None' (string)

##Enums

* add_waveform_processing shoudl have enum
* cal_self_calibrate needs enum
* clear_waveform_measurement_stats needs enum
* configure_vertical coupling is enum
* fetch_measurement scalar_meas_function
* fetch_measurement_stats scalar_meas_function
* read_measurement scalar_meas_function
* acquisition_status return enum
* configure_trigger_digital slope
* configure_trigger_edge slope, trigger_coupling
* configure_trigger_hysteresis(self, trigger_source, level, hysteresis, slope, trigger_coupling, holdoff, delay):
* configure_trigger_video signal_format, event, polarity, trigger_coupling
* configure_trigger_window window_mode, trigger_coupling
* export_signal signal
* send_software_trigger_edge which_trigger

##Other notes

* Make cal_self_calibrate name consistnet
* Keep configure_chan_characteristics
* fetch_measurement needs size mechanism python_code
* fetch_measurement_stats size mechanism python_code
* number_of_coefficients size mechanism python_code (from attribute)
* get_frequency_response parameters should be outputs
* In wiki guidelines specify
    * we do reset=false in init
    * When in doubt - don't include the function
* actual_meas_wfm_size private
* actual_num_waveforms private
* Make sure we aren't removing useful ext cal functions
* The following still need review, awaiting PR from Mark
    * 'Fetch'
    * 'FetchArrayMeasurement'
    * 'FetchBinary16'
    * 'FetchBinary32'
    * 'FetchBinary8'
    * 'FetchComplex'
    * 'FetchComplexBinary16'
    * 'Read'

##Remove

* configure_channel
* configure_clock - use export signal and reference clock attribute source
* configure_edge_trigger_source (obsolete)
* configure_tv_trigger_line_number
* configure_tv_trigger_source (obsolete)
* configure_trigger (use configure_trigger_...)
* configure_trigger_coupling
* configure_trigger_output use export signal
* fetch_waveform
* fetch_waveform_measurement
* get_channel_name
* get_error_message
* get_stream_endpoint_handle
* is_invalid_wfm_element
* read_waveform
* read_waveform_measurement
* sample_rate
* send_sw_trigger
* error_handler

