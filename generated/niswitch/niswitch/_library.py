# -*- coding: utf-8 -*-
# This file was generated

import ctypes
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

    def niSwitch_AbortScan(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_AbortScan_cfunc is None:
                try:
                    self.niSwitch_AbortScan_cfunc = self._library.niSwitch_AbortScan
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_AbortScan was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_AbortScan_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_AbortScan_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_AbortScan_cfunc(vi)

    def niSwitch_CanConnect(self, vi, channel1, channel2, path_capability):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_CanConnect_cfunc is None:
                try:
                    self.niSwitch_CanConnect_cfunc = self._library.niSwitch_CanConnect
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_CanConnect was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_CanConnect_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSwitch_CanConnect_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_CanConnect_cfunc(vi, channel1, channel2, path_capability)

    def niSwitch_Commit(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_Commit_cfunc is None:
                try:
                    self.niSwitch_Commit_cfunc = self._library.niSwitch_Commit
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_Commit was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_Commit_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_Commit_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_Commit_cfunc(vi)

    def niSwitch_Connect(self, vi, channel1, channel2):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_Connect_cfunc is None:
                try:
                    self.niSwitch_Connect_cfunc = self._library.niSwitch_Connect
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_Connect was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_Connect_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_Connect_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_Connect_cfunc(vi, channel1, channel2)

    def niSwitch_ConnectMultiple(self, vi, connection_list):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_ConnectMultiple_cfunc is None:
                try:
                    self.niSwitch_ConnectMultiple_cfunc = self._library.niSwitch_ConnectMultiple
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_ConnectMultiple was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_ConnectMultiple_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_ConnectMultiple_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_ConnectMultiple_cfunc(vi, connection_list)

    def niSwitch_Disable(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_Disable_cfunc is None:
                try:
                    self.niSwitch_Disable_cfunc = self._library.niSwitch_Disable
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_Disable was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_Disable_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_Disable_cfunc(vi)

    def niSwitch_Disconnect(self, vi, channel1, channel2):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_Disconnect_cfunc is None:
                try:
                    self.niSwitch_Disconnect_cfunc = self._library.niSwitch_Disconnect
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_Disconnect was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_Disconnect_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_Disconnect_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_Disconnect_cfunc(vi, channel1, channel2)

    def niSwitch_DisconnectAll(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_DisconnectAll_cfunc is None:
                try:
                    self.niSwitch_DisconnectAll_cfunc = self._library.niSwitch_DisconnectAll
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_DisconnectAll was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_DisconnectAll_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_DisconnectAll_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_DisconnectAll_cfunc(vi)

    def niSwitch_DisconnectMultiple(self, vi, disconnection_list):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_DisconnectMultiple_cfunc is None:
                try:
                    self.niSwitch_DisconnectMultiple_cfunc = self._library.niSwitch_DisconnectMultiple
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_DisconnectMultiple was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_DisconnectMultiple_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_DisconnectMultiple_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_DisconnectMultiple_cfunc(vi, disconnection_list)

    def niSwitch_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetAttributeViBoolean_cfunc is None:
                try:
                    self.niSwitch_GetAttributeViBoolean_cfunc = self._library.niSwitch_GetAttributeViBoolean
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_GetAttributeViBoolean was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niSwitch_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niSwitch_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetAttributeViInt32_cfunc is None:
                try:
                    self.niSwitch_GetAttributeViInt32_cfunc = self._library.niSwitch_GetAttributeViInt32
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_GetAttributeViInt32 was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSwitch_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niSwitch_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetAttributeViReal64_cfunc is None:
                try:
                    self.niSwitch_GetAttributeViReal64_cfunc = self._library.niSwitch_GetAttributeViReal64
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_GetAttributeViReal64 was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niSwitch_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niSwitch_GetAttributeViString(self, vi, channel_name, attribute_id, array_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetAttributeViString_cfunc is None:
                try:
                    self.niSwitch_GetAttributeViString_cfunc = self._library.niSwitch_GetAttributeViString
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_GetAttributeViString was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetAttributeViString_cfunc(vi, channel_name, attribute_id, array_size, attribute_value)

    def niSwitch_GetChannelName(self, vi, index, buffer_size, channel_name_buffer):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetChannelName_cfunc is None:
                try:
                    self.niSwitch_GetChannelName_cfunc = self._library.niSwitch_GetChannelName
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_GetChannelName was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_GetChannelName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_GetChannelName_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetChannelName_cfunc(vi, index, buffer_size, channel_name_buffer)

    def niSwitch_GetError(self, vi, code, buffer_size, description):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetError_cfunc is None:
                try:
                    self.niSwitch_GetError_cfunc = self._library.niSwitch_GetError
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_GetError was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetError_cfunc(vi, code, buffer_size, description)

    def niSwitch_GetPath(self, vi, channel1, channel2, buffer_size, path):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetPath_cfunc is None:
                try:
                    self.niSwitch_GetPath_cfunc = self._library.niSwitch_GetPath
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_GetPath was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_GetPath_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_GetPath_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetPath_cfunc(vi, channel1, channel2, buffer_size, path)

    def niSwitch_GetRelayCount(self, vi, relay_name, relay_count):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetRelayCount_cfunc is None:
                try:
                    self.niSwitch_GetRelayCount_cfunc = self._library.niSwitch_GetRelayCount
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_GetRelayCount was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_GetRelayCount_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSwitch_GetRelayCount_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetRelayCount_cfunc(vi, relay_name, relay_count)

    def niSwitch_GetRelayName(self, vi, index, relay_name_buffer_size, relay_name_buffer):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetRelayName_cfunc is None:
                try:
                    self.niSwitch_GetRelayName_cfunc = self._library.niSwitch_GetRelayName
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_GetRelayName was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_GetRelayName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_GetRelayName_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetRelayName_cfunc(vi, index, relay_name_buffer_size, relay_name_buffer)

    def niSwitch_GetRelayPosition(self, vi, relay_name, relay_position):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_GetRelayPosition_cfunc is None:
                try:
                    self.niSwitch_GetRelayPosition_cfunc = self._library.niSwitch_GetRelayPosition
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_GetRelayPosition was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_GetRelayPosition_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niSwitch_GetRelayPosition_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_GetRelayPosition_cfunc(vi, relay_name, relay_position)

    def niSwitch_InitWithTopology(self, resource_name, topology, simulate, reset_device, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_InitWithTopology_cfunc is None:
                try:
                    self.niSwitch_InitWithTopology_cfunc = self._library.niSwitch_InitWithTopology
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_InitWithTopology was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_InitWithTopology_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean, ViBoolean, ctypes.POINTER(ViSession)]  # noqa: F405
                self.niSwitch_InitWithTopology_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_InitWithTopology_cfunc(resource_name, topology, simulate, reset_device, vi)

    def niSwitch_InitiateScan(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_InitiateScan_cfunc is None:
                try:
                    self.niSwitch_InitiateScan_cfunc = self._library.niSwitch_InitiateScan
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_InitiateScan was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_InitiateScan_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_InitiateScan_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_InitiateScan_cfunc(vi)

    def niSwitch_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_LockSession_cfunc is None:
                try:
                    self.niSwitch_LockSession_cfunc = self._library.niSwitch_LockSession
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_LockSession was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niSwitch_LockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_LockSession_cfunc(vi, caller_has_lock)

    def niSwitch_RelayControl(self, vi, relay_name, relay_action):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_RelayControl_cfunc is None:
                try:
                    self.niSwitch_RelayControl_cfunc = self._library.niSwitch_RelayControl
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_RelayControl was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_RelayControl_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niSwitch_RelayControl_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_RelayControl_cfunc(vi, relay_name, relay_action)

    def niSwitch_ResetWithDefaults(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_ResetWithDefaults_cfunc is None:
                try:
                    self.niSwitch_ResetWithDefaults_cfunc = self._library.niSwitch_ResetWithDefaults
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_ResetWithDefaults was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_ResetWithDefaults_cfunc(vi)

    def niSwitch_RouteScanAdvancedOutput(self, vi, scan_advanced_output_connector, scan_advanced_output_bus_line, invert):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_RouteScanAdvancedOutput_cfunc is None:
                try:
                    self.niSwitch_RouteScanAdvancedOutput_cfunc = self._library.niSwitch_RouteScanAdvancedOutput
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_RouteScanAdvancedOutput was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_RouteScanAdvancedOutput_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ViBoolean]  # noqa: F405
                self.niSwitch_RouteScanAdvancedOutput_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_RouteScanAdvancedOutput_cfunc(vi, scan_advanced_output_connector, scan_advanced_output_bus_line, invert)

    def niSwitch_RouteTriggerInput(self, vi, trigger_input_connector, trigger_input_bus_line, invert):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_RouteTriggerInput_cfunc is None:
                try:
                    self.niSwitch_RouteTriggerInput_cfunc = self._library.niSwitch_RouteTriggerInput
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_RouteTriggerInput was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_RouteTriggerInput_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ViBoolean]  # noqa: F405
                self.niSwitch_RouteTriggerInput_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_RouteTriggerInput_cfunc(vi, trigger_input_connector, trigger_input_bus_line, invert)

    def niSwitch_SendSoftwareTrigger(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_SendSoftwareTrigger_cfunc is None:
                try:
                    self.niSwitch_SendSoftwareTrigger_cfunc = self._library.niSwitch_SendSoftwareTrigger
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_SendSoftwareTrigger was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_SendSoftwareTrigger_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_SendSoftwareTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_SendSoftwareTrigger_cfunc(vi)

    def niSwitch_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_SetAttributeViBoolean_cfunc is None:
                try:
                    self.niSwitch_SetAttributeViBoolean_cfunc = self._library.niSwitch_SetAttributeViBoolean
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_SetAttributeViBoolean was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niSwitch_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_SetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niSwitch_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_SetAttributeViInt32_cfunc is None:
                try:
                    self.niSwitch_SetAttributeViInt32_cfunc = self._library.niSwitch_SetAttributeViInt32
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_SetAttributeViInt32 was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niSwitch_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_SetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niSwitch_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_SetAttributeViReal64_cfunc is None:
                try:
                    self.niSwitch_SetAttributeViReal64_cfunc = self._library.niSwitch_SetAttributeViReal64
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_SetAttributeViReal64 was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niSwitch_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_SetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niSwitch_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_SetAttributeViString_cfunc is None:
                try:
                    self.niSwitch_SetAttributeViString_cfunc = self._library.niSwitch_SetAttributeViString
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_SetAttributeViString was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_SetAttributeViString_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niSwitch_SetPath(self, vi, path_list):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_SetPath_cfunc is None:
                try:
                    self.niSwitch_SetPath_cfunc = self._library.niSwitch_SetPath
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_SetPath was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_SetPath_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_SetPath_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_SetPath_cfunc(vi, path_list)

    def niSwitch_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_UnlockSession_cfunc is None:
                try:
                    self.niSwitch_UnlockSession_cfunc = self._library.niSwitch_UnlockSession
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_UnlockSession was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niSwitch_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_UnlockSession_cfunc(vi, caller_has_lock)

    def niSwitch_WaitForDebounce(self, vi, maximum_time_ms):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_WaitForDebounce_cfunc is None:
                try:
                    self.niSwitch_WaitForDebounce_cfunc = self._library.niSwitch_WaitForDebounce
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_WaitForDebounce was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_WaitForDebounce_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niSwitch_WaitForDebounce_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_WaitForDebounce_cfunc(vi, maximum_time_ms)

    def niSwitch_WaitForScanComplete(self, vi, maximum_time_ms):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_WaitForScanComplete_cfunc is None:
                try:
                    self.niSwitch_WaitForScanComplete_cfunc = self._library.niSwitch_WaitForScanComplete
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_WaitForScanComplete was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_WaitForScanComplete_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niSwitch_WaitForScanComplete_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_WaitForScanComplete_cfunc(vi, maximum_time_ms)

    def niSwitch_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_close_cfunc is None:
                try:
                    self.niSwitch_close_cfunc = self._library.niSwitch_close
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_close was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_close_cfunc(vi)

    def niSwitch_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_error_message_cfunc is None:
                try:
                    self.niSwitch_error_message_cfunc = self._library.niSwitch_error_message
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_error_message was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_error_message_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_error_message_cfunc(vi, error_code, error_message)

    def niSwitch_reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_reset_cfunc is None:
                try:
                    self.niSwitch_reset_cfunc = self._library.niSwitch_reset
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_reset was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSwitch_reset_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_reset_cfunc(vi)

    def niSwitch_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niSwitch_self_test_cfunc is None:
                try:
                    self.niSwitch_self_test_cfunc = self._library.niSwitch_self_test
                except AttributeError as e:
                    raise AttributeError("Function niSwitch_self_test was not found in the NI-SWITCH runtime. Please visit "
                                         "http://www.ni.com/downloads/drivers/ to download a newer version and "
                                         "install it.") from e
                self.niSwitch_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niSwitch_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niSwitch_self_test_cfunc(vi, self_test_result, self_test_message)
