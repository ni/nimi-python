# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import threading

from nisync._visatype import *  # noqa: F403,H303


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niSync_ClearClock_cfunc = None
        self.niSync_ClearFutureTimeEvents_cfunc = None
        self.niSync_ConfigureFpga_cfunc = None
        self.niSync_ConnectClkTerminals_cfunc = None
        self.niSync_ConnectSwTrigToTerminal_cfunc = None
        self.niSync_ConnectTrigTerminals_cfunc = None
        self.niSync_CreateClock_cfunc = None
        self.niSync_CreateFutureTimeEvent_cfunc = None
        self.niSync_DisableGpsTimestamping_cfunc = None
        self.niSync_DisableIrigTimestamping_cfunc = None
        self.niSync_DisableTimeStampTrigger_cfunc = None
        self.niSync_DisconnectClkTerminals_cfunc = None
        self.niSync_DisconnectSwTrigFromTerminal_cfunc = None
        self.niSync_DisconnectTrigTerminals_cfunc = None
        self.niSync_EnableGpsTimestamping_cfunc = None
        self.niSync_EnableIrigTimestamping_cfunc = None
        self.niSync_EnableTimeStampTrigger_cfunc = None
        self.niSync_EnableTimeStampTriggerWithDecimation_cfunc = None
        self.niSync_GetAttributeViBoolean_cfunc = None
        self.niSync_GetAttributeViInt32_cfunc = None
        self.niSync_GetAttributeViReal64_cfunc = None
        self.niSync_GetAttributeViString_cfunc = None
        self.niSync_GetLocation_cfunc = None
        self.niSync_GetTime_cfunc = None
        self.niSync_GetTimeReferenceNames_cfunc = None
        self.niSync_GetVelocity_cfunc = None
        self.niSync_MeasureFrequency_cfunc = None
        self.niSync_MeasureFrequencyEx_cfunc = None
        self.niSync_PersistConfig_cfunc = None
        self.niSync_ReadCurrentTemperature_cfunc = None
        self.niSync_ReadLastGpsTimestamp_cfunc = None
        self.niSync_ReadLastIrigTimestamp_cfunc = None
        self.niSync_ReadMultipleTriggerTimeStamp_cfunc = None
        self.niSync_ReadTriggerTimeStamp_cfunc = None
        self.niSync_ResetFrequency_cfunc = None
        self.niSync_SendSoftwareTrigger_cfunc = None
        self.niSync_SetAttributeViBoolean_cfunc = None
        self.niSync_SetAttributeViInt32_cfunc = None
        self.niSync_SetAttributeViReal64_cfunc = None
        self.niSync_SetAttributeViString_cfunc = None
        self.niSync_SetTime_cfunc = None
        self.niSync_SetTimeReference1588OrdinaryClock_cfunc = None
        self.niSync_SetTimeReferenceFreeRunning_cfunc = None
        self.niSync_SetTimeReferenceGps_cfunc = None
        self.niSync_SetTimeReferenceIrig_cfunc = None
        self.niSync_SetTimeReferencePps_cfunc = None
        self.niSync_Start1588_cfunc = None
        self.niSync_Stop1588_cfunc = None
        self.niSync_close_cfunc = None
        self.niSync_error_message_cfunc = None
        self.niSync_init_cfunc = None
        self.niSync_reset_cfunc = None
        self.niSync_revision_query_cfunc = None
        self.niSync_self_test_cfunc = None

    def niSync_ClearClock(self, vi, terminal):  # noqa: N802
        with self._func_lock:
            if self.niSync_ClearClock_cfunc is None:
                self.niSync_ClearClock_cfunc = self._library.niSync_ClearClock
                self.niSync_ClearClock_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSync_ClearClock_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ClearClock_cfunc(vi, terminal)

    def niSync_ClearFutureTimeEvents(self, vi, terminal):  # noqa: N802
        with self._func_lock:
            if self.niSync_ClearFutureTimeEvents_cfunc is None:
                self.niSync_ClearFutureTimeEvents_cfunc = self._library.niSync_ClearFutureTimeEvents
                self.niSync_ClearFutureTimeEvents_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSync_ClearFutureTimeEvents_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ClearFutureTimeEvents_cfunc(vi, terminal)

    def niSync_ConfigureFpga(self, vi, fpga_program_path):  # noqa: N802
        with self._func_lock:
            if self.niSync_ConfigureFpga_cfunc is None:
                self.niSync_ConfigureFpga_cfunc = self._library.niSync_ConfigureFpga
                self.niSync_ConfigureFpga_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSync_ConfigureFpga_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ConfigureFpga_cfunc(vi, fpga_program_path)

    def niSync_ConnectClkTerminals(self, vi, source_terminal, destination_terminal):  # noqa: N802
        with self._func_lock:
            if self.niSync_ConnectClkTerminals_cfunc is None:
                self.niSync_ConnectClkTerminals_cfunc = self._library.niSync_ConnectClkTerminals
                self.niSync_ConnectClkTerminals_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSync_ConnectClkTerminals_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ConnectClkTerminals_cfunc(vi, source_terminal, destination_terminal)

    def niSync_ConnectSwTrigToTerminal(self, vi, source_terminal, destination_terminal, synchronization_clock, invert, update_edge, delay):  # noqa: N802
        with self._func_lock:
            if self.niSync_ConnectSwTrigToTerminal_cfunc is None:
                self.niSync_ConnectSwTrigToTerminal_cfunc = self._library.niSync_ConnectSwTrigToTerminal
                self.niSync_ConnectSwTrigToTerminal_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViInt32, ViReal64]  # noqa: F405
                self.niSync_ConnectSwTrigToTerminal_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ConnectSwTrigToTerminal_cfunc(vi, source_terminal, destination_terminal, synchronization_clock, invert, update_edge, delay)

    def niSync_ConnectTrigTerminals(self, vi, source_terminal, destination_terminal, synchronization_clock, invert, update_edge):  # noqa: N802
        with self._func_lock:
            if self.niSync_ConnectTrigTerminals_cfunc is None:
                self.niSync_ConnectTrigTerminals_cfunc = self._library.niSync_ConnectTrigTerminals
                self.niSync_ConnectTrigTerminals_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViInt32]  # noqa: F405
                self.niSync_ConnectTrigTerminals_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ConnectTrigTerminals_cfunc(vi, source_terminal, destination_terminal, synchronization_clock, invert, update_edge)

    def niSync_CreateClock(self, vi, terminal, high_ticks, low_ticks, start_time_seconds, start_time_nanoseconds, start_time_fractional_nsecs, stop_time_seconds, stop_time_nanoseconds, stop_time_fractional_nsecs):  # noqa: N802
        with self._func_lock:
            if self.niSync_CreateClock_cfunc is None:
                self.niSync_CreateClock_cfunc = self._library.niSync_CreateClock
                self.niSync_CreateClock_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViUInt32, ViUInt32, ViUInt32, ViUInt32, ViUInt16, ViUInt32, ViUInt32, ViUInt16]  # noqa: F405
                self.niSync_CreateClock_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_CreateClock_cfunc(vi, terminal, high_ticks, low_ticks, start_time_seconds, start_time_nanoseconds, start_time_fractional_nsecs, stop_time_seconds, stop_time_nanoseconds, stop_time_fractional_nsecs)

    def niSync_CreateFutureTimeEvent(self, vi, terminal, output_level, time_seconds, time_nanoseconds, time_fractional_nanoseconds):  # noqa: N802
        with self._func_lock:
            if self.niSync_CreateFutureTimeEvent_cfunc is None:
                self.niSync_CreateFutureTimeEvent_cfunc = self._library.niSync_CreateFutureTimeEvent
                self.niSync_CreateFutureTimeEvent_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViUInt32, ViUInt32, ViUInt16]  # noqa: F405
                self.niSync_CreateFutureTimeEvent_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_CreateFutureTimeEvent_cfunc(vi, terminal, output_level, time_seconds, time_nanoseconds, time_fractional_nanoseconds)

    def niSync_DisableGpsTimestamping(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSync_DisableGpsTimestamping_cfunc is None:
                self.niSync_DisableGpsTimestamping_cfunc = self._library.niSync_DisableGpsTimestamping
                self.niSync_DisableGpsTimestamping_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_DisableGpsTimestamping_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_DisableGpsTimestamping_cfunc(vi)

    def niSync_DisableIrigTimestamping(self, vi, terminal_name):  # noqa: N802
        with self._func_lock:
            if self.niSync_DisableIrigTimestamping_cfunc is None:
                self.niSync_DisableIrigTimestamping_cfunc = self._library.niSync_DisableIrigTimestamping
                self.niSync_DisableIrigTimestamping_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSync_DisableIrigTimestamping_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_DisableIrigTimestamping_cfunc(vi, terminal_name)

    def niSync_DisableTimeStampTrigger(self, vi, terminal):  # noqa: N802
        with self._func_lock:
            if self.niSync_DisableTimeStampTrigger_cfunc is None:
                self.niSync_DisableTimeStampTrigger_cfunc = self._library.niSync_DisableTimeStampTrigger
                self.niSync_DisableTimeStampTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSync_DisableTimeStampTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_DisableTimeStampTrigger_cfunc(vi, terminal)

    def niSync_DisconnectClkTerminals(self, vi, source_terminal, destination_terminal):  # noqa: N802
        with self._func_lock:
            if self.niSync_DisconnectClkTerminals_cfunc is None:
                self.niSync_DisconnectClkTerminals_cfunc = self._library.niSync_DisconnectClkTerminals
                self.niSync_DisconnectClkTerminals_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSync_DisconnectClkTerminals_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_DisconnectClkTerminals_cfunc(vi, source_terminal, destination_terminal)

    def niSync_DisconnectSwTrigFromTerminal(self, vi, source_terminal, destination_terminal):  # noqa: N802
        with self._func_lock:
            if self.niSync_DisconnectSwTrigFromTerminal_cfunc is None:
                self.niSync_DisconnectSwTrigFromTerminal_cfunc = self._library.niSync_DisconnectSwTrigFromTerminal
                self.niSync_DisconnectSwTrigFromTerminal_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSync_DisconnectSwTrigFromTerminal_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_DisconnectSwTrigFromTerminal_cfunc(vi, source_terminal, destination_terminal)

    def niSync_DisconnectTrigTerminals(self, vi, source_terminal, destination_terminal):  # noqa: N802
        with self._func_lock:
            if self.niSync_DisconnectTrigTerminals_cfunc is None:
                self.niSync_DisconnectTrigTerminals_cfunc = self._library.niSync_DisconnectTrigTerminals
                self.niSync_DisconnectTrigTerminals_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSync_DisconnectTrigTerminals_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_DisconnectTrigTerminals_cfunc(vi, source_terminal, destination_terminal)

    def niSync_EnableGpsTimestamping(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSync_EnableGpsTimestamping_cfunc is None:
                self.niSync_EnableGpsTimestamping_cfunc = self._library.niSync_EnableGpsTimestamping
                self.niSync_EnableGpsTimestamping_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_EnableGpsTimestamping_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_EnableGpsTimestamping_cfunc(vi)

    def niSync_EnableIrigTimestamping(self, vi, irig_type, terminal_name):  # noqa: N802
        with self._func_lock:
            if self.niSync_EnableIrigTimestamping_cfunc is None:
                self.niSync_EnableIrigTimestamping_cfunc = self._library.niSync_EnableIrigTimestamping
                self.niSync_EnableIrigTimestamping_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSync_EnableIrigTimestamping_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_EnableIrigTimestamping_cfunc(vi, irig_type, terminal_name)

    def niSync_EnableTimeStampTrigger(self, vi, terminal, active_edge):  # noqa: N802
        with self._func_lock:
            if self.niSync_EnableTimeStampTrigger_cfunc is None:
                self.niSync_EnableTimeStampTrigger_cfunc = self._library.niSync_EnableTimeStampTrigger
                self.niSync_EnableTimeStampTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niSync_EnableTimeStampTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_EnableTimeStampTrigger_cfunc(vi, terminal, active_edge)

    def niSync_EnableTimeStampTriggerWithDecimation(self, vi, terminal, active_edge, decimation_count):  # noqa: N802
        with self._func_lock:
            if self.niSync_EnableTimeStampTriggerWithDecimation_cfunc is None:
                self.niSync_EnableTimeStampTriggerWithDecimation_cfunc = self._library.niSync_EnableTimeStampTriggerWithDecimation
                self.niSync_EnableTimeStampTriggerWithDecimation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViUInt32]  # noqa: F405
                self.niSync_EnableTimeStampTriggerWithDecimation_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_EnableTimeStampTriggerWithDecimation_cfunc(vi, terminal, active_edge, decimation_count)

    def niSync_GetAttributeViBoolean(self, vi, active_item, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSync_GetAttributeViBoolean_cfunc is None:
                self.niSync_GetAttributeViBoolean_cfunc = self._library.niSync_GetAttributeViBoolean
                self.niSync_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niSync_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetAttributeViBoolean_cfunc(vi, active_item, attribute_id, attribute_value)

    def niSync_GetAttributeViInt32(self, vi, active_item, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSync_GetAttributeViInt32_cfunc is None:
                self.niSync_GetAttributeViInt32_cfunc = self._library.niSync_GetAttributeViInt32
                self.niSync_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSync_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetAttributeViInt32_cfunc(vi, active_item, attribute_id, attribute_value)

    def niSync_GetAttributeViReal64(self, vi, active_item, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSync_GetAttributeViReal64_cfunc is None:
                self.niSync_GetAttributeViReal64_cfunc = self._library.niSync_GetAttributeViReal64
                self.niSync_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niSync_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetAttributeViReal64_cfunc(vi, active_item, attribute_id, attribute_value)

    def niSync_GetAttributeViString(self, vi, active_item, attribute_id, buffer_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSync_GetAttributeViString_cfunc is None:
                self.niSync_GetAttributeViString_cfunc = self._library.niSync_GetAttributeViString
                self.niSync_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSync_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetAttributeViString_cfunc(vi, active_item, attribute_id, buffer_size, attribute_value)

    def niSync_GetLocation(self, vi, latitude, longitude, altitude):  # noqa: N802
        with self._func_lock:
            if self.niSync_GetLocation_cfunc is None:
                self.niSync_GetLocation_cfunc = self._library.niSync_GetLocation
                self.niSync_GetLocation_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niSync_GetLocation_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetLocation_cfunc(vi, latitude, longitude, altitude)

    def niSync_GetTime(self, vi, time_seconds, time_nanoseconds, time_fractional_nanoseconds):  # noqa: N802
        with self._func_lock:
            if self.niSync_GetTime_cfunc is None:
                self.niSync_GetTime_cfunc = self._library.niSync_GetTime
                self.niSync_GetTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViUInt32), ctypes.POINTER(ViUInt32), ctypes.POINTER(ViUInt16)]  # noqa: F405
                self.niSync_GetTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetTime_cfunc(vi, time_seconds, time_nanoseconds, time_fractional_nanoseconds)

    def niSync_GetTimeReferenceNames(self, vi, buffer_size, time_reference_names):  # noqa: N802
        with self._func_lock:
            if self.niSync_GetTimeReferenceNames_cfunc is None:
                self.niSync_GetTimeReferenceNames_cfunc = self._library.niSync_GetTimeReferenceNames
                self.niSync_GetTimeReferenceNames_cfunc.argtypes = [ViSession, ViUInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSync_GetTimeReferenceNames_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetTimeReferenceNames_cfunc(vi, buffer_size, time_reference_names)

    def niSync_GetVelocity(self, vi, east_velocity, north_velocity, up_velocity):  # noqa: N802
        with self._func_lock:
            if self.niSync_GetVelocity_cfunc is None:
                self.niSync_GetVelocity_cfunc = self._library.niSync_GetVelocity
                self.niSync_GetVelocity_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niSync_GetVelocity_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetVelocity_cfunc(vi, east_velocity, north_velocity, up_velocity)

    def niSync_MeasureFrequency(self, vi, source_terminal, duration, actual_duration, measured_frequency, frequency_error):  # noqa: N802
        with self._func_lock:
            if self.niSync_MeasureFrequency_cfunc is None:
                self.niSync_MeasureFrequency_cfunc = self._library.niSync_MeasureFrequency
                self.niSync_MeasureFrequency_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niSync_MeasureFrequency_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_MeasureFrequency_cfunc(vi, source_terminal, duration, actual_duration, measured_frequency, frequency_error)

    def niSync_MeasureFrequencyEx(self, vi, source_terminal, duration, decimation_count, actual_duration, measured_frequency, frequency_error):  # noqa: N802
        with self._func_lock:
            if self.niSync_MeasureFrequencyEx_cfunc is None:
                self.niSync_MeasureFrequencyEx_cfunc = self._library.niSync_MeasureFrequencyEx
                self.niSync_MeasureFrequencyEx_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ViUInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niSync_MeasureFrequencyEx_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_MeasureFrequencyEx_cfunc(vi, source_terminal, duration, decimation_count, actual_duration, measured_frequency, frequency_error)

    def niSync_PersistConfig(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSync_PersistConfig_cfunc is None:
                self.niSync_PersistConfig_cfunc = self._library.niSync_PersistConfig
                self.niSync_PersistConfig_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_PersistConfig_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_PersistConfig_cfunc(vi)

    def niSync_ReadCurrentTemperature(self, vi, temperature):  # noqa: N802
        with self._func_lock:
            if self.niSync_ReadCurrentTemperature_cfunc is None:
                self.niSync_ReadCurrentTemperature_cfunc = self._library.niSync_ReadCurrentTemperature
                self.niSync_ReadCurrentTemperature_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niSync_ReadCurrentTemperature_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ReadCurrentTemperature_cfunc(vi, temperature)

    def niSync_ReadLastGpsTimestamp(self, vi, time_seconds, time_nanoseconds, time_fractional_nanoseconds, gps_seconds, gps_nanoseconds, gps_fractional_nanoseconds):  # noqa: N802
        with self._func_lock:
            if self.niSync_ReadLastGpsTimestamp_cfunc is None:
                self.niSync_ReadLastGpsTimestamp_cfunc = self._library.niSync_ReadLastGpsTimestamp
                self.niSync_ReadLastGpsTimestamp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViUInt32), ctypes.POINTER(ViUInt32), ctypes.POINTER(ViUInt16), ctypes.POINTER(ViUInt32), ctypes.POINTER(ViUInt32), ctypes.POINTER(ViUInt16)]  # noqa: F405
                self.niSync_ReadLastGpsTimestamp_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ReadLastGpsTimestamp_cfunc(vi, time_seconds, time_nanoseconds, time_fractional_nanoseconds, gps_seconds, gps_nanoseconds, gps_fractional_nanoseconds)

    def niSync_ReadLastIrigTimestamp(self, vi, time_seconds, time_nanoseconds, time_fractional_nanoseconds, irig_seconds, irig_nanoseconds, irig_fractional_nanoseconds):  # noqa: N802
        with self._func_lock:
            if self.niSync_ReadLastIrigTimestamp_cfunc is None:
                self.niSync_ReadLastIrigTimestamp_cfunc = self._library.niSync_ReadLastIrigTimestamp
                self.niSync_ReadLastIrigTimestamp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViUInt32), ctypes.POINTER(ViUInt32), ctypes.POINTER(ViUInt16), ctypes.POINTER(ViUInt32), ctypes.POINTER(ViUInt32), ctypes.POINTER(ViUInt16)]  # noqa: F405
                self.niSync_ReadLastIrigTimestamp_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ReadLastIrigTimestamp_cfunc(vi, time_seconds, time_nanoseconds, time_fractional_nanoseconds, irig_seconds, irig_nanoseconds, irig_fractional_nanoseconds)

    def niSync_ReadMultipleTriggerTimeStamp(self, vi, terminal, time_stamps_to_read, timeout, time_seconds, time_nanoseconds, time_fractional_nanoseconds, detected_edge_buffer, time_stamps_read):  # noqa: N802
        with self._func_lock:
            if self.niSync_ReadMultipleTriggerTimeStamp_cfunc is None:
                self.niSync_ReadMultipleTriggerTimeStamp_cfunc = self._library.niSync_ReadMultipleTriggerTimeStamp
                self.niSync_ReadMultipleTriggerTimeStamp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViUInt32, ViReal64, ctypes.POINTER(ViUInt32), ctypes.POINTER(ViUInt32), ctypes.POINTER(ViUInt16), ctypes.POINTER(ViInt32), ctypes.POINTER(ViUInt32)]  # noqa: F405
                self.niSync_ReadMultipleTriggerTimeStamp_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ReadMultipleTriggerTimeStamp_cfunc(vi, terminal, time_stamps_to_read, timeout, time_seconds, time_nanoseconds, time_fractional_nanoseconds, detected_edge_buffer, time_stamps_read)

    def niSync_ReadTriggerTimeStamp(self, vi, terminal, timeout, time_seconds, time_nanoseconds, time_fractional_nanoseconds, detected_edge):  # noqa: N802
        with self._func_lock:
            if self.niSync_ReadTriggerTimeStamp_cfunc is None:
                self.niSync_ReadTriggerTimeStamp_cfunc = self._library.niSync_ReadTriggerTimeStamp
                self.niSync_ReadTriggerTimeStamp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViReal64, ctypes.POINTER(ViUInt32), ctypes.POINTER(ViUInt32), ctypes.POINTER(ViUInt16), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSync_ReadTriggerTimeStamp_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ReadTriggerTimeStamp_cfunc(vi, terminal, timeout, time_seconds, time_nanoseconds, time_fractional_nanoseconds, detected_edge)

    def niSync_ResetFrequency(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSync_ResetFrequency_cfunc is None:
                self.niSync_ResetFrequency_cfunc = self._library.niSync_ResetFrequency
                self.niSync_ResetFrequency_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_ResetFrequency_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ResetFrequency_cfunc(vi)

    def niSync_SendSoftwareTrigger(self, vi, source_terminal):  # noqa: N802
        with self._func_lock:
            if self.niSync_SendSoftwareTrigger_cfunc is None:
                self.niSync_SendSoftwareTrigger_cfunc = self._library.niSync_SendSoftwareTrigger
                self.niSync_SendSoftwareTrigger_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSync_SendSoftwareTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SendSoftwareTrigger_cfunc(vi, source_terminal)

    def niSync_SetAttributeViBoolean(self, vi, active_item, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSync_SetAttributeViBoolean_cfunc is None:
                self.niSync_SetAttributeViBoolean_cfunc = self._library.niSync_SetAttributeViBoolean
                self.niSync_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niSync_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetAttributeViBoolean_cfunc(vi, active_item, attribute_id, attribute_value)

    def niSync_SetAttributeViInt32(self, vi, active_item, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSync_SetAttributeViInt32_cfunc is None:
                self.niSync_SetAttributeViInt32_cfunc = self._library.niSync_SetAttributeViInt32
                self.niSync_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niSync_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetAttributeViInt32_cfunc(vi, active_item, attribute_id, attribute_value)

    def niSync_SetAttributeViReal64(self, vi, active_item, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSync_SetAttributeViReal64_cfunc is None:
                self.niSync_SetAttributeViReal64_cfunc = self._library.niSync_SetAttributeViReal64
                self.niSync_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niSync_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetAttributeViReal64_cfunc(vi, active_item, attribute_id, attribute_value)

    def niSync_SetAttributeViString(self, vi, active_item, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSync_SetAttributeViString_cfunc is None:
                self.niSync_SetAttributeViString_cfunc = self._library.niSync_SetAttributeViString
                self.niSync_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSync_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetAttributeViString_cfunc(vi, active_item, attribute_id, attribute_value)

    def niSync_SetTime(self, vi, time_source, time_seconds, time_nanoseconds, time_fractional_nanoseconds):  # noqa: N802
        with self._func_lock:
            if self.niSync_SetTime_cfunc is None:
                self.niSync_SetTime_cfunc = self._library.niSync_SetTime
                self.niSync_SetTime_cfunc.argtypes = [ViSession, ViInt32, ViUInt32, ViUInt32, ViUInt16]  # noqa: F405
                self.niSync_SetTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetTime_cfunc(vi, time_source, time_seconds, time_nanoseconds, time_fractional_nanoseconds)

    def niSync_SetTimeReference1588OrdinaryClock(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSync_SetTimeReference1588OrdinaryClock_cfunc is None:
                self.niSync_SetTimeReference1588OrdinaryClock_cfunc = self._library.niSync_SetTimeReference1588OrdinaryClock
                self.niSync_SetTimeReference1588OrdinaryClock_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_SetTimeReference1588OrdinaryClock_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetTimeReference1588OrdinaryClock_cfunc(vi)

    def niSync_SetTimeReferenceFreeRunning(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSync_SetTimeReferenceFreeRunning_cfunc is None:
                self.niSync_SetTimeReferenceFreeRunning_cfunc = self._library.niSync_SetTimeReferenceFreeRunning
                self.niSync_SetTimeReferenceFreeRunning_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_SetTimeReferenceFreeRunning_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetTimeReferenceFreeRunning_cfunc(vi)

    def niSync_SetTimeReferenceGps(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSync_SetTimeReferenceGps_cfunc is None:
                self.niSync_SetTimeReferenceGps_cfunc = self._library.niSync_SetTimeReferenceGps
                self.niSync_SetTimeReferenceGps_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_SetTimeReferenceGps_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetTimeReferenceGps_cfunc(vi)

    def niSync_SetTimeReferenceIrig(self, vi, irig_type, terminal_name):  # noqa: N802
        with self._func_lock:
            if self.niSync_SetTimeReferenceIrig_cfunc is None:
                self.niSync_SetTimeReferenceIrig_cfunc = self._library.niSync_SetTimeReferenceIrig
                self.niSync_SetTimeReferenceIrig_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSync_SetTimeReferenceIrig_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetTimeReferenceIrig_cfunc(vi, irig_type, terminal_name)

    def niSync_SetTimeReferencePps(self, vi, terminal_name, use_manual_time, initial_time_seconds, initial_nanoseconds, initial_fractional_nanoseconds):  # noqa: N802
        with self._func_lock:
            if self.niSync_SetTimeReferencePps_cfunc is None:
                self.niSync_SetTimeReferencePps_cfunc = self._library.niSync_SetTimeReferencePps
                self.niSync_SetTimeReferencePps_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViBoolean, ViUInt32, ViUInt32, ViUInt16]  # noqa: F405
                self.niSync_SetTimeReferencePps_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetTimeReferencePps_cfunc(vi, terminal_name, use_manual_time, initial_time_seconds, initial_nanoseconds, initial_fractional_nanoseconds)

    def niSync_Start1588(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSync_Start1588_cfunc is None:
                self.niSync_Start1588_cfunc = self._library.niSync_Start1588
                self.niSync_Start1588_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_Start1588_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_Start1588_cfunc(vi)

    def niSync_Stop1588(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSync_Stop1588_cfunc is None:
                self.niSync_Stop1588_cfunc = self._library.niSync_Stop1588
                self.niSync_Stop1588_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_Stop1588_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_Stop1588_cfunc(vi)

    def niSync_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSync_close_cfunc is None:
                self.niSync_close_cfunc = self._library.niSync_close
                self.niSync_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_close_cfunc(vi)

    def niSync_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niSync_error_message_cfunc is None:
                self.niSync_error_message_cfunc = self._library.niSync_error_message
                self.niSync_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSync_error_message_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_error_message_cfunc(vi, error_code, error_message)

    def niSync_init(self, resource_name, id_query, reset_device, vi):  # noqa: N802
        with self._func_lock:
            if self.niSync_init_cfunc is None:
                self.niSync_init_cfunc = self._library.niSync_init
                self.niSync_init_cfunc.argtypes = [ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViSession)]  # noqa: F405
                self.niSync_init_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_init_cfunc(resource_name, id_query, reset_device, vi)

    def niSync_reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSync_reset_cfunc is None:
                self.niSync_reset_cfunc = self._library.niSync_reset
                self.niSync_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_reset_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_reset_cfunc(vi)

    def niSync_revision_query(self, vi, instrument_driver_revision, firmware_revision):  # noqa: N802
        with self._func_lock:
            if self.niSync_revision_query_cfunc is None:
                self.niSync_revision_query_cfunc = self._library.niSync_revision_query
                self.niSync_revision_query_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSync_revision_query_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_revision_query_cfunc(vi, instrument_driver_revision, firmware_revision)

    def niSync_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niSync_self_test_cfunc is None:
                self.niSync_self_test_cfunc = self._library.niSync_self_test
                self.niSync_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSync_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_self_test_cfunc(vi, self_test_result, self_test_message)
