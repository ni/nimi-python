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
    '''
    Enables or disables sharing of an analog bus line so that multiple
    NI SwitchBlock devices may connect to it simultaneously. To enable
    multiple NI SwitchBlock devices to share an analog bus line, set this
    property to TRUE for each device on the channel that corresponds with
    the shared analog bus line. The default value for all devices is FALSE,
    which disables sharing of the analog bus.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Using the
    Analog Bus on an NI SwitchBlock
    Carrier <switch.chm::/SwitchBlock_analog_bus_reservation.html>`__
    '''
    bandwidth = AttributeViReal64(1250005)
    '''
    Returns the bandwidth for the channel in hertz.

    **Related topics**

    `Bandwidth and Insertion Loss <SWITCH.chm::/bandwidth.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__ `RF Switching
    Considerations <SWITCH.chm::/rf.html>`__
    '''
    cabled_module_scan_advanced_bus = AttributeViInt32(1150009)
    '''
    This property has been deprecated and might be removed from a future
    release of NI-SWITCH. Use `niSwitch Route Scan Advanced
    Output <switchviref.chm::/niSwitch_Route_Scan_Advanced_Output.html>`__
    VI instead.
    '''
    cabled_module_trigger_bus = AttributeViInt32(1150008)
    '''
    This property has been deprecated and might be removed from a future
    release of NI-SWITCH. Use the `niSwitch Route Trigger
    Input <switchviref.chm::/niSwitch_Route_Trigger_Input.html>`__ VI
    instead.
    '''
    cache = AttributeViBoolean(1050004)
    '''
    Specifies whether to cache the value of properties. The default value is
    TRUE. Use the `niSwitch Initialize With
    Options <switchviref.chm::/niSwitch_Initialize_With_Options.html>`__ VI
    to override the default value.

    Set this property to TRUE to ensure the instrument driver tracks the
    current instrument settings and avoid sending redundant commands to the
    instrument. The instrument driver can always cache or never cache
    regardless of the setting of this property.

    **Related topics**

    `niSwitch Initialize With
    Options <switchviref.chm::/niSwitch_Initialize_With_Options.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    channel_count = AttributeViInt32(1050203)
    '''
    Contains the number of channels that the instrument driver supports.

    **Related topics**

    `niSwitch Get Channel
    Name <switchviref.chm::/niSwitch_Get_Channel_Name.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    characteristic_impedance = AttributeViReal64(1250016)
    '''
    Returns the characteristic impedance for the channel in ohms.

    **Related topics**

    `Characteristic
    Impedance <SWITCH.chm::/characteristic_impedance.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__ `RF Switching
    Considerations <SWITCH.chm::/rf.html>`__
    '''
    continuous_scan = AttributeViBoolean(1150002)
    '''
    Specifies whether to continuously scan through a scan list. Set the
    property to FALSE to stop scanning after one pass through the scan list.
    Set this property to TRUE to loop continuously through the scan list.

    If you set the property to TRUE, the `niSwitch Wait For Scan To
    Complete <switchviref.chm::/niSwitch_Wait_For_Scan_To_Complete.html>`__
    VI times out, and you must call the `niSwitch Abort
    Scan <switchviref.chm::/niSwitch_Abort_Scan.html>`__ VI to stop the
    scan.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__
    '''
    digital_filter_enable = AttributeViBoolean(1150016)
    '''
    Specifies whether to apply the pulse width filter to the Trigger Input.
    Set the property to TRUE to prevent the switch module from being
    triggered by pulses that are less than 150 ns on PXI trigger lines 0-7.

    When this property is set to FALSE, noise on the PXI trigger lines might
    trigger the switch module. If the device triggering the switch module
    can send pulses greater than 150 ns, do not disable this property.

    **Related topics**

    `Disabling Digital Filtering <SWITCH.chm::/fast_pxi_triggering.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    driver_setup = AttributeViString(1050007)
    '''
    Contains the Driver Setup string that you specified when initializing
    the instrument driver.

    In some cases, you must specify instrument driver options at
    initialization time—for example, when specifying a particular instrument
    model from among a family of instruments that the instrument driver
    supports. This is useful when using simulation.

    You can specify instrument driver-specific options through the
    DriverSetup keyword in the **option string** parameter of the `niSwitch
    Initialize With
    Options <switchviref.chm::/niSwitch_Initialize_With_Options.html>`__ VI,
    or through the IVI Configuration Utility. If you did not specify a
    Driver Setup string, this property returns an empty string.

    **Related topics**

    `niSwitch Initialize With
    Options <switchviref.chm::/niSwitch_Initialize_With_Options.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    group_capabilities = AttributeViString(1050401)
    '''
    Contains a comma-separated (,) list of class-extension groups that the
    instrument driver implements.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    handshaking_initiation = AttributeEnum(1150013, enums.HandshakingInitiation)
    '''
    Specifies how to start handshaking with a measurement device.

    **Related topics**

    `Handshaking <SWITCH.chm::/handshakingg.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__
    '''
    instrument_firmware_revision = AttributeViString(1050510)
    '''
    Contains the firmware revision information for the instrument currently
    in use.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `niSwitch
    Revision Query <switchviref.chm::/niSwitch_Revision_Query.html>`__
    '''
    instrument_manufacturer = AttributeViString(1050511)
    '''
    Contains the name of the manufacturer of the instrument currently in
    use.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    instrument_model = AttributeViString(1050512)
    '''
    Contains the model number or name of the instrument currently in use.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    interchange_check = AttributeViBoolean(1050021)
    '''
    Specifies whether to perform interchangeability checking and retrieve
    interchangeability warnings when you call the `niSwitch Connect
    Channels <switchviref.chm::/niSwitch_Connect_Channels.html>`__,
    `niSwitch Set Path <switchviref.chm::/niSwitch_Set_Path.html>`__ and
    `niSwitch Initiate
    Scan <switchviref.chm::/niSwitch_Initiate_Scan.html>`__ VIs. The default
    value is FALSE.

    Interchangeability checking examines the properties in a capability
    group only if you specify a value for at least one property within that
    group. Interchangeability warnings can occur when a property that you
    have not set or that has been invalidated affects the behavior of the
    instrument.

    Interchangeability warnings indicate that using your application with a
    different instrument might cause different behavior. Call `niSwitch Get
    Next Interchange
    Warning <switchviref.chm::/niSwitch_Get_Next_Interchange_Warning.html>`__
    VI to extract interchange warnings. Call the `niSwitch Clear Interchange
    Warnings <switchviref.chm::/niSwitch_Clear_Interchange_Warnings.html>`__
    VI to clear the list of interchangeability warnings without reading
    them.

    **Related topics**

    `niSwitch Get Next Interchange
    Warning <switchviref.chm::/niSwitch_Get_Next_Interchange_Warning.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `niSwitch
    Reset Interchange
    Check <switchviref.chm::/niSwitch_Reset_Interchange_Check.html>`__
    '''
    io_resource_descriptor = AttributeViString(1050304)
    '''
    Contains the resource descriptor the instrument driver uses to identify
    the physical device.

    If you initialize the instrument driver with a logical name, this
    property contains the resource descriptor that corresponds to the entry
    in the IVI Configuration Utility. If you initialize the instrument
    driver with the resource descriptor, this property contains that value.

    **Related topics**

    `Initialization <SWITCH.chm::/flow_init.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    is_configuration_channel = AttributeViBoolean(1250003)
    '''
    Specifies whether to designate the channel as a configuration channel—a
    channel reserved for internal path creation. The instrument driver uses
    configuration channels to create paths between the channels you specify
    in the `niSwitch Connect
    Channels <switchviref.chm::/niSwitch_Connect_Channels.html>`__ VI.

    Set this property to TRUE to designate the channel as a configuration
    channel. Set this property to FALSE to designate the channel as
    available for external connections. Because you cannot use a
    configuration channel for external connections, the `niSwitch Connect
    Channels <switchviref.chm::/niSwitch_Connect_Channels.html>`__ VI
    returns the Is Configuration Channel error when you attempt to establish
    a connection between a configuration channel and any other channel.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Setting
    Source and Configuration Channels <SWITCH.chm::/configchannels.html>`__
    '''
    is_debounced = AttributeViBoolean(1250002)
    '''
    Indicates whether the entire switch module has settled since the last
    switching command. A value of TRUE indicates that all signals going
    through the switch module are valid.

    **Related topics**

    `Electromechanical Relays <SWITCH.chm::/electromechanical_relay.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Settling
    Time <SWITCH.chm::/settling_time.html>`__
    '''
    is_scanning = AttributeViBoolean(1250024)
    '''
    Indicates whether the switch module has completed the scan operation.
    TRUE indicates that the scan has completed.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__
    '''
    is_source_channel = AttributeViBoolean(1250001)
    '''
    Specifies whether to designate the channel as a source channel.

    Set this property to TRUE when you connect the channel to a power
    supply, a function generator, or an active measurement point on the unit
    under test, and you do not want to connect the channel to another
    source. The instrument driver prevents source channels from connecting
    to each other: when you attempt to connect two source channels, the
    `niSwitch Connect
    Channels <switchviref.chm::/niSwitch_Connect_Channels.html>`__ VI
    returns the Attempt To Connect Sources error.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Setting
    Source and Configuration Channels <SWITCH.chm::/configchannels.html>`__
    '''
    is_waiting_for_trig = AttributeViBoolean(1150004)
    '''
    Indicates with a semi-colon (;) that at that point in the scan list, the
    scan engine should pause until a trigger is received from the trigger
    input. If you generate that trigger through either a hardware pulse or
    the `niSwitch Send Software
    Trigger <switchviref.chm::/niSwitch_Send_Software_Trigger.html>`__ VI,
    you must know when the scan engine has reached such a state.

    **Related topics**

    `niSwitch Configure Scan
    Trigger <switchviref.chm::/niSwitch_Configure_Scan_List.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__
    '''
    logical_name = AttributeViString(1050305)
    '''
    Contains the logical name you specified when opening the current IVI
    session.

    You can wire a logical name to the `niSwitch
    Initialize <switchviref.chm::/niSwitch_Initialize.html>`__ or the
    `niSwitch Initialize With
    Options <switchviref.chm::/niSwitch_Initialize_With_Options.html>`__
    VIs. The IVI Configuration Utility must contain an entry for the logical
    name. The logical name entry refers to a virtual instrument section,
    which specifies a physical device and initial user options, in the IVI
    Configuration file.

    **Related topics**

    `Initialization <SWITCH.chm::/flow_init.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__ `Using NI Switches in
    IVI <SWITCH.chm::/switches_in_ivi.html>`__
    '''
    master_slave_scan_advanced_bus = AttributeViInt32(1150007)
    '''
    This property has been deprecated and might be removed from a future
    release of NI-SWITCH. Use `niSwitch Route Scan Advanced
    Output <switchviref.chm::/niSwitch_Route_Scan_Advanced_Output.html>`__
    VI instead.
    '''
    master_slave_trigger_bus = AttributeViInt32(1150006)
    '''
    This property has been deprecated and might be removed from a future
    release of NI-SWITCH. Use the `niSwitch Route Trigger
    Input <switchviref.chm::/niSwitch_Route_Trigger_Input.html>`__ VI
    instead.
    '''
    max_ac_voltage = AttributeViReal64(1250007)
    '''
    Returns the maximum AC voltage the channel can switch in volts RMS.

    **Related topics**

    `General Switching Considerations <SWITCH.chm::/considerations.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    max_carry_ac_current = AttributeViReal64(1250011)
    '''
    Returns the maximum AC current the channel can carry in amperes RMS.

    **Related topics**

    `General Switching Considerations <SWITCH.chm::/considerations.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    max_carry_ac_power = AttributeViReal64(1250015)
    '''
    Returns the maximum AC power the channel can carry in volt-amperes.

    **Related topics**

    `General Switching Considerations <SWITCH.chm::/considerations.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    max_carry_dc_current = AttributeViReal64(1250010)
    '''
    Returns the maximum DC current the channel can carry in amperes.

    **Related topics**

    `General Switching Considerations <SWITCH.chm::/considerations.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    max_carry_dc_power = AttributeViReal64(1250014)
    '''
    Returns the maximum DC power the channel can carry in watts.

    **Related topics**

    `General Switching Considerations <SWITCH.chm::/considerations.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    max_dc_voltage = AttributeViReal64(1250006)
    '''
    Returns the maximum DC voltage the channel can switch in volts.

    **Related topics**

    `General Switching Considerations <SWITCH.chm::/considerations.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    max_switching_ac_current = AttributeViReal64(1250009)
    '''
    Returns the maximum AC current the channel can switch in amperes RMS.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Switching
    Current <SWITCH.chm::/switching_current.html>`__
    '''
    max_switching_ac_power = AttributeViReal64(1250013)
    '''
    Returns the maximum AC power the channel can switch in volt-amperes.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Switching
    Power <SWITCH.chm::/switching_power.html>`__
    '''
    max_switching_dc_current = AttributeViReal64(1250008)
    '''
    Returns the maximum DC current the channel can switch in amperes.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Switching
    Current <SWITCH.chm::/switching_current.html>`__
    '''
    max_switching_dc_power = AttributeViReal64(1250012)
    '''
    Returns the maximum DC power the channel can switch in watts.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Switching
    Power <SWITCH.chm::/switching_power.html>`__
    '''
    number_of_relays = AttributeViInt32(1150014)
    '''
    Returns the number of relays that the instrument driver supports.

    **Related topics**

    `niSwitch Get Relay
    Name <switchviref.chm::/niSwitch_Get_Relay_Name.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    num_of_columns = AttributeViInt32(1250019)
    '''
    Returns the number of channels on the column of a matrix or scanner. If
    the switch module is a scanner, this property returns the number of
    input channels.

    The `Wire mode <pniSwitch_Wiremode.html>`__ property affects the number
    of available columns. For example, if your switch module has eight input
    lines and you use the 4-wire mode, then the number of columns available
    is two.

    **Related topics**

    `Matrix <SWITCH.chm::/matrix.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    num_of_rows = AttributeViInt32(1250018)
    '''
    Returns the number of channels on the row of a matrix or scanner. If the
    switch module is a scanner, this property returns the number of output
    channels.

    The `Wire mode <pniSwitch_Wiremode.html>`__ property affects the number
    of available rows. For example, if your switch module has eight input
    lines and you use the 2-wire mode, then the number of columns you have
    available is four.

    **Related topics**

    `Matrix <SWITCH.chm::/matrix.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    parsed_scan_list = AttributeViString(1150012)
    '''
    This property has been deprecated and might be removed from a future
    release of NI-SWITCH.
    '''
    power_down_latching_relays_after_debounce = AttributeViBoolean(1150017)
    '''
    Specifies whether to power down latching relays after calling the
    `niSwitch Wait For
    Debounce <switchviref.chm::/niSwitch_Wait_For_Debounce.html>`__ VI. Set
    this property to TRUE to ensure that the relays settle and the latching
    relays power down after you call the `niSwitch Wait for
    Debounce <switchviref.chm::/niSwitch_Wait_For_Debounce.html>`__ VI.

    **Related topics**

    `Armature Relays <SWITCH.chm::/armature_relay.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    query_instrument_status = AttributeViBoolean(1050003)
    '''
    Specifies whether the instrument driver queries the instrument status
    after each operation. The default value is TRUE. Use the `niSwitch
    Initialize With
    Options <switchviref.chm::/niSwitch_Initialize_With_Options.html>`__ VI
    to override the default value.

    Querying the instrument status is useful for debugging. After you
    validate your program, set this property to FALSE to disable status
    checking and maximize performance. The instrument driver can choose to
    ignore status checking for particular properties regardless of the
    setting of this property.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    range_check = AttributeViBoolean(1050002)
    '''
    Specifies whether to validate property values and VI parameters. The
    default value is TRUE. Use the `niSwitch Initialize With
    Options <switchviref.chm::/niSwitch_Initialize_With_Options.html>`__ VI
    to override the default value.

    Set this property to TRUE to validate the parameter values that you pass
    to instrument driver VIs. Range checking parameters is useful for
    debugging. After validating your program, set this property to FALSE to
    disable range checking and maximize performance.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    record_coercions = AttributeViBoolean(1050006)
    '''
    Specifies whether the IVI engine keeps a list of the value coercions it
    makes for properties with ViInt32 and ViReal64 datatypes. The default
    value is FALSE. Use the `niSwitch Initialize With
    Options <switchviref.chm::/niSwitch_Initialize_With_Options.html>`__ VI
    to override the default value.

    Call `niSwitch Get Next Coercion
    Record <switchviref.chm::/niSwitch_Get_Next_Coercion_Record.html>`__ VI
    to extract and delete the oldest coercion record from the list.

    **Related topics**

    `niSwitch Get Next Coercion
    Record <switchviref.chm::/niSwitch_Get_Next_Coercion_Record.html>`__
    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    scan_advanced_output = AttributeEnum(1250023, enums.ScanAdvancedOutput)
    '''
    Specifies the method to use to notify another instrument that all
    signals through the switch module have settled following the processing
    of one entry in the scan list.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__
    '''
    scan_advanced_polarity = AttributeEnum(1150011, enums.ScanAdvancedPolarity)
    '''
    Specifies the driving level for the Scan Advanced Output signal sent
    from the switch module through either the external (PXI/PXIe) or front
    connector (SCXI) lines. When the Scan Advanced Output signal is sent to
    one of the PXI_Trig lines, the driven level is always low and this
    property is ignored. Between each Scan Advanced Output signal, the line
    is not driven and is in a high-impedance state.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__
    '''
    scan_delay = AttributeViReal64(1250025)
    '''
    Specifies the minimum amount of time the switch module waits before it
    asserts the scan advanced output trigger after opening or closing the
    switch. The switch module always waits for debounce before asserting the
    trigger. Thus, the actual delay will always be the greater value of the
    settling time and the value you specify as the switch delay, measured in
    seconds. Settling time can vary depending on the switch module.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__
    '''
    scan_list = AttributeViString(1250020)
    '''
    Contains a scan list (a string that specifies channel connections and
    trigger conditions). The `niSwitch Initiate
    Scan <switchviref.chm::/niSwitch_Initiate_Scan.html>`__ VI makes or
    breaks connections and waits for triggers according to the instructions
    in the scan list. The scan list is comprised of channel names separated
    by special characters that determine the operations the scanner performs
    on the channels when it executes the scan list.

    To create a path between two channels, use the following character
    between the two channel names: -> (a dash followed by a '>' sign)
    Example: 'CH1->CH2' tells the switch to make a path from channel CH1 to
    channel CH2.

    To break or clear a path, use the following character as a prefix before
    the path: ~ (tilde) Example: '~CH1->CH2' tells the switch to break the
    path from channel CH1 to channel CH2.

    To tell the switch module to wait for a trigger event, use the following
    character as a separator between paths: ; (semi-colon) Example:
    'CH1->CH2;CH3->CH4' tells the switch to make the path from channel CH1
    to channel CH2, wait for a trigger, and then make the path from CH3 to
    CH4.

    To tell the switch module to create multiple paths as quickly as
    possible, use the & (ampersand) or && (double ampersand) as a separator
    between the paths. The & in 'CH0->CH1;CH2->CH3&CH4->CH5' instructs the
    scanner to make the path between channels CH0 and CH1, wait for a
    trigger, and then make the paths between channels CH2 and CH3 and
    between channels CH4 and CH5 in no particular order without waiting for
    settling or waiting for a trigger. If wait for settling is desired,
    replace & with &&. The && in 'CH0->CH1;CH2->CH3&&CH4->CH5' instructs the
    scanner to make the path between channels CH0 and CH1, wait for a
    trigger, and then make the path between channels CH2 and CH3, wait for
    settling, then make the path between channels CH4 and CH5.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Scan
    Lists <SWITCH.chm::/scan_list.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__
    '''
    scan_mode = AttributeEnum(1250021, enums.ScanMode)
    '''
    Specifies how to handle existing connections that conflict with the
    connections you make in a scan list. For example, if CH1 is already
    connected to CH2 and the scan list instructs the switch module to
    connect CH1 to CH3, this property specifies what happens to the
    connection between CH1 and CH2.

    Set the property value to **None** to make the switch module take no
    action on existing paths. Set the value to **Break Before Make** to make
    the switch module break conflicting paths before making new ones. Set
    the value to **Break After Make** to make the switch module break
    conflicting paths after making new ones. Most switch modules support
    only one of the possible values: in such cases, this property serves as
    an indicator of the module's behavior.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__
    '''
    serial_number = AttributeViString(1150015)
    '''
    Returns the serial number for the switch module controlled by the
    instrument driver. If the switch module does not return a serial number,
    the instrument driver returns the Invalid Attribute error.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    serial_number_i32 = AttributeViInt32(1150001)
    '''
    This property has been deprecated and might be removed from a future
    release of NI-SWITCH.
    '''
    settling_time = AttributeViReal64(1250004)
    '''
    Returns the maximum length of time in seconds from after you make a
    connection until the signal flowing through the channel settles.
    Settling time can vary depending on the switch module.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Settling
    Time <SWITCH.chm::/settling_time.html>`__
    '''
    simulate = AttributeViBoolean(1050005)
    '''
    Specifies whether to simulate instrument driver I/O operations. The
    default value is FALSE. Use the `niSwitch Initialize With
    Options <switchviref.chm::/niSwitch_Initialize_With_Options.html>`__ VI
    to override the default value.

    Set this property to TRUE to perform range checking and call
    Ivi_GetAttribute and Ivi_SetAttribute functions without performing
    instrument I/O. For output parameters that represent instrument data,
    the instrument driver VIs return calculated values.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `Simulating
    a Switch <SWITCH.chm::/simulate.html>`__
    '''
    specific_driver_class_spec_major_version = AttributeViInt32(1050515)
    '''
    Contains the major version number of the IviSwtch class specification.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    specific_driver_class_spec_minor_version = AttributeViInt32(1050516)
    '''
    Contains the minor version number of the class specification with which
    the instrument driver is compliant.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    specific_driver_description = AttributeViString(1050514)
    '''
    Contains a brief description of the instrument driver.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    specific_driver_prefix = AttributeViString(1050302)
    '''
    Contains the prefix for all of the instrument driver VIs.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    specific_driver_revision = AttributeViString(1050551)
    '''
    Contains additional version information about the instrument driver.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__ `niSwitch
    Revision Query VI <switchviref.chm::/niSwitch_Revision_Query.html>`__
    '''
    specific_driver_vendor = AttributeViString(1050513)
    '''
    Contains the name of the vendor that supplies the instrument driver.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    supported_instrument_models = AttributeViString(1050327)
    '''
    Contains a comma-separated (,) list of supported instrument models.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    temperature = AttributeViReal64(1150019)
    '''
    Returns the temperature as read by the Switch module in degrees Celsius.
    Refer to the device documentation for more information.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    '''
    trigger_input = AttributeEnum(1250022, enums.TriggerInput)
    '''
    Specifies the source of the trigger for which the switch module can wait
    upon encountering a semi-colon (;) when processing a scan list. When the
    trigger occurs, the switch module advances to the next entry in the scan
    list.

    **Related topics**

    `niSwitch Configure Scan
    List <switchviref.chm::/niSwitch_Configure_Scan_List.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__
    '''
    trigger_input_polarity = AttributeEnum(1150010, enums.TriggerInputPolarity)
    '''
    Determines the behavior of the trigger input.

    **Related topics**

    `niSwitch Properties <switchpropref.chm::/cniSwitch.html>`__
    `Scanning <SWITCH.chm::/scanning_fundamentals.html>`__
    '''
    trigger_mode = AttributeViInt32(1150005)
    '''
    This property has been deprecated and might be removed from a future
    release of NI-SWITCH. Use the `niSwitch Route Trigger
    Input <switchviref.chm::/niSwitch_Route_Trigger_Input.html>`__ and/or
    `niSwitch Route Scan Advanced
    Output <switchviref.chm::/niSwitch_Route_Scan_Advanced_Output.html>`__
    VIs instead.
    '''
    wire_mode = AttributeViInt32(1250017)
    '''
    Returns the wire mode of the switch module. This property affects the
    values of the `Number of Rows <pniSwitch_NumberofRows.html>`__ and
    `Number of Columns <pniSwitch_NumberofColumns.html>`__ properties. The
    actual number of input and output lines on the switch module does not
    change, but the number of channels depends on how many lines constitute
    each channel.

    **Related topics**

    `N-Wire Switching Modes <SWITCH.chm::/xwire.html>`__ `niSwitch
    Properties <switchpropref.chm::/cniSwitch.html>`__
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
        try:
            '''
            Return code > 0 from first call to GetError represents the size of
            the description.  Call it again.
            Ignore incoming IVI error code and return description from the driver
            (trust that the IVI error code was properly stored in the session
            by the driver)
            '''
            # TODO(texasaggie97) This currently does not work - _get_error() will raise
            # an exception that then calls this function, causing infinite recursion.
            # Fix is beyond the scope of this PR
            # Also fix documentation.
            (new_error_code, new_error_string) = self._get_error()
            return new_error_code, new_error_string
        except errors.Error:
            '''
            Return code <= 0 from GetError indicates a problem.  This is expected
            when the session is invalid (IVI spec requires GetError to fail).
            Use GetErrorMessage instead.  It doesn't require a session.

            Call niSwitch_GetErrorMessage, pass VI_NULL for the buffer in order to retrieve
            the length of the error message.
            '''
            new_error_string = self._get_error_message(error_code)
            return error_code, new_error_string

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
        description_ctype = ctypes.cast(ctypes.create_string_buffer(buffersize), ctypes_types.ViString_ctype)
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

