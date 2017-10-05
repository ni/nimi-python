# This file was generated

import ctypes
from nimodinst import errors
from nimodinst import library_singleton
from nimodinst import visatype


class AttributeViInt32(object):

    def __init__(self, owner, attribute_id, index):
        self._owner = owner
        self._index = index
        self._attribute_id = attribute_id

    def __getitem__(self, index):
        return self._owner._get_installed_device_attribute_vi_int32(self._owner._handle, self._index, self._attribute_id)


class AttributeViString(object):

    def __init__(self, owner, attribute_id, index):
        self._owner = owner
        self._index = index
        self._attribute_id = attribute_id

    def __getitem__(self, index):
        return self._owner._get_installed_device_attribute_vi_string(self._owner._handle, self._index, self._attribute_id)


class Device(object):

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

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
        self._is_frozen = True

    def __getattribute__(self, name):
        if name in ['_is_frozen', 'index']:
            return object.__getattribute__(self, name)
        else:
            return object.__getattribute__(self, name).__getitem__(None)

    def __setattr__(self, name, value):
        if self._is_frozen and name not in ['_is_frozen', 'index']:
            raise TypeError("%s is not writable" % name)
        object.__setattr__(self, name, value)


class Session(object):
    '''A NI-ModInst session to get device information'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    def __init__(self, driver):
        self._handle = 0
        self._item_count = 0
        self._current_item = 0
        self._library = library_singleton.get()
        self._handle, self._item_count = self._open_installed_devices_session(driver)

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
        # We hand-maintain the code that calls into self._library rather than leverage code-generation
        # because niModInst_GetExtendedErrorInfo() does not properly do the IVI-dance.
        # See https://github.com/ni/nimi-python/issues/166
        error_info_buffer_size = 0
        error_info_ctype = None
        error_code = self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size, error_info_ctype)
        if error_code <= 0:
            return "Failed to retrieve error description."
        error_info_buffer_size = error_code
        error_info_ctype = ctypes.create_string_buffer(error_info_buffer_size)
        # Note we don't look at the return value. This is intentional as niModInst returns the
        # original error code rather than 0 (VI_SUCCESS).
        self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size, error_info_ctype)
        return error_info_ctype.value.decode("ascii")

    # Iterator functions
    def __len__(self):
        return self._item_count

    def __iter__(self):
        self._current_item = 0
        return self

    def get_next(self):
        if self._current_item + 1 > self._item_count:
            raise StopIteration
        else:
            result = Device(self, self._current_item)
            self._current_item += 1
            return result

    def next(self):
        return self.get_next()

    def __next__(self):
        return self.get_next()

    def close(self):
        # TODO(marcoskirsch): Should we raise an exception on double close? Look at what File does.
        if(self._handle != 0):
            self._close_installed_devices_session(self._handle)
            self._handle = 0

    ''' These are code-generated '''

    def _close_installed_devices_session(self, handle):
        error_code = self._library.niModInst_CloseInstalledDevicesSession(self._handle)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _get_extended_error_info(self):
        error_info_buffer_size = 0
        error_info_ctype = None
        error_code = self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size, error_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        error_info_buffer_size = error_code
        error_info_ctype = ctypes.cast(ctypes.create_string_buffer(error_info_buffer_size), visatype.ViString)
        error_code = self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size, error_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_info_ctype.value.decode("ascii")

    def _get_installed_device_attribute_vi_int32(self, handle, index, attribute_id):
        attribute_value_ctype = visatype.ViInt32(0)
        error_code = self._library.niModInst_GetInstalledDeviceAttributeViInt32(self._handle, index, attribute_id, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_installed_device_attribute_vi_string(self, handle, index, attribute_id):
        attribute_value_buffer_size = 0
        attribute_value_ctype = None
        error_code = self._library.niModInst_GetInstalledDeviceAttributeViString(self._handle, index, attribute_id, attribute_value_buffer_size, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        attribute_value_buffer_size = error_code
        attribute_value_ctype = ctypes.cast(ctypes.create_string_buffer(attribute_value_buffer_size), visatype.ViString)
        error_code = self._library.niModInst_GetInstalledDeviceAttributeViString(self._handle, index, attribute_id, attribute_value_buffer_size, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode("ascii")

    def _open_installed_devices_session(self, driver):
        handle_ctype = visatype.ViSession(0)
        device_count_ctype = visatype.ViInt32(0)
        error_code = self._library.niModInst_OpenInstalledDevicesSession(driver.encode('ascii'), ctypes.pointer(handle_ctype), ctypes.pointer(device_count_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(handle_ctype.value), int(device_count_ctype.value)

