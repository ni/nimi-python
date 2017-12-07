# -*- coding: utf-8 -*-
# This file was generated
import ctypes

from niswitch import attributes
from niswitch import enums
from niswitch import errors
from niswitch import library_singleton
from niswitch import visatype


class _Scan(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        self._session._initiate_scan()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session._abort_scan()


class _SessionBase(object):
    '''Base class for all NI-SWITCH sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    analog_bus_sharing_enable = attributes.AttributeViBoolean(1150018)
    '''
    Enables or disables sharing of an analog bus line so that multiple  NI SwitchBlock devices may connect to it simultaneously. To enable  multiple NI SwitchBlock devices to share an analog bus line, set this  attribute to VI_TRUE for each device on the channel that corresponds  with the shared analog bus line. The default value for all devices is  VI_FALSE, which disables sharing of the analog bus.
    Refer to the Using the Analog Bus on an NI SwitchBlock Carrier topic  in the NI Switches Help for more information about sharing the analog bus.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    analog_bus_sharing_enable.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    analog_bus_sharing_enable.Session instance, and calling set/get value on the result.:

        session['0,1'].analog_bus_sharing_enable = var
        var = session['0,1'].analog_bus_sharing_enable
    '''
    bandwidth = attributes.AttributeViReal64(1250005)
    '''
    This channel-based attribute returns the bandwidth for the channel.
    The units are hertz.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    bandwidth.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    bandwidth.Session instance, and calling set/get value on the result.:

        session['0,1'].bandwidth = var
        var = session['0,1'].bandwidth
    '''
    cabled_module_scan_advanced_bus = attributes.AttributeViInt32(1150009)
    '''
    This attribute has been deprecated and may be removed from a future release of  NI-SWITCH.  Use the niSwitch_RouteScanAdvancedOutput function instead.
    '''
    cabled_module_trigger_bus = attributes.AttributeViInt32(1150008)
    '''
    This attribute has been deprecated and may be removed from a future release of  NI-SWITCH.  Use the niSwitch_RouteTriggerInput function instead.
    '''
    cache = attributes.AttributeViBoolean(1050004)
    '''
    Specifies whether to cache the value of attributes.  When caching is  enabled, the instrument driver keeps track of the current instrument  settings and avoids sending redundant commands to the instrument.
    The instrument driver can choose always to cache or never to cache  particular attributes regardless of the setting of this attribute.
    The default value is VI_TRUE.   Use the niSwitch_InitWithOptions  function to override this value.
    '''
    channel_count = attributes.AttributeViInt32(1050203)
    '''
    Indicates the number of channels that the specific instrument  driver supports.
    '''
    characteristic_impedance = attributes.AttributeViReal64(1250016)
    '''
    This channel-based attribute returns the characteristic impedance for the  channel.
    The units are ohms.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    characteristic_impedance.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    characteristic_impedance.Session instance, and calling set/get value on the result.:

        session['0,1'].characteristic_impedance = var
        var = session['0,1'].characteristic_impedance
    '''
    continuous_scan = attributes.AttributeViBoolean(1150002)
    '''
    When a switch device is scanning, the swich can either stop scanning when  the end of the scan (VI_FALSE) or continue scanning from the top of the  scan list again (VI_TRUE).
    Notice that if you set the scan to continuous (VI_TRUE), the Wait For Scan  Complete operation will always time out and you must call Abort to stop  the scan.
    '''
    digital_filter_enable = attributes.AttributeViBoolean(1150016)
    '''
    This property specifies whether to apply the pulse width filter to the  Trigger Input. Enabling the Digital Filter (VI_TRUE) prevents the switch  module from being triggered by pulses that are less than 150 ns on PXI  trigger lines 0–7.
    When Digital Filter is disabled (VI_FALSE), it is possible for the switch  module to be triggered by noise on the PXI trigger lines. If the device  triggering the switch is capable of sending pulses greater than 150 ns, you should not disable the Digital Filter.
    '''
    driver_setup = attributes.AttributeViString(1050007)
    '''
    This attribute indicates the Driver Setup string that the user  specified when initializing the driver.
    Some cases exist where the end-user must specify instrument driver  options at initialization time.  An example of this is specifying  a particular instrument model from among a family of instruments  that the driver supports.  This is useful when using simulation.   The end-user can specify driver-specific options through  the DriverSetup keyword in the optionsString parameter to the  niSwitch_InitWithOptions function, or through the IVI Configuration Utility.
    If the user does not specify a Driver Setup string, this attribute returns an empty string.
    '''
    group_capabilities = attributes.AttributeViString(1050401)
    '''
    A string that contains a comma-separated list of class-extention groups that  this driver implements.
    '''
    handshaking_initiation = attributes.AttributeEnum(attributes.AttributeViInt32, enums.HandshakingInitiation, 1150013)
    instrument_firmware_revision = attributes.AttributeViString(1050510)
    '''
    A string that contains the firmware revision information  for the instrument you are currently using.
    '''
    instrument_manufacturer = attributes.AttributeViString(1050511)
    '''
    A string that contains the name of the instrument manufacturer you are currently  using.
    '''
    instrument_model = attributes.AttributeViString(1050512)
    '''
    A string that contains the model number or name of the instrument that you  are currently using.
    '''
    interchange_check = attributes.AttributeViBoolean(1050021)
    '''
    Specifies whether to perform interchangeability checking and retrieve  interchangeability warnings when you call  niSwitch_Connect, niSwitch_SetPath and niSwitch_InitiateScan functions.
    The default value is VI_FALSE.
    Interchangeability warnings indicate that using your application with a  different instrument might cause different behavior.   You call niSwitch_GetNextInterchangeWarning to extract interchange warnings.   Call the niSwitch_ClearInterchangeWarnings function to clear the list  of interchangeability warnings without reading them.
    Interchangeability checking examines the attributes in a  capability group only if you specify a value for at least one  attribute within that group.  Interchangeability warnings can  occur when an attribute affects the behavior of the instrument and you  have not set that attribute, or the attribute has been invalidated since you set it.
    '''
    io_resource_descriptor = attributes.AttributeViString(1050304)
    '''
    Indicates the resource descriptor the driver  uses to identify the physical device.
    If you initialize the driver with a logical name, this  attribute contains the resource descriptor that corresponds  to the entry in the IVI Configuration utility.
    If you initialize the instrument driver with the resource  descriptor, this attribute contains that value.
    '''
    is_configuration_channel = attributes.AttributeViBoolean(1250003)
    '''
    This channel-based attribute specifies whether to reserve the channel for  internal path creation.  A channel that is available for internal path  creation is called a configuration channel.  The driver may use  configuration channels to create paths between two channels you specify in  the niSwitch_Connect function.  Configuration channels are not available  for external connections.
    Set this attribute to VI_TRUE to mark the channel as a configuration  channel.  Set this attribute to VI_FALSE to mark the channel as available  for external connections.
    After you identify a channel as a configuration channel, you cannot  use that channel for external connections.  The niSwitch_Connect function  returns the NISWITCH_ERROR_IS_CONFIGURATION_CHANNEL error when you attempt  to establish a connection between a configuration channel and any other  channel.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    is_configuration_channel.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    is_configuration_channel.Session instance, and calling set/get value on the result.:

        session['0,1'].is_configuration_channel = var
        var = session['0,1'].is_configuration_channel
    '''
    is_debounced = attributes.AttributeViBoolean(1250002)
    '''
    This attribute indicates whether the entire switch device has settled  since the last switching command.  A value of VI_TRUE indicates that all  signals going through the switch device are valid.
    '''
    is_scanning = attributes.AttributeViBoolean(1250024)
    '''
    If VI_TRUE, the switch module is currently scanning through the scan list  (i.e. it is not in the Idle state). If VI_FALSE, the switch module is not  currently scanning through the scan list (i.e. it is in the Idle state).
    '''
    is_source_channel = attributes.AttributeViBoolean(1250001)
    '''
    This channel-based attribute specifies whether you want to identify the  channel as a source channel.  Typically, you set this attribute to VI_TRUE  when you attach the channel to a power supply, a function generator, or an  active measurement point on the unit under test, and you do not want to  connect the channel to another source.  The driver prevents source  channels from connecting to each other.  The niSwitch_Connect function  returns the NISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES when you attempt to  connect two channels that you identify as source channels.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    is_source_channel.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    is_source_channel.Session instance, and calling set/get value on the result.:

        session['0,1'].is_source_channel = var
        var = session['0,1'].is_source_channel
    '''
    is_waiting_for_trig = attributes.AttributeViBoolean(1150004)
    '''
    In a scan list, a semi-colon (;) is used to indicate that at that point in  the scan list, the scan engine should pause until a trigger is received  from the trigger input.  If that trigger is user generated through either  a hardware pulse or the Send SW Trigger operation, it is necessary for the  user to know  when the scan engine has reached such a state.
    '''
    logical_name = attributes.AttributeViString(1050305)
    '''
    A string containing the logical name you specified when opening the  current IVI session.
    You may pass a logical name to the niSwitch_init or  niSwitch_InitWithOptions functions.   The IVI Configuration utility must contain an entry for the logical name.   The logical name entry refers to a virtual instrument section in the  IVI Configuration file.  The virtual instrument section specifies a physical  device and initial user options.
    '''
    master_slave_scan_advanced_bus = attributes.AttributeViInt32(1150007)
    '''
    This attribute has been deprecated and may be removed from a future release of  NI-SWITCH.  Use the niSwitch_RouteScanAdvancedOutput function instead.
    '''
    master_slave_trigger_bus = attributes.AttributeViInt32(1150006)
    '''
    This attribute has been deprecated and may be removed from a future release of  NI-SWITCH.  Use the niSwitch_RouteTriggerInput function instead.
    '''
    max_ac_voltage = attributes.AttributeViReal64(1250007)
    '''
    This channel-based attribute returns the maximum AC voltage the channel  can switch.
    The units are volts RMS.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    max_ac_voltage.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    max_ac_voltage.Session instance, and calling set/get value on the result.:

        session['0,1'].max_ac_voltage = var
        var = session['0,1'].max_ac_voltage
    '''
    max_carry_ac_current = attributes.AttributeViReal64(1250011)
    '''
    This channel-based attribute returns the maximum AC current the channel  can carry.
    The units are amperes RMS.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    max_carry_ac_current.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    max_carry_ac_current.Session instance, and calling set/get value on the result.:

        session['0,1'].max_carry_ac_current = var
        var = session['0,1'].max_carry_ac_current
    '''
    max_carry_ac_power = attributes.AttributeViReal64(1250015)
    '''
    This channel-based attribute returns the maximum AC power the channel can  carry.
    The units are volt-amperes.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    max_carry_ac_power.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    max_carry_ac_power.Session instance, and calling set/get value on the result.:

        session['0,1'].max_carry_ac_power = var
        var = session['0,1'].max_carry_ac_power
    '''
    max_carry_dc_current = attributes.AttributeViReal64(1250010)
    '''
    This channel-based attribute returns the maximum DC current the channel  can carry.
    The units are amperes.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    max_carry_dc_current.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    max_carry_dc_current.Session instance, and calling set/get value on the result.:

        session['0,1'].max_carry_dc_current = var
        var = session['0,1'].max_carry_dc_current
    '''
    max_carry_dc_power = attributes.AttributeViReal64(1250014)
    '''
    This channel-based attribute returns the maximum DC power the channel can  carry.
    The units are watts.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    max_carry_dc_power.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    max_carry_dc_power.Session instance, and calling set/get value on the result.:

        session['0,1'].max_carry_dc_power = var
        var = session['0,1'].max_carry_dc_power
    '''
    max_dc_voltage = attributes.AttributeViReal64(1250006)
    '''
    This channel-based attribute returns the maximum DC voltage the channel  can switch.
    The units are volts.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    max_dc_voltage.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    max_dc_voltage.Session instance, and calling set/get value on the result.:

        session['0,1'].max_dc_voltage = var
        var = session['0,1'].max_dc_voltage
    '''
    max_switching_ac_current = attributes.AttributeViReal64(1250009)
    '''
    This channel-based attribute returns the maximum AC current the channel  can switch.
    The units are amperes RMS.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    max_switching_ac_current.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    max_switching_ac_current.Session instance, and calling set/get value on the result.:

        session['0,1'].max_switching_ac_current = var
        var = session['0,1'].max_switching_ac_current
    '''
    max_switching_ac_power = attributes.AttributeViReal64(1250013)
    '''
    This channel-based attribute returns the maximum AC power the channel can  switch.
    The units are volt-amperes.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    max_switching_ac_power.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    max_switching_ac_power.Session instance, and calling set/get value on the result.:

        session['0,1'].max_switching_ac_power = var
        var = session['0,1'].max_switching_ac_power
    '''
    max_switching_dc_current = attributes.AttributeViReal64(1250008)
    '''
    This channel-based attribute returns the maximum DC current the channel  can switch.
    The units are amperes.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    max_switching_dc_current.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    max_switching_dc_current.Session instance, and calling set/get value on the result.:

        session['0,1'].max_switching_dc_current = var
        var = session['0,1'].max_switching_dc_current
    '''
    max_switching_dc_power = attributes.AttributeViReal64(1250012)
    '''
    This channel-based attribute returns the maximum DC power the channel can  switch.
    The units are watts.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    max_switching_dc_power.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    max_switching_dc_power.Session instance, and calling set/get value on the result.:

        session['0,1'].max_switching_dc_power = var
        var = session['0,1'].max_switching_dc_power
    '''
    number_of_relays = attributes.AttributeViInt32(1150014)
    '''
    This attribute returns the number of relays.
    '''
    num_of_columns = attributes.AttributeViInt32(1250019)
    '''
    This attribute returns the number of channels on the column of a matrix or  scanner.  If the switch device is a scanner, this value is the number of  input channels.
    The NISWITCH_ATTR_WIRE_MODE attribute affects the number of available  columns.  For example, if your device has 8 input lines and you use the  four-wire mode, then the number of columns you have available is 2.
    '''
    num_of_rows = attributes.AttributeViInt32(1250018)
    '''
    This attribute returns the number of channels on the row of a matrix or  scanner.  If the switch device is a scanner, this value is the number of  output channels.
    The NISWITCH_ATTR_WIRE_MODE attribute affects the number of available  rows.  For example, if your device has 8 input lines and you use the  two-wire mode, then the number of columns you have available is 4.
    '''
    parsed_scan_list = attributes.AttributeViString(1150012)
    '''
    This attribute has been deprecated and may be removed from a future release of  NI-SWITCH.
    '''
    power_down_latching_relays_after_debounce = attributes.AttributeViBoolean(1150017)
    '''
    This property specifies whether to power down latching relays after  calling Wait For Debounce.
    When Power Down Latching Relays After Debounce is enabled (VI_TRUE),  a call to Wait For Debounce ensures that the relays are settled  and the latching relays are powered down.
    '''
    query_instrument_status = attributes.AttributeViBoolean(1050003)
    '''
    Specifies whether the instrument driver queries the instrument status  after each operation.  Querying the instrument status is very useful for  debugging.  After you validate your program, you can set this attribute to  VI_FALSE to disable status checking and maximize performance
    The instrument driver can choose to ignore status checking for  particular attributes regardless of the setting of this attribute.
    The default value is VI_TRUE.   Use the niSwitch_InitWithOptions  function to override this value.
    '''
    range_check = attributes.AttributeViBoolean(1050002)
    '''
    Specifies whether to validate attribute values and function parameters.   If enabled, the instrument driver validates the parameter values that  you pass to driver functions.  Range checking  parameters is very useful for debugging.  After you validate your program,  you can set this attribute to VI_FALSE to disable range checking and  maximize performance.
    The default value is VI_TRUE.   Use the niSwitch_InitWithOptions  function to override this value.
    '''
    record_coercions = attributes.AttributeViBoolean(1050006)
    '''
    Specifies whether the IVI engine keeps a list of  the value coercions it makes for ViInt32 and ViReal64 attributes.   You call niSwitch_GetNextCoercionRecord to extract and delete the oldest  coercion record from the list.
    The default value is VI_FALSE.   Use the  niSwitch_InitWithOptions function to override this value.
    '''
    scan_advanced_output = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ScanAdvancedOutput, 1250023)
    '''
    This attribute specifies the method you want to use to notify another  instrument that all signals going through the switch device have settled  following the processing of one entry in the scan list.
    '''
    scan_advanced_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ScanAdvancedPolarity, 1150011)
    scan_delay = attributes.AttributeViReal64(1250025)
    '''
    This attribute specifies the minimum amount of time the switch device  waits before it asserts the scan advanced output trigger after opening or  closing the switch.  The switch device always waits for debounce before  asserting the trigger. The units are seconds.
    the greater value of the settling time and the value you specify as the  scan delay.

    Note: NI PXI-2501/2503/2565/2590/2591 Users--the actual delay will always be
    '''
    scan_list = attributes.AttributeViString(1250020)
    '''
    This attribute contains a scan list, which is a string that specifies  channel connections and trigger conditions.  The niSwitch_InitiateScan  function makes or breaks connections and waits for triggers according to  the instructions in the scan list.
    The scan list is comprised of channel names that you separate with  special characters.  These special characters determine the operations the  scanner performs on the channels when it executes this scan list.
    To create a path between two channels, use the following character between  the two channel names:
    -> (a dash followed by a '>' sign)
    Example:  'CH1->CH2' tells the switch to make a path from channel CH1 to channel  CH2.
    To break or clear a path, use the following character as a prefix before  the path:
    ~ (tilde)
    Example:  '~CH1->CH2' tells the switch to break the path from channel CH1 to  channel CH2.
    To tell the switch device to wait for a trigger event, use the following  character as a separator between paths:
    ; (semi-colon)
    Example:  'CH1->CH2;CH3->CH4' tells the switch to make the path from channel CH1  to channel CH2, wait for a trigger, and then make the path from CH3 to  CH4.
    '''
    scan_mode = attributes.AttributeEnum(attributes.AttributeViInt32, enums.ScanMode, 1250021)
    '''
    This attribute specifies what happens to existing connections that  conflict with the connections you make in a scan list.  For example, if  CH1 is already connected to CH2 and the scan list instructs the switch  device to connect CH1 to CH3, this attribute specifies what happens to the  connection between CH1 and CH2.
    If the value of this attribute is NISWITCH_VAL_NONE, the switch device  takes no action on existing paths.  If the value is  NISWITCH_VAL_BREAK_BEFORE_MAKE, the switch device breaks conflicting paths  before making new ones.  If the value is NISWITCH_VAL_BREAK_AFTER_MAKE,  the switch device breaks conflicting paths after making new ones.
    Most switch devices support only one of the possible values.  In such  cases, this attribute serves as an indicator of the device's behavior.
    '''
    serial_number = attributes.AttributeViString(1150015)
    '''
    This read-only attribute returns the serial number for the switch device  controlled by this instrument driver.  If the device does not return a  serial number, the driver returns the IVI_ERROR_ATTRIBUTE_NOT_SUPPORTED error.
    '''
    settling_time = attributes.AttributeViReal64(1250004)
    '''
    This channel-based attribute returns the maximum length of time from after  you make a connection until the signal flowing through the channel  settles. The units are seconds.
    the greater value of the settling time and the value you specify as the  scan delay.

    Note: NI PXI-2501/2503/2565/2590/2591 Users--the actual delay will always be

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    settling_time.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    settling_time.Session instance, and calling set/get value on the result.:

        session['0,1'].settling_time = var
        var = session['0,1'].settling_time
    '''
    simulate = attributes.AttributeViBoolean(1050005)
    '''
    Specifies whether or not to simulate instrument driver I/O operations.  If  simulation is enabled, instrument driver functions perform range checking  and call Ivi_GetAttribute and Ivi_SetAttribute functions, but they do not  perform instrument I/O.  For output parameters that represent instrument  data, the instrument driver functions return calculated values.
    The default value is VI_FALSE.   Use the niSwitch_InitWithOptions  function to override this value.
    '''
    specific_driver_class_spec_major_version = attributes.AttributeViInt32(1050515)
    '''
    The major version number of the IviSwtch class specification.
    '''
    specific_driver_class_spec_minor_version = attributes.AttributeViInt32(1050516)
    '''
    The minor version number of the class specification with which this driver is compliant.
    '''
    specific_driver_description = attributes.AttributeViString(1050514)
    '''
    A string that contains a brief description of the specific  driver.
    '''
    specific_driver_prefix = attributes.AttributeViString(1050302)
    '''
    A string that contains the prefix for the instrument driver.  The name of each  user-callable function in this driver starts with this prefix.
    '''
    specific_driver_revision = attributes.AttributeViString(1050551)
    '''
    A string that contains additional version information about this  instrument driver.
    '''
    specific_driver_vendor = attributes.AttributeViString(1050513)
    '''
    A string that contains the name of the vendor that supplies this driver.
    '''
    supported_instrument_models = attributes.AttributeViString(1050327)
    '''
    Contains a comma-separated list of supported instrument models.
    '''
    temperature = attributes.AttributeViReal64(1150019)
    '''
    This attribute returns the temperature as read by the Switch module.     The units are degrees Celsius.
    '''
    trigger_input = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerInput, 1250022)
    '''
    This attribute specifies the source of the trigger for which the switch  device can wait when processing a scan list.  The switch device waits for  a trigger when it encounters a semi-colon in a scan list.  When the trigger  occurs, the switch device advances to the next entry in the scan list.
    '''
    trigger_input_polarity = attributes.AttributeEnum(attributes.AttributeViInt32, enums.TriggerInputPolarity, 1150010)
    '''
    Determines the behavior of the trigger Input.
    '''
    trigger_mode = attributes.AttributeViInt32(1150005)
    '''
    This attribute has been deprecated and may be removed from a future release of  NI-SWITCH.  Use the niSwitch_RouteTriggerInput and/or niSwitch_RouteScanAdvancedOutput  functions instead.
    '''
    wire_mode = attributes.AttributeViInt32(1250017)
    '''
    This attribute returns the wire mode of the switch device.
    This attribute affects the values of the NISWITCH_ATTR_NUM_OF_ROWS and  NISWITCH_ATTR_NUM_OF_COLUMNS attributes.   The actual number of input and  output lines on the switch device is fixed, but the number of channels  depends on how many lines constitute each channel.

    Tip:
    This property can use repeated capabilities (usually channels). If set or get directly on the
    wire_mode.Session object, then the set/get will use all repeated capabilities in the session.
    You can specify a subset of repeated capabilities using the Python index notation on an
    wire_mode.Session instance, and calling set/get value on the result.:

        session['0,1'].wire_mode = var
        var = session['0,1'].wire_mode
    '''

    def __init__(self, repeated_capability):
        self._library = library_singleton.get()
        self._repeated_capability = repeated_capability
        self._encoding = 'windows-1251'

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    def _get_error_description(self, error_code):
        '''_get_error_description

        Returns the error description.
        '''
        try:
            _, error_string = self._get_error()
            return error_string
        except errors.Error:
            pass

        try:
            '''
            It is expected for _get_error to raise when the session is invalid
            (IVI spec requires GetError to fail).
            Use _error_message instead. It doesn't require a session.
            '''
            error_string = self._error_message(error_code)
            return error_string
        except errors.Error:
            return "Failed to retrieve error description."

    ''' These are code-generated '''

    def _get_attribute_vi_boolean(self, attribute_id):
        '''_get_attribute_vi_boolean

        This function queries the value of a ViBoolean attribute. You can use
        this function to get the values of instrument specific attributes and
        inherent IVI attributes. If the attribute represents an instrument
        state, this function performs instrument I/O in the following cases: -
        State caching is disabled for the entire session or for the particular
        attribute. - State caching is enabled and the currently cached value is
        invalid.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niswitch.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niswitch.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_boolean(attribute_id)

        Args:
            attribute_id (int): Pass the ID of an attribute. From the function panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                attributes. Attributes whose value cannot be set are dim. Help text is
                shown for each attribute. Select an attribute by double-clicking on it
                or by selecting it and then pressing . A ring control at the top of the
                dialog box allows you to see all IVI attributes or only the attributes
                of the ViInt32 type. If you choose to see all IVI attributes, the data
                types appear to the right of the attribute names in the list box. The
                data types that are not consistent with this function are dim. If you
                select an attribute data type that is dim, LabWindows/CVI transfers you
                to the function panel for the corresponding function that is consistent
                with the data type. - If you want to enter a variable name, press to
                change this ring control to a manual input box. - If the attribute in
                this ring control has constants as valid values, you can view the
                constants by moving to the Attribute Value control and pressing .

        Returns:
            attribute_value (bool): Returns the current value of the attribute. Pass the address of a
                ViBoolean variable. From the function panel window, you can use this
                control as follows. - If the attribute currently showing in the
                Attribute ID ring control has constants as valid values, you can view a
                list of the constants by pressing on this control. Select a value by
                double-clicking on it or by selecting it and then pressing .
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViBoolean()  # case 14
        error_code = self._library.niSwitch_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def _get_attribute_vi_int32(self, attribute_id):
        '''_get_attribute_vi_int32

        This function queries the value of a ViInt32 attribute. You can use this
        function to get the values of instrument specific attributes and
        inherent IVI attributes. If the attribute represents an instrument
        state, this function performs instrument I/O in the following cases: -
        State caching is disabled for the entire session or for the particular
        attribute. - State caching is enabled and the currently cached value is
        invalid.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niswitch.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niswitch.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_int32(attribute_id)

        Args:
            attribute_id (int): Pass the ID of an attribute. From the function panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                attributes. Attributes whose value cannot be set are dim. Help text is
                shown for each attribute. Select an attribute by double-clicking on it
                or by selecting it and then pressing . A ring control at the top of the
                dialog box allows you to see all IVI attributes or only the attributes
                of the ViInt32 type. If you choose to see all IVI attributes, the data
                types appear to the right of the attribute names in the list box. The
                data types that are not consistent with this function are dim. If you
                select an attribute data type that is dim, LabWindows/CVI transfers you
                to the function panel for the corresponding function that is consistent
                with the data type. - If you want to enter a variable name, press to
                change this ring control to a manual input box. - If the attribute in
                this ring control has constants as valid values, you can view the
                constants by moving to the Attribute Value control and pressing .

        Returns:
            attribute_value (int): Returns the current value of the attribute. Pass the address of a
                ViInt32 variable. From the function panel window, you can use this
                control as follows. - If the attribute currently showing in the
                Attribute ID ring control has constants as valid values, you can view a
                list of the constants by pressing on this control. Select a value by
                double-clicking on it or by selecting it and then pressing .
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViInt32()  # case 14
        error_code = self._library.niSwitch_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def _get_attribute_vi_real64(self, attribute_id):
        '''_get_attribute_vi_real64

        This function queries the value of a ViReal64 attribute. You can use
        this function to get the values of instrument specific attributes and
        inherent IVI attributes. If the attribute represents an instrument
        state, this function performs instrument I/O in the following cases: -
        State caching is disabled for the entire session or for the particular
        attribute. - State caching is enabled and the currently cached value is
        invalid.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niswitch.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niswitch.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_real64(attribute_id)

        Args:
            attribute_id (int): Pass the ID of an attribute. From the function panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                attributes. Attributes whose value cannot be set are dim. Help text is
                shown for each attribute. Select an attribute by double-clicking on it
                or by selecting it and then pressing . A ring control at the top of the
                dialog box allows you to see all IVI attributes or only the attributes
                of the ViInt32 type. If you choose to see all IVI attributes, the data
                types appear to the right of the attribute names in the list box. The
                data types that are not consistent with this function are dim. If you
                select an attribute data type that is dim, LabWindows/CVI transfers you
                to the function panel for the corresponding function that is consistent
                with the data type. - If you want to enter a variable name, press to
                change this ring control to a manual input box. - If the attribute in
                this ring control has constants as valid values, you can view the
                constants by moving to the Attribute Value control and pressing .

        Returns:
            attribute_value (float): Returns the current value of the attribute. Pass the address of a
                ViReal64 variable. From the function panel window, you can use this
                control as follows. - If the attribute currently showing in the
                Attribute ID ring control has constants as valid values, you can view a
                list of the constants by pressing on this control. Select a value by
                double-clicking on it or by selecting it and then pressing .
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViReal64()  # case 14
        error_code = self._library.niSwitch_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, ctypes.pointer(attribute_value_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def _get_attribute_vi_string(self, attribute_id):
        '''_get_attribute_vi_string

        This function queries the value of a ViString attribute. You can use
        this function to get the values of instrument specific attributes and
        inherent IVI attributes. If the attribute represents an instrument
        state, this function performs instrument I/O in the following cases: -
        State caching is disabled for the entire session or for the particular
        attribute. - State caching is enabled and the currently cached value is
        invalid. You must provide a ViChar array to serve as a buffer for the
        value. You pass the number of bytes in the buffer as the Array Size
        parameter. If the current value of the attribute, including the
        terminating NULL byte, is larger than the size you indicate in the Array
        Size parameter, the function copies Array Size-1 bytes into the buffer,
        places an ASCII NULL byte at the end of the buffer, and returns the
        array size you must pass to get the entire value. For example, if the
        value is "123456" and the Array Size is 4, the function places "123"
        into the buffer and returns 7. If you want to call this function just to
        get the required array size, you can pass 0 for the Array Size and
        VI_NULL for the Attribute Value buffer. If you want the function to
        fill in the buffer regardless of the number of bytes in the value, pass
        a negative number for the Array Size parameter.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niswitch.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niswitch.Session instance, and calling this method on the result.:

            session['0,1']._get_attribute_vi_string(attribute_id)

        Args:
            attribute_id (int): Pass the ID of an attribute. From the function panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                attributes. Attributes whose value cannot be set are dim. Help text is
                shown for each attribute. Select an attribute by double-clicking on it
                or by selecting it and then pressing . A ring control at the top of the
                dialog box allows you to see all IVI attributes or only the attributes
                of the ViInt32 type. If you choose to see all IVI attributes, the data
                types appear to the right of the attribute names in the list box. The
                data types that are not consistent with this function are dim. If you
                select an attribute data type that is dim, LabWindows/CVI transfers you
                to the function panel for the corresponding function that is consistent
                with the data type. - If you want to enter a variable name, press to
                change this ring control to a manual input box. - If the attribute in
                this ring control has constants as valid values, you can view the
                constants by moving to the Attribute Value control and pressing .
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        array_size_ctype = visatype.ViInt32()  # case 7
        attribute_value_ctype = None  # case 12
        error_code = self._library.niSwitch_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, array_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        array_size_ctype = visatype.ViInt32(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        attribute_value_ctype = (visatype.ViChar * array_size_ctype.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_code = self._library.niSwitch_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, array_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def _get_error(self):
        '''_get_error

        This function retrieves and then clears the IVI error information for
        the session or the current execution thread. One exception exists: If
        the buffer_size parameter is 0, the function does not clear the error
        information. By passing 0 for the buffer size, the caller can ascertain
        the buffer size required to get the entire error description string and
        then call the function again with a sufficiently large buffer. If the
        user specifies a valid IVI session for the InstrumentHandle parameter,
        Get Error retrieves and then clears the error information for the
        session. If the user passes VI_NULL for the InstrumentHandle parameter,
        this function retrieves and then clears the error information for the
        current execution thread. If the InstrumentHandle parameter is an
        invalid session, the function does nothing and returns an error.
        Normally, the error information describes the first error that occurred
        since the user last called _get_error or ClearError.

        Returns:
            code (int): Returns the error code for the session or execution thread. If you pass
                0 for the Buffer Size, you can pass VI_NULL for this parameter.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        code_ctype = visatype.ViStatus()  # case 14
        buffer_size_ctype = visatype.ViInt32()  # case 7
        description_ctype = None  # case 12
        error_code = self._library.niSwitch_GetError(vi_ctype, ctypes.pointer(code_ctype), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        buffer_size_ctype = visatype.ViInt32(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        description_ctype = (visatype.ViChar * buffer_size_ctype.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_code = self._library.niSwitch_GetError(vi_ctype, ctypes.pointer(code_ctype), buffer_size_ctype, description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(code_ctype.value), description_ctype.value.decode(self._encoding)

    def _set_attribute_vi_boolean(self, attribute_id, attribute_value):
        '''_set_attribute_vi_boolean

        This function sets the value of a ViBoolean attribute. This is a
        low-level function that you can use to set the values of
        instrument-specific attributes and inherent IVI attributes. If the
        attribute represents an instrument state, this function performs
        instrument I/O in the following cases: - State caching is disabled for
        the entire session or for the particular attribute. - State caching is
        enabled and the currently cached value is invalid or is different than
        the value you specify. This instrument driver contains high-level
        functions that set most of the instrument attributes. It is best to use
        the high-level driver functions as much as possible. They handle order
        dependencies and multithread locking for you. In addition, they perform
        status checking only after setting all of the attributes. In contrast,
        when you set multiple attributes using the SetAttribute functions, the
        functions check the instrument status after each call. Also, when state
        caching is enabled, the high-level functions that configure multiple
        attributes perform instrument I/O only for the attributes whose value
        you change. Thus, you can safely call the high-level functions without
        the penalty of redundant instrument I/O.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niswitch.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niswitch.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_boolean(attribute_id, attribute_value)

        Args:
            attribute_id (int): Pass the ID of an attribute. From the function panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                attributes. Attributes whose value cannot be set are dim. Help text is
                shown for each attribute. Select an attribute by double-clicking on it
                or by selecting it and then pressing . Read-only attributes appear dim
                in the list box. If you select a read-only attribute, an error message
                appears. A ring control at the top of the dialog box allows you to see
                all IVI attributes or only the attributes of the ViInt32 type. If you
                choose to see all IVI attributes, the data types appear to the right of
                the attribute names in the list box. The data types that are not
                consistent with this function are dim. If you select an attribute data
                type that is dim, LabWindows/CVI transfers you to the function panel for
                the corresponding function that is consistent with the data type. - If
                you want to enter a variable name, press to change this ring control to
                a manual input box. - If the attribute in this ring control has
                constants as valid values, you can view the constants by moving to the
                Attribute Value control and pressing .
            attribute_value (bool): Pass the value to which you want to set the attribute. From the function
                panel window, you can use this control as follows. - If the attribute
                currently showing in the Attribute ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing . Note: Some of the values might not be valid depending on
                the current settings of the instrument session. Default Value: none
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViBoolean(attribute_value)  # case 9
        error_code = self._library.niSwitch_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_int32(self, attribute_id, attribute_value):
        '''_set_attribute_vi_int32

        This function sets the value of a ViInt32 attribute. This is a low-level
        function that you can use to set the values of instrument-specific
        attributes and inherent IVI attributes. If the attribute represents an
        instrument state, this function performs instrument I/O in the following
        cases: - State caching is disabled for the entire session or for the
        particular attribute. - State caching is enabled and the currently
        cached value is invalid or is different than the value you specify. This
        instrument driver contains high-level functions that set most of the
        instrument attributes. It is best to use the high-level driver functions
        as much as possible. They handle order dependencies and multithread
        locking for you. In addition, they perform status checking only after
        setting all of the attributes. In contrast, when you set multiple
        attributes using the SetAttribute functions, the functions check the
        instrument status after each call. Also, when state caching is enabled,
        the high-level functions that configure multiple attributes perform
        instrument I/O only for the attributes whose value you change. Thus, you
        can safely call the high-level functions without the penalty of
        redundant instrument I/O.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niswitch.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niswitch.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_int32(attribute_id, attribute_value)

        Args:
            attribute_id (int): Pass the ID of an attribute. From the function panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                attributes. Attributes whose value cannot be set are dim. Help text is
                shown for each attribute. Select an attribute by double-clicking on it
                or by selecting it and then pressing . Read-only attributes appear dim
                in the list box. If you select a read-only attribute, an error message
                appears. A ring control at the top of the dialog box allows you to see
                all IVI attributes or only the attributes of the ViInt32 type. If you
                choose to see all IVI attributes, the data types appear to the right of
                the attribute names in the list box. The data types that are not
                consistent with this function are dim. If you select an attribute data
                type that is dim, LabWindows/CVI transfers you to the function panel for
                the corresponding function that is consistent with the data type. - If
                you want to enter a variable name, press to change this ring control to
                a manual input box. - If the attribute in this ring control has
                constants as valid values, you can view the constants by moving to the
                Attribute Value control and pressing .
            attribute_value (int): Pass the value to which you want to set the attribute. From the function
                panel window, you can use this control as follows. - If the attribute
                currently showing in the Attribute ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing . Note: Some of the values might not be valid depending on
                the current settings of the instrument session. Default Value: none
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViInt32(attribute_value)  # case 9
        error_code = self._library.niSwitch_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_real64(self, attribute_id, attribute_value):
        '''_set_attribute_vi_real64

        This function sets the value of a ViReal64 attribute. This is a
        low-level function that you can use to set the values of
        instrument-specific attributes and inherent IVI attributes. If the
        attribute represents an instrument state, this function performs
        instrument I/O in the following cases: - State caching is disabled for
        the entire session or for the particular attribute. - State caching is
        enabled and the currently cached value is invalid or is different than
        the value you specify. This instrument driver contains high-level
        functions that set most of the instrument attributes. It is best to use
        the high-level driver functions as much as possible. They handle order
        dependencies and multithread locking for you. In addition, they perform
        status checking only after setting all of the attributes. In contrast,
        when you set multiple attributes using the SetAttribute functions, the
        functions check the instrument status after each call. Also, when state
        caching is enabled, the high-level functions that configure multiple
        attributes perform instrument I/O only for the attributes whose value
        you change. Thus, you can safely call the high-level functions without
        the penalty of redundant instrument I/O.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niswitch.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niswitch.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_real64(attribute_id, attribute_value)

        Args:
            attribute_id (int): Pass the ID of an attribute. From the function panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                attributes. Attributes whose value cannot be set are dim. Help text is
                shown for each attribute. Select an attribute by double-clicking on it
                or by selecting it and then pressing . Read-only attributes appear dim
                in the list box. If you select a read-only attribute, an error message
                appears. A ring control at the top of the dialog box allows you to see
                all IVI attributes or only the attributes of the ViInt32 type. If you
                choose to see all IVI attributes, the data types appear to the right of
                the attribute names in the list box. The data types that are not
                consistent with this function are dim. If you select an attribute data
                type that is dim, LabWindows/CVI transfers you to the function panel for
                the corresponding function that is consistent with the data type. - If
                you want to enter a variable name, press to change this ring control to
                a manual input box. - If the attribute in this ring control has
                constants as valid values, you can view the constants by moving to the
                Attribute Value control and pressing .
            attribute_value (float): Pass the value to which you want to set the attribute. From the function
                panel window, you can use this control as follows. - If the attribute
                currently showing in the Attribute ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing . Note: Some of the values might not be valid depending on
                the current settings of the instrument session. Default Value: none
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = visatype.ViReal64(attribute_value)  # case 9
        error_code = self._library.niSwitch_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _set_attribute_vi_string(self, attribute_id, attribute_value):
        '''_set_attribute_vi_string

        This function sets the value of a ViString attribute. This is a
        low-level function that you can use to set the values of
        instrument-specific attributes and inherent IVI attributes. If the
        attribute represents an instrument state, this function performs
        instrument I/O in the following cases: - State caching is disabled for
        the entire session or for the particular attribute. - State caching is
        enabled and the currently cached value is invalid or is different than
        the value you specify. This instrument driver contains high-level
        functions that set most of the instrument attributes. It is best to use
        the high-level driver functions as much as possible. They handle order
        dependencies and multithread locking for you. In addition, they perform
        status checking only after setting all of the attributes. In contrast,
        when you set multiple attributes using the SetAttribute functions, the
        functions check the instrument status after each call. Also, when state
        caching is enabled, the high-level functions that configure multiple
        attributes perform instrument I/O only for the attributes whose value
        you change. Thus, you can safely call the high-level functions without
        the penalty of redundant instrument I/O.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        niswitch.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        niswitch.Session instance, and calling this method on the result.:

            session['0,1']._set_attribute_vi_string(attribute_id, attribute_value)

        Args:
            attribute_id (int): Pass the ID of an attribute. From the function panel window, you can use
                this control as follows. - Click on the control or press , , or , to
                display a dialog box containing a hierarchical list of the available
                attributes. Attributes whose value cannot be set are dim. Help text is
                shown for each attribute. Select an attribute by double-clicking on it
                or by selecting it and then pressing . Read-only attributes appear dim
                in the list box. If you select a read-only attribute, an error message
                appears. A ring control at the top of the dialog box allows you to see
                all IVI attributes or only the attributes of the ViInt32 type. If you
                choose to see all IVI attributes, the data types appear to the right of
                the attribute names in the list box. The data types that are not
                consistent with this function are dim. If you select an attribute data
                type that is dim, LabWindows/CVI transfers you to the function panel for
                the corresponding function that is consistent with the data type. - If
                you want to enter a variable name, press to change this ring control to
                a manual input box. - If the attribute in this ring control has
                constants as valid values, you can view the constants by moving to the
                Attribute Value control and pressing .
            attribute_value (string): Pass the value to which you want to set the attribute. From the function
                panel window, you can use this control as follows. - If the attribute
                currently showing in the Attribute ID ring control has constants as
                valid values, you can view a list of the constants by pressing on this
                control. Select a value by double-clicking on it or by selecting it and
                then pressing . Note: Some of the values might not be valid depending on
                the current settings of the instrument session. Default Value: none
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel_name_ctype = ctypes.create_string_buffer(self._repeated_capability.encode(self._encoding))  # case 2
        attribute_id_ctype = visatype.ViAttr(attribute_id)  # case 9
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case 3
        error_code = self._library.niSwitch_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _error_message(self, error_code):
        '''_error_message

        Converts an error code returned by NI-SWITCH into a user-readable
        string. Generally this information is supplied in error out of any
        NI-SWITCH VI. Use _error_message for a static lookup of an
        error code description.

        Args:
            error_code (int): Status code returned by any NI-SWITCH function. Default Value: 0
                (VI_SUCCESS)

        Returns:
            error_message (string): The error information formatted into a string. You must pass a ViChar
                array with at least 256 bytes.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code_ctype = visatype.ViStatus(error_code)  # case 9
        error_message_ctype = (visatype.ViChar * 256)()  # case 11
        error_code = self._library.niSwitch_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)


class _RepeatedCapability(_SessionBase):
    '''Allows for setting/getting properties and calling methods for specific repeated capabilities (such as channels) on your session.'''

    def __init__(self, vi, repeated_capability):
        super(_RepeatedCapability, self).__init__(repeated_capability)
        self._vi = vi
        self._is_frozen = True


class Session(_SessionBase):
    '''An NI-SWITCH session to a National Instruments Switch Module'''

    def __init__(self, resource_name, topology='Configured Topology', simulate=False, reset_device=False):
        super(Session, self).__init__(repeated_capability='')
        self._vi = 0  # This must be set before calling init_with_topology().
        self._vi = self.init_with_topology(resource_name, topology, simulate, reset_device)
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        return _RepeatedCapability(self._vi, repeated_capability)

    def initiate(self):
        return _Scan(self)

    def close(self):
        try:
            self._close()
        except errors.Error as e:
            self._vi = 0
            raise
        self._vi = 0

    ''' These are code-generated '''

    def _abort_scan(self):
        '''_abort_scan

        Aborts the scan in progress. Initiate a scan with
        _initiate_scan. If the switch module is not scanning,
        NISWITCH_ERROR_NO_SCAN_IN_PROGRESS error is returned.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niSwitch_AbortScan(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def can_connect(self, channel1, channel2):
        '''can_connect

        Verifies that a path between channel 1 and channel 2 can be created. If
        a path is possible in the switch module, the availability of that path
        is returned given the existing connections. If the path is possible but
        in use, a NISWITCH_WARN_IMPLICIT_CONNECTION_EXISTS warning is
        returned.

        Args:
            channel1 (string): Input one of the channel names of the desired path. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""
            channel2 (string): Input one of the channel names of the desired path. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""

        Returns:
            path_capability (enums.PathCapability): Indicates whether a path is valid. Possible values include:
                ------------------------------------ NISWITCH_VAL_PATH_AVAILABLE 1
                NISWITCH_VAL_PATH_EXISTS 2 NISWITCH_VAL_PATH_UNSUPPORTED 3
                NISWITCH_VAL_RSRC_IN_USE 4 NISWITCH_VAL_SOURCE_CONFLICT 5
                NISWITCH_VAL_CHANNEL_NOT_AVAILABLE 6 Notes: (1)
                NISWITCH_VAL_PATH_AVAILABLE indicates that the driver can create the
                path at this time. (2) NISWITCH_VAL_PATH_EXISTS indicates that the
                path already exists. (3) NISWITCH_VAL_PATH_UNSUPPORTED indicates that
                the instrument is not capable of creating a path between the channels
                you specify. (4) NISWITCH_VAL_RSRC_IN_USE indicates that although
                the path is valid, the driver cannot create the path at this moment
                because the switch device is currently using one or more of the required
                channels to create another path. You must destroy the other path before
                creating this one. (5) NISWITCH_VAL_SOURCE_CONFLICT indicates that
                the instrument cannot create a path because both channels are connected
                to a different source channel. (6)
                NISWITCH_VAL_CHANNEL_NOT_AVAILABLE indicates that the driver cannot
                create a path between the two channels because one of the channels is a
                configuration channel and thus unavailable for external connections.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(self._encoding))  # case 3
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(self._encoding))  # case 3
        path_capability_ctype = visatype.ViInt32()  # case 14
        error_code = self._library.niSwitch_CanConnect(vi_ctype, channel1_ctype, channel2_ctype, ctypes.pointer(path_capability_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.PathCapability(path_capability_ctype.value)

    def commit(self):
        '''commit

        Downloads the configured scan list and trigger settings to hardware.
        Calling commit optional as it is implicitly called during
        _initiate_scan. Use commit to arm triggers in a given
        order or to control when expensive hardware operations are performed.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niSwitch_Commit(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_scan_list(self, scanlist, scan_mode=enums.ScanMode.BREAK_BEFORE_MAKE):
        '''configure_scan_list

        Configures the scan list and scan mode used for scanning. Refer to
        Devices Overview to determine if the switch module supports scanning.
        The scan list is comprised of a list of channel connections separated by
        semi-colons. For example, the following scan list will scan the first
        three channels of a multiplexer: com0->ch0; com0->ch1; com0->ch2; Refer
        to Scan Lists for more information on scan list syntax To see the status
        of the scan, call either IsScanning or
        wait_for_scan_complete. Use the configure_scan_trigger
        function to configure the scan trigger. Use the _initiate_scan
        function to start the scan.

        Args:
            scanlist (string): The scan list to use. The driver uses this value to set the Scan List
                attribute. Default value: None
            scan_mode (enums.ScanMode): Specifies how the switch module breaks existing connections when
                scanning. The driver uses this value to set the Scan Mode attribute.
                Refer to scan modes for more information. Default value: Break Before
                Make
        '''
        if type(scan_mode) is not enums.ScanMode:
            raise TypeError('Parameter mode must be of type ' + str(enums.ScanMode))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        scanlist_ctype = ctypes.create_string_buffer(scanlist.encode(self._encoding))  # case 3
        scan_mode_ctype = visatype.ViInt32(scan_mode.value)  # case 10
        error_code = self._library.niSwitch_ConfigureScanList(vi_ctype, scanlist_ctype, scan_mode_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_scan_trigger(self, trigger_input, scan_advanced_output, scan_delay=0.0):
        '''configure_scan_trigger

        Configures the scan triggers for the scan list established with
        configure_scan_list. Refer to Devices Overview to determine if
        the switch module supports scanning. configure_scan_trigger sets
        the location that the switch expects to receive an input trigger to
        advance through the scan list. This function also sets the location
        where it outputs a scan advanced signal after it completes an entry in
        the scan list.

        Args:
            trigger_input (enums.TriggerInput): Trigger source you want the switch module to use during scanning. The
                driver uses this value to set the TRIGGER_INPUT
                attribute. The switch device waits for the trigger you specify when it
                encounters a semicolon in the scanlist. When the trigger occurs, the
                switch device advances to the next entry in the scanlist. Refer to the
                TRIGGER_INPUT topic in the NI Switches Help for a list
                of valid values.
            scan_advanced_output (enums.ScanAdvancedOutput): Output destination of the scan advanced trigger signal. The driver uses
                this value to set the SCAN_ADVANCED_OUTPUT attribute.
                After the switch processes each entry in the scan list, it waits the
                length of time you specify in the Scan Delay parameter and then asserts
                a trigger on the line you specify with this parameter. Refer to the
                SCAN_ADVANCED_OUTPUT topic in the NI Switches Help for
                a list of valid values.
            scan_delay (float): The minimum length of time you want the switch device to wait after it
                creates a path until it asserts a trigger on the scan advanced output
                line. The driver uses this value to set the Scan Delay attribute. The
                scan delay is in addition to the settling time.The driver uses this
                value to set the SCAN_DELAY attribute. Express this
                value in seconds. Default value: 0.0 s
        '''
        if type(trigger_input) is not enums.TriggerInput:
            raise TypeError('Parameter mode must be of type ' + str(enums.TriggerInput))
        if type(scan_advanced_output) is not enums.ScanAdvancedOutput:
            raise TypeError('Parameter mode must be of type ' + str(enums.ScanAdvancedOutput))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        scan_delay_ctype = visatype.ViReal64(scan_delay)  # case 9
        trigger_input_ctype = visatype.ViInt32(trigger_input.value)  # case 10
        scan_advanced_output_ctype = visatype.ViInt32(scan_advanced_output.value)  # case 10
        error_code = self._library.niSwitch_ConfigureScanTrigger(vi_ctype, scan_delay_ctype, trigger_input_ctype, scan_advanced_output_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def connect(self, channel1, channel2):
        '''connect

        Creates a path between channel 1 and channel 2. The driver calculates
        and uses the shortest path between the two channels. Refer to Immediate
        Operations for information about Channel Usage types. If a path is not
        available, the function returns one of the following errors: -
        NISWITCH_ERROR_EXPLICIT_CONNECTION_EXISTS, if the two channels are
        already explicitly connected by calling either the connect or
        set_path function. -
        NISWITCH_ERROR_IS_CONFIGURATION_CHANNEL, if a channel is a
        configuration channel. Error elaboration contains information about
        which of the two channels is a configuration channel. -
        NISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES, if both channels are
        connected to a different source. Error elaboration contains information
        about sources channel 1 and 2 connect to. -
        NISWITCH_ERROR_CANNOT_CONNECT_TO_ITSELF, if channels 1 and 2 are
        one and the same channel. - NISWITCH_ERROR_PATH_NOT_FOUND, if the
        driver cannot find a path between the two channels. Note: Paths are
        bidirectional. For example, if a path exists between channels CH1 and
        CH2, then the path also exists between channels CH2 and CH1.

        Args:
            channel1 (string): Input one of the channel names of the desired path. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None
            channel2 (string): Input one of the channel names of the desired path. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(self._encoding))  # case 3
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(self._encoding))  # case 3
        error_code = self._library.niSwitch_Connect(vi_ctype, channel1_ctype, channel2_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def connect_multiple(self, connection_list):
        '''connect_multiple

        Creates the connections between channels specified in Connection List.
        Specify connections with two endpoints only or the explicit path between
        two endpoints. NI-SWITCH calculates and uses the shortest path between
        the channels. Refer to Setting Source and Configuration Channels for
        information about channel usage types. In the event of an error,
        connecting stops at the point in the list where the error occurred. If a
        path is not available, the function returns one of the following errors:
        - NISWITCH_ERROR_EXPLICIT_CONNECTION_EXISTS, if the two channels are
        already explicitly connected. -
        NISWITCH_ERROR_IS_CONFIGURATION_CHANNEL, if a channel is a
        configuration channel. Error elaboration contains information about
        which of the two channels is a configuration channel. -
        NISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES, if both channels are
        connected to a different source. Error elaboration contains information
        about sources channel 1 and 2 to connect. -
        NISWITCH_ERROR_CANNOT_CONNECT_TO_ITSELF, if channels 1 and 2 are
        one and the same channel. - NISWITCH_ERROR_PATH_NOT_FOUND, if the
        driver cannot find a path between the two channels. Note: Paths are
        bidirectional. For example, if a path exists between channels ch1 and
        ch2, then the path also exists between channels ch1 and ch2.

        Args:
            connection_list (string): Connection List specifies a list of connections between channels to
                make. NI-SWITCH validates the connection list, and aborts execution of
                the list if errors are returned. Refer to Connection and Disconnection
                List Syntax for valid connection list syntax and examples. Refer to
                Devices Overview for valid channel names for the switch module. Example
                of a valid connection list: c0 -> r1, [c2 -> r2 -> c3] In this example,
                r2 is a configuration channel. Default value: None
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        connection_list_ctype = ctypes.create_string_buffer(connection_list.encode(self._encoding))  # case 3
        error_code = self._library.niSwitch_ConnectMultiple(vi_ctype, connection_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self):
        '''disable

        Places the switch module in a quiescent state where it has minimal or no
        impact on the system to which it is connected. All channels are
        disconnected and any scan in progress is aborted.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niSwitch_Disable(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect(self, channel1, channel2):
        '''disconnect

        This function destroys the path between two channels that you create
        with the connect or set_path function. If a path is
        not connected or not available, the function returns the
        IVISWTCH_ERROR_NO_SUCH_PATH error.

        Args:
            channel1 (string): Input one of the channel names of the path to break. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None
            channel2 (string): Input one of the channel names of the path to break. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: None
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(self._encoding))  # case 3
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(self._encoding))  # case 3
        error_code = self._library.niSwitch_Disconnect(vi_ctype, channel1_ctype, channel2_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect_all(self):
        '''disconnect_all

        Breaks all existing paths. If the switch module cannot break all paths,
        NISWITCH_WARN_PATH_REMAINS warning is returned.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niSwitch_DisconnectAll(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disconnect_multiple(self, disconnection_list):
        '''disconnect_multiple

        Breaks the connections between channels specified in Disconnection List.
        If no connections exist between channels, NI-SWITCH returns an error. In
        the event of an error, the VI stops at the point in the list where the
        error occurred.

        Args:
            disconnection_list (string): Disconnection List specifies a list of connections between channels to
                break. NI-SWITCH validates the disconnection list, and aborts execution
                of the list if errors are returned. Refer to Connection and
                Disconnection List Syntax for valid disconnection list syntax and
                examples. Refer to Devices Overview for valid channel names for the
                switch module. Example of a valid disconnection list: c0 -> r1, [c2 ->
                r2 -> c3] In this example, r2 is a configuration channel. Default value:
                None
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        disconnection_list_ctype = ctypes.create_string_buffer(disconnection_list.encode(self._encoding))  # case 3
        error_code = self._library.niSwitch_DisconnectMultiple(vi_ctype, disconnection_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def get_channel_name(self, index):
        '''get_channel_name

        Returns the channel string that is in the channel table at the specified
        index. Use get_channel_name in a For Loop to get a complete list
        of valid channel names for the switch module. Use the Channel Count
        attribute to determine the number of channels.

        Args:
            index (int): A 1-based index into the channel table. Default value: 1 Maximum value:
                Value of Channel Count attribute.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        index_ctype = visatype.ViInt32(index)  # case 9
        buffer_size_ctype = visatype.ViInt32()  # case 7
        channel_name_buffer_ctype = None  # case 12
        error_code = self._library.niSwitch_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, channel_name_buffer_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = visatype.ViInt32(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        channel_name_buffer_ctype = (visatype.ViChar * buffer_size_ctype.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_code = self._library.niSwitch_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, channel_name_buffer_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return channel_name_buffer_ctype.value.decode(self._encoding)

    def get_path(self, channel1, channel2):
        '''get_path

        Returns a string that identifies the explicit path created with
        connect. Pass this string to set_path to establish
        the exact same path in future connections. In some cases, multiple paths
        are available between two channels. When you call connect, the
        driver selects an available path. With connect, there is no
        guarantee that the driver selected path will always be the same path
        through the switch module. get_path only returns those paths
        explicitly created by niSwitch Connect Channels or set_path.
        For example, if you connect channels CH1 and CH3,and then channels CH2
        and CH3, an explicit path between channels CH1 and CH2 does not exist an
        error is returned

        Args:
            channel1 (string): Input one of the channel names of the desired path. Pass the other
                channel name as the channel 2 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""
            channel2 (string): Input one of the channel names of the desired path. Pass the other
                channel name as the channel 1 parameter. Refer to Devices Overview for
                valid channel names for the switch module. Examples of valid channel
                names: ch0, com0, ab0, r1, c2, cjtemp Default value: ""
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        channel1_ctype = ctypes.create_string_buffer(channel1.encode(self._encoding))  # case 3
        channel2_ctype = ctypes.create_string_buffer(channel2.encode(self._encoding))  # case 3
        buffer_size_ctype = visatype.ViInt32()  # case 7
        path_ctype = None  # case 12
        error_code = self._library.niSwitch_GetPath(vi_ctype, channel1_ctype, channel2_ctype, buffer_size_ctype, path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = visatype.ViInt32(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        path_ctype = (visatype.ViChar * buffer_size_ctype.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_code = self._library.niSwitch_GetPath(vi_ctype, channel1_ctype, channel2_ctype, buffer_size_ctype, path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return path_ctype.value.decode(self._encoding)

    def get_relay_count(self, relay_name):
        '''get_relay_count

        Returns the number of times the relay has changed from Closed to Open.
        Relay count is useful for tracking relay lifetime and usage. Call
        wait_for_debounce before get_relay_count to ensure an
        accurate count. Refer to the Relay Count topic in the NI Switches Help
        to determine if the switch module supports relay counting.

        Args:
            relay_name (string): Name of the relay. Default value: None Examples of valid relay names:
                ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
                relay names for the switch module.

        Returns:
            relay_count (int): The number of relay cycles.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        relay_name_ctype = ctypes.create_string_buffer(relay_name.encode(self._encoding))  # case 3
        relay_count_ctype = visatype.ViInt32()  # case 14
        error_code = self._library.niSwitch_GetRelayCount(vi_ctype, relay_name_ctype, ctypes.pointer(relay_count_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(relay_count_ctype.value)

    def get_relay_name(self, index):
        '''get_relay_name

        Returns the relay name string that is in the relay list at the specified
        index. Use get_relay_name in a For Loop to get a complete list
        of valid relay names for the switch module. Use the Number of Relays
        attribute to determine the number of relays.

        Args:
            index (int): A 1-based index into the channel table. Default value: 1 Maximum value:
                Value of Channel Count attribute.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        index_ctype = visatype.ViInt32(index)  # case 9
        relay_name_buffer_size_ctype = visatype.ViInt32()  # case 7
        relay_name_buffer_ctype = None  # case 12
        error_code = self._library.niSwitch_GetRelayName(vi_ctype, index_ctype, relay_name_buffer_size_ctype, relay_name_buffer_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        relay_name_buffer_size_ctype = visatype.ViInt32(error_code)  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        relay_name_buffer_ctype = (visatype.ViChar * relay_name_buffer_size_ctype.value)()  # TODO(marcoskirsch): use get_ctype_variable_declaration_snippet()
        error_code = self._library.niSwitch_GetRelayName(vi_ctype, index_ctype, relay_name_buffer_size_ctype, relay_name_buffer_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return relay_name_buffer_ctype.value.decode(self._encoding)

    def get_relay_position(self, relay_name):
        '''get_relay_position

        Returns the relay position for the relay specified in the Relay Name
        parameter.

        Args:
            relay_name (string): Name of the relay. Default value: None Examples of valid relay names:
                ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
                relay names for the switch module.

        Returns:
            relay_position (enums.RelayPosition): Indicates whether the relay is open or closed. NISWITCH_VAL_OPEN 10
                NIWITCH_VAL_CLOSED 11
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        relay_name_ctype = ctypes.create_string_buffer(relay_name.encode(self._encoding))  # case 3
        relay_position_ctype = visatype.ViInt32()  # case 14
        error_code = self._library.niSwitch_GetRelayPosition(vi_ctype, relay_name_ctype, ctypes.pointer(relay_position_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.RelayPosition(relay_position_ctype.value)

    def init_with_topology(self, resource_name, topology='Configured Topology', simulate=False, reset_device=False):
        '''init_with_topology

        Returns a session handle used to identify the switch in all subsequent
        instrument driver calls and sets the topology of the switch.
        init_with_topology creates a new IVI instrument driver session
        for the switch specified in the resourceName parameter. The driver uses
        the topology specified in the topology parameter and overrides the
        topology specified in MAX. Note: When initializing an NI SwitchBlock
        device with topology, you must specify the toplogy created when you
        configured the device in MAX, using either
        NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY or the toplogy string of the
        device. Refer to the Initializing with Toplogy for NI SwitchBlock
        Devices topic in the NI Switches Help for information about determining
        the topology string of an NI SwitchBlock device. By default, the switch
        is reset to a known state. Enable simulation by specifying the topology
        and setting the simulate parameter to VI_TRUE.

        Args:
            resource_name (string): Resource name of the switch module to initialize. Default value: None
                Syntax: Optional fields are shown in square brackets ([]). Configured in
                MAX Under Valid Syntax Devices and Interfaces DeviceName Traditional
                NI-DAQ Devices SCXI[chassis ID]::slot number PXI System PXI[bus
                number]::device number TIP: IVI logical names are also valid for the
                resource name. Default values for optional fields: chassis ID = 1 bus
                number = 0 Example resource names: Resource Name Description SC1Mod3
                NI-DAQmx module in chassis "SC1" slot 3 MySwitch NI-DAQmx module renamed
                to "MySwitch" SCXI1::3 Traditional NI-DAQ module in chassis 1, slot 3
                SCXI::3 Traditional NI-DAQ module in chassis 1, slot 3 PXI0::16 PXI bus
                0, device number 16 PXI::16 PXI bus 0, device number 16
            topology (string): Pass the topology name you want to use for the switch you specify with
                Resource Name parameter. You can also pass
                NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY to use the last topology that
                was configured for the device in MAX. Default Value:
                NISWITCH_TOPOLOGY_CONFIGURED_TOPOLOGY Valid Values:
                NISWITCH_TOPOLOGY_1127_1_WIRE_64X1_MUX
                NISWITCH_TOPOLOGY_1127_2_WIRE_32X1_MUX
                NISWITCH_TOPOLOGY_1127_2_WIRE_4X8_MATRIX
                NISWITCH_TOPOLOGY_1127_4_WIRE_16X1_MUX
                NISWITCH_TOPOLOGY_1127_INDEPENDENT
                NISWITCH_TOPOLOGY_1128_1_WIRE_64X1_MUX
                NISWITCH_TOPOLOGY_1128_2_WIRE_32X1_MUX
                NISWITCH_TOPOLOGY_1128_2_WIRE_4X8_MATRIX
                NISWITCH_TOPOLOGY_1128_4_WIRE_16X1_MUX
                NISWITCH_TOPOLOGY_1128_INDEPENDENT
                NISWITCH_TOPOLOGY_1129_2_WIRE_16X16_MATRIX
                NISWITCH_TOPOLOGY_1129_2_WIRE_8X32_MATRIX
                NISWITCH_TOPOLOGY_1129_2_WIRE_4X64_MATRIX
                NISWITCH_TOPOLOGY_1129_2_WIRE_DUAL_8X16_MATRIX
                NISWITCH_TOPOLOGY_1129_2_WIRE_DUAL_4X32_MATRIX
                NISWITCH_TOPOLOGY_1129_2_WIRE_QUAD_4X16_MATRIX
                NISWITCH_TOPOLOGY_1130_1_WIRE_256X1_MUX
                NISWITCH_TOPOLOGY_1130_1_WIRE_DUAL_128X1_MUX
                NISWITCH_TOPOLOGY_1130_1_WIRE_4X64_MATRIX
                NISWITCH_TOPOLOGY_1130_1_WIRE_8x32_MATRIX
                NISWITCH_TOPOLOGY_1130_1_WIRE_OCTAL_32X1_MUX
                NISWITCH_TOPOLOGY_1130_1_WIRE_QUAD_64X1_MUX
                NISWITCH_TOPOLOGY_1130_1_WIRE_SIXTEEN_16X1_MUX
                NISWITCH_TOPOLOGY_1130_2_WIRE_4X32_MATRIX
                NISWITCH_TOPOLOGY_1130_2_WIRE_128X1_MUX
                NISWITCH_TOPOLOGY_1130_2_WIRE_OCTAL_16X1_MUX
                NISWITCH_TOPOLOGY_1130_2_WIRE_QUAD_32X1_MUX
                NISWITCH_TOPOLOGY_1130_4_WIRE_64X1_MUX
                NISWITCH_TOPOLOGY_1130_4_WIRE_QUAD_16X1_MUX
                NISWITCH_TOPOLOGY_1130_INDEPENDENT NISWITCH_TOPOLOGY_1160_16_SPDT
                NISWITCH_TOPOLOGY_1161_8_SPDT
                NISWITCH_TOPOLOGY_1163R_OCTAL_4X1_MUX
                NISWITCH_TOPOLOGY_1166_16_DPDT NISWITCH_TOPOLOGY_1166_32_SPDT
                NISWITCH_TOPOLOGY_1167_INDEPENDENT
                NISWITCH_TOPOLOGY_1169_100_SPST NISWITCH_TOPOLOGY_1169_50_DPST
                NISWITCH_TOPOLOGY_1175_1_WIRE_196X1_MUX
                NISWITCH_TOPOLOGY_1175_2_WIRE_98X1_MUX
                NISWITCH_TOPOLOGY_1175_2_WIRE_95X1_MUX
                NISWITCH_TOPOLOGY_1190_QUAD_4X1_MUX
                NISWITCH_TOPOLOGY_1191_QUAD_4X1_MUX
                NISWITCH_TOPOLOGY_1192_8_SPDT NISWITCH_TOPOLOGY_1193_32X1_MUX
                NISWITCH_TOPOLOGY_1193_16X1_TERMINATED_MUX
                NISWITCH_TOPOLOGY_1193_DUAL_16X1_MUX
                NISWITCH_TOPOLOGY_1193_DUAL_8X1_TERMINATED_MUX
                NISWITCH_TOPOLOGY_1193_QUAD_8X1_MUX
                NISWITCH_TOPOLOGY_1193_QUAD_4X1_TERMINATED_MUX
                NISWITCH_TOPOLOGY_1193_INDEPENDENT
                NISWITCH_TOPOLOGY_1194_QUAD_4X1_MUX
                NISWITCH_TOPOLOGY_1195_QUAD_4X1_MUX
                NISWITCH_TOPOLOGY_2501_1_WIRE_48X1_MUX
                NISWITCH_TOPOLOGY_2501_1_WIRE_48X1_AMPLIFIED_MUX
                NISWITCH_TOPOLOGY_2501_2_WIRE_24X1_MUX
                NISWITCH_TOPOLOGY_2501_2_WIRE_24X1_AMPLIFIED_MUX
                NISWITCH_TOPOLOGY_2501_2_WIRE_DUAL_12X1_MUX
                NISWITCH_TOPOLOGY_2501_2_WIRE_QUAD_6X1_MUX
                NISWITCH_TOPOLOGY_2501_2_WIRE_4X6_MATRIX
                NISWITCH_TOPOLOGY_2501_4_WIRE_12X1_MUX
                NISWITCH_TOPOLOGY_2503_1_WIRE_48X1_MUX
                NISWITCH_TOPOLOGY_2503_2_WIRE_24X1_MUX
                NISWITCH_TOPOLOGY_2503_2_WIRE_DUAL_12X1_MUX
                NISWITCH_TOPOLOGY_2503_2_WIRE_QUAD_6X1_MUX
                NISWITCH_TOPOLOGY_2503_2_WIRE_4X6_MATRIX
                NISWITCH_TOPOLOGY_2503_4_WIRE_12X1_MUX
                NISWITCH_TOPOLOGY_2510_INDEPENDENT
                NISWITCH_TOPOLOGY_2512_INDEPENDENT
                NISWITCH_TOPOLOGY_2514_INDEPENDENT
                NISWITCH_TOPOLOGY_2515_INDEPENDENT NISWITCH_TOPOLOGY_2520_80_SPST
                NISWITCH_TOPOLOGY_2521_40_DPST NISWITCH_TOPOLOGY_2522_53_SPDT
                NISWITCH_TOPOLOGY_2523_26_DPDT
                NISWITCH_TOPOLOGY_2524_1_WIRE_128X1_MUX
                NISWITCH_TOPOLOGY_2524_1_WIRE_DUAL_64X1_MUX
                NISWITCH_TOPOLOGY_2524_1_WIRE_QUAD_32X1_MUX
                NISWITCH_TOPOLOGY_2524_1_WIRE_OCTAL_16X1_MUX
                NISWITCH_TOPOLOGY_2524_1_WIRE_SIXTEEN_8X1_MUX
                NISWITCH_TOPOLOGY_2525_2_WIRE_64X1_MUX
                NISWITCH_TOPOLOGY_2525_2_WIRE_DUAL_32X1_MUX
                NISWITCH_TOPOLOGY_2525_2_WIRE_QUAD_16X1_MUX
                NISWITCH_TOPOLOGY_2525_2_WIRE_OCTAL_8X1_MUX
                NISWITCH_TOPOLOGY_2525_2_WIRE_SIXTEEN_4X1_MUX
                NISWITCH_TOPOLOGY_2526_1_WIRE_158X1_MUX
                NISWITCH_TOPOLOGY_2526_2_WIRE_79X1_MUX
                NISWITCH_TOPOLOGY_2527_1_WIRE_64X1_MUX
                NISWITCH_TOPOLOGY_2527_1_WIRE_DUAL_32X1_MUX
                NISWITCH_TOPOLOGY_2527_2_WIRE_32X1_MUX
                NISWITCH_TOPOLOGY_2527_2_WIRE_DUAL_16X1_MUX
                NISWITCH_TOPOLOGY_2527_4_WIRE_16X1_MUX
                NISWITCH_TOPOLOGY_2527_INDEPENDENT
                NISWITCH_TOPOLOGY_2529_2_WIRE_DUAL_4X16_MATRIX
                NISWITCH_TOPOLOGY_2529_2_WIRE_8X16_MATRIX
                NISWITCH_TOPOLOGY_2529_2_WIRE_4X32_MATRIX
                NISWITCH_TOPOLOGY_2530_1_WIRE_128X1_MUX
                NISWITCH_TOPOLOGY_2530_1_WIRE_DUAL_64X1_MUX
                NISWITCH_TOPOLOGY_2530_1_WIRE_4x32_MATRIX
                NISWITCH_TOPOLOGY_2530_1_WIRE_8x16_MATRIX
                NISWITCH_TOPOLOGY_2530_1_WIRE_OCTAL_16X1_MUX
                NISWITCH_TOPOLOGY_2530_1_WIRE_QUAD_32X1_MUX
                NISWITCH_TOPOLOGY_2530_2_WIRE_4x16_MATRIX
                NISWITCH_TOPOLOGY_2530_2_WIRE_64X1_MUX
                NISWITCH_TOPOLOGY_2530_2_WIRE_DUAL_32X1_MUX
                NISWITCH_TOPOLOGY_2530_2_WIRE_QUAD_16X1_MUX
                NISWITCH_TOPOLOGY_2530_4_WIRE_32X1_MUX
                NISWITCH_TOPOLOGY_2530_4_WIRE_DUAL_16X1_MUX
                NISWITCH_TOPOLOGY_2530_INDEPENDENT
                NISWITCH_TOPOLOGY_2531_1_WIRE_4X128_MATRIX
                NISWITCH_TOPOLOGY_2531_1_WIRE_8X64_MATRIX
                NISWITCH_TOPOLOGY_2531_1_WIRE_DUAL_4X64_MATRIX
                NISWITCH_TOPOLOGY_2531_1_WIRE_DUAL_8X32_MATRIX
                NISWITCH_TOPOLOGY_2531_2_WIRE_4X64_MATRIX
                NISWITCH_TOPOLOGY_2531_2_WIRE_8X32_MATRIX
                NISWITCH_TOPOLOGY_2532_1_WIRE_16X32_MATRIX
                NISWITCH_TOPOLOGY_2532_1_WIRE_4X128_MATRIX
                NISWITCH_TOPOLOGY_2532_1_WIRE_8X64_MATRIX
                NISWITCH_TOPOLOGY_2532_1_WIRE_DUAL_16X16_MATRIX
                NISWITCH_TOPOLOGY_2532_1_WIRE_DUAL_4X64_MATRIX
                NISWITCH_TOPOLOGY_2532_1_WIRE_DUAL_8X32_MATRIX
                NISWITCH_TOPOLOGY_2532_1_WIRE_SIXTEEN_2X16_MATRIX
                NISWITCH_TOPOLOGY_2532_2_WIRE_16X16_MATRIX
                NISWITCH_TOPOLOGY_2532_2_WIRE_4X64_MATRIX
                NISWITCH_TOPOLOGY_2532_2_WIRE_8X32_MATRIX
                NISWITCH_TOPOLOGY_2532_2_WIRE_DUAL_4X32_MATRIX
                NISWITCH_TOPOLOGY_2533_1_WIRE_4X64_MATRIX
                NISWITCH_TOPOLOGY_2534_1_WIRE_8X32_MATRIX
                NISWITCH_TOPOLOGY_2535_1_WIRE_4X136_MATRIX
                NISWITCH_TOPOLOGY_2536_1_WIRE_8X68_MATRIX
                NISWITCH_TOPOLOGY_2540_1_WIRE_8X9_MATRIX
                NISWITCH_TOPOLOGY_2541_1_WIRE_8X12_MATRIX
                NISWITCH_TOPOLOGY_2542_QUAD_2X1_TERMINATED_MUX
                NISWITCH_TOPOLOGY_2543_DUAL_4X1_TERMINATED_MUX
                NISWITCH_TOPOLOGY_2544_8X1_TERMINATED_MUX
                NISWITCH_TOPOLOGY_2545_4X1_TERMINATED_MUX
                NISWITCH_TOPOLOGY_2546_DUAL_4X1_MUX
                NISWITCH_TOPOLOGY_2547_8X1_MUX NISWITCH_TOPOLOGY_2548_4_SPDT
                NISWITCH_TOPOLOGY_2549_TERMINATED_2_SPDT
                NISWITCH_TOPOLOGY_2554_4X1_MUX
                NISWITCH_TOPOLOGY_2555_4X1_TERMINATED_MUX
                NISWITCH_TOPOLOGY_2556_DUAL_4X1_MUX
                NISWITCH_TOPOLOGY_2557_8X1_MUX NISWITCH_TOPOLOGY_2558_4_SPDT
                NISWITCH_TOPOLOGY_2559_TERMINATED_2_SPDT
                NISWITCH_TOPOLOGY_2564_16_SPST NISWITCH_TOPOLOGY_2564_8_DPST
                NISWITCH_TOPOLOGY_2565_16_SPST NISWITCH_TOPOLOGY_2566_16_SPDT
                NISWITCH_TOPOLOGY_2566_8_DPDT NISWITCH_TOPOLOGY_2567_INDEPENDENT
                NISWITCH_TOPOLOGY_2568_15_DPST NISWITCH_TOPOLOGY_2568_31_SPST
                NISWITCH_TOPOLOGY_2569_100_SPST NISWITCH_TOPOLOGY_2569_50_DPST
                NISWITCH_TOPOLOGY_2570_20_DPDT NISWITCH_TOPOLOGY_2570_40_SPDT
                NISWITCH_TOPOLOGY_2571_66_SPDT
                NISWITCH_TOPOLOGY_2575_1_WIRE_196X1_MUX
                NISWITCH_TOPOLOGY_2575_2_WIRE_98X1_MUX
                NISWITCH_TOPOLOGY_2575_2_WIRE_95X1_MUX
                NISWITCH_TOPOLOGY_2576_2_WIRE_64X1_MUX
                NISWITCH_TOPOLOGY_2576_2_WIRE_DUAL_32X1_MUX
                NISWITCH_TOPOLOGY_2576_2_WIRE_OCTAL_8X1_MUX
                NISWITCH_TOPOLOGY_2576_2_WIRE_QUAD_16X1_MUX
                NISWITCH_TOPOLOGY_2576_2_WIRE_SIXTEEN_4X1_MUX
                NISWITCH_TOPOLOGY_2576_INDEPENDENT
                NISWITCH_TOPOLOGY_2584_1_WIRE_12X1_MUX
                NISWITCH_TOPOLOGY_2584_1_WIRE_DUAL_6X1_MUX
                NISWITCH_TOPOLOGY_2584_2_WIRE_6X1_MUX
                NISWITCH_TOPOLOGY_2584_INDEPENDENT
                NISWITCH_TOPOLOGY_2585_1_WIRE_10X1_MUX
                NISWITCH_TOPOLOGY_2586_10_SPST NISWITCH_TOPOLOGY_2586_5_DPST
                NISWITCH_TOPOLOGY_2590_4X1_MUX NISWITCH_TOPOLOGY_2591_4X1_MUX
                NISWITCH_TOPOLOGY_2593_16X1_MUX
                NISWITCH_TOPOLOGY_2593_8X1_TERMINATED_MUX
                NISWITCH_TOPOLOGY_2593_DUAL_8X1_MUX
                NISWITCH_TOPOLOGY_2593_DUAL_4X1_TERMINATED_MUX
                NISWITCH_TOPOLOGY_2593_INDEPENDENT NISWITCH_TOPOLOGY_2594_4X1_MUX
                NISWITCH_TOPOLOGY_2595_4X1_MUX
                NISWITCH_TOPOLOGY_2596_DUAL_6X1_MUX
                NISWITCH_TOPOLOGY_2597_6X1_TERMINATED_MUX
                NISWITCH_TOPOLOGY_2598_DUAL_TRANSFER
                NISWITCH_TOPOLOGY_2599_2_SPDT NISWITCH_TOPOLOGY_2720_INDEPENDENT
                NISWITCH_TOPOLOGY_2722_INDEPENDENT
                NISWITCH_TOPOLOGY_2725_INDEPENDENT
                NISWITCH_TOPOLOGY_2727_INDEPENDENT
                NISWITCH_TOPOLOGY_2737_2_WIRE_4X64_MATRIX
                NISWITCH_TOPOLOGY_2738_2_WIRE_8X32_MATRIX
                NISWITCH_TOPOLOGY_2739_2_WIRE_16X16_MATRIX
                NISWITCH_TOPOLOGY_2746_QUAD_4X1_MUX
                NISWITCH_TOPOLOGY_2747_DUAL_8X1_MUX
                NISWITCH_TOPOLOGY_2748_16X1_MUX
                NISWITCH_TOPOLOGY_2790_INDEPENDENT
                NISWITCH_TOPOLOGY_2796_DUAL_6X1_MUX
                NISWITCH_TOPOLOGY_2797_6X1_TERMINATED_MUX
                NISWITCH_TOPOLOGY_2798_DUAL_TRANSFER
                NISWITCH_TOPOLOGY_2799_2_SPDT
            simulate (bool): Enables simulation of the switch module specified in the resource name
                parameter. Valid Values: VI_TRUE - simulate VI_FALSE - Don't simulate
                (Default Value)
            reset_device (bool): Specifies whether to reset the switch module during the initialization
                process. Valid Values: VI_TRUE - Reset Device (Default Value) VI_FALSE
                - Currently unsupported. The device will not reset.

        Returns:
            vi (int): A particular NI-SWITCH session established with
                init_with_topology, InitWithOptions, or init
                and used for all subsequent NI-SWITCH calls.
        '''
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case 3
        topology_ctype = ctypes.create_string_buffer(topology.encode(self._encoding))  # case 3
        simulate_ctype = visatype.ViBoolean(simulate)  # case 9
        reset_device_ctype = visatype.ViBoolean(reset_device)  # case 9
        vi_ctype = visatype.ViSession()  # case 14
        error_code = self._library.niSwitch_InitWithTopology(resource_name_ctype, topology_ctype, simulate_ctype, reset_device_ctype, ctypes.pointer(vi_ctype))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(vi_ctype.value)

    def _initiate_scan(self):
        '''_initiate_scan

        Commits the configured scan list and trigger settings to hardware and
        initiates the scan. If niSwitch Commit was called earlier, niSwitch
        Initiate Scan only initiates the scan and returns immediately. Once the
        scanning operation begins, you cannot perform any other operation other
        than GetAttribute, AbortScan, or SendSoftwareTrigger. All other
        functions return NISWITCH_ERROR_SCAN_IN_PROGRESS. To stop the
        scanning operation, To stop the scanning operation, call
        _abort_scan.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niSwitch_InitiateScan(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def relay_control(self, relay_name, relay_action):
        '''relay_control

        Controls individual relays of the switch. When controlling individual
        relays, the protection offered by setting the usage of source channels
        and configuration channels, and by enabling or disabling analog bus
        sharing on the NI SwitchBlock, does not apply. Refer to the device book
        for your switch in the NI Switches Help to determine if the switch
        supports individual relay control.

        Args:
            relay_name (string): Name of the relay. Default value: None Examples of valid relay names:
                ch0, ab0, 1wire, hlselect Refer to Devices Overview for a list of valid
                relay names for the switch module.
            relay_action (enums.RelayAction): Specifies whether to open or close a given relay. Default value: Relay
                Close Defined values: NISWITCH_VAL_OPEN_RELAY
                NISWITCH_VAL_CLOSE_RELAY (Default Value)
        '''
        if type(relay_action) is not enums.RelayAction:
            raise TypeError('Parameter mode must be of type ' + str(enums.RelayAction))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        relay_name_ctype = ctypes.create_string_buffer(relay_name.encode(self._encoding))  # case 3
        relay_action_ctype = visatype.ViInt32(relay_action.value)  # case 10
        error_code = self._library.niSwitch_RelayControl(vi_ctype, relay_name_ctype, relay_action_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_defaults(self):
        '''reset_with_defaults

        Resets the switch module and applies initial user specified settings
        from the logical name used to initialize the session. If the session was
        created without a logical name, this function is equivalent to
        reset.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niSwitch_ResetWithDefaults(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def route_scan_advanced_output(self, scan_advanced_output_connector, scan_advanced_output_bus_line, invert=False):
        '''route_scan_advanced_output

        Routes the scan advanced output trigger from a trigger bus line (TTLx)
        to the front or rear connector.

        Args:
            scan_advanced_output_connector (enums.ScanAdvancedOutput): The scan advanced trigger destination. Valid locations are the
                NISWITCH_VAL_FRONTCONNECTOR and NISWITCH_VAL_REARCONNECTOR. Default
                value: NISWITCH_VAL_FRONTCONNECTOR
            scan_advanced_output_bus_line (enums.ScanAdvancedOutput): The trigger line to route the scan advanced output trigger from the
                front or rear connector. Select NISWITCH_VAL_NONE to break an existing
                route. Default value: None Valid Values: NISWITCH_VAL_NONE
                NISWITCH_VAL_TTL0 NISWITCH_VAL_TTL1 NISWITCH_VAL_TTL2
                NISWITCH_VAL_TTL3 NISWITCH_VAL_TTL4 NISWITCH_VAL_TTL5
                NISWITCH_VAL_TTL6 NISWITCH_VAL_TTL7
            invert (bool): If VI_TRUE, inverts the input trigger signal from falling to rising or
                vice versa. Default value: VI_FALSE
        '''
        if type(scan_advanced_output_connector) is not enums.ScanAdvancedOutput:
            raise TypeError('Parameter mode must be of type ' + str(enums.ScanAdvancedOutput))
        if type(scan_advanced_output_bus_line) is not enums.ScanAdvancedOutput:
            raise TypeError('Parameter mode must be of type ' + str(enums.ScanAdvancedOutput))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        scan_advanced_output_connector_ctype = visatype.ViInt32(scan_advanced_output_connector.value)  # case 10
        scan_advanced_output_bus_line_ctype = visatype.ViInt32(scan_advanced_output_bus_line.value)  # case 10
        invert_ctype = visatype.ViBoolean(invert)  # case 9
        error_code = self._library.niSwitch_RouteScanAdvancedOutput(vi_ctype, scan_advanced_output_connector_ctype, scan_advanced_output_bus_line_ctype, invert_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def route_trigger_input(self, trigger_input_connector, trigger_input_bus_line, invert=False):
        '''route_trigger_input

        Routes the input trigger from the front or rear connector to a trigger
        bus line (TTLx). To disconnect the route, call this function again and
        specify None for trigger bus line parameter.

        Args:
            trigger_input_connector (enums.TriggerInput): The location of the input trigger source on the switch module. Valid
                locations are the NISWITCH_VAL_FRONTCONNECTOR and
                NISWITCH_VAL_REARCONNECTOR. Default value:
                NISWITCH_VAL_FRONTCONNECTOR
            trigger_input_bus_line (enums.TriggerInput): The trigger line to route the input trigger. Select NISWITCH_VAL_NONE
                to break an existing route. Default value: None Valid Values:
                NISWITCH_VAL_NONE NISWITCH_VAL_TTL0 NISWITCH_VAL_TTL1
                NISWITCH_VAL_TTL2 NISWITCH_VAL_TTL3 NISWITCH_VAL_TTL4
                NISWITCH_VAL_TTL5 NISWITCH_VAL_TTL6 NISWITCH_VAL_TTL7
            invert (bool): If VI_TRUE, inverts the input trigger signal from falling to rising or
                vice versa. Default value: VI_FALSE
        '''
        if type(trigger_input_connector) is not enums.TriggerInput:
            raise TypeError('Parameter mode must be of type ' + str(enums.TriggerInput))
        if type(trigger_input_bus_line) is not enums.TriggerInput:
            raise TypeError('Parameter mode must be of type ' + str(enums.TriggerInput))
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        trigger_input_connector_ctype = visatype.ViInt32(trigger_input_connector.value)  # case 10
        trigger_input_bus_line_ctype = visatype.ViInt32(trigger_input_bus_line.value)  # case 10
        invert_ctype = visatype.ViBoolean(invert)  # case 9
        error_code = self._library.niSwitch_RouteTriggerInput(vi_ctype, trigger_input_connector_ctype, trigger_input_bus_line_ctype, invert_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_trigger(self):
        '''send_software_trigger

        Sends a software trigger to the switch module specified in the NI-SWITCH
        session. When the trigger input is set to NISWITCH_VAL_SOFTWARE_TRIG
        through either the configure_scan_trigger or the
        TRIGGER_INPUT attribute, the scan does not proceed from
        a semi-colon (wait for trigger) until send_software_trigger is
        called.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niSwitch_SendSoftwareTrigger(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_continuous_scan(self, continuous_scan):
        '''set_continuous_scan

        Sets the to loop continuously through the scan list or to stop scanning
        after one pass through the scan list.

        Args:
            continuous_scan (bool): If VI_TRUE, loops continuously through the scan list during scanning.
                If VI_FALSE, the scan stops after one pass through the scan list.
                Default value: VI_FALSE
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        continuous_scan_ctype = visatype.ViBoolean(continuous_scan)  # case 9
        error_code = self._library.niSwitch_SetContinuousScan(vi_ctype, continuous_scan_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_path(self, path_list):
        '''set_path

        Connects two channels by specifying an explicit path in the path list
        parameter. set_path is particularly useful where path
        repeatability is important, such as in calibrated signal paths. If this
        is not necessary, use connect.

        Args:
            path_list (string): A string composed of comma-separated paths between channel 1 and channel
                2. The first and last names in the path are the endpoints of the path.
                Every other channel in the path are configuration channels. Example of a
                valid path list string: ch0->com0, com0->ab0. In this example, com0 is a
                configuration channel. Default value: None Obtain the path list for a
                previously created path with get_path.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        path_list_ctype = ctypes.create_string_buffer(path_list.encode(self._encoding))  # case 3
        error_code = self._library.niSwitch_SetPath(vi_ctype, path_list_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def wait_for_debounce(self, maximum_time_ms=5000):
        '''wait_for_debounce

        Pauses until all created paths have settled. If the time you specify
        with the Maximum Time (ms) parameter elapsed before the switch paths
        have settled, this function returns the
        NISWITCH_ERROR_MAX_TIME_EXCEEDED error.

        Args:
            maximum_time_ms (int): Specifies the maximum length of time to wait for all relays in the
                switch module to activate or deactivate. If the specified time elapses
                before all relays active or deactivate, a timeout error is returned.
                Default Value:5000 ms
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        maximum_time_ms_ctype = visatype.ViInt32(maximum_time_ms)  # case 9
        error_code = self._library.niSwitch_WaitForDebounce(vi_ctype, maximum_time_ms_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def wait_for_scan_complete(self, maximum_time_ms=5000):
        '''wait_for_scan_complete

        Pauses until the switch module stops scanning or the maximum time has
        elapsed and returns a timeout error. If the time you specify with the
        Maximum Time (ms) parameter elapsed before the scanning operation has
        finished, this function returns the NISWITCH_ERROR_MAX_TIME_EXCEEDED
        error.

        Args:
            maximum_time_ms (int): Specifies the maximum length of time to wait for the switch module to
                stop scanning. If the specified time elapses before the scan ends,
                NISWITCH_ERROR_MAX_TIME_EXCEEDED error is returned. Default
                Value:5000 ms
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        maximum_time_ms_ctype = visatype.ViInt32(maximum_time_ms)  # case 9
        error_code = self._library.niSwitch_WaitForScanComplete(vi_ctype, maximum_time_ms_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def _close(self):
        '''_close

        Terminates the NI-SWITCH session and all of its attributes and
        deallocates any memory resources the driver uses. Notes: (1) You must
        unlock the session before calling _close. (2) After calling
        _close, you cannot use the instrument driver again until you
        call init or InitWithOptions.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niSwitch_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset(self):
        '''reset

        Disconnects all created paths and returns the switch module to the state
        at initialization. Configuration channel and source channel settings
        remain unchanged.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        error_code = self._library.niSwitch_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_test(self):
        '''self_test

        Verifies that the driver can communicate with the switch module.

        Returns:
            self_test_result (int): Value returned from the switch device self-test. Passed 0 Failed 1
            self_test_message (string): Self-test response string from the switch device. You must pass a ViChar
                array with at least 256 bytes.
        '''
        vi_ctype = visatype.ViSession(self._vi)  # case 1
        self_test_result_ctype = visatype.ViInt16()  # case 14
        self_test_message_ctype = (visatype.ViChar * 256)()  # case 11
        error_code = self._library.niSwitch_self_test(vi_ctype, ctypes.pointer(self_test_result_ctype), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)



