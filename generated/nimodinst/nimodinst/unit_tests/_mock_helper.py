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
        self._defaults['CloseInstalledDevicesSession'] = {}
        self._defaults['CloseInstalledDevicesSession']['return'] = 0
        self._defaults['GetExtendedErrorInfo'] = {}
        self._defaults['GetExtendedErrorInfo']['return'] = 0
        self._defaults['GetExtendedErrorInfo']['errorInfo'] = None
        self._defaults['GetInstalledDeviceAttributeViInt32'] = {}
        self._defaults['GetInstalledDeviceAttributeViInt32']['return'] = 0
        self._defaults['GetInstalledDeviceAttributeViInt32']['attributeValue'] = None
        self._defaults['GetInstalledDeviceAttributeViString'] = {}
        self._defaults['GetInstalledDeviceAttributeViString']['return'] = 0
        self._defaults['GetInstalledDeviceAttributeViString']['attributeValue'] = None
        self._defaults['OpenInstalledDevicesSession'] = {}
        self._defaults['OpenInstalledDevicesSession']['return'] = 0
        self._defaults['OpenInstalledDevicesSession']['handle'] = None
        self._defaults['OpenInstalledDevicesSession']['deviceCount'] = None

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niModInst_CloseInstalledDevicesSession(self, handle):  # noqa: N802
        if self._defaults['CloseInstalledDevicesSession']['return'] != 0:
            return self._defaults['CloseInstalledDevicesSession']['return']
        return self._defaults['CloseInstalledDevicesSession']['return']

    def niModInst_GetExtendedErrorInfo(self, error_info_buffer_size, error_info):  # noqa: N802
        if self._defaults['GetExtendedErrorInfo']['return'] != 0:
            return self._defaults['GetExtendedErrorInfo']['return']
        if self._defaults['GetExtendedErrorInfo']['errorInfo'] is None:
            raise MockFunctionCallError("niModInst_GetExtendedErrorInfo", param='errorInfo')
        if error_info_buffer_size.value == 0:
            return len(self._defaults['GetExtendedErrorInfo']['errorInfo'])
        error_info.value = self._defaults['GetExtendedErrorInfo']['errorInfo'].encode('ascii')
        return self._defaults['GetExtendedErrorInfo']['return']

    def niModInst_GetInstalledDeviceAttributeViInt32(self, handle, index, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetInstalledDeviceAttributeViInt32']['return'] != 0:
            return self._defaults['GetInstalledDeviceAttributeViInt32']['return']
        # attribute_value
        if self._defaults['GetInstalledDeviceAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niModInst_GetInstalledDeviceAttributeViInt32", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetInstalledDeviceAttributeViInt32']['attributeValue']
        return self._defaults['GetInstalledDeviceAttributeViInt32']['return']

    def niModInst_GetInstalledDeviceAttributeViString(self, handle, index, attribute_id, attribute_value_buffer_size, attribute_value):  # noqa: N802
        if self._defaults['GetInstalledDeviceAttributeViString']['return'] != 0:
            return self._defaults['GetInstalledDeviceAttributeViString']['return']
        if self._defaults['GetInstalledDeviceAttributeViString']['attributeValue'] is None:
            raise MockFunctionCallError("niModInst_GetInstalledDeviceAttributeViString", param='attributeValue')
        if attribute_value_buffer_size.value == 0:
            return len(self._defaults['GetInstalledDeviceAttributeViString']['attributeValue'])
        attribute_value.value = self._defaults['GetInstalledDeviceAttributeViString']['attributeValue'].encode('ascii')
        return self._defaults['GetInstalledDeviceAttributeViString']['return']

    def niModInst_OpenInstalledDevicesSession(self, driver, handle, device_count):  # noqa: N802
        if self._defaults['OpenInstalledDevicesSession']['return'] != 0:
            return self._defaults['OpenInstalledDevicesSession']['return']
        # handle
        if self._defaults['OpenInstalledDevicesSession']['handle'] is None:
            raise MockFunctionCallError("niModInst_OpenInstalledDevicesSession", param='handle')
        if handle is not None:
            handle.contents.value = self._defaults['OpenInstalledDevicesSession']['handle']
        # device_count
        if self._defaults['OpenInstalledDevicesSession']['deviceCount'] is None:
            raise MockFunctionCallError("niModInst_OpenInstalledDevicesSession", param='deviceCount')
        if device_count is not None:
            device_count.contents.value = self._defaults['OpenInstalledDevicesSession']['deviceCount']
        return self._defaults['OpenInstalledDevicesSession']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niModInst_CloseInstalledDevicesSession.side_effect = MockFunctionCallError("niModInst_CloseInstalledDevicesSession")
        mock_library.niModInst_CloseInstalledDevicesSession.return_value = 0
        mock_library.niModInst_GetExtendedErrorInfo.side_effect = MockFunctionCallError("niModInst_GetExtendedErrorInfo")
        mock_library.niModInst_GetExtendedErrorInfo.return_value = 0
        mock_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = MockFunctionCallError("niModInst_GetInstalledDeviceAttributeViInt32")
        mock_library.niModInst_GetInstalledDeviceAttributeViInt32.return_value = 0
        mock_library.niModInst_GetInstalledDeviceAttributeViString.side_effect = MockFunctionCallError("niModInst_GetInstalledDeviceAttributeViString")
        mock_library.niModInst_GetInstalledDeviceAttributeViString.return_value = 0
        mock_library.niModInst_OpenInstalledDevicesSession.side_effect = MockFunctionCallError("niModInst_OpenInstalledDevicesSession")
        mock_library.niModInst_OpenInstalledDevicesSession.return_value = 0
