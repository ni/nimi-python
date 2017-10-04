# This file was generated

import ctypes
import threading

from niswitch.visatype import *  # noqa: F403,H303


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, library_name, library_type):
        self._func_lock = threading.Lock()
        # We cache the cfunc object from the ctypes.CDLL object
        self.niSwitch_AbortScan_cfunc = None
        self.niSwitch_CanConnect_cfunc = None
        self.niSwitch_Commit_cfunc = None
        self.niSwitch_ConfigureScanList_cfunc = None
        self.niSwitch_ConfigureScanTrigger_cfunc = None
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
        self.niSwitch_IsDebounced_cfunc = None
        self.niSwitch_IsScanning_cfunc = None
        self.niSwitch_RelayControl_cfunc = None
        self.niSwitch_ResetWithDefaults_cfunc = None
        self.niSwitch_RouteScanAdvancedOutput_cfunc = None
        self.niSwitch_RouteTriggerInput_cfunc = None
        self.niSwitch_SendSoftwareTrigger_cfunc = None
        self.niSwitch_SetAttributeViBoolean_cfunc = None
        self.niSwitch_SetAttributeViInt32_cfunc = None
        self.niSwitch_SetAttributeViReal64_cfunc = None
        self.niSwitch_SetAttributeViString_cfunc = None
        self.niSwitch_SetContinuousScan_cfunc = None
        self.niSwitch_SetPath_cfunc = None
        self.niSwitch_WaitForDebounce_cfunc = None
        self.niSwitch_WaitForScanComplete_cfunc = None
        self.niSwitch_close_cfunc = None
        self.niSwitch_error_message_cfunc = None
        self.niSwitch_reset_cfunc = None
        self.niSwitch_revision_query_cfunc = None
        self.niSwitch_self_test_cfunc = None

        if library_type == 'windll':
            self._library = ctypes.WinDLL(library_name)
        else:  # pragma: no cover
            assert library_type == 'cdll'
            self._library = ctypes.CDLL(library_name)

    def niSwitch_AbortScan(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_AbortScan_cfunc is None:
                self.niSwitch_AbortScan_cfunc = self._library.niSwitch_AbortScan
                self.niSwitch_AbortScan_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_AbortScan_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_AbortScan_cfunc(vi).value

    def niSwitch_CanConnect(self, vi, channel1, channel2, path_capability):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_CanConnect_cfunc is None:
                self.niSwitch_CanConnect_cfunc = self._library.niSwitch_CanConnect
                self.niSwitch_CanConnect_cfunc.argtypes = [ViSession, ViConstString, ViConstString, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSwitch_CanConnect_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_CanConnect_cfunc(vi, channel1, channel2, path_capability).value

    def niSwitch_Commit(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_Commit_cfunc is None:
                self.niSwitch_Commit_cfunc = self._library.niSwitch_Commit
                self.niSwitch_Commit_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_Commit_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_Commit_cfunc(vi).value

    def niSwitch_ConfigureScanList(self, vi, scanlist, scan_mode):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_ConfigureScanList_cfunc is None:
                self.niSwitch_ConfigureScanList_cfunc = self._library.niSwitch_ConfigureScanList
                self.niSwitch_ConfigureScanList_cfunc.argtypes = [ViSession, ViConstString, ViInt32]  # noqa: F405
                self.niSwitch_ConfigureScanList_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_ConfigureScanList_cfunc(vi, scanlist, scan_mode).value

    def niSwitch_ConfigureScanTrigger(self, vi, scan_delay, trigger_input, scan_advanced_output):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_ConfigureScanTrigger_cfunc is None:
                self.niSwitch_ConfigureScanTrigger_cfunc = self._library.niSwitch_ConfigureScanTrigger
                self.niSwitch_ConfigureScanTrigger_cfunc.argtypes = [ViSession, ViReal64, ViInt32, ViInt32]  # noqa: F405
                self.niSwitch_ConfigureScanTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_ConfigureScanTrigger_cfunc(vi, scan_delay, trigger_input, scan_advanced_output).value

    def niSwitch_Connect(self, vi, channel1, channel2):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_Connect_cfunc is None:
                self.niSwitch_Connect_cfunc = self._library.niSwitch_Connect
                self.niSwitch_Connect_cfunc.argtypes = [ViSession, ViConstString, ViConstString]  # noqa: F405
                self.niSwitch_Connect_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_Connect_cfunc(vi, channel1, channel2).value

    def niSwitch_ConnectMultiple(self, vi, connection_list):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_ConnectMultiple_cfunc is None:
                self.niSwitch_ConnectMultiple_cfunc = self._library.niSwitch_ConnectMultiple
                self.niSwitch_ConnectMultiple_cfunc.argtypes = [ViSession, ViConstString]  # noqa: F405
                self.niSwitch_ConnectMultiple_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_ConnectMultiple_cfunc(vi, connection_list).value

    def niSwitch_Disable(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_Disable_cfunc is None:
                self.niSwitch_Disable_cfunc = self._library.niSwitch_Disable
                self.niSwitch_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_Disable_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_Disable_cfunc(vi).value

    def niSwitch_Disconnect(self, vi, channel1, channel2):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_Disconnect_cfunc is None:
                self.niSwitch_Disconnect_cfunc = self._library.niSwitch_Disconnect
                self.niSwitch_Disconnect_cfunc.argtypes = [ViSession, ViConstString, ViConstString]  # noqa: F405
                self.niSwitch_Disconnect_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_Disconnect_cfunc(vi, channel1, channel2).value

    def niSwitch_DisconnectAll(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_DisconnectAll_cfunc is None:
                self.niSwitch_DisconnectAll_cfunc = self._library.niSwitch_DisconnectAll
                self.niSwitch_DisconnectAll_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_DisconnectAll_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_DisconnectAll_cfunc(vi).value

    def niSwitch_DisconnectMultiple(self, vi, disconnection_list):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_DisconnectMultiple_cfunc is None:
                self.niSwitch_DisconnectMultiple_cfunc = self._library.niSwitch_DisconnectMultiple
                self.niSwitch_DisconnectMultiple_cfunc.argtypes = [ViSession, ViConstString]  # noqa: F405
                self.niSwitch_DisconnectMultiple_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_DisconnectMultiple_cfunc(vi, disconnection_list).value

    def niSwitch_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetAttributeViBoolean_cfunc is None:
                self.niSwitch_GetAttributeViBoolean_cfunc = self._library.niSwitch_GetAttributeViBoolean
                self.niSwitch_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ViConstString, ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niSwitch_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value).value

    def niSwitch_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetAttributeViInt32_cfunc is None:
                self.niSwitch_GetAttributeViInt32_cfunc = self._library.niSwitch_GetAttributeViInt32
                self.niSwitch_GetAttributeViInt32_cfunc.argtypes = [ViSession, ViConstString, ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSwitch_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value).value

    def niSwitch_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetAttributeViReal64_cfunc is None:
                self.niSwitch_GetAttributeViReal64_cfunc = self._library.niSwitch_GetAttributeViReal64
                self.niSwitch_GetAttributeViReal64_cfunc.argtypes = [ViSession, ViConstString, ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niSwitch_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value).value

    def niSwitch_GetAttributeViString(self, vi, channel_name, attribute_id, array_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetAttributeViString_cfunc is None:
                self.niSwitch_GetAttributeViString_cfunc = self._library.niSwitch_GetAttributeViString
                self.niSwitch_GetAttributeViString_cfunc.argtypes = [ViSession, ViConstString, ViAttr, ViInt32, ViString]  # noqa: F405
                self.niSwitch_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetAttributeViString_cfunc(vi, channel_name, attribute_id, array_size, attribute_value).value

    def niSwitch_GetChannelName(self, vi, index, buffer_size, channel_name_buffer):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetChannelName_cfunc is None:
                self.niSwitch_GetChannelName_cfunc = self._library.niSwitch_GetChannelName
                self.niSwitch_GetChannelName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ViString]  # noqa: F405
                self.niSwitch_GetChannelName_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetChannelName_cfunc(vi, index, buffer_size, channel_name_buffer).value

    def niSwitch_GetError(self, vi, code, buffer_size, description):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetError_cfunc is None:
                self.niSwitch_GetError_cfunc = self._library.niSwitch_GetError
                self.niSwitch_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ViString]  # noqa: F405
                self.niSwitch_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetError_cfunc(vi, code, buffer_size, description).value

    def niSwitch_GetPath(self, vi, channel1, channel2, buffer_size, path):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetPath_cfunc is None:
                self.niSwitch_GetPath_cfunc = self._library.niSwitch_GetPath
                self.niSwitch_GetPath_cfunc.argtypes = [ViSession, ViConstString, ViConstString, ViInt32, ViString]  # noqa: F405
                self.niSwitch_GetPath_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetPath_cfunc(vi, channel1, channel2, buffer_size, path).value

    def niSwitch_GetRelayCount(self, vi, relay_name, relay_count):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetRelayCount_cfunc is None:
                self.niSwitch_GetRelayCount_cfunc = self._library.niSwitch_GetRelayCount
                self.niSwitch_GetRelayCount_cfunc.argtypes = [ViSession, ViConstString, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSwitch_GetRelayCount_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetRelayCount_cfunc(vi, relay_name, relay_count).value

    def niSwitch_GetRelayName(self, vi, index, relay_name_buffer_size, relay_name_buffer):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetRelayName_cfunc is None:
                self.niSwitch_GetRelayName_cfunc = self._library.niSwitch_GetRelayName
                self.niSwitch_GetRelayName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ViString]  # noqa: F405
                self.niSwitch_GetRelayName_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetRelayName_cfunc(vi, index, relay_name_buffer_size, relay_name_buffer).value

    def niSwitch_GetRelayPosition(self, vi, relay_name, relay_position):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetRelayPosition_cfunc is None:
                self.niSwitch_GetRelayPosition_cfunc = self._library.niSwitch_GetRelayPosition
                self.niSwitch_GetRelayPosition_cfunc.argtypes = [ViSession, ViConstString, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSwitch_GetRelayPosition_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetRelayPosition_cfunc(vi, relay_name, relay_position).value

    def niSwitch_InitWithTopology(self, resource_name, topology, simulate, reset_device, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_InitWithTopology_cfunc is None:
                self.niSwitch_InitWithTopology_cfunc = self._library.niSwitch_InitWithTopology
                self.niSwitch_InitWithTopology_cfunc.argtypes = [ViRsrc, ViConstString, ViBoolean, ViBoolean, ctypes.POINTER(ViSession)]  # noqa: F405
                self.niSwitch_InitWithTopology_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_InitWithTopology_cfunc(resource_name, topology, simulate, reset_device, vi).value

    def niSwitch_InitiateScan(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_InitiateScan_cfunc is None:
                self.niSwitch_InitiateScan_cfunc = self._library.niSwitch_InitiateScan
                self.niSwitch_InitiateScan_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_InitiateScan_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_InitiateScan_cfunc(vi).value

    def niSwitch_IsDebounced(self, vi, is_debounced):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_IsDebounced_cfunc is None:
                self.niSwitch_IsDebounced_cfunc = self._library.niSwitch_IsDebounced
                self.niSwitch_IsDebounced_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niSwitch_IsDebounced_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_IsDebounced_cfunc(vi, is_debounced).value

    def niSwitch_IsScanning(self, vi, is_scanning):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_IsScanning_cfunc is None:
                self.niSwitch_IsScanning_cfunc = self._library.niSwitch_IsScanning
                self.niSwitch_IsScanning_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niSwitch_IsScanning_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_IsScanning_cfunc(vi, is_scanning).value

    def niSwitch_RelayControl(self, vi, relay_name, relay_action):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_RelayControl_cfunc is None:
                self.niSwitch_RelayControl_cfunc = self._library.niSwitch_RelayControl
                self.niSwitch_RelayControl_cfunc.argtypes = [ViSession, ViConstString, ViInt32]  # noqa: F405
                self.niSwitch_RelayControl_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_RelayControl_cfunc(vi, relay_name, relay_action).value

    def niSwitch_ResetWithDefaults(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_ResetWithDefaults_cfunc is None:
                self.niSwitch_ResetWithDefaults_cfunc = self._library.niSwitch_ResetWithDefaults
                self.niSwitch_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_ResetWithDefaults_cfunc(vi).value

    def niSwitch_RouteScanAdvancedOutput(self, vi, scan_advanced_output_connector, scan_advanced_output_bus_line, invert):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_RouteScanAdvancedOutput_cfunc is None:
                self.niSwitch_RouteScanAdvancedOutput_cfunc = self._library.niSwitch_RouteScanAdvancedOutput
                self.niSwitch_RouteScanAdvancedOutput_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ViBoolean]  # noqa: F405
                self.niSwitch_RouteScanAdvancedOutput_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_RouteScanAdvancedOutput_cfunc(vi, scan_advanced_output_connector, scan_advanced_output_bus_line, invert).value

    def niSwitch_RouteTriggerInput(self, vi, trigger_input_connector, trigger_input_bus_line, invert):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_RouteTriggerInput_cfunc is None:
                self.niSwitch_RouteTriggerInput_cfunc = self._library.niSwitch_RouteTriggerInput
                self.niSwitch_RouteTriggerInput_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ViBoolean]  # noqa: F405
                self.niSwitch_RouteTriggerInput_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_RouteTriggerInput_cfunc(vi, trigger_input_connector, trigger_input_bus_line, invert).value

    def niSwitch_SendSoftwareTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_SendSoftwareTrigger_cfunc is None:
                self.niSwitch_SendSoftwareTrigger_cfunc = self._library.niSwitch_SendSoftwareTrigger
                self.niSwitch_SendSoftwareTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_SendSoftwareTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_SendSoftwareTrigger_cfunc(vi).value

    def niSwitch_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_SetAttributeViBoolean_cfunc is None:
                self.niSwitch_SetAttributeViBoolean_cfunc = self._library.niSwitch_SetAttributeViBoolean
                self.niSwitch_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ViConstString, ViAttr, ViBoolean]  # noqa: F405
                self.niSwitch_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_SetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value).value

    def niSwitch_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_SetAttributeViInt32_cfunc is None:
                self.niSwitch_SetAttributeViInt32_cfunc = self._library.niSwitch_SetAttributeViInt32
                self.niSwitch_SetAttributeViInt32_cfunc.argtypes = [ViSession, ViConstString, ViAttr, ViInt32]  # noqa: F405
                self.niSwitch_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_SetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value).value

    def niSwitch_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_SetAttributeViReal64_cfunc is None:
                self.niSwitch_SetAttributeViReal64_cfunc = self._library.niSwitch_SetAttributeViReal64
                self.niSwitch_SetAttributeViReal64_cfunc.argtypes = [ViSession, ViConstString, ViAttr, ViReal64]  # noqa: F405
                self.niSwitch_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_SetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value).value

    def niSwitch_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_SetAttributeViString_cfunc is None:
                self.niSwitch_SetAttributeViString_cfunc = self._library.niSwitch_SetAttributeViString
                self.niSwitch_SetAttributeViString_cfunc.argtypes = [ViSession, ViConstString, ViAttr, ViString]  # noqa: F405
                self.niSwitch_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_SetAttributeViString_cfunc(vi, channel_name, attribute_id, attribute_value).value

    def niSwitch_SetContinuousScan(self, vi, continuous_scan):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_SetContinuousScan_cfunc is None:
                self.niSwitch_SetContinuousScan_cfunc = self._library.niSwitch_SetContinuousScan
                self.niSwitch_SetContinuousScan_cfunc.argtypes = [ViSession, ViBoolean]  # noqa: F405
                self.niSwitch_SetContinuousScan_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_SetContinuousScan_cfunc(vi, continuous_scan).value

    def niSwitch_SetPath(self, vi, path_list):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_SetPath_cfunc is None:
                self.niSwitch_SetPath_cfunc = self._library.niSwitch_SetPath
                self.niSwitch_SetPath_cfunc.argtypes = [ViSession, ViConstString]  # noqa: F405
                self.niSwitch_SetPath_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_SetPath_cfunc(vi, path_list).value

    def niSwitch_WaitForDebounce(self, vi, maximum_time_ms):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_WaitForDebounce_cfunc is None:
                self.niSwitch_WaitForDebounce_cfunc = self._library.niSwitch_WaitForDebounce
                self.niSwitch_WaitForDebounce_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niSwitch_WaitForDebounce_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_WaitForDebounce_cfunc(vi, maximum_time_ms).value

    def niSwitch_WaitForScanComplete(self, vi, maximum_time_ms):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_WaitForScanComplete_cfunc is None:
                self.niSwitch_WaitForScanComplete_cfunc = self._library.niSwitch_WaitForScanComplete
                self.niSwitch_WaitForScanComplete_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niSwitch_WaitForScanComplete_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_WaitForScanComplete_cfunc(vi, maximum_time_ms).value

    def niSwitch_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_close_cfunc is None:
                self.niSwitch_close_cfunc = self._library.niSwitch_close
                self.niSwitch_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_close_cfunc(vi).value

    def niSwitch_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_error_message_cfunc is None:
                self.niSwitch_error_message_cfunc = self._library.niSwitch_error_message
                self.niSwitch_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_error_message_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_error_message_cfunc(vi, error_code, error_message).value

    def niSwitch_reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_reset_cfunc is None:
                self.niSwitch_reset_cfunc = self._library.niSwitch_reset
                self.niSwitch_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_reset_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_reset_cfunc(vi).value

    def niSwitch_revision_query(self, vi, instrument_driver_revision, firmware_revision):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_revision_query_cfunc is None:
                self.niSwitch_revision_query_cfunc = self._library.niSwitch_revision_query
                self.niSwitch_revision_query_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_revision_query_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_revision_query_cfunc(vi, instrument_driver_revision, firmware_revision).value

    def niSwitch_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_self_test_cfunc is None:
                self.niSwitch_self_test_cfunc = self._library.niSwitch_self_test
                self.niSwitch_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_self_test_cfunc(vi, self_test_result, self_test_message).value
