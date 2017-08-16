
# This file was generated
import ctypes

from niswitch import ctypes_types
from niswitch import enums
from niswitch import errors
from niswitch import library


class AttributeViInt32(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj._get_attribute_vi_int32(self.channel, self.attribute_id)

    def __set__(self, obj, value):
        obj._set_attribute_vi_int32(self.channel, self.attribute_id, value)


class AttributeViReal64(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj._get_attribute_vi_real64(self.channel, self.attribute_id)

    def __set__(self, obj, value):
        obj._set_attribute_vi_real64(self.channel, self.attribute_id, value)


class AttributeViString(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj._get_attribute_vi_string(self.channel, self.attribute_id)

    def __set__(self, obj, value):
        obj._set_attribute_vi_string(self.channel, self.attribute_id, value)


class AttributeViBoolean(object):

    def __init__(self, attribute_id):
        self.attribute_id = attribute_id
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return obj._get_attribute_vi_boolean(self.channel, self.attribute_id) is not 0

    def __set__(self, obj, value):
        obj._set_attribute_vi_boolean(self.channel, self.attribute_id, (value is not 0))


class AttributeEnum(object):

    def __init__(self, attribute_id, enum_meta_class):
        self.attribute_id = attribute_id
        self.attribute_type = enum_meta_class
        self.channel = ''

    def __get__(self, obj, objtype):
        assert objtype is Session
        return self.attribute_type(obj._get_attribute_vi_int32(self.channel, self.attribute_id))

    def __set__(self, obj, value):
        if type(value) is not self.attribute_type:
            raise TypeError('Value mode must be of type ' + str(self.attribute_type))
        obj._set_attribute_vi_int32(self.channel, self.attribute_id, value.value)


class Acquisition(object):
    def __init__(self, session):
        self.session = session

    def __enter__(self):
        self.session._initiate()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.session._abort()


class Session(object):
    '''An NI-SWITCH session to a National Instruments Switch Module'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    analog_bus_sharing_enable = AttributeViBoolean(1150018)
    '''
    Enables or disables sharing of an analog bus line so that multiple
    NI SwitchBlock devices may connect to it simultaneously. To enable
    multiple NI SwitchBlock devices to share an analog bus line, set this
    property to TRUE for each device on the channel that corresponds with
    the shared analog bus line. The default value for all devices is FALSE,
    which disables sharing of the analog bus.
    '''
    bandwidth = AttributeViReal64(1250005)
    '''
    Returns the bandwidth for the channel in hertz.
    '''
    cabled_module_scan_advanced_bus = AttributeViInt32(1150009)
    '''
    This property has been deprecated and might be removed from a future
    release of NI-SWITCH. Use niSwitch Route Scan Advanced Output VI
    instead.
    '''
    cabled_module_trigger_bus = AttributeViInt32(1150008)
    '''
    This property has been deprecated and might be removed from a future
    release of NI-SWITCH. Use the niSwitch Route Trigger Input VI instead.
    '''
    cache = AttributeViBoolean(1050004)
    '''
    Specifies whether to cache the value of properties. The default value is
    TRUE. Use the niSwitch Initialize With Options VI to override the
    default value.
    '''
    channel_count = AttributeViInt32(1050203)
    '''
    Contains the number of channels that the instrument driver supports.
    '''
    characteristic_impedance = AttributeViReal64(1250016)
    '''
    Returns the characteristic impedance for the channel in ohms.
    '''
    class_group_capabilities = AttributeViString(1050401)
    '''
    Contains a comma-separated (,) list of class-extension groups that the
    instrument driver implements.
    '''
    class_specification_major_version = AttributeViInt32(1050515)
    '''
    Contains the major version number of the IviSwtch class specification.
    '''
    class_specification_minor_version = AttributeViInt32(1050516)
    '''
    Contains the minor version number of the class specification with which
    the instrument driver is compliant.
    '''
    continuous_scan = AttributeViBoolean(1150002)
    '''
    Specifies whether to continuously scan through a scan list. Set the
    property to FALSE to stop scanning after one pass through the scan list.
    Set this property to TRUE to loop continuously through the scan list.
    '''
    description = AttributeViString(1050514)
    '''
    Contains a brief description of the instrument driver.
    '''
    digital_filter_enable = AttributeViBoolean(1150016)
    '''
    Specifies whether to apply the pulse width filter to the Trigger Input.
    Set the property to TRUE to prevent the switch module from being
    triggered by pulses that are less than 150 ns on PXI trigger lines 0-7.
    '''
    driver_prefix = AttributeViString(1050302)
    '''
    Contains the prefix for all of the instrument driver VIs.
    '''
    driver_setup = AttributeViString(1050007)
    '''
    Contains the Driver Setup string that you specified when initializing
    the instrument driver.
    '''
    driver_vendor = AttributeViString(1050513)
    '''
    Contains the name of the vendor that supplies the instrument driver.
    '''
    firmware_revision = AttributeViString(1050510)
    '''
    Contains the firmware revision information for the instrument currently
    in use.
    '''
    handshaking_initiation = AttributeEnum(1150013, enums.HandshakingInitiation)
    '''
    Specifies how to start handshaking with a measurement device.
    '''
    interchange_check = AttributeViBoolean(1050021)
    '''
    Specifies whether to perform interchangeability checking and retrieve
    interchangeability warnings when you call the niSwitch Connect Channels
    , niSwitch Set Path and niSwitch Initiate Scan VIs. The default value is
    FALSE.
    '''
    io_resource_descriptor = AttributeViString(1050304)
    '''
    Contains the resource descriptor the instrument driver uses to identify
    the physical device.
    '''
    is_configuration_channel = AttributeViBoolean(1250003)
    '''
    Specifies whether to designate the channel as a configuration channel—a
    channel reserved for internal path creation. The instrument driver uses
    configuration channels to create paths between the channels you specify
    in the niSwitch Connect Channels VI.
    '''
    is_debounced = AttributeViBoolean(1250002)
    '''
    Indicates whether the entire switch module has settled since the last
    switching command. A value of TRUE indicates that all signals going
    through the switch module are valid.
    '''
    is_scanning = AttributeViBoolean(1250024)
    '''
    Indicates whether the switch module has completed the scan operation.
    TRUE indicates that the scan has completed.
    '''
    is_source_channel = AttributeViBoolean(1250001)
    '''
    Specifies whether to designate the channel as a source channel.
    '''
    is_waiting_for_trigger = AttributeViBoolean(1150004)
    '''
    Indicates with a semi-colon (;) that at that point in the scan list, the
    scan engine should pause until a trigger is received from the trigger
    input. If you generate that trigger through either a hardware pulse or
    the niSwitch Send Software Trigger VI, you must know when the scan
    engine has reached such a state.
    '''
    logical_name = AttributeViString(1050305)
    '''
    Contains the logical name you specified when opening the current IVI
    session.
    '''
    manufacturer = AttributeViString(1050511)
    '''
    Contains the name of the manufacturer of the instrument currently in
    use.
    '''
    master_slave_scan_advanced_bus = AttributeViInt32(1150007)
    '''
    This property has been deprecated and might be removed from a future
    release of NI-SWITCH. Use niSwitch Route Scan Advanced Output VI
    instead.
    '''
    master_slave_trigger_bus = AttributeViInt32(1150006)
    '''
    This property has been deprecated and might be removed from a future
    release of NI-SWITCH. Use the niSwitch Route Trigger Input VI instead.
    '''
    maximum_ac_voltage = AttributeViReal64(1250007)
    '''
    Returns the maximum AC voltage the channel can switch in volts RMS.
    '''
    maximum_carry_ac_current = AttributeViReal64(1250011)
    '''
    Returns the maximum AC current the channel can carry in amperes RMS.
    '''
    maximum_carry_ac_power = AttributeViReal64(1250015)
    '''
    Returns the maximum AC power the channel can carry in volt-amperes.
    '''
    maximum_carry_dc_current = AttributeViReal64(1250010)
    '''
    Returns the maximum DC current the channel can carry in amperes.
    '''
    maximum_carry_dc_power = AttributeViReal64(1250014)
    '''
    Returns the maximum DC power the channel can carry in watts.
    '''
    maximum_dc_voltage = AttributeViReal64(1250006)
    '''
    Returns the maximum DC voltage the channel can switch in volts.
    '''
    maximum_switching_ac_current = AttributeViReal64(1250009)
    '''
    Returns the maximum AC current the channel can switch in amperes RMS.
    '''
    maximum_switching_ac_power = AttributeViReal64(1250013)
    '''
    Returns the maximum AC power the channel can switch in volt-amperes.
    '''
    maximum_switching_dc_current = AttributeViReal64(1250008)
    '''
    Returns the maximum DC current the channel can switch in amperes.
    '''
    maximum_switching_dc_power = AttributeViReal64(1250012)
    '''
    Returns the maximum DC power the channel can switch in watts.
    '''
    model = AttributeViString(1050512)
    '''
    Contains the model number or name of the instrument currently in use.
    '''
    number_of_columns = AttributeViInt32(1250019)
    '''
    Returns the number of channels on the column of a matrix or scanner. If
    the switch module is a scanner, this property returns the number of
    input channels.
    '''
    number_of_relays = AttributeViInt32(1150014)
    '''
    Returns the number of relays that the instrument driver supports.
    '''
    number_of_rows = AttributeViInt32(1250018)
    '''
    Returns the number of channels on the row of a matrix or scanner. If the
    switch module is a scanner, this property returns the number of output
    channels.
    '''
    parsed_scan_list = AttributeViString(1150012)
    '''
    This property has been deprecated and might be removed from a future
    release of NI-SWITCH.
    '''
    power_down_latching_relays_after_debounce = AttributeViBoolean(1150017)
    '''
    Specifies whether to power down latching relays after calling the
    niSwitch Wait For Debounce VI. Set this property to TRUE to ensure that
    the relays settle and the latching relays power down after you call the
    niSwitch Wait for Debounce VI.
    '''
    query_instrument_status = AttributeViBoolean(1050003)
    '''
    Specifies whether the instrument driver queries the instrument status
    after each operation. The default value is TRUE. Use the niSwitch
    Initialize With Options VI to override the default value.
    '''
    range_check = AttributeViBoolean(1050002)
    '''
    Specifies whether to validate property values and VI parameters. The
    default value is TRUE. Use the niSwitch Initialize With Options VI to
    override the default value.
    '''
    record_value_coercions = AttributeViBoolean(1050006)
    '''
    Specifies whether the IVI engine keeps a list of the value coercions it
    makes for properties with ViInt32 and ViReal64 datatypes. The default
    value is FALSE. Use the niSwitch Initialize With Options VI to override
    the default value.
    '''
    revision = AttributeViString(1050551)
    '''
    Contains additional version information about the instrument driver.
    '''
    scan_advanced_output = AttributeEnum(1250023, enums.ScanAdvancedOutput)
    '''
    Specifies the method to use to notify another instrument that all
    signals through the switch module have settled following the processing
    of one entry in the scan list.
    '''
    scan_advanced_polarity = AttributeEnum(1150011, enums.ScanAdvancedPolarity)
    '''
    Specifies the driving level for the Scan Advanced Output signal sent
    from the switch module through either the external (PXI/PXIe) or front
    connector (SCXI) lines. When the Scan Advanced Output signal is sent to
    one of the PXI\_Trig lines, the driven level is always low and this
    property is ignored. Between each Scan Advanced Output signal, the line
    is not driven and is in a high-impedance state.
    '''
    scan_delay = AttributeViReal64(1250025)
    '''
    Specifies the minimum amount of time the switch module waits before it
    asserts the scan advanced output trigger after opening or closing the
    switch. The switch module always waits for debounce before asserting the
    trigger. Thus, the actual delay will always be the greater value of the
    settling time and the value you specify as the switch delay, measured in
    seconds. Settling time can vary depending on the switch module.
    '''
    scan_list = AttributeViString(1250020)
    '''
    Contains a scan list (a string that specifies channel connections and
    trigger conditions). The niSwitch Initiate Scan VI makes or breaks
    connections and waits for triggers according to the instructions in the
    scan list. The scan list is comprised of channel names separated by
    special characters that determine the operations the scanner performs on
    the channels when it executes the scan list.
    '''
    scan_mode = AttributeEnum(1250021, enums.ScanMode)
    '''
    Specifies how to handle existing connections that conflict with the
    connections you make in a scan list. For example, if CH1 is already
    connected to CH2 and the scan list instructs the switch module to
    connect CH1 to CH3, this property specifies what happens to the
    connection between CH1 and CH2.
    '''
    serial_number = AttributeViString(1150015)
    '''
    Returns the serial number for the switch module controlled by the
    instrument driver. If the switch module does not return a serial number,
    the instrument driver returns the Invalid Attribute error.
    '''
    serial_numberi32 = AttributeViInt32(1150001)
    '''
    This property has been deprecated and might be removed from a future
    release of NI-SWITCH.
    '''
    settling_time = AttributeViReal64(1250004)
    '''
    Returns the maximum length of time in seconds from after you make a
    connection until the signal flowing through the channel settles.
    Settling time can vary depending on the switch module.
    '''
    simulate = AttributeViBoolean(1050005)
    '''
    Specifies whether to simulate instrument driver I/O operations. The
    default value is FALSE. Use the niSwitch Initialize With Options VI to
    override the default value.
    '''
    supported_instrument_models = AttributeViString(1050327)
    '''
    Contains a comma-separated (,) list of supported instrument models.
    '''
    temperature = AttributeViReal64(1150019)
    '''
    Returns the temperature as read by the Switch module in degrees Celsius.
    Refer to the device documentation for more information.
    '''
    trigger_input = AttributeEnum(1250022, enums.TriggerInput)
    '''
    Specifies the source of the trigger for which the switch module can wait
    upon encountering a semi-colon (;) when processing a scan list. When the
    trigger occurs, the switch module advances to the next entry in the scan
    list.
    '''
    trigger_input_polarity = AttributeEnum(1150010, enums.TriggerInputPolarity)
    '''
    Determines the behavior of the trigger input.
    '''
    trigger_mode = AttributeViInt32(1150005)
    '''
    This property has been deprecated and might be removed from a future
    release of NI-SWITCH. Use the niSwitch Route Trigger Input and/or
    niSwitch Route Scan Advanced Output VIs instead.
    '''
    wire_mode = AttributeViInt32(1250017)
    '''
    Returns the wire mode of the switch module. This property affects the
    values of the Number of Rows and Number of Columns properties. The
    actual number of input and output lines on the switch module does not
    change, but the number of channels depends on how many lines constitute
    each channel.
    '''

    def __init__(self, resource_name, id_query=0, reset_device=False, options_string=""):
        self.library = library.get_library()
        self.vi = 0  # This must be set before calling _init_with_options.
        self.vi = self._init_with_options(resource_name, id_query, reset_device, options_string)

        self._is_frozen = True

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise TypeError("%r is a frozen class" % self)
        object.__setattr__(self, key, value)

    def initiate(self):
        return Acquisition(self)

    def __del__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        # TODO(marcoskirsch): Should we raise an exception on double close? Look at what File does.
        try:
            self._close()
        except errors.Error:
            # TODO(marcoskirsch): This will occur when session is "stolen". Change to log instead
            print("Failed to close session.")
        self.vi = 0

    # method needed for generic driver exceptions
    def _get_error_description(self, error_code):
        new_error_code = ctypes_types.ViStatus_ctype(0)
        buffer_size = self.library.niSwitch_GetError(self.vi, ctypes.byref(new_error_code), 0, None)
        assert (new_error_code.value == error_code)

        if (buffer_size > 0):
            '''
            Return code > 0 from first call to GetError represents the size of
            the description.  Call it again.
            Ignore incoming IVI error code and return description from the driver
            (trust that the IVI error code was properly stored in the session
            by the driver)
            '''
            error_code = ctypes_types.ViStatus_ctype(error_code)
            error_message = (ctypes_types.ViChar_ctype * buffer_size)()
            self.library.niSwitch_GetError(self.vi, ctypes.byref(error_code), buffer_size, ctypes.cast(error_message, ctypes.POINTER(ctypes_types.ViChar_ctype)))
        else:
            '''
            Return code <= 0 from GetError indicates a problem.  This is expected
            when the session is invalid (IVI spec requires GetError to fail).
            Use GetErrorMessage instead.  It doesn't require a session.

            Call niSwitch_GetErrorMessage, pass VI_NULL for the buffer in order to retrieve
            the length of the error message.
            '''
            error_code = buffer_size
            buffer_size = self.library.niSwitch_GetErrorMessage(self.vi, error_code, 0, None)
            error_message = (ctypes_types.ViChar_ctype * buffer_size)()
            self.library.niSwitch_GetErrorMessage(self.vi, error_code, buffer_size, ctypes.cast(error_message, ctypes.POINTER(ctypes_types.ViChar_ctype)))

        # TODO(marcoskirsch): By hardcoding encoding "ascii", internationalized strings will throw.
        #       Which encoding should we be using? https://docs.python.org/3/library/codecs.html#standard-encodings
        return new_error_code.value, error_message.value.decode("ascii")

    ''' These are code-generated '''

    def _abort_scan(self):
        error_code = self.library.niSwitch_AbortScan(self.vi)
        errors._handle_error(self, error_code)
        return

    def can_connect(self, channel1, channel2):
        path_capability_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niSwitch_CanConnect(self.vi, channel1.encode('ascii'), channel2.encode('ascii'), ctypes.pointer(path_capability_ctype))
        errors._handle_error(self, error_code)
        return path_capability_ctype.value

    def _clear_error(self):
        error_code = self.library.niSwitch_ClearError(self.vi)
        errors._handle_error(self, error_code)
        return

    def clear_interchange_warnings(self):
        error_code = self.library.niSwitch_ClearInterchangeWarnings(self.vi)
        errors._handle_error(self, error_code)
        return

    def commit(self):
        error_code = self.library.niSwitch_Commit(self.vi)
        errors._handle_error(self, error_code)
        return

    def configure_scan_list(self, scanlist, scan_mode):
        error_code = self.library.niSwitch_ConfigureScanList(self.vi, scanlist.encode('ascii'), scan_mode)
        errors._handle_error(self, error_code)
        return

    def configure_scan_trigger(self, scan_delay, trigger_input, scan_advanced_output):
        error_code = self.library.niSwitch_ConfigureScanTrigger(self.vi, scan_delay, trigger_input, scan_advanced_output)
        errors._handle_error(self, error_code)
        return

    def connect(self, channel1, channel2):
        error_code = self.library.niSwitch_Connect(self.vi, channel1.encode('ascii'), channel2.encode('ascii'))
        errors._handle_error(self, error_code)
        return

    def connect_multiple(self, connection_list):
        error_code = self.library.niSwitch_ConnectMultiple(self.vi, connection_list.encode('ascii'))
        errors._handle_error(self, error_code)
        return

    def disable(self):
        error_code = self.library.niSwitch_Disable(self.vi)
        errors._handle_error(self, error_code)
        return

    def disconnect(self, channel1, channel2):
        error_code = self.library.niSwitch_Disconnect(self.vi, channel1.encode('ascii'), channel2.encode('ascii'))
        errors._handle_error(self, error_code)
        return

    def disconnect_all(self):
        error_code = self.library.niSwitch_DisconnectAll(self.vi)
        errors._handle_error(self, error_code)
        return

    def disconnect_multiple(self, disconnection_list):
        error_code = self.library.niSwitch_DisconnectMultiple(self.vi, disconnection_list.encode('ascii'))
        errors._handle_error(self, error_code)
        return

    def _get_attribute_vi_boolean(self, channel_name, attribute_id):
        attribute_value_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niSwitch_GetAttributeViBoolean(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors._handle_error(self, error_code)
        return attribute_value_ctype.value

    def _get_attribute_vi_int32(self, channel_name, attribute_id):
        attribute_value_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niSwitch_GetAttributeViInt32(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors._handle_error(self, error_code)
        return attribute_value_ctype.value

    def _get_attribute_vi_real64(self, channel_name, attribute_id):
        attribute_value_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niSwitch_GetAttributeViReal64(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors._handle_error(self, error_code)
        return attribute_value_ctype.value

    def _get_attribute_vi_session(self, channel_name, attribute_id):
        attribute_value_ctype = ctypes_types.ViSession_ctype(0)
        error_code = self.library.niSwitch_GetAttributeViSession(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors._handle_error(self, error_code)
        return attribute_value_ctype.value

    def _get_attribute_vi_string(self, channel_name, attribute_id, array_size):
        attribute_value_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niSwitch_GetAttributeViString(self.vi, channel_name.encode('ascii'), attribute_id, array_size, ctypes.pointer(attribute_value_ctype))
        errors._handle_error(self, error_code)
        return attribute_value_ctype.value

    def get_channel_name(self, index, buffer_size):
        channel_name_buffer_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niSwitch_GetChannelName(self.vi, index, buffer_size, ctypes.pointer(channel_name_buffer_ctype))
        errors._handle_error(self, error_code)
        return channel_name_buffer_ctype.value

    def _get_error(self, buffersize):
        code_ctype = ctypes_types.ViStatus_ctype(0)
        description_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niSwitch_GetError(self.vi, ctypes.pointer(code_ctype), buffersize, ctypes.pointer(description_ctype))
        errors._handle_error(self, error_code)
        return code_ctype.value, description_ctype.value

    def get_next_coercion_record(self, buffer_size):
        coercion_record_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niSwitch_GetNextCoercionRecord(self.vi, buffer_size, ctypes.pointer(coercion_record_ctype))
        errors._handle_error(self, error_code)
        return coercion_record_ctype.value

    def get_next_interchange_warning(self, buffer_size):
        interchange_warning_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niSwitch_GetNextInterchangeWarning(self.vi, buffer_size, ctypes.pointer(interchange_warning_ctype))
        errors._handle_error(self, error_code)
        return interchange_warning_ctype.value

    def get_path(self, channel1, channel2, buffer_size):
        path_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niSwitch_GetPath(self.vi, channel1.encode('ascii'), channel2.encode('ascii'), buffer_size, ctypes.pointer(path_ctype))
        errors._handle_error(self, error_code)
        return path_ctype.value

    def get_relay_count(self, relay_name):
        relay_count_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niSwitch_GetRelayCount(self.vi, relay_name.encode('ascii'), ctypes.pointer(relay_count_ctype))
        errors._handle_error(self, error_code)
        return relay_count_ctype.value

    def get_relay_name(self, index, relay_name_buffer_size):
        relay_name_buffer_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niSwitch_GetRelayName(self.vi, index, relay_name_buffer_size, ctypes.pointer(relay_name_buffer_ctype))
        errors._handle_error(self, error_code)
        return relay_name_buffer_ctype.value

    def get_relay_position(self, relay_name):
        relay_position_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niSwitch_GetRelayPosition(self.vi, relay_name.encode('ascii'), ctypes.pointer(relay_position_ctype))
        errors._handle_error(self, error_code)
        return relay_position_ctype.value

    def _init_with_options(self, resource_name, id_query, reset_device, options_string):
        vi_ctype = ctypes_types.ViSession_ctype(0)
        error_code = self.library.niSwitch_InitWithOptions(resource_name.encode('ascii'), id_query, reset_device, options_string.encode('ascii'), ctypes.pointer(vi_ctype))
        errors._handle_error(self, error_code)
        return vi_ctype.value

    def init_with_topology(self, resource_name, topology, simulate, reset_device):
        vi_ctype = ctypes_types.ViSession_ctype(0)
        error_code = self.library.niSwitch_InitWithTopology(resource_name.encode('ascii'), topology.encode('ascii'), simulate, reset_device, ctypes.pointer(vi_ctype))
        errors._handle_error(self, error_code)
        return vi_ctype.value

    def _initiate_scan(self):
        error_code = self.library.niSwitch_InitiateScan(self.vi)
        errors._handle_error(self, error_code)
        return

    def is_debounced(self):
        is_debounced_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niSwitch_IsDebounced(self.vi, ctypes.pointer(is_debounced_ctype))
        errors._handle_error(self, error_code)
        return is_debounced_ctype.value

    def is_scanning(self):
        is_scanning_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niSwitch_IsScanning(self.vi, ctypes.pointer(is_scanning_ctype))
        errors._handle_error(self, error_code)
        return is_scanning_ctype.value

    def _lock_session(self):
        caller_has_lock_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niSwitch_LockSession(self.vi, ctypes.pointer(caller_has_lock_ctype))
        errors._handle_error(self, error_code)
        return caller_has_lock_ctype.value

    def reset_interchange_check(self):
        error_code = self.library.niSwitch_ResetInterchangeCheck(self.vi)
        errors._handle_error(self, error_code)
        return

    def reset_with_defaults(self):
        error_code = self.library.niSwitch_ResetWithDefaults(self.vi)
        errors._handle_error(self, error_code)
        return

    def route_scan_advanced_output(self, scan_advanced_output_connector, scan_advanced_output_bus_line, invert):
        error_code = self.library.niSwitch_RouteScanAdvancedOutput(self.vi, scan_advanced_output_connector, scan_advanced_output_bus_line, invert)
        errors._handle_error(self, error_code)
        return

    def route_trigger_input(self, trigger_input_connector, trigger_input_bus_line, invert):
        error_code = self.library.niSwitch_RouteTriggerInput(self.vi, trigger_input_connector, trigger_input_bus_line, invert)
        errors._handle_error(self, error_code)
        return

    def scan(self, scanlist, initiation):
        error_code = self.library.niSwitch_Scan(self.vi, scanlist.encode('ascii'), initiation)
        errors._handle_error(self, error_code)
        return

    def send_software_trigger(self):
        error_code = self.library.niSwitch_SendSoftwareTrigger(self.vi)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value):
        error_code = self.library.niSwitch_SetAttributeViBoolean(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value):
        error_code = self.library.niSwitch_SetAttributeViInt32(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value):
        error_code = self.library.niSwitch_SetAttributeViReal64(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_session(self, channel_name, attribute_id, attribute_value):
        error_code = self.library.niSwitch_SetAttributeViSession(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_string(self, channel_name, attribute_id, attribute_value):
        error_code = self.library.niSwitch_SetAttributeViString(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors._handle_error(self, error_code)
        return

    def set_continuous_scan(self, continuous_scan):
        error_code = self.library.niSwitch_SetContinuousScan(self.vi, continuous_scan)
        errors._handle_error(self, error_code)
        return

    def set_path(self, path_list):
        error_code = self.library.niSwitch_SetPath(self.vi, path_list.encode('ascii'))
        errors._handle_error(self, error_code)
        return

    def _unlock_session(self):
        caller_has_lock_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niSwitch_UnlockSession(self.vi, ctypes.pointer(caller_has_lock_ctype))
        errors._handle_error(self, error_code)
        return caller_has_lock_ctype.value

    def wait_for_debounce(self, maximum_time_ms):
        error_code = self.library.niSwitch_WaitForDebounce(self.vi, maximum_time_ms)
        errors._handle_error(self, error_code)
        return

    def wait_for_scan_complete(self, maximum_time_ms):
        error_code = self.library.niSwitch_WaitForScanComplete(self.vi, maximum_time_ms)
        errors._handle_error(self, error_code)
        return

    def _close(self):
        error_code = self.library.niSwitch_close(self.vi)
        errors._handle_error(self, error_code)
        return

    def error_message(self, error_code):
        error_message_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niSwitch_error_message(self.vi, error_code, ctypes.pointer(error_message_ctype))
        errors._handle_error(self, error_code)
        return error_message_ctype.value

    def error_query(self):
        error_code_ctype = ctypes_types.ViInt32_ctype(0)
        error_message_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niSwitch_error_query(self.vi, ctypes.pointer(error_code_ctype), ctypes.pointer(error_message_ctype))
        errors._handle_error(self, error_code)
        return error_code_ctype.value, error_message_ctype.value

    def reset(self):
        error_code = self.library.niSwitch_reset(self.vi)
        errors._handle_error(self, error_code)
        return

    def revision_query(self):
        instrument_driver_revision_ctype = ctypes_types.ViChar_ctype(0)
        firmware_revision_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niSwitch_revision_query(self.vi, ctypes.pointer(instrument_driver_revision_ctype), ctypes.pointer(firmware_revision_ctype))
        errors._handle_error(self, error_code)
        return instrument_driver_revision_ctype.value, firmware_revision_ctype.value

    def self_test(self):
        self_test_result_ctype = ctypes_types.ViInt16_ctype(0)
        self_test_message_ctype = ctypes_types.ViChar_ctype(0)
        error_code = self.library.niSwitch_self_test(self.vi, ctypes.pointer(self_test_result_ctype), ctypes.pointer(self_test_message_ctype))
        errors._handle_error(self, error_code)
        return self_test_result_ctype.value, self_test_message_ctype.value

