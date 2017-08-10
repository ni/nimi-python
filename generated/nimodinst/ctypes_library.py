# This file was generated

# Python ctypes wrapper around driver DLL.
# ctypes is a library to manage calling into C/C++ DLLs. It will ensure the correct
#  number and types of parameters are passed into the different entry points

import ctypes
import threading

from nimodinst.ctypes_types import *  # noqa: F403,H303
import nimodinst.python_types


class NimodinstCtypesLibrary(object):
    def __init__(self, library_name, library_type):
        self._func_lock = threading.Lock()
        # We cache the cfunc object from the ctypes.CDLL object
        self.niModInst_CloseInstalledDevicesSession_cfunc = None
        self.niModInst_GetExtendedErrorInfo_cfunc = None
        self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc = None
        self.niModInst_GetInstalledDeviceAttributeViString_cfunc = None
        self.niModInst_OpenInstalledDevicesSession_cfunc = None

        if library_type == 'windll':
            self._library = ctypes.WinDLL(library_name)
        else:
            assert library_type == 'cdll'
            self._library = ctypes.CDLL(library_name)

    def niModInst_CloseInstalledDevicesSession(self, handle):  # noqa: N802
        with self._func_lock:
            if self.niModInst_CloseInstalledDevicesSession_cfunc is None:
                self.niModInst_CloseInstalledDevicesSession_cfunc = self._library.niModInst_CloseInstalledDevicesSession
                self.niModInst_CloseInstalledDevicesSession_cfunc.argtypes = [ViSession_ctype]  # noqa: F405
                self.niModInst_CloseInstalledDevicesSession_cfunc.restype = nimodinst.python_types.ViStatus
        return self.niModInst_CloseInstalledDevicesSession_cfunc(handle)

    def niModInst_GetExtendedErrorInfo(self, error_info_buffer_size, error_info):  # noqa: N802
        with self._func_lock:
            if self.niModInst_GetExtendedErrorInfo_cfunc is None:
                self.niModInst_GetExtendedErrorInfo_cfunc = self._library.niModInst_GetExtendedErrorInfo
                self.niModInst_GetExtendedErrorInfo_cfunc.argtypes = [ViInt32_ctype, ViString_ctype]  # noqa: F405
                self.niModInst_GetExtendedErrorInfo_cfunc.restype = nimodinst.python_types.ViStatus
        return self.niModInst_GetExtendedErrorInfo_cfunc(error_info_buffer_size, error_info)

    def niModInst_GetInstalledDeviceAttributeViInt32(self, handle, index, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc is None:
                self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc = self._library.niModInst_GetInstalledDeviceAttributeViInt32
                self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
                self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc.restype = nimodinst.python_types.ViStatus
        return self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc(handle, index, attribute_id, attribute_value)

    def niModInst_GetInstalledDeviceAttributeViString(self, handle, index, attribute_id, attribute_value_buffer_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niModInst_GetInstalledDeviceAttributeViString_cfunc is None:
                self.niModInst_GetInstalledDeviceAttributeViString_cfunc = self._library.niModInst_GetInstalledDeviceAttributeViString
                self.niModInst_GetInstalledDeviceAttributeViString_cfunc.argtypes = [ViSession_ctype, ViInt32_ctype, ViInt32_ctype, ViInt32_ctype, ViString_ctype]  # noqa: F405
                self.niModInst_GetInstalledDeviceAttributeViString_cfunc.restype = nimodinst.python_types.ViStatus
        return self.niModInst_GetInstalledDeviceAttributeViString_cfunc(handle, index, attribute_id, attribute_value_buffer_size, attribute_value)

    def niModInst_OpenInstalledDevicesSession(self, driver, handle, item_count):  # noqa: N802
        with self._func_lock:
            if self.niModInst_OpenInstalledDevicesSession_cfunc is None:
                self.niModInst_OpenInstalledDevicesSession_cfunc = self._library.niModInst_OpenInstalledDevicesSession
                self.niModInst_OpenInstalledDevicesSession_cfunc.argtypes = [ViConstString_ctype, ctypes.POINTER(ViSession_ctype), ctypes.POINTER(ViInt32_ctype)]  # noqa: F405
                self.niModInst_OpenInstalledDevicesSession_cfunc.restype = nimodinst.python_types.ViStatus
        return self.niModInst_OpenInstalledDevicesSession_cfunc(driver, handle, item_count)
