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
        self._defaults['ExpandRouteSpec']['expandedRouteSpec'] = None
        self._defaults['FindRoute'] = {}
        self._defaults['FindRoute']['return'] = 0
        self._defaults['FindRoute']['routeSpec'] = None
        self._defaults['FindRoute']['pathCapability'] = None
        self._defaults['GetAllConnections'] = {}
        self._defaults['GetAllConnections']['return'] = 0
        self._defaults['GetAllConnections']['routeSpec'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorNumber'] = None
        self._defaults['GetError']['errorDescription'] = None
        self._defaults['IsConnected'] = {}
        self._defaults['IsConnected']['return'] = 0
        self._defaults['IsConnected']['isConnected'] = None
        self._defaults['IsDebounced'] = {}
        self._defaults['IsDebounced']['return'] = 0
        self._defaults['IsDebounced']['isDebounced'] = None
        self._defaults['OpenSession'] = {}
        self._defaults['OpenSession']['return'] = 0
        self._defaults['OpenSession']['vi'] = None
        self._defaults['WaitForDebounce'] = {}
        self._defaults['WaitForDebounce']['return'] = 0

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niSE_CloseSession(self, vi):  # noqa: N802
        if self._defaults['CloseSession']['return'] != 0:
            return self._defaults['CloseSession']['return']
        return self._defaults['CloseSession']['return']

    def niSE_Connect(self, vi, connect_spec, multiconnect_mode, wait_for_debounce):  # noqa: N802
        if self._defaults['Connect']['return'] != 0:
            return self._defaults['Connect']['return']
        return self._defaults['Connect']['return']

    def niSE_ConnectAndDisconnect(self, vi, connect_spec, disconnect_spec, multiconnect_mode, operation_order, wait_for_debounce):  # noqa: N802
        if self._defaults['ConnectAndDisconnect']['return'] != 0:
            return self._defaults['ConnectAndDisconnect']['return']
        return self._defaults['ConnectAndDisconnect']['return']

    def niSE_Disconnect(self, vi, disconnect_spec):  # noqa: N802
        if self._defaults['Disconnect']['return'] != 0:
            return self._defaults['Disconnect']['return']
        return self._defaults['Disconnect']['return']

    def niSE_DisconnectAll(self, vi):  # noqa: N802
        if self._defaults['DisconnectAll']['return'] != 0:
            return self._defaults['DisconnectAll']['return']
        return self._defaults['DisconnectAll']['return']

    def niSE_ExpandRouteSpec(self, vi, route_spec, expand_action, expanded_route_spec, expanded_route_spec_size):  # noqa: N802
        if self._defaults['ExpandRouteSpec']['return'] != 0:
            return self._defaults['ExpandRouteSpec']['return']
        # expanded_route_spec
        if self._defaults['ExpandRouteSpec']['expandedRouteSpec'] is None:
            raise MockFunctionCallError("niSE_ExpandRouteSpec", param='expandedRouteSpec')
        test_value = self._defaults['ExpandRouteSpec']['expandedRouteSpec']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(expanded_route_spec) >= len(test_value)
        for i in range(len(test_value)):
            expanded_route_spec[i] = test_value[i]
        return self._defaults['ExpandRouteSpec']['return']

    def niSE_FindRoute(self, vi, channel1, channel2, route_spec, route_spec_size, path_capability):  # noqa: N802
        if self._defaults['FindRoute']['return'] != 0:
            return self._defaults['FindRoute']['return']
        # route_spec
        if self._defaults['FindRoute']['routeSpec'] is None:
            raise MockFunctionCallError("niSE_FindRoute", param='routeSpec')
        test_value = self._defaults['FindRoute']['routeSpec']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(route_spec) >= len(test_value)
        for i in range(len(test_value)):
            route_spec[i] = test_value[i]
        # path_capability
        if self._defaults['FindRoute']['pathCapability'] is None:
            raise MockFunctionCallError("niSE_FindRoute", param='pathCapability')
        if path_capability is not None:
            path_capability.contents.value = self._defaults['FindRoute']['pathCapability']
        return self._defaults['FindRoute']['return']

    def niSE_GetAllConnections(self, vi, route_spec, route_spec_size):  # noqa: N802
        if self._defaults['GetAllConnections']['return'] != 0:
            return self._defaults['GetAllConnections']['return']
        # route_spec
        if self._defaults['GetAllConnections']['routeSpec'] is None:
            raise MockFunctionCallError("niSE_GetAllConnections", param='routeSpec')
        test_value = self._defaults['GetAllConnections']['routeSpec']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(route_spec) >= len(test_value)
        for i in range(len(test_value)):
            route_spec[i] = test_value[i]
        return self._defaults['GetAllConnections']['return']

    def niSE_GetError(self, vi, error_number, error_description, error_description_size):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        # error_number
        if self._defaults['GetError']['errorNumber'] is None:
            raise MockFunctionCallError("niSE_GetError", param='errorNumber')
        if error_number is not None:
            error_number.contents.value = self._defaults['GetError']['errorNumber']
        # error_description
        if self._defaults['GetError']['errorDescription'] is None:
            raise MockFunctionCallError("niSE_GetError", param='errorDescription')
        test_value = self._defaults['GetError']['errorDescription']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(error_description) >= len(test_value)
        for i in range(len(test_value)):
            error_description[i] = test_value[i]
        return self._defaults['GetError']['return']

    def niSE_IsConnected(self, vi, route_spec, is_connected):  # noqa: N802
        if self._defaults['IsConnected']['return'] != 0:
            return self._defaults['IsConnected']['return']
        # is_connected
        if self._defaults['IsConnected']['isConnected'] is None:
            raise MockFunctionCallError("niSE_IsConnected", param='isConnected')
        if is_connected is not None:
            is_connected.contents.value = self._defaults['IsConnected']['isConnected']
        return self._defaults['IsConnected']['return']

    def niSE_IsDebounced(self, vi, is_debounced):  # noqa: N802
        if self._defaults['IsDebounced']['return'] != 0:
            return self._defaults['IsDebounced']['return']
        # is_debounced
        if self._defaults['IsDebounced']['isDebounced'] is None:
            raise MockFunctionCallError("niSE_IsDebounced", param='isDebounced')
        if is_debounced is not None:
            is_debounced.contents.value = self._defaults['IsDebounced']['isDebounced']
        return self._defaults['IsDebounced']['return']

    def niSE_OpenSession(self, virtual_device_name, option_string, vi):  # noqa: N802
        if self._defaults['OpenSession']['return'] != 0:
            return self._defaults['OpenSession']['return']
        # vi
        if self._defaults['OpenSession']['vi'] is None:
            raise MockFunctionCallError("niSE_OpenSession", param='vi')
        if vi is not None:
            vi.contents.value = self._defaults['OpenSession']['vi']
        return self._defaults['OpenSession']['return']

    def niSE_WaitForDebounce(self, vi, maximum_time_ms):  # noqa: N802
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
        mock_library.niSE_IsConnected.side_effect = MockFunctionCallError("niSE_IsConnected")
        mock_library.niSE_IsConnected.return_value = 0
        mock_library.niSE_IsDebounced.side_effect = MockFunctionCallError("niSE_IsDebounced")
        mock_library.niSE_IsDebounced.return_value = 0
        mock_library.niSE_OpenSession.side_effect = MockFunctionCallError("niSE_OpenSession")
        mock_library.niSE_OpenSession.return_value = 0
        mock_library.niSE_WaitForDebounce.side_effect = MockFunctionCallError("niSE_WaitForDebounce")
        mock_library.niSE_WaitForDebounce.return_value = 0
