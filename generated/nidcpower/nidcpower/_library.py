# -*- coding: utf-8 -*-
# This file was generated

import array  # noqa: F401
import ctypes
import nidcpower._converters as _converters
import nidcpower._visatype as _visatype
import nidcpower.enums as enums
import nidcpower.errors as errors
import threading

from nidcpower._visatype import *  # noqa: F403,H303

import nidcpower.lcr_load_compensation_spot as lcr_load_compensation_spot  # noqa: F401

import nidcpower.lcr_measurement as lcr_measurement  # noqa: F401


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
        self.niDCPower_AbortWithChannels_cfunc = None
        self.niDCPower_CalSelfCalibrate_cfunc = None
        self.niDCPower_ClearLatchedOutputCutoffState_cfunc = None
        self.niDCPower_CommitWithChannels_cfunc = None
        self.niDCPower_ConfigureApertureTime_cfunc = None
        self.niDCPower_ConfigureLCRCustomCableCompensation_cfunc = None
        self.niDCPower_CreateAdvancedSequenceCommitStepWithChannels_cfunc = None
        self.niDCPower_CreateAdvancedSequenceStepWithChannels_cfunc = None
        self.niDCPower_CreateAdvancedSequenceWithChannels_cfunc = None
        self.niDCPower_DeleteAdvancedSequenceWithChannels_cfunc = None
        self.niDCPower_Disable_cfunc = None
        self.niDCPower_ExportAttributeConfigurationBuffer_cfunc = None
        self.niDCPower_ExportAttributeConfigurationFile_cfunc = None
        self.niDCPower_FancyInitialize_cfunc = None
        self.niDCPower_FetchMultiple_cfunc = None
        self.niDCPower_FetchMultipleLCR_cfunc = None
        self.niDCPower_GetAttributeViBoolean_cfunc = None
        self.niDCPower_GetAttributeViInt32_cfunc = None
        self.niDCPower_GetAttributeViInt64_cfunc = None
        self.niDCPower_GetAttributeViReal64_cfunc = None
        self.niDCPower_GetAttributeViString_cfunc = None
        self.niDCPower_GetChannelName_cfunc = None
        self.niDCPower_GetChannelNameFromString_cfunc = None
        self.niDCPower_GetError_cfunc = None
        self.niDCPower_GetExtCalLastDateAndTime_cfunc = None
        self.niDCPower_GetExtCalLastTemp_cfunc = None
        self.niDCPower_GetExtCalRecommendedInterval_cfunc = None
        self.niDCPower_GetLCRCompensationLastDateAndTime_cfunc = None
        self.niDCPower_GetLCRCustomCableCompensationData_cfunc = None
        self.niDCPower_GetSelfCalLastDateAndTime_cfunc = None
        self.niDCPower_GetSelfCalLastTemp_cfunc = None
        self.niDCPower_ImportAttributeConfigurationBuffer_cfunc = None
        self.niDCPower_ImportAttributeConfigurationFile_cfunc = None
        self.niDCPower_InitializeWithChannels_cfunc = None
        self.niDCPower_InitializeWithIndependentChannels_cfunc = None
        self.niDCPower_InitiateWithChannels_cfunc = None
        self.niDCPower_LockSession_cfunc = None
        self.niDCPower_Measure_cfunc = None
        self.niDCPower_MeasureMultiple_cfunc = None
        self.niDCPower_MeasureMultipleLCR_cfunc = None
        self.niDCPower_ParseChannelCount_cfunc = None
        self.niDCPower_PerformLCRLoadCompensation_cfunc = None
        self.niDCPower_PerformLCROpenCompensation_cfunc = None
        self.niDCPower_PerformLCROpenCustomCableCompensation_cfunc = None
        self.niDCPower_PerformLCRShortCompensation_cfunc = None
        self.niDCPower_PerformLCRShortCustomCableCompensation_cfunc = None
        self.niDCPower_QueryInCompliance_cfunc = None
        self.niDCPower_QueryLatchedOutputCutoffState_cfunc = None
        self.niDCPower_QueryMaxCurrentLimit_cfunc = None
        self.niDCPower_QueryMaxVoltageLevel_cfunc = None
        self.niDCPower_QueryMinCurrentLimit_cfunc = None
        self.niDCPower_QueryOutputState_cfunc = None
        self.niDCPower_ReadCurrentTemperature_cfunc = None
        self.niDCPower_ResetDevice_cfunc = None
        self.niDCPower_ResetWithChannels_cfunc = None
        self.niDCPower_ResetWithDefaults_cfunc = None
        self.niDCPower_SendSoftwareEdgeTriggerWithChannels_cfunc = None
        self.niDCPower_SetAttributeViBoolean_cfunc = None
        self.niDCPower_SetAttributeViInt32_cfunc = None
        self.niDCPower_SetAttributeViInt64_cfunc = None
        self.niDCPower_SetAttributeViReal64_cfunc = None
        self.niDCPower_SetAttributeViString_cfunc = None
        self.niDCPower_SetSequence_cfunc = None
        self.niDCPower_UnlockSession_cfunc = None
        self.niDCPower_WaitForEventWithChannels_cfunc = None
        self.niDCPower_close_cfunc = None
        self.niDCPower_error_message_cfunc = None
        self.niDCPower_self_test_cfunc = None

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

    def abort(self, session, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        with self._func_lock:
            if self.niDCPower_AbortWithChannels_cfunc is None:
                self.niDCPower_AbortWithChannels_cfunc = self._get_library_function('niDCPower_AbortWithChannels')
                self.niDCPower_AbortWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_AbortWithChannels_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_AbortWithChannels_cfunc(vi_ctype, channel_name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_cal(self, session, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        with self._func_lock:
            if self.niDCPower_CalSelfCalibrate_cfunc is None:
                self.niDCPower_CalSelfCalibrate_cfunc = self._get_library_function('niDCPower_CalSelfCalibrate')
                self.niDCPower_CalSelfCalibrate_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_CalSelfCalibrate_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_CalSelfCalibrate_cfunc(vi_ctype, channel_name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_latched_output_cutoff_state(self, session, channel_name, output_cutoff_reason):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        output_cutoff_reason_ctype = _visatype.ViInt32(output_cutoff_reason.value)  # case S130
        with self._func_lock:
            if self.niDCPower_ClearLatchedOutputCutoffState_cfunc is None:
                self.niDCPower_ClearLatchedOutputCutoffState_cfunc = self._get_library_function('niDCPower_ClearLatchedOutputCutoffState')
                self.niDCPower_ClearLatchedOutputCutoffState_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niDCPower_ClearLatchedOutputCutoffState_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_ClearLatchedOutputCutoffState_cfunc(vi_ctype, channel_name_ctype, output_cutoff_reason_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def commit(self, session, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        with self._func_lock:
            if self.niDCPower_CommitWithChannels_cfunc is None:
                self.niDCPower_CommitWithChannels_cfunc = self._get_library_function('niDCPower_CommitWithChannels')
                self.niDCPower_CommitWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_CommitWithChannels_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_CommitWithChannels_cfunc(vi_ctype, channel_name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_aperture_time(self, session, channel_name, aperture_time, units):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        aperture_time_ctype = _visatype.ViReal64(aperture_time)  # case S150
        units_ctype = _visatype.ViInt32(units.value)  # case S130
        with self._func_lock:
            if self.niDCPower_ConfigureApertureTime_cfunc is None:
                self.niDCPower_ConfigureApertureTime_cfunc = self._get_library_function('niDCPower_ConfigureApertureTime')
                self.niDCPower_ConfigureApertureTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32]  # noqa: F405
                self.niDCPower_ConfigureApertureTime_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_ConfigureApertureTime_cfunc(vi_ctype, channel_name_ctype, aperture_time_ctype, units_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_lcr_custom_cable_compensation(self, session, channel_name, custom_cable_compensation_data):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        custom_cable_compensation_data_size_ctype = _visatype.ViInt32(0 if custom_cable_compensation_data is None else len(custom_cable_compensation_data))  # case S160
        custom_cable_compensation_data_converted = _converters.convert_to_bytes(custom_cable_compensation_data)  # case B520
        custom_cable_compensation_data_ctype = get_ctypes_pointer_for_buffer(value=custom_cable_compensation_data_converted, library_type=_visatype.ViInt8)  # case B520
        with self._func_lock:
            if self.niDCPower_ConfigureLCRCustomCableCompensation_cfunc is None:
                self.niDCPower_ConfigureLCRCustomCableCompensation_cfunc = self._get_library_function('niDCPower_ConfigureLCRCustomCableCompensation')
                self.niDCPower_ConfigureLCRCustomCableCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDCPower_ConfigureLCRCustomCableCompensation_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_ConfigureLCRCustomCableCompensation_cfunc(vi_ctype, channel_name_ctype, custom_cable_compensation_data_size_ctype, custom_cable_compensation_data_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_advanced_sequence_commit_step(self, session, channel_name, set_as_active_step):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        set_as_active_step_ctype = _visatype.ViBoolean(set_as_active_step)  # case S150
        with self._func_lock:
            if self.niDCPower_CreateAdvancedSequenceCommitStepWithChannels_cfunc is None:
                self.niDCPower_CreateAdvancedSequenceCommitStepWithChannels_cfunc = self._get_library_function('niDCPower_CreateAdvancedSequenceCommitStepWithChannels')
                self.niDCPower_CreateAdvancedSequenceCommitStepWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean]  # noqa: F405
                self.niDCPower_CreateAdvancedSequenceCommitStepWithChannels_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_CreateAdvancedSequenceCommitStepWithChannels_cfunc(vi_ctype, channel_name_ctype, set_as_active_step_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_advanced_sequence_step(self, session, channel_name, set_as_active_step):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        set_as_active_step_ctype = _visatype.ViBoolean(set_as_active_step)  # case S150
        with self._func_lock:
            if self.niDCPower_CreateAdvancedSequenceStepWithChannels_cfunc is None:
                self.niDCPower_CreateAdvancedSequenceStepWithChannels_cfunc = self._get_library_function('niDCPower_CreateAdvancedSequenceStepWithChannels')
                self.niDCPower_CreateAdvancedSequenceStepWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean]  # noqa: F405
                self.niDCPower_CreateAdvancedSequenceStepWithChannels_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_CreateAdvancedSequenceStepWithChannels_cfunc(vi_ctype, channel_name_ctype, set_as_active_step_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _create_advanced_sequence_with_channels(self, session, channel_name, sequence_name, attribute_ids, set_as_active_sequence):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        sequence_name_ctype = ctypes.create_string_buffer(sequence_name.encode(session._encoding))  # case C020
        attribute_id_count_ctype = _visatype.ViInt32(0 if attribute_ids is None else len(attribute_ids))  # case S160
        attribute_ids_ctype = get_ctypes_pointer_for_buffer(value=attribute_ids, library_type=_visatype.ViInt32)  # case B550
        set_as_active_sequence_ctype = _visatype.ViBoolean(set_as_active_sequence)  # case S150
        with self._func_lock:
            if self.niDCPower_CreateAdvancedSequenceWithChannels_cfunc is None:
                self.niDCPower_CreateAdvancedSequenceWithChannels_cfunc = self._get_library_function('niDCPower_CreateAdvancedSequenceWithChannels')
                self.niDCPower_CreateAdvancedSequenceWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32), ViBoolean]  # noqa: F405
                self.niDCPower_CreateAdvancedSequenceWithChannels_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_CreateAdvancedSequenceWithChannels_cfunc(vi_ctype, channel_name_ctype, sequence_name_ctype, attribute_id_count_ctype, attribute_ids_ctype, set_as_active_sequence_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_advanced_sequence(self, session, channel_name, sequence_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        sequence_name_ctype = ctypes.create_string_buffer(sequence_name.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niDCPower_DeleteAdvancedSequenceWithChannels_cfunc is None:
                self.niDCPower_DeleteAdvancedSequenceWithChannels_cfunc = self._get_library_function('niDCPower_DeleteAdvancedSequenceWithChannels')
                self.niDCPower_DeleteAdvancedSequenceWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_DeleteAdvancedSequenceWithChannels_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_DeleteAdvancedSequenceWithChannels_cfunc(vi_ctype, channel_name_ctype, sequence_name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niDCPower_Disable_cfunc is None:
                self.niDCPower_Disable_cfunc = self._get_library_function('niDCPower_Disable')
                self.niDCPower_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDCPower_Disable_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_Disable_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_attribute_configuration_buffer(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        size_ctype = _visatype.ViInt32()  # case S170
        configuration_ctype = None  # case B580
        with self._func_lock:
            if self.niDCPower_ExportAttributeConfigurationBuffer_cfunc is None:
                self.niDCPower_ExportAttributeConfigurationBuffer_cfunc = self._get_library_function('niDCPower_ExportAttributeConfigurationBuffer')
                self.niDCPower_ExportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDCPower_ExportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_ExportAttributeConfigurationBuffer_cfunc(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        size_ctype = _visatype.ViInt32(error_code)  # case S180
        configuration_size = size_ctype.value  # case B590
        configuration_array = array.array("b", [0] * configuration_size)  # case B590
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self.niDCPower_ExportAttributeConfigurationBuffer_cfunc(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_to_bytes(configuration_array)

    def export_attribute_configuration_file(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niDCPower_ExportAttributeConfigurationFile_cfunc is None:
                self.niDCPower_ExportAttributeConfigurationFile_cfunc = self._get_library_function('niDCPower_ExportAttributeConfigurationFile')
                self.niDCPower_ExportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_ExportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_ExportAttributeConfigurationFile_cfunc(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _fancy_initialize(self, session, resource_name, channels, reset, option_string, independent_channels):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(_converters.convert_repeated_capabilities_without_prefix(resource_name).encode(session._encoding))  # case C040
        channels_ctype = ctypes.create_string_buffer(_converters.convert_repeated_capabilities_without_prefix(channels).encode(session._encoding))  # case C040
        reset_ctype = _visatype.ViBoolean(reset)  # case S150
        option_string_ctype = ctypes.create_string_buffer(_converters.convert_init_with_options_dictionary(option_string).encode(session._encoding))  # case C040
        vi_ctype = _visatype.ViSession()  # case S220
        independent_channels_ctype = _visatype.ViBoolean(independent_channels)  # case S150
        with self._func_lock:
            if self.niDCPower_FancyInitialize_cfunc is None:
                self.niDCPower_FancyInitialize_cfunc = self._get_library_function('niDCPower_FancyInitialize')
                self.niDCPower_FancyInitialize_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession), ViBoolean]  # noqa: F405
                self.niDCPower_FancyInitialize_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_FancyInitialize_cfunc(resource_name_ctype, channels_ctype, reset_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)), independent_channels_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def _fetch_multiple(self, session, channel_name, timeout, count):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        count_ctype = _visatype.ViInt32(count)  # case S210
        voltage_measurements_size = count  # case B600
        voltage_measurements_array = array.array("d", [0] * voltage_measurements_size)  # case B600
        voltage_measurements_ctype = get_ctypes_pointer_for_buffer(value=voltage_measurements_array, library_type=_visatype.ViReal64)  # case B600
        current_measurements_size = count  # case B600
        current_measurements_array = array.array("d", [0] * current_measurements_size)  # case B600
        current_measurements_ctype = get_ctypes_pointer_for_buffer(value=current_measurements_array, library_type=_visatype.ViReal64)  # case B600
        in_compliance_size = count  # case B600
        in_compliance_ctype = get_ctypes_pointer_for_buffer(library_type=_visatype.ViBoolean, size=in_compliance_size)  # case B600
        actual_count_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDCPower_FetchMultiple_cfunc is None:
                self.niDCPower_FetchMultiple_cfunc = self._get_library_function('niDCPower_FetchMultiple')
                self.niDCPower_FetchMultiple_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViBoolean), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_FetchMultiple_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_FetchMultiple_cfunc(vi_ctype, channel_name_ctype, timeout_ctype, count_ctype, voltage_measurements_ctype, current_measurements_ctype, in_compliance_ctype, None if actual_count_ctype is None else (ctypes.pointer(actual_count_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return voltage_measurements_array, current_measurements_array, [bool(in_compliance_ctype[i]) for i in range(count_ctype.value)]

    def _fetch_multiple_lcr(self, session, channel_name, timeout, count):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        count_ctype = _visatype.ViInt32(count)  # case S210
        measurements_size = count  # case B600
        measurements_ctype = get_ctypes_pointer_for_buffer(library_type=lcr_measurement.struct_NILCRMeasurement, size=measurements_size)  # case B600
        actual_count_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDCPower_FetchMultipleLCR_cfunc is None:
                self.niDCPower_FetchMultipleLCR_cfunc = self._get_library_function('niDCPower_FetchMultipleLCR')
                self.niDCPower_FetchMultipleLCR_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(lcr_measurement.struct_NILCRMeasurement), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_FetchMultipleLCR_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_FetchMultipleLCR_cfunc(vi_ctype, channel_name_ctype, timeout_ctype, count_ctype, measurements_ctype, None if actual_count_ctype is None else (ctypes.pointer(actual_count_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [lcr_measurement.LCRMeasurement(measurements_ctype[i]) for i in range(count_ctype.value)]

    def _get_attribute_vi_boolean(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niDCPower_GetAttributeViBoolean_cfunc is None:
                self.niDCPower_GetAttributeViBoolean_cfunc = self._get_library_function('niDCPower_GetAttributeViBoolean')
                self.niDCPower_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDCPower_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_GetAttributeViBoolean_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def _get_attribute_vi_int32(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDCPower_GetAttributeViInt32_cfunc is None:
                self.niDCPower_GetAttributeViInt32_cfunc = self._get_library_function('niDCPower_GetAttributeViInt32')
                self.niDCPower_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_GetAttributeViInt32_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_int64(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt64()  # case S220
        with self._func_lock:
            if self.niDCPower_GetAttributeViInt64_cfunc is None:
                self.niDCPower_GetAttributeViInt64_cfunc = self._get_library_function('niDCPower_GetAttributeViInt64')
                self.niDCPower_GetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niDCPower_GetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_GetAttributeViInt64_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_real64(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niDCPower_GetAttributeViReal64_cfunc is None:
                self.niDCPower_GetAttributeViReal64_cfunc = self._get_library_function('niDCPower_GetAttributeViReal64')
                self.niDCPower_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_GetAttributeViReal64_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def _get_attribute_vi_string(self, session, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        with self._func_lock:
            if self.niDCPower_GetAttributeViString_cfunc is None:
                self.niDCPower_GetAttributeViString_cfunc = self._get_library_function('niDCPower_GetAttributeViString')
                self.niDCPower_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_GetAttributeViString_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self.niDCPower_GetAttributeViString_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(session._encoding)

    def get_channel_name(self, session, index):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        channel_name_ctype = None  # case C050
        with self._func_lock:
            if self.niDCPower_GetChannelName_cfunc is None:
                self.niDCPower_GetChannelName_cfunc = self._get_library_function('niDCPower_GetChannelName')
                self.niDCPower_GetChannelName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_GetChannelName_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_GetChannelName_cfunc(vi_ctype, index_ctype, buffer_size_ctype, channel_name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        channel_name_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self.niDCPower_GetChannelName_cfunc(vi_ctype, index_ctype, buffer_size_ctype, channel_name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return channel_name_ctype.value.decode(session._encoding)

    def _get_channel_names(self, session, indices):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        indices_ctype = ctypes.create_string_buffer(_converters.convert_repeated_capabilities_without_prefix(indices).encode(session._encoding))  # case C040
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        names_ctype = None  # case C050
        with self._func_lock:
            if self.niDCPower_GetChannelNameFromString_cfunc is None:
                self.niDCPower_GetChannelNameFromString_cfunc = self._get_library_function('niDCPower_GetChannelNameFromString')
                self.niDCPower_GetChannelNameFromString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_GetChannelNameFromString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_GetChannelNameFromString_cfunc(vi_ctype, indices_ctype, buffer_size_ctype, names_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        names_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self.niDCPower_GetChannelNameFromString_cfunc(vi_ctype, indices_ctype, buffer_size_ctype, names_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_comma_separated_string_to_list(names_ctype.value.decode(session._encoding))

    def _get_error(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        code_ctype = _visatype.ViStatus()  # case S220
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        description_ctype = None  # case C050
        with self._func_lock:
            if self.niDCPower_GetError_cfunc is None:
                self.niDCPower_GetError_cfunc = self._get_library_function('niDCPower_GetError')
                self.niDCPower_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_GetError_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_GetError_cfunc(vi_ctype, None if code_ctype is None else (ctypes.pointer(code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        description_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self.niDCPower_GetError_cfunc(vi_ctype, None if code_ctype is None else (ctypes.pointer(code_ctype)), buffer_size_ctype, description_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return int(code_ctype.value), description_ctype.value.decode(session._encoding)

    def _get_ext_cal_last_date_and_time(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDCPower_GetExtCalLastDateAndTime_cfunc is None:
                self.niDCPower_GetExtCalLastDateAndTime_cfunc = self._get_library_function('niDCPower_GetExtCalLastDateAndTime')
                self.niDCPower_GetExtCalLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_GetExtCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_GetExtCalLastDateAndTime_cfunc(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_ext_cal_last_temp(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niDCPower_GetExtCalLastTemp_cfunc is None:
                self.niDCPower_GetExtCalLastTemp_cfunc = self._get_library_function('niDCPower_GetExtCalLastTemp')
                self.niDCPower_GetExtCalLastTemp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_GetExtCalLastTemp_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_GetExtCalLastTemp_cfunc(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_ext_cal_recommended_interval(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        months_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDCPower_GetExtCalRecommendedInterval_cfunc is None:
                self.niDCPower_GetExtCalRecommendedInterval_cfunc = self._get_library_function('niDCPower_GetExtCalRecommendedInterval')
                self.niDCPower_GetExtCalRecommendedInterval_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_GetExtCalRecommendedInterval_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_GetExtCalRecommendedInterval_cfunc(vi_ctype, None if months_ctype is None else (ctypes.pointer(months_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_month_to_timedelta(int(months_ctype.value))

    def _get_lcr_compensation_last_date_and_time(self, session, channel_name, compensation_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        compensation_type_ctype = _visatype.ViInt32(compensation_type.value)  # case S130
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDCPower_GetLCRCompensationLastDateAndTime_cfunc is None:
                self.niDCPower_GetLCRCompensationLastDateAndTime_cfunc = self._get_library_function('niDCPower_GetLCRCompensationLastDateAndTime')
                self.niDCPower_GetLCRCompensationLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_GetLCRCompensationLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_GetLCRCompensationLastDateAndTime_cfunc(vi_ctype, channel_name_ctype, compensation_type_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_lcr_custom_cable_compensation_data(self, session, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        custom_cable_compensation_data_size_ctype = _visatype.ViInt32()  # case S170
        custom_cable_compensation_data_ctype = None  # case B580
        with self._func_lock:
            if self.niDCPower_GetLCRCustomCableCompensationData_cfunc is None:
                self.niDCPower_GetLCRCustomCableCompensationData_cfunc = self._get_library_function('niDCPower_GetLCRCustomCableCompensationData')
                self.niDCPower_GetLCRCustomCableCompensationData_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDCPower_GetLCRCustomCableCompensationData_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_GetLCRCustomCableCompensationData_cfunc(vi_ctype, channel_name_ctype, custom_cable_compensation_data_size_ctype, custom_cable_compensation_data_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        custom_cable_compensation_data_size_ctype = _visatype.ViInt32(error_code)  # case S180
        custom_cable_compensation_data_size = custom_cable_compensation_data_size_ctype.value  # case B590
        custom_cable_compensation_data_array = array.array("b", [0] * custom_cable_compensation_data_size)  # case B590
        custom_cable_compensation_data_ctype = get_ctypes_pointer_for_buffer(value=custom_cable_compensation_data_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self.niDCPower_GetLCRCustomCableCompensationData_cfunc(vi_ctype, channel_name_ctype, custom_cable_compensation_data_size_ctype, custom_cable_compensation_data_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return _converters.convert_to_bytes(custom_cable_compensation_data_array)

    def _get_self_cal_last_date_and_time(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niDCPower_GetSelfCalLastDateAndTime_cfunc is None:
                self.niDCPower_GetSelfCalLastDateAndTime_cfunc = self._get_library_function('niDCPower_GetSelfCalLastDateAndTime')
                self.niDCPower_GetSelfCalLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_GetSelfCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_GetSelfCalLastDateAndTime_cfunc(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_self_cal_last_temp(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niDCPower_GetSelfCalLastTemp_cfunc is None:
                self.niDCPower_GetSelfCalLastTemp_cfunc = self._get_library_function('niDCPower_GetSelfCalLastTemp')
                self.niDCPower_GetSelfCalLastTemp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_GetSelfCalLastTemp_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_GetSelfCalLastTemp_cfunc(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def import_attribute_configuration_buffer(self, session, configuration):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        size_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_converted = _converters.convert_to_bytes(configuration)  # case B520
        configuration_ctype = get_ctypes_pointer_for_buffer(value=configuration_converted, library_type=_visatype.ViInt8)  # case B520
        with self._func_lock:
            if self.niDCPower_ImportAttributeConfigurationBuffer_cfunc is None:
                self.niDCPower_ImportAttributeConfigurationBuffer_cfunc = self._get_library_function('niDCPower_ImportAttributeConfigurationBuffer')
                self.niDCPower_ImportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDCPower_ImportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_ImportAttributeConfigurationBuffer_cfunc(vi_ctype, size_ctype, configuration_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def import_attribute_configuration_file(self, session, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niDCPower_ImportAttributeConfigurationFile_cfunc is None:
                self.niDCPower_ImportAttributeConfigurationFile_cfunc = self._get_library_function('niDCPower_ImportAttributeConfigurationFile')
                self.niDCPower_ImportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_ImportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_ImportAttributeConfigurationFile_cfunc(vi_ctype, file_path_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _initialize_with_channels(self, session, resource_name, channels, reset, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(session._encoding))  # case C020
        channels_ctype = ctypes.create_string_buffer(channels.encode(session._encoding))  # case C020
        reset_ctype = _visatype.ViBoolean(reset)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(session._encoding))  # case C020
        vi_ctype = _visatype.ViSession()  # case S220
        with self._func_lock:
            if self.niDCPower_InitializeWithChannels_cfunc is None:
                self.niDCPower_InitializeWithChannels_cfunc = self._get_library_function('niDCPower_InitializeWithChannels')
                self.niDCPower_InitializeWithChannels_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niDCPower_InitializeWithChannels_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_InitializeWithChannels_cfunc(resource_name_ctype, channels_ctype, reset_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def _initialize_with_independent_channels(self, session, resource_name, reset, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(session._encoding))  # case C020
        reset_ctype = _visatype.ViBoolean(reset)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(session._encoding))  # case C020
        vi_ctype = _visatype.ViSession()  # case S220
        with self._func_lock:
            if self.niDCPower_InitializeWithIndependentChannels_cfunc is None:
                self.niDCPower_InitializeWithIndependentChannels_cfunc = self._get_library_function('niDCPower_InitializeWithIndependentChannels')
                self.niDCPower_InitializeWithIndependentChannels_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niDCPower_InitializeWithIndependentChannels_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_InitializeWithIndependentChannels_cfunc(resource_name_ctype, reset_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def _initiate_with_channels(self, session, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        with self._func_lock:
            if self.niDCPower_InitiateWithChannels_cfunc is None:
                self.niDCPower_InitiateWithChannels_cfunc = self._get_library_function('niDCPower_InitiateWithChannels')
                self.niDCPower_InitiateWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_InitiateWithChannels_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_InitiateWithChannels_cfunc(vi_ctype, channel_name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def lock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niDCPower_LockSession_cfunc is None:
                self.niDCPower_LockSession_cfunc = self._get_library_function('niDCPower_LockSession')
                self.niDCPower_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDCPower_LockSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_LockSession_cfunc(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def measure(self, session, channel_name, measurement_type):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        measurement_type_ctype = _visatype.ViInt32(measurement_type.value)  # case S130
        measurement_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niDCPower_Measure_cfunc is None:
                self.niDCPower_Measure_cfunc = self._get_library_function('niDCPower_Measure')
                self.niDCPower_Measure_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_Measure_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_Measure_cfunc(vi_ctype, channel_name_ctype, measurement_type_ctype, None if measurement_ctype is None else (ctypes.pointer(measurement_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(measurement_ctype.value)

    def _measure_multiple(self, session, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        voltage_measurements_size = self._parse_channel_count()  # case B560
        voltage_measurements_array = array.array("d", [0] * voltage_measurements_size)  # case B560
        voltage_measurements_ctype = get_ctypes_pointer_for_buffer(value=voltage_measurements_array, library_type=_visatype.ViReal64)  # case B560
        current_measurements_size = self._parse_channel_count()  # case B560
        current_measurements_array = array.array("d", [0] * current_measurements_size)  # case B560
        current_measurements_ctype = get_ctypes_pointer_for_buffer(value=current_measurements_array, library_type=_visatype.ViReal64)  # case B560
        with self._func_lock:
            if self.niDCPower_MeasureMultiple_cfunc is None:
                self.niDCPower_MeasureMultiple_cfunc = self._get_library_function('niDCPower_MeasureMultiple')
                self.niDCPower_MeasureMultiple_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_MeasureMultiple_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_MeasureMultiple_cfunc(vi_ctype, channel_name_ctype, voltage_measurements_ctype, current_measurements_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return voltage_measurements_array, current_measurements_array

    def _measure_multiple_lcr(self, session, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        measurements_size = self._parse_channel_count()  # case B560
        measurements_ctype = get_ctypes_pointer_for_buffer(library_type=lcr_measurement.struct_NILCRMeasurement, size=measurements_size)  # case B560
        with self._func_lock:
            if self.niDCPower_MeasureMultipleLCR_cfunc is None:
                self.niDCPower_MeasureMultipleLCR_cfunc = self._get_library_function('niDCPower_MeasureMultipleLCR')
                self.niDCPower_MeasureMultipleLCR_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(lcr_measurement.struct_NILCRMeasurement)]  # noqa: F405
                self.niDCPower_MeasureMultipleLCR_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_MeasureMultipleLCR_cfunc(vi_ctype, channel_name_ctype, measurements_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return [lcr_measurement.LCRMeasurement(measurements_ctype[i]) for i in range(self._parse_channel_count())]

    def _parse_channel_count(self, session, channels_string):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channels_string_ctype = ctypes.create_string_buffer(channels_string.encode(session._encoding))  # case C010
        number_of_channels_ctype = _visatype.ViUInt32()  # case S220
        with self._func_lock:
            if self.niDCPower_ParseChannelCount_cfunc is None:
                self.niDCPower_ParseChannelCount_cfunc = self._get_library_function('niDCPower_ParseChannelCount')
                self.niDCPower_ParseChannelCount_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViUInt32)]  # noqa: F405
                self.niDCPower_ParseChannelCount_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_ParseChannelCount_cfunc(vi_ctype, channels_string_ctype, None if number_of_channels_ctype is None else (ctypes.pointer(number_of_channels_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(number_of_channels_ctype.value)

    def perform_lcr_load_compensation(self, session, channel_name, compensation_spots):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        num_compensation_spots_ctype = _visatype.ViInt32(0 if compensation_spots is None else len(compensation_spots))  # case S160
        compensation_spots_ctype = get_ctypes_pointer_for_buffer([lcr_load_compensation_spot.struct_NILCRLoadCompensationSpot(c) for c in compensation_spots], library_type=lcr_load_compensation_spot.struct_NILCRLoadCompensationSpot)  # case B540
        with self._func_lock:
            if self.niDCPower_PerformLCRLoadCompensation_cfunc is None:
                self.niDCPower_PerformLCRLoadCompensation_cfunc = self._get_library_function('niDCPower_PerformLCRLoadCompensation')
                self.niDCPower_PerformLCRLoadCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(lcr_load_compensation_spot.struct_NILCRLoadCompensationSpot)]  # noqa: F405
                self.niDCPower_PerformLCRLoadCompensation_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_PerformLCRLoadCompensation_cfunc(vi_ctype, channel_name_ctype, num_compensation_spots_ctype, compensation_spots_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def perform_lcr_open_compensation(self, session, channel_name, additional_frequencies):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        num_frequencies_ctype = _visatype.ViInt32(0 if additional_frequencies is None else len(additional_frequencies))  # case S160
        additional_frequencies_ctype = get_ctypes_pointer_for_buffer(value=additional_frequencies, library_type=_visatype.ViReal64)  # case B550
        with self._func_lock:
            if self.niDCPower_PerformLCROpenCompensation_cfunc is None:
                self.niDCPower_PerformLCROpenCompensation_cfunc = self._get_library_function('niDCPower_PerformLCROpenCompensation')
                self.niDCPower_PerformLCROpenCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_PerformLCROpenCompensation_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_PerformLCROpenCompensation_cfunc(vi_ctype, channel_name_ctype, num_frequencies_ctype, additional_frequencies_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def perform_lcr_open_custom_cable_compensation(self, session, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        with self._func_lock:
            if self.niDCPower_PerformLCROpenCustomCableCompensation_cfunc is None:
                self.niDCPower_PerformLCROpenCustomCableCompensation_cfunc = self._get_library_function('niDCPower_PerformLCROpenCustomCableCompensation')
                self.niDCPower_PerformLCROpenCustomCableCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_PerformLCROpenCustomCableCompensation_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_PerformLCROpenCustomCableCompensation_cfunc(vi_ctype, channel_name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def perform_lcr_short_compensation(self, session, channel_name, additional_frequencies):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        num_frequencies_ctype = _visatype.ViInt32(0 if additional_frequencies is None else len(additional_frequencies))  # case S160
        additional_frequencies_ctype = get_ctypes_pointer_for_buffer(value=additional_frequencies, library_type=_visatype.ViReal64)  # case B550
        with self._func_lock:
            if self.niDCPower_PerformLCRShortCompensation_cfunc is None:
                self.niDCPower_PerformLCRShortCompensation_cfunc = self._get_library_function('niDCPower_PerformLCRShortCompensation')
                self.niDCPower_PerformLCRShortCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_PerformLCRShortCompensation_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_PerformLCRShortCompensation_cfunc(vi_ctype, channel_name_ctype, num_frequencies_ctype, additional_frequencies_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def perform_lcr_short_custom_cable_compensation(self, session, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        with self._func_lock:
            if self.niDCPower_PerformLCRShortCustomCableCompensation_cfunc is None:
                self.niDCPower_PerformLCRShortCustomCableCompensation_cfunc = self._get_library_function('niDCPower_PerformLCRShortCustomCableCompensation')
                self.niDCPower_PerformLCRShortCustomCableCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_PerformLCRShortCustomCableCompensation_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_PerformLCRShortCustomCableCompensation_cfunc(vi_ctype, channel_name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def query_in_compliance(self, session, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        in_compliance_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niDCPower_QueryInCompliance_cfunc is None:
                self.niDCPower_QueryInCompliance_cfunc = self._get_library_function('niDCPower_QueryInCompliance')
                self.niDCPower_QueryInCompliance_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDCPower_QueryInCompliance_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_QueryInCompliance_cfunc(vi_ctype, channel_name_ctype, None if in_compliance_ctype is None else (ctypes.pointer(in_compliance_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(in_compliance_ctype.value)

    def query_latched_output_cutoff_state(self, session, channel_name, output_cutoff_reason):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        output_cutoff_reason_ctype = _visatype.ViInt32(output_cutoff_reason.value)  # case S130
        output_cutoff_state_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niDCPower_QueryLatchedOutputCutoffState_cfunc is None:
                self.niDCPower_QueryLatchedOutputCutoffState_cfunc = self._get_library_function('niDCPower_QueryLatchedOutputCutoffState')
                self.niDCPower_QueryLatchedOutputCutoffState_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDCPower_QueryLatchedOutputCutoffState_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_QueryLatchedOutputCutoffState_cfunc(vi_ctype, channel_name_ctype, output_cutoff_reason_ctype, None if output_cutoff_state_ctype is None else (ctypes.pointer(output_cutoff_state_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(output_cutoff_state_ctype.value)

    def query_max_current_limit(self, session, channel_name, voltage_level):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        voltage_level_ctype = _visatype.ViReal64(voltage_level)  # case S150
        max_current_limit_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niDCPower_QueryMaxCurrentLimit_cfunc is None:
                self.niDCPower_QueryMaxCurrentLimit_cfunc = self._get_library_function('niDCPower_QueryMaxCurrentLimit')
                self.niDCPower_QueryMaxCurrentLimit_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_QueryMaxCurrentLimit_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_QueryMaxCurrentLimit_cfunc(vi_ctype, channel_name_ctype, voltage_level_ctype, None if max_current_limit_ctype is None else (ctypes.pointer(max_current_limit_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(max_current_limit_ctype.value)

    def query_max_voltage_level(self, session, channel_name, current_limit):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        current_limit_ctype = _visatype.ViReal64(current_limit)  # case S150
        max_voltage_level_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niDCPower_QueryMaxVoltageLevel_cfunc is None:
                self.niDCPower_QueryMaxVoltageLevel_cfunc = self._get_library_function('niDCPower_QueryMaxVoltageLevel')
                self.niDCPower_QueryMaxVoltageLevel_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_QueryMaxVoltageLevel_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_QueryMaxVoltageLevel_cfunc(vi_ctype, channel_name_ctype, current_limit_ctype, None if max_voltage_level_ctype is None else (ctypes.pointer(max_voltage_level_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(max_voltage_level_ctype.value)

    def query_min_current_limit(self, session, channel_name, voltage_level):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        voltage_level_ctype = _visatype.ViReal64(voltage_level)  # case S150
        min_current_limit_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niDCPower_QueryMinCurrentLimit_cfunc is None:
                self.niDCPower_QueryMinCurrentLimit_cfunc = self._get_library_function('niDCPower_QueryMinCurrentLimit')
                self.niDCPower_QueryMinCurrentLimit_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_QueryMinCurrentLimit_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_QueryMinCurrentLimit_cfunc(vi_ctype, channel_name_ctype, voltage_level_ctype, None if min_current_limit_ctype is None else (ctypes.pointer(min_current_limit_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(min_current_limit_ctype.value)

    def query_output_state(self, session, channel_name, output_state):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        output_state_ctype = _visatype.ViInt32(output_state.value)  # case S130
        in_state_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niDCPower_QueryOutputState_cfunc is None:
                self.niDCPower_QueryOutputState_cfunc = self._get_library_function('niDCPower_QueryOutputState')
                self.niDCPower_QueryOutputState_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDCPower_QueryOutputState_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_QueryOutputState_cfunc(vi_ctype, channel_name_ctype, output_state_ctype, None if in_state_ctype is None else (ctypes.pointer(in_state_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(in_state_ctype.value)

    def read_current_temperature(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        with self._func_lock:
            if self.niDCPower_ReadCurrentTemperature_cfunc is None:
                self.niDCPower_ReadCurrentTemperature_cfunc = self._get_library_function('niDCPower_ReadCurrentTemperature')
                self.niDCPower_ReadCurrentTemperature_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_ReadCurrentTemperature_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_ReadCurrentTemperature_cfunc(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def reset_device(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niDCPower_ResetDevice_cfunc is None:
                self.niDCPower_ResetDevice_cfunc = self._get_library_function('niDCPower_ResetDevice')
                self.niDCPower_ResetDevice_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDCPower_ResetDevice_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_ResetDevice_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset(self, session, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        with self._func_lock:
            if self.niDCPower_ResetWithChannels_cfunc is None:
                self.niDCPower_ResetWithChannels_cfunc = self._get_library_function('niDCPower_ResetWithChannels')
                self.niDCPower_ResetWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_ResetWithChannels_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_ResetWithChannels_cfunc(vi_ctype, channel_name_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_defaults(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niDCPower_ResetWithDefaults_cfunc is None:
                self.niDCPower_ResetWithDefaults_cfunc = self._get_library_function('niDCPower_ResetWithDefaults')
                self.niDCPower_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDCPower_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_ResetWithDefaults_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_edge_trigger(self, session, channel_name, trigger):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        trigger_ctype = _visatype.ViInt32(trigger.value)  # case S130
        with self._func_lock:
            if self.niDCPower_SendSoftwareEdgeTriggerWithChannels_cfunc is None:
                self.niDCPower_SendSoftwareEdgeTriggerWithChannels_cfunc = self._get_library_function('niDCPower_SendSoftwareEdgeTriggerWithChannels')
                self.niDCPower_SendSoftwareEdgeTriggerWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niDCPower_SendSoftwareEdgeTriggerWithChannels_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_SendSoftwareEdgeTriggerWithChannels_cfunc(vi_ctype, channel_name_ctype, trigger_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_boolean(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        with self._func_lock:
            if self.niDCPower_SetAttributeViBoolean_cfunc is None:
                self.niDCPower_SetAttributeViBoolean_cfunc = self._get_library_function('niDCPower_SetAttributeViBoolean')
                self.niDCPower_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niDCPower_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_SetAttributeViBoolean_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int32(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        with self._func_lock:
            if self.niDCPower_SetAttributeViInt32_cfunc is None:
                self.niDCPower_SetAttributeViInt32_cfunc = self._get_library_function('niDCPower_SetAttributeViInt32')
                self.niDCPower_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niDCPower_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_SetAttributeViInt32_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int64(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt64(attribute_value)  # case S150
        with self._func_lock:
            if self.niDCPower_SetAttributeViInt64_cfunc is None:
                self.niDCPower_SetAttributeViInt64_cfunc = self._get_library_function('niDCPower_SetAttributeViInt64')
                self.niDCPower_SetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niDCPower_SetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_SetAttributeViInt64_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_real64(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        with self._func_lock:
            if self.niDCPower_SetAttributeViReal64_cfunc is None:
                self.niDCPower_SetAttributeViReal64_cfunc = self._get_library_function('niDCPower_SetAttributeViReal64')
                self.niDCPower_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niDCPower_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_SetAttributeViReal64_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, session, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(session._encoding))  # case C020
        with self._func_lock:
            if self.niDCPower_SetAttributeViString_cfunc is None:
                self.niDCPower_SetAttributeViString_cfunc = self._get_library_function('niDCPower_SetAttributeViString')
                self.niDCPower_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_SetAttributeViString_cfunc(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_sequence(self, session, channel_name, values, source_delays):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        values_ctype = get_ctypes_pointer_for_buffer(value=values, library_type=_visatype.ViReal64)  # case B550
        source_delays_ctype = get_ctypes_pointer_for_buffer(value=source_delays, library_type=_visatype.ViReal64)  # case B550
        size_ctype = _visatype.ViUInt32(0 if values is None else len(values))  # case S160
        if source_delays is not None and len(source_delays) != len(values):  # case S160
            raise ValueError("Length of source_delays and values parameters do not match.")  # case S160
        with self._func_lock:
            if self.niDCPower_SetSequence_cfunc is None:
                self.niDCPower_SetSequence_cfunc = self._get_library_function('niDCPower_SetSequence')
                self.niDCPower_SetSequence_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ViUInt32]  # noqa: F405
                self.niDCPower_SetSequence_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_SetSequence_cfunc(vi_ctype, channel_name_ctype, values_ctype, source_delays_ctype, size_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        caller_has_lock_ctype = _visatype.ViBoolean()  # case S220
        with self._func_lock:
            if self.niDCPower_UnlockSession_cfunc is None:
                self.niDCPower_UnlockSession_cfunc = self._get_library_function('niDCPower_UnlockSession')
                self.niDCPower_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDCPower_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_UnlockSession_cfunc(vi_ctype, None if caller_has_lock_ctype is None else (ctypes.pointer(caller_has_lock_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(caller_has_lock_ctype.value)

    def wait_for_event(self, session, channel_name, event_id, timeout):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(session._encoding))  # case C010
        event_id_ctype = _visatype.ViInt32(event_id.value)  # case S130
        timeout_ctype = _converters.convert_timedelta_to_seconds_real64(timeout)  # case S140
        with self._func_lock:
            if self.niDCPower_WaitForEventWithChannels_cfunc is None:
                self.niDCPower_WaitForEventWithChannels_cfunc = self._get_library_function('niDCPower_WaitForEventWithChannels')
                self.niDCPower_WaitForEventWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64]  # noqa: F405
                self.niDCPower_WaitForEventWithChannels_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_WaitForEventWithChannels_cfunc(vi_ctype, channel_name_ctype, event_id_ctype, timeout_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        with self._func_lock:
            if self.niDCPower_close_cfunc is None:
                self.niDCPower_close_cfunc = self._get_library_function('niDCPower_close')
                self.niDCPower_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDCPower_close_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_close_cfunc(vi_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _error_message(self, session, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        with self._func_lock:
            if self.niDCPower_error_message_cfunc is None:
                self.niDCPower_error_message_cfunc = self._get_library_function('niDCPower_error_message')
                self.niDCPower_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_error_message_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_error_message_cfunc(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(session._encoding)

    def _self_test(self, session):  # noqa: N802
        vi_ctype = _visatype.ViSession(session._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        with self._func_lock:
            if self.niDCPower_self_test_cfunc is None:
                self.niDCPower_self_test_cfunc = self._get_library_function('niDCPower_self_test')
                self.niDCPower_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_self_test_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niDCPower_self_test_cfunc(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(session._encoding)
