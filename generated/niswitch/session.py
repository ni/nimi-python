# -*- coding: utf-8 -*-
# This file was generated
import ctypes

from niswitch import ctypes_types
from niswitch import enums
from niswitch import errors
from niswitch import library
from niswitch import python_types


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
        return obj._get_attribute_vi_boolean(self.channel, self.attribute_id)

    def __set__(self, obj, value):
        obj._set_attribute_vi_boolean(self.channel, self.attribute_id, value)


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
    bandwidth = AttributeViReal64(1250005)
    cabled_module_scan_advanced_bus = AttributeViInt32(1150009)
    cabled_module_trigger_bus = AttributeViInt32(1150008)
    cache = AttributeViBoolean(1050004)
    channel_count = AttributeViInt32(1050203)
    characteristic_impedance = AttributeViReal64(1250016)
    class_group_capabilities = AttributeViString(1050401)
    class_specification_major_version = AttributeViInt32(1050515)
    class_specification_minor_version = AttributeViInt32(1050516)
    continuous_scan = AttributeViBoolean(1150002)
    description = AttributeViString(1050514)
    digital_filter_enable = AttributeViBoolean(1150016)
    driver_prefix = AttributeViString(1050302)
    driver_setup = AttributeViString(1050007)
    driver_vendor = AttributeViString(1050513)
    firmware_revision = AttributeViString(1050510)
    handshaking_initiation = AttributeEnum(1150013, enums.HandshakingInitiation)
    interchange_check = AttributeViBoolean(1050021)
    io_resource_descriptor = AttributeViString(1050304)
    is_configuration_channel = AttributeViBoolean(1250003)
    is_debounced = AttributeViBoolean(1250002)
    is_scanning = AttributeViBoolean(1250024)
    is_source_channel = AttributeViBoolean(1250001)
    is_waiting_for_trigger = AttributeViBoolean(1150004)
    logical_name = AttributeViString(1050305)
    manufacturer = AttributeViString(1050511)
    master_slave_scan_advanced_bus = AttributeViInt32(1150007)
    master_slave_trigger_bus = AttributeViInt32(1150006)
    maximum_ac_voltage = AttributeViReal64(1250007)
    maximum_carry_ac_current = AttributeViReal64(1250011)
    maximum_carry_ac_power = AttributeViReal64(1250015)
    maximum_carry_dc_current = AttributeViReal64(1250010)
    maximum_carry_dc_power = AttributeViReal64(1250014)
    maximum_dc_voltage = AttributeViReal64(1250006)
    maximum_switching_ac_current = AttributeViReal64(1250009)
    maximum_switching_ac_power = AttributeViReal64(1250013)
    maximum_switching_dc_current = AttributeViReal64(1250008)
    maximum_switching_dc_power = AttributeViReal64(1250012)
    model = AttributeViString(1050512)
    number_of_columns = AttributeViInt32(1250019)
    number_of_relays = AttributeViInt32(1150014)
    number_of_rows = AttributeViInt32(1250018)
    parsed_scan_list = AttributeViString(1150012)
    power_down_latching_relays_after_debounce = AttributeViBoolean(1150017)
    query_instrument_status = AttributeViBoolean(1050003)
    range_check = AttributeViBoolean(1050002)
    record_value_coercions = AttributeViBoolean(1050006)
    revision = AttributeViString(1050551)
    scan_advanced_output = AttributeEnum(1250023, enums.ScanAdvancedOutput)
    scan_advanced_polarity = AttributeEnum(1150011, enums.ScanAdvancedPolarity)
    scan_delay = AttributeViReal64(1250025)
    scan_list = AttributeViString(1250020)
    scan_mode = AttributeEnum(1250021, enums.ScanMode)
    serial_number = AttributeViString(1150015)
    serial_numberi32 = AttributeViInt32(1150001)
    settling_time = AttributeViReal64(1250004)
    simulate = AttributeViBoolean(1050005)
    supported_instrument_models = AttributeViString(1050327)
    temperature = AttributeViReal64(1150019)
    trigger_input = AttributeEnum(1250022, enums.TriggerInput)
    trigger_input_polarity = AttributeEnum(1150010, enums.TriggerInputPolarity)
    trigger_mode = AttributeViInt32(1150005)
    wire_mode = AttributeViInt32(1250017)

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
        assert (new_error_code.value == error_code), 'buffer_size is {0}, new_error_code.value is {1}, error_code is {2}'.format(buffer_size, new_error_code.value, error_code)

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
        '''_abort_scan

        
        '''
        error_code = self.library.niSwitch_AbortScan(self.vi)
        errors._handle_error(self, error_code)
        return

    def can_connect(self, channel1, channel2):
        '''can_connect

        

        Args:
            channel1 (str):
            channel2 (str):

        Returns:
            path_capability (int):
        '''
        path_capability_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niSwitch_CanConnect(self.vi, channel1.encode('ascii'), channel2.encode('ascii'), ctypes.pointer(path_capability_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViInt32(path_capability_ctype.value)

    def _clear_error(self):
        '''_clear_error

        
        '''
        error_code = self.library.niSwitch_ClearError(self.vi)
        errors._handle_error(self, error_code)
        return

    def clear_interchange_warnings(self):
        '''clear_interchange_warnings

        
        '''
        error_code = self.library.niSwitch_ClearInterchangeWarnings(self.vi)
        errors._handle_error(self, error_code)
        return

    def commit(self):
        '''commit

        
        '''
        error_code = self.library.niSwitch_Commit(self.vi)
        errors._handle_error(self, error_code)
        return

    def configure_scan_list(self, scanlist, scan_mode):
        '''configure_scan_list

        

        Args:
            scanlist (str):
            scan_mode (int):
        '''
        error_code = self.library.niSwitch_ConfigureScanList(self.vi, scanlist.encode('ascii'), scan_mode)
        errors._handle_error(self, error_code)
        return

    def configure_scan_trigger(self, scan_delay, trigger_input, scan_advanced_output):
        '''configure_scan_trigger

        

        Args:
            scan_delay (float):
            trigger_input (int):
            scan_advanced_output (int):
        '''
        error_code = self.library.niSwitch_ConfigureScanTrigger(self.vi, scan_delay, trigger_input, scan_advanced_output)
        errors._handle_error(self, error_code)
        return

    def connect(self, channel1, channel2):
        '''connect

        

        Args:
            channel1 (str):
            channel2 (str):
        '''
        error_code = self.library.niSwitch_Connect(self.vi, channel1.encode('ascii'), channel2.encode('ascii'))
        errors._handle_error(self, error_code)
        return

    def connect_multiple(self, connection_list):
        '''connect_multiple

        

        Args:
            connection_list (str):
        '''
        error_code = self.library.niSwitch_ConnectMultiple(self.vi, connection_list.encode('ascii'))
        errors._handle_error(self, error_code)
        return

    def disable(self):
        '''disable

        
        '''
        error_code = self.library.niSwitch_Disable(self.vi)
        errors._handle_error(self, error_code)
        return

    def disconnect(self, channel1, channel2):
        '''disconnect

        

        Args:
            channel1 (str):
            channel2 (str):
        '''
        error_code = self.library.niSwitch_Disconnect(self.vi, channel1.encode('ascii'), channel2.encode('ascii'))
        errors._handle_error(self, error_code)
        return

    def disconnect_all(self):
        '''disconnect_all

        
        '''
        error_code = self.library.niSwitch_DisconnectAll(self.vi)
        errors._handle_error(self, error_code)
        return

    def disconnect_multiple(self, disconnection_list):
        '''disconnect_multiple

        

        Args:
            disconnection_list (str):
        '''
        error_code = self.library.niSwitch_DisconnectMultiple(self.vi, disconnection_list.encode('ascii'))
        errors._handle_error(self, error_code)
        return

    def _get_attribute_vi_boolean(self, channel_name, attribute_id):
        '''_get_attribute_vi_boolean

        

        Args:
            channel_name (str):
            attribute_id (int):

        Returns:
            attribute_value (bool):
        '''
        attribute_value_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niSwitch_GetAttributeViBoolean(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViBoolean(attribute_value_ctype.value)

    def _get_attribute_vi_int32(self, channel_name, attribute_id):
        '''_get_attribute_vi_int32

        

        Args:
            channel_name (str):
            attribute_id (int):

        Returns:
            attribute_value (int):
        '''
        attribute_value_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niSwitch_GetAttributeViInt32(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViInt32(attribute_value_ctype.value)

    def _get_attribute_vi_real64(self, channel_name, attribute_id):
        '''_get_attribute_vi_real64

        

        Args:
            channel_name (str):
            attribute_id (int):

        Returns:
            attribute_value (float):
        '''
        attribute_value_ctype = ctypes_types.ViReal64_ctype(0)
        error_code = self.library.niSwitch_GetAttributeViReal64(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViReal64(attribute_value_ctype.value)

    def _get_attribute_vi_session(self, channel_name, attribute_id):
        '''_get_attribute_vi_session

        

        Args:
            channel_name (str):
            attribute_id (int):

        Returns:
            attribute_value (int):
        '''
        attribute_value_ctype = ctypes_types.ViSession_ctype(0)
        error_code = self.library.niSwitch_GetAttributeViSession(self.vi, channel_name.encode('ascii'), attribute_id, ctypes.pointer(attribute_value_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViSession(attribute_value_ctype.value)

    def _get_attribute_vi_string(self, channel_name, attribute_id):
        '''_get_attribute_vi_string

        

        Args:
            channel_name (str):
            attribute_id (int):
            array_size (int):
        '''
        array_size = 0
        attribute_value_ctype = None
        error_code = self.library.niSwitch_GetAttributeViString(self.vi, channel_name.encode('ascii'), attribute_id, array_size, attribute_value_ctype)
        # Don't use _handle_error, because positive value in error_code means size, not warning.
        if (errors._is_error(error_code)):
            raise errors.Error(self, error_code)
        array_size = error_code
        attribute_value_ctype = ctypes.cast(ctypes.create_string_buffer(array_size), ctypes_types.ViString_ctype)
        error_code = self.library.niSwitch_GetAttributeViString(self.vi, channel_name.encode('ascii'), attribute_id, array_size, attribute_value_ctype)
        errors._handle_error(self, error_code)
        return attribute_value_ctype.value.decode("ascii")

    def get_channel_name(self, index):
        '''get_channel_name

        

        Args:
            index (int):
            buffer_size (int):
        '''
        buffer_size = 0
        channel_name_buffer_ctype = None
        error_code = self.library.niSwitch_GetChannelName(self.vi, index, buffer_size, channel_name_buffer_ctype)
        # Don't use _handle_error, because positive value in error_code means size, not warning.
        if (errors._is_error(error_code)):
            raise errors.Error(self, error_code)
        buffer_size = error_code
        channel_name_buffer_ctype = ctypes.cast(ctypes.create_string_buffer(buffer_size), ctypes_types.ViString_ctype)
        error_code = self.library.niSwitch_GetChannelName(self.vi, index, buffer_size, channel_name_buffer_ctype)
        errors._handle_error(self, error_code)
        return channel_name_buffer_ctype.value.decode("ascii")

    def _get_error(self):
        '''_get_error

        

        Args:
            buffersize (int):

        Returns:
            code (int):
        '''
        code_ctype = ctypes_types.ViStatus_ctype(0)
        buffersize = 0
        description_ctype = None
        error_code = self.library.niSwitch_GetError(self.vi, ctypes.pointer(code_ctype), buffersize, description_ctype)
        # Don't use _handle_error, because positive value in error_code means size, not warning.
        if (errors._is_error(error_code)):
            raise errors.Error(self, error_code)
        buffersize = error_code
        description_ctype = ctypes.cast(ctypes.create_string_buffer(buffersize), ctypes_types.ViChar_ctype)
        error_code = self.library.niSwitch_GetError(self.vi, ctypes.pointer(code_ctype), buffersize, description_ctype)
        errors._handle_error(self, error_code)
        return python_types.ViStatus(code_ctype.value), description_ctype.value.decode("ascii")

    def get_next_coercion_record(self):
        '''get_next_coercion_record

        

        Args:
            buffer_size (int):
        '''
        buffer_size = 0
        coercion_record_ctype = None
        error_code = self.library.niSwitch_GetNextCoercionRecord(self.vi, buffer_size, coercion_record_ctype)
        # Don't use _handle_error, because positive value in error_code means size, not warning.
        if (errors._is_error(error_code)):
            raise errors.Error(self, error_code)
        buffer_size = error_code
        coercion_record_ctype = ctypes.cast(ctypes.create_string_buffer(buffer_size), ctypes_types.ViString_ctype)
        error_code = self.library.niSwitch_GetNextCoercionRecord(self.vi, buffer_size, coercion_record_ctype)
        errors._handle_error(self, error_code)
        return coercion_record_ctype.value.decode("ascii")

    def get_next_interchange_warning(self):
        '''get_next_interchange_warning

        

        Args:
            buffer_size (int):
        '''
        buffer_size = 0
        interchange_warning_ctype = None
        error_code = self.library.niSwitch_GetNextInterchangeWarning(self.vi, buffer_size, interchange_warning_ctype)
        # Don't use _handle_error, because positive value in error_code means size, not warning.
        if (errors._is_error(error_code)):
            raise errors.Error(self, error_code)
        buffer_size = error_code
        interchange_warning_ctype = ctypes.cast(ctypes.create_string_buffer(buffer_size), ctypes_types.ViString_ctype)
        error_code = self.library.niSwitch_GetNextInterchangeWarning(self.vi, buffer_size, interchange_warning_ctype)
        errors._handle_error(self, error_code)
        return interchange_warning_ctype.value.decode("ascii")

    def get_path(self, channel1, channel2):
        '''get_path

        

        Args:
            channel1 (str):
            channel2 (str):
            buffer_size (int):
        '''
        buffer_size = 0
        path_ctype = None
        error_code = self.library.niSwitch_GetPath(self.vi, channel1.encode('ascii'), channel2.encode('ascii'), buffer_size, path_ctype)
        # Don't use _handle_error, because positive value in error_code means size, not warning.
        if (errors._is_error(error_code)):
            raise errors.Error(self, error_code)
        buffer_size = error_code
        path_ctype = ctypes.cast(ctypes.create_string_buffer(buffer_size), ctypes_types.ViString_ctype)
        error_code = self.library.niSwitch_GetPath(self.vi, channel1.encode('ascii'), channel2.encode('ascii'), buffer_size, path_ctype)
        errors._handle_error(self, error_code)
        return path_ctype.value.decode("ascii")

    def get_relay_count(self, relay_name):
        '''get_relay_count

        

        Args:
            relay_name (str):

        Returns:
            relay_count (int):
        '''
        relay_count_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niSwitch_GetRelayCount(self.vi, relay_name.encode('ascii'), ctypes.pointer(relay_count_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViInt32(relay_count_ctype.value)

    def get_relay_name(self, index):
        '''get_relay_name

        

        Args:
            index (int):
            relay_name_buffer_size (int):
        '''
        relay_name_buffer_size = 0
        relay_name_buffer_ctype = None
        error_code = self.library.niSwitch_GetRelayName(self.vi, index, relay_name_buffer_size, relay_name_buffer_ctype)
        # Don't use _handle_error, because positive value in error_code means size, not warning.
        if (errors._is_error(error_code)):
            raise errors.Error(self, error_code)
        relay_name_buffer_size = error_code
        relay_name_buffer_ctype = ctypes.cast(ctypes.create_string_buffer(relay_name_buffer_size), ctypes_types.ViString_ctype)
        error_code = self.library.niSwitch_GetRelayName(self.vi, index, relay_name_buffer_size, relay_name_buffer_ctype)
        errors._handle_error(self, error_code)
        return relay_name_buffer_ctype.value.decode("ascii")

    def get_relay_position(self, relay_name):
        '''get_relay_position

        

        Args:
            relay_name (str):

        Returns:
            relay_position (int):
        '''
        relay_position_ctype = ctypes_types.ViInt32_ctype(0)
        error_code = self.library.niSwitch_GetRelayPosition(self.vi, relay_name.encode('ascii'), ctypes.pointer(relay_position_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViInt32(relay_position_ctype.value)

    def _init_with_options(self, resource_name, id_query, reset_device, options_string):
        '''_init_with_options

        

        Args:
            resource_name (str):
            id_query (bool):
            reset_device (bool):
            options_string (str):

        Returns:
            vi (int):
        '''
        vi_ctype = ctypes_types.ViSession_ctype(0)
        error_code = self.library.niSwitch_InitWithOptions(resource_name.encode('ascii'), id_query, reset_device, options_string.encode('ascii'), ctypes.pointer(vi_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViSession(vi_ctype.value)

    def init_with_topology(self, resource_name, topology, simulate, reset_device):
        '''init_with_topology

        

        Args:
            resource_name (str):
            topology (str):
            simulate (bool):
            reset_device (bool):

        Returns:
            vi (int):
        '''
        vi_ctype = ctypes_types.ViSession_ctype(0)
        error_code = self.library.niSwitch_InitWithTopology(resource_name.encode('ascii'), topology.encode('ascii'), simulate, reset_device, ctypes.pointer(vi_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViSession(vi_ctype.value)

    def _initiate_scan(self):
        '''_initiate_scan

        
        '''
        error_code = self.library.niSwitch_InitiateScan(self.vi)
        errors._handle_error(self, error_code)
        return

    def is_debounced(self):
        '''is_debounced

        

        Returns:
            is_debounced (bool):
        '''
        is_debounced_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niSwitch_IsDebounced(self.vi, ctypes.pointer(is_debounced_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViBoolean(is_debounced_ctype.value)

    def is_scanning(self):
        '''is_scanning

        

        Returns:
            is_scanning (bool):
        '''
        is_scanning_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niSwitch_IsScanning(self.vi, ctypes.pointer(is_scanning_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViBoolean(is_scanning_ctype.value)

    def _lock_session(self):
        '''_lock_session

        

        Returns:
            caller_has_lock (bool):
        '''
        caller_has_lock_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niSwitch_LockSession(self.vi, ctypes.pointer(caller_has_lock_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViBoolean(caller_has_lock_ctype.value)

    def relay_control(self, relay_name, relay_action):
        '''relay_control

        

        Args:
            relay_name (str):
            relay_action (int):
        '''
        error_code = self.library.niSwitch_RelayControl(self.vi, relay_name.encode('ascii'), relay_action)
        errors._handle_error(self, error_code)
        return

    def reset_interchange_check(self):
        '''reset_interchange_check

        
        '''
        error_code = self.library.niSwitch_ResetInterchangeCheck(self.vi)
        errors._handle_error(self, error_code)
        return

    def reset_with_defaults(self):
        '''reset_with_defaults

        
        '''
        error_code = self.library.niSwitch_ResetWithDefaults(self.vi)
        errors._handle_error(self, error_code)
        return

    def route_scan_advanced_output(self, scan_advanced_output_connector, scan_advanced_output_bus_line, invert):
        '''route_scan_advanced_output

        

        Args:
            scan_advanced_output_connector (int):
            scan_advanced_output_bus_line (int):
            invert (bool):
        '''
        error_code = self.library.niSwitch_RouteScanAdvancedOutput(self.vi, scan_advanced_output_connector, scan_advanced_output_bus_line, invert)
        errors._handle_error(self, error_code)
        return

    def route_trigger_input(self, trigger_input_connector, trigger_input_bus_line, invert):
        '''route_trigger_input

        

        Args:
            trigger_input_connector (int):
            trigger_input_bus_line (int):
            invert (bool):
        '''
        error_code = self.library.niSwitch_RouteTriggerInput(self.vi, trigger_input_connector, trigger_input_bus_line, invert)
        errors._handle_error(self, error_code)
        return

    def scan(self, scanlist, initiation):
        '''scan

        

        Args:
            scanlist (str):
            initiation (int):
        '''
        error_code = self.library.niSwitch_Scan(self.vi, scanlist.encode('ascii'), initiation)
        errors._handle_error(self, error_code)
        return

    def send_software_trigger(self):
        '''send_software_trigger

        
        '''
        error_code = self.library.niSwitch_SendSoftwareTrigger(self.vi)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value):
        '''_set_attribute_vi_boolean

        

        Args:
            channel_name (str):
            attribute_id (int):
            attribute_value (bool):
        '''
        error_code = self.library.niSwitch_SetAttributeViBoolean(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value):
        '''_set_attribute_vi_int32

        

        Args:
            channel_name (str):
            attribute_id (int):
            attribute_value (int):
        '''
        error_code = self.library.niSwitch_SetAttributeViInt32(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value):
        '''_set_attribute_vi_real64

        

        Args:
            channel_name (str):
            attribute_id (int):
            attribute_value (float):
        '''
        error_code = self.library.niSwitch_SetAttributeViReal64(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_session(self, channel_name, attribute_id, attribute_value):
        '''_set_attribute_vi_session

        

        Args:
            channel_name (str):
            attribute_id (int):
            attribute_value (int):
        '''
        error_code = self.library.niSwitch_SetAttributeViSession(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors._handle_error(self, error_code)
        return

    def _set_attribute_vi_string(self, channel_name, attribute_id, attribute_value):
        '''_set_attribute_vi_string

        

        Args:
            channel_name (str):
            attribute_id (int):
            attribute_value (int):
        '''
        error_code = self.library.niSwitch_SetAttributeViString(self.vi, channel_name.encode('ascii'), attribute_id, attribute_value)
        errors._handle_error(self, error_code)
        return

    def set_continuous_scan(self, continuous_scan):
        '''set_continuous_scan

        

        Args:
            continuous_scan (bool):
        '''
        error_code = self.library.niSwitch_SetContinuousScan(self.vi, continuous_scan)
        errors._handle_error(self, error_code)
        return

    def set_path(self, path_list):
        '''set_path

        

        Args:
            path_list (str):
        '''
        error_code = self.library.niSwitch_SetPath(self.vi, path_list.encode('ascii'))
        errors._handle_error(self, error_code)
        return

    def _unlock_session(self):
        '''_unlock_session

        

        Returns:
            caller_has_lock (bool):
        '''
        caller_has_lock_ctype = ctypes_types.ViBoolean_ctype(0)
        error_code = self.library.niSwitch_UnlockSession(self.vi, ctypes.pointer(caller_has_lock_ctype))
        errors._handle_error(self, error_code)
        return python_types.ViBoolean(caller_has_lock_ctype.value)

    def wait_for_debounce(self, maximum_time_ms):
        '''wait_for_debounce

        

        Args:
            maximum_time_ms (int):
        '''
        error_code = self.library.niSwitch_WaitForDebounce(self.vi, maximum_time_ms)
        errors._handle_error(self, error_code)
        return

    def wait_for_scan_complete(self, maximum_time_ms):
        '''wait_for_scan_complete

        

        Args:
            maximum_time_ms (int):
        '''
        error_code = self.library.niSwitch_WaitForScanComplete(self.vi, maximum_time_ms)
        errors._handle_error(self, error_code)
        return

    def _close(self):
        '''_close

        
        '''
        error_code = self.library.niSwitch_close(self.vi)
        errors._handle_error(self, error_code)
        return

    def error_message(self, error_code):
        '''error_message

        

        Args:
            error_code (int):

        Returns:
            error_message (int):
        '''
        error_message_ctype = (ctypes_types.ViChar_ctype * 256)()
        error_code = self.library.niSwitch_error_message(self.vi, error_code, ctypes.cast(error_message_ctype, ctypes.POINTER(ctypes_types.ViChar_ctype)))
        errors._handle_error(self, error_code)
        return error_message_ctype.value.decode("ascii")

    def error_query(self):
        '''error_query

        

        Returns:
            error_code (int):
            error_message (int):
        '''
        error_code_ctype = ctypes_types.ViInt32_ctype(0)
        error_message_ctype = (ctypes_types.ViChar_ctype * 256)()
        error_code = self.library.niSwitch_error_query(self.vi, ctypes.pointer(error_code_ctype), ctypes.cast(error_message_ctype, ctypes.POINTER(ctypes_types.ViChar_ctype)))
        errors._handle_error(self, error_code)
        return python_types.ViInt32(error_code_ctype.value), error_message_ctype.value.decode("ascii")

    def reset(self):
        '''reset

        
        '''
        error_code = self.library.niSwitch_reset(self.vi)
        errors._handle_error(self, error_code)
        return

    def revision_query(self):
        '''revision_query

        

        Returns:
            instrument_driver_revision (int):
            firmware_revision (int):
        '''
        instrument_driver_revision_ctype = (ctypes_types.ViChar_ctype * 256)()
        firmware_revision_ctype = (ctypes_types.ViChar_ctype * 256)()
        error_code = self.library.niSwitch_revision_query(self.vi, ctypes.cast(instrument_driver_revision_ctype, ctypes.POINTER(ctypes_types.ViChar_ctype)), ctypes.cast(firmware_revision_ctype, ctypes.POINTER(ctypes_types.ViChar_ctype)))
        errors._handle_error(self, error_code)
        return instrument_driver_revision_ctype.value.decode("ascii"), firmware_revision_ctype.value.decode("ascii")

    def self_test(self):
        '''self_test

        

        Returns:
            self_test_result (int):
            self_test_message (int):
        '''
        self_test_result_ctype = ctypes_types.ViInt16_ctype(0)
        self_test_message_ctype = (ctypes_types.ViChar_ctype * 256)()
        error_code = self.library.niSwitch_self_test(self.vi, ctypes.pointer(self_test_result_ctype), ctypes.cast(self_test_message_ctype, ctypes.POINTER(ctypes_types.ViChar_ctype)))
        errors._handle_error(self, error_code)
        return python_types.ViInt16(self_test_result_ctype.value), self_test_message_ctype.value.decode("ascii")

