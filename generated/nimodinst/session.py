# This file was generated

import ctypes
from nimodinst import ctypes_types
from nimodinst import errors
from nimodinst import library


class AttributeViInt32(object):

    def __init__(self, owner, attribute_id, index=None):
        self._owner = owner
        self._index = index
        self._attribute_id = attribute_id

    def __getitem__(self, index):
        i = self._index if self._index is not None else index
        return self._owner._get_installed_device_attribute_vi_int32(i, self._attribute_id)

    def __format__(self, format_spec):
        return format(self._owner._get_installed_device_attribute_vi_int32(self._index, self._attribute_id), format_spec)


class AttributeViString(object):

    def __init__(self, owner, attribute_id, index=None):
        self._owner = owner
        self._index = index
        self._attribute_id = attribute_id

    def __getitem__(self, index):
        i = self._index if self._index is not None else index
        return self._owner._get_installed_device_attribute_vi_string(i, self._attribute_id)

    def __format__(self, format_spec):
        return format(self._owner._get_installed_device_attribute_vi_string(self._index, self._attribute_id), format_spec)


class Device(object):

    def __init__(self, owner, index):
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


class Session(object):
    '''A NI-ModInst session to get device information'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    def __init__(self, driver):
        self.bus_number = AttributeViInt32(self, 12)
        '''
        The bus on which the device has been enumerated.
        '''
        self.chassis_number = AttributeViInt32(self, 11)
        '''
        The number of the chassis in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.
        '''
        self.device_model = AttributeViString(self, 1)
        '''
        The model of the device (for example, NI PXI-5122)
        '''
        self.device_name = AttributeViString(self, 0)
        '''
        The name of the device, which can be used to open an instrument driver session for that device
        '''
        self.max_pciexpress_link_width = AttributeViInt32(self, 18)
        '''
        **MAX_PCIEXPRESS_LINK_WIDTH**
        '''
        self.pciexpress_link_width = AttributeViInt32(self, 17)
        '''
        **PCIEXPRESS_LINK_WIDTH**
        '''
        self.serial_number = AttributeViString(self, 2)
        '''
        The serial number of the device
        '''
        self.slot_number = AttributeViInt32(self, 10)
        '''
        The slot (for example, in a PXI chassis) in which the device is installed. This attribute can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.
        '''
        self.socket_number = AttributeViInt32(self, 13)
        '''
        The socket number on which the device has been enumerated
        '''

        self.handle = 0
        self.item_count = 0
        self.current_item = 0
        self.library = library.get_library()
        self.handle, self.item_count = self._open_installed_devices_session(driver)

        self._is_frozen = True

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise TypeError("%r is a frozen class" % self)
        object.__setattr__(self, key, value)

    def __del__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    # method needed for generic driver exceptions
    # TODO(texasaggie97) Rewrite to use session function instead of library once buffer
    #   retrieval is working
    def _get_error_description(self, error_code):
        buffer_size = library.niModInst_GetExtendedErrorInfo(0, None)

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
            library.niModInst_GetExtendedErrorInfo(buffer_size, error_message)

        # TODO(marcoskirsch): By hardcoding encoding "ascii", internationalized strings will throw.
        #       Which encoding should we be using? https://docs.python.org/3/library/codecs.html#standard-encodings
        return error_code, error_message.value.decode("ascii")

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
        error_code = self.library.niModInst_CloseInstalledDevicesSession(handle)
        errors._handle_error(self, error_code)
        return

    def get_extended_error_info(self, error_info_buffer_size):
        error_info_ctype = ctypes_types.ViChar_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        error_code = self.library.niModInst_GetExtendedErrorInfo(error_info_buffer_size, ctypes.pointer(error_info_ctype))
        errors._handle_error(self, error_code)
        return error_info_ctype.value.decode("ascii")

    def _get_installed_device_attribute_vi_int32(self, handle, index, attribute_id):
        attribute_value_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niModInst_GetInstalledDeviceAttributeViInt32(handle, index, attribute_id, ctypes.pointer(attribute_value_ctype))
        errors._handle_error(self, error_code)
        return attribute_value_ctype.value

    def _get_installed_device_attribute_vi_string(self, handle, index, attribute_id, attribute_value_buffer_size):
        attribute_value_ctype = ctypes_types.ViChar_ctype(0)  # TODO(marcoskirsch): allocate a buffer
        error_code = self.library.niModInst_GetInstalledDeviceAttributeViString(handle, index, attribute_id, attribute_value_buffer_size, ctypes.pointer(attribute_value_ctype))
        errors._handle_error(self, error_code)
        return attribute_value_ctype.value.decode("ascii")

    def _open_installed_devices_session(self, driver):
        handle_ctype = ctypes_types.ViSession_ctype(0)
        item_count_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niModInst_OpenInstalledDevicesSession(driver.encode('ascii'), ctypes.pointer(handle_ctype), ctypes.pointer(item_count_ctype))
        errors._handle_error(self, error_code)
        return handle_ctype.value, item_count_ctype.value

    ''' These are temporarily hand-coded because the generator can't handle buffers yet '''

    def _get_installed_device_attribute_vi_string(self, index, attribute_id):  # noqa: F811
        # Do the IVI dance
        # Don't use _handle_error, because positive value in error_code means size, not warning.
        buffer_size = 0
        value_ctype = ctypes.create_string_buffer(buffer_size)
        error_code = self.library.niModInst_GetInstalledDeviceAttributeViString(self.handle, index, attribute_id, buffer_size, ctypes.cast(value_ctype, ctypes.POINTER(ctypes_types.ViChar_ctype)))
        if(errors._is_error(error_code)):
            raise errors.Error(self, error_code)
        buffer_size = error_code
        value_ctype = ctypes.create_string_buffer(buffer_size)
        error_code = self.library.niModInst_GetInstalledDeviceAttributeViString(self.handle, index, attribute_id, buffer_size, ctypes.cast(value_ctype, ctypes.POINTER(ctypes_types.ViChar_ctype)))
        errors._handle_error(self, error_code)
        return value_ctype.value.decode("ascii")
