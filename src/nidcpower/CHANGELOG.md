# Changelog

* [Unreleased](#unreleased)
* [1.4.4](#144---2023-04-14)
* [1.4.3](#143---2022-12-16)
* [1.4.2](#142---2022-08-03)
* [1.4.1](#141---2021-08-23)
* [1.4.0](#140---2021-07-09)
* [1.3.3](#133---2021-02-26)
* [1.3.2](#132---2020-09-18)
* [1.3.1](#131---2020-06-08)
* [1.3.0](#130---2020-05-21)
* [1.2.1](#121---2020-04-21)
* [1.2.0](#120---2020-03-06)
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

## Unreleased
* #### Added
* #### Changed
    * Repo CHANGELOG split into module CHANGELOGs. No more ALL or `nidcpower` (NI-DCPower) section labels from now on. Sections not relevant to nidcpower were removed from the nidcpower CHANGELOG.
* #### Removed
    * `easy_install` support


## 1.4.4 - 2023-04-14
* ### ALL
    * #### Added
        * Support for Python 3.11
    * #### Changed
        * Fix [#1888](https://github.com/ni/nimi-python/issues/1888): Deadlock on multithreaded usage due to UnlockSession always being called with callerHasLock=False.
* ### `nidcpower` (NI-DCPower)
    * #### Added
        * Pass Python interpreter information if the driver runtime version supports it. This is used by NI in order to better understand client usage.
        * API parity with NI-DCPower 2023 Q2.
            * Properties added:
                * `lcr_ac_dither_enabled`
                * `lcr_ac_electrical_cable_length_delay`
                * `lcr_dc_bias_transient_response`
                * `lcr_source_aperture_time`
                * `measure_complete_event_output_behavior`
                * `measure_complete_event_toggle_initial_state`
                * `sequence_engine_done_event_output_behavior`
                * `sequence_engine_done_event_toggle_initial_state`
                * `sequence_iteration_complete_event_output_behavior`
                * `sequence_iteration_complete_event_toggle_initial_state`
                * `source_complete_event_output_behavior`
                * `source_complete_event_toggle_initial_state`
            * Enums added:
                * `CurrentLimitBehavior`
                * `EventOutputBehavior`
                * `EventToggleInitialState`
                * `LCRDCBiasTransientResponse`
            * Enum values added:
                * `AS_CONFIGURED` added to enum `LCROpenShortLoadCompensationDataSource`
                * `NI_STANDARD_0_5M` added to enum `CableLength`
            * Methods added:
                * `configure_lcr_compensation`
                * `get_lcr_compensation_data`
    * #### Changed
        * Enums reordered:
            * `AutoZero`
            * `CableLength`

## 1.4.3 - 2022-12-16
* ### ALL
    * #### Added
        * Support for Python 3.10
    * #### Removed
        * Support for Python 3.6
* ### `nidcpower` (NI-DCPower)
    * #### Added
        * MeasurementLink support
    * #### Changed
        * Binary compatibility change for type `LCRLoadCompensationSpot` on Linux. Client code using method `nidcpower.Session.perform_lcr_load_compensation` on Linux now requires NI-DCPower 2023 Q1 driver runtime or newer.

## 1.4.2 - 2022-08-03
* ### `nidcpower` (NI-DCPower)
    * #### Added
        * API parity with NI-DCPower 2022 Q3.
            * Properties added:
                * `aperture_time_auto_mode`
                * `autorange_maximum_delay_after_range_change`
                * `cable_length`
                * `instrument_mode`
                * `isolation_state`
                * `lcr_actual_load_reactance`
                * `lcr_actual_load_resistance`
                * `lcr_automatic_level_control`
                * `lcr_current_amplitude`
                * `lcr_current_range`
                * `lcr_custom_measurement_time`
                * `lcr_dc_bias_automatic_level_control`
                * `lcr_dc_bias_current_level`
                * `lcr_dc_bias_current_range`
                * `lcr_dc_bias_source`
                * `lcr_dc_bias_voltage_level`
                * `lcr_dc_bias_voltage_range`
                * `lcr_frequency`
                * `lcr_impedance_auto_range`
                * `lcr_impedance_range`
                * `lcr_impedance_range_source`
                * `lcr_load_capacitance`
                * `lcr_load_compensation_enabled`
                * `lcr_load_inductance`
                * `lcr_load_resistance`
                * `lcr_measured_load_reactance`
                * `lcr_measured_load_resistance`
                * `lcr_measurement_time`
                * `lcr_open_compensation_enabled`
                * `lcr_open_conductance`
                * `lcr_open_short_load_compensation_data_source`
                * `lcr_open_susceptance`
                * `lcr_short_compensation_enabled`
                * `lcr_short_custom_cable_compensation_enabled`
                * `lcr_short_reactance`
                * `lcr_short_resistance`
                * `lcr_source_delay_mode`
                * `lcr_stimulus_function`
                * `lcr_voltage_amplitude`
                * `lcr_voltage_range`
            * Enums added:
                * `ApertureTimeAutoMode`
                * `CableLength`
                * `InstrumentMode`
                * `LCRCompensationType`
                * `LCRDCBiasSource`
                * `LCRImpedanceRangeSource`
                * `LCRMeasurementTime`
                * `LCROpenShortLoadCompensationDataSource`
                * `LCRReferenceValueType`
                * `LCRSourceDelayMode`
                * `LCRStimulusFunction`
            * Methods added:
                * `configure_lcr_custom_cable_compensation`
                * `fetch_multiple_lcr`
                * `get_lcr_compensation_last_date_and_time`
                * `get_lcr_custom_cable_compensation_data`
                * `measure_multiple_lcr`
                * `perform_lcr_load_compensation`
                * `perform_lcr_open_compensation`
                * `perform_lcr_open_custom_cable_compensation`
                * `perform_lcr_short_compensation`
                * `perform_lcr_short_custom_cable_compensation`
            * Custom types added:
                * `LCRLoadCompensationSpot`
                * `LCRMeasurement`
        * `nidcpower_lcr_source_ac_voltage.py` example
    * #### Changed
        * Updated supported devices information in documentation for methods and properties
        * Added `channel` field to the `Measurement` namedtuple instances returned by `fetch_multiple` and `measure_multiple`

## 1.4.1 - 2021-08-23
* ### ALL
    * #### Added
        * Support for Python 3.9
    * #### Removed
        * Support for Python 3.5
* ### `nidcpower` (NI-DCPower)
    * #### Added
        * API parity with NI-DCPower 21.0.0.
            * Properties added:
                * `output_cutoff_delay`

## 1.4.0 - 2021-07-09
* ### `nidcpower` (NI-DCPower)
    * #### Added
        * `get_channel_names` - [#1588](https://github.com/ni/nimi-python/issues/1588)
        * `create_advanced_sequence_commit_step` - [#1636](https://github.com/ni/nimi-python/issues/1636)
        * API parity with NI-DCPower 20.7.0 by adding Output Cutoff functionality.
            * Properties added:
                * `output_cutoff_current_change_limit_high`
                * `output_cutoff_current_change_limit_low`
                * `output_cutoff_current_measure_limit_high`
                * `output_cutoff_current_measure_limit_low`
                * `output_cutoff_current_overrange_enabled`
                * `output_cutoff_enabled`
                * `output_cutoff_voltage_change_limit_high`
                * `output_cutoff_voltage_change_limit_low`
                * `output_cutoff_voltage_output_limit_high`
                * `output_cutoff_voltage_output_limit_low`
            * Methods added:
                * `clear_latched_output_cutoff_state`
                * `query_latched_output_cutoff_state`
        * Support for independent operation of instrument channels. Creating an `nidcpower.Session`
          with independent channels allows you to use multiple instruments in the same session. With
          independent channels, you can configure multiple channels of the same instrument, or of
          multiple instruments, independently of one another within the same session. Requires NI-DCPower
          driver runtime 20.6.0 or later. In order to use with older runtime or to maintain old behavior,
          pass `independent_channels=False` to `nidcpower.Session` constructor.

## 1.3.3 - 2021-02-26
* ### `nidcpower` (NI-DCPower)
    * #### Added
        * API parity with NI-DCPower 20.6.0 by adding Merged Channels and Shutdown Triggers support. The following properties are added:
            * `merged_channels`
            * `digital_edge_shutdown_trigger_input_terminal`
            * `shutdown_trigger_type`

## 1.3.2 - 2020-09-18
* ### ALL
    * #### Changed
        * Fix [#1491](https://github.com/ni/nimi-python/issues/1491): import_attribute_configuration_buffer() fails intermittently when `list` or `array.array` is passed in.
        * Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.5.0 for NI-DCPower, NI-SWITCH, and NI-DMM. no changes on other drivers.
* ### `nidcpower` (NI-DCPower)
    * #### Added
        * API parity with NI-DCPower 20.5.0 by adding measurement autoranging threshold range support, for which the following properties are added:
            * `autorange`
            * `autorange_aperture_time_mode`
            * `autorange_behavior`
            * `autorange_minimum_aperture_time`
            * `autorange_minimum_aperture_time_units`
            * `autorange_minimum_current_range`
            * `autorange_minimum_voltage_range`
            * `autorange_threshold_mode`

## 1.3.1 - 2020-06-08
* ### ALL
    * #### Changed
        * Fix [#1473](https://github.com/ni/nimi-python/issues/1473): Unintentional dependency on pytest
        * Fix [#1474](https://github.com/ni/nimi-python/issues/1474): Requires hightime>=0.2.0


## 1.3.0 - 2020-05-21
* ### ALL
    * #### Changed
        * Change the type of applicable properties and method parameters from `datetime.timedelta` to `hightime.timedelta` and from `datetime.datetime` to `hightime.datetime`. - [#744](https://github.com/ni/nimi-python/issues/744), [#1368](https://github.com/ni/nimi-python/issues/1368), [#1382](https://github.com/ni/nimi-python/issues/1382), [#1397](https://github.com/ni/nimi-python/issues/1397)
        * Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.0.0 for all modules except `nidigital`, for which it is 19.0.1.
* ### `nidcpower` (NI-DCPower)
    * #### Added
        * API parity with NI-DCPower 20.0 by adding the following properties:
            * `Session.serial_number`
            * `Session.actual_power_allocation`
            * `Session.requested_power_allocation`
            * `Session.power_allocation_mode`

## 1.2.1 - 2020-04-21
* ### ALL
    * #### Added
        * Support for chained repeated capabilities. This allows things like
            ``` python
            session.sites[0, 1].pins['PinA', 'PinB'].ppmu_voltage_level = 4
            ```

            The repeated capabilities will be expanded to `'site0/PinA,site0/PinB,site1/PinA,site1/PinB'`


## 1.2.0 - 2020-03-06
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
        * PyPy and PyPy3 support [#1271](https://github.com/ni/nimi-python/issues/1271)
* ### `nidcpower` (NI-DCPower)
    * #### Added
        * `create_advanced_sequence()` - [#504](https://github.com/ni/nimi-python/issues/504)
            * Instead of a list of attribute IDs, you pass in a list of property names as strings
            * Includes example to see how to use it
            * Additional methods and properties that were made public (rather than private)
                * `create_advanced_sequence_step()`
                * `delete_advanced_sequence()`
                * `active_advanced_sequence`
                * `active_advanced_sequence_step`


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
* ### `nidcpower` (NI-DCPower)
    * #### Changed
        * Fix type of `sequence_step_delta_time_enabled ` property - [#1015](https://github.com/ni/nimi-python/issues/1015)



## 1.1.2 - 2019-06-06
* ### ALL
    * #### Changed
        * Switched to slightly different metadata format - Actual `True`/`False` instead of strings
        * New internal process for generating metadata

## 1.1.0 - 2018-10-25
* ### ALL
    * #### Changed
        * Updated generated metadata
        * Updated "Driver Version Tested Against"
        * Update visatype definitions to work on Linux as well as Windows - [#911](https://github.com/ni/nimi-python/issues/911)
* ### `nidcpower` (NI-DCPower)
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

## 1.0.0 - 2018-06-08
* ### ALL
    * #### Removed
        * Explicitly disallow using a repeated capability on Session. `session[0].vertical_range = 1.0` will no longer work. Instead use `session.channels[0].vertical_range = 1.0` - [#853](https://github.com/ni/nimi-python/issues/853)
* ### `nidcpower` (NI-DCPower)
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

## 0.9.0 - 2018-05-22
* ### ALL
    * #### Added
        * Add `session.lock()` and `session.unlock()` to all drivers except `nimodinst` - [#846](https://github.com/ni/nimi-python/issues/846)
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
* ### `nidcpower` (NI-DCPower)
    * #### Removed
        * `export_signal()` - [#828](https://github.com/ni/nimi-python/issues/828)
        * `active_advanced_sequence` [#832](https://github.com/ni/nimi-python/issues/832)
        * `active_advanced_sequence_step` [#832](https://github.com/ni/nimi-python/issues/832)
        * Default value for trigger parameter on `send_software_edge_trigger()` [#832](https://github.com/ni/nimi-python/issues/832)

## 0.8.0 - 2018-04-27
* ### ALL
    * #### Changed
        * All exceptions raised by the Python bindings inherit from `<driver>.Error`
        * Exception type formerly known as `<driver>.Error` is now known as `<driver>.DriverError`
            * This encapsulates any error that is returned by the underlying driver
        * All timeout parameters can now also take a simple number in seconds. `timeout=datetime.timedelta(milliseconds=100)` and `timeout=0.1` are identical. [#796](https://github.com/ni/nimi-python/issues/796)
* ### `nidcpower` (NI-DCPower)
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
* ### `nidcpower` (NI-DCPower)
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

## 0.6.0 - 2017-12-20
* ### ALL
  * #### Added
    * `abort`. See [#660](https://github.com/ni/nimi-python/issues/655).
* ### `nidcpower` (NI-DCPower)
  * #### Changed
    * Property power_line_frequency no longer uses enum PowerLineFrequency.
    * Removed `actual_count` from `fetch_multiple()` returned tuple

## 0.5.0 - 2017-11-27
* ### ALL
  * #### Removed
    * enum definitions that are not referenced by a function and/or an attributes
* ### `nidcpower` (NI-DCPower)
  * #### Added
    * `get_ext_cal_last_date_and_time`
    * `get_ext_cal_last_temp`
    * `get_ext_cal_recommended_interval`
    * `measure_multiple`

## 0.4.0 - 2017-11-07
* ### ALL
  * #### Changed
    * Simplified examples by removing try/except
    * **SOURCE BREAKER:** Changed names of enum value names to correspond to C #defines
* ### `nidcpower` (NI-DCPower)
  * #### Added
    * New example `nidcpower_advanced_sequence.py`
  * #### Changed
    * Fixed method signature for:
      * `wait_for_event`
      * `create_sequence`
      * `create_advanced_sequence`
  * #### Removed
    * Support for `measure_multiple` until issue #444 is addressed.

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
* ### `nidcpower` (NI-DCPower)
  * #### Added
    * Initial release


The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Python Versioning](http://legacy.python.org/dev/peps/pep-0396/).

<!--
* [Unreleased](#unreleased)
## Unreleased
* #### Added
* #### Changed
* #### Removed
-->
