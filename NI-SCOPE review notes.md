NI-SCOPE review notes for addons

Left it at configure_trigger_window, will continue

Buffer sizes
    * configure_equalization_filter_coefficients
    * get_equalization_filter_coefficients number_of_coefficients should be queried from attribute
    * get_frequency_response is ivi dance

Defaults
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

Enums
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

Other notes
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

Remove
    * check_attribute_vi_boolean and rest
    * is_device_ready
    * actual_record_length
    * adjust_sample_clock_relative_delay
    * adjust_sample_clock_relative_delay ALSO REMOVE FROM NI-FGEN
    * configure_acquisition
    * configure_acquisition_record
    * configure_channel
    * configure_clock - use export signal and reference clock attribute source
    * configure_edge_trigger_source (obsolete)
    * configure_tv_trigger_line_number
    * configure_tv_trigger_source (obsolete)
    * configure_trigger (use configure_trigger_...)
    * configure_trigger_coupling
    * configure_trigger_output use export signal



