# -*- coding: utf-8 -*-
# This file was generated

import array  # noqa: F401
import ctypes
import niscope._converters as _converters
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


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niScope_Abort_cfunc = None
        self.niScope_AcquisitionStatus_cfunc = None
        self.niScope_ActualMeasWfmSize_cfunc = None
        self.niScope_ActualNumWfms_cfunc = None
        self.niScope_AddWaveformProcessing_cfunc = None
        self.niScope_AutoSetup_cfunc = None
        self.niScope_CalFetchDate_cfunc = None
        self.niScope_CalFetchTemperature_cfunc = None
        self.niScope_CalSelfCalibrate_cfunc = None
        self.niScope_ClearWaveformMeasurementStats_cfunc = None
        self.niScope_ClearWaveformProcessing_cfunc = None
        self.niScope_Commit_cfunc = None
        self.niScope_ConfigureChanCharacteristics_cfunc = None
        self.niScope_ConfigureEqualizationFilterCoefficients_cfunc = None
        self.niScope_ConfigureHorizontalTiming_cfunc = None
        self.niScope_ConfigureRefLevels_cfunc = None
        self.niScope_ConfigureTriggerDigital_cfunc = None
        self.niScope_ConfigureTriggerEdge_cfunc = None
        self.niScope_ConfigureTriggerHysteresis_cfunc = None
        self.niScope_ConfigureTriggerImmediate_cfunc = None
        self.niScope_ConfigureTriggerSoftware_cfunc = None
        self.niScope_ConfigureTriggerVideo_cfunc = None
        self.niScope_ConfigureTriggerWindow_cfunc = None
        self.niScope_ConfigureVertical_cfunc = None
        self.niScope_Disable_cfunc = None
        self.niScope_ExportAttributeConfigurationBuffer_cfunc = None
        self.niScope_ExportAttributeConfigurationFile_cfunc = None
        self.niScope_Fetch_cfunc = None
        self.niScope_FetchArrayMeasurement_cfunc = None
        self.niScope_FetchBinary16_cfunc = None
        self.niScope_FetchBinary32_cfunc = None
        self.niScope_FetchBinary8_cfunc = None
        self.niScope_FetchMeasurementStats_cfunc = None
        self.niScope_GetAttributeViBoolean_cfunc = None
        self.niScope_GetAttributeViInt32_cfunc = None
        self.niScope_GetAttributeViInt64_cfunc = None
        self.niScope_GetAttributeViReal64_cfunc = None
        self.niScope_GetAttributeViString_cfunc = None
        self.niScope_GetEqualizationFilterCoefficients_cfunc = None
        self.niScope_GetError_cfunc = None
        self.niScope_ImportAttributeConfigurationBuffer_cfunc = None
        self.niScope_ImportAttributeConfigurationFile_cfunc = None
        self.niScope_InitWithOptions_cfunc = None
        self.niScope_InitiateAcquisition_cfunc = None
        self.niScope_LockSession_cfunc = None
        self.niScope_ProbeCompensationSignalStart_cfunc = None
        self.niScope_ProbeCompensationSignalStop_cfunc = None
        self.niScope_Read_cfunc = None
        self.niScope_ResetDevice_cfunc = None
        self.niScope_ResetWithDefaults_cfunc = None
        self.niScope_SendSoftwareTriggerEdge_cfunc = None
        self.niScope_SetAttributeViBoolean_cfunc = None
        self.niScope_SetAttributeViInt32_cfunc = None
        self.niScope_SetAttributeViInt64_cfunc = None
        self.niScope_SetAttributeViReal64_cfunc = None
        self.niScope_SetAttributeViString_cfunc = None
        self.niScope_UnlockSession_cfunc = None
        self.niScope_close_cfunc = None
        self.niScope_error_message_cfunc = None
        self.niScope_reset_cfunc = None
        self.niScope_self_test_cfunc = None

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

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
        with self._func_lock:
            if self.niScope_Abort_cfunc is None:
                self.niScope_Abort_cfunc = self._get_library_function('niScope_Abort')
                self.niScope_Abort_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_Abort_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_Abort_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def acquisition_status(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        acquisition_status_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niScope_AcquisitionStatus_cfunc is None:
                self.niScope_AcquisitionStatus_cfunc = self._get_library_function('niScope_AcquisitionStatus')
                self.niScope_AcquisitionStatus_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_AcquisitionStatus_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_AcquisitionStatus_cfunc(vi_ctype, None if acquisition_status_ctype is None else (ctypes.pointer(acquisition_status_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.AcquisitionStatus(acquisition_status_ctype.value)

    def _actual_meas_wfm_size(self, session, array_meas_function):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        array_meas_function_ctype = _visatype.ViInt32(array_meas_function.value)  # case S130
        meas_waveform_size_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niScope_ActualMeasWfmSize_cfunc is None:
                self.niScope_ActualMeasWfmSize_cfunc = self._get_library_function('niScope_ActualMeasWfmSize')
                self.niScope_ActualMeasWfmSize_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_ActualMeasWfmSize_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ActualMeasWfmSize_cfunc(vi_ctype, array_meas_function_ctype, None if meas_waveform_size_ctype is None else (ctypes.pointer(meas_waveform_size_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(meas_waveform_size_ctype.value)

    def _actual_num_wfms(self, session, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        num_wfms_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niScope_ActualNumWfms_cfunc is None:
                self.niScope_ActualNumWfms_cfunc = self._get_library_function('niScope_ActualNumWfms')
                self.niScope_ActualNumWfms_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_ActualNumWfms_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ActualNumWfms_cfunc(vi_ctype, channel_list_ctype, None if num_wfms_ctype is None else (ctypes.pointer(num_wfms_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(num_wfms_ctype.value)

    def add_waveform_processing(self, session, channel_list, meas_function):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        meas_function_ctype = _visatype.ViInt32(meas_function.value)  # case S130
        with self._func_lock:
            if self.niScope_AddWaveformProcessing_cfunc is None:
                self.niScope_AddWaveformProcessing_cfunc = self._get_library_function('niScope_AddWaveformProcessing')
                self.niScope_AddWaveformProcessing_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niScope_AddWaveformProcessing_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_AddWaveformProcessing_cfunc(vi_ctype, channel_list_ctype, meas_function_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def auto_setup(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niScope_AutoSetup_cfunc is None:
                self.niScope_AutoSetup_cfunc = self._get_library_function('niScope_AutoSetup')
                self.niScope_AutoSetup_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_AutoSetup_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_AutoSetup_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _cal_fetch_date(self, session, which_one):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        which_one_ctype = _visatype.ViInt32(which_one.value)  # case S130
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niScope_CalFetchDate_cfunc is None:
                self.niScope_CalFetchDate_cfunc = self._get_library_function('niScope_CalFetchDate')
                self.niScope_CalFetchDate_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_CalFetchDate_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_CalFetchDate_cfunc(vi_ctype, which_one_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value)

    def _cal_fetch_temperature(self, session, which_one):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        which_one_ctype = _visatype.ViInt32(which_one)  # case S150
        temperature_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niScope_CalFetchTemperature_cfunc is None:
                self.niScope_CalFetchTemperature_cfunc = self._get_library_function('niScope_CalFetchTemperature')
                self.niScope_CalFetchTemperature_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_CalFetchTemperature_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_CalFetchTemperature_cfunc(vi_ctype, which_one_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def self_cal(self, session, channel_list, option):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        option_ctype = _visatype.ViInt32(option.value)  # case S130
        with self._func_lock:
            if self.niScope_CalSelfCalibrate_cfunc is None:
                self.niScope_CalSelfCalibrate_cfunc = self._get_library_function('niScope_CalSelfCalibrate')
                self.niScope_CalSelfCalibrate_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niScope_CalSelfCalibrate_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_CalSelfCalibrate_cfunc(vi_ctype, channel_list_ctype, option_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_waveform_measurement_stats(self, session, channel_list, clearable_measurement_function):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        clearable_measurement_function_ctype = _visatype.ViInt32(clearable_measurement_function.value)  # case S130
        with self._func_lock:
            if self.niScope_ClearWaveformMeasurementStats_cfunc is None:
                self.niScope_ClearWaveformMeasurementStats_cfunc = self._get_library_function('niScope_ClearWaveformMeasurementStats')
                self.niScope_ClearWaveformMeasurementStats_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niScope_ClearWaveformMeasurementStats_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ClearWaveformMeasurementStats_cfunc(vi_ctype, channel_list_ctype, clearable_measurement_function_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_waveform_processing(self, session, channel_list):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        with self._func_lock:
            if self.niScope_ClearWaveformProcessing_cfunc is None:
                self.niScope_ClearWaveformProcessing_cfunc = self._get_library_function('niScope_ClearWaveformProcessing')
                self.niScope_ClearWaveformProcessing_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_ClearWaveformProcessing_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ClearWaveformProcessing_cfunc(vi_ctype, channel_list_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def commit(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niScope_Commit_cfunc is None:
                self.niScope_Commit_cfunc = self._get_library_function('niScope_Commit')
                self.niScope_Commit_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_Commit_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_Commit_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_chan_characteristics(self, session, channel_list, input_impedance, max_input_frequency):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        input_impedance_ctype = _visatype.ViReal64(input_impedance)  # case S150
        max_input_frequency_ctype = _visatype.ViReal64(max_input_frequency)  # case S150
        with self._func_lock:
            if self.niScope_ConfigureChanCharacteristics_cfunc is None:
                self.niScope_ConfigureChanCharacteristics_cfunc = self._get_library_function('niScope_ConfigureChanCharacteristics')
                self.niScope_ConfigureChanCharacteristics_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureChanCharacteristics_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ConfigureChanCharacteristics_cfunc(vi_ctype, channel_list_ctype, input_impedance_ctype, max_input_frequency_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_equalization_filter_coefficients(self, session, channel_list, coefficients):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        number_of_coefficients_ctype = _visatype.ViInt32(0 if coefficients is None else len(coefficients))  # case S160
        coefficients_ctype = get_ctypes_pointer_for_buffer(value=coefficients, library_type=_visatype.ViReal64)  # case B550
        with self._func_lock:
            if self.niScope_ConfigureEqualizationFilterCoefficients_cfunc is None:
                self.niScope_ConfigureEqualizationFilterCoefficients_cfunc = self._get_library_function('niScope_ConfigureEqualizationFilterCoefficients')
                self.niScope_ConfigureEqualizationFilterCoefficients_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_ConfigureEqualizationFilterCoefficients_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ConfigureEqualizationFilterCoefficients_cfunc(vi_ctype, channel_list_ctype, number_of_coefficients_ctype, coefficients_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_horizontal_timing(self, session, min_sample_rate, min_num_pts, ref_position, num_records, enforce_realtime):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        min_sample_rate_ctype = _visatype.ViReal64(min_sample_rate)  # case S150
        min_num_pts_ctype = _visatype.ViInt32(min_num_pts)  # case S150
        ref_position_ctype = _visatype.ViReal64(ref_position)  # case S150
        num_records_ctype = _visatype.ViInt32(num_records)  # case S150
        enforce_realtime_ctype = _visatype.ViBoolean(enforce_realtime)  # case S150
        with self._func_lock:
            if self.niScope_ConfigureHorizontalTiming_cfunc is None:
                self.niScope_ConfigureHorizontalTiming_cfunc = self._get_library_function('niScope_ConfigureHorizontalTiming')
                self.niScope_ConfigureHorizontalTiming_cfunc.argtypes = [ViSession, ViReal64, ViInt32, ViReal64, ViInt32, ViBoolean]  # noqa: F405
                self.niScope_ConfigureHorizontalTiming_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ConfigureHorizontalTiming_cfunc(vi_ctype, min_sample_rate_ctype, min_num_pts_ctype, ref_position_ctype, num_records_ctype, enforce_realtime_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _configure_ref_levels(self, session, low, mid, high):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        low_ctype = _visatype.ViReal64(low)  # case S150
        mid_ctype = _visatype.ViReal64(mid)  # case S150
        high_ctype = _visatype.ViReal64(high)  # case S150
        with self._func_lock:
            if self.niScope_ConfigureRefLevels_cfunc is None:
                self.niScope_ConfigureRefLevels_cfunc = self._get_library_function('niScope_ConfigureRefLevels')
                self.niScope_ConfigureRefLevels_cfunc.argtypes = [ViSession, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureRefLevels_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ConfigureRefLevels_cfunc(vi_ctype, low_ctype, mid_ctype, high_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_digital(self, session, trigger_source, slope, holdoff, delay):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(session._encoding))  # case C020
        slope_ctype = _visatype.ViInt32(slope.value)  # case S130
        holdoff_ctype = _converters.convert_timedelta_to_seconds_real64(holdoff)  # case S140
        delay_ctype = _converters.convert_timedelta_to_seconds_real64(delay)  # case S140
        with self._func_lock:
            if self.niScope_ConfigureTriggerDigital_cfunc is None:
                self.niScope_ConfigureTriggerDigital_cfunc = self._get_library_function('niScope_ConfigureTriggerDigital')
                self.niScope_ConfigureTriggerDigital_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerDigital_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ConfigureTriggerDigital_cfunc(vi_ctype, trigger_source_ctype, slope_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_edge(self, session, trigger_source, level, slope, trigger_coupling, holdoff, delay):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(session._encoding))  # case C020
        level_ctype = _visatype.ViReal64(level)  # case S150
        slope_ctype = _visatype.ViInt32(slope.value)  # case S130
        trigger_coupling_ctype = _visatype.ViInt32(trigger_coupling.value)  # case S130
        holdoff_ctype = _converters.convert_timedelta_to_seconds_real64(holdoff)  # case S140
        delay_ctype = _converters.convert_timedelta_to_seconds_real64(delay)  # case S140
        with self._func_lock:
            if self.niScope_ConfigureTriggerEdge_cfunc is None:
                self.niScope_ConfigureTriggerEdge_cfunc = self._get_library_function('niScope_ConfigureTriggerEdge')
                self.niScope_ConfigureTriggerEdge_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerEdge_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ConfigureTriggerEdge_cfunc(vi_ctype, trigger_source_ctype, level_ctype, slope_ctype, trigger_coupling_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_hysteresis(self, session, trigger_source, level, hysteresis, slope, trigger_coupling, holdoff, delay):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(session._encoding))  # case C020
        level_ctype = _visatype.ViReal64(level)  # case S150
        hysteresis_ctype = _visatype.ViReal64(hysteresis)  # case S150
        slope_ctype = _visatype.ViInt32(slope.value)  # case S130
        trigger_coupling_ctype = _visatype.ViInt32(trigger_coupling.value)  # case S130
        holdoff_ctype = _converters.convert_timedelta_to_seconds_real64(holdoff)  # case S140
        delay_ctype = _converters.convert_timedelta_to_seconds_real64(delay)  # case S140
        with self._func_lock:
            if self.niScope_ConfigureTriggerHysteresis_cfunc is None:
                self.niScope_ConfigureTriggerHysteresis_cfunc = self._get_library_function('niScope_ConfigureTriggerHysteresis')
                self.niScope_ConfigureTriggerHysteresis_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64, ViInt32, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerHysteresis_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ConfigureTriggerHysteresis_cfunc(vi_ctype, trigger_source_ctype, level_ctype, hysteresis_ctype, slope_ctype, trigger_coupling_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_immediate(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niScope_ConfigureTriggerImmediate_cfunc is None:
                self.niScope_ConfigureTriggerImmediate_cfunc = self._get_library_function('niScope_ConfigureTriggerImmediate')
                self.niScope_ConfigureTriggerImmediate_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ConfigureTriggerImmediate_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ConfigureTriggerImmediate_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_software(self, session, holdoff, delay):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        holdoff_ctype = _converters.convert_timedelta_to_seconds_real64(holdoff)  # case S140
        delay_ctype = _converters.convert_timedelta_to_seconds_real64(delay)  # case S140
        with self._func_lock:
            if self.niScope_ConfigureTriggerSoftware_cfunc is None:
                self.niScope_ConfigureTriggerSoftware_cfunc = self._get_library_function('niScope_ConfigureTriggerSoftware')
                self.niScope_ConfigureTriggerSoftware_cfunc.argtypes = [ViSession, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerSoftware_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ConfigureTriggerSoftware_cfunc(vi_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_video(self, session, trigger_source, enable_dc_restore, signal_format, event, line_number, polarity, trigger_coupling, holdoff, delay):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(session._encoding))  # case C020
        enable_dc_restore_ctype = _visatype.ViBoolean(enable_dc_restore)  # case S150
        signal_format_ctype = _visatype.ViInt32(signal_format.value)  # case S130
        event_ctype = _visatype.ViInt32(event.value)  # case S130
        line_number_ctype = _visatype.ViInt32(line_number)  # case S150
        polarity_ctype = _visatype.ViInt32(polarity.value)  # case S130
        trigger_coupling_ctype = _visatype.ViInt32(trigger_coupling.value)  # case S130
        holdoff_ctype = _converters.convert_timedelta_to_seconds_real64(holdoff)  # case S140
        delay_ctype = _converters.convert_timedelta_to_seconds_real64(delay)  # case S140
        with self._func_lock:
            if self.niScope_ConfigureTriggerVideo_cfunc is None:
                self.niScope_ConfigureTriggerVideo_cfunc = self._get_library_function('niScope_ConfigureTriggerVideo')
                self.niScope_ConfigureTriggerVideo_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean, ViInt32, ViInt32, ViInt32, ViInt32, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerVideo_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ConfigureTriggerVideo_cfunc(vi_ctype, trigger_source_ctype, enable_dc_restore_ctype, signal_format_ctype, event_ctype, line_number_ctype, polarity_ctype, trigger_coupling_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_trigger_window(self, session, trigger_source, low_level, high_level, window_mode, trigger_coupling, holdoff, delay):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        trigger_source_ctype = ctypes.create_string_buffer(trigger_source.encode(session._encoding))  # case C020
        low_level_ctype = _visatype.ViReal64(low_level)  # case S150
        high_level_ctype = _visatype.ViReal64(high_level)  # case S150
        window_mode_ctype = _visatype.ViInt32(window_mode.value)  # case S130
        trigger_coupling_ctype = _visatype.ViInt32(trigger_coupling.value)  # case S130
        holdoff_ctype = _converters.convert_timedelta_to_seconds_real64(holdoff)  # case S140
        delay_ctype = _converters.convert_timedelta_to_seconds_real64(delay)  # case S140
        with self._func_lock:
            if self.niScope_ConfigureTriggerWindow_cfunc is None:
                self.niScope_ConfigureTriggerWindow_cfunc = self._get_library_function('niScope_ConfigureTriggerWindow')
                self.niScope_ConfigureTriggerWindow_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64, ViInt32, ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niScope_ConfigureTriggerWindow_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ConfigureTriggerWindow_cfunc(vi_ctype, trigger_source_ctype, low_level_ctype, high_level_ctype, window_mode_ctype, trigger_coupling_ctype, holdoff_ctype, delay_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_vertical(self, session, channel_list, range, offset, coupling, probe_attenuation, enabled):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        range_ctype = _visatype.ViReal64(range)  # case S150
        offset_ctype = _visatype.ViReal64(offset)  # case S150
        coupling_ctype = _visatype.ViInt32(coupling.value)  # case S130
        probe_attenuation_ctype = _visatype.ViReal64(probe_attenuation)  # case S150
        enabled_ctype = _visatype.ViBoolean(enabled)  # case S150
        with self._func_lock:
            if self.niScope_ConfigureVertical_cfunc is None:
                self.niScope_ConfigureVertical_cfunc = self._get_library_function('niScope_ConfigureVertical')
                self.niScope_ConfigureVertical_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViReal64, ViInt32, ViReal64, ViBoolean]  # noqa: F405
                self.niScope_ConfigureVertical_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ConfigureVertical_cfunc(vi_ctype, channel_list_ctype, range_ctype, offset_ctype, coupling_ctype, probe_attenuation_ctype, enabled_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niScope_Disable_cfunc is None:
                self.niScope_Disable_cfunc = self._get_library_function('niScope_Disable')
                self.niScope_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_Disable_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_Disable_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_attribute_configuration_buffer(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32()  # case S170
        configuration_ctype = None  # case B580
        with self._func_lock:
            if self.niScope_ExportAttributeConfigurationBuffer_cfunc is None:
                self.niScope_ExportAttributeConfigurationBuffer_cfunc = self._get_library_function('niScope_ExportAttributeConfigurationBuffer')
                self.niScope_ExportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niScope_ExportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ExportAttributeConfigurationBuffer_cfunc(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        size_in_bytes_ctype = _visatype.ViInt32(error_code)  # case S180
        configuration_size = size_in_bytes_ctype.value  # case B590
        configuration_array = array.array("b", [0] * configuration_size)  # case B590
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self.niScope_ExportAttributeConfigurationBuffer_cfunc(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_to_bytes(configuration_array)

    def export_attribute_configuration_file(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niScope_ExportAttributeConfigurationFile_cfunc is None:
                self.niScope_ExportAttributeConfigurationFile_cfunc = self._get_library_function('niScope_ExportAttributeConfigurationFile')
                self.niScope_ExportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_ExportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ExportAttributeConfigurationFile_cfunc(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _fetch(self, session, channel_list, timeout, num_samples):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        num_samples_ctype = _visatype.ViInt32(num_samples)  # case S150
        waveform_size = (num_samples * self._actual_num_wfms())  # case B560
        waveform_array = array.array("d", [0] * waveform_size)  # case B560
        waveform_ctype = get_ctypes_pointer_for_buffer(value=waveform_array, library_type=_visatype.ViReal64)  # case B560
        wfm_info_size = self._actual_num_wfms()  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        with self._func_lock:
            if self.niScope_Fetch_cfunc is None:
                self.niScope_Fetch_cfunc = self._get_library_function('niScope_Fetch')
                self.niScope_Fetch_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(waveform_info.struct_niScope_wfmInfo)]  # noqa: F405
                self.niScope_Fetch_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_Fetch_cfunc(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, waveform_ctype, wfm_info_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_array, [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms())]

    def _fetch_into_numpy(self, session, num_samples, waveform, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        num_samples_ctype = _visatype.ViInt32(num_samples)  # case S150
        waveform_ctype = get_ctypes_pointer_for_buffer(value=waveform)  # case B510
        wfm_info_size = self._actual_num_wfms()  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        with self._func_lock:
            if self.niScope_Fetch_cfunc is None:
                self.niScope_Fetch_cfunc = self._get_library_function('niScope_Fetch')
                self.niScope_Fetch_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(waveform_info.struct_niScope_wfmInfo)]  # noqa: F405
                self.niScope_Fetch_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_Fetch_cfunc(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, waveform_ctype, wfm_info_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms())]

    def _fetch_array_measurement(self, session, channel_list, timeout, array_meas_function, measurement_waveform_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        array_meas_function_ctype = _visatype.ViInt32(array_meas_function.value)  # case S130
        measurement_waveform_size_ctype = _visatype.ViInt32(measurement_waveform_size)  # case S150
        meas_wfm_size = (measurement_waveform_size * self._actual_num_wfms())  # case B560
        meas_wfm_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=meas_wfm_size)  # case B560
        wfm_info_size = self._actual_num_wfms()  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        with self._func_lock:
            if self.niScope_FetchArrayMeasurement_cfunc is None:
                self.niScope_FetchArrayMeasurement_cfunc = self._get_library_function('niScope_FetchArrayMeasurement')
                self.niScope_FetchArrayMeasurement_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(waveform_info.struct_niScope_wfmInfo)]  # noqa: F405
                self.niScope_FetchArrayMeasurement_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_FetchArrayMeasurement_cfunc(vi_ctype, channel_list_ctype, timeout_ctype, array_meas_function_ctype, measurement_waveform_size_ctype, meas_wfm_ctype, wfm_info_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(meas_wfm_ctype[i]) for i in range((measurement_waveform_size * self._actual_num_wfms()))], [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms())]

    def _fetch_binary16_into_numpy(self, session, num_samples, waveform, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        num_samples_ctype = _visatype.ViInt32(num_samples)  # case S150
        waveform_ctype = get_ctypes_pointer_for_buffer(value=waveform)  # case B510
        wfm_info_size = self._actual_num_wfms()  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        with self._func_lock:
            if self.niScope_FetchBinary16_cfunc is None:
                self.niScope_FetchBinary16_cfunc = self._get_library_function('niScope_FetchBinary16')
                self.niScope_FetchBinary16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViInt16), ctypes.POINTER(waveform_info.struct_niScope_wfmInfo)]  # noqa: F405
                self.niScope_FetchBinary16_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_FetchBinary16_cfunc(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, waveform_ctype, wfm_info_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms())]

    def _fetch_binary32_into_numpy(self, session, num_samples, waveform, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        num_samples_ctype = _visatype.ViInt32(num_samples)  # case S150
        waveform_ctype = get_ctypes_pointer_for_buffer(value=waveform)  # case B510
        wfm_info_size = self._actual_num_wfms()  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        with self._func_lock:
            if self.niScope_FetchBinary32_cfunc is None:
                self.niScope_FetchBinary32_cfunc = self._get_library_function('niScope_FetchBinary32')
                self.niScope_FetchBinary32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(waveform_info.struct_niScope_wfmInfo)]  # noqa: F405
                self.niScope_FetchBinary32_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_FetchBinary32_cfunc(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, waveform_ctype, wfm_info_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms())]

    def _fetch_binary8_into_numpy(self, session, num_samples, waveform, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        num_samples_ctype = _visatype.ViInt32(num_samples)  # case S150
        waveform_ctype = get_ctypes_pointer_for_buffer(value=waveform)  # case B510
        wfm_info_size = self._actual_num_wfms()  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        with self._func_lock:
            if self.niScope_FetchBinary8_cfunc is None:
                self.niScope_FetchBinary8_cfunc = self._get_library_function('niScope_FetchBinary8')
                self.niScope_FetchBinary8_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViInt8), ctypes.POINTER(waveform_info.struct_niScope_wfmInfo)]  # noqa: F405
                self.niScope_FetchBinary8_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_FetchBinary8_cfunc(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, waveform_ctype, wfm_info_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms())]

    def _fetch_measurement_stats(self, session, channel_list, timeout, scalar_meas_function):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        scalar_meas_function_ctype = _visatype.ViInt32(scalar_meas_function.value)  # case S130
        result_size = self._actual_num_wfms()  # case B560
        result_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=result_size)  # case B560
        mean_size = self._actual_num_wfms()  # case B560
        mean_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=mean_size)  # case B560
        stdev_size = self._actual_num_wfms()  # case B560
        stdev_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=stdev_size)  # case B560
        min_size = self._actual_num_wfms()  # case B560
        min_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=min_size)  # case B560
        max_size = self._actual_num_wfms()  # case B560
        max_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=max_size)  # case B560
        num_in_stats_size = self._actual_num_wfms()  # case B560
        num_in_stats_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=num_in_stats_size)  # case B560
        with self._func_lock:
            if self.niScope_FetchMeasurementStats_cfunc is None:
                self.niScope_FetchMeasurementStats_cfunc = self._get_library_function('niScope_FetchMeasurementStats')
                self.niScope_FetchMeasurementStats_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_FetchMeasurementStats_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_FetchMeasurementStats_cfunc(vi_ctype, channel_list_ctype, timeout_ctype, scalar_meas_function_ctype, result_ctype, mean_ctype, stdev_ctype, min_ctype, max_ctype, num_in_stats_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(result_ctype[i]) for i in range(self._actual_num_wfms())], [float(mean_ctype[i]) for i in range(self._actual_num_wfms())], [float(stdev_ctype[i]) for i in range(self._actual_num_wfms())], [float(min_ctype[i]) for i in range(self._actual_num_wfms())], [float(max_ctype[i]) for i in range(self._actual_num_wfms())], [int(num_in_stats_ctype[i]) for i in range(self._actual_num_wfms())]

    def _get_attribute_vi_boolean(self, session, channel_list, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niScope_GetAttributeViBoolean_cfunc is None:
                self.niScope_GetAttributeViBoolean_cfunc = self._get_library_function('niScope_GetAttributeViBoolean')
                self.niScope_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niScope_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_GetAttributeViBoolean_cfunc(vi_ctype, channel_list_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(value_ctype.value)

    def _get_attribute_vi_int32(self, session, channel_list, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niScope_GetAttributeViInt32_cfunc is None:
                self.niScope_GetAttributeViInt32_cfunc = self._get_library_function('niScope_GetAttributeViInt32')
                self.niScope_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niScope_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_GetAttributeViInt32_cfunc(vi_ctype, channel_list_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def _get_attribute_vi_int64(self, session, channel_list, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt64()  # case S220
        with self._func_lock:
            if self.niScope_GetAttributeViInt64_cfunc is None:
                self.niScope_GetAttributeViInt64_cfunc = self._get_library_function('niScope_GetAttributeViInt64')
                self.niScope_GetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niScope_GetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_GetAttributeViInt64_cfunc(vi_ctype, channel_list_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(value_ctype.value)

    def _get_attribute_vi_real64(self, session, channel_list, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niScope_GetAttributeViReal64_cfunc is None:
                self.niScope_GetAttributeViReal64_cfunc = self._get_library_function('niScope_GetAttributeViReal64')
                self.niScope_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_GetAttributeViReal64_cfunc(vi_ctype, channel_list_ctype, attribute_id_ctype, None if value_ctype is None else (ctypes.pointer(value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(value_ctype.value)

    def _get_attribute_vi_string(self, session, channel_list, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buf_size_ctype = _visatype.ViInt32()  # case S170
        value_ctype = None  # case C050
        with self._func_lock:
            if self.niScope_GetAttributeViString_cfunc is None:
                self.niScope_GetAttributeViString_cfunc = self._get_library_function('niScope_GetAttributeViString')
                self.niScope_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_GetAttributeViString_cfunc(vi_ctype, channel_list_ctype, attribute_id_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buf_size_ctype = _visatype.ViInt32(error_code)  # case S180
        value_ctype = (_visatype.ViChar * buf_size_ctype.value)()  # case C060
        error_code = self.niScope_GetAttributeViString_cfunc(vi_ctype, channel_list_ctype, attribute_id_ctype, buf_size_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return value_ctype.value.decode(session._encoding)

    def _get_equalization_filter_coefficients(self, session, channel, number_of_coefficients):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_ctype = ctypes.create_string_buffer(channel.encode(session._encoding))  # case C010
        number_of_coefficients_ctype = _visatype.ViInt32(number_of_coefficients)  # case S210
        coefficients_size = number_of_coefficients  # case B600
        coefficients_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViReal64, size=coefficients_size)  # case B600
        with self._func_lock:
            if self.niScope_GetEqualizationFilterCoefficients_cfunc is None:
                self.niScope_GetEqualizationFilterCoefficients_cfunc = self._get_library_function('niScope_GetEqualizationFilterCoefficients')
                self.niScope_GetEqualizationFilterCoefficients_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niScope_GetEqualizationFilterCoefficients_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_GetEqualizationFilterCoefficients_cfunc(vi_ctype, channel_ctype, number_of_coefficients_ctype, coefficients_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [float(coefficients_ctype[i]) for i in range(number_of_coefficients_ctype.value)]

    def _get_error(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        with self._func_lock:
            if self.niScope_GetError_cfunc is None:
                self.niScope_GetError_cfunc = self._get_library_function('niScope_GetError')
                self.niScope_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_GetError_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_GetError_cfunc(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        description_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self.niScope_GetError_cfunc(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), description_ctype.value.decode(session._encoding)

    def import_attribute_configuration_buffer(self, session, configuration):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_converted = _converters.convert_to_bytes(configuration)  # case B520
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_converted, library_type=_visatype.ViInt8)  # case B520
        with self._func_lock:
            if self.niScope_ImportAttributeConfigurationBuffer_cfunc is None:
                self.niScope_ImportAttributeConfigurationBuffer_cfunc = self._get_library_function('niScope_ImportAttributeConfigurationBuffer')
                self.niScope_ImportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niScope_ImportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ImportAttributeConfigurationBuffer_cfunc(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def import_attribute_configuration_file(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niScope_ImportAttributeConfigurationFile_cfunc is None:
                self.niScope_ImportAttributeConfigurationFile_cfunc = self._get_library_function('niScope_ImportAttributeConfigurationFile')
                self.niScope_ImportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_ImportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ImportAttributeConfigurationFile_cfunc(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _init_with_options(self, session, resource_name, id_query, reset_device, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(session._encoding))  # case C020
        id_query_ctype = _visatype.ViBoolean(id_query)  # case S150
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(_converters.convert_init_with_options_dictionary(option_string).encode(session._encoding))  # case C040
        vi_ctype = _visatype.ViSession()  # case S220
        with self._func_lock:
            if self.niScope_InitWithOptions_cfunc is None:
                self.niScope_InitWithOptions_cfunc = self._get_library_function('niScope_InitWithOptions')
                self.niScope_InitWithOptions_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niScope_InitWithOptions_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_InitWithOptions_cfunc(resource_name_ctype, id_query_ctype, reset_device_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def _initiate_acquisition(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niScope_InitiateAcquisition_cfunc is None:
                self.niScope_InitiateAcquisition_cfunc = self._get_library_function('niScope_InitiateAcquisition')
                self.niScope_InitiateAcquisition_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_InitiateAcquisition_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_InitiateAcquisition_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niScope_LockSession_cfunc is None:
                self.niScope_LockSession_cfunc = self._get_library_function('niScope_LockSession')
                self.niScope_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niScope_LockSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_LockSession_cfunc(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def probe_compensation_signal_start(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niScope_ProbeCompensationSignalStart_cfunc is None:
                self.niScope_ProbeCompensationSignalStart_cfunc = self._get_library_function('niScope_ProbeCompensationSignalStart')
                self.niScope_ProbeCompensationSignalStart_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ProbeCompensationSignalStart_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ProbeCompensationSignalStart_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def probe_compensation_signal_stop(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niScope_ProbeCompensationSignalStop_cfunc is None:
                self.niScope_ProbeCompensationSignalStop_cfunc = self._get_library_function('niScope_ProbeCompensationSignalStop')
                self.niScope_ProbeCompensationSignalStop_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ProbeCompensationSignalStop_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ProbeCompensationSignalStop_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _read(self, session, channel_list, timeout, num_samples):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        num_samples_ctype = _visatype.ViInt32(num_samples)  # case S150
        waveform_size = (num_samples * self._actual_num_wfms())  # case B560
        waveform_array = array.array("d", [0] * waveform_size)  # case B560
        waveform_ctype = get_ctypes_pointer_for_buffer(value=waveform_array, library_type=_visatype.ViReal64)  # case B560
        wfm_info_size = self._actual_num_wfms()  # case B560
        wfm_info_ctype = get_ctypes_pointer_for_buffer(library_type=waveform_info.struct_niScope_wfmInfo, size=wfm_info_size)  # case B560
        with self._func_lock:
            if self.niScope_Read_cfunc is None:
                self.niScope_Read_cfunc = self._get_library_function('niScope_Read')
                self.niScope_Read_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(waveform_info.struct_niScope_wfmInfo)]  # noqa: F405
                self.niScope_Read_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_Read_cfunc(vi_ctype, channel_list_ctype, timeout_ctype, num_samples_ctype, waveform_ctype, wfm_info_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return waveform_array, [waveform_info.WaveformInfo(wfm_info_ctype[i]) for i in range(self._actual_num_wfms())]

    def reset_device(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niScope_ResetDevice_cfunc is None:
                self.niScope_ResetDevice_cfunc = self._get_library_function('niScope_ResetDevice')
                self.niScope_ResetDevice_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ResetDevice_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ResetDevice_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_defaults(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niScope_ResetWithDefaults_cfunc is None:
                self.niScope_ResetWithDefaults_cfunc = self._get_library_function('niScope_ResetWithDefaults')
                self.niScope_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_ResetWithDefaults_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_trigger_edge(self, session, which_trigger):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        which_trigger_ctype = _visatype.ViInt32(which_trigger.value)  # case S130
        with self._func_lock:
            if self.niScope_SendSoftwareTriggerEdge_cfunc is None:
                self.niScope_SendSoftwareTriggerEdge_cfunc = self._get_library_function('niScope_SendSoftwareTriggerEdge')
                self.niScope_SendSoftwareTriggerEdge_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niScope_SendSoftwareTriggerEdge_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_SendSoftwareTriggerEdge_cfunc(vi_ctype, which_trigger_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_boolean(self, session, channel_list, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViBoolean(value)  # case S150
        with self._func_lock:
            if self.niScope_SetAttributeViBoolean_cfunc is None:
                self.niScope_SetAttributeViBoolean_cfunc = self._get_library_function('niScope_SetAttributeViBoolean')
                self.niScope_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niScope_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_SetAttributeViBoolean_cfunc(vi_ctype, channel_list_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int32(self, session, channel_list, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt32(value)  # case S150
        with self._func_lock:
            if self.niScope_SetAttributeViInt32_cfunc is None:
                self.niScope_SetAttributeViInt32_cfunc = self._get_library_function('niScope_SetAttributeViInt32')
                self.niScope_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niScope_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_SetAttributeViInt32_cfunc(vi_ctype, channel_list_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int64(self, session, channel_list, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViInt64(value)  # case S150
        with self._func_lock:
            if self.niScope_SetAttributeViInt64_cfunc is None:
                self.niScope_SetAttributeViInt64_cfunc = self._get_library_function('niScope_SetAttributeViInt64')
                self.niScope_SetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niScope_SetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_SetAttributeViInt64_cfunc(vi_ctype, channel_list_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_real64(self, session, channel_list, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = _visatype.ViReal64(value)  # case S150
        with self._func_lock:
            if self.niScope_SetAttributeViReal64_cfunc is None:
                self.niScope_SetAttributeViReal64_cfunc = self._get_library_function('niScope_SetAttributeViReal64')
                self.niScope_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niScope_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_SetAttributeViReal64_cfunc(vi_ctype, channel_list_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, session, channel_list, attribute_id, value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_list_ctype = ctypes.create_string_buffer(channel_list.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        value_ctype = ctypes.create_string_buffer(value.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niScope_SetAttributeViString_cfunc is None:
                self.niScope_SetAttributeViString_cfunc = self._get_library_function('niScope_SetAttributeViString')
                self.niScope_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_SetAttributeViString_cfunc(vi_ctype, channel_list_ctype, attribute_id_ctype, value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niScope_UnlockSession_cfunc is None:
                self.niScope_UnlockSession_cfunc = self._get_library_function('niScope_UnlockSession')
                self.niScope_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niScope_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_UnlockSession_cfunc(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def _close(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niScope_close_cfunc is None:
                self.niScope_close_cfunc = self._get_library_function('niScope_close')
                self.niScope_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_close_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_close_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _error_message(self, session, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        with self._func_lock:
            if self.niScope_error_message_cfunc is None:
                self.niScope_error_message_cfunc = self._get_library_function('niScope_error_message')
                self.niScope_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_error_message_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_error_message_cfunc(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(session._encoding)

    def reset(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niScope_reset_cfunc is None:
                self.niScope_reset_cfunc = self._get_library_function('niScope_reset')
                self.niScope_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niScope_reset_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_reset_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _self_test(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        with self._func_lock:
            if self.niScope_self_test_cfunc is None:
                self.niScope_self_test_cfunc = self._get_library_function('niScope_self_test')
                self.niScope_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niScope_self_test_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niScope_self_test_cfunc(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(session._encoding)
