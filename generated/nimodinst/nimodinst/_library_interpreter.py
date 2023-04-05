# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import nimodinst._library_singleton as _library_singleton
import nimodinst._visatype as _visatype
import nimodinst.errors as errors


# Helper functions for creating ctypes needed for calling into the driver DLL
def _get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
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


def _convert_to_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class LibraryInterpreter(object):
    '''Library C<->Python interpreter.

    This class is responsible for interpreting the Library's C API. It is responsible for:
    * Converting ctypes to native Python types.
    * Dealing with string encoding.
    * Allocating memory.
    * Converting errors returned by Library into Python exceptions.
    '''

    def __init__(self, encoding):
        self._encoding = encoding
        self._library = _library_singleton.get()
        # Initialize _handle to 0 for now.
        # Session will directly update it once the driver runtime init function has been called and
        # we have a valid session handle.
        self.set_session_handle()

    def set_session_handle(self, value=0):
        self._handle = value

    def get_session_handle(self):
        return self._handle

    def get_error_description(self, error_code):
        '''get_error_description

        Returns the error description.
        '''
        # We hand-maintain the code that calls into the cfunc rather than leverage code-generation
        # because niModInst_GetExtendedErrorInfo() does not properly do the IVI-dance.
        # See https://github.com/ni/nimi-python/issues/166
        error_info_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_info_ctype = None  # case C050
        error_code = self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size_ctype, error_info_ctype)
        if error_code <= 0:
            return 'Failed to retrieve error description.'
        error_info_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_info_ctype = (_visatype.ViChar * error_info_buffer_size_ctype.value)()  # case C060
        # Note we don't look at the return value. This is intentional as niModInst returns the
        # original error code rather than 0 (VI_SUCCESS).
        self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size_ctype, error_info_ctype)
        return error_info_ctype.value.decode("ascii")

    def close_installed_devices_session(self):  # noqa: N802
        handle_ctype = _visatype.ViSession(self._handle)  # case S110
        error_code = self._library.niModInst_CloseInstalledDevicesSession(handle_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def get_extended_error_info(self):  # noqa: N802
        error_info_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_info_ctype = None  # case C050
        error_code = self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size_ctype, error_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        error_info_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_info_ctype = (_visatype.ViChar * error_info_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size_ctype, error_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_info_ctype.value.decode(self._encoding)

    def get_installed_device_attribute_vi_int32(self, index, attribute_id):  # noqa: N802
        handle_ctype = _visatype.ViSession(self._handle)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        attribute_id_ctype = _visatype.ViInt32(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niModInst_GetInstalledDeviceAttributeViInt32(handle_ctype, index_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def get_installed_device_attribute_vi_string(self, index, attribute_id):  # noqa: N802
        handle_ctype = _visatype.ViSession(self._handle)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        attribute_id_ctype = _visatype.ViInt32(attribute_id)  # case S150
        attribute_value_buffer_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        error_code = self._library.niModInst_GetInstalledDeviceAttributeViString(handle_ctype, index_ctype, attribute_id_ctype, attribute_value_buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        attribute_value_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * attribute_value_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niModInst_GetInstalledDeviceAttributeViString(handle_ctype, index_ctype, attribute_id_ctype, attribute_value_buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def open_installed_devices_session(self, driver):  # noqa: N802
        driver_ctype = ctypes.create_string_buffer(driver.encode(self._encoding))  # case C020
        handle_ctype = _visatype.ViSession()  # case S220
        device_count_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niModInst_OpenInstalledDevicesSession(driver_ctype, None if handle_ctype is None else (ctypes.pointer(handle_ctype)), None if device_count_ctype is None else (ctypes.pointer(device_count_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(handle_ctype.value), int(device_count_ctype.value)
