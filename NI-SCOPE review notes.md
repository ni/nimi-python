#NI-SCOPE review notes for addons.

Everything listed here still needs to be implemented.

##Enums

* add_waveform_processing should have enum
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

* The following still need review. PR to support them has been merged.
    * 'Fetch'
    * 'FetchArrayMeasurement'
    * 'Read'
* Add system tests for all touched functions

