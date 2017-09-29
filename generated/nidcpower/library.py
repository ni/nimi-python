# This file was generated

import ctypes
import threading

from nidcpower.ctypes_types import *  # noqa: F403,H303
import nidcpower.python_types


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, library_name, library_type):
        self._func_lock = threading.Lock()
        # We cache the cfunc object from the ctypes.CDLL object
        self.niDCPower_Abort_cfunc = None
        self.niDCPower_CalAdjustCurrentLimit_cfunc = None
        self.niDCPower_CalAdjustCurrentMeasurement_cfunc = None
        self.niDCPower_CalAdjustInternalReference_cfunc = None
        self.niDCPower_CalAdjustOutputResistance_cfunc = None
        self.niDCPower_CalAdjustResidualCurrentOffset_cfunc = None
        self.niDCPower_CalAdjustResidualVoltageOffset_cfunc = None
        self.niDCPower_CalAdjustVoltageLevel_cfunc = None
        self.niDCPower_CalAdjustVoltageMeasurement_cfunc = None
        self.niDCPower_CalSelfCalibrate_cfunc = None
        self.niDCPower_ChangeExtCalPassword_cfunc = None
        self.niDCPower_ClearError_cfunc = None
        self.niDCPower_ClearInterchangeWarnings_cfunc = None
        self.niDCPower_CloseExtCal_cfunc = None
        self.niDCPower_Commit_cfunc = None
        self.niDCPower_ConfigureApertureTime_cfunc = None
        self.niDCPower_ConfigureAutoZero_cfunc = None
        self.niDCPower_ConfigureCurrentLevel_cfunc = None
        self.niDCPower_ConfigureCurrentLevelRange_cfunc = None
        self.niDCPower_ConfigureCurrentLimit_cfunc = None
        self.niDCPower_ConfigureCurrentLimitRange_cfunc = None
        self.niDCPower_ConfigureDigitalEdgeMeasureTrigger_cfunc = None
        self.niDCPower_ConfigureDigitalEdgePulseTrigger_cfunc = None
        self.niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger_cfunc = None
        self.niDCPower_ConfigureDigitalEdgeSourceTrigger_cfunc = None
        self.niDCPower_ConfigureDigitalEdgeStartTrigger_cfunc = None
        self.niDCPower_ConfigureOutputEnabled_cfunc = None
        self.niDCPower_ConfigureOutputFunction_cfunc = None
        self.niDCPower_ConfigureOutputRange_cfunc = None
        self.niDCPower_ConfigureOutputResistance_cfunc = None
        self.niDCPower_ConfigurePowerLineFrequency_cfunc = None
        self.niDCPower_ConfigurePulseBiasCurrentLevel_cfunc = None
        self.niDCPower_ConfigurePulseBiasCurrentLimit_cfunc = None
        self.niDCPower_ConfigurePulseBiasVoltageLevel_cfunc = None
        self.niDCPower_ConfigurePulseBiasVoltageLimit_cfunc = None
        self.niDCPower_ConfigurePulseCurrentLevel_cfunc = None
        self.niDCPower_ConfigurePulseCurrentLevelRange_cfunc = None
        self.niDCPower_ConfigurePulseCurrentLimit_cfunc = None
        self.niDCPower_ConfigurePulseCurrentLimitRange_cfunc = None
        self.niDCPower_ConfigurePulseVoltageLevel_cfunc = None
        self.niDCPower_ConfigurePulseVoltageLevelRange_cfunc = None
        self.niDCPower_ConfigurePulseVoltageLimit_cfunc = None
        self.niDCPower_ConfigurePulseVoltageLimitRange_cfunc = None
        self.niDCPower_ConfigureSense_cfunc = None
        self.niDCPower_ConfigureSoftwareEdgeMeasureTrigger_cfunc = None
        self.niDCPower_ConfigureSoftwareEdgePulseTrigger_cfunc = None
        self.niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTrigger_cfunc = None
        self.niDCPower_ConfigureSoftwareEdgeSourceTrigger_cfunc = None
        self.niDCPower_ConfigureSoftwareEdgeStartTrigger_cfunc = None
        self.niDCPower_ConfigureSourceMode_cfunc = None
        self.niDCPower_ConfigureVoltageLevel_cfunc = None
        self.niDCPower_ConfigureVoltageLevelRange_cfunc = None
        self.niDCPower_ConfigureVoltageLimit_cfunc = None
        self.niDCPower_ConfigureVoltageLimitRange_cfunc = None
        self.niDCPower_ConnectInternalReference_cfunc = None
        self.niDCPower_CreateAdvancedSequence_cfunc = None
        self.niDCPower_CreateAdvancedSequenceStep_cfunc = None
        self.niDCPower_DeleteAdvancedSequence_cfunc = None
        self.niDCPower_Disable_cfunc = None
        self.niDCPower_DisablePulseTrigger_cfunc = None
        self.niDCPower_DisableSequenceAdvanceTrigger_cfunc = None
        self.niDCPower_DisableSourceTrigger_cfunc = None
        self.niDCPower_DisableStartTrigger_cfunc = None
        self.niDCPower_ExportSignal_cfunc = None
        self.niDCPower_FetchMultiple_cfunc = None
        self.niDCPower_GetAttributeViBoolean_cfunc = None
        self.niDCPower_GetAttributeViInt32_cfunc = None
        self.niDCPower_GetAttributeViInt64_cfunc = None
        self.niDCPower_GetAttributeViReal64_cfunc = None
        self.niDCPower_GetAttributeViSession_cfunc = None
        self.niDCPower_GetAttributeViString_cfunc = None
        self.niDCPower_GetCalUserDefinedInfo_cfunc = None
        self.niDCPower_GetCalUserDefinedInfoMaxSize_cfunc = None
        self.niDCPower_GetChannelName_cfunc = None
        self.niDCPower_GetError_cfunc = None
        self.niDCPower_GetExtCalLastDateAndTime_cfunc = None
        self.niDCPower_GetExtCalLastTemp_cfunc = None
        self.niDCPower_GetExtCalRecommendedInterval_cfunc = None
        self.niDCPower_GetNextCoercionRecord_cfunc = None
        self.niDCPower_GetNextInterchangeWarning_cfunc = None
        self.niDCPower_GetSelfCalLastDateAndTime_cfunc = None
        self.niDCPower_GetSelfCalLastTemp_cfunc = None
        self.niDCPower_InitExtCal_cfunc = None
        self.niDCPower_InitWithOptions_cfunc = None
        self.niDCPower_InitializeWithChannels_cfunc = None
        self.niDCPower_Initiate_cfunc = None
        self.niDCPower_LockSession_cfunc = None
        self.niDCPower_Measure_cfunc = None
        self.niDCPower_MeasureMultiple_cfunc = None
        self.niDCPower_QueryInCompliance_cfunc = None
        self.niDCPower_QueryMaxCurrentLimit_cfunc = None
        self.niDCPower_QueryMaxVoltageLevel_cfunc = None
        self.niDCPower_QueryMinCurrentLimit_cfunc = None
        self.niDCPower_QueryOutputState_cfunc = None
        self.niDCPower_ReadCurrentTemperature_cfunc = None
        self.niDCPower_ResetDevice_cfunc = None
        self.niDCPower_ResetInterchangeCheck_cfunc = None
        self.niDCPower_ResetWithDefaults_cfunc = None
        self.niDCPower_SendSoftwareEdgeTrigger_cfunc = None
        self.niDCPower_SetAttributeViBoolean_cfunc = None
        self.niDCPower_SetAttributeViInt32_cfunc = None
        self.niDCPower_SetAttributeViInt64_cfunc = None
        self.niDCPower_SetAttributeViReal64_cfunc = None
        self.niDCPower_SetAttributeViSession_cfunc = None
        self.niDCPower_SetAttributeViString_cfunc = None
        self.niDCPower_SetCalUserDefinedInfo_cfunc = None
        self.niDCPower_SetSequence_cfunc = None
        self.niDCPower_UnlockSession_cfunc = None
        self.niDCPower_WaitForEvent_cfunc = None
        self.niDCPower_close_cfunc = None
        self.niDCPower_error_message_cfunc = None
        self.niDCPower_init_cfunc = None
        self.niDCPower_reset_cfunc = None
        self.niDCPower_revision_query_cfunc = None
        self.niDCPower_self_test_cfunc = None

        if library_type == 'windll':
            self._library = ctypes.WinDLL(library_name)
        else:  # pragma: no cover
            assert library_type == 'cdll'
            self._library = ctypes.CDLL(library_name)

    def niDCPower_Abort(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_Abort_cfunc is None:
                self.niDCPower_Abort_cfunc = self._library.niDCPower_Abort
                self.niDCPower_Abort_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_Abort_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_Abort_cfunc(vi)

    def niDCPower_CalAdjustCurrentLimit(self, vi, channel_name, range, number_of_measurements, requested_outputs, measured_outputs):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CalAdjustCurrentLimit_cfunc is None:
                self.niDCPower_CalAdjustCurrentLimit_cfunc = self._library.niDCPower_CalAdjustCurrentLimit
                self.niDCPower_CalAdjustCurrentLimit_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype, ViUInt32_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_CalAdjustCurrentLimit_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_CalAdjustCurrentLimit_cfunc(vi, channel_name, range, number_of_measurements, requested_outputs, measured_outputs)

    def niDCPower_CalAdjustCurrentMeasurement(self, vi, channel_name, range, number_of_measurements, reported_outputs, measured_outputs):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CalAdjustCurrentMeasurement_cfunc is None:
                self.niDCPower_CalAdjustCurrentMeasurement_cfunc = self._library.niDCPower_CalAdjustCurrentMeasurement
                self.niDCPower_CalAdjustCurrentMeasurement_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype, ViUInt32_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_CalAdjustCurrentMeasurement_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_CalAdjustCurrentMeasurement_cfunc(vi, channel_name, range, number_of_measurements, reported_outputs, measured_outputs)

    def niDCPower_CalAdjustInternalReference(self, vi, internal_reference, adjusted_internal_reference):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CalAdjustInternalReference_cfunc is None:
                self.niDCPower_CalAdjustInternalReference_cfunc = self._library.niDCPower_CalAdjustInternalReference
                self.niDCPower_CalAdjustInternalReference_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_CalAdjustInternalReference_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_CalAdjustInternalReference_cfunc(vi, internal_reference, adjusted_internal_reference)

    def niDCPower_CalAdjustOutputResistance(self, vi, channel_name, number_of_measurements, requested_outputs, measured_outputs):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CalAdjustOutputResistance_cfunc is None:
                self.niDCPower_CalAdjustOutputResistance_cfunc = self._library.niDCPower_CalAdjustOutputResistance
                self.niDCPower_CalAdjustOutputResistance_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViUInt32_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_CalAdjustOutputResistance_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_CalAdjustOutputResistance_cfunc(vi, channel_name, number_of_measurements, requested_outputs, measured_outputs)

    def niDCPower_CalAdjustResidualCurrentOffset(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CalAdjustResidualCurrentOffset_cfunc is None:
                self.niDCPower_CalAdjustResidualCurrentOffset_cfunc = self._library.niDCPower_CalAdjustResidualCurrentOffset
                self.niDCPower_CalAdjustResidualCurrentOffset_cfunc.argtypes = [ViSession_ctype, ViChar_ctype]  # noqa: F405
                self.niDCPower_CalAdjustResidualCurrentOffset_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_CalAdjustResidualCurrentOffset_cfunc(vi, channel_name)

    def niDCPower_CalAdjustResidualVoltageOffset(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CalAdjustResidualVoltageOffset_cfunc is None:
                self.niDCPower_CalAdjustResidualVoltageOffset_cfunc = self._library.niDCPower_CalAdjustResidualVoltageOffset
                self.niDCPower_CalAdjustResidualVoltageOffset_cfunc.argtypes = [ViSession_ctype, ViChar_ctype]  # noqa: F405
                self.niDCPower_CalAdjustResidualVoltageOffset_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_CalAdjustResidualVoltageOffset_cfunc(vi, channel_name)

    def niDCPower_CalAdjustVoltageLevel(self, vi, channel_name, range, number_of_measurements, requested_outputs, measured_outputs):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CalAdjustVoltageLevel_cfunc is None:
                self.niDCPower_CalAdjustVoltageLevel_cfunc = self._library.niDCPower_CalAdjustVoltageLevel
                self.niDCPower_CalAdjustVoltageLevel_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype, ViUInt32_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_CalAdjustVoltageLevel_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_CalAdjustVoltageLevel_cfunc(vi, channel_name, range, number_of_measurements, requested_outputs, measured_outputs)

    def niDCPower_CalAdjustVoltageMeasurement(self, vi, channel_name, range, number_of_measurements, reported_outputs, measured_outputs):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CalAdjustVoltageMeasurement_cfunc is None:
                self.niDCPower_CalAdjustVoltageMeasurement_cfunc = self._library.niDCPower_CalAdjustVoltageMeasurement
                self.niDCPower_CalAdjustVoltageMeasurement_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype, ViUInt32_ctype, ViReal64_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_CalAdjustVoltageMeasurement_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_CalAdjustVoltageMeasurement_cfunc(vi, channel_name, range, number_of_measurements, reported_outputs, measured_outputs)

    def niDCPower_CalSelfCalibrate(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CalSelfCalibrate_cfunc is None:
                self.niDCPower_CalSelfCalibrate_cfunc = self._library.niDCPower_CalSelfCalibrate
                self.niDCPower_CalSelfCalibrate_cfunc.argtypes = [ViSession_ctype, ViChar_ctype]  # noqa: F405
                self.niDCPower_CalSelfCalibrate_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_CalSelfCalibrate_cfunc(vi, channel_name)

    def niDCPower_ChangeExtCalPassword(self, vi, old_password, new_password):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ChangeExtCalPassword_cfunc is None:
                self.niDCPower_ChangeExtCalPassword_cfunc = self._library.niDCPower_ChangeExtCalPassword
                self.niDCPower_ChangeExtCalPassword_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViChar_ctype]  # noqa: F405
                self.niDCPower_ChangeExtCalPassword_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ChangeExtCalPassword_cfunc(vi, old_password, new_password)

    def niDCPower_ClearError(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ClearError_cfunc is None:
                self.niDCPower_ClearError_cfunc = self._library.niDCPower_ClearError
                self.niDCPower_ClearError_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_ClearError_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ClearError_cfunc(vi)

    def niDCPower_ClearInterchangeWarnings(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ClearInterchangeWarnings_cfunc is None:
                self.niDCPower_ClearInterchangeWarnings_cfunc = self._library.niDCPower_ClearInterchangeWarnings
                self.niDCPower_ClearInterchangeWarnings_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_ClearInterchangeWarnings_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ClearInterchangeWarnings_cfunc(vi)

    def niDCPower_CloseExtCal(self, vi, action):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CloseExtCal_cfunc is None:
                self.niDCPower_CloseExtCal_cfunc = self._library.niDCPower_CloseExtCal
                self.niDCPower_CloseExtCal_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
                self.niDCPower_CloseExtCal_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_CloseExtCal_cfunc(vi, action)

    def niDCPower_Commit(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_Commit_cfunc is None:
                self.niDCPower_Commit_cfunc = self._library.niDCPower_Commit
                self.niDCPower_Commit_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_Commit_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_Commit_cfunc(vi)

    def niDCPower_ConfigureApertureTime(self, vi, channel_name, aperture_time, units):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureApertureTime_cfunc is None:
                self.niDCPower_ConfigureApertureTime_cfunc = self._library.niDCPower_ConfigureApertureTime
                self.niDCPower_ConfigureApertureTime_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype, ViInt32_ctype]  # noqa: F405
                self.niDCPower_ConfigureApertureTime_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureApertureTime_cfunc(vi, channel_name, aperture_time, units)

    def niDCPower_ConfigureAutoZero(self, vi, channel_name, auto_zero):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureAutoZero_cfunc is None:
                self.niDCPower_ConfigureAutoZero_cfunc = self._library.niDCPower_ConfigureAutoZero
                self.niDCPower_ConfigureAutoZero_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViInt32_ctype]  # noqa: F405
                self.niDCPower_ConfigureAutoZero_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureAutoZero_cfunc(vi, channel_name, auto_zero)

    def niDCPower_ConfigureCurrentLevel(self, vi, channel_name, level):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureCurrentLevel_cfunc is None:
                self.niDCPower_ConfigureCurrentLevel_cfunc = self._library.niDCPower_ConfigureCurrentLevel
                self.niDCPower_ConfigureCurrentLevel_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigureCurrentLevel_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureCurrentLevel_cfunc(vi, channel_name, level)

    def niDCPower_ConfigureCurrentLevelRange(self, vi, channel_name, range):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureCurrentLevelRange_cfunc is None:
                self.niDCPower_ConfigureCurrentLevelRange_cfunc = self._library.niDCPower_ConfigureCurrentLevelRange
                self.niDCPower_ConfigureCurrentLevelRange_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigureCurrentLevelRange_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureCurrentLevelRange_cfunc(vi, channel_name, range)

    def niDCPower_ConfigureCurrentLimit(self, vi, channel_name, behavior, limit):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureCurrentLimit_cfunc is None:
                self.niDCPower_ConfigureCurrentLimit_cfunc = self._library.niDCPower_ConfigureCurrentLimit
                self.niDCPower_ConfigureCurrentLimit_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViInt32_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigureCurrentLimit_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureCurrentLimit_cfunc(vi, channel_name, behavior, limit)

    def niDCPower_ConfigureCurrentLimitRange(self, vi, channel_name, range):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureCurrentLimitRange_cfunc is None:
                self.niDCPower_ConfigureCurrentLimitRange_cfunc = self._library.niDCPower_ConfigureCurrentLimitRange
                self.niDCPower_ConfigureCurrentLimitRange_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigureCurrentLimitRange_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureCurrentLimitRange_cfunc(vi, channel_name, range)

    def niDCPower_ConfigureDigitalEdgeMeasureTrigger(self, vi, input_terminal, edge):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureDigitalEdgeMeasureTrigger_cfunc is None:
                self.niDCPower_ConfigureDigitalEdgeMeasureTrigger_cfunc = self._library.niDCPower_ConfigureDigitalEdgeMeasureTrigger
                self.niDCPower_ConfigureDigitalEdgeMeasureTrigger_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViInt32_ctype]  # noqa: F405
                self.niDCPower_ConfigureDigitalEdgeMeasureTrigger_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureDigitalEdgeMeasureTrigger_cfunc(vi, input_terminal, edge)

    def niDCPower_ConfigureDigitalEdgePulseTrigger(self, vi, input_terminal, edge):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureDigitalEdgePulseTrigger_cfunc is None:
                self.niDCPower_ConfigureDigitalEdgePulseTrigger_cfunc = self._library.niDCPower_ConfigureDigitalEdgePulseTrigger
                self.niDCPower_ConfigureDigitalEdgePulseTrigger_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViInt32_ctype]  # noqa: F405
                self.niDCPower_ConfigureDigitalEdgePulseTrigger_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureDigitalEdgePulseTrigger_cfunc(vi, input_terminal, edge)

    def niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger(self, vi, input_terminal, edge):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger_cfunc is None:
                self.niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger_cfunc = self._library.niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger
                self.niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViInt32_ctype]  # noqa: F405
                self.niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger_cfunc(vi, input_terminal, edge)

    def niDCPower_ConfigureDigitalEdgeSourceTrigger(self, vi, input_terminal, edge):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureDigitalEdgeSourceTrigger_cfunc is None:
                self.niDCPower_ConfigureDigitalEdgeSourceTrigger_cfunc = self._library.niDCPower_ConfigureDigitalEdgeSourceTrigger
                self.niDCPower_ConfigureDigitalEdgeSourceTrigger_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViInt32_ctype]  # noqa: F405
                self.niDCPower_ConfigureDigitalEdgeSourceTrigger_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureDigitalEdgeSourceTrigger_cfunc(vi, input_terminal, edge)

    def niDCPower_ConfigureDigitalEdgeStartTrigger(self, vi, input_terminal, edge):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureDigitalEdgeStartTrigger_cfunc is None:
                self.niDCPower_ConfigureDigitalEdgeStartTrigger_cfunc = self._library.niDCPower_ConfigureDigitalEdgeStartTrigger
                self.niDCPower_ConfigureDigitalEdgeStartTrigger_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViInt32_ctype]  # noqa: F405
                self.niDCPower_ConfigureDigitalEdgeStartTrigger_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureDigitalEdgeStartTrigger_cfunc(vi, input_terminal, edge)

    def niDCPower_ConfigureOutputEnabled(self, vi, channel_name, enabled):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureOutputEnabled_cfunc is None:
                self.niDCPower_ConfigureOutputEnabled_cfunc = self._library.niDCPower_ConfigureOutputEnabled
                self.niDCPower_ConfigureOutputEnabled_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViBoolean_ctype]  # noqa: F405
                self.niDCPower_ConfigureOutputEnabled_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureOutputEnabled_cfunc(vi, channel_name, enabled)

    def niDCPower_ConfigureOutputFunction(self, vi, channel_name, function):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureOutputFunction_cfunc is None:
                self.niDCPower_ConfigureOutputFunction_cfunc = self._library.niDCPower_ConfigureOutputFunction
                self.niDCPower_ConfigureOutputFunction_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViInt32_ctype]  # noqa: F405
                self.niDCPower_ConfigureOutputFunction_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureOutputFunction_cfunc(vi, channel_name, function)

    def niDCPower_ConfigureOutputRange(self, vi, channel_name, range_type, range):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureOutputRange_cfunc is None:
                self.niDCPower_ConfigureOutputRange_cfunc = self._library.niDCPower_ConfigureOutputRange
                self.niDCPower_ConfigureOutputRange_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViInt32_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigureOutputRange_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureOutputRange_cfunc(vi, channel_name, range_type, range)

    def niDCPower_ConfigureOutputResistance(self, vi, channel_name, resistance):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureOutputResistance_cfunc is None:
                self.niDCPower_ConfigureOutputResistance_cfunc = self._library.niDCPower_ConfigureOutputResistance
                self.niDCPower_ConfigureOutputResistance_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigureOutputResistance_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureOutputResistance_cfunc(vi, channel_name, resistance)

    def niDCPower_ConfigurePowerLineFrequency(self, vi, powerline_frequency):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigurePowerLineFrequency_cfunc is None:
                self.niDCPower_ConfigurePowerLineFrequency_cfunc = self._library.niDCPower_ConfigurePowerLineFrequency
                self.niDCPower_ConfigurePowerLineFrequency_cfunc.argtypes = [ViSession_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigurePowerLineFrequency_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigurePowerLineFrequency_cfunc(vi, powerline_frequency)

    def niDCPower_ConfigurePulseBiasCurrentLevel(self, vi, channel_name, level):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigurePulseBiasCurrentLevel_cfunc is None:
                self.niDCPower_ConfigurePulseBiasCurrentLevel_cfunc = self._library.niDCPower_ConfigurePulseBiasCurrentLevel
                self.niDCPower_ConfigurePulseBiasCurrentLevel_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigurePulseBiasCurrentLevel_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigurePulseBiasCurrentLevel_cfunc(vi, channel_name, level)

    def niDCPower_ConfigurePulseBiasCurrentLimit(self, vi, channel_name, limit):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigurePulseBiasCurrentLimit_cfunc is None:
                self.niDCPower_ConfigurePulseBiasCurrentLimit_cfunc = self._library.niDCPower_ConfigurePulseBiasCurrentLimit
                self.niDCPower_ConfigurePulseBiasCurrentLimit_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigurePulseBiasCurrentLimit_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigurePulseBiasCurrentLimit_cfunc(vi, channel_name, limit)

    def niDCPower_ConfigurePulseBiasVoltageLevel(self, vi, channel_name, level):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigurePulseBiasVoltageLevel_cfunc is None:
                self.niDCPower_ConfigurePulseBiasVoltageLevel_cfunc = self._library.niDCPower_ConfigurePulseBiasVoltageLevel
                self.niDCPower_ConfigurePulseBiasVoltageLevel_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigurePulseBiasVoltageLevel_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigurePulseBiasVoltageLevel_cfunc(vi, channel_name, level)

    def niDCPower_ConfigurePulseBiasVoltageLimit(self, vi, channel_name, limit):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigurePulseBiasVoltageLimit_cfunc is None:
                self.niDCPower_ConfigurePulseBiasVoltageLimit_cfunc = self._library.niDCPower_ConfigurePulseBiasVoltageLimit
                self.niDCPower_ConfigurePulseBiasVoltageLimit_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigurePulseBiasVoltageLimit_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigurePulseBiasVoltageLimit_cfunc(vi, channel_name, limit)

    def niDCPower_ConfigurePulseCurrentLevel(self, vi, channel_name, level):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigurePulseCurrentLevel_cfunc is None:
                self.niDCPower_ConfigurePulseCurrentLevel_cfunc = self._library.niDCPower_ConfigurePulseCurrentLevel
                self.niDCPower_ConfigurePulseCurrentLevel_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigurePulseCurrentLevel_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigurePulseCurrentLevel_cfunc(vi, channel_name, level)

    def niDCPower_ConfigurePulseCurrentLevelRange(self, vi, channel_name, range):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigurePulseCurrentLevelRange_cfunc is None:
                self.niDCPower_ConfigurePulseCurrentLevelRange_cfunc = self._library.niDCPower_ConfigurePulseCurrentLevelRange
                self.niDCPower_ConfigurePulseCurrentLevelRange_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigurePulseCurrentLevelRange_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigurePulseCurrentLevelRange_cfunc(vi, channel_name, range)

    def niDCPower_ConfigurePulseCurrentLimit(self, vi, channel_name, limit):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigurePulseCurrentLimit_cfunc is None:
                self.niDCPower_ConfigurePulseCurrentLimit_cfunc = self._library.niDCPower_ConfigurePulseCurrentLimit
                self.niDCPower_ConfigurePulseCurrentLimit_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigurePulseCurrentLimit_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigurePulseCurrentLimit_cfunc(vi, channel_name, limit)

    def niDCPower_ConfigurePulseCurrentLimitRange(self, vi, channel_name, range):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigurePulseCurrentLimitRange_cfunc is None:
                self.niDCPower_ConfigurePulseCurrentLimitRange_cfunc = self._library.niDCPower_ConfigurePulseCurrentLimitRange
                self.niDCPower_ConfigurePulseCurrentLimitRange_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigurePulseCurrentLimitRange_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigurePulseCurrentLimitRange_cfunc(vi, channel_name, range)

    def niDCPower_ConfigurePulseVoltageLevel(self, vi, channel_name, level):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigurePulseVoltageLevel_cfunc is None:
                self.niDCPower_ConfigurePulseVoltageLevel_cfunc = self._library.niDCPower_ConfigurePulseVoltageLevel
                self.niDCPower_ConfigurePulseVoltageLevel_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigurePulseVoltageLevel_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigurePulseVoltageLevel_cfunc(vi, channel_name, level)

    def niDCPower_ConfigurePulseVoltageLevelRange(self, vi, channel_name, range):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigurePulseVoltageLevelRange_cfunc is None:
                self.niDCPower_ConfigurePulseVoltageLevelRange_cfunc = self._library.niDCPower_ConfigurePulseVoltageLevelRange
                self.niDCPower_ConfigurePulseVoltageLevelRange_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigurePulseVoltageLevelRange_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigurePulseVoltageLevelRange_cfunc(vi, channel_name, range)

    def niDCPower_ConfigurePulseVoltageLimit(self, vi, channel_name, limit):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigurePulseVoltageLimit_cfunc is None:
                self.niDCPower_ConfigurePulseVoltageLimit_cfunc = self._library.niDCPower_ConfigurePulseVoltageLimit
                self.niDCPower_ConfigurePulseVoltageLimit_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigurePulseVoltageLimit_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigurePulseVoltageLimit_cfunc(vi, channel_name, limit)

    def niDCPower_ConfigurePulseVoltageLimitRange(self, vi, channel_name, range):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigurePulseVoltageLimitRange_cfunc is None:
                self.niDCPower_ConfigurePulseVoltageLimitRange_cfunc = self._library.niDCPower_ConfigurePulseVoltageLimitRange
                self.niDCPower_ConfigurePulseVoltageLimitRange_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigurePulseVoltageLimitRange_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigurePulseVoltageLimitRange_cfunc(vi, channel_name, range)

    def niDCPower_ConfigureSense(self, vi, channel_name, sense):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureSense_cfunc is None:
                self.niDCPower_ConfigureSense_cfunc = self._library.niDCPower_ConfigureSense
                self.niDCPower_ConfigureSense_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViInt32_ctype]  # noqa: F405
                self.niDCPower_ConfigureSense_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureSense_cfunc(vi, channel_name, sense)

    def niDCPower_ConfigureSoftwareEdgeMeasureTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureSoftwareEdgeMeasureTrigger_cfunc is None:
                self.niDCPower_ConfigureSoftwareEdgeMeasureTrigger_cfunc = self._library.niDCPower_ConfigureSoftwareEdgeMeasureTrigger
                self.niDCPower_ConfigureSoftwareEdgeMeasureTrigger_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_ConfigureSoftwareEdgeMeasureTrigger_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureSoftwareEdgeMeasureTrigger_cfunc(vi)

    def niDCPower_ConfigureSoftwareEdgePulseTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureSoftwareEdgePulseTrigger_cfunc is None:
                self.niDCPower_ConfigureSoftwareEdgePulseTrigger_cfunc = self._library.niDCPower_ConfigureSoftwareEdgePulseTrigger
                self.niDCPower_ConfigureSoftwareEdgePulseTrigger_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_ConfigureSoftwareEdgePulseTrigger_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureSoftwareEdgePulseTrigger_cfunc(vi)

    def niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTrigger_cfunc is None:
                self.niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTrigger_cfunc = self._library.niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTrigger
                self.niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTrigger_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTrigger_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTrigger_cfunc(vi)

    def niDCPower_ConfigureSoftwareEdgeSourceTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureSoftwareEdgeSourceTrigger_cfunc is None:
                self.niDCPower_ConfigureSoftwareEdgeSourceTrigger_cfunc = self._library.niDCPower_ConfigureSoftwareEdgeSourceTrigger
                self.niDCPower_ConfigureSoftwareEdgeSourceTrigger_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_ConfigureSoftwareEdgeSourceTrigger_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureSoftwareEdgeSourceTrigger_cfunc(vi)

    def niDCPower_ConfigureSoftwareEdgeStartTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureSoftwareEdgeStartTrigger_cfunc is None:
                self.niDCPower_ConfigureSoftwareEdgeStartTrigger_cfunc = self._library.niDCPower_ConfigureSoftwareEdgeStartTrigger
                self.niDCPower_ConfigureSoftwareEdgeStartTrigger_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_ConfigureSoftwareEdgeStartTrigger_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureSoftwareEdgeStartTrigger_cfunc(vi)

    def niDCPower_ConfigureSourceMode(self, vi, source_mode):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureSourceMode_cfunc is None:
                self.niDCPower_ConfigureSourceMode_cfunc = self._library.niDCPower_ConfigureSourceMode
                self.niDCPower_ConfigureSourceMode_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
                self.niDCPower_ConfigureSourceMode_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureSourceMode_cfunc(vi, source_mode)

    def niDCPower_ConfigureVoltageLevel(self, vi, channel_name, level):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureVoltageLevel_cfunc is None:
                self.niDCPower_ConfigureVoltageLevel_cfunc = self._library.niDCPower_ConfigureVoltageLevel
                self.niDCPower_ConfigureVoltageLevel_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigureVoltageLevel_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureVoltageLevel_cfunc(vi, channel_name, level)

    def niDCPower_ConfigureVoltageLevelRange(self, vi, channel_name, range):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureVoltageLevelRange_cfunc is None:
                self.niDCPower_ConfigureVoltageLevelRange_cfunc = self._library.niDCPower_ConfigureVoltageLevelRange
                self.niDCPower_ConfigureVoltageLevelRange_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigureVoltageLevelRange_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureVoltageLevelRange_cfunc(vi, channel_name, range)

    def niDCPower_ConfigureVoltageLimit(self, vi, channel_name, limit):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureVoltageLimit_cfunc is None:
                self.niDCPower_ConfigureVoltageLimit_cfunc = self._library.niDCPower_ConfigureVoltageLimit
                self.niDCPower_ConfigureVoltageLimit_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigureVoltageLimit_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureVoltageLimit_cfunc(vi, channel_name, limit)

    def niDCPower_ConfigureVoltageLimitRange(self, vi, channel_name, range):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConfigureVoltageLimitRange_cfunc is None:
                self.niDCPower_ConfigureVoltageLimitRange_cfunc = self._library.niDCPower_ConfigureVoltageLimitRange
                self.niDCPower_ConfigureVoltageLimitRange_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_ConfigureVoltageLimitRange_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConfigureVoltageLimitRange_cfunc(vi, channel_name, range)

    def niDCPower_ConnectInternalReference(self, vi, internal_reference):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ConnectInternalReference_cfunc is None:
                self.niDCPower_ConnectInternalReference_cfunc = self._library.niDCPower_ConnectInternalReference
                self.niDCPower_ConnectInternalReference_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
                self.niDCPower_ConnectInternalReference_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ConnectInternalReference_cfunc(vi, internal_reference)

    def niDCPower_CreateAdvancedSequence(self, vi, sequence_name, attribute_id_count, attribute_ids, set_as_active_sequence):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CreateAdvancedSequence_cfunc is None:
                self.niDCPower_CreateAdvancedSequence_cfunc = self._library.niDCPower_CreateAdvancedSequence
                self.niDCPower_CreateAdvancedSequence_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype, ViInt32_ctype, ViInt32_ctype, ViBoolean_ctype]  # noqa: F405
                self.niDCPower_CreateAdvancedSequence_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_CreateAdvancedSequence_cfunc(vi, sequence_name, attribute_id_count, attribute_ids, set_as_active_sequence)

    def niDCPower_CreateAdvancedSequenceStep(self, vi, set_as_active_step):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_CreateAdvancedSequenceStep_cfunc is None:
                self.niDCPower_CreateAdvancedSequenceStep_cfunc = self._library.niDCPower_CreateAdvancedSequenceStep
                self.niDCPower_CreateAdvancedSequenceStep_cfunc.argtypes = [ViSession_ctype, ViBoolean_ctype]  # noqa: F405
                self.niDCPower_CreateAdvancedSequenceStep_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_CreateAdvancedSequenceStep_cfunc(vi, set_as_active_step)

    def niDCPower_DeleteAdvancedSequence(self, vi, sequence_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_DeleteAdvancedSequence_cfunc is None:
                self.niDCPower_DeleteAdvancedSequence_cfunc = self._library.niDCPower_DeleteAdvancedSequence
                self.niDCPower_DeleteAdvancedSequence_cfunc.argtypes = [ViSession_ctype, ViConstString_ctype]  # noqa: F405
                self.niDCPower_DeleteAdvancedSequence_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_DeleteAdvancedSequence_cfunc(vi, sequence_name)

    def niDCPower_Disable(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_Disable_cfunc is None:
                self.niDCPower_Disable_cfunc = self._library.niDCPower_Disable
                self.niDCPower_Disable_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_Disable_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_Disable_cfunc(vi)

    def niDCPower_DisablePulseTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_DisablePulseTrigger_cfunc is None:
                self.niDCPower_DisablePulseTrigger_cfunc = self._library.niDCPower_DisablePulseTrigger
                self.niDCPower_DisablePulseTrigger_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_DisablePulseTrigger_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_DisablePulseTrigger_cfunc(vi)

    def niDCPower_DisableSequenceAdvanceTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_DisableSequenceAdvanceTrigger_cfunc is None:
                self.niDCPower_DisableSequenceAdvanceTrigger_cfunc = self._library.niDCPower_DisableSequenceAdvanceTrigger
                self.niDCPower_DisableSequenceAdvanceTrigger_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_DisableSequenceAdvanceTrigger_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_DisableSequenceAdvanceTrigger_cfunc(vi)

    def niDCPower_DisableSourceTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_DisableSourceTrigger_cfunc is None:
                self.niDCPower_DisableSourceTrigger_cfunc = self._library.niDCPower_DisableSourceTrigger
                self.niDCPower_DisableSourceTrigger_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_DisableSourceTrigger_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_DisableSourceTrigger_cfunc(vi)

    def niDCPower_DisableStartTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_DisableStartTrigger_cfunc is None:
                self.niDCPower_DisableStartTrigger_cfunc = self._library.niDCPower_DisableStartTrigger
                self.niDCPower_DisableStartTrigger_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_DisableStartTrigger_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_DisableStartTrigger_cfunc(vi)

    def niDCPower_ExportSignal(self, vi, signal, signal_identifier, output_terminal):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ExportSignal_cfunc is None:
                self.niDCPower_ExportSignal_cfunc = self._library.niDCPower_ExportSignal
                self.niDCPower_ExportSignal_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViChar_ctype, ViChar_ctype]  # noqa: F405
                self.niDCPower_ExportSignal_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ExportSignal_cfunc(vi, signal, signal_identifier, output_terminal)

    def niDCPower_FetchMultiple(self, vi, channel_name, timeout, count, voltage_measurements, current_measurements, in_compliance, actual_count):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_FetchMultiple_cfunc is None:
                self.niDCPower_FetchMultiple_cfunc = self._library.niDCPower_FetchMultiple
                self.niDCPower_FetchMultiple_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViBoolean_ctype), ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
                self.niDCPower_FetchMultiple_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_FetchMultiple_cfunc(vi, channel_name, timeout, count, voltage_measurements, current_measurements, in_compliance, actual_count)

    def niDCPower_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetAttributeViBoolean_cfunc is None:
                self.niDCPower_GetAttributeViBoolean_cfunc = self._library.niDCPower_GetAttributeViBoolean
                self.niDCPower_GetAttributeViBoolean_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViAttr_ctype, ctypes.POINTER(ViBoolean_ctype)]  # noqa: F405
                self.niDCPower_GetAttributeViBoolean_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_GetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetAttributeViInt32_cfunc is None:
                self.niDCPower_GetAttributeViInt32_cfunc = self._library.niDCPower_GetAttributeViInt32
                self.niDCPower_GetAttributeViInt32_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViAttr_ctype, ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
                self.niDCPower_GetAttributeViInt32_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_GetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_GetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetAttributeViInt64_cfunc is None:
                self.niDCPower_GetAttributeViInt64_cfunc = self._library.niDCPower_GetAttributeViInt64
                self.niDCPower_GetAttributeViInt64_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViAttr_ctype, ctypes.POINTER(ViInt64_ctype)]  # noqa: F405
                self.niDCPower_GetAttributeViInt64_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_GetAttributeViInt64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetAttributeViReal64_cfunc is None:
                self.niDCPower_GetAttributeViReal64_cfunc = self._library.niDCPower_GetAttributeViReal64
                self.niDCPower_GetAttributeViReal64_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViAttr_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niDCPower_GetAttributeViReal64_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_GetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_GetAttributeViSession(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetAttributeViSession_cfunc is None:
                self.niDCPower_GetAttributeViSession_cfunc = self._library.niDCPower_GetAttributeViSession
                self.niDCPower_GetAttributeViSession_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViAttr_ctype, ctypes.POINTER(ViSession_ctype)]  # noqa: F405
                self.niDCPower_GetAttributeViSession_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_GetAttributeViSession_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetAttributeViString_cfunc is None:
                self.niDCPower_GetAttributeViString_cfunc = self._library.niDCPower_GetAttributeViString
                self.niDCPower_GetAttributeViString_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViAttr_ctype, ViInt32_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niDCPower_GetAttributeViString_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_GetAttributeViString_cfunc(vi, channel_name, attribute_id, buffer_size, attribute_value)

    def niDCPower_GetCalUserDefinedInfo(self, vi, info):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetCalUserDefinedInfo_cfunc is None:
                self.niDCPower_GetCalUserDefinedInfo_cfunc = self._library.niDCPower_GetCalUserDefinedInfo
                self.niDCPower_GetCalUserDefinedInfo_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niDCPower_GetCalUserDefinedInfo_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_GetCalUserDefinedInfo_cfunc(vi, info)

    def niDCPower_GetCalUserDefinedInfoMaxSize(self, vi, info_size):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetCalUserDefinedInfoMaxSize_cfunc is None:
                self.niDCPower_GetCalUserDefinedInfoMaxSize_cfunc = self._library.niDCPower_GetCalUserDefinedInfoMaxSize
                self.niDCPower_GetCalUserDefinedInfoMaxSize_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
                self.niDCPower_GetCalUserDefinedInfoMaxSize_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_GetCalUserDefinedInfoMaxSize_cfunc(vi, info_size)

    def niDCPower_GetChannelName(self, vi, index, buffer_size, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetChannelName_cfunc is None:
                self.niDCPower_GetChannelName_cfunc = self._library.niDCPower_GetChannelName
                self.niDCPower_GetChannelName_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niDCPower_GetChannelName_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_GetChannelName_cfunc(vi, index, buffer_size, channel_name)

    def niDCPower_GetError(self, vi, code, buffer_size, description):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetError_cfunc is None:
                self.niDCPower_GetError_cfunc = self._library.niDCPower_GetError
                self.niDCPower_GetError_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViStatus_ctype), ViInt32_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niDCPower_GetError_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_GetError_cfunc(vi, code, buffer_size, description)

    def niDCPower_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetExtCalLastDateAndTime_cfunc is None:
                self.niDCPower_GetExtCalLastDateAndTime_cfunc = self._library.niDCPower_GetExtCalLastDateAndTime
                self.niDCPower_GetExtCalLastDateAndTime_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
                self.niDCPower_GetExtCalLastDateAndTime_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_GetExtCalLastDateAndTime_cfunc(vi, year, month, day, hour, minute)

    def niDCPower_GetExtCalLastTemp(self, vi, temperature):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetExtCalLastTemp_cfunc is None:
                self.niDCPower_GetExtCalLastTemp_cfunc = self._library.niDCPower_GetExtCalLastTemp
                self.niDCPower_GetExtCalLastTemp_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niDCPower_GetExtCalLastTemp_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_GetExtCalLastTemp_cfunc(vi, temperature)

    def niDCPower_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetExtCalRecommendedInterval_cfunc is None:
                self.niDCPower_GetExtCalRecommendedInterval_cfunc = self._library.niDCPower_GetExtCalRecommendedInterval
                self.niDCPower_GetExtCalRecommendedInterval_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
                self.niDCPower_GetExtCalRecommendedInterval_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_GetExtCalRecommendedInterval_cfunc(vi, months)

    def niDCPower_GetNextCoercionRecord(self, vi, buffer_size, coercion_record):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetNextCoercionRecord_cfunc is None:
                self.niDCPower_GetNextCoercionRecord_cfunc = self._library.niDCPower_GetNextCoercionRecord
                self.niDCPower_GetNextCoercionRecord_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niDCPower_GetNextCoercionRecord_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_GetNextCoercionRecord_cfunc(vi, buffer_size, coercion_record)

    def niDCPower_GetNextInterchangeWarning(self, vi, buffer_size, interchange_warning):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetNextInterchangeWarning_cfunc is None:
                self.niDCPower_GetNextInterchangeWarning_cfunc = self._library.niDCPower_GetNextInterchangeWarning
                self.niDCPower_GetNextInterchangeWarning_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niDCPower_GetNextInterchangeWarning_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_GetNextInterchangeWarning_cfunc(vi, buffer_size, interchange_warning)

    def niDCPower_GetSelfCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetSelfCalLastDateAndTime_cfunc is None:
                self.niDCPower_GetSelfCalLastDateAndTime_cfunc = self._library.niDCPower_GetSelfCalLastDateAndTime
                self.niDCPower_GetSelfCalLastDateAndTime_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt32_ctype), ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
                self.niDCPower_GetSelfCalLastDateAndTime_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_GetSelfCalLastDateAndTime_cfunc(vi, year, month, day, hour, minute)

    def niDCPower_GetSelfCalLastTemp(self, vi, temperature):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetSelfCalLastTemp_cfunc is None:
                self.niDCPower_GetSelfCalLastTemp_cfunc = self._library.niDCPower_GetSelfCalLastTemp
                self.niDCPower_GetSelfCalLastTemp_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niDCPower_GetSelfCalLastTemp_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_GetSelfCalLastTemp_cfunc(vi, temperature)

    def niDCPower_InitExtCal(self, resource_name, password, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_InitExtCal_cfunc is None:
                self.niDCPower_InitExtCal_cfunc = self._library.niDCPower_InitExtCal
                self.niDCPower_InitExtCal_cfunc.argtypes = [ViRsrc_ctype, ViChar_ctype, ctypes.POINTER(ViSession_ctype)]  # noqa: F405
                self.niDCPower_InitExtCal_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_InitExtCal_cfunc(resource_name, password, vi)

    def niDCPower_InitWithOptions(self, resource_name, id_query, reset_device, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_InitWithOptions_cfunc is None:
                self.niDCPower_InitWithOptions_cfunc = self._library.niDCPower_InitWithOptions
                self.niDCPower_InitWithOptions_cfunc.argtypes = [ViRsrc_ctype, ViBoolean_ctype, ViBoolean_ctype, ViChar_ctype, ctypes.POINTER(ViSession_ctype)]  # noqa: F405
                self.niDCPower_InitWithOptions_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_InitWithOptions_cfunc(resource_name, id_query, reset_device, option_string, vi)

    def niDCPower_InitializeWithChannels(self, resource_name, channels, reset, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_InitializeWithChannels_cfunc is None:
                self.niDCPower_InitializeWithChannels_cfunc = self._library.niDCPower_InitializeWithChannels
                self.niDCPower_InitializeWithChannels_cfunc.argtypes = [ViRsrc_ctype, ViChar_ctype, ViBoolean_ctype, ViChar_ctype, ctypes.POINTER(ViSession_ctype)]  # noqa: F405
                self.niDCPower_InitializeWithChannels_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_InitializeWithChannels_cfunc(resource_name, channels, reset, option_string, vi)

    def niDCPower_Initiate(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_Initiate_cfunc is None:
                self.niDCPower_Initiate_cfunc = self._library.niDCPower_Initiate
                self.niDCPower_Initiate_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_Initiate_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_Initiate_cfunc(vi)

    def niDCPower_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_LockSession_cfunc is None:
                self.niDCPower_LockSession_cfunc = self._library.niDCPower_LockSession
                self.niDCPower_LockSession_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViBoolean_ctype)]  # noqa: F405
                self.niDCPower_LockSession_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_LockSession_cfunc(vi, caller_has_lock)

    def niDCPower_Measure(self, vi, channel_name, measurement_type, measurement):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_Measure_cfunc is None:
                self.niDCPower_Measure_cfunc = self._library.niDCPower_Measure
                self.niDCPower_Measure_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViInt32_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niDCPower_Measure_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_Measure_cfunc(vi, channel_name, measurement_type, measurement)

    def niDCPower_MeasureMultiple(self, vi, channel_name, voltage_measurements, current_measurements):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_MeasureMultiple_cfunc is None:
                self.niDCPower_MeasureMultiple_cfunc = self._library.niDCPower_MeasureMultiple
                self.niDCPower_MeasureMultiple_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ctypes.POINTER(ViReal64_ctype), ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niDCPower_MeasureMultiple_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_MeasureMultiple_cfunc(vi, channel_name, voltage_measurements, current_measurements)

    def niDCPower_QueryInCompliance(self, vi, channel_name, in_compliance):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_QueryInCompliance_cfunc is None:
                self.niDCPower_QueryInCompliance_cfunc = self._library.niDCPower_QueryInCompliance
                self.niDCPower_QueryInCompliance_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ctypes.POINTER(ViBoolean_ctype)]  # noqa: F405
                self.niDCPower_QueryInCompliance_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_QueryInCompliance_cfunc(vi, channel_name, in_compliance)

    def niDCPower_QueryMaxCurrentLimit(self, vi, channel_name, voltage_level, max_current_limit):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_QueryMaxCurrentLimit_cfunc is None:
                self.niDCPower_QueryMaxCurrentLimit_cfunc = self._library.niDCPower_QueryMaxCurrentLimit
                self.niDCPower_QueryMaxCurrentLimit_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niDCPower_QueryMaxCurrentLimit_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_QueryMaxCurrentLimit_cfunc(vi, channel_name, voltage_level, max_current_limit)

    def niDCPower_QueryMaxVoltageLevel(self, vi, channel_name, current_limit, max_voltage_level):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_QueryMaxVoltageLevel_cfunc is None:
                self.niDCPower_QueryMaxVoltageLevel_cfunc = self._library.niDCPower_QueryMaxVoltageLevel
                self.niDCPower_QueryMaxVoltageLevel_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niDCPower_QueryMaxVoltageLevel_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_QueryMaxVoltageLevel_cfunc(vi, channel_name, current_limit, max_voltage_level)

    def niDCPower_QueryMinCurrentLimit(self, vi, channel_name, voltage_level, min_current_limit):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_QueryMinCurrentLimit_cfunc is None:
                self.niDCPower_QueryMinCurrentLimit_cfunc = self._library.niDCPower_QueryMinCurrentLimit
                self.niDCPower_QueryMinCurrentLimit_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niDCPower_QueryMinCurrentLimit_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_QueryMinCurrentLimit_cfunc(vi, channel_name, voltage_level, min_current_limit)

    def niDCPower_QueryOutputState(self, vi, channel_name, output_state, in_state):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_QueryOutputState_cfunc is None:
                self.niDCPower_QueryOutputState_cfunc = self._library.niDCPower_QueryOutputState
                self.niDCPower_QueryOutputState_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViInt32_ctype, ctypes.POINTER(ViBoolean_ctype)]  # noqa: F405
                self.niDCPower_QueryOutputState_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_QueryOutputState_cfunc(vi, channel_name, output_state, in_state)

    def niDCPower_ReadCurrentTemperature(self, vi, temperature):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ReadCurrentTemperature_cfunc is None:
                self.niDCPower_ReadCurrentTemperature_cfunc = self._library.niDCPower_ReadCurrentTemperature
                self.niDCPower_ReadCurrentTemperature_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViReal64_ctype)]  # noqa: F405
                self.niDCPower_ReadCurrentTemperature_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ReadCurrentTemperature_cfunc(vi, temperature)

    def niDCPower_ResetDevice(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ResetDevice_cfunc is None:
                self.niDCPower_ResetDevice_cfunc = self._library.niDCPower_ResetDevice
                self.niDCPower_ResetDevice_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_ResetDevice_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ResetDevice_cfunc(vi)

    def niDCPower_ResetInterchangeCheck(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ResetInterchangeCheck_cfunc is None:
                self.niDCPower_ResetInterchangeCheck_cfunc = self._library.niDCPower_ResetInterchangeCheck
                self.niDCPower_ResetInterchangeCheck_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_ResetInterchangeCheck_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ResetInterchangeCheck_cfunc(vi)

    def niDCPower_ResetWithDefaults(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_ResetWithDefaults_cfunc is None:
                self.niDCPower_ResetWithDefaults_cfunc = self._library.niDCPower_ResetWithDefaults
                self.niDCPower_ResetWithDefaults_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_ResetWithDefaults_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_ResetWithDefaults_cfunc(vi)

    def niDCPower_SendSoftwareEdgeTrigger(self, vi, trigger):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SendSoftwareEdgeTrigger_cfunc is None:
                self.niDCPower_SendSoftwareEdgeTrigger_cfunc = self._library.niDCPower_SendSoftwareEdgeTrigger
                self.niDCPower_SendSoftwareEdgeTrigger_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype]  # noqa: F405
                self.niDCPower_SendSoftwareEdgeTrigger_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_SendSoftwareEdgeTrigger_cfunc(vi, trigger)

    def niDCPower_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetAttributeViBoolean_cfunc is None:
                self.niDCPower_SetAttributeViBoolean_cfunc = self._library.niDCPower_SetAttributeViBoolean
                self.niDCPower_SetAttributeViBoolean_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViAttr_ctype, ViBoolean_ctype]  # noqa: F405
                self.niDCPower_SetAttributeViBoolean_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_SetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetAttributeViInt32_cfunc is None:
                self.niDCPower_SetAttributeViInt32_cfunc = self._library.niDCPower_SetAttributeViInt32
                self.niDCPower_SetAttributeViInt32_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViAttr_ctype, ViInt32_ctype]  # noqa: F405
                self.niDCPower_SetAttributeViInt32_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_SetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_SetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetAttributeViInt64_cfunc is None:
                self.niDCPower_SetAttributeViInt64_cfunc = self._library.niDCPower_SetAttributeViInt64
                self.niDCPower_SetAttributeViInt64_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViAttr_ctype, ViInt64_ctype]  # noqa: F405
                self.niDCPower_SetAttributeViInt64_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_SetAttributeViInt64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetAttributeViReal64_cfunc is None:
                self.niDCPower_SetAttributeViReal64_cfunc = self._library.niDCPower_SetAttributeViReal64
                self.niDCPower_SetAttributeViReal64_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViAttr_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_SetAttributeViReal64_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_SetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_SetAttributeViSession(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetAttributeViSession_cfunc is None:
                self.niDCPower_SetAttributeViSession_cfunc = self._library.niDCPower_SetAttributeViSession
                self.niDCPower_SetAttributeViSession_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViAttr_ctype, ViSession_ctype]  # noqa: F405
                self.niDCPower_SetAttributeViSession_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_SetAttributeViSession_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetAttributeViString_cfunc is None:
                self.niDCPower_SetAttributeViString_cfunc = self._library.niDCPower_SetAttributeViString
                self.niDCPower_SetAttributeViString_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViAttr_ctype, ViChar_ctype]  # noqa: F405
                self.niDCPower_SetAttributeViString_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_SetAttributeViString_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_SetCalUserDefinedInfo(self, vi, info):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetCalUserDefinedInfo_cfunc is None:
                self.niDCPower_SetCalUserDefinedInfo_cfunc = self._library.niDCPower_SetCalUserDefinedInfo
                self.niDCPower_SetCalUserDefinedInfo_cfunc.argtypes = [ViSession_ctype, ViChar_ctype]  # noqa: F405
                self.niDCPower_SetCalUserDefinedInfo_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_SetCalUserDefinedInfo_cfunc(vi, info)

    def niDCPower_SetSequence(self, vi, channel_name, values, source_delays, size):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetSequence_cfunc is None:
                self.niDCPower_SetSequence_cfunc = self._library.niDCPower_SetSequence
                self.niDCPower_SetSequence_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype, ViReal64_ctype, ViUInt32_ctype]  # noqa: F405
                self.niDCPower_SetSequence_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_SetSequence_cfunc(vi, channel_name, values, source_delays, size)

    def niDCPower_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_UnlockSession_cfunc is None:
                self.niDCPower_UnlockSession_cfunc = self._library.niDCPower_UnlockSession
                self.niDCPower_UnlockSession_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViBoolean_ctype)]  # noqa: F405
                self.niDCPower_UnlockSession_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_UnlockSession_cfunc(vi, caller_has_lock)

    def niDCPower_WaitForEvent(self, vi, event_id, timeout):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_WaitForEvent_cfunc is None:
                self.niDCPower_WaitForEvent_cfunc = self._library.niDCPower_WaitForEvent
                self.niDCPower_WaitForEvent_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViReal64_ctype]  # noqa: F405
                self.niDCPower_WaitForEvent_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_WaitForEvent_cfunc(vi, event_id, timeout)

    def niDCPower_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_close_cfunc is None:
                self.niDCPower_close_cfunc = self._library.niDCPower_close
                self.niDCPower_close_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_close_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_close_cfunc(vi)

    def niDCPower_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_error_message_cfunc is None:
                self.niDCPower_error_message_cfunc = self._library.niDCPower_error_message
                self.niDCPower_error_message_cfunc.argtypes = [ViSession_ctype, ViStatus_ctype, ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niDCPower_error_message_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_error_message_cfunc(vi, error_code, error_message)

    def niDCPower_init(self, resource_name, id_query, reset_device, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_init_cfunc is None:
                self.niDCPower_init_cfunc = self._library.niDCPower_init
                self.niDCPower_init_cfunc.argtypes = [ViRsrc_ctype, ViBoolean_ctype, ViBoolean_ctype, ctypes.POINTER(ViSession_ctype)]  # noqa: F405
                self.niDCPower_init_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_init_cfunc(resource_name, id_query, reset_device, vi)

    def niDCPower_reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_reset_cfunc is None:
                self.niDCPower_reset_cfunc = self._library.niDCPower_reset
                self.niDCPower_reset_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niDCPower_reset_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_reset_cfunc(vi)

    def niDCPower_revision_query(self, vi, instrument_driver_revision, firmware_revision):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_revision_query_cfunc is None:
                self.niDCPower_revision_query_cfunc = self._library.niDCPower_revision_query
                self.niDCPower_revision_query_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViChar_ctype), ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niDCPower_revision_query_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_revision_query_cfunc(vi, instrument_driver_revision, firmware_revision)

    def niDCPower_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_self_test_cfunc is None:
                self.niDCPower_self_test_cfunc = self._library.niDCPower_self_test
                self.niDCPower_self_test_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViInt16_ctype), ctypes.POINTER(ViChar_ctype)]  # noqa: F405
                self.niDCPower_self_test_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_self_test_cfunc(vi, self_test_result, self_test_message)
