# -*- coding: utf-8 -*-
# This file was generated

import array  # noqa: F401
import ctypes
import hightime
import niscope._converters as _converters
import niscope._library_singleton as _library_singleton
import niscope._visatype as _visatype
import niscope.enums as enums
import niscope.errors as errors
import threading

from niscope._visatype import *  # noqa: F403,H303

import niscope.waveform_info as waveform_info  # noqa: F401

import niscope.measurement_stats as measurement_stats  # noqa: F401


# Helper functions for creating ctypes needed for calling into the driver DLL
def get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        return numpy.ctypeslib.as_ctypes(value)
    elif isinstance(value, bytes):
        return ctypes.cast(value, ctypes.POINTER(library_type))
    elif isinstance(value, list):
        assert library_type is not None, 'library_type is required for list'
        return (library_type * len(value))(*value)
    else:
        if library_type is not None and size is not None:
            return (library_type * size)()
        else:
            return None


def get_ctypes_and_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class LibraryInterpreter(object):
    '''Library C<->Python interpreter.'''

    def __init__(self, encoding):
        self._encoding = encoding
        self._library = _library_singleton.get()

    def _get_error_description(self, session, error_code):
        '''_get_error_description

        Returns the error description.
        '''
        try:
            _, error_string = self._get_error(session)
            return error_string
        except errors.Error:
            pass

        try:
            '''
            It is expected for _get_error to raise when the session is invalid
            (IVI spec requires GetError to fail).
            Use _error_message instead. It doesn't require a session.
            '''
            error_string = self._error_message(session, error_code)
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."

    def abort(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.abort(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def acquisition_status(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        acquisition_status_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.acquisition_status(vi_ctype, None if acquisition_status_ctype is None else (ctypes.pointer(acquisition_status_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.AcquisitionStatus(acquisition_status_ctype.value)

    def _actual_meas_wfm_size(self, session, array_meas_function):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        array_meas_function_ctype = _visatype.ViInt32(array_meas_function.value)  # case S130
        meas_waveform_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library._actual_meas_wfm_size(vi_ctype, array_meas_function_ctype, None if meas_waveform_size_ctype is None else (ctypes.pointer(meas_waveform_size_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(meas_waveform_size_ctype.value)

    def _actual_num_wfms(self, session, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        num_wfms_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library._actual_num_wfms(vi_ctype, channel_list_ctype, None if num_wfms_ctype is None else (ctypes.pointer(num_wfms_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(num_wfms_ctype.value)

    def add_waveform_processing(self, session, channel_list, meas_function):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        meas_function_ctype = _visatype.ViInt32(meas_function.value)  # case S130
        error_code = self._library.add_waveform_processing(vi_ctype, channel_list_ctype, meas_function_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def auto_setup(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.auto_setup(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _cal_fetch_date(self, session, which_one):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        which_one_ctype = _visatype.ViInt32(which_one.value)  # case S130
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library._cal_fetch_date(vi_ctype, which_one_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value)

    def _cal_fetch_temperature(self, session, which_one):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        which_one_ctype = _visatype.ViInt32(which_one)  # case S150
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library._cal_fetch_temperature(vi_ctype, which_one_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def self_cal(self, session, channel_list, option=enums.Option.SELF_CALIBRATE_ALL_CHANNELS):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        option_ctype = _visatype.ViInt32(option.value)  # case S130
        error_code = self._library.self_cal(vi_ctype, channel_list_ctype, option_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_waveform_measurement_stats(self, session, channel_list, clearable_measurement_function=enums.ClearableMeasurement.ALL_MEASUREMENTS):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        clearable_measurement_function_ctype = _visatype.ViInt32(clearable_measurement_function.value)  # case S130
        error_code = self._library.clear_waveform_measurement_stats(vi_ctype, channel_list_ctype, clearable_measurement_function_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_waveform_processing(self, session, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        error_code = self._library.clear_waveform_processing(vi_ctype, channel_list_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def commit(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.commit(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_chan_characteristics(self, session, channel_list, input_impedance, max_input_frequency):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        input_impedance_ctype = _visatype.ViReal64(input_impedance)  # case S150
        max_input_frequency_ctype = _visatype.ViReal64(max_input_frequency)  # case S150
        error_code = self._library.configure_chan_characteristics(vi_ctype, channel_list_ctype, input_impedance_ctype, max_input_frequency_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_equalization_filter_coefficients(self, session, channel_list, coefficients):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        number_of_coefficients_ctype = _visatype.ViInt32(0 if coefficients is None else len(coefficients))  # case S160
        coefficients_ctype = get_ctypes_pointer_for_buffer(value=coefficients, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.configure_equalization_filter_coefficients(vi_ctype, channel_list_ctype, number_of_coefficients_ctype, coefficients_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_horizontal_timing(self, session, min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        min_sample_rate_ctype = _visatype.ViReal64(min_sample_rate)  # case S150
        min_num_pts_ctype = _visatype.ViInt32(min_num_pts)  # case S150
        ref_position_ctype = _visatype.ViReal64(ref_position)  # case S150
        num_records_ctype = _visatype.ViInt32(num_records)  # case S150
        enforce_realtime_ctype = _visatype.ViBoolean(enforce_realtime)  # case S150
        error_code = self._library.configure_horizontal_timing(vi_ctype, min_sample_rate_ctype, min_num_pts_ctype, ref_position_ctype, num_records_ctype, enforce_realtime_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _configure_ref_levels(self, session, low=10.0, mid=50.0, high=90.0):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        low_ctype = _visatype.ViReal64(low)  # case S150
        mid_ctype = _visatype.ViReal64(mid)  # case S150
        high_ctype = _visatype.ViReal64(high)  # case S150
        error_code = self._library._configure_ref_levels(vi_ctype, low_ctype, mid_ctype, high_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_digital(self, session, trigger_source, slope=enums.TriggerSlope.POSITIVE, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(self._encoding))  # case C020
        slope_ctype = _visatype.ViInt32(slope.value)  # case S130
        holdoff_ctype = _converters.convert_timedelta_to_seconds_real64(holdoff)  # case S140
        delay_ctype = _converters.convert_timedelta_to_seconds_real64(delay)  # case S140
        error_code = self._library.configure_trigger_digital(vi_ctype, trigger_source_ctype, slope_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_edge(self, session, trigger_source, level, trigger_coupling, slope=enums.TriggerSlope.POSITIVE, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(self._encoding))  # case C020
        level_ctype = _visatype.ViReal64(level)  # case S150
        slope_ctype = _visatype.ViInt32(slope.value)  # case S130
        trigger_coupling_ctype = _visatype.ViInt32(trigger_coupling.value)  # case S130
        holdoff_ctype = _converters.convert_timedelta_to_seconds_real64(holdoff)  # case S140
        delay_ctype = _converters.convert_timedelta_to_seconds_real64(delay)  # case S140
        error_code = self._library.configure_trigger_edge(vi_ctype, trigger_source_ctype, level_ctype, slope_ctype, trigger_coupling_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_hysteresis(self, session, trigger_source, level, hysteresis, trigger_coupling, slope=enums.TriggerSlope.POSITIVE, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(self._encoding))  # case C020
        level_ctype = _visatype.ViReal64(level)  # case S150
        hysteresis_ctype = _visatype.ViReal64(hysteresis)  # case S150
        slope_ctype = _visatype.ViInt32(slope.value)  # case S130
        trigger_coupling_ctype = _visatype.ViInt32(trigger_coupling.value)  # case S130
        holdoff_ctype = _converters.convert_timedelta_to_seconds_real64(holdoff)  # case S140
        delay_ctype = _converters.convert_timedelta_to_seconds_real64(delay)  # case S140
        error_code = self._library.configure_trigger_hysteresis(vi_ctype, trigger_source_ctype, level_ctype, hysteresis_ctype, slope_ctype, trigger_coupling_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_immediate(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.configure_trigger_immediate(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_software(self, session, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        holdoff_ctype = _converters.convert_timedelta_to_seconds_real64(holdoff)  # case S140
        delay_ctype = _converters.convert_timedelta_to_seconds_real64(delay)  # case S140
        error_code = self._library.configure_trigger_software(vi_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_video(self, session, trigger_source, signal_format, event, polarity, trigger_coupling, enable_dc_restore=False, line_number=1, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(self._encoding))  # case C020
        enable_dc_restore_ctype = _visatype.ViBoolean(enable_dc_restore)  # case S150
        signal_format_ctype = _visatype.ViInt32(signal_format.value)  # case S130
        event_ctype = _visatype.ViInt32(event.value)  # case S130
        line_number_ctype = _visatype.ViInt32(line_number)  # case S150
        polarity_ctype = _visatype.ViInt32(polarity.value)  # case S130
        trigger_coupling_ctype = _visatype.ViInt32(trigger_coupling.value)  # case S130
        holdoff_ctype = _converters.convert_timedelta_to_seconds_real64(holdoff)  # case S140
        delay_ctype = _converters.convert_timedelta_to_seconds_real64(delay)  # case S140
        error_code = self._library.configure_trigger_video(vi_ctype, trigger_source_ctype, enable_dc_restore_ctype, signal_format_ctype, event_ctype, line_number_ctype, polarity_ctype, trigger_coupling_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_window(self, session, trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff=hightime.timedelta(seconds=0.0), delay=hightime.timedelta(seconds=0.0)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(self._encoding))  # case C020
        low_level_ctype = _visatype.ViReal64(low_level)  # case S150
        high_level_ctype = _visatype.ViReal64(high_level)  # case S150
        window_mode_ctype = _visatype.ViInt32(window_mode.value)  # case S130
        trigger_coupling_ctype = _visatype.ViInt32(trigger_coupling.value)  # case S130
        holdoff_ctype = _converters.convert_timedelta_to_seconds_real64(holdoff)  # case S140
        delay_ctype = _converters.convert_timedelta_to_seconds_real64(delay)  # case S140
        error_code = self._library.configure_trigger_window(vi_ctype, trigger_source_ctype, low_level_ctype, high_level_ctype, window_mode_ctype, trigger_coupling_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_vertical(self, session, channel_list, range, coupling, offset=0.0, probe_attenuation=1.0, enabled=True):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        range_ctype = _visatype.ViReal64(range)  # case S150
        offset_ctype = _visatype.ViReal64(offset)  # case S150
        coupling_ctype = _visatype.ViInt32(coupling.value)  # case S130
        probe_attenuation_ctype = _visatype.ViReal64(probe_attenuation)  # case S150
        enabled_ctype = _visatype.ViBoolean(enabled)  # case S150
        error_code = self._library.configure_vertical(vi_ctype, channel_list_ctype, range_ctype, offset_ctype, coupling_ctype, probe_attenuation_ctype, enabled_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.disable(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_attribute_configuration_buffer(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32()  # case S170
        configuration_ctype = None  # case B580
        error_code = self._library.export_attribute_configuration_buffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        size_in_bytes_ctype = _visatype.ViInt32(error_code)  # case S180
        configuration_size = size_in_bytes_ctype.value  # case B590
        configuration_array = array.array("b", [0] * configuration_size)  # case B590
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self._library.export_attribute_configuration_buffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_to_bytes(configuration_array)

    def export_attribute_configuration_file(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.export_attribute_configuration_file(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _fetch(self, session, channel_list, num_samples, timeout=hightime.timedelta(seconds=5.0)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        num_samples_ctype = _visatype.ViInt32(num_samples)  # case S150
        waveform_size = (num_samples * self._actual_num_wfms(session, channel_list))  # case B560
        waveform_array = array.array("d", [0] * waveform_size)  # case B560
        waveform_ctype = get_ctypes_pointer_for_buffer(value=waveform_array, library_type=_visatype.ViReal64)  # case B560
        wfm_info_size = self._actual_num_wfms(session, channel_list)  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library._fetch(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, waveform_ctype, wfm_info_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_array, [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms(session, channel_list))]

    def _fetch_into_numpy(self, session, num_samples, waveform, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        num_samples_ctype = _visatype.ViInt32(num_samples)  # case S150
        waveform_ctype = get_ctypes_pointer_for_buffer(value=waveform)  # case B510
        wfm_info_size = self._actual_num_wfms(session, channel_list)  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library._fetch(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, waveform_ctype, wfm_info_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms(session, channel_list))]

    def _fetch_array_measurement(self, session, channel_list, array_meas_function, measurement_waveform_size, timeout=hightime.timedelta(seconds=5.0)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        array_meas_function_ctype = _visatype.ViInt32(array_meas_function.value)  # case S130
        measurement_waveform_size_ctype = _visatype.ViInt32(measurement_waveform_size)  # case S150
        meas_wfm_size = (measurement_waveform_size * self._actual_num_wfms(session, channel_list))  # case B560
        meas_wfm_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=meas_wfm_size)  # case B560
        wfm_info_size = self._actual_num_wfms(session, channel_list)  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library._fetch_array_measurement(vi_ctype, channel_list_ctype, timeout_ctype, array_meas_function_ctype, measurement_waveform_size_ctype, meas_wfm_ctype, wfm_info_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(meas_wfm_ctype[i]) for i in range((measurement_waveform_size * self._actual_num_wfms(session, channel_list)))], [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms(session, channel_list))]

    def _fetch_binary16_into_numpy(self, session, num_samples, waveform, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        num_samples_ctype = _visatype.ViInt32(num_samples)  # case S150
        waveform_ctype = get_ctypes_pointer_for_buffer(value=waveform)  # case B510
        wfm_info_size = self._actual_num_wfms(session, channel_list)  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library._fetch_binary16(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, waveform_ctype, wfm_info_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms(session, channel_list))]

    def _fetch_binary32_into_numpy(self, session, num_samples, waveform, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        num_samples_ctype = _visatype.ViInt32(num_samples)  # case S150
        waveform_ctype = get_ctypes_pointer_for_buffer(value=waveform)  # case B510
        wfm_info_size = self._actual_num_wfms(session, channel_list)  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library._fetch_binary32(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, waveform_ctype, wfm_info_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms(session, channel_list))]

    def _fetch_binary8_into_numpy(self, session, num_samples, waveform, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        num_samples_ctype = _visatype.ViInt32(num_samples)  # case S150
        waveform_ctype = get_ctypes_pointer_for_buffer(value=waveform)  # case B510
        wfm_info_size = self._actual_num_wfms(session, channel_list)  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library._fetch_binary8(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, waveform_ctype, wfm_info_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms(session, channel_list))]

    def _fetch_measurement_stats(self, session, channel_list, scalar_meas_function, timeout=hightime.timedelta(seconds=5.0)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        scalar_meas_function_ctype = _visatype.ViInt32(scalar_meas_function.value)  # case S130
        result_size = self._actual_num_wfms(session, channel_list)  # case B560
        result_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=result_size)  # case B560
        mean_size = self._actual_num_wfms(session, channel_list)  # case B560
        mean_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=mean_size)  # case B560
        stdev_size = self._actual_num_wfms(session, channel_list)  # case B560
        stdev_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=stdev_size)  # case B560
        min_size = self._actual_num_wfms(session, channel_list)  # case B560
        min_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=min_size)  # case B560
        max_size = self._actual_num_wfms(session, channel_list)  # case B560
        max_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=max_size)  # case B560
        num_in_stats_size = self._actual_num_wfms(session, channel_list)  # case B560
        num_in_stats_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=num_in_stats_size)  # case B560
        error_code = self._library._fetch_measurement_stats(vi_ctype, channel_list_ctype, timeout_ctype, scalar_meas_function_ctype, result_ctype, mean_ctype, stdev_ctype, min_ctype, max_ctype, num_in_stats_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(result_ctype[i]) for i in range(self._actual_num_wfms(session, channel_list))], [float(mean_ctype[i]) for i in range(self._actual_num_wfms(session, channel_list))], [float(stdev_ctype[i]) for i in range(self._actual_num_wfms(session, channel_list))], [float(min_ctype[i]) for i in range(self._actual_num_wfms(session, channel_list))], [float(max_ctype[i]) for i in range(self._actual_num_wfms(session, channel_list))], [int(num_in_stats_ctype[i]) for i in range(self._actual_num_wfms(session, channel_list))]

    def _get_attribute_vi_boolean(self, session, channel_list, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library._get_attribute_vi_boolean(vi_ctype, channel_list_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(value_ctype.value)

    def _get_attribute_vi_int32(self, session, channel_list, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library._get_attribute_vi_int32(vi_ctype, channel_list_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def _get_attribute_vi_int64(self, session, channel_list, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt64()  # case S220
        error_code = self._library._get_attribute_vi_int64(vi_ctype, channel_list_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def _get_attribute_vi_real64(self, session, channel_list, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library._get_attribute_vi_real64(vi_ctype, channel_list_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(value_ctype.value)

    def _get_attribute_vi_string(self, session, channel_list, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buf_size_ctype = _visatype.ViInt32()  # case S170
        value_ctype = None  # case C050
        error_code = self._library._get_attribute_vi_string(vi_ctype, channel_list_ctype, attribute_id_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buf_size_ctype = _visatype.ViInt32(error_code)  # case S180
        value_ctype = (_visatype.ViChar * buf_size_ctype.value)()  # case C060
        error_code = self._library._get_attribute_vi_string(vi_ctype, channel_list_ctype, attribute_id_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return value_ctype.value.decode(self._encoding)

    def _get_equalization_filter_coefficients(self, session, channel, number_of_coefficients):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_ctype = ctypes.create_string_buffer(channel.encode(self._encoding))  # case C010
        number_of_coefficients_ctype = _visatype.ViInt32(number_of_coefficients)  # case S210
        coefficients_size = number_of_coefficients  # case B600
        coefficients_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=coefficients_size)  # case B600
        error_code = self._library._get_equalization_filter_coefficients(vi_ctype, channel_ctype, number_of_coefficients_ctype, coefficients_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(coefficients_ctype[i]) for i in range(number_of_coefficients_ctype.value)]

    def _get_error(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        error_code = self._library._get_error(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        description_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library._get_error(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), description_ctype.value.decode(self._encoding)

    def import_attribute_configuration_buffer(self, session, configuration):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_converted = _converters.convert_to_bytes(configuration)  # case B520
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_converted, library_type=_visatype.ViInt8)  # case B520
        error_code = self._library.import_attribute_configuration_buffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def import_attribute_configuration_file(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.import_attribute_configuration_file(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _init_with_options(self, session, resource_name, id_query=False, reset_device=False, option_string=""):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(_converters.convert_init_with_options_dictionary(option_string).encode(self._encoding))  # case C040
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library._init_with_options(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def _initiate_acquisition(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library._initiate_acquisition(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.lock(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def probe_compensation_signal_start(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.probe_compensation_signal_start(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def probe_compensation_signal_stop(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.probe_compensation_signal_stop(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _read(self, session, channel_list, num_samples, timeout=hightime.timedelta(seconds=5.0)):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        num_samples_ctype = _visatype.ViInt32(num_samples)  # case S150
        waveform_size = (num_samples * self._actual_num_wfms(session, channel_list))  # case B560
        waveform_array = array.array("d", [0] * waveform_size)  # case B560
        waveform_ctype = get_ctypes_pointer_for_buffer(value=waveform_array, library_type=_visatype.ViReal64)  # case B560
        wfm_info_size = self._actual_num_wfms(session, channel_list)  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        error_code = self._library._read(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, waveform_ctype, wfm_info_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_array, [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms(session, channel_list))]

    def reset_device(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.reset_device(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_defaults(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.reset_with_defaults(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_trigger_edge(self, session, which_trigger):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        which_trigger_ctype = _visatype.ViInt32(which_trigger.value)  # case S130
        error_code = self._library.send_software_trigger_edge(vi_ctype, which_trigger_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_boolean(self, session, channel_list, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViBoolean(value)  # case S150
        error_code = self._library._set_attribute_vi_boolean(vi_ctype, channel_list_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int32(self, session, channel_list, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt32(value)  # case S150
        error_code = self._library._set_attribute_vi_int32(vi_ctype, channel_list_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int64(self, session, channel_list, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt64(value)  # case S150
        error_code = self._library._set_attribute_vi_int64(vi_ctype, channel_list_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_real64(self, session, channel_list, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViReal64(value)  # case S150
        error_code = self._library._set_attribute_vi_real64(vi_ctype, channel_list_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, session, channel_list, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = ctypes.create_string_buffer(value.encode(self._encoding))  # case C020
        error_code = self._library._set_attribute_vi_string(vi_ctype, channel_list_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.unlock(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def _close(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library._close(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _error_message(self, session, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library._error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)

    def reset(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code = self._library.reset(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _self_test(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library._self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)
