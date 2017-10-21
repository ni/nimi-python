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
        return self._owner._get_installed_device_attribute_vi_int32(self._index, self._attribute_id)


class AttributeViString(object):

    def __init__(self, owner, attribute_id, index):
        self._owner = owner
        self._index = index
        self._attribute_id = attribute_id

    def __getitem__(self, index):
        return self._owner._get_installed_device_attribute_vi_string(self._index, self._attribute_id)


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
        if self._is_frozen:
            raise AttributeError("__setattr__ not supported.")
        object.__setattr__(self, name, value)


class Session(object):
    '''A NI-ModInst session to get device information'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    def __init__(self, driver):
        self._handle = 0
        self._item_count = 0
        self._current_item = 0
        self._encoding = 'windows-1251'
        self._library = library_singleton.get()
        self._handle, self._item_count = self._open_installed_devices_session(driver)

        self._is_frozen = True

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("__setattr__ not supported.")
        object.__setattr__(self, key, value)

    def __getitem__(self, index):
        return Device(self, index)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def _get_error_description(self, error_code):
        '''_get_error_description

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
            self._close_installed_devices_session()
            self._handle = 0

    ''' These are code-generated '''

    def _close_installed_devices_session(self):
        '''_close_installed_devices_session

        Cleans up the NI-ModInst session created by a call to
        _open_installed_devices_session. Call this function when you are
        finished using the session handle and do not use this handle again.
        '''
        handle_ctype = visatype.ViSession(self._handle)  # case 1
        error_code = self._library.niModInst_CloseInstalledDevicesSession(handle_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _get_extended_error_info(self):
        '''_get_extended_error_info

        Returns detailed information about the last error that occurred in the
        current thread during a call to one of the NI-ModInst functions. When
        one of the other functions returns a negative value as its return value,
        immediately call this function to get detailed information about the
        error. Because error information is stored on a thread-by-thread basis,
        be sure to call this function in the same thread that called the
        function that returned an error. The extended error information is
        returned as a string. To find out the length of the error information
        string before you allocate a buffer for it, call this function and pass
        0 as the errorInfoBufferSize parameter or NULL as the errorInfo
        parameter. When you do this, the function returns the size of the buffer
        required to hold the error information string as its return value. You
        can then allocate an appropriately sized string character buffer and
        call this function again.

        Args:
            error_info_buffer_size (int): The size of the buffer allocated and passed in as the errorInfo
                parameter. The buffer should be large enough to hold the errorInfo
                string (including a NULL terminating character). The size of the buffer
                allocated and passed in as the errorInfo parameter. The buffer should be
                large enough to hold the errorInfo string (including a NULL terminating
                character). Refer to the function help to find out how to determine the
                exact buffer size required.
        '''
        error_info_buffer_size_ctype = visatype.ViInt32()  # case 5
        error_info_ctype = None  # case 9
        error_code = self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size_ctype, error_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        error_info_buffer_size_ctype = visatype.ViInt32(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_info_ctype = (visatype.ViChar * error_info_buffer_size_ctype.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_code = self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size_ctype, error_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_info_ctype.value.decode(self._encoding)

    def _get_installed_device_attribute_vi_int32(self, index, attribute_id):
        '''_get_installed_device_attribute_vi_int32

        Returns an integer attribute specified by the attributeID parameter for
        a device specified by the handle and index parameters. The handle
        parameter is expected to be a valid handle returned by
        _open_installed_devices_session. It therefore acts as a handle to
        a list of installed devices. The index parameter specifies the device in
        the list for which you want the attribute.

        Args:
            index (int): A zero-based index that specifies the device for which you want the
                attribute. This index parameter should be between 0 and (deviceCount -
                1), inclusive, where deviceCount is the number of installed devices
                returned by _open_installed_devices_session.
            attribute_id (int): The ID of the integer attribute you want to query. Valid Values Slot
                Number--the slot (for example, in a PXI chassis) in which the device is
                installed. This attribute can only be queried for PXI devices installed
                in a chassis that has been properly identified in MAX. Chassis
                Number--the number of the chassis in which the device is installed. This
                attribute can only be queried for PXI devices installed in a chassis
                that has been properly identified in MAX. Bus Number--the bus on which
                the device has been enumerated. Socket Number--the socket number on
                which the device has been enumerated. Notes The bus number and socket
                number can be used to form a VISA resource string for this device, of
                the form "PXI::::INSTR". Traditional NI-DAQ devices do not support the
                chassis number, bus number, and socket number attributes.

        Returns:
            attribute_value (int): A pointer to a signed 32-bit integer variable that receives the value of
                the requested attribute.
        '''
        handle_ctype = visatype.ViSession(self._handle)  # case 1
        index_ctype = visatype.ViInt32(index)  # case 6
        attribute_id_ctype = visatype.ViInt32(attribute_id)  # case 6
        attribute_value_ctype = visatype.ViInt32()  # case 11
        error_code = self._library.niModInst_GetInstalledDeviceAttributeViInt32(handle_ctype, index_ctype, attribute_id_ctype, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_installed_device_attribute_vi_string(self, index, attribute_id):
        '''_get_installed_device_attribute_vi_string

        Returns a string attribute specified by the attributeID parameter for a
        device specified by the handle and index parameters. The handle
        parameter is expected to be a valid handle returned by
        _open_installed_devices_session. Therefore, it acts as a handle
        to a list of installed devices. The index parameter specifies for which
        device in the list you want the attribute. To find out the length of the
        device name string before you allocate a buffer for it, simply call this
        function and pass 0 as the attributeValueBufferSize parameter or NULL as
        the attributeValue parameter. When you do this, the function returns the
        size of the buffer required to hold the attribute value string as its
        return value. You can then allocate an appropriately sized character
        buffer and call this function again.

        Args:
            index (int): A zero-based index that specifies the device for which you want the
                attribute. This index parameter should be between 0 and (deviceCount -
                1), inclusive, where deviceCount is the number of installed devices
                returned by _open_installed_devices_session.
            attribute_id (int): The ID of the string attribute you want to query. Valid Values
                DEVICE_NAME--the name of the device, which can be used
                to open an instrument driver session for that device
                DEVICE_MODEL--the model of the device (for example, NI
                PXI-5122) SERIAL_NUMBER--the serial number of the
                device
            attribute_value_buffer_size (int): The size of the buffer allocated and passed in as the attributeValue
                parameter. The buffer should be large enough to hold the attribute value
                string (including a NULL terminating character). Refer to the
                Description section for information on how to determine the exact buffer
                size required.
        '''
        handle_ctype = visatype.ViSession(self._handle)  # case 1
        index_ctype = visatype.ViInt32(index)  # case 6
        attribute_id_ctype = visatype.ViInt32(attribute_id)  # case 6
        attribute_value_buffer_size_ctype = visatype.ViInt32()  # case 5
        attribute_value_ctype = None  # case 9
        error_code = self._library.niModInst_GetInstalledDeviceAttributeViString(handle_ctype, index_ctype, attribute_id_ctype, attribute_value_buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        attribute_value_buffer_size_ctype = visatype.ViInt32(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        attribute_value_ctype = (visatype.ViChar * attribute_value_buffer_size_ctype.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_code = self._library.niModInst_GetInstalledDeviceAttributeViString(handle_ctype, index_ctype, attribute_id_ctype, attribute_value_buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def _open_installed_devices_session(self, driver):
        '''_open_installed_devices_session

        Creates a handle to a list of installed devices supported by the
        specified driver. Call this function and pass in the name of a National
        Instruments instrument driver, such as "NI-SCOPE". This function
        searches the system and constructs a list of all the installed devices
        that are supported by that driver, and then returns both a handle to
        this list and the number of devices found. The handle is used with other
        functions to query for attributes such as device name and model, and to
        safely discard the list when finished. Note This handle reflects the
        system state when the handle is created (that is, when you call this
        function. If you remove devices from the system or rename them in
        Measurement & Automation Explorer (MAX), this handle may not refer to an
        accurate list of devices. You should destroy the handle using
        _close_installed_devices_session and create a new handle using
        this function.

        Args:
            driver (string): A string specifying the driver whose supported devices you want to find.
                This string is not case-sensitive. Some examples are: NI-SCOPE niScope
                NI-FGEN niFgen NI-HSDIO niHSDIO NI-DMM niDMM NI-SWITCH niSwitch Note If
                you use the empty string for this parameter, NI-ModInst creates a list
                of all Modular Instruments devices installed in the system.

        Returns:
            handle (int): A pointer to a ViSession variable that receives the value of the
                NI-ModInst session handle. This value acts as a handle to the list of
                installed devices and is used in other NI-ModInst functions.
            device_count (int): A pointer to an integer variable that receives the number of devices
                found in the system that are supported by the driver specified in the
                driver parameter.
        '''
        driver_ctype = ctypes.create_string_buffer(driver.encode(self._encoding))  # case 3
        handle_ctype = visatype.ViSession()  # case 11
        device_count_ctype = visatype.ViInt32()  # case 11
        error_code = self._library.niModInst_OpenInstalledDevicesSession(driver_ctype, ctypes.pointer(handle_ctype), ctypes.pointer(device_count_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(handle_ctype.value), int(device_count_ctype.value)

