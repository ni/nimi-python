# Changelog

* [Unreleased](#unreleased)
* [1.1.5](#115---2019-11-22)
* [1.1.4](#114---2019-11-19)
* [1.1.3](#113---2019-10-21)
* [1.1.2](#112---2019-06-06)
* [1.1.0](#110---2018-10-25)
* [1.0.1](#101---2018-10-17)
* [1.0.0](#100---2018-06-08)
* [0.9.0](#090---2018-05-22)
* [0.8.0](#080---2018-04-27)
* [0.7.0](#070---2018-02-20)
* [0.6.0](#060---2017-12-20)
* [0.5.0](#050---2017-11-27)
* [0.4.0](#040---2017-11-07)
* [0.3.0](#030---2017-10-13)
* [0.2.0](#020---2017-09-20)
* [0.1.0](#010---2017-09-01)

All notable changes to this project will be documented in this file.

## [Unreleased]
* ### ALL
    * #### Added
        * Zip file per driver for all examples and any helper files
        * Link to zip file on examples documentation
        * Support for Python 3.8
    * #### Changed
        * `import_attribute_configuration_buffer()` now accepts `list` of numbers that are integers less than 255, `array.array('b')`, `bytes`, `bytearray` for configuration buffer - [#1013](https://github.com/ni/nimi-python/issues/1013)
        * `export_attribute_configuration_buffer()` now returns `bytes` as the buffer type - [#1013](https://github.com/ni/nimi-python/issues/1013)
    * #### Removed
        * Python 2.7 support - [Python Software Foundation version status](https://devguide.python.org/#status-of-python-branches)
        * Python 3.4 support - [Python Software Foundation PEP 429](https://www.python.org/dev/peps/pep-0429/)
* ### NI-DMM
    * #### Added
    * #### Changed
    * #### Removed
* ### NI-ModInst
    * #### Added
    * #### Changed
    * #### Removed
* ### NI-Switch
    * #### Added
    * #### Changed
    * #### Removed
* ### NI-DCPower
    * #### Added
    * #### Changed
    * #### Removed
* ### NI-FGEN
    * #### Added
    * #### Changed
    * #### Removed
* ### NI-SCOPE
    * #### Added
    * #### Changed
    * #### Removed
* ### NI Switch Executive
    * #### Added
    * #### Changed
    * #### Removed
* ### NI-Digital Pattern Driver
    * #### Added
        * `conditional_jump_triggers` and `pattern_opcode_events` repeated capabilities - [#1191](https://github.com/ni/nimi-python/issues/1191), [#1192](https://github.com/ni/nimi-python/issues/1192)
    * #### Changed
        * `write_source_waveform_site_unique()` now supports `numpy.array` and `list` as site waveform types
    * #### Removed
        * Removed redundant (redundant because corresponding properties can be used instead) API methods - [#1065](https://github.com/ni/nimi-python/issues/1065)
* ### NI-TClk
    * #### Added
    * #### Changed
    * #### Removed
    
    
## 1.1.5 - 2019-11-22
* ### ALL
    * #### Changed
        * Fix #1140: Linux support was accidentally broken.
        * Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot.


## 1.1.4 - 2019-11-19
* ### ALL
    * #### Added
        * Support for Python 3.8
        * `ViUInt8` is now a valid type in APIs
* ### NI-Digital Pattern Driver
    * #### Added
        * `fetch_capture_waveform()` - returns dictionary { site: data, site: data, ... }
        * `write_source_waveform_site_unique()` - takes waveform_name and dictionary { site: data, site: data, ... }
        * `pins` is now a valid repeated capability
    * #### Changed
        * Fix get/set properties - [#1062](https://github.com/ni/nimi-python/issues/1062)
        * Removed array-size parameter from apply_tdr_offsets() and write_source_waveform_broadcast_u32() methods - [#1070](https://github.com/ni/nimi-python/issues/1070)
        * Renamed `write_source_waveform_broadcast_u32()` to `write_source_waveform_broadcast()`
        * `get_pin_results_pin_information()` - returns namedtuple `PinInfo(pin_indexes, site_numbers, channel_indexes)`
* ### NI Switch Executive
    * #### Changed
        * Version updated to 1.1.4 to match other released nimi-python modules


## 1.1.3 - 2019-10-21
* ### ALL
    * #### Changed
        * The development status in `setup.py` will be based on the module version:
            * version >= 1.0
                * .devN or .aN - Alpha
                * .bN, .cN or .rcN - Beta
                * \<nothing\> or .postN - Stable
            * version < 1.0 and version >= 0.5 - Beta
            * version < 0.5 - Alpha
        * Improved installation instructions by not putting a version to pin to. This is confusing in master (what read the docs shows by default) since that version doesn't exist yet.
* ### NI-DCPower
    * #### Changed
        * Fix type of `sequence_step_delta_time_enabled ` property - [#1015](https://github.com/ni/nimi-python/issues/1015)
* ### NI-FGEN
    * #### Removed
        * `configure_custom_fir_filter_coefficients()` - [#996](https://github.com/ni/nimi-python/issues/996) - Should have been removed as part of - [#891](https://github.com/ni/nimi-python/issues/891)
* ### NI-SCOPE
    * #### Added
        * `cable_sense_signal_enable`, `cable_sense_voltage`, `cable_sense_mode` properties and associated enum
        * `enabled_channels`, `product_code` properties
        * `glitch_condition`, `glitch_polarity`, `glitch_width` properties and associated enums
        * `runt_high_threshold`, `runt_low_threshold`, `runt_polarity`, `runt_condition`, `runt_time_high_limit`, `runt_time_low_limit` properties and associated enums
        * `width_condition`, `width_high_threshold`, `width_low_threshold`, `width_polarity` properties and associated enums
* ### NI Switch Executive
    * #### Changed
        * Update to 1.0 - now ready for production use
* ### NI-Digital Pattern Driver
    * #### Added
        * Initial support
        * Very basic at this point and subject to change
        * Looking for any testing and/or feedback
        * `get_channel_name_from_string()`
    * #### Changed
        *  New enums:

           | Enum name                  | Where used                                                                       |
           |----------------------------|----------------------------------------------------------------------------------|
           | `DigitalEdge`              | `digital_edge_conditional_jump_trigger_edge`, `digital_edge_start_trigger_edge`  |
           | `ApertureTimeUnits`        | `ppmu_aperture_time_units`, `ppmu_configure_aperture_time(units)`                |
           | `PPMUOutputFunction`       | `ppmu_output_function`                                                           |
           | `SelectedFunction`         | `selected_function`                                                              |
           | `TDREndpointTermination`   | `tdr_endpoint_termination`                                                       |
           | `Signal`                   | `export_signal(signal)`                                                          |
        * **[Source Breaker]** No longer return the "actual size" from functions that use 'ivi-dance-with-a-twist'. This only affects `nidigital`.

    * #### Removed
        * Should be private - `get_session_state()`, `get_desired_attribute_*()`, `ppmu_measure_cached()`, `read_static_cached()`, `configure_ref_clock()`, `disable()`, 
            `get_number_of_vectors()`, `get_pattern_file_path()`, `get_pin_type()`, `get_time_set_compare_edges()`, `get_time_set_drive_edges()`,
            `is_pattern_file_modified_since_load()`, `load_levels_internal()`, `load_pattern_internal()`, `load_timing_internal()`, `uncommit()`
        * Need to determine how to generate this function - `fetch_capture_waveform_u32()`
* ### NI-TClk
    * #### Added
        * Initial support


## 1.1.2 - 2019-06-06
* ### ALL
    * #### Changed
        * Switched to slightly different metadata format - Actual `True`/`False` instead of strings
        * New internal process for generating metadata
* ### NI-FGEN
    * #### Changed
        * Enum values for `HardwareState` were incorrect - fix to match niFgen.h
* ### NI-SCOPE
    * #### Changed
        * Fixed enum values for `TIME_HISTOGRAM_MEAN_PLUS_STDEV`, `TIME_HISTOGRAM_MEAN_PLUS_2_STDEV`, `HF_REJECT` and `LF_REJECT`


## 1.1.0 - 2018-10-25
* ### ALL
    * #### Changed
        * Updated generated metadata
        * Updated "Driver Version Tested Against"
        * Update visatype definitions to work on Linux as well as Windows - [#911](https://github.com/ni/nimi-python/issues/911)
* ### NI-DMM
    * #### Added
        * import_attribute_configuration_file function
        * export_attribute_configuration_file function
        * import_attribute_configuration_buffer function
        * import_attribute_configuration_buffer function
* ### NI-DCPower
    * #### Added
        * import_attribute_configuration_file function
        * export_attribute_configuration_file function
        * import_attribute_configuration_buffer function
        * import_attribute_configuration_buffer function
* ### NI-SCOPE
    * #### Added
        * import_attribute_configuration_file function
        * export_attribute_configuration_file function
        * import_attribute_configuration_buffer function
        * import_attribute_configuration_buffer function


## 1.0.1 - 2018-10-17
* ### ALL
    * #### Added
        * Support for Python 3.7 - [#895](https://github.com/ni/nimi-python/issues/895)
        * \_\_version\_\_ for all drivers - [#928](https://github.com/ni/nimi-python/issues/928)
    * #### Changed
        * No longer globally set warnings filter for `DriverWarning` - if you want all warnings from the driver, you will need to set `warnings.filterwarnings("always", category=<driver>.DriverWarning)` in your code
        * Fix \_\_repr\_\_ for niscope.WaveformInfo - [#920](https://github.com/ni/nimi-python/issues/920)
* ### NI-SCOPE
    * #### Changed
        * Format of output of wavefrom_info.__str__()
* ### NI Switch Executive
    * #### Added
        * Initial Release


## 1.0.0 - 2018-06-08
* ### ALL
    * #### Removed
        * Explicitly disallow using a repeated capability on Session. `session[0].vertical_range = 1.0` will no longer work. Instead use `session.channels[0].vertical_range = 1.0` - [#853](https://github.com/ni/nimi-python/issues/853)
* ### NI-DMM
    * #### Changed
        * Fixed name `freq_voltage_autorange` became `freq_voltage_auto_range`
    * #### Removed
        * `configure_ac_bandwidth()` - [#875](https://github.com/ni/nimi-python/issues/875)
        * `configure_open_cable_comp_values()` - [#875](https://github.com/ni/nimi-python/issues/875)
        * `configure_power_line_frequency()` - [#875](https://github.com/ni/nimi-python/issues/875)
        * `configure_short_cable_comp_values()` - [#875](https://github.com/ni/nimi-python/issues/875)
        * `get_aperture_time_info()` - [#875](https://github.com/ni/nimi-python/issues/875)
        * `get_auto_range_value()` - [#875](https://github.com/ni/nimi-python/issues/875)
        * `get_measurement_period()` - [#875](https://github.com/ni/nimi-python/issues/875)
        * `latency` - [#875](https://github.com/ni/nimi-python/issues/875)
        * `shunt_value` - [#875](https://github.com/ni/nimi-python/issues/875)
        * `meas_dest_slope` - [#875](https://github.com/ni/nimi-python/issues/875)
        * `sample_trigger_slope` - [#875](https://github.com/ni/nimi-python/issues/875)
        * `trigger_slope` - [#875](https://github.com/ni/nimi-python/issues/875)
* ### NI-ModInst
    * #### Changed
        * Double close will now allow NI-ModInst to return error
* ### NI-Switch
    * #### Removed
        * `cabled_module_scan_advanced_bus` - [#881](https://github.com/ni/nimi-python/issues/881)
        * `cabled_module_trigger_bus` - [#881](https://github.com/ni/nimi-python/issues/881)
        * `master_slave_scan_advanced_bus` - [#881](https://github.com/ni/nimi-python/issues/881)
        * `master_slave_trigger_bus` - [#881](https://github.com/ni/nimi-python/issues/881)
        * `parsed_scan_list` - [#881](https://github.com/ni/nimi-python/issues/881)
        * `trigger_mode` - [#881](https://github.com/ni/nimi-python/issues/881)
        * `scan_advanced_polarity` - [#881](https://github.com/ni/nimi-python/issues/881)
        * `trigger_input_polarity` - [#881](https://github.com/ni/nimi-python/issues/881)
        * `configure_scan_list()` - [#881](https://github.com/ni/nimi-python/issues/881)
        * `configure_scan_trigger()` - [#881](https://github.com/ni/nimi-python/issues/881)
        * `route_trigger_input()` - [#881](https://github.com/ni/nimi-python/issues/881)
        * `set_continuous_scan()` - [#881](https://github.com/ni/nimi-python/issues/881)
* ### NI-DCPower
    * #### Removed
        * Remove trigger configuration methods, use attributes instead [#860](https://github.com/ni/nimi-python/issues/860)
            * `configure_digital_edge_measure_trigger()` - use `session.digital_edge_measure_trigger_edge` & `session.digital_edge_measure_trigger_input_terminal`
            * `configure_digital_edge_pulse_trigger()` - use `session.digital_edge_pulse_trigger_edge` & `session.digital_edge_pulse_trigger_input_terminal`
            * `configure_digital_edge_sequence_advance_trigger()` - use `session.digital_edge_sequence_advance_trigger_edge` & `session.digital_edge_sequence_advance_trigger_input_terminal`
            * `configure_digital_edge_source_trigger()` - use `session.digital_edge_source_trigger_edge` & `session.digital_edge_source_trigger_input_terminal`
            * `configure_digital_edge_start_trigger()` - use `session.digital_edge_start_trigger_edge` & `session.digital_edge_start_trigger_input_terminal`
        * Remove polarity attributes for triggers that are PXI backplane only (only support rising edge) [#860](https://github.com/ni/nimi-python/issues/860)
            * `digital_edge_measure_trigger_edge`
            * `digital_edge_pulse_trigger_edge`
            * `digital_edge_sequence_advance_trigger_edge`
            * `digital_edge_source_trigger_edge`
            * `digital_edge_start_trigger_edge`
* ### NI-FGEN
    * #### Changed
        * `num_channels` attribute renamed to `channel_count` - now consistent with other drivers
        * `send_software_edge_trigger()` no longer takes any parameters.
            * To send a start software trigger, call it on the session directly:
                    ``` python
                    session.send_software_edge_trigger()
                    ```
            * To send a script software trigger, call it on the script triggers container:
                    ``` python
                    session.script_triggers[1].send_software_edge_trigger()
                    ```
    * #### Removed
        * Remove trigger configuration methods, use attributes instead [#860](https://github.com/ni/nimi-python/issues/860)
            * `configure_digital_edge_script_trigger()` - use `session.digital_edge_script_trigger_source` & `session.digital_edge_script_trigger_edge`
            * `configure_digital_level_script_trigger()` - use `session.digital_level_script_trigger_source` & `session.digital_level_script_trigger_active_level`
            * `configure_digital_edge_start_trigger()` - use `session.digital_edge_start_trigger_source` & `session.digital_edge_start_trigger_edge`
        * Removed `get_fir_filter_coefficients()` - [#535](https://github.com/ni/nimi-python/issues/535), [#596](https://github.com/ni/nimi-python/issues/596)
* ### NI-SCOPE
    * #### Added
        * `niscope_fetch_forever.py` example
    * #### Removed
        * Removed default value for `level` parameter on `configure_trigger_edge()`
            * parameter list is now
                ``` python
                configure_trigger_edge(self, trigger_source, level, trigger_coupling, slope=enums.TriggerSlope.POSITIVE, holdoff=datetime.timedelta(seconds=0.0), delay=datetime.timedelta(seconds=0.0))
                ```
        * Removed default values for `level` and `hysteresis` parameters on `configure_trigger_hysteresis()`
            * parameter list is now
                ``` python
                configure_trigger_hysteresis(self, trigger_source, level, hysteresis, trigger_coupling, slope=enums.TriggerSlope.POSITIVE, holdoff=datetime.timedelta(seconds=0.0), delay=datetime.timedelta(seconds=0.0))
                ```

## 0.9.0 - 2018-05-22
* ### ALL
    * #### Added
        * Add `session.lock()` and `session.unlock()` to all drivers except nimodinst - [#846](https://github.com/ni/nimi-python/issues/846)
        * `session.lock()` returns a context manager for managing locks - [#846](https://github.com/ni/nimi-python/issues/846)
        * Fix thread-safety issues by using IVI session lock where aplicable
    * #### Changed
        * `SelfTestError` now inherits from `<driver>.Error` rather than `Exception` - [#830](https://github.com/ni/nimi-python/issues/830)
        * Warning class name changed to `<driver>.DriverWarning` for all drivers - [#658](https://github.com/ni/nimi-python/issues/658)
    * #### Removed
        * IVI properties as applicable - some were already removed from some drivers [#824](https://github.com/ni/nimi-python/issues/824)
            * `engine_major_version`
            * `engine_minor_version`
            * `engine_revision`
            * `primary_error`
            * `secondary_error`
            * `error_elaboration`
            * `io_session_type`
            * `io_session` / `visa_rm_session`
            * `group_capabilities`
            * `interchange_check`
            * `range_check`
            * `record_coercions`
            * `specific_driver_class_spec_major_version`
            * `specific_driver_class_spec_minor_version`
            * `query_instrument_status`
            * `cache`
            * `specific_driver_prefix`
* ### NI-DCPower
    * #### Removed
        * `export_signal()` - [#828](https://github.com/ni/nimi-python/issues/828)
        * `active_advanced_sequence` [#832](https://github.com/ni/nimi-python/issues/832)
        * `active_advanced_sequence_step` [#832](https://github.com/ni/nimi-python/issues/832)
        * Default value for trigger parameter on `send_software_edge_trigger()` [#832](https://github.com/ni/nimi-python/issues/832)
* ### NI-FGEN
    * #### Changed
        * Some functions missed setting repeated capabilities, leaving these as parameters instead of using the repeated capabilites object.
            * `session.configure_digital_edge_script_trigger('ScriptTrigger0', source, ...)` becomes `session.script_triggers[0].configure_digital_edge_script_trigger(source, ...)`
            * `session.configure_digital_level_script_trigger('ScriptTrigger0', source, ...)` becomes `session.script_triggers[0].configure_digital_level_script_trigger(source, ...)`
        * Combined named and un-named waveform methods into one [#862](https://github.com/ni/nimi-python/issues/862)
            * `set_waveform_next_write_position()` and `set_named_waveform_next_write_position()` becomes `set_next_write_position()`
            * `clear_arb_waveform()` and `delete_named_waveform()` becomes `delete_waveform()`
    * #### Removed
        * `export_signal()` - [#828](https://github.com/ni/nimi-python/issues/828)
        * `osp_fir_filter_interpolation` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_fir_filter_gaussian_bt` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_fir_filter_flat_passband` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_fir_filter_enabled` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_enabled` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_data_processing_mode` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_compensate_for_filter_group_delay` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_cic_filter_interpolation` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_cic_filter_gain` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_cic_filter_enabled` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_carrier_phase_q` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_carrier_phase_i` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_carrier_frequency` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_carrier_enabled` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_pre_filter_offset_q` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_pre_filter_offset_i` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_pre_filter_gain_q` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_pre_filter_gain_i` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_overflow_status` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_overflow_error_reporting` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_mode` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_frequency_shift` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_fir_filter_type` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_fir_filter_root_raised_cosine_alpha` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `osp_fir_filter_raised_cosine_alpha` - [#864](https://github.com/ni/nimi-python/issues/864)
        * `ready_for_start_event_level_active_level` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `started_event_level_active_level` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `done_event_level_active_level` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `started_event_output_behavior` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `done_event_output_behavior` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `marker_event_output_behavior` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `marker_event_pulse_polarity` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `started_event_pulse_polarity` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `done_event_pulse_polarity` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `started_event_pulse_width` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `done_event_pulse_width` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `marker_event_pulse_width` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `started_event_pulse_width_units` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `done_event_pulse_width_units` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `marker_event_pulse_width_units` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `marker_event_toggle_initial_state` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `marker_event_live_status` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `ready_for_start_event_live_status` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `marker_event_latched_status` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `done_event_latched_status` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `started_event_latched_status` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `marker_event_delay` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `started_event_delay` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `done_event_delay` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `marker_event_delay_units` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `started_event_delay_units` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `done_event_delay_units` - [#859](https://github.com/ni/nimi-python/issues/859)
        * `direct_dma_enabled` - [#858](https://github.com/ni/nimi-python/issues/858)
        * `direct_dma_windowaddress` - [#858](https://github.com/ni/nimi-python/issues/858)
        * `direct_dma_window_size`  [#858](https://github.com/ni/nimi-python/issues/858)
        * `gain_dac_value` - [#88](https://github.com/ni/nimi-python/issues/858)
        * `offset_dac_vaue` - [#858](https://github.com/ni/nimi-python/issues/858)
        * `id_query_respone` - [#858](https://github.com/ni/nimi-python/issues/858)
        * `oscillator_freq_ac_value` - [#858](https://github.com/ni/nimi-python/issues/858)
        * `oscillator_phase_dac_vale` - [#858](https://github.com/ni/nimi-python/issues/858)
        * `post_amplifier_attenuatio` - [#858](https://github.com/ni/nimi-python/issues/858)
        * `pre_amplifier_attenuation` - [#858](https://github.com/ni/nimi-python/issues/858)
        * `p2p_endpoint_fullness_strt_trigger_level` - [#858](https://github.com/ni/nimi-python/issues/858)
        * `pci_dma_optimizations_enabled` - [#858](ttps://github.com/ni/nimi-python/issues/858)
        * `sample_clock_absolute_delay`- [#858](https://github.com/ni/nimi-python/issues/858)
        * `synchronization` - [#858](ttps://github.com/ni/nimi-python/issues/858)
        * `sync_duty_cycl_high` - [#858](https://github.com/ni/nimi-python/issues/858)
        * `sync_out_output_terinal` - [#858](https://github.com/ni/nimi-python/issues/858)
        * `trigger_source` - [#858](https://github.com/ni/nimi-python/issues/858)
        * `video_wavefor_type` - [#858](https://github.com/ni/nimi-python/issues/858)
* ### NI-SCOPE
    * #### Removed
        * Properties removed
            * `stream_relative_to` [#825](https://github.com/ni/nimi-python/issues/825)
            * `oscillator_phase_dac_value` [#825](https://github.com/ni/nimi-python/issues/825)
            * `mux_mode_register` [#825](https://github.com/ni/nimi-python/issues/825)
            * `ddc_center_frequency` [#823](https://github.com/ni/nimi-python/issues/823)
            * `ddc_data_processing_mode` [#823](https://github.com/ni/nimi-python/issues/823)
            * `ddc_enabled` [#823](https://github.com/ni/nimi-python/issues/823)
            * `ddc_frequency_translation_enabled` [#823](https://github.com/ni/nimi-python/issues/823)
            * `ddc_frequency_translation_phase_i` [#823](https://github.com/ni/nimi-python/issues/823)
            * `ddc_frequency_translation_phase_q` [#823](https://github.com/ni/nimi-python/issues/823)
            * `ddc_q_source` [#823](https://github.com/ni/nimi-python/issues/823)
            * `digital_gain` [#823](https://github.com/ni/nimi-python/issues/823)
            * `digital_offset` [#823](https://github.com/ni/nimi-python/issues/823)
            * `dither_enabled` [#823](https://github.com/ni/nimi-python/issues/823)
            * `fetch_interleaved_iq_data` [#823](https://github.com/ni/nimi-python/issues/823)
            * `fractional_resample_enabled` [#823](https://github.com/ni/nimi-python/issues/823)
            * `overflow_error_reporting` [#823](https://github.com/ni/nimi-python/issues/823)
            * `adjust_pretrigger_samples_5102` [#822](https://github.com/ni/nimi-python/issues/822)
            * `five_v_out_output_terminal` [#822](https://github.com/ni/nimi-python/issues/822)
            * `clock_sync_pulse_source` [#822](https://github.com/ni/nimi-python/issues/822)
            * `device_number` [#822](https://github.com/ni/nimi-python/issues/822)
            * `fetch_interleaved_data` [#822](https://github.com/ni/nimi-python/issues/822)
            * `trigger_from_pfi_delay` [#822](https://github.com/ni/nimi-python/issues/822)
            * `trigger_from_rtsi_delay` [#822](https://github.com/ni/nimi-python/issues/822)
            * `trigger_from_star_delay` [#822](https://github.com/ni/nimi-python/issues/822)
            * `trigger_to_pfi_delay` [#822](https://github.com/ni/nimi-python/issues/822)
            * `trigger_to_rtsi_delay` [#822](https://github.com/ni/nimi-python/issues/822)
            * `trigger_to_star_delay` [#822](https://github.com/ni/nimi-python/issues/822)
            * `slave_trigger_delay` [#822](https://github.com/ni/nimi-python/issues/822)
        * Methods removed
            * `get_frequency_response()` [#823](https://github.com/ni/nimi-python/issues/823)
            * `export_signal()` - [#828](https://github.com/ni/nimi-python/issues/828)
* ### NI-ModInst
    * #### Changed
        * Indexing on `nimodinst.Session` is no longer allowed
            * `session[0].device_name` becomes `session.devices[0].device_name`
            * This is to be consistent with other drivers

## 0.8.0 - 2018-04-27
* ### ALL
    * #### Changed
        * All exceptions raised by the Python bindings inherit from `<driver>.Error`
        * Exception type formerly known as `<driver>.Error` is now known as `<driver>.DriverError`
            * This encapsulates any error that is returned by the underlying driver
        * All timeout parameters can now also take a simple number in seconds. `timeout=datetime.timedelta(milliseconds=100)` and `timeout=0.1` are identical. [#796](https://github.com/ni/nimi-python/issues/796)
* ### NI-DMM
    * #### Changed
        * Enum values that start with an underscore + digit have been renamed
            * `Function._2_WIRE_RES` --> `Function.TWO_WIRE_RES`
            * `Function._4_WIRE_RES` --> `Function.FOUR_WIRE_RES`
            * `ThermistorType._44004` --> `ThermistorType.THERMISTOR_44004`
            * `ThermistorType._44006` --> `ThermistorType.THERMISTOR_44006`
            * `ThermistorType._44007` --> `ThermistorType.THERMISTOR_44007`
            * `TransducerType._2_WIRE_RTD` --> `TransducerType.TWO_WIRE_RTD`
            * `TransducerType._4_WIRE_RTD` --> `TransducerType.FOUR_WIRE_RTD`
        * `Session.get_ext_cal_recommended_interval()` now returns a `datetime.timedelta` for the interval [#794](https://github.com/ni/nimi-python/issues/794)
* ### NI-DCPower
    * #### Changed
        * `Session.fetch_multiple()` and `Session.measure_multiple()` now return list of named tuples instead of multiple arrays. See [fetch_multiple](http://nimi-python.readthedocs.io/en/master/nidcpower/functions.html#nidcpower.Session.fetch_multiple) and [measure_multiple](http://nimi-python.readthedocs.io/en/master/nidcpower/functions.html#nidcpower.Session.measure_multiple)
        * `Session.cal_self_calibration()` renamed to `Session.self_cal()` to match other drivers - issue [#615](https://github.com/ni/nimi-python/issues/615)
        * `Session.set_sequence()` values parameter no longer has a default value and must be passed in. Parameter order has changed as a result of this - issue [#797](https://github.com/ni/nimi-python/issues/797)
        * Session constructor channel parameter can now use any channel format that repeated capabilities can use [#807](https://github.com/ni/nimi-python/issues/807)
        * `Session.get_ext_cal_recommended_interval()` now returns a `datetime.timedelta` for the interval [#794](https://github.com/ni/nimi-python/issues/794)
    * #### Removed
        * Advanced Sequence functions - until [#504](https://github.com/ni/nimi-python/issues/504) can be fixed in a proper way
            * `create_advanced_sequence()`
            * `create_advanced_sequence_step()`
            * `delete_advanced_sequence()`
* ### NI-FGEN
    * #### Changed
        * `Session.export_signal()` signal_identifier now has a default of "". This moves it to the end of the parameter list [#801](https://github.com/ni/nimi-python/issues/801)
        * `Session.get_ext_cal_recommended_interval()` now returns a `datetime.timedelta` for the interval [#794](https://github.com/ni/nimi-python/issues/794)
    * #### Removed
        * `Session.cal_adc_input` attribute and `Session.enums.CalADCInput` enum - External Cal not supported in Python
        * Session constructor channel parameter can now use any channel format that repeated capabilities can use [#807](https://github.com/ni/nimi-python/issues/807)
* ### NI-SCOPE
    * #### Changed
        * `Session.fetch()`, `Session.read()` and `Session.fetch_into()` updated
            * Takes additional parameters that modify fetch behavior
            * Add resulting record as part of the waveform info
            * Channel name and record number added to waveform info
            * See documentation for [fetch](http://nimi-python.readthedocs.io/en/master/niscope/functions.html#niscope.Session.fetch),
                [read](http://nimi-python.readthedocs.io/en/master/niscope/functions.html#niscope.Session.read),
                and [fetch_into](http://nimi-python.readthedocs.io/en/master/niscope/functions.html#niscope.Session.fetch_into) for more details.
        * Rename `wfm` parameter to `waveform` in `fetch()` and `fetch_into()`
        * Enum values and attribute names that start with an underscore + digit have been renamed
            * `Session._5102_adjust_pretrigger_samples` --> `Session.adjust_pretrigger_samples_5102`
            * `Session._5v_out_output_terminal` --> `Session.five_v_out_output_terminal`
            * `ExportableSignals._5V_OUT` --> `ExportableSignals.FIVE_V_OUT`
            * `FlexFIRAntialiasFilterType._48_TAP_STANDARD` --> `FlexFIRAntialiasFilterType.FOURTYEIGHT_TAP_STANDARD`
            * `FlexFIRAntialiasFilterType._48_TAP_HANNING` --> `FlexFIRAntialiasFilterType.FOURTYEIGHT_TAP_HANNING`
            * `FlexFIRAntialiasFilterType._16_TAP_HANNING` --> `FlexFIRAntialiasFilterType.SIXTEEN_TAP_HANNING`
            * `FlexFIRAntialiasFilterType._8_TAP_HANNING` --> `FlexFIRAntialiasFilterType.EIGHT_TAP_HANNING`
            * `VideoSignalFormat._480I_59_94_FIELDS_PER_SECOND` --> `VideoSignalFormat.VIDEO_480I_59_94_FIELDS_PER_SECOND`
            * `VideoSignalFormat._480I_60_FIELDS_PER_SECOND` --> `VideoSignalFormat.VIDEO_480I_60_FIELDS_PER_SECOND`
            * `VideoSignalFormat._480P_59_94_FRAMES_PER_SECOND` --> `VideoSignalFormat.VIDEO_480P_59_94_FRAMES_PER_SECOND`
            * `VideoSignalFormat._480P_60_FRAMES_PER_SECOND` --> `VideoSignalFormat.VIDEO_480P_60_FRAMES_PER_SECOND`
            * `VideoSignalFormat._576I_50_FIELDS_PER_SECOND` --> `VideoSignalFormat.VIDEO_576I_50_FIELDS_PER_SECOND`
            * `VideoSignalFormat._576P_50_FRAMES_PER_SECOND` --> `VideoSignalFormat.VIDEO_576P_50_FRAMES_PER_SECOND`
            * `VideoSignalFormat._720P_50_FRAMES_PER_SECOND` --> `VideoSignalFormat.VIDEO_720P_50_FRAMES_PER_SECOND`
            * `VideoSignalFormat._720P_59_94_FRAMES_PER_SECOND` --> `VideoSignalFormat.VIDEO_720P_59_94_FRAMES_PER_SECOND`
            * `VideoSignalFormat._720P_60_FRAMES_PER_SECOND` --> `VideoSignalFormat.VIDEO_720P_60_FRAMES_PER_SECOND`
            * `VideoSignalFormat._1080I_50_FIELDS_PER_SECOND` --> `VideoSignalFormat.VIDEO_1080I_50_FIELDS_PER_SECOND`
            * `VideoSignalFormat._1080I_59_94_FIELDS_PER_SECOND` --> `VideoSignalFormat.VIDEO_1080I_59_94_FIELDS_PER_SECOND`
            * `VideoSignalFormat._1080I_60_FIELDS_PER_SECOND` --> `VideoSignalFormat.VIDEO_1080I_60_FIELDS_PER_SECOND`
            * `VideoSignalFormat._1080P_24_FRAMES_PER_SECOND` --> `VideoSignalFormat.VIDEO_1080P_24_FRAMES_PER_SECOND`
        * `Session.cal_self_calibration()` renamed to `Session.self_cal()` to match other drivers - issue [#615](https://github.com/ni/nimi-python/issues/615)
    * #### Removed
        * Following properties are now removed (use parameters to fetch calls):
            * `fetch_relative_to`
            * `fetch_offset`
            * `fetch_record_number`
            * `fetch_num_records`
        * Removed `number_of_coefficients` parameter from `get_equalization_filter_coefficients()`
        * Removed Measurement Library waveform methods and properties - issue [#809](https://github.com/ni/nimi-python/issues/809)
            * `actual_meas_wfm_size()`
            * `add_waveform_processing()`
            * `clear_waveform_processing()`
            * `fetch_array_measurement()`
            * `clear_waveform_measurement_stats()`
            * `fetch_measurement()`
            * `fetch_measurement_stats()`
            * `read_measurement()`
            * `configure_ref_levels()`
            * `meas_ref_level_units`
            * `meas_other_channel`
            * `meas_hysteresis_percent`
            * `meas_last_acq_histogram_size`
            * `meas_voltage_histogram_size`
            * `meas_voltage_histogram_low_volts`
            * `meas_voltage_histogram_high_volts`
            * `meas_time_histogram_size`
            * `meas_time_histogram_low_volts`
            * `meas_time_histogram_high_volts`
            * `meas_time_histogram_low_time`
            * `meas_time_histogram_high_time`
            * `meas_polynomial_interpolation_order`
            * `meas_interpolation_sampling_factor`
            * `meas_filter_cutoff_freq`
            * `meas_filter_center_freq`
            * `meas_filter_ripple`
            * `meas_filter_transient_waveform_percent`
            * `meas_filter_type`
            * `meas_filter_order`
            * `meas_filter_taps`
            * `meas_chan_low_ref_level`
            * `meas_chan_mid_ref_level`
            * `meas_chan_high_ref_level`
            * `meas_filter_width`
            * `meas_fir_filter_window`
            * `meas_array_gain`
            * `meas_array_offset`
            * `meas_percentage_method`
            * `fetch_meas_num_samples`

## 0.7.0 - 2018-02-20
* ### ALL
    * #### Changed
        * Option string can now be a python dictionary instead of a string. (Fix [#661](https://github.com/ni/nimi-python/issues/661))
            * Key/Value pairs approporiate for desired behavior
                ``` python
                session = nidmm.Session('Dev1', False, {'simulate': True, 'driver_setup': {'Model': '4071', 'BoardType': 'PXI'}})
                ```
        * Repeated capabilities are handled differently. See [#737](https://github.com/ni/nimi-python/issues/737) for discussion
        * All function parameters or attributes that represent time now use `datetime.timedelta()`. See [#659](https://github.com/ni/nimi-python/issues/659) for discussion
        * All functions that return calibration dates now return `datetime.datetime()`. See [#659](https://github.com/ni/nimi-python/issues/659) for discussion
* ### NI-DMM
    * #### Changed
        * `nidmm.Session()` no longer takes id_query parameter (Fix [#670](https://github.com/ni/nimi-python/issues/670))
        * The following functions timeout or delay parameter now is required to be a `datetime.timedelta()` object:
            * `configure_multi_point()`
            * `configure_trigger()`
            * `fetch()`
            * `fetch_multi_point()`
            * `fetch_waveform()`
            * `read()`
            * `read_multi_point()`
            * `read_waveform()`
        * The following functions return a `datetime.datetime()` object representing the date and time
            * `get_cal_date_and_time()`
        * Metadata updated to NI-DMM 17.5
    * #### Removed
        * Removed these enums and disconnected them from the associated attribute (Fix [#666](https://github.com/ni/nimi-python/issues/666))
            * `DCBias` - `DC_BIAS`
            * `OffsetCompensatedOhms` - `OFFSET_COMP_OHMS`
* ### NI-Switch
    * #### Changed
        * The following functions timeout, delay or holdoff parameters now is required to be a `datetime.timedelta()` object:
            * `configure_scan_trigger()`
            * `wait_for_debounce()`
            * `wait_for_scan_complete()`
* ### NI-DCPower
    * #### Added
        * `channel` repeated capability - See [#737](https://github.com/ni/nimi-python/issues/737) for discussion
    * #### Changed
        * Metadata updated to NI-DCPower 17.6.1
        * The following functions timeout parameter now is required to be a `datetime.timedelta()` object:
            * `fetch_multiple()`
            * `wait_for_event()`
        * The following functions return a `datetime.datetime()` object representing the date and time
            * `get_ext_cal_last_date_and_time()`
            * `get_self_cal_last_date_and_time()`
    * #### Removed
        * Removed these enums and disconnected them from the associated attribute (Fix [#666](https://github.com/ni/nimi-python/issues/666))
            * `CurrentLimitAutorange` - `CURRENT_LIMIT_AUTORANGE`
            * `CurrentLevelAutorange` - `CURRENT_LEVEL_AUTORANGE`
            * `VoltageLevelAutorange` - `VOLTAGE_LEVEL_AUTORANGE`
            * `VoltageLimitAutorange` - `VOLTAGE_LIMIT_AUTORANGE`
* ### NI-FGEN
    * #### Changed
        * Repeated capablilites - See [#737](https://github.com/ni/nimi-python/issues/737) for discussion:
            * `channel` repeated capability
            * `markers` repeated capability
            * `script_triggers` repeated capability
        * The following functions timeout parameter now is required to be a `datetime.timedelta()` object:
            * `adjust_sample_clock_relative_delay()`
            * `wait_until_done()`
        * The following functions return a `datetime.datetime()` object representing the date and time
            * `get_ext_cal_last_date_and_time()`
            * `get_self_cal_last_date_and_time()`
* ### NI-SCOPE
    * #### Added
        * Repeated capablilites - See [#737](https://github.com/ni/nimi-python/issues/737) for discussion:
            * `channel` repeated capability
    * #### Changed
        * `niscope.Session()` no longer takes id_query parameter (Fix [#670](https://github.com/ni/nimi-python/issues/670))
        * The following functions timeout, delay or holdoff parameters now is required to be a `datetime.timedelta()` object:
            * `configure_trigger_digital()`
            * `configure_trigger_edge()`
            * `configure_trigger_hysteresis()`
            * `configure_trigger_software()`
            * `configure_trigger_video()`
            * `configure_trigger_window()`
            * `fetch()`
            * `fetch_measurement_stats()`
            * `read()`
    * #### Removed
        * Removed these enums and disconnected them from the associated attribute (Fix [#666](https://github.com/ni/nimi-python/issues/666))
            * `BoolEnableDisable` - `P2P_ENABLED`, `P2P_ADVANCED_ATTRIBUTES_ENABLED`, `P2P_ONBOARD_MEMORY_ENABLED`
            * `BoolEnableDisableChan` - `CHANNEL_ENABLED`
            * `BoolEnableDisableIQ` - `FETCH_INTERLEAVED_IQ_DATA`
            * `BoolEnableDisableRealtime` - `HORZ_ENFORCE_REALTIME`
            * `BoolEnableDisableTIS` - `ENABLE_TIME_INTERLEAVED_SAMPLING`

## 0.6.0 - 2017-12-20
* ### ALL
  * #### Added
    * `abort`. See [#660](https://github.com/ni/nimi-python/issues/655).
* ### NI-DMM
  * #### Added
    * `fetch_waveform_into` for high-performance fetch using numpy.array of float64.
  * #### Changed
    * Property powerline_freq no longer uses enum PowerlineFrequency.
    * Property current_source no longer uses enum CurrentSource.
    * Property input_resistance no longer uses enum InputResistance.
    * Removed `actual_number_of_points` from `fetch_waveform()` returned tuple
    * Removed `actual_number_of_points` from `fetch_multi_point()` returned tuple
    * Removed `actual_number_of_points` from `read_multi_point()` returned tuple
    * Removed `actual_number_of_points` from `read_waveform()` returned tuple
* ### NI-Switch
  * #### Removed
    * Removed `init_with_topology`. Clients should use `niswitch.Session` constructor. See [#660](https://github.com/ni/nimi-python/issues/660).
* ### NI-DCPower
  * #### Changed
    * Property power_line_frequency no longer uses enum PowerLineFrequency.
    * Removed `actual_count` from `fetch_multiple()` returned tuple
* ### NI-FGEN
  * #### Added
    * Support for calling `write_waveform` using list (float) or numpy.array (int16 or float64)
    * Support for calling `write_waveform` with a waveform handle (int) or a name (str).
    * Support for calling `create_waveform` using list (float) or numpy.array (int16 or float64)
  * #### Changed
    * Renamed `create_waveform_f64` -> `create_waveform`
  * #### Removed
    * `create_waveform_i16`
    * `write_binary16_waveform`: Use `write_waveform`
    * `write_named_waveform_i16`: Use `write_waveform`
    * `write_named_waveform_f64`: Use `write_waveform`
* ### NI-SCOPE
  * #### Added
    * `fetch_into` for high-performance fetch using numpy.array. Supported element types:
      * `numpy.float64`
      * `numpy.int8`
      * `numpy.int16`
      * `numpy.int32`
  * #### Changed
    * Added default values for timeout on all fetch and read functions.
    * Property input_impedance no longer uses enum InputImpedance.
  * #### Removed
    * `AddWaveformProcessing` - See #667 for rationale
    * `ClearWaveformProcessing` - See #667 for rationale
    * `FetchArrayMeasurement` - See #667 for rationale

## 0.5.0 - 2017-11-27
* ### ALL
  * #### Removed
    * enum definitions that are not referenced by a function and/or an attributes
* ### NI-DMM
  * #### Added
    * `get_ext_cal_recommended_interval`
* ### NI-DCPower
  * #### Added
    * `get_ext_cal_last_date_and_time`
    * `get_ext_cal_last_temp`
    * `get_ext_cal_recommended_interval`
    * `measure_multiple`
* ### NI-FGEN
  * #### Removed
    * `adjust_sample_clock_relative_delay`
* ### NI-SCOPE
  * #### Added
    * Initial release
  * #### Removed
    * Removed Peer to Peer attributes

## 0.4.0 - 2017-11-07
* ### ALL
  * #### Changed
    * Simplified examples by removing try/except
    * **SOURCE BREAKER:** Changed names of enum value names to correspond to C #defines
* ### NI-DMM
  * #### Changed
    * Removed incorrect leading underscore from some enum values:
      * `Function.AC_VOLTS_DC_COUPLED`
      * `Function.WAVEFORM_CURRENT`
      * `MeasurementCompleteDest.LBR_TRIG_0`
      * `OperationMode.IVIDMM_MODE`
      * `SampleTrigger.EXTERNAL`
      * `SampleTrigger.TTL_3`
      * `TriggerSource.TTL_0`
      * `TriggerSource.TTL_3`
      * `TriggerSource.TTL_7`
      * `TriggerSource.PXI_STAR`
* ### NI-SWITCH
  * #### Removed
    * Support for `is_debounced` and `is_scanning` functions. Instead use the attribute of the same name.
* ### NI-DCPower
  * #### Added
    * New example `nidcpower_advanced_sequence.py`
  * #### Changed
    * Fixed method signature for:
      * `wait_for_event`
      * `create_sequence`
      * `create_advanced_sequence`
  * #### Removed
    * Support for `measure_multiple` until issue #444 is addressed.
* ### NI-FGEN
  * #### Added
    * Initial release

## 0.3.0 - 2017-10-13
* ### ALL
  * #### Added
    * Support for ViInt64 (64-bit integers)
  * #### Changed
    * Modified how methods with repeated capabilities are invoked. There's no longer (for example) a `channel_name` input. Instead:
      ```python
      # Sets sequence on channels 0 through 3
      session['0-3'].set_sequence(values, source_delays)
      ```
    * Enum value documentation lists the fully qualified name - this is to allow easy copy/paste
* ### NI-DMM
  * #### Changed
    * Added default values to some parameters.
  * #### Removed
    * Removed methods that aren’t useful in the Python bindings.
* ### NI-SWITCH
  * #### Changed
    * Added default values to some parameters.
  * #### Removed
    * Removed methods that aren’t useful in the Python bindings.
* ### NI-DCPower
  * #### Added
    * Initial release

## 0.2.0 - 2017-09-20
* ### ALL
  * #### Added
    * Suport for channel-based properties
  * #### Changed
    * Warnings no longer raise an exception
      * Warnings are now added to warnings.warn()
* ### NI-DMM
  * #### Changed
    * Added support for enums with types other than ViInt32 (Fixes [#330](https://github.com/ni/nimi-python/issues/330))
* ### NI-ModInst
  * #### Changed
    * Device index is now on session not attribute. The correct way is now
      ```python
      i = 0
      with nimodinst.Session('nidmm') as session:
          name = session[i].device_name
      ```
* ### NI-SWITCH
  * #### Added
    * Initial release

## 0.1.0 - 2017-09-01
* ### NI-DMM
  * #### Added
    * Initial release
* ### NI-ModInst
  * #### Added
    * Initial release

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Python Versioning](http://legacy.python.org/dev/peps/pep-0396/).

<!--
* [Unreleased](#unreleased)
## [Unreleased]
* ### ALL
    * #### Added
    * #### Changed
    * #### Removed
* ### NI-DMM
    * #### Added
    * #### Changed
    * #### Removed
* ### NI-ModInst
    * #### Added
    * #### Changed
    * #### Removed
* ### NI-Switch
    * #### Added
    * #### Changed
    * #### Removed
* ### NI-DCPower
    * #### Added
    * #### Changed
    * #### Removed
* ### NI-FGEN
    * #### Added
    * #### Changed
    * #### Removed
* ### NI-SCOPE
    * #### Added
    * #### Changed
    * #### Removed
* ### NI Switch Executive
    * #### Added
    * #### Changed
    * #### Removed
* ### NI-Digital Pattern Driver
    * #### Added
    * #### Changed
    * #### Removed
* ### NI-TClk
    * #### Added
    * #### Changed
    * #### Removed
-->


