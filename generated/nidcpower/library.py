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
        self.niDCPower_Commit_cfunc = None
        self.niDCPower_ConfigureApertureTime_cfunc = None
        self.niDCPower_ConfigureDigitalEdgeMeasureTrigger_cfunc = None
        self.niDCPower_ConfigureDigitalEdgePulseTrigger_cfunc = None
        self.niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger_cfunc = None
        self.niDCPower_ConfigureDigitalEdgeSourceTrigger_cfunc = None
        self.niDCPower_ConfigureDigitalEdgeStartTrigger_cfunc = None
        self.niDCPower_CreateAdvancedSequence_cfunc = None
        self.niDCPower_CreateAdvancedSequenceStep_cfunc = None
        self.niDCPower_DeleteAdvancedSequence_cfunc = None
        self.niDCPower_Disable_cfunc = None
        self.niDCPower_ExportSignal_cfunc = None
        self.niDCPower_FetchMultiple_cfunc = None
        self.niDCPower_GetAttributeViBoolean_cfunc = None
        self.niDCPower_GetAttributeViInt32_cfunc = None
        self.niDCPower_GetAttributeViInt64_cfunc = None
        self.niDCPower_GetAttributeViReal64_cfunc = None
        self.niDCPower_GetAttributeViString_cfunc = None
        self.niDCPower_GetError_cfunc = None
        self.niDCPower_GetSelfCalLastDateAndTime_cfunc = None
        self.niDCPower_GetSelfCalLastTemp_cfunc = None
        self.niDCPower_InitializeWithChannels_cfunc = None
        self.niDCPower_Initiate_cfunc = None
        self.niDCPower_Measure_cfunc = None
        self.niDCPower_MeasureMultiple_cfunc = None
        self.niDCPower_QueryInCompliance_cfunc = None
        self.niDCPower_QueryMaxCurrentLimit_cfunc = None
        self.niDCPower_QueryMaxVoltageLevel_cfunc = None
        self.niDCPower_QueryMinCurrentLimit_cfunc = None
        self.niDCPower_QueryOutputState_cfunc = None
        self.niDCPower_ReadCurrentTemperature_cfunc = None
        self.niDCPower_ResetDevice_cfunc = None
        self.niDCPower_ResetWithDefaults_cfunc = None
        self.niDCPower_SendSoftwareEdgeTrigger_cfunc = None
        self.niDCPower_SetAttributeViBoolean_cfunc = None
        self.niDCPower_SetAttributeViInt32_cfunc = None
        self.niDCPower_SetAttributeViInt64_cfunc = None
        self.niDCPower_SetAttributeViReal64_cfunc = None
        self.niDCPower_SetAttributeViString_cfunc = None
        self.niDCPower_SetSequence_cfunc = None
        self.niDCPower_WaitForEvent_cfunc = None
        self.niDCPower_close_cfunc = None
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

    def niDCPower_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetAttributeViString_cfunc is None:
                self.niDCPower_GetAttributeViString_cfunc = self._library.niDCPower_GetAttributeViString
                self.niDCPower_GetAttributeViString_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViAttr_ctype, ViInt32_ctype, ViString_ctype]  # noqa: F405
                self.niDCPower_GetAttributeViString_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_GetAttributeViString_cfunc(vi, channel_name, attribute_id, buffer_size, attribute_value)

    def niDCPower_GetError(self, vi, code, buffer_size, description):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_GetError_cfunc is None:
                self.niDCPower_GetError_cfunc = self._library.niDCPower_GetError
                self.niDCPower_GetError_cfunc.argtypes = [ViSession_ctype, ctypes.POINTER(ViStatus_ctype), ViInt32_ctype, ViString_ctype]  # noqa: F405
                self.niDCPower_GetError_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_GetError_cfunc(vi, code, buffer_size, description)

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

    def niDCPower_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetAttributeViString_cfunc is None:
                self.niDCPower_SetAttributeViString_cfunc = self._library.niDCPower_SetAttributeViString
                self.niDCPower_SetAttributeViString_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViAttr_ctype, ViString_ctype]  # noqa: F405
                self.niDCPower_SetAttributeViString_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_SetAttributeViString_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niDCPower_SetSequence(self, vi, channel_name, values, source_delays, size):  # noqa: N802
        with self._func_lock:
            if self.niDCPower_SetSequence_cfunc is None:
                self.niDCPower_SetSequence_cfunc = self._library.niDCPower_SetSequence
                self.niDCPower_SetSequence_cfunc.argtypes = [ViSession_ctype, ViChar_ctype, ViReal64_ctype, ViReal64_ctype, ViUInt32_ctype]  # noqa: F405
                self.niDCPower_SetSequence_cfunc.restype = nidcpower.python_types.ViStatus
        return self.niDCPower_SetSequence_cfunc(vi, channel_name, values, source_delays, size)

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
