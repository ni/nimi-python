# This file was generated

import ctypes
from nimodinst import ctypes_types
from nimodinst import errors
from nimodinst import library_singleton
from nimodinst import python_types


class AttributeViInt32(object):

    def __init__(self, owner, attribute_id, index):
        self._owner = owner
        self._index = index
        self._attribute_id = attribute_id

    def __getitem__(self, index):
        return self._owner._get_installed_device_attribute_vi_int32(self._owner.handle, self._index, self._attribute_id)

    def __format__(self, format_spec):
        return format(self._owner._get_installed_device_attribute_vi_int32(self._owner.handle, self._index, self._attribute_id), format_spec)


class AttributeViString(object):

    def __init__(self, owner, attribute_id, index):
        self._owner = owner
        self._index = index
        self._attribute_id = attribute_id

    def __getitem__(self, index):
        return self._owner._get_installed_device_attribute_vi_string(self._owner.handle, self._index, self._attribute_id)

    def __format__(self, format_spec):
        return format(self._owner._get_installed_device_attribute_vi_string(self._owner.handle, self._index, self._attribute_id), format_spec)


class Device(object):

    def __init__(self, owner, index):
        self._index = index
        self.bus_number = AttributeViInt32(owner, 12, index=index)
        '''
        The bus on which the device has been enumerated.
        '''
        self.chassis_number = AttributeViInt32(owner, 11, index=index)
        '''
        The number of the chassis in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.
        '''
        self.device_model = AttributeViString(owner, 1, index=index)
        '''
        The model of the device (for example, NI PXI-5122)
        '''
        self.device_name = AttributeViString(owner, 0, index=index)
        '''
        The name of the device, which can be used to open an instrument driver session for that device
        '''
        self.max_pciexpress_link_width = AttributeViInt32(owner, 18, index=index)
        '''
        **MAX_PCIEXPRESS_LINK_WIDTH**
        '''
        self.pciexpress_link_width = AttributeViInt32(owner, 17, index=index)
        '''
        **PCIEXPRESS_LINK_WIDTH**
        '''
        self.serial_number = AttributeViString(owner, 2, index=index)
        '''
        The serial number of the device
        '''
        self.slot_number = AttributeViInt32(owner, 10, index=index)
        '''
        The slot (for example, in a PXI chassis) in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.
        '''
        self.socket_number = AttributeViInt32(owner, 13, index=index)
        '''
        The socket number on which the device has been enumerated
        '''

    def __getattribute__(self, name):
        return object.__getattribute__(self, name).__getitem__(None)


class Session(object):
    '''A NI-ModInst session to get device information'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    def __init__(self, driver):
        self.handle = 0
        self.item_count = 0
        self.current_item = 0
        self.library = library_singleton.get()
        self.handle, self.item_count = self._open_installed_devices_session(driver)

        self._is_frozen = True

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise TypeError("%r is a frozen class" % self)
        object.__setattr__(self, key, value)

    def __getitem__(self, index):
        return Device(self, index)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def get_error_description(self, error_code):
        '''get_error_description

        Returns the error description.
        '''
        # TODO(texasaggie97) Rewrite to use code generated method, if possible.
        buffer_size = self.library.niModInst_GetExtendedErrorInfo(0, None)

        if (buffer_size > 0):
            '''
            Return code > 0 from first call to GetError represents the size of
            the description.  Call it again.
            Ignore incoming IVI error code and return description from the driver
            (trust that the IVI error code was properly stored in the session
            by the driver)
            '''
            error_code = ctypes_types.ViStatus_ctype(error_code)
            error_message = ctypes.create_string_buffer(buffer_size)
            self.library.niModInst_GetExtendedErrorInfo(buffer_size, error_message)

        # TODO(marcoskirsch): By hardcoding encoding "ascii", internationalized strings will throw.
        #       Which encoding should we be using? https://docs.python.org/3/library/codecs.html#standard-encodings
        return error_message.value.decode("ascii")

    # Iterator functions
    def __len__(self):
        return self.item_count

    def __iter__(self):
        self.current_item = 0
        return self

    def get_next(self):
        if self.current_item + 1 > self.item_count:
            raise StopIteration
        else:
            result = Device(self, self.current_item)
            self.current_item += 1
            return result

    def next(self):
        return self.get_next()

    def __next__(self):
        return self.get_next()

    def close(self):
        # TODO(marcoskirsch): Should we raise an exception on double close? Look at what File does.
        if(self.handle != 0):
            self._close_installed_devices_session(self.handle)
            self.handle = 0

    ''' These are code-generated '''

    def _close_installed_devices_session(self, handle):
        error_code = self.library.niModInst_CloseInstalledDevicesSession(self.handle)
        errors.handle_error(self, error_code, ignore_warnings=False)
        return

    def _get_extended_error_info(self):
        error_info_buffer_size = 0
        error_info_ctype = ctypes.cast(ctypes.create_string_buffer(error_info_buffer_size), ctypes_types.ViString_ctype)
        error_code = self.library.niModInst_GetExtendedErrorInfo(error_info_buffer_size, error_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True)
        error_info_buffer_size = error_code
        error_info_ctype = ctypes.cast(ctypes.create_string_buffer(error_info_buffer_size), ctypes_types.ViString_ctype)
        error_code = self.library.niModInst_GetExtendedErrorInfo(error_info_buffer_size, error_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False)
        return error_info_ctype.value.decode("ascii")

    def _get_installed_device_attribute_vi_int32(self, handle, index, attribute_id):
        attribute_value_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niModInst_GetInstalledDeviceAttributeViInt32(self.handle, index, attribute_id, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False)
        return python_types.ViInt32(attribute_value_ctype.value)

    def _get_installed_device_attribute_vi_string(self, handle, index, attribute_id):
        attribute_value_buffer_size = 0
        attribute_value_ctype = ctypes.cast(ctypes.create_string_buffer(attribute_value_buffer_size), ctypes_types.ViString_ctype)
        error_code = self.library.niModInst_GetInstalledDeviceAttributeViString(self.handle, index, attribute_id, attribute_value_buffer_size, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True)
        attribute_value_buffer_size = error_code
        attribute_value_ctype = ctypes.cast(ctypes.create_string_buffer(attribute_value_buffer_size), ctypes_types.ViString_ctype)
        error_code = self.library.niModInst_GetInstalledDeviceAttributeViString(self.handle, index, attribute_id, attribute_value_buffer_size, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False)
        return attribute_value_ctype.value.decode("ascii")

    def _open_installed_devices_session(self, driver):
        handle_ctype = ctypes_types.ViSession_ctype(0)
        device_count_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niModInst_OpenInstalledDevicesSession(driver.encode('ascii'), ctypes.pointer(handle_ctype), ctypes.pointer(device_count_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False)
        return python_types.ViSession(handle_ctype.value), python_types.ViInt32(device_count_ctype.value)

