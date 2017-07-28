# This file was generated

import ctypes

import nimodinst.ctypes_types
import nimodinst.python_types


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
        self._defaults['OpenInstalledDevicesSession'] = {}
        self._defaults['OpenInstalledDevicesSession']['return'] = 0
        self._defaults['OpenInstalledDevicesSession']['handle'] = None
        self._defaults['OpenInstalledDevicesSession']['item_count'] = None
        self._defaults['GetInstalledDeviceAttributeViString'] = {}
        self._defaults['GetInstalledDeviceAttributeViString']['return'] = 0
        self._defaults['GetInstalledDeviceAttributeViString']['attributeValue'] = None
        self._defaults['GetInstalledDeviceAttributeViInt32'] = {}
        self._defaults['GetInstalledDeviceAttributeViInt32']['return'] = 0
        self._defaults['GetInstalledDeviceAttributeViInt32']['attributeValue'] = None
        self._defaults['CloseInstalledDevicesSession'] = {}
        self._defaults['CloseInstalledDevicesSession']['return'] = 0
        self._defaults['GetExtendedErrorInfo'] = {}
        self._defaults['GetExtendedErrorInfo']['return'] = 0
        self._defaults['GetExtendedErrorInfo']['errorInfo'] = None

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niModInst_OpenInstalledDevicesSession(self, driver, handle, item_count):  # noqa: N802
        if self._defaults['OpenInstalledDevicesSession']['handle'] is None:
            raise MockFunctionCallError("niModInst_OpenInstalledDevicesSession", param='handle')
        handle.contents.value = self._defaults['OpenInstalledDevicesSession']['handle']
        if self._defaults['OpenInstalledDevicesSession']['item_count'] is None:
            raise MockFunctionCallError("niModInst_OpenInstalledDevicesSession", param='item_count')
        item_count.contents.value = self._defaults['OpenInstalledDevicesSession']['item_count']
        return self._defaults['OpenInstalledDevicesSession']['return']

    def niModInst_GetInstalledDeviceAttributeViString(self, handle, index, attribute_id, attribute_value_buffer_size, attribute_value):  # noqa: N802
        if self._defaults['GetInstalledDeviceAttributeViString']['attributeValue'] is None:
            raise MockFunctionCallError("niModInst_GetInstalledDeviceAttributeViString", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetInstalledDeviceAttributeViString']['attributeValue']
        return self._defaults['GetInstalledDeviceAttributeViString']['return']

    def niModInst_GetInstalledDeviceAttributeViInt32(self, handle, index, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetInstalledDeviceAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niModInst_GetInstalledDeviceAttributeViInt32", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetInstalledDeviceAttributeViInt32']['attributeValue']
        return self._defaults['GetInstalledDeviceAttributeViInt32']['return']

    def niModInst_CloseInstalledDevicesSession(self, handle):  # noqa: N802
        return self._defaults['CloseInstalledDevicesSession']['return']

    def niModInst_GetExtendedErrorInfo(self, error_info_buffer_size, error_info):  # noqa: N802
        if self._defaults['GetExtendedErrorInfo']['errorInfo'] is None:
            raise MockFunctionCallError("niModInst_GetExtendedErrorInfo", param='errorInfo')
        error_info.contents.value = self._defaults['GetExtendedErrorInfo']['errorInfo']
        return self._defaults['GetExtendedErrorInfo']['return']

    # TODO(texasaggie97) Remove hand coded functions once metadata contains enough information to code generate these
    def niModInst_GetAttributeViString(self, vi, channel_name, attribute_id, buf_size, value):  # noqa: N802,F811
        if self._defaults['GetAttributeViString']['value'] is None:
            raise MockFunctionCallError("niDMM_GetAttributeViString", param='value')
        if buf_size == 0:
            return len(self._defaults['GetAttributeViString']['value'])
        t = nimodinst.ctypes_types.ViString_ctype(self._defaults['GetAttributeViString']['value'].encode('ascii'))
        value.value = ctypes.cast(t, nimodinst.ctypes_types.ViString_ctype).value
        return self._defaults['GetAttributeViString']['return']

    def niModInst_GetError(self, vi, error_code, buffer_size, description):  # noqa: N802,F811
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niDMM_GetError", param='errorCode')
        error_code.contents.value = self._defaults['GetError']['errorCode']
        if self._defaults['GetError']['description'] is None:
            raise MockFunctionCallError("niDMM_GetError", param='description')
        if buffer_size == 0:
            return len(self._defaults['GetError'][description])
        t = nimodinst.ctypes_types.ViString_ctype(self._defaults['GetError'][description].encode('ascii'))
        description.value = ctypes.cast(t, nimodinst.ctypes_types.ViString_ctype).value
        return self._defaults['GetError']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niModInst_OpenInstalledDevicesSession.side_effect = MockFunctionCallError("niModInst_OpenInstalledDevicesSession")
        mock_library.niModInst_OpenInstalledDevicesSession.return_value = nimodinst.python_types.ViStatus(0)
        mock_library.niModInst_GetInstalledDeviceAttributeViString.side_effect = MockFunctionCallError("niModInst_GetInstalledDeviceAttributeViString")
        mock_library.niModInst_GetInstalledDeviceAttributeViString.return_value = nimodinst.python_types.ViStatus(0)
        mock_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = MockFunctionCallError("niModInst_GetInstalledDeviceAttributeViInt32")
        mock_library.niModInst_GetInstalledDeviceAttributeViInt32.return_value = nimodinst.python_types.ViStatus(0)
        mock_library.niModInst_CloseInstalledDevicesSession.side_effect = MockFunctionCallError("niModInst_CloseInstalledDevicesSession")
        mock_library.niModInst_CloseInstalledDevicesSession.return_value = nimodinst.python_types.ViStatus(0)
        mock_library.niModInst_GetExtendedErrorInfo.side_effect = MockFunctionCallError("niModInst_GetExtendedErrorInfo")
        mock_library.niModInst_GetExtendedErrorInfo.return_value = nimodinst.python_types.ViStatus(0)
