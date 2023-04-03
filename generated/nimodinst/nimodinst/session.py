# This file was generated

import nimodinst._library_interpreter as _library_interpreter
import nimodinst.errors as errors

# Used for __repr__ and __str__
import pprint

pp = pprint.PrettyPrinter(indent=4)


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


class _Device(object):

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
        The number of the chassis in which the device is installed. This property can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.
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
        The slot (for example, in a PXI chassis) in which the device is installed. This property can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.
        '''
        self.socket_number = AttributeViInt32(owner, 13, index=index)
        '''
        The socket number on which the device has been enumerated
        '''
        self._param_list = 'owner=' + pp.pformat(owner) + ', index=' + pp.pformat(index)
        self._is_frozen = True

    def __repr__(self):
        return '{0}.{1}({2})'.format('nimodinst', self.__class__.__name__, self._param_list)

    def __str__(self):
        ret_str = self.__repr__() + ':\n'
        ret_str += '    bus_number = ' + pp.pformat(self.bus_number) + '\n'
        ret_str += '    chassis_number = ' + pp.pformat(self.chassis_number) + '\n'
        ret_str += '    device_model = ' + pp.pformat(self.device_model) + '\n'
        ret_str += '    device_name = ' + pp.pformat(self.device_name) + '\n'
        ret_str += '    max_pciexpress_link_width = ' + pp.pformat(self.max_pciexpress_link_width) + '\n'
        ret_str += '    pciexpress_link_width = ' + pp.pformat(self.pciexpress_link_width) + '\n'
        ret_str += '    serial_number = ' + pp.pformat(self.serial_number) + '\n'
        ret_str += '    slot_number = ' + pp.pformat(self.slot_number) + '\n'
        ret_str += '    socket_number = ' + pp.pformat(self.socket_number) + '\n'
        return ret_str

    def __getattribute__(self, name):
        if name in ['_is_frozen', 'index', '_param_list', '__class__', '__name__', '__repr__', '__str__', '__setattr__', ]:
            return object.__getattribute__(self, name)
        else:
            return object.__getattribute__(self, name).__getitem__(None)

    def __setattr__(self, name, value):
        if self._is_frozen:
            raise AttributeError("__setattr__ not supported.")
        object.__setattr__(self, name, value)


class _DeviceIterable(object):
    def __init__(self, owner, count):
        self._current_index = 0
        self._owner = owner
        self._count = count
        self._param_list = 'owner=' + pp.pformat(owner) + ', count=' + pp.pformat(count)
        self._is_frozen = True

    def _get_next(self):
        if self._current_index + 1 > self._count:
            raise StopIteration
        else:
            dev = _Device(self._owner, self._current_index)
            self._current_index += 1
            return dev

    def next(self):
        return self._get_next()

    def __next__(self):
        return self._get_next()

    def __repr__(self):
        return '{0}.{1}({2})'.format('nimodinst', self.__class__.__name__, self._param_list)

    def __str__(self):
        ret_str = self.__repr__() + ':\n'
        ret_str += '    current index = {0}'.format(self._current_index)
        return ret_str


class Session(object):
    '''A NI-ModInst session to get device information'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    def __init__(self, driver):
        self._item_count = 0
        self._current_item = 0
        self._interpreter = _library_interpreter.LibraryInterpreter('windows-1251')
        # Note that _library_interpreter clears the session handle in its constructor, so that if
        # _open_installed_devices_session fails, the error handler can reference it.
        # And then once _open_installed_devices_session succeeds, we can call this again with the
        # actual session handle.
        handle, self._item_count = self._open_installed_devices_session(driver)
        self._interpreter.set_session_handle(handle)
        self._param_list = "driver=" + pp.pformat(driver)

        self.devices = []
        for i in range(self._item_count):
            self.devices.append(_Device(self, i))

        self._is_frozen = True

    def __repr__(self):
        return '{0}.{1}({2})'.format('nimodinst', self.__class__.__name__, self._param_list)

    def __str__(self):
        ret_str = self.__repr__() + ':\n'
        for i in range(self._item_count):
            ret_str += str(_Device(self, i)) + '\n'
        return ret_str

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("__setattr__ not supported.")
        object.__setattr__(self, key, value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    # Iterator functions
    def __len__(self):
        return self._item_count

    def __iter__(self):
        return _DeviceIterable(self, self._item_count)

    def close(self):
        try:
            self._close_installed_devices_session()
        except errors.DriverError:
            self._interpreter.set_session_handle()
            raise
        self._interpreter.set_session_handle()

    ''' These are code-generated '''

    def _close_installed_devices_session(self):
        r'''_close_installed_devices_session

        Cleans up the NI-ModInst session created by a call to
        _open_installed_devices_session. Call this method when you are
        finished using the session handle and do not use this handle again.
        '''
        self._interpreter.close_installed_devices_session()

    def _get_installed_device_attribute_vi_int32(self, index, attribute_id):
        r'''_get_installed_device_attribute_vi_int32

        Returns an integer property specified by the attributeID parameter for
        a device specified by the handle and index parameters. The handle
        parameter is expected to be a valid handle returned by
        _open_installed_devices_session. It therefore acts as a handle to
        a list of installed devices. The index parameter specifies the device in
        the list for which you want the property.

        Args:
            index (int): A zero-based index that specifies the device for which you want the
                property. This index parameter should be between 0 and (deviceCount -
                1), inclusive, where deviceCount is the number of installed devices
                returned by _open_installed_devices_session.

            attribute_id (int): The ID of the integer property you want to query. Valid Values Slot
                Number--the slot (for example, in a PXI chassis) in which the device is
                installed. This property can only be queried for PXI devices installed
                in a chassis that has been properly identified in MAX. Chassis
                Number--the number of the chassis in which the device is installed. This
                property can only be queried for PXI devices installed in a chassis
                that has been properly identified in MAX. Bus Number--the bus on which
                the device has been enumerated. Socket Number--the socket number on
                which the device has been enumerated. Notes The bus number and socket
                number can be used to form a VISA resource string for this device, of
                the form "PXI::::INSTR". Traditional NI-DAQ devices do not support the
                chassis number, bus number, and socket number properties.


        Returns:
            attribute_value (int): A pointer to a signed 32-bit integer variable that receives the value of
                the requested property.

        '''
        attribute_value = self._interpreter.get_installed_device_attribute_vi_int32(index, attribute_id)
        return attribute_value

    def _get_installed_device_attribute_vi_string(self, index, attribute_id):
        r'''_get_installed_device_attribute_vi_string

        Returns a string property specified by the attributeID parameter for a
        device specified by the handle and index parameters. The handle
        parameter is expected to be a valid handle returned by
        _open_installed_devices_session. Therefore, it acts as a handle
        to a list of installed devices. The index parameter specifies for which
        device in the list you want the property. To find out the length of the
        device name string before you allocate a buffer for it, simply call this
        method and pass 0 as the attributeValueBufferSize parameter or NULL as
        the attributeValue parameter. When you do this, the method returns the
        size of the buffer required to hold the property value string as its
        return value. You can then allocate an appropriately sized character
        buffer and call this method again.

        Args:
            index (int): A zero-based index that specifies the device for which you want the
                property. This index parameter should be between 0 and (deviceCount -
                1), inclusive, where deviceCount is the number of installed devices
                returned by _open_installed_devices_session.

            attribute_id (int): The ID of the string property you want to query. Valid Values
                device_name--the name of the device, which can be used
                to open an instrument driver session for that device
                device_model--the model of the device (for example, NI
                PXI-5122) serial_number--the serial number of the
                device


        Returns:
            attribute_value (str): The character buffer into which the property value string is copied.

        '''
        attribute_value = self._interpreter.get_installed_device_attribute_vi_string(index, attribute_id)
        return attribute_value

    def _open_installed_devices_session(self, driver):
        r'''_open_installed_devices_session

        Creates a handle to a list of installed devices supported by the
        specified driver. Call this method and pass in the name of an NI
        instrument driver, such as "NI-SCOPE". This method
        searches the system and constructs a list of all the installed devices
        that are supported by that driver, and then returns both a handle to
        this list and the number of devices found. The handle is used with other
        methods to query for properties such as device name and model, and to
        safely discard the list when finished. Note This handle reflects the
        system state when the handle is created (that is, when you call this
        method. If you remove devices from the system or rename them in
        Measurement & Automation Explorer (MAX), this handle may not refer to an
        accurate list of devices. You should destroy the handle using
        _close_installed_devices_session and create a new handle using
        this method.

        Args:
            driver (str): A string specifying the driver whose supported devices you want to find.
                This string is not case-sensitive. Some examples are: NI-SCOPE niScope
                NI-FGEN niFgen NI-HSDIO niHSDIO NI-DMM niDMM NI-SWITCH niSwitch Note If
                you use the empty string for this parameter, NI-ModInst creates a list
                of all Modular Instruments devices installed in the system.


        Returns:
            handle (int): A pointer to a ViSession variable that receives the value of the
                NI-ModInst session handle. This value acts as a handle to the list of
                installed devices and is used in other NI-ModInst methods.

            device_count (int): A pointer to an integer variable that receives the number of devices
                found in the system that are supported by the driver specified in the
                driver parameter.

        '''
        handle, device_count = self._interpreter.open_installed_devices_session(driver)
        return handle, device_count
