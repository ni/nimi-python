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
        self._defaults['CloseSession'] = {}
        self._defaults['CloseSession']['return'] = 0
        self._defaults['Connect'] = {}
        self._defaults['Connect']['return'] = 0
        self._defaults['ConnectAndDisconnect'] = {}
        self._defaults['ConnectAndDisconnect']['return'] = 0
        self._defaults['Disconnect'] = {}
        self._defaults['Disconnect']['return'] = 0
        self._defaults['DisconnectAll'] = {}
        self._defaults['DisconnectAll']['return'] = 0
        self._defaults['ExpandRouteSpec'] = {}
        self._defaults['ExpandRouteSpec']['return'] = 0
        self._defaults['ExpandRouteSpec']['expandedRouteSpecSize'] = None
        self._defaults['ExpandRouteSpec']['expandedRouteSpec'] = None
        self._defaults['FindRoute'] = {}
        self._defaults['FindRoute']['return'] = 0
        self._defaults['FindRoute']['routeSpecSize'] = None
        self._defaults['FindRoute']['pathCapability'] = None
        self._defaults['FindRoute']['routeSpec'] = None
        self._defaults['GetAllConnections'] = {}
        self._defaults['GetAllConnections']['return'] = 0
        self._defaults['GetAllConnections']['routeSpecSize'] = None
        self._defaults['GetAllConnections']['routeSpec'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorNumber'] = None
        self._defaults['GetError']['errorDescriptionSize'] = None
        self._defaults['GetError']['errorDescription'] = None
        self._defaults['GetIviDeviceSession'] = {}
        self._defaults['GetIviDeviceSession']['return'] = 0
        self._defaults['GetIviDeviceSession']['iviSessionHandle'] = None
        self._defaults['IsConnected'] = {}
        self._defaults['IsConnected']['return'] = 0
        self._defaults['IsConnected']['isConnected'] = None
        self._defaults['IsDebounced'] = {}
        self._defaults['IsDebounced']['return'] = 0
        self._defaults['IsDebounced']['isDebounced'] = None
        self._defaults['OpenSession'] = {}
        self._defaults['OpenSession']['return'] = 0
        self._defaults['OpenSession']['sessionHandle'] = None
        self._defaults['WaitForDebounce'] = {}
        self._defaults['WaitForDebounce']['return'] = 0

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niSE_CloseSession(self, session_handle):  # noqa: N802
        if self._defaults['CloseSession']['return'] != 0:
            return self._defaults['CloseSession']['return']
        return self._defaults['CloseSession']['return']

    def niSE_Connect(self, session_handle, connect_spec, multiconnect_mode, wait_for_debounce):  # noqa: N802
        if self._defaults['Connect']['return'] != 0:
            return self._defaults['Connect']['return']
        return self._defaults['Connect']['return']

    def niSE_ConnectAndDisconnect(self, session_handle, connect_spec, disconnect_spec, multiconnect_mode, operation_order, wait_for_debounce):  # noqa: N802
        if self._defaults['ConnectAndDisconnect']['return'] != 0:
            return self._defaults['ConnectAndDisconnect']['return']
        return self._defaults['ConnectAndDisconnect']['return']

    def niSE_Disconnect(self, session_handle, disconnect_spec):  # noqa: N802
        if self._defaults['Disconnect']['return'] != 0:
            return self._defaults['Disconnect']['return']
        return self._defaults['Disconnect']['return']

    def niSE_DisconnectAll(self, session_handle):  # noqa: N802
        if self._defaults['DisconnectAll']['return'] != 0:
            return self._defaults['DisconnectAll']['return']
        return self._defaults['DisconnectAll']['return']

    def niSE_ExpandRouteSpec(self, session_handle, route_spec, expand_action, expanded_route_spec, expanded_route_spec_size):  # noqa: N802
        if self._defaults['ExpandRouteSpec']['return'] != 0:
            return self._defaults['ExpandRouteSpec']['return']
        # expanded_route_spec_size
        if self._defaults['ExpandRouteSpec']['expandedRouteSpecSize'] is None:
            raise MockFunctionCallError("niSE_ExpandRouteSpec", param='expandedRouteSpecSize')
        if expanded_route_spec_size is not None:
            expanded_route_spec_size.contents.value = self._defaults['ExpandRouteSpec']['expandedRouteSpecSize']
        if self._defaults['ExpandRouteSpec']['expandedRouteSpec'] is None:
            raise MockFunctionCallError("niSE_ExpandRouteSpec", param='expandedRouteSpec')
        if expanded_route_spec_size.value == 0:
            return len(self._defaults['ExpandRouteSpec']['expandedRouteSpec'])
        try:
            expanded_route_spec_ref = expanded_route_spec.contents
        except AttributeError:
            expanded_route_spec_ref = expanded_route_spec
        for i in range(len(self._defaults['ExpandRouteSpec']['expandedRouteSpec'])):
            expanded_route_spec_ref[i] = self._defaults['ExpandRouteSpec']['expandedRouteSpec'][i]
        return self._defaults['ExpandRouteSpec']['return']

    def niSE_FindRoute(self, session_handle, channel1, channel2, route_spec, route_spec_size, path_capability):  # noqa: N802
        if self._defaults['FindRoute']['return'] != 0:
            return self._defaults['FindRoute']['return']
        # route_spec_size
        if self._defaults['FindRoute']['routeSpecSize'] is None:
            raise MockFunctionCallError("niSE_FindRoute", param='routeSpecSize')
        if route_spec_size is not None:
            route_spec_size.contents.value = self._defaults['FindRoute']['routeSpecSize']
        # path_capability
        if self._defaults['FindRoute']['pathCapability'] is None:
            raise MockFunctionCallError("niSE_FindRoute", param='pathCapability')
        if path_capability is not None:
            path_capability.contents.value = self._defaults['FindRoute']['pathCapability']
        if self._defaults['FindRoute']['routeSpec'] is None:
            raise MockFunctionCallError("niSE_FindRoute", param='routeSpec')
        if route_spec_size.value == 0:
            return len(self._defaults['FindRoute']['routeSpec'])
        try:
            route_spec_ref = route_spec.contents
        except AttributeError:
            route_spec_ref = route_spec
        for i in range(len(self._defaults['FindRoute']['routeSpec'])):
            route_spec_ref[i] = self._defaults['FindRoute']['routeSpec'][i]
        return self._defaults['FindRoute']['return']

    def niSE_GetAllConnections(self, session_handle, route_spec, route_spec_size):  # noqa: N802
        if self._defaults['GetAllConnections']['return'] != 0:
            return self._defaults['GetAllConnections']['return']
        # route_spec_size
        if self._defaults['GetAllConnections']['routeSpecSize'] is None:
            raise MockFunctionCallError("niSE_GetAllConnections", param='routeSpecSize')
        if route_spec_size is not None:
            route_spec_size.contents.value = self._defaults['GetAllConnections']['routeSpecSize']
        if self._defaults['GetAllConnections']['routeSpec'] is None:
            raise MockFunctionCallError("niSE_GetAllConnections", param='routeSpec')
        if route_spec_size.value == 0:
            return len(self._defaults['GetAllConnections']['routeSpec'])
        try:
            route_spec_ref = route_spec.contents
        except AttributeError:
            route_spec_ref = route_spec
        for i in range(len(self._defaults['GetAllConnections']['routeSpec'])):
            route_spec_ref[i] = self._defaults['GetAllConnections']['routeSpec'][i]
        return self._defaults['GetAllConnections']['return']

    def niSE_GetError(self, session_handle, error_number, error_description, error_description_size):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        # error_number
        if self._defaults['GetError']['errorNumber'] is None:
            raise MockFunctionCallError("niSE_GetError", param='errorNumber')
        if error_number is not None:
            error_number.contents.value = self._defaults['GetError']['errorNumber']
        # error_description_size
        if self._defaults['GetError']['errorDescriptionSize'] is None:
            raise MockFunctionCallError("niSE_GetError", param='errorDescriptionSize')
        if error_description_size is not None:
            error_description_size.contents.value = self._defaults['GetError']['errorDescriptionSize']
        if self._defaults['GetError']['errorDescription'] is None:
            raise MockFunctionCallError("niSE_GetError", param='errorDescription')
        if error_description_size.value == 0:
            return len(self._defaults['GetError']['errorDescription'])
        try:
            error_description_ref = error_description.contents
        except AttributeError:
            error_description_ref = error_description
        for i in range(len(self._defaults['GetError']['errorDescription'])):
            error_description_ref[i] = self._defaults['GetError']['errorDescription'][i]
        return self._defaults['GetError']['return']

    def niSE_GetIviDeviceSession(self, session_handle, ivi_logical_name, ivi_session_handle):  # noqa: N802
        if self._defaults['GetIviDeviceSession']['return'] != 0:
            return self._defaults['GetIviDeviceSession']['return']
        # ivi_session_handle
        if self._defaults['GetIviDeviceSession']['iviSessionHandle'] is None:
            raise MockFunctionCallError("niSE_GetIviDeviceSession", param='iviSessionHandle')
        if ivi_session_handle is not None:
            ivi_session_handle.contents.value = self._defaults['GetIviDeviceSession']['iviSessionHandle']
        return self._defaults['GetIviDeviceSession']['return']

    def niSE_IsConnected(self, session_handle, route_spec, is_connected):  # noqa: N802
        if self._defaults['IsConnected']['return'] != 0:
            return self._defaults['IsConnected']['return']
        # is_connected
        if self._defaults['IsConnected']['isConnected'] is None:
            raise MockFunctionCallError("niSE_IsConnected", param='isConnected')
        if is_connected is not None:
            is_connected.contents.value = self._defaults['IsConnected']['isConnected']
        return self._defaults['IsConnected']['return']

    def niSE_IsDebounced(self, session_handle, is_debounced):  # noqa: N802
        if self._defaults['IsDebounced']['return'] != 0:
            return self._defaults['IsDebounced']['return']
        # is_debounced
        if self._defaults['IsDebounced']['isDebounced'] is None:
            raise MockFunctionCallError("niSE_IsDebounced", param='isDebounced')
        if is_debounced is not None:
            is_debounced.contents.value = self._defaults['IsDebounced']['isDebounced']
        return self._defaults['IsDebounced']['return']

    def niSE_OpenSession(self, virtual_device_name, option_string, session_handle):  # noqa: N802
        if self._defaults['OpenSession']['return'] != 0:
            return self._defaults['OpenSession']['return']
        # session_handle
        if self._defaults['OpenSession']['sessionHandle'] is None:
            raise MockFunctionCallError("niSE_OpenSession", param='sessionHandle')
        if session_handle is not None:
            session_handle.contents.value = self._defaults['OpenSession']['sessionHandle']
        return self._defaults['OpenSession']['return']

    def niSE_WaitForDebounce(self, session_handle, maximum_time_ms):  # noqa: N802
        if self._defaults['WaitForDebounce']['return'] != 0:
            return self._defaults['WaitForDebounce']['return']
        return self._defaults['WaitForDebounce']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niSE_CloseSession.side_effect = MockFunctionCallError("niSE_CloseSession")
        mock_library.niSE_CloseSession.return_value = 0
        mock_library.niSE_Connect.side_effect = MockFunctionCallError("niSE_Connect")
        mock_library.niSE_Connect.return_value = 0
        mock_library.niSE_ConnectAndDisconnect.side_effect = MockFunctionCallError("niSE_ConnectAndDisconnect")
        mock_library.niSE_ConnectAndDisconnect.return_value = 0
        mock_library.niSE_Disconnect.side_effect = MockFunctionCallError("niSE_Disconnect")
        mock_library.niSE_Disconnect.return_value = 0
        mock_library.niSE_DisconnectAll.side_effect = MockFunctionCallError("niSE_DisconnectAll")
        mock_library.niSE_DisconnectAll.return_value = 0
        mock_library.niSE_ExpandRouteSpec.side_effect = MockFunctionCallError("niSE_ExpandRouteSpec")
        mock_library.niSE_ExpandRouteSpec.return_value = 0
        mock_library.niSE_FindRoute.side_effect = MockFunctionCallError("niSE_FindRoute")
        mock_library.niSE_FindRoute.return_value = 0
        mock_library.niSE_GetAllConnections.side_effect = MockFunctionCallError("niSE_GetAllConnections")
        mock_library.niSE_GetAllConnections.return_value = 0
        mock_library.niSE_GetError.side_effect = MockFunctionCallError("niSE_GetError")
        mock_library.niSE_GetError.return_value = 0
        mock_library.niSE_GetIviDeviceSession.side_effect = MockFunctionCallError("niSE_GetIviDeviceSession")
        mock_library.niSE_GetIviDeviceSession.return_value = 0
        mock_library.niSE_IsConnected.side_effect = MockFunctionCallError("niSE_IsConnected")
        mock_library.niSE_IsConnected.return_value = 0
        mock_library.niSE_IsDebounced.side_effect = MockFunctionCallError("niSE_IsDebounced")
        mock_library.niSE_IsDebounced.return_value = 0
        mock_library.niSE_OpenSession.side_effect = MockFunctionCallError("niSE_OpenSession")
        mock_library.niSE_OpenSession.return_value = 0
        mock_library.niSE_WaitForDebounce.side_effect = MockFunctionCallError("niSE_WaitForDebounce")
        mock_library.niSE_WaitForDebounce.return_value = 0
