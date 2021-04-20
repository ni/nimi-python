# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import niswitch.errors as errors
import threading

from niswitch._visatype import *  # noqa: F403,H303


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niSwitch_AbortScan_cfunc = None
        self.niSwitch_CanConnect_cfunc = None
        self.niSwitch_Commit_cfunc = None
        self.niSwitch_Connect_cfunc = None
        self.niSwitch_ConnectMultiple_cfunc = None
        self.niSwitch_Disable_cfunc = None
        self.niSwitch_Disconnect_cfunc = None
        self.niSwitch_DisconnectAll_cfunc = None
        self.niSwitch_DisconnectMultiple_cfunc = None
        self.niSwitch_GetAttributeViBoolean_cfunc = None
        self.niSwitch_GetAttributeViInt32_cfunc = None
        self.niSwitch_GetAttributeViReal64_cfunc = None
        self.niSwitch_GetAttributeViString_cfunc = None
        self.niSwitch_GetChannelName_cfunc = None
        self.niSwitch_GetError_cfunc = None
        self.niSwitch_GetPath_cfunc = None
        self.niSwitch_GetRelayCount_cfunc = None
        self.niSwitch_GetRelayName_cfunc = None
        self.niSwitch_GetRelayPosition_cfunc = None
        self.niSwitch_InitWithTopology_cfunc = None
        self.niSwitch_InitiateScan_cfunc = None
        self.niSwitch_LockSession_cfunc = None
        self.niSwitch_RelayControl_cfunc = None
        self.niSwitch_ResetWithDefaults_cfunc = None
        self.niSwitch_RouteScanAdvancedOutput_cfunc = None
        self.niSwitch_RouteTriggerInput_cfunc = None
        self.niSwitch_SendSoftwareTrigger_cfunc = None
        self.niSwitch_SetAttributeViBoolean_cfunc = None
        self.niSwitch_SetAttributeViInt32_cfunc = None
        self.niSwitch_SetAttributeViReal64_cfunc = None
        self.niSwitch_SetAttributeViString_cfunc = None
        self.niSwitch_SetPath_cfunc = None
        self.niSwitch_UnlockSession_cfunc = None
        self.niSwitch_WaitForDebounce_cfunc = None
        self.niSwitch_WaitForScanComplete_cfunc = None
        self.niSwitch_close_cfunc = None
        self.niSwitch_error_message_cfunc = None
        self.niSwitch_reset_cfunc = None
        self.niSwitch_self_test_cfunc = None

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

    def niSwitch_AbortScan(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_AbortScan_cfunc is None:
                self.niSwitch_AbortScan_cfunc = self._get_library_function('niSwitch_AbortScan')
                self.niSwitch_AbortScan_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_AbortScan_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_AbortScan_cfunc(vi)

    def niSwitch_CanConnect(self, vi, channel1, channel2, path_capability):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_CanConnect_cfunc is None:
                self.niSwitch_CanConnect_cfunc = self._get_library_function('niSwitch_CanConnect')
                self.niSwitch_CanConnect_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSwitch_CanConnect_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_CanConnect_cfunc(vi, channel1, channel2, path_capability)

    def niSwitch_Commit(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_Commit_cfunc is None:
                self.niSwitch_Commit_cfunc = self._get_library_function('niSwitch_Commit')
                self.niSwitch_Commit_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_Commit_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_Commit_cfunc(vi)

    def niSwitch_Connect(self, vi, channel1, channel2):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_Connect_cfunc is None:
                self.niSwitch_Connect_cfunc = self._get_library_function('niSwitch_Connect')
                self.niSwitch_Connect_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_Connect_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_Connect_cfunc(vi, channel1, channel2)

    def niSwitch_ConnectMultiple(self, vi, connection_list):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_ConnectMultiple_cfunc is None:
                self.niSwitch_ConnectMultiple_cfunc = self._get_library_function('niSwitch_ConnectMultiple')
                self.niSwitch_ConnectMultiple_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_ConnectMultiple_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_ConnectMultiple_cfunc(vi, connection_list)

    def niSwitch_Disable(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_Disable_cfunc is None:
                self.niSwitch_Disable_cfunc = self._get_library_function('niSwitch_Disable')
                self.niSwitch_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_Disable_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_Disable_cfunc(vi)

    def niSwitch_Disconnect(self, vi, channel1, channel2):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_Disconnect_cfunc is None:
                self.niSwitch_Disconnect_cfunc = self._get_library_function('niSwitch_Disconnect')
                self.niSwitch_Disconnect_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_Disconnect_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_Disconnect_cfunc(vi, channel1, channel2)

    def niSwitch_DisconnectAll(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_DisconnectAll_cfunc is None:
                self.niSwitch_DisconnectAll_cfunc = self._get_library_function('niSwitch_DisconnectAll')
                self.niSwitch_DisconnectAll_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_DisconnectAll_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_DisconnectAll_cfunc(vi)

    def niSwitch_DisconnectMultiple(self, vi, disconnection_list):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_DisconnectMultiple_cfunc is None:
                self.niSwitch_DisconnectMultiple_cfunc = self._get_library_function('niSwitch_DisconnectMultiple')
                self.niSwitch_DisconnectMultiple_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_DisconnectMultiple_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_DisconnectMultiple_cfunc(vi, disconnection_list)

    def niSwitch_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetAttributeViBoolean_cfunc is None:
                self.niSwitch_GetAttributeViBoolean_cfunc = self._get_library_function('niSwitch_GetAttributeViBoolean')
                self.niSwitch_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niSwitch_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niSwitch_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetAttributeViInt32_cfunc is None:
                self.niSwitch_GetAttributeViInt32_cfunc = self._get_library_function('niSwitch_GetAttributeViInt32')
                self.niSwitch_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSwitch_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niSwitch_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetAttributeViReal64_cfunc is None:
                self.niSwitch_GetAttributeViReal64_cfunc = self._get_library_function('niSwitch_GetAttributeViReal64')
                self.niSwitch_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niSwitch_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niSwitch_GetAttributeViString(self, vi, channel_name, attribute_id, array_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetAttributeViString_cfunc is None:
                self.niSwitch_GetAttributeViString_cfunc = self._get_library_function('niSwitch_GetAttributeViString')
                self.niSwitch_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetAttributeViString_cfunc(vi, channel_name, attribute_id, array_size, attribute_value)

    def niSwitch_GetChannelName(self, vi, index, buffer_size, channel_name_buffer):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetChannelName_cfunc is None:
                self.niSwitch_GetChannelName_cfunc = self._get_library_function('niSwitch_GetChannelName')
                self.niSwitch_GetChannelName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_GetChannelName_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetChannelName_cfunc(vi, index, buffer_size, channel_name_buffer)

    def niSwitch_GetError(self, vi, code, buffer_size, description):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetError_cfunc is None:
                self.niSwitch_GetError_cfunc = self._get_library_function('niSwitch_GetError')
                self.niSwitch_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetError_cfunc(vi, code, buffer_size, description)

    def niSwitch_GetPath(self, vi, channel1, channel2, buffer_size, path):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetPath_cfunc is None:
                self.niSwitch_GetPath_cfunc = self._get_library_function('niSwitch_GetPath')
                self.niSwitch_GetPath_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_GetPath_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetPath_cfunc(vi, channel1, channel2, buffer_size, path)

    def niSwitch_GetRelayCount(self, vi, relay_name, relay_count):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetRelayCount_cfunc is None:
                self.niSwitch_GetRelayCount_cfunc = self._get_library_function('niSwitch_GetRelayCount')
                self.niSwitch_GetRelayCount_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSwitch_GetRelayCount_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetRelayCount_cfunc(vi, relay_name, relay_count)

    def niSwitch_GetRelayName(self, vi, index, relay_name_buffer_size, relay_name_buffer):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetRelayName_cfunc is None:
                self.niSwitch_GetRelayName_cfunc = self._get_library_function('niSwitch_GetRelayName')
                self.niSwitch_GetRelayName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_GetRelayName_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetRelayName_cfunc(vi, index, relay_name_buffer_size, relay_name_buffer)

    def niSwitch_GetRelayPosition(self, vi, relay_name, relay_position):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetRelayPosition_cfunc is None:
                self.niSwitch_GetRelayPosition_cfunc = self._get_library_function('niSwitch_GetRelayPosition')
                self.niSwitch_GetRelayPosition_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSwitch_GetRelayPosition_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetRelayPosition_cfunc(vi, relay_name, relay_position)

    def niSwitch_InitWithTopology(self, resource_name, topology, simulate, reset_device, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_InitWithTopology_cfunc is None:
                self.niSwitch_InitWithTopology_cfunc = self._get_library_function('niSwitch_InitWithTopology')
                self.niSwitch_InitWithTopology_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViSession)]  # noqa: F405
                self.niSwitch_InitWithTopology_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_InitWithTopology_cfunc(resource_name, topology, simulate, reset_device, vi)

    def niSwitch_InitiateScan(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_InitiateScan_cfunc is None:
                self.niSwitch_InitiateScan_cfunc = self._get_library_function('niSwitch_InitiateScan')
                self.niSwitch_InitiateScan_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_InitiateScan_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_InitiateScan_cfunc(vi)

    def niSwitch_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_LockSession_cfunc is None:
                self.niSwitch_LockSession_cfunc = self._get_library_function('niSwitch_LockSession')
                self.niSwitch_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niSwitch_LockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_LockSession_cfunc(vi, caller_has_lock)

    def niSwitch_RelayControl(self, vi, relay_name, relay_action):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_RelayControl_cfunc is None:
                self.niSwitch_RelayControl_cfunc = self._get_library_function('niSwitch_RelayControl')
                self.niSwitch_RelayControl_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niSwitch_RelayControl_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_RelayControl_cfunc(vi, relay_name, relay_action)

    def niSwitch_ResetWithDefaults(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_ResetWithDefaults_cfunc is None:
                self.niSwitch_ResetWithDefaults_cfunc = self._get_library_function('niSwitch_ResetWithDefaults')
                self.niSwitch_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_ResetWithDefaults_cfunc(vi)

    def niSwitch_RouteScanAdvancedOutput(self, vi, scan_advanced_output_connector, scan_advanced_output_bus_line, invert):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_RouteScanAdvancedOutput_cfunc is None:
                self.niSwitch_RouteScanAdvancedOutput_cfunc = self._get_library_function('niSwitch_RouteScanAdvancedOutput')
                self.niSwitch_RouteScanAdvancedOutput_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ViBoolean]  # noqa: F405
                self.niSwitch_RouteScanAdvancedOutput_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_RouteScanAdvancedOutput_cfunc(vi, scan_advanced_output_connector, scan_advanced_output_bus_line, invert)

    def niSwitch_RouteTriggerInput(self, vi, trigger_input_connector, trigger_input_bus_line, invert):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_RouteTriggerInput_cfunc is None:
                self.niSwitch_RouteTriggerInput_cfunc = self._get_library_function('niSwitch_RouteTriggerInput')
                self.niSwitch_RouteTriggerInput_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ViBoolean]  # noqa: F405
                self.niSwitch_RouteTriggerInput_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_RouteTriggerInput_cfunc(vi, trigger_input_connector, trigger_input_bus_line, invert)

    def niSwitch_SendSoftwareTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_SendSoftwareTrigger_cfunc is None:
                self.niSwitch_SendSoftwareTrigger_cfunc = self._get_library_function('niSwitch_SendSoftwareTrigger')
                self.niSwitch_SendSoftwareTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_SendSoftwareTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_SendSoftwareTrigger_cfunc(vi)

    def niSwitch_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_SetAttributeViBoolean_cfunc is None:
                self.niSwitch_SetAttributeViBoolean_cfunc = self._get_library_function('niSwitch_SetAttributeViBoolean')
                self.niSwitch_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niSwitch_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_SetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niSwitch_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_SetAttributeViInt32_cfunc is None:
                self.niSwitch_SetAttributeViInt32_cfunc = self._get_library_function('niSwitch_SetAttributeViInt32')
                self.niSwitch_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niSwitch_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_SetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niSwitch_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_SetAttributeViReal64_cfunc is None:
                self.niSwitch_SetAttributeViReal64_cfunc = self._get_library_function('niSwitch_SetAttributeViReal64')
                self.niSwitch_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niSwitch_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_SetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niSwitch_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_SetAttributeViString_cfunc is None:
                self.niSwitch_SetAttributeViString_cfunc = self._get_library_function('niSwitch_SetAttributeViString')
                self.niSwitch_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_SetAttributeViString_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niSwitch_SetPath(self, vi, path_list):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_SetPath_cfunc is None:
                self.niSwitch_SetPath_cfunc = self._get_library_function('niSwitch_SetPath')
                self.niSwitch_SetPath_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_SetPath_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_SetPath_cfunc(vi, path_list)

    def niSwitch_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_UnlockSession_cfunc is None:
                self.niSwitch_UnlockSession_cfunc = self._get_library_function('niSwitch_UnlockSession')
                self.niSwitch_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niSwitch_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_UnlockSession_cfunc(vi, caller_has_lock)

    def niSwitch_WaitForDebounce(self, vi, maximum_time_ms):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_WaitForDebounce_cfunc is None:
                self.niSwitch_WaitForDebounce_cfunc = self._get_library_function('niSwitch_WaitForDebounce')
                self.niSwitch_WaitForDebounce_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niSwitch_WaitForDebounce_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_WaitForDebounce_cfunc(vi, maximum_time_ms)

    def niSwitch_WaitForScanComplete(self, vi, maximum_time_ms):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_WaitForScanComplete_cfunc is None:
                self.niSwitch_WaitForScanComplete_cfunc = self._get_library_function('niSwitch_WaitForScanComplete')
                self.niSwitch_WaitForScanComplete_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niSwitch_WaitForScanComplete_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_WaitForScanComplete_cfunc(vi, maximum_time_ms)

    def niSwitch_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_close_cfunc is None:
                self.niSwitch_close_cfunc = self._get_library_function('niSwitch_close')
                self.niSwitch_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_close_cfunc(vi)

    def niSwitch_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_error_message_cfunc is None:
                self.niSwitch_error_message_cfunc = self._get_library_function('niSwitch_error_message')
                self.niSwitch_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_error_message_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_error_message_cfunc(vi, error_code, error_message)

    def niSwitch_reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_reset_cfunc is None:
                self.niSwitch_reset_cfunc = self._get_library_function('niSwitch_reset')
                self.niSwitch_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_reset_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_reset_cfunc(vi)

    def niSwitch_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_self_test_cfunc is None:
                self.niSwitch_self_test_cfunc = self._get_library_function('niSwitch_self_test')
                self.niSwitch_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_self_test_cfunc(vi, self_test_result, self_test_message)
