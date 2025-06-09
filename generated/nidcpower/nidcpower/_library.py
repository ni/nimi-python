# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import nidcpower.errors as errors
import threading

from nidcpower._visatype import *  # noqa: F403,H303

import nidcpower.lcr_measurement as lcr_measurement  # noqa: F401

import nidcpower.lcr_load_compensation_spot as lcr_load_compensation_spot  # noqa: F401


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
        self.niDCPower_ConfigureLCRCompensation_cfunc = None
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
        self.niDCPower_GetLCRCompensationData_cfunc = None
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
        self.niDCPower_SetRuntimeEnvironment_cfunc = None
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

    def niDCPower_AbortWithChannels(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_AbortWithChannels_cfunc is None:
                self.niDCPower_AbortWithChannels_cfunc = self._get_library_function('niDCPower_AbortWithChannels')
                self.niDCPower_AbortWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_AbortWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_AbortWithChannels_cfunc(vi, channel_name)

    def niDCPower_CalSelfCalibrate(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CalSelfCalibrate_cfunc is None:
                self.niDCPower_CalSelfCalibrate_cfunc = self._get_library_function('niDCPower_CalSelfCalibrate')
                self.niDCPower_CalSelfCalibrate_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_CalSelfCalibrate_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_CalSelfCalibrate_cfunc(vi, channel_name)

    def niDCPower_ClearLatchedOutputCutoffState(self, vi, channel_name, output_cutoff_reason):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ClearLatchedOutputCutoffState_cfunc is None:
                self.niDCPower_ClearLatchedOutputCutoffState_cfunc = self._get_library_function('niDCPower_ClearLatchedOutputCutoffState')
                self.niDCPower_ClearLatchedOutputCutoffState_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niDCPower_ClearLatchedOutputCutoffState_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ClearLatchedOutputCutoffState_cfunc(vi, channel_name, output_cutoff_reason)

    def niDCPower_CommitWithChannels(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CommitWithChannels_cfunc is None:
                self.niDCPower_CommitWithChannels_cfunc = self._get_library_function('niDCPower_CommitWithChannels')
                self.niDCPower_CommitWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_CommitWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_CommitWithChannels_cfunc(vi, channel_name)

    def niDCPower_ConfigureApertureTime(self, vi, channel_name, aperture_time, units):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureApertureTime_cfunc is None:
                self.niDCPower_ConfigureApertureTime_cfunc = self._get_library_function('niDCPower_ConfigureApertureTime')
                self.niDCPower_ConfigureApertureTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32]  # noqa: F405
                self.niDCPower_ConfigureApertureTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ConfigureApertureTime_cfunc(vi, channel_name, aperture_time, units)

    def niDCPower_ConfigureLCRCompensation(self, vi, channel_name, compensation_data_size, compensation_data):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureLCRCompensation_cfunc is None:
                self.niDCPower_ConfigureLCRCompensation_cfunc = self._get_library_function('niDCPower_ConfigureLCRCompensation')
                self.niDCPower_ConfigureLCRCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDCPower_ConfigureLCRCompensation_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ConfigureLCRCompensation_cfunc(vi, channel_name, compensation_data_size, compensation_data)

    def niDCPower_ConfigureLCRCustomCableCompensation(self, vi, channel_name, custom_cable_compensation_data_size, custom_cable_compensation_data):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureLCRCustomCableCompensation_cfunc is None:
                self.niDCPower_ConfigureLCRCustomCableCompensation_cfunc = self._get_library_function('niDCPower_ConfigureLCRCustomCableCompensation')
                self.niDCPower_ConfigureLCRCustomCableCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDCPower_ConfigureLCRCustomCableCompensation_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ConfigureLCRCustomCableCompensation_cfunc(vi, channel_name, custom_cable_compensation_data_size, custom_cable_compensation_data)

    def niDCPower_CreateAdvancedSequenceCommitStepWithChannels(self, vi, channel_name, set_as_active_step):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CreateAdvancedSequenceCommitStepWithChannels_cfunc is None:
                self.niDCPower_CreateAdvancedSequenceCommitStepWithChannels_cfunc = self._get_library_function('niDCPower_CreateAdvancedSequenceCommitStepWithChannels')
                self.niDCPower_CreateAdvancedSequenceCommitStepWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean]  # noqa: F405
                self.niDCPower_CreateAdvancedSequenceCommitStepWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_CreateAdvancedSequenceCommitStepWithChannels_cfunc(vi, channel_name, set_as_active_step)

    def niDCPower_CreateAdvancedSequenceStepWithChannels(self, vi, channel_name, set_as_active_step):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CreateAdvancedSequenceStepWithChannels_cfunc is None:
                self.niDCPower_CreateAdvancedSequenceStepWithChannels_cfunc = self._get_library_function('niDCPower_CreateAdvancedSequenceStepWithChannels')
                self.niDCPower_CreateAdvancedSequenceStepWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean]  # noqa: F405
                self.niDCPower_CreateAdvancedSequenceStepWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_CreateAdvancedSequenceStepWithChannels_cfunc(vi, channel_name, set_as_active_step)

    def niDCPower_CreateAdvancedSequenceWithChannels(self, vi, channel_name, sequence_name, attribute_id_count, attribute_ids, set_as_active_sequence):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CreateAdvancedSequenceWithChannels_cfunc is None:
                self.niDCPower_CreateAdvancedSequenceWithChannels_cfunc = self._get_library_function('niDCPower_CreateAdvancedSequenceWithChannels')
                self.niDCPower_CreateAdvancedSequenceWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32), ViBoolean]  # noqa: F405
                self.niDCPower_CreateAdvancedSequenceWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_CreateAdvancedSequenceWithChannels_cfunc(vi, channel_name, sequence_name, attribute_id_count, attribute_ids, set_as_active_sequence)

    def niDCPower_DeleteAdvancedSequenceWithChannels(self, vi, channel_name, sequence_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_DeleteAdvancedSequenceWithChannels_cfunc is None:
                self.niDCPower_DeleteAdvancedSequenceWithChannels_cfunc = self._get_library_function('niDCPower_DeleteAdvancedSequenceWithChannels')
                self.niDCPower_DeleteAdvancedSequenceWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_DeleteAdvancedSequenceWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_DeleteAdvancedSequenceWithChannels_cfunc(vi, channel_name, sequence_name)

    def niDCPower_Disable(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_Disable_cfunc is None:
                self.niDCPower_Disable_cfunc = self._get_library_function('niDCPower_Disable')
                self.niDCPower_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDCPower_Disable_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_Disable_cfunc(vi)

    def niDCPower_ExportAttributeConfigurationBuffer(self, vi, size, configuration):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ExportAttributeConfigurationBuffer_cfunc is None:
                self.niDCPower_ExportAttributeConfigurationBuffer_cfunc = self._get_library_function('niDCPower_ExportAttributeConfigurationBuffer')
                self.niDCPower_ExportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDCPower_ExportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ExportAttributeConfigurationBuffer_cfunc(vi, size, configuration)

    def niDCPower_ExportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ExportAttributeConfigurationFile_cfunc is None:
                self.niDCPower_ExportAttributeConfigurationFile_cfunc = self._get_library_function('niDCPower_ExportAttributeConfigurationFile')
                self.niDCPower_ExportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_ExportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ExportAttributeConfigurationFile_cfunc(vi, file_path)

    def niDCPower_FancyInitialize(self, resource_name, channels, reset, option_string, vi, independent_channels):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_FancyInitialize_cfunc is None:
                self.niDCPower_FancyInitialize_cfunc = self._get_library_function('niDCPower_FancyInitialize')
                self.niDCPower_FancyInitialize_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession), ViBoolean]  # noqa: F405
                self.niDCPower_FancyInitialize_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_FancyInitialize_cfunc(resource_name, channels, reset, option_string, vi, independent_channels)

    def niDCPower_FetchMultiple(self, vi, channel_name, timeout, count, voltage_measurements, current_measurements, in_compliance, actual_count):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_FetchMultiple_cfunc is None:
                self.niDCPower_FetchMultiple_cfunc = self._get_library_function('niDCPower_FetchMultiple')
                self.niDCPower_FetchMultiple_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViBoolean), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_FetchMultiple_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_FetchMultiple_cfunc(vi, channel_name, timeout, count, voltage_measurements, current_measurements, in_compliance, actual_count)

    def niDCPower_FetchMultipleLCR(self, vi, channel_name, timeout, count, measurements, actual_count):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_FetchMultipleLCR_cfunc is None:
                self.niDCPower_FetchMultipleLCR_cfunc = self._get_library_function('niDCPower_FetchMultipleLCR')
                self.niDCPower_FetchMultipleLCR_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViInt32, ctypes.POINTER(lcr_measurement.struct_NILCRMeasurement), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_FetchMultipleLCR_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_FetchMultipleLCR_cfunc(vi, channel_name, timeout, count, measurements, actual_count)

    def niDCPower_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetAttributeViBoolean_cfunc is None:
                self.niDCPower_GetAttributeViBoolean_cfunc = self._get_library_function('niDCPower_GetAttributeViBoolean')
                self.niDCPower_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDCPower_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetAttributeViInt32_cfunc is None:
                self.niDCPower_GetAttributeViInt32_cfunc = self._get_library_function('niDCPower_GetAttributeViInt32')
                self.niDCPower_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_GetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetAttributeViInt64_cfunc is None:
                self.niDCPower_GetAttributeViInt64_cfunc = self._get_library_function('niDCPower_GetAttributeViInt64')
                self.niDCPower_GetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt64)]  # noqa: F405
                self.niDCPower_GetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetAttributeViInt64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetAttributeViReal64_cfunc is None:
                self.niDCPower_GetAttributeViReal64_cfunc = self._get_library_function('niDCPower_GetAttributeViReal64')
                self.niDCPower_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetAttributeViString_cfunc is None:
                self.niDCPower_GetAttributeViString_cfunc = self._get_library_function('niDCPower_GetAttributeViString')
                self.niDCPower_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetAttributeViString_cfunc(vi, channel_name, attribute_id, buffer_size, attribute_value)

    def niDCPower_GetChannelName(self, vi, index, buffer_size, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetChannelName_cfunc is None:
                self.niDCPower_GetChannelName_cfunc = self._get_library_function('niDCPower_GetChannelName')
                self.niDCPower_GetChannelName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_GetChannelName_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetChannelName_cfunc(vi, index, buffer_size, channel_name)

    def niDCPower_GetChannelNameFromString(self, vi, indices, buffer_size, names):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetChannelNameFromString_cfunc is None:
                self.niDCPower_GetChannelNameFromString_cfunc = self._get_library_function('niDCPower_GetChannelNameFromString')
                self.niDCPower_GetChannelNameFromString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_GetChannelNameFromString_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetChannelNameFromString_cfunc(vi, indices, buffer_size, names)

    def niDCPower_GetError(self, vi, code, buffer_size, description):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetError_cfunc is None:
                self.niDCPower_GetError_cfunc = self._get_library_function('niDCPower_GetError')
                self.niDCPower_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetError_cfunc(vi, code, buffer_size, description)

    def niDCPower_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetExtCalLastDateAndTime_cfunc is None:
                self.niDCPower_GetExtCalLastDateAndTime_cfunc = self._get_library_function('niDCPower_GetExtCalLastDateAndTime')
                self.niDCPower_GetExtCalLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_GetExtCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetExtCalLastDateAndTime_cfunc(vi, year, month, day, hour, minute)

    def niDCPower_GetExtCalLastTemp(self, vi, temperature):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetExtCalLastTemp_cfunc is None:
                self.niDCPower_GetExtCalLastTemp_cfunc = self._get_library_function('niDCPower_GetExtCalLastTemp')
                self.niDCPower_GetExtCalLastTemp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_GetExtCalLastTemp_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetExtCalLastTemp_cfunc(vi, temperature)

    def niDCPower_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetExtCalRecommendedInterval_cfunc is None:
                self.niDCPower_GetExtCalRecommendedInterval_cfunc = self._get_library_function('niDCPower_GetExtCalRecommendedInterval')
                self.niDCPower_GetExtCalRecommendedInterval_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_GetExtCalRecommendedInterval_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetExtCalRecommendedInterval_cfunc(vi, months)

    def niDCPower_GetLCRCompensationData(self, vi, channel_name, compensation_data_size, compensation_data):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetLCRCompensationData_cfunc is None:
                self.niDCPower_GetLCRCompensationData_cfunc = self._get_library_function('niDCPower_GetLCRCompensationData')
                self.niDCPower_GetLCRCompensationData_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDCPower_GetLCRCompensationData_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetLCRCompensationData_cfunc(vi, channel_name, compensation_data_size, compensation_data)

    def niDCPower_GetLCRCompensationLastDateAndTime(self, vi, channel_name, compensation_type, year, month, day, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetLCRCompensationLastDateAndTime_cfunc is None:
                self.niDCPower_GetLCRCompensationLastDateAndTime_cfunc = self._get_library_function('niDCPower_GetLCRCompensationLastDateAndTime')
                self.niDCPower_GetLCRCompensationLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_GetLCRCompensationLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetLCRCompensationLastDateAndTime_cfunc(vi, channel_name, compensation_type, year, month, day, hour, minute)

    def niDCPower_GetLCRCustomCableCompensationData(self, vi, channel_name, custom_cable_compensation_data_size, custom_cable_compensation_data):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetLCRCustomCableCompensationData_cfunc is None:
                self.niDCPower_GetLCRCustomCableCompensationData_cfunc = self._get_library_function('niDCPower_GetLCRCustomCableCompensationData')
                self.niDCPower_GetLCRCustomCableCompensationData_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDCPower_GetLCRCustomCableCompensationData_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetLCRCustomCableCompensationData_cfunc(vi, channel_name, custom_cable_compensation_data_size, custom_cable_compensation_data)

    def niDCPower_GetSelfCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetSelfCalLastDateAndTime_cfunc is None:
                self.niDCPower_GetSelfCalLastDateAndTime_cfunc = self._get_library_function('niDCPower_GetSelfCalLastDateAndTime')
                self.niDCPower_GetSelfCalLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niDCPower_GetSelfCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetSelfCalLastDateAndTime_cfunc(vi, year, month, day, hour, minute)

    def niDCPower_GetSelfCalLastTemp(self, vi, temperature):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetSelfCalLastTemp_cfunc is None:
                self.niDCPower_GetSelfCalLastTemp_cfunc = self._get_library_function('niDCPower_GetSelfCalLastTemp')
                self.niDCPower_GetSelfCalLastTemp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_GetSelfCalLastTemp_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_GetSelfCalLastTemp_cfunc(vi, temperature)

    def niDCPower_ImportAttributeConfigurationBuffer(self, vi, size, configuration):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ImportAttributeConfigurationBuffer_cfunc is None:
                self.niDCPower_ImportAttributeConfigurationBuffer_cfunc = self._get_library_function('niDCPower_ImportAttributeConfigurationBuffer')
                self.niDCPower_ImportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niDCPower_ImportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ImportAttributeConfigurationBuffer_cfunc(vi, size, configuration)

    def niDCPower_ImportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ImportAttributeConfigurationFile_cfunc is None:
                self.niDCPower_ImportAttributeConfigurationFile_cfunc = self._get_library_function('niDCPower_ImportAttributeConfigurationFile')
                self.niDCPower_ImportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_ImportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ImportAttributeConfigurationFile_cfunc(vi, file_path)

    def niDCPower_InitializeWithChannels(self, resource_name, channels, reset, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_InitializeWithChannels_cfunc is None:
                self.niDCPower_InitializeWithChannels_cfunc = self._get_library_function('niDCPower_InitializeWithChannels')
                self.niDCPower_InitializeWithChannels_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niDCPower_InitializeWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_InitializeWithChannels_cfunc(resource_name, channels, reset, option_string, vi)

    def niDCPower_InitializeWithIndependentChannels(self, resource_name, reset, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_InitializeWithIndependentChannels_cfunc is None:
                self.niDCPower_InitializeWithIndependentChannels_cfunc = self._get_library_function('niDCPower_InitializeWithIndependentChannels')
                self.niDCPower_InitializeWithIndependentChannels_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niDCPower_InitializeWithIndependentChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_InitializeWithIndependentChannels_cfunc(resource_name, reset, option_string, vi)

    def niDCPower_InitiateWithChannels(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_InitiateWithChannels_cfunc is None:
                self.niDCPower_InitiateWithChannels_cfunc = self._get_library_function('niDCPower_InitiateWithChannels')
                self.niDCPower_InitiateWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_InitiateWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_InitiateWithChannels_cfunc(vi, channel_name)

    def niDCPower_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_LockSession_cfunc is None:
                self.niDCPower_LockSession_cfunc = self._get_library_function('niDCPower_LockSession')
                self.niDCPower_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDCPower_LockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_LockSession_cfunc(vi, caller_has_lock)

    def niDCPower_Measure(self, vi, channel_name, measurement_type, measurement):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_Measure_cfunc is None:
                self.niDCPower_Measure_cfunc = self._get_library_function('niDCPower_Measure')
                self.niDCPower_Measure_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_Measure_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_Measure_cfunc(vi, channel_name, measurement_type, measurement)

    def niDCPower_MeasureMultiple(self, vi, channel_name, voltage_measurements, current_measurements):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_MeasureMultiple_cfunc is None:
                self.niDCPower_MeasureMultiple_cfunc = self._get_library_function('niDCPower_MeasureMultiple')
                self.niDCPower_MeasureMultiple_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_MeasureMultiple_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_MeasureMultiple_cfunc(vi, channel_name, voltage_measurements, current_measurements)

    def niDCPower_MeasureMultipleLCR(self, vi, channel_name, measurements):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_MeasureMultipleLCR_cfunc is None:
                self.niDCPower_MeasureMultipleLCR_cfunc = self._get_library_function('niDCPower_MeasureMultipleLCR')
                self.niDCPower_MeasureMultipleLCR_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(lcr_measurement.struct_NILCRMeasurement)]  # noqa: F405
                self.niDCPower_MeasureMultipleLCR_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_MeasureMultipleLCR_cfunc(vi, channel_name, measurements)

    def niDCPower_ParseChannelCount(self, vi, channels_string, number_of_channels):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ParseChannelCount_cfunc is None:
                self.niDCPower_ParseChannelCount_cfunc = self._get_library_function('niDCPower_ParseChannelCount')
                self.niDCPower_ParseChannelCount_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViUInt32)]  # noqa: F405
                self.niDCPower_ParseChannelCount_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ParseChannelCount_cfunc(vi, channels_string, number_of_channels)

    def niDCPower_PerformLCRLoadCompensation(self, vi, channel_name, num_compensation_spots, compensation_spots):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_PerformLCRLoadCompensation_cfunc is None:
                self.niDCPower_PerformLCRLoadCompensation_cfunc = self._get_library_function('niDCPower_PerformLCRLoadCompensation')
                self.niDCPower_PerformLCRLoadCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(lcr_load_compensation_spot.struct_NILCRLoadCompensationSpot)]  # noqa: F405
                self.niDCPower_PerformLCRLoadCompensation_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_PerformLCRLoadCompensation_cfunc(vi, channel_name, num_compensation_spots, compensation_spots)

    def niDCPower_PerformLCROpenCompensation(self, vi, channel_name, num_frequencies, additional_frequencies):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_PerformLCROpenCompensation_cfunc is None:
                self.niDCPower_PerformLCROpenCompensation_cfunc = self._get_library_function('niDCPower_PerformLCROpenCompensation')
                self.niDCPower_PerformLCROpenCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_PerformLCROpenCompensation_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_PerformLCROpenCompensation_cfunc(vi, channel_name, num_frequencies, additional_frequencies)

    def niDCPower_PerformLCROpenCustomCableCompensation(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_PerformLCROpenCustomCableCompensation_cfunc is None:
                self.niDCPower_PerformLCROpenCustomCableCompensation_cfunc = self._get_library_function('niDCPower_PerformLCROpenCustomCableCompensation')
                self.niDCPower_PerformLCROpenCustomCableCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_PerformLCROpenCustomCableCompensation_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_PerformLCROpenCustomCableCompensation_cfunc(vi, channel_name)

    def niDCPower_PerformLCRShortCompensation(self, vi, channel_name, num_frequencies, additional_frequencies):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_PerformLCRShortCompensation_cfunc is None:
                self.niDCPower_PerformLCRShortCompensation_cfunc = self._get_library_function('niDCPower_PerformLCRShortCompensation')
                self.niDCPower_PerformLCRShortCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_PerformLCRShortCompensation_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_PerformLCRShortCompensation_cfunc(vi, channel_name, num_frequencies, additional_frequencies)

    def niDCPower_PerformLCRShortCustomCableCompensation(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_PerformLCRShortCustomCableCompensation_cfunc is None:
                self.niDCPower_PerformLCRShortCustomCableCompensation_cfunc = self._get_library_function('niDCPower_PerformLCRShortCustomCableCompensation')
                self.niDCPower_PerformLCRShortCustomCableCompensation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_PerformLCRShortCustomCableCompensation_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_PerformLCRShortCustomCableCompensation_cfunc(vi, channel_name)

    def niDCPower_QueryInCompliance(self, vi, channel_name, in_compliance):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_QueryInCompliance_cfunc is None:
                self.niDCPower_QueryInCompliance_cfunc = self._get_library_function('niDCPower_QueryInCompliance')
                self.niDCPower_QueryInCompliance_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDCPower_QueryInCompliance_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_QueryInCompliance_cfunc(vi, channel_name, in_compliance)

    def niDCPower_QueryLatchedOutputCutoffState(self, vi, channel_name, output_cutoff_reason, output_cutoff_state):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_QueryLatchedOutputCutoffState_cfunc is None:
                self.niDCPower_QueryLatchedOutputCutoffState_cfunc = self._get_library_function('niDCPower_QueryLatchedOutputCutoffState')
                self.niDCPower_QueryLatchedOutputCutoffState_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDCPower_QueryLatchedOutputCutoffState_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_QueryLatchedOutputCutoffState_cfunc(vi, channel_name, output_cutoff_reason, output_cutoff_state)

    def niDCPower_QueryMaxCurrentLimit(self, vi, channel_name, voltage_level, max_current_limit):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_QueryMaxCurrentLimit_cfunc is None:
                self.niDCPower_QueryMaxCurrentLimit_cfunc = self._get_library_function('niDCPower_QueryMaxCurrentLimit')
                self.niDCPower_QueryMaxCurrentLimit_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_QueryMaxCurrentLimit_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_QueryMaxCurrentLimit_cfunc(vi, channel_name, voltage_level, max_current_limit)

    def niDCPower_QueryMaxVoltageLevel(self, vi, channel_name, current_limit, max_voltage_level):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_QueryMaxVoltageLevel_cfunc is None:
                self.niDCPower_QueryMaxVoltageLevel_cfunc = self._get_library_function('niDCPower_QueryMaxVoltageLevel')
                self.niDCPower_QueryMaxVoltageLevel_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_QueryMaxVoltageLevel_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_QueryMaxVoltageLevel_cfunc(vi, channel_name, current_limit, max_voltage_level)

    def niDCPower_QueryMinCurrentLimit(self, vi, channel_name, voltage_level, min_current_limit):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_QueryMinCurrentLimit_cfunc is None:
                self.niDCPower_QueryMinCurrentLimit_cfunc = self._get_library_function('niDCPower_QueryMinCurrentLimit')
                self.niDCPower_QueryMinCurrentLimit_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_QueryMinCurrentLimit_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_QueryMinCurrentLimit_cfunc(vi, channel_name, voltage_level, min_current_limit)

    def niDCPower_QueryOutputState(self, vi, channel_name, output_state, in_state):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_QueryOutputState_cfunc is None:
                self.niDCPower_QueryOutputState_cfunc = self._get_library_function('niDCPower_QueryOutputState')
                self.niDCPower_QueryOutputState_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDCPower_QueryOutputState_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_QueryOutputState_cfunc(vi, channel_name, output_state, in_state)

    def niDCPower_ReadCurrentTemperature(self, vi, temperature):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ReadCurrentTemperature_cfunc is None:
                self.niDCPower_ReadCurrentTemperature_cfunc = self._get_library_function('niDCPower_ReadCurrentTemperature')
                self.niDCPower_ReadCurrentTemperature_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niDCPower_ReadCurrentTemperature_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ReadCurrentTemperature_cfunc(vi, temperature)

    def niDCPower_ResetDevice(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ResetDevice_cfunc is None:
                self.niDCPower_ResetDevice_cfunc = self._get_library_function('niDCPower_ResetDevice')
                self.niDCPower_ResetDevice_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDCPower_ResetDevice_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ResetDevice_cfunc(vi)

    def niDCPower_ResetWithChannels(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ResetWithChannels_cfunc is None:
                self.niDCPower_ResetWithChannels_cfunc = self._get_library_function('niDCPower_ResetWithChannels')
                self.niDCPower_ResetWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_ResetWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ResetWithChannels_cfunc(vi, channel_name)

    def niDCPower_ResetWithDefaults(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ResetWithDefaults_cfunc is None:
                self.niDCPower_ResetWithDefaults_cfunc = self._get_library_function('niDCPower_ResetWithDefaults')
                self.niDCPower_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDCPower_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_ResetWithDefaults_cfunc(vi)

    def niDCPower_SendSoftwareEdgeTriggerWithChannels(self, vi, channel_name, trigger):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SendSoftwareEdgeTriggerWithChannels_cfunc is None:
                self.niDCPower_SendSoftwareEdgeTriggerWithChannels_cfunc = self._get_library_function('niDCPower_SendSoftwareEdgeTriggerWithChannels')
                self.niDCPower_SendSoftwareEdgeTriggerWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niDCPower_SendSoftwareEdgeTriggerWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_SendSoftwareEdgeTriggerWithChannels_cfunc(vi, channel_name, trigger)

    def niDCPower_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetAttributeViBoolean_cfunc is None:
                self.niDCPower_SetAttributeViBoolean_cfunc = self._get_library_function('niDCPower_SetAttributeViBoolean')
                self.niDCPower_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niDCPower_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_SetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetAttributeViInt32_cfunc is None:
                self.niDCPower_SetAttributeViInt32_cfunc = self._get_library_function('niDCPower_SetAttributeViInt32')
                self.niDCPower_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niDCPower_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_SetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_SetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetAttributeViInt64_cfunc is None:
                self.niDCPower_SetAttributeViInt64_cfunc = self._get_library_function('niDCPower_SetAttributeViInt64')
                self.niDCPower_SetAttributeViInt64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt64]  # noqa: F405
                self.niDCPower_SetAttributeViInt64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_SetAttributeViInt64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetAttributeViReal64_cfunc is None:
                self.niDCPower_SetAttributeViReal64_cfunc = self._get_library_function('niDCPower_SetAttributeViReal64')
                self.niDCPower_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niDCPower_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_SetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetAttributeViString_cfunc is None:
                self.niDCPower_SetAttributeViString_cfunc = self._get_library_function('niDCPower_SetAttributeViString')
                self.niDCPower_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_SetAttributeViString_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetRuntimeEnvironment_cfunc is None:
                self.niDCPower_SetRuntimeEnvironment_cfunc = self._get_library_function('niDCPower_SetRuntimeEnvironment')
                self.niDCPower_SetRuntimeEnvironment_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_SetRuntimeEnvironment_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_SetRuntimeEnvironment_cfunc(environment, environment_version, reserved1, reserved2)

    def niDCPower_SetSequence(self, vi, channel_name, values, source_delays, size):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetSequence_cfunc is None:
                self.niDCPower_SetSequence_cfunc = self._get_library_function('niDCPower_SetSequence')
                self.niDCPower_SetSequence_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ViUInt32]  # noqa: F405
                self.niDCPower_SetSequence_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_SetSequence_cfunc(vi, channel_name, values, source_delays, size)

    def niDCPower_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_UnlockSession_cfunc is None:
                self.niDCPower_UnlockSession_cfunc = self._get_library_function('niDCPower_UnlockSession')
                self.niDCPower_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niDCPower_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_UnlockSession_cfunc(vi, caller_has_lock)

    def niDCPower_WaitForEventWithChannels(self, vi, channel_name, event_id, timeout):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_WaitForEventWithChannels_cfunc is None:
                self.niDCPower_WaitForEventWithChannels_cfunc = self._get_library_function('niDCPower_WaitForEventWithChannels')
                self.niDCPower_WaitForEventWithChannels_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64]  # noqa: F405
                self.niDCPower_WaitForEventWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_WaitForEventWithChannels_cfunc(vi, channel_name, event_id, timeout)

    def niDCPower_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_close_cfunc is None:
                self.niDCPower_close_cfunc = self._get_library_function('niDCPower_close')
                self.niDCPower_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niDCPower_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_close_cfunc(vi)

    def niDCPower_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_error_message_cfunc is None:
                self.niDCPower_error_message_cfunc = self._get_library_function('niDCPower_error_message')
                self.niDCPower_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_error_message_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_error_message_cfunc(vi, error_code, error_message)

    def niDCPower_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_self_test_cfunc is None:
                self.niDCPower_self_test_cfunc = self._get_library_function('niDCPower_self_test')
                self.niDCPower_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niDCPower_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niDCPower_self_test_cfunc(vi, self_test_result, self_test_message)
