# -*- coding: utf-8 -*-
# This file was generated
import sys  # noqa: F401   - Not all mock_helpers will need this


class MockFunctionCallError(Exception):
    def __init__(self, function, param=None):
        self.function = function
        self.param = param
        msg = "{0} called without setting side_effect".format(self.function)
        if param is not None:
            msg += " or setting the {0} parameter return value".format(self.param)
        super(Exception, self).__init__(msg)


class SideEffectsHelper(object):
    def __init__(self):
        self._defaults = {}
        self._defaults['AbortScan'] = {}
        self._defaults['AbortScan']['return'] = 0
        self._defaults['CanConnect'] = {}
        self._defaults['CanConnect']['return'] = 0
        self._defaults['CanConnect']['pathCapability'] = None
        self._defaults['Commit'] = {}
        self._defaults['Commit']['return'] = 0
        self._defaults['Connect'] = {}
        self._defaults['Connect']['return'] = 0
        self._defaults['ConnectMultiple'] = {}
        self._defaults['ConnectMultiple']['return'] = 0
        self._defaults['Disable'] = {}
        self._defaults['Disable']['return'] = 0
        self._defaults['Disconnect'] = {}
        self._defaults['Disconnect']['return'] = 0
        self._defaults['DisconnectAll'] = {}
        self._defaults['DisconnectAll']['return'] = 0
        self._defaults['DisconnectMultiple'] = {}
        self._defaults['DisconnectMultiple']['return'] = 0
        self._defaults['GetAttributeViBoolean'] = {}
        self._defaults['GetAttributeViBoolean']['return'] = 0
        self._defaults['GetAttributeViBoolean']['attributeValue'] = None
        self._defaults['GetAttributeViInt32'] = {}
        self._defaults['GetAttributeViInt32']['return'] = 0
        self._defaults['GetAttributeViInt32']['attributeValue'] = None
        self._defaults['GetAttributeViReal64'] = {}
        self._defaults['GetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViReal64']['attributeValue'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['attributeValue'] = None
        self._defaults['GetChannelName'] = {}
        self._defaults['GetChannelName']['return'] = 0
        self._defaults['GetChannelName']['channelNameBuffer'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['code'] = None
        self._defaults['GetError']['description'] = None
        self._defaults['GetPath'] = {}
        self._defaults['GetPath']['return'] = 0
        self._defaults['GetPath']['path'] = None
        self._defaults['GetRelayCount'] = {}
        self._defaults['GetRelayCount']['return'] = 0
        self._defaults['GetRelayCount']['relayCount'] = None
        self._defaults['GetRelayName'] = {}
        self._defaults['GetRelayName']['return'] = 0
        self._defaults['GetRelayName']['relayNameBuffer'] = None
        self._defaults['GetRelayPosition'] = {}
        self._defaults['GetRelayPosition']['return'] = 0
        self._defaults['GetRelayPosition']['relayPosition'] = None
        self._defaults['InitWithTopology'] = {}
        self._defaults['InitWithTopology']['return'] = 0
        self._defaults['InitWithTopology']['vi'] = None
        self._defaults['InitiateScan'] = {}
        self._defaults['InitiateScan']['return'] = 0
        self._defaults['LockSession'] = {}
        self._defaults['LockSession']['return'] = 0
        self._defaults['LockSession']['callerHasLock'] = None
        self._defaults['RelayControl'] = {}
        self._defaults['RelayControl']['return'] = 0
        self._defaults['ResetWithDefaults'] = {}
        self._defaults['ResetWithDefaults']['return'] = 0
        self._defaults['RouteScanAdvancedOutput'] = {}
        self._defaults['RouteScanAdvancedOutput']['return'] = 0
        self._defaults['RouteTriggerInput'] = {}
        self._defaults['RouteTriggerInput']['return'] = 0
        self._defaults['SendSoftwareTrigger'] = {}
        self._defaults['SendSoftwareTrigger']['return'] = 0
        self._defaults['SetAttributeViBoolean'] = {}
        self._defaults['SetAttributeViBoolean']['return'] = 0
        self._defaults['SetAttributeViInt32'] = {}
        self._defaults['SetAttributeViInt32']['return'] = 0
        self._defaults['SetAttributeViReal64'] = {}
        self._defaults['SetAttributeViReal64']['return'] = 0
        self._defaults['SetAttributeViString'] = {}
        self._defaults['SetAttributeViString']['return'] = 0
        self._defaults['SetPath'] = {}
        self._defaults['SetPath']['return'] = 0
        self._defaults['UnlockSession'] = {}
        self._defaults['UnlockSession']['return'] = 0
        self._defaults['UnlockSession']['callerHasLock'] = None
        self._defaults['WaitForDebounce'] = {}
        self._defaults['WaitForDebounce']['return'] = 0
        self._defaults['WaitForScanComplete'] = {}
        self._defaults['WaitForScanComplete']['return'] = 0
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0
        self._defaults['error_message'] = {}
        self._defaults['error_message']['return'] = 0
        self._defaults['error_message']['errorMessage'] = None
        self._defaults['reset'] = {}
        self._defaults['reset']['return'] = 0
        self._defaults['self_test'] = {}
        self._defaults['self_test']['return'] = 0
        self._defaults['self_test']['selfTestResult'] = None
        self._defaults['self_test']['selfTestMessage'] = None

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niSwitch_AbortScan(self, vi):  # noqa: N802
        if self._defaults['AbortScan']['return'] != 0:
            return self._defaults['AbortScan']['return']
        return self._defaults['AbortScan']['return']

    def niSwitch_CanConnect(self, vi, channel1, channel2, path_capability):  # noqa: N802
        if self._defaults['CanConnect']['return'] != 0:
            return self._defaults['CanConnect']['return']
        # path_capability
        if self._defaults['CanConnect']['pathCapability'] is None:
            raise MockFunctionCallError("niSwitch_CanConnect", param='pathCapability')
        if path_capability is not None:
            path_capability.contents.value = self._defaults['CanConnect']['pathCapability']
        return self._defaults['CanConnect']['return']

    def niSwitch_Commit(self, vi):  # noqa: N802
        if self._defaults['Commit']['return'] != 0:
            return self._defaults['Commit']['return']
        return self._defaults['Commit']['return']

    def niSwitch_Connect(self, vi, channel1, channel2):  # noqa: N802
        if self._defaults['Connect']['return'] != 0:
            return self._defaults['Connect']['return']
        return self._defaults['Connect']['return']

    def niSwitch_ConnectMultiple(self, vi, connection_list):  # noqa: N802
        if self._defaults['ConnectMultiple']['return'] != 0:
            return self._defaults['ConnectMultiple']['return']
        return self._defaults['ConnectMultiple']['return']

    def niSwitch_Disable(self, vi):  # noqa: N802
        if self._defaults['Disable']['return'] != 0:
            return self._defaults['Disable']['return']
        return self._defaults['Disable']['return']

    def niSwitch_Disconnect(self, vi, channel1, channel2):  # noqa: N802
        if self._defaults['Disconnect']['return'] != 0:
            return self._defaults['Disconnect']['return']
        return self._defaults['Disconnect']['return']

    def niSwitch_DisconnectAll(self, vi):  # noqa: N802
        if self._defaults['DisconnectAll']['return'] != 0:
            return self._defaults['DisconnectAll']['return']
        return self._defaults['DisconnectAll']['return']

    def niSwitch_DisconnectMultiple(self, vi, disconnection_list):  # noqa: N802
        if self._defaults['DisconnectMultiple']['return'] != 0:
            return self._defaults['DisconnectMultiple']['return']
        return self._defaults['DisconnectMultiple']['return']

    def niSwitch_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        # attribute_value
        if self._defaults['GetAttributeViBoolean']['attributeValue'] is None:
            raise MockFunctionCallError("niSwitch_GetAttributeViBoolean", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViBoolean']['attributeValue']
        return self._defaults['GetAttributeViBoolean']['return']

    def niSwitch_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # attribute_value
        if self._defaults['GetAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niSwitch_GetAttributeViInt32", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViInt32']['attributeValue']
        return self._defaults['GetAttributeViInt32']['return']

    def niSwitch_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # attribute_value
        if self._defaults['GetAttributeViReal64']['attributeValue'] is None:
            raise MockFunctionCallError("niSwitch_GetAttributeViReal64", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViReal64']['attributeValue']
        return self._defaults['GetAttributeViReal64']['return']

    def niSwitch_GetAttributeViString(self, vi, channel_name, attribute_id, array_size, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        if self._defaults['GetAttributeViString']['attributeValue'] is None:
            raise MockFunctionCallError("niSwitch_GetAttributeViString", param='attributeValue')
        if array_size.value == 0:
            return len(self._defaults['GetAttributeViString']['attributeValue'])
        attribute_value.value = self._defaults['GetAttributeViString']['attributeValue'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niSwitch_GetChannelName(self, vi, index, buffer_size, channel_name_buffer):  # noqa: N802
        if self._defaults['GetChannelName']['return'] != 0:
            return self._defaults['GetChannelName']['return']
        if self._defaults['GetChannelName']['channelNameBuffer'] is None:
            raise MockFunctionCallError("niSwitch_GetChannelName", param='channelNameBuffer')
        if buffer_size.value == 0:
            return len(self._defaults['GetChannelName']['channelNameBuffer'])
        channel_name_buffer.value = self._defaults['GetChannelName']['channelNameBuffer'].encode('ascii')
        return self._defaults['GetChannelName']['return']

    def niSwitch_GetError(self, vi, code, buffer_size, description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        # code
        if self._defaults['GetError']['code'] is None:
            raise MockFunctionCallError("niSwitch_GetError", param='code')
        if code is not None:
            code.contents.value = self._defaults['GetError']['code']
        if self._defaults['GetError']['description'] is None:
            raise MockFunctionCallError("niSwitch_GetError", param='description')
        if buffer_size.value == 0:
            return len(self._defaults['GetError']['description'])
        description.value = self._defaults['GetError']['description'].encode('ascii')
        return self._defaults['GetError']['return']

    def niSwitch_GetPath(self, vi, channel1, channel2, buffer_size, path):  # noqa: N802
        if self._defaults['GetPath']['return'] != 0:
            return self._defaults['GetPath']['return']
        if self._defaults['GetPath']['path'] is None:
            raise MockFunctionCallError("niSwitch_GetPath", param='path')
        if buffer_size.value == 0:
            return len(self._defaults['GetPath']['path'])
        path.value = self._defaults['GetPath']['path'].encode('ascii')
        return self._defaults['GetPath']['return']

    def niSwitch_GetRelayCount(self, vi, relay_name, relay_count):  # noqa: N802
        if self._defaults['GetRelayCount']['return'] != 0:
            return self._defaults['GetRelayCount']['return']
        # relay_count
        if self._defaults['GetRelayCount']['relayCount'] is None:
            raise MockFunctionCallError("niSwitch_GetRelayCount", param='relayCount')
        if relay_count is not None:
            relay_count.contents.value = self._defaults['GetRelayCount']['relayCount']
        return self._defaults['GetRelayCount']['return']

    def niSwitch_GetRelayName(self, vi, index, relay_name_buffer_size, relay_name_buffer):  # noqa: N802
        if self._defaults['GetRelayName']['return'] != 0:
            return self._defaults['GetRelayName']['return']
        if self._defaults['GetRelayName']['relayNameBuffer'] is None:
            raise MockFunctionCallError("niSwitch_GetRelayName", param='relayNameBuffer')
        if relay_name_buffer_size.value == 0:
            return len(self._defaults['GetRelayName']['relayNameBuffer'])
        relay_name_buffer.value = self._defaults['GetRelayName']['relayNameBuffer'].encode('ascii')
        return self._defaults['GetRelayName']['return']

    def niSwitch_GetRelayPosition(self, vi, relay_name, relay_position):  # noqa: N802
        if self._defaults['GetRelayPosition']['return'] != 0:
            return self._defaults['GetRelayPosition']['return']
        # relay_position
        if self._defaults['GetRelayPosition']['relayPosition'] is None:
            raise MockFunctionCallError("niSwitch_GetRelayPosition", param='relayPosition')
        if relay_position is not None:
            relay_position.contents.value = self._defaults['GetRelayPosition']['relayPosition']
        return self._defaults['GetRelayPosition']['return']

    def niSwitch_InitWithTopology(self, resource_name, topology, simulate, reset_device, vi):  # noqa: N802
        if self._defaults['InitWithTopology']['return'] != 0:
            return self._defaults['InitWithTopology']['return']
        # vi
        if self._defaults['InitWithTopology']['vi'] is None:
            raise MockFunctionCallError("niSwitch_InitWithTopology", param='vi')
        if vi is not None:
            vi.contents.value = self._defaults['InitWithTopology']['vi']
        return self._defaults['InitWithTopology']['return']

    def niSwitch_InitiateScan(self, vi):  # noqa: N802
        if self._defaults['InitiateScan']['return'] != 0:
            return self._defaults['InitiateScan']['return']
        return self._defaults['InitiateScan']['return']

    def niSwitch_LockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['LockSession']['return'] != 0:
            return self._defaults['LockSession']['return']
        # caller_has_lock
        if self._defaults['LockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niSwitch_LockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['LockSession']['callerHasLock']
        return self._defaults['LockSession']['return']

    def niSwitch_RelayControl(self, vi, relay_name, relay_action):  # noqa: N802
        if self._defaults['RelayControl']['return'] != 0:
            return self._defaults['RelayControl']['return']
        return self._defaults['RelayControl']['return']

    def niSwitch_ResetWithDefaults(self, vi):  # noqa: N802
        if self._defaults['ResetWithDefaults']['return'] != 0:
            return self._defaults['ResetWithDefaults']['return']
        return self._defaults['ResetWithDefaults']['return']

    def niSwitch_RouteScanAdvancedOutput(self, vi, scan_advanced_output_connector, scan_advanced_output_bus_line, invert):  # noqa: N802
        if self._defaults['RouteScanAdvancedOutput']['return'] != 0:
            return self._defaults['RouteScanAdvancedOutput']['return']
        return self._defaults['RouteScanAdvancedOutput']['return']

    def niSwitch_RouteTriggerInput(self, vi, trigger_input_connector, trigger_input_bus_line, invert):  # noqa: N802
        if self._defaults['RouteTriggerInput']['return'] != 0:
            return self._defaults['RouteTriggerInput']['return']
        return self._defaults['RouteTriggerInput']['return']

    def niSwitch_SendSoftwareTrigger(self, vi):  # noqa: N802
        if self._defaults['SendSoftwareTrigger']['return'] != 0:
            return self._defaults['SendSoftwareTrigger']['return']
        return self._defaults['SendSoftwareTrigger']['return']

    def niSwitch_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niSwitch_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niSwitch_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niSwitch_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niSwitch_SetPath(self, vi, path_list):  # noqa: N802
        if self._defaults['SetPath']['return'] != 0:
            return self._defaults['SetPath']['return']
        return self._defaults['SetPath']['return']

    def niSwitch_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['UnlockSession']['return'] != 0:
            return self._defaults['UnlockSession']['return']
        # caller_has_lock
        if self._defaults['UnlockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niSwitch_UnlockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['UnlockSession']['callerHasLock']
        return self._defaults['UnlockSession']['return']

    def niSwitch_WaitForDebounce(self, vi, maximum_time_ms):  # noqa: N802
        if self._defaults['WaitForDebounce']['return'] != 0:
            return self._defaults['WaitForDebounce']['return']
        return self._defaults['WaitForDebounce']['return']

    def niSwitch_WaitForScanComplete(self, vi, maximum_time_ms):  # noqa: N802
        if self._defaults['WaitForScanComplete']['return'] != 0:
            return self._defaults['WaitForScanComplete']['return']
        return self._defaults['WaitForScanComplete']['return']

    def niSwitch_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niSwitch_error_message(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['error_message']['return'] != 0:
            return self._defaults['error_message']['return']
        # error_message
        if self._defaults['error_message']['errorMessage'] is None:
            raise MockFunctionCallError("niSwitch_error_message", param='errorMessage')
        test_value = self._defaults['error_message']['errorMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(error_message) >= len(test_value)
        for i in range(len(test_value)):
            error_message[i] = test_value[i]
        return self._defaults['error_message']['return']

    def niSwitch_reset(self, vi):  # noqa: N802
        if self._defaults['reset']['return'] != 0:
            return self._defaults['reset']['return']
        return self._defaults['reset']['return']

    def niSwitch_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        # self_test_result
        if self._defaults['self_test']['selfTestResult'] is None:
            raise MockFunctionCallError("niSwitch_self_test", param='selfTestResult')
        if self_test_result is not None:
            self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        # self_test_message
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niSwitch_self_test", param='selfTestMessage')
        test_value = self._defaults['self_test']['selfTestMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(self_test_message) >= len(test_value)
        for i in range(len(test_value)):
            self_test_message[i] = test_value[i]
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niSwitch_AbortScan_cfunc.side_effect = MockFunctionCallError("niSwitch_AbortScan_cfunc")
        mock_library.niSwitch_AbortScan_cfunc.return_value = 0
        mock_library.niSwitch_CanConnect_cfunc.side_effect = MockFunctionCallError("niSwitch_CanConnect_cfunc")
        mock_library.niSwitch_CanConnect_cfunc.return_value = 0
        mock_library.niSwitch_Commit_cfunc.side_effect = MockFunctionCallError("niSwitch_Commit_cfunc")
        mock_library.niSwitch_Commit_cfunc.return_value = 0
        mock_library.niSwitch_Connect_cfunc.side_effect = MockFunctionCallError("niSwitch_Connect_cfunc")
        mock_library.niSwitch_Connect_cfunc.return_value = 0
        mock_library.niSwitch_ConnectMultiple_cfunc.side_effect = MockFunctionCallError("niSwitch_ConnectMultiple_cfunc")
        mock_library.niSwitch_ConnectMultiple_cfunc.return_value = 0
        mock_library.niSwitch_Disable_cfunc.side_effect = MockFunctionCallError("niSwitch_Disable_cfunc")
        mock_library.niSwitch_Disable_cfunc.return_value = 0
        mock_library.niSwitch_Disconnect_cfunc.side_effect = MockFunctionCallError("niSwitch_Disconnect_cfunc")
        mock_library.niSwitch_Disconnect_cfunc.return_value = 0
        mock_library.niSwitch_DisconnectAll_cfunc.side_effect = MockFunctionCallError("niSwitch_DisconnectAll_cfunc")
        mock_library.niSwitch_DisconnectAll_cfunc.return_value = 0
        mock_library.niSwitch_DisconnectMultiple_cfunc.side_effect = MockFunctionCallError("niSwitch_DisconnectMultiple_cfunc")
        mock_library.niSwitch_DisconnectMultiple_cfunc.return_value = 0
        mock_library.niSwitch_GetAttributeViBoolean_cfunc.side_effect = MockFunctionCallError("niSwitch_GetAttributeViBoolean_cfunc")
        mock_library.niSwitch_GetAttributeViBoolean_cfunc.return_value = 0
        mock_library.niSwitch_GetAttributeViInt32_cfunc.side_effect = MockFunctionCallError("niSwitch_GetAttributeViInt32_cfunc")
        mock_library.niSwitch_GetAttributeViInt32_cfunc.return_value = 0
        mock_library.niSwitch_GetAttributeViReal64_cfunc.side_effect = MockFunctionCallError("niSwitch_GetAttributeViReal64_cfunc")
        mock_library.niSwitch_GetAttributeViReal64_cfunc.return_value = 0
        mock_library.niSwitch_GetAttributeViString_cfunc.side_effect = MockFunctionCallError("niSwitch_GetAttributeViString_cfunc")
        mock_library.niSwitch_GetAttributeViString_cfunc.return_value = 0
        mock_library.niSwitch_GetChannelName_cfunc.side_effect = MockFunctionCallError("niSwitch_GetChannelName_cfunc")
        mock_library.niSwitch_GetChannelName_cfunc.return_value = 0
        mock_library.niSwitch_GetError_cfunc.side_effect = MockFunctionCallError("niSwitch_GetError_cfunc")
        mock_library.niSwitch_GetError_cfunc.return_value = 0
        mock_library.niSwitch_GetPath_cfunc.side_effect = MockFunctionCallError("niSwitch_GetPath_cfunc")
        mock_library.niSwitch_GetPath_cfunc.return_value = 0
        mock_library.niSwitch_GetRelayCount_cfunc.side_effect = MockFunctionCallError("niSwitch_GetRelayCount_cfunc")
        mock_library.niSwitch_GetRelayCount_cfunc.return_value = 0
        mock_library.niSwitch_GetRelayName_cfunc.side_effect = MockFunctionCallError("niSwitch_GetRelayName_cfunc")
        mock_library.niSwitch_GetRelayName_cfunc.return_value = 0
        mock_library.niSwitch_GetRelayPosition_cfunc.side_effect = MockFunctionCallError("niSwitch_GetRelayPosition_cfunc")
        mock_library.niSwitch_GetRelayPosition_cfunc.return_value = 0
        mock_library.niSwitch_InitWithTopology_cfunc.side_effect = MockFunctionCallError("niSwitch_InitWithTopology_cfunc")
        mock_library.niSwitch_InitWithTopology_cfunc.return_value = 0
        mock_library.niSwitch_InitiateScan_cfunc.side_effect = MockFunctionCallError("niSwitch_InitiateScan_cfunc")
        mock_library.niSwitch_InitiateScan_cfunc.return_value = 0
        mock_library.niSwitch_LockSession_cfunc.side_effect = MockFunctionCallError("niSwitch_LockSession_cfunc")
        mock_library.niSwitch_LockSession_cfunc.return_value = 0
        mock_library.niSwitch_RelayControl_cfunc.side_effect = MockFunctionCallError("niSwitch_RelayControl_cfunc")
        mock_library.niSwitch_RelayControl_cfunc.return_value = 0
        mock_library.niSwitch_ResetWithDefaults_cfunc.side_effect = MockFunctionCallError("niSwitch_ResetWithDefaults_cfunc")
        mock_library.niSwitch_ResetWithDefaults_cfunc.return_value = 0
        mock_library.niSwitch_RouteScanAdvancedOutput_cfunc.side_effect = MockFunctionCallError("niSwitch_RouteScanAdvancedOutput_cfunc")
        mock_library.niSwitch_RouteScanAdvancedOutput_cfunc.return_value = 0
        mock_library.niSwitch_RouteTriggerInput_cfunc.side_effect = MockFunctionCallError("niSwitch_RouteTriggerInput_cfunc")
        mock_library.niSwitch_RouteTriggerInput_cfunc.return_value = 0
        mock_library.niSwitch_SendSoftwareTrigger_cfunc.side_effect = MockFunctionCallError("niSwitch_SendSoftwareTrigger_cfunc")
        mock_library.niSwitch_SendSoftwareTrigger_cfunc.return_value = 0
        mock_library.niSwitch_SetAttributeViBoolean_cfunc.side_effect = MockFunctionCallError("niSwitch_SetAttributeViBoolean_cfunc")
        mock_library.niSwitch_SetAttributeViBoolean_cfunc.return_value = 0
        mock_library.niSwitch_SetAttributeViInt32_cfunc.side_effect = MockFunctionCallError("niSwitch_SetAttributeViInt32_cfunc")
        mock_library.niSwitch_SetAttributeViInt32_cfunc.return_value = 0
        mock_library.niSwitch_SetAttributeViReal64_cfunc.side_effect = MockFunctionCallError("niSwitch_SetAttributeViReal64_cfunc")
        mock_library.niSwitch_SetAttributeViReal64_cfunc.return_value = 0
        mock_library.niSwitch_SetAttributeViString_cfunc.side_effect = MockFunctionCallError("niSwitch_SetAttributeViString_cfunc")
        mock_library.niSwitch_SetAttributeViString_cfunc.return_value = 0
        mock_library.niSwitch_SetPath_cfunc.side_effect = MockFunctionCallError("niSwitch_SetPath_cfunc")
        mock_library.niSwitch_SetPath_cfunc.return_value = 0
        mock_library.niSwitch_UnlockSession_cfunc.side_effect = MockFunctionCallError("niSwitch_UnlockSession_cfunc")
        mock_library.niSwitch_UnlockSession_cfunc.return_value = 0
        mock_library.niSwitch_WaitForDebounce_cfunc.side_effect = MockFunctionCallError("niSwitch_WaitForDebounce_cfunc")
        mock_library.niSwitch_WaitForDebounce_cfunc.return_value = 0
        mock_library.niSwitch_WaitForScanComplete_cfunc.side_effect = MockFunctionCallError("niSwitch_WaitForScanComplete_cfunc")
        mock_library.niSwitch_WaitForScanComplete_cfunc.return_value = 0
        mock_library.niSwitch_close_cfunc.side_effect = MockFunctionCallError("niSwitch_close_cfunc")
        mock_library.niSwitch_close_cfunc.return_value = 0
        mock_library.niSwitch_error_message_cfunc.side_effect = MockFunctionCallError("niSwitch_error_message_cfunc")
        mock_library.niSwitch_error_message_cfunc.return_value = 0
        mock_library.niSwitch_reset_cfunc.side_effect = MockFunctionCallError("niSwitch_reset_cfunc")
        mock_library.niSwitch_reset_cfunc.return_value = 0
        mock_library.niSwitch_self_test_cfunc.side_effect = MockFunctionCallError("niSwitch_self_test_cfunc")
        mock_library.niSwitch_self_test_cfunc.return_value = 0
