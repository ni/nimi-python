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
    * Repo CHANGELOG split into module CHANGELOGs. No more ALL or `nidigital` (NI-Digital Pattern Driver) section labels from now on. Sections not relevant to nidigital were removed from the nidigital CHANGELOG.
* #### Removed
    * `easy_install` support

## 1.4.4 - 2023-04-14
* ### ALL
    * #### Added
        * Support for Python 3.11
    * #### Changed
        * Fix [#1888](https://github.com/ni/nimi-python/issues/1888): Deadlock on multithreaded usage due to UnlockSession always being called with callerHasLock=False.
* ### `nidigital` (NI-Digital Pattern Driver)
    * #### Changed
        * Update `GRPC_SERVICE_INTERFACE_NAME` to use the correct gRPC package name (`nidigitalpattern_grpc`).

## 1.4.3 - 2022-12-16
* ### ALL
    * #### Added
        * Support for Python 3.10
    * #### Removed
        * Support for Python 3.6
* ### `nidigital` (NI-Digital Pattern Driver)
    * #### Added
        * MeasurementLink support

## 1.4.2 - 2022-08-03

## 1.4.1 - 2021-08-23
* ### ALL
    * #### Added
        * Support for Python 3.9
    * #### Removed
        * Support for Python 3.5
* ### `nidigital` (NI-Digital Pattern Driver)
    * #### Added
        * API parity with NI-Digital Pattern Driver 21.0.0.
            * Properties added:
                * `digital_edge_rio_trigger_edge`
                * `digital_edge_rio_trigger_source`
                * `exported_rio_event_output_terminal`
                * `rio_event_terminal_name`
                * `rio_trigger_terminal_name`
                * `rio_trigger_type`
            * Repeated Capabilities added:
                * `rio_events`
                * `rio_triggers`

## 1.4.0 - 2021-07-09

## 1.3.3 - 2021-02-26
* ### `nidigital` (NI-Digital Pattern Driver)
    * #### Added
        * 1.0.0 release:
            * API reference documentation and API usage examples
        * API parity with NI-Digital Pattern Driver 20.6.0 by adding support for configuration of frequency counter measurement mode. The following properties are added:
            * `frequency_counter_measurement_mode`
            * `frequency_counter_hysteresis_enabled`

## 1.3.2 - 2020-09-18
* ### ALL
    * #### Changed
        * Fix [#1491](https://github.com/ni/nimi-python/issues/1491): import_attribute_configuration_buffer() fails intermittently when `list` or `array.array` is passed in.
        * Update "Driver Version Tested Against", in documentation, with latest versions installed on nimi-bot. The version is 20.5.0 for NI-DCPower, NI-SWITCH, and NI-DMM. no changes on other drivers.

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
* ### `nidigital` (NI-Digital Pattern Driver)
    * #### Added
        * 0.9.0 release:
            * Public API is considered complete, stable, and tested
            * Parity with public API for other ADEs supported in NI-Digital Pattern Driver 19.0.1
            * API reference documentation and example code are not complete
    * #### Changed
        * Changed initial_state parameters in `apply_levels_and_timing` to basic sequence types - [#1391](https://github.com/ni/nimi-python/issues/1391)
        * Changed HistoryRAMCycleInformation.__repr__ to include `__module__` - [#1426](https://github.com/ni/nimi-python/issues/1426)
        * Changed return type of `get_time_set_period` and `get_time_set_edge` to `datetime.timedelta` - [#1397](https://github.com/ni/nimi-python/issues/1397)

## 1.2.1 - 2020-04-21
* ### ALL
    * #### Added
        * Support for chained repeated capabilities. This allows things like
            ``` python
            session.sites[0, 1].pins['PinA', 'PinB'].ppmu_voltage_level = 4
            ```

            The repeated capabilities will be expanded to `'site0/PinA,site0/PinB,site1/PinA,site1/PinB'`
* ### `nidigital` (NI-Digital Pattern Driver)
    * #### Added
        * `get_pattern_pin_names` - [#1292](https://github.com/ni/nimi-python/issues/1292)
        * Support for `instruments` repeated capability in the following properties - `instrument_firmware_revision`, `serial_number`, and `timing_absolute_delay` -  [#1228](https://github.com/ni/nimi-python/issues/1228)
        * `load_specifications_levels_and_timing` that allows loading of multiple specs, levels, and/or timing files in a single call - [#1392](https://github.com/ni/nimi-python/issues/1392)
        * `get_channel_names` - [#1386](https://github.com/ni/nimi-python/issues/1386)
    * #### Changed
        * Change the type of applicable method parameters and properties to enums - [#1066](https://github.com/ni/nimi-python/issues/1066)
        * `get_site_pass_fail` returns dictionary where each key is a site number and value is a bool indicating pass/fail - [#1297](https://github.com/ni/nimi-python/issues/1297)
        * `burst_pattern` returns dictionary where each key is a site number and value is a bool indicating pass/fail, if `wait_until_done` is specified as `True` - [#1296](https://github.com/ni/nimi-python/issues/1296)
        * Update enum types to match the API in other ADEs - [#1330](https://github.com/ni/nimi-python/issues/1330):
            * Update the names of many enum types. See [#1330](https://github.com/ni/nimi-python/issues/1330) for the full list.
            * Added `WriteStaticPinState` enum type and changed the parameter type of `write_static` method to the newly added enum.
            * Added `SoftwareTrigger` enum type and changed the parameter type of `send_software_edge_trigger` method to the newly added enum.
        * Update `fetch_history_ram_cycle_information`, `get_history_ram_sample_count`, and `is_site_enabled` to use `sites` repeated capability - [#1337](https://github.com/ni/nimi-python/issues/1337)
        * Rename parameter `time_set` to `time_set_name` in applicable time set methods - [#1396](https://github.com/ni/nimi-python/issues/1396)
        * Modified `unload_specifications` to allow unloading of one or more specs files in a single call - [#1392](https://github.com/ni/nimi-python/issues/1392)
        * In `load_pin_map`, changed parameter name `pin_map_file_path` to `file_path` - [#1393](https://github.com/ni/nimi-python/issues/1393)
    * #### Removed
        * `get_pattern_pin_list`, `get_pattern_pin_indexes` and `get_pin_name` - [#1292](https://github.com/ni/nimi-python/issues/1292)
        * `get_site_results_site_numbers` method and `SiteResultType` enum - [#1298](https://github.com/ni/nimi-python/issues/1298)
        * `reset_attribute` - [#1364](https://github.com/ni/nimi-python/issues/1364)
        * `clear_error` - [#1366](https://github.com/ni/nimi-python/issues/1366)
        * `clock_generator_initiate` - [#1370](https://github.com/ni/nimi-python/issues/1370)
        * `load_specifications`, `load_levels`, and `load_timing` - [#1392](https://github.com/ni/nimi-python/issues/1392)
        * `get_channel_name` and `get_channel_name_from_string` - [#1386](https://github.com/ni/nimi-python/issues/1386)

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
* ### `nidigital` (NI-Digital Pattern Driver)
    * #### Added
        * `conditional_jump_triggers` and `pattern_opcode_events` repeated capabilities - [#1191](https://github.com/ni/nimi-python/issues/1191), [#1192](https://github.com/ni/nimi-python/issues/1192)
    * #### Changed
        * `write_source_waveform_site_unique()` now supports `numpy.array` and `list` as site waveform types
        * sites are now a repeated capability instead of a parameter: `session.sites[1,2].fetch_capture_waveform(...)` - [#1111](https://github.com/ni/nimi-python/issues/1111)
        * `fetch_history_ram_cycle_information` method now supports fetching multiple History RAM samples in a single API call - [#1071](https://github.com/ni/nimi-python/issues/1071)
        * Update methods that require `pin_list` to be passed in, such that `pin_list` can be passed in via `pins` repeated capability - [#1294](https://github.com/ni/nimi-python/issues/1294)
    * #### Removed
        * Removed redundant (redundant because corresponding properties can be used instead) API methods - [#1065](https://github.com/ni/nimi-python/issues/1065)
        * Removed programmatic pin map creation API - [#1124](https://github.com/ni/nimi-python/issues/1124)
        * Removed `fetch_history_ram_cycle_pin_data` and `fetch_history_ram_scan_cycle_number`. They are not needed since `fetch_history_ram_cycle_information`
            was updated to return class instances that contains cycle pin data and scan cycle number - [#1071](https://github.com/ni/nimi-python/issues/1071)

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
* ### `nidigital` (NI-Digital Pattern Driver)
    * #### Added
        * `fetch_capture_waveform()` - returns dictionary { site: data, site: data, ... }
        * `write_source_waveform_site_unique()` - takes waveform_name and dictionary { site: data, site: data, ... }
        * `pins` is now a valid repeated capability
    * #### Changed
        * Fix get/set properties - [#1062](https://github.com/ni/nimi-python/issues/1062)
        * Removed array-size parameter from apply_tdr_offsets() and write_source_waveform_broadcast_u32() methods - [#1070](https://github.com/ni/nimi-python/issues/1070)
        * Renamed `write_source_waveform_broadcast_u32()` to `write_source_waveform_broadcast()`
        * `get_pin_results_pin_information()` - returns namedtuple `PinInfo(pin_indexes, site_numbers, channel_indexes)`

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
* ### `nidigital` (NI-Digital Pattern Driver)
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

<!--
* [Unreleased](#unreleased)
## Unreleased
* #### Added
* #### Changed
* #### Removed
-->
