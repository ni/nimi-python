# -*- coding: utf-8 -*-
# This file was generated

import array  # noqa: F401
import ctypes
import hightime
import nimodinst._converters as _converters
import nimodinst._visatype as _visatype
import nimodinst.errors as errors
import threading

from nimodinst._visatype import *  # noqa: F403,H303


# Helper functions for creating ctypes needed for calling into the driver DLL
def get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        return numpy.ctypeslib.as_ctypes(value)
    elif isinstance(value, bytes):
        return ctypes.cast(value, ctypes.POINTER(library_type))
    elif isinstance(value, list):
        assert library_type is not None, 'library_type is required for list'
        return (library_type * len(value))(*value)
    else:
        if library_type is not None and size is not None:
            return (library_type * size)()
        else:
            return None


def get_ctypes_and_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niModInst_CloseInstalledDevicesSession_cfunc = None
        self.niModInst_GetExtendedErrorInfo_cfunc = None
        self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc = None
        self.niModInst_GetInstalledDeviceAttributeViString_cfunc = None
        self.niModInst_OpenInstalledDevicesSession_cfunc = None

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

    def _get_error_description(self, session, error_code):
        '''_get_error_description

        Returns the error description.
        '''
        # We hand-maintain the code that calls into the cfunc rather than leverage code-generation
        # because niModInst_GetExtendedErrorInfo() does not properly do the IVI-dance.
        # See https://github.com/ni/nimi-python/issues/166
        error_info_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_info_ctype = None  # case C050
        with self._func_lock:
            if self.niModInst_GetExtendedErrorInfo_cfunc is None:
                self.niModInst_GetExtendedErrorInfo_cfunc = self._get_library_function('niModInst_GetExtendedErrorInfo')
                self.niModInst_GetExtendedErrorInfo_cfunc.argtypes = [ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niModInst_GetExtendedErrorInfo_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niModInst_GetExtendedErrorInfo_cfunc(error_info_buffer_size_ctype, error_info_ctype)
        if error_code <= 0:
            return 'Failed to retrieve error description.'
        error_info_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_info_ctype = (_visatype.ViChar * error_info_buffer_size_ctype.value)()  # case C060
        # Note we don't look at the return value. This is intentional as niModInst returns the
        # original error code rather than 0 (VI_SUCCESS).
        self.niModInst_GetExtendedErrorInfo_cfunc(error_info_buffer_size_ctype, error_info_ctype)
        return error_info_ctype.value.decode("ascii")

    def _close_installed_devices_session(self, session):  # noqa: N802
        handle_ctype = _visatype.ViSession(session._handle)  # case S110
        with self._func_lock:
            if self.niModInst_CloseInstalledDevicesSession_cfunc is None:
                self.niModInst_CloseInstalledDevicesSession_cfunc = self._get_library_function('niModInst_CloseInstalledDevicesSession')
                self.niModInst_CloseInstalledDevicesSession_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niModInst_CloseInstalledDevicesSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niModInst_CloseInstalledDevicesSession_cfunc(handle_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _get_extended_error_info(self, session):  # noqa: N802
        error_info_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_info_ctype = None  # case C050
        with self._func_lock:
            if self.niModInst_GetExtendedErrorInfo_cfunc is None:
                self.niModInst_GetExtendedErrorInfo_cfunc = self._get_library_function('niModInst_GetExtendedErrorInfo')
                self.niModInst_GetExtendedErrorInfo_cfunc.argtypes = [ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niModInst_GetExtendedErrorInfo_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niModInst_GetExtendedErrorInfo_cfunc(error_info_buffer_size_ctype, error_info_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=True)
        error_info_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_info_ctype = (_visatype.ViChar * error_info_buffer_size_ctype.value)()  # case C060
        error_code = self.niModInst_GetExtendedErrorInfo_cfunc(error_info_buffer_size_ctype, error_info_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=True)
        return error_info_ctype.value.decode(session._encoding)

    def _get_installed_device_attribute_vi_int32(self, session, index, attribute_id):  # noqa: N802
        handle_ctype = _visatype.ViSession(session._handle)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        attribute_id_ctype = _visatype.ViInt32(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc is None:
                self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc = self._get_library_function('niModInst_GetInstalledDeviceAttributeViInt32')
                self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc(handle_ctype, index_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_installed_device_attribute_vi_string(self, session, index, attribute_id):  # noqa: N802
        handle_ctype = _visatype.ViSession(session._handle)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        attribute_id_ctype = _visatype.ViInt32(attribute_id)  # case S150
        attribute_value_buffer_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        with self._func_lock:
            if self.niModInst_GetInstalledDeviceAttributeViString_cfunc is None:
                self.niModInst_GetInstalledDeviceAttributeViString_cfunc = self._get_library_function('niModInst_GetInstalledDeviceAttributeViString')
                self.niModInst_GetInstalledDeviceAttributeViString_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niModInst_GetInstalledDeviceAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niModInst_GetInstalledDeviceAttributeViString_cfunc(handle_ctype, index_ctype, attribute_id_ctype, attribute_value_buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=True, is_error_handling=False)
        attribute_value_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * attribute_value_buffer_size_ctype.value)()  # case C060
        error_code = self.niModInst_GetInstalledDeviceAttributeViString_cfunc(handle_ctype, index_ctype, attribute_id_ctype, attribute_value_buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(session._encoding)

    def _open_installed_devices_session(self, session, driver):  # noqa: N802
        driver_ctype = ctypes.create_string_buffer(driver.encode(session._encoding))  # case C020
        handle_ctype = _visatype.ViSession()  # case S220
        device_count_ctype = _visatype.ViInt32()  # case S220
        with self._func_lock:
            if self.niModInst_OpenInstalledDevicesSession_cfunc is None:
                self.niModInst_OpenInstalledDevicesSession_cfunc = self._get_library_function('niModInst_OpenInstalledDevicesSession')
                self.niModInst_OpenInstalledDevicesSession_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViSession), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niModInst_OpenInstalledDevicesSession_cfunc.restype = ViStatus  # noqa: F405
        error_code = self.niModInst_OpenInstalledDevicesSession_cfunc(driver_ctype, None if handle_ctype is None else (ctypes.pointer(handle_ctype)), None if device_count_ctype is None else (ctypes.pointer(device_count_ctype)))
        errors.handle_error(self, session, error_code, ignore_warnings=False, is_error_handling=False)
        return int(handle_ctype.value), int(device_count_ctype.value)
