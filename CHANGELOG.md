# Changelog

* [Unreleased](#unreleased)
* [0.7.0](#060---2018-02-20)
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
        * `niscope.fetch()` now takes additional parameters for associated attributes and add resulting record as part of the waveform info 
    * #### Removed

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
-->

