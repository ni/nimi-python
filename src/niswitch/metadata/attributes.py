# -*- coding: utf-8 -*-
attributes = {
    1050002: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Specifies whether to validate property values and VI parameters. The
default value is TRUE. Use the niSwitch Initialize With Options VI to
override the default value.

Set this property to TRUE to validate the parameter values that you pass
to instrument driver VIs. Range checking parameters is useful for
debugging. After validating your program, set this property to FALSE to
disable range checking and maximize performance.
''',
        'lv_property': 'Inherent IVI Attributes:User Options:Range Check',
        'name': 'RANGE_CHECK',
        'resettable': 'No',
        'short_description': '''
Specifies whether to validate property values and VI parameters. The
default value is TRUE. Use the niSwitch Initialize With Options VI to
override the default value.
''',
        'type': 'ViBoolean',
    },
    1050003: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Specifies whether the instrument driver queries the instrument status
after each operation. The default value is TRUE. Use the niSwitch
Initialize With Options VI to override the default value.

Querying the instrument status is useful for debugging. After you
validate your program, set this property to FALSE to disable status
checking and maximize performance. The instrument driver can choose to
ignore status checking for particular properties regardless of the
setting of this property.
''',
        'lv_property': '''
Inherent IVI Attributes:User Options:Query Instrument Status
''',
        'name': 'QUERY_INSTRUMENT_STATUS',
        'resettable': 'No',
        'short_description': '''
Specifies whether the instrument driver queries the instrument status
after each operation. The default value is TRUE. Use the niSwitch
Initialize With Options VI to override the default value.
''',
        'type': 'ViBoolean',
    },
    1050004: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Specifies whether to cache the value of properties. The default value is
TRUE. Use the niSwitch Initialize With Options VI to override the
default value.

Set this property to TRUE to ensure the instrument driver tracks the
current instrument settings and avoid sending redundant commands to the
instrument. The instrument driver can always cache or never cache
regardless of the setting of this property.
''',
        'lv_property': 'Inherent IVI Attributes:User Options:Cache',
        'name': 'CACHE',
        'resettable': 'No',
        'short_description': '''
Specifies whether to cache the value of properties. The default value is
TRUE. Use the niSwitch Initialize With Options VI to override the
default value.
''',
        'type': 'ViBoolean',
    },
    1050005: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Specifies whether to simulate instrument driver I/O operations. The
default value is FALSE. Use the niSwitch Initialize With Options VI to
override the default value.

Set this property to TRUE to perform range checking and call
Ivi\_GetAttribute and Ivi\_SetAttribute functions without performing
instrument I/O. For output parameters that represent instrument data,
the instrument driver VIs return calculated values.
''',
        'lv_property': 'Inherent IVI Attributes:User Options:Simulate',
        'name': 'SIMULATE',
        'resettable': 'No',
        'short_description': '''
Specifies whether to simulate instrument driver I/O operations. The
default value is FALSE. Use the niSwitch Initialize With Options VI to
override the default value.
''',
        'type': 'ViBoolean',
    },
    1050006: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Specifies whether the IVI engine keeps a list of the value coercions it
makes for properties with ViInt32 and ViReal64 datatypes. The default
value is FALSE. Use the niSwitch Initialize With Options VI to override
the default value.

Call niSwitch Get Next Coercion Record VI to extract and delete the
oldest coercion record from the list.
''',
        'lv_property': '''
Inherent IVI Attributes:User Options:Record Value Coercions
''',
        'name': 'RECORD_VALUE_COERCIONS',
        'resettable': 'No',
        'short_description': '''
Specifies whether the IVI engine keeps a list of the value coercions it
makes for properties with ViInt32 and ViReal64 datatypes. The default
value is FALSE. Use the niSwitch Initialize With Options VI to override
the default value.
''',
        'type': 'ViBoolean',
    },
    1050007: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Contains the Driver Setup string that you specified when initializing
the instrument driver.

In some cases, you must specify instrument driver options at
initialization time—for example, when specifying a particular instrument
model from among a family of instruments that the instrument driver
supports. This is useful when using simulation.

You can specify instrument driver-specific options through the
DriverSetup keyword in the niSwitch Initialize With Options VI, or
through the IVI Configuration Utility. If you did not specify a Driver
Setup string, this property returns an empty string.\ **option string**
parameter of the
''',
        'lv_property': '''
Inherent IVI Attributes:Advanced Session Information:Driver Setup
''',
        'name': 'DRIVER_SETUP',
        'resettable': 'No',
        'short_description': '''
Contains the Driver Setup string that you specified when initializing
the instrument driver.
''',
        'type': 'ViString',
    },
    1050021: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Specifies whether to perform interchangeability checking and retrieve
interchangeability warnings when you call the niSwitch Connect Channels
, niSwitch Set Path and niSwitch Initiate Scan VIs. The default value is
FALSE.

Interchangeability checking examines the properties in a capability
group only if you specify a value for at least one property within that
group. Interchangeability warnings can occur when a property that you
have not set or that has been invalidated affects the behavior of the
instrument.

Interchangeability warnings indicate that using your application with a
different instrument might cause different behavior. Call niSwitch Get
Next Interchange Warning VI to extract interchange warnings. Call the
niSwitch Clear Interchange Warnings VI to clear the list of
interchangeability warnings without reading them.
''',
        'lv_property': '''
Inherent IVI Attributes:User Options:Interchange Check
''',
        'name': 'INTERCHANGE_CHECK',
        'resettable': 'No',
        'short_description': '''
Specifies whether to perform interchangeability checking and retrieve
interchangeability warnings when you call the niSwitch Connect Channels
, niSwitch Set Path and niSwitch Initiate Scan VIs. The default value is
FALSE.
''',
        'type': 'ViBoolean',
    },
    1050203: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Driver Capabilities:Channel Count
''',
        'name': 'CHANNEL_COUNT',
        'resettable': 'No',
        'short_description': '''
Contains the number of channels that the instrument driver supports.
''',
        'type': 'ViInt32',
    },
    1050302: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Driver Identification:Driver Prefix
''',
        'name': 'DRIVER_PREFIX',
        'resettable': 'No',
        'short_description': '''
Contains the prefix for all of the instrument driver VIs.
''',
        'type': 'ViString',
    },
    1050304: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Contains the resource descriptor the instrument driver uses to identify
the physical device.

If you initialize the instrument driver with a logical name, this
property contains the resource descriptor that corresponds to the entry
in the IVI Configuration Utility. If you initialize the instrument
driver with the resource descriptor, this property contains that value.
''',
        'lv_property': '''
Inherent IVI Attributes:Advanced Session Information:IO Resource Descriptor
''',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'resettable': 'No',
        'short_description': '''
Contains the resource descriptor the instrument driver uses to identify
the physical device.
''',
        'type': 'ViString',
    },
    1050305: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Contains the logical name you specified when opening the current IVI
session.

You can wire a logical name to the niSwitch Initialize or the niSwitch
Initialize With Options VIs. The IVI Configuration Utility must contain
an entry for the logical name. The logical name entry refers to a
virtual instrument section, which specifies a physical device and
initial user options, in the IVI Configuration file.
''',
        'lv_property': '''
Inherent IVI Attributes:Advanced Session Information:Logical Name
''',
        'name': 'LOGICAL_NAME',
        'resettable': 'No',
        'short_description': '''
Contains the logical name you specified when opening the current IVI
session.
''',
        'type': 'ViString',
    },
    1050327: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models
''',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'resettable': 'No',
        'short_description': '''
Contains a comma-separated (,) list of supported instrument models.
''',
        'type': 'ViString',
    },
    1050401: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities
''',
        'name': 'CLASS_GROUP_CAPABILITIES',
        'resettable': 'No',
        'short_description': '''
Contains a comma-separated (,) list of class-extension groups that the
instrument driver implements.
''',
        'type': 'ViString',
    },
    1050510: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Instrument Identification:Firmware Revision
''',
        'name': 'FIRMWARE_REVISION',
        'resettable': 'No',
        'short_description': '''
Contains the firmware revision information for the instrument currently
in use.
''',
        'type': 'ViString',
    },
    1050511: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Instrument Identification:Manufacturer
''',
        'name': 'MANUFACTURER',
        'resettable': 'No',
        'short_description': '''
Contains the name of the manufacturer of the instrument currently in
use.
''',
        'type': 'ViString',
    },
    1050512: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Instrument Identification:Model
''',
        'name': 'MODEL',
        'resettable': 'No',
        'short_description': '''
Contains the model number or name of the instrument currently in use.
''',
        'type': 'ViString',
    },
    1050513: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Driver Identification:Driver Vendor
''',
        'name': 'DRIVER_VENDOR',
        'resettable': 'No',
        'short_description': '''
Contains the name of the vendor that supplies the instrument driver.
''',
        'type': 'ViString',
    },
    1050514: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Driver Identification:Description
''',
        'name': 'DESCRIPTION',
        'resettable': 'No',
        'short_description': '''
Contains a brief description of the instrument driver.
''',
        'type': 'ViString',
    },
    1050515: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Driver Identification:Class Specification Major Version
''',
        'name': 'CLASS_SPECIFICATION_MAJOR_VERSION',
        'resettable': 'No',
        'short_description': '''
Contains the major version number of the IviSwtch class specification.
''',
        'type': 'ViInt32',
    },
    1050516: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Driver Identification:Class Specification Minor Version
''',
        'name': 'CLASS_SPECIFICATION_MINOR_VERSION',
        'resettable': 'No',
        'short_description': '''
Contains the minor version number of the class specification with which
the instrument driver is compliant.
''',
        'type': 'ViInt32',
    },
    1050551: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Driver Identification:Revision
''',
        'name': 'REVISION',
        'resettable': 'No',
        'short_description': '''
Contains additional version information about the instrument driver.
''',
        'type': 'ViString',
    },
    1150001: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Obsolete Attributes:Serial Number',
        'name': 'SERIAL_NUMBERI32',
        'resettable': 'No',
        'short_description': '''
This property has been deprecated and might be removed from a future
release of NI-SWITCH.
''',
        'type': 'ViInt32',
    },
    1150002: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Specifies whether to continuously scan through a scan list. Set the
property to FALSE to stop scanning after one pass through the scan list.
Set this property to TRUE to loop continuously through the scan list.

If you set the property to TRUE, the niSwitch Wait For Scan To Complete
VI times out, and you must call the niSwitch Abort Scan VI to stop the
scan.
''',
        'lv_property': 'Scanning Configuration:Continuous Scan',
        'name': 'CONTINUOUS_SCAN',
        'resettable': 'No',
        'short_description': '''
Specifies whether to continuously scan through a scan list. Set the
property to FALSE to stop scanning after one pass through the scan list.
Set this property to TRUE to loop continuously through the scan list.
''',
        'type': 'ViBoolean',
    },
    1150004: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Scanning Configuration:Is Waiting for Trigger?',
        'name': 'IS_WAITING_FOR_TRIGGER',
        'resettable': 'No',
        'short_description': '''
Indicates with a semi-colon (;) that at that point in the scan list, the
scan engine should pause until a trigger is received from the trigger
input. If you generate that trigger through either a hardware pulse or
the niSwitch Send Software Trigger VI, you must know when the scan
engine has reached such a state.
''',
        'type': 'ViBoolean',
    },
    1150005: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Obsolete Attributes:Trigger Mode',
        'name': 'TRIGGER_MODE',
        'resettable': 'No',
        'short_description': '''
This property has been deprecated and might be removed from a future
release of NI-SWITCH. Use the niSwitch Route Trigger Input and/or
niSwitch Route Scan Advanced Output VIs instead.
''',
        'type': 'ViInt32',
    },
    1150006: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Obsolete Attributes:Master Slave Trigger Bus',
        'name': 'MASTER_SLAVE_TRIGGER_BUS',
        'resettable': 'No',
        'short_description': '''
This property has been deprecated and might be removed from a future
release of NI-SWITCH. Use the niSwitch Route Trigger Input VI instead.
''',
        'type': 'ViInt32',
    },
    1150007: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Obsolete Attributes:Master Slave Scan Advanced Bus
''',
        'name': 'MASTER_SLAVE_SCAN_ADVANCED_BUS',
        'resettable': 'No',
        'short_description': '''
This property has been deprecated and might be removed from a future
release of NI-SWITCH. Use niSwitch Route Scan Advanced Output VI
instead.
''',
        'type': 'ViInt32',
    },
    1150008: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Obsolete Attributes:Cabled Module Trigger Bus',
        'name': 'CABLED_MODULE_TRIGGER_BUS',
        'resettable': 'No',
        'short_description': '''
This property has been deprecated and might be removed from a future
release of NI-SWITCH. Use the niSwitch Route Trigger Input VI instead.
''',
        'type': 'ViInt32',
    },
    1150009: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Obsolete Attributes:Cabled Module Scan Advanced Bus
''',
        'name': 'CABLED_MODULE_SCAN_ADVANCED_BUS',
        'resettable': 'No',
        'short_description': '''
This property has been deprecated and might be removed from a future
release of NI-SWITCH. Use niSwitch Route Scan Advanced Output VI
instead.
''',
        'type': 'ViInt32',
    },
    1150010: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TriggerInputPolarity',
        'lv_property': 'Scanning Configuration:Trigger Input Polarity',
        'name': 'TRIGGER_INPUT_POLARITY',
        'resettable': 'No',
        'short_description': 'Determines the behavior of the trigger input.',
        'type': 'ViInt32',
    },
    1150011: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'ScanAdvancedPolarity',
        'lv_property': 'Scanning Configuration:Scan Advanced Polarity',
        'name': 'SCAN_ADVANCED_POLARITY',
        'resettable': 'No',
        'short_description': '''
Specifies the driving level for the Scan Advanced Output signal sent
from the switch module through either the external (PXI/PXIe) or front
connector (SCXI) lines. When the Scan Advanced Output signal is sent to
one of the PXI\_Trig lines, the driven level is always low and this
property is ignored. Between each Scan Advanced Output signal, the line
is not driven and is in a high-impedance state.
''',
        'type': 'ViInt32',
    },
    1150012: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Obsolete Attributes:Parsed Scan List',
        'name': 'PARSED_SCAN_LIST',
        'resettable': 'No',
        'short_description': '''
This property has been deprecated and might be removed from a future
release of NI-SWITCH.
''',
        'type': 'ViString',
    },
    1150013: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'HandshakingInitiation',
        'lv_property': 'Scanning Configuration:Handshaking Initiation',
        'name': 'HANDSHAKING_INITIATION',
        'resettable': 'No',
        'short_description': '''
Specifies how to start handshaking with a measurement device.
''',
        'type': 'ViInt32',
    },
    1150014: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Module Characteristics:Number of Relays',
        'name': 'NUMBER_OF_RELAYS',
        'resettable': 'No',
        'short_description': '''
Returns the number of relays that the instrument driver supports.
''',
        'type': 'ViInt32',
    },
    1150015: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Module Characteristics:Serial Number',
        'name': 'SERIAL_NUMBER',
        'resettable': 'No',
        'short_description': '''
Returns the serial number for the switch module controlled by the
instrument driver. If the switch module does not return a serial number,
the instrument driver returns the Invalid Attribute error.
''',
        'type': 'ViString',
    },
    1150016: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Specifies whether to apply the pulse width filter to the Trigger Input.
Set the property to TRUE to prevent the switch module from being
triggered by pulses that are less than 150 ns on PXI trigger lines 0-7.

When this property is set to FALSE, noise on the PXI trigger lines might
trigger the switch module. If the device triggering the switch module
can send pulses greater than 150 ns, do not disable this property.
''',
        'lv_property': 'Scanning Configuration:Digital Filter Enable',
        'name': 'DIGITAL_FILTER_ENABLE',
        'resettable': 'No',
        'short_description': '''
Specifies whether to apply the pulse width filter to the Trigger Input.
Set the property to TRUE to prevent the switch module from being
triggered by pulses that are less than 150 ns on PXI trigger lines 0-7.
''',
        'type': 'ViBoolean',
    },
    1150017: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Module Characteristics:Power Down Latching Relays After Debounce
''',
        'name': 'POWER_DOWN_LATCHING_RELAYS_AFTER_DEBOUNCE',
        'resettable': 'No',
        'short_description': '''
Specifies whether to power down latching relays after calling the
niSwitch Wait For Debounce VI. Set this property to TRUE to ensure that
the relays settle and the latching relays power down after you call the
niSwitch Wait for Debounce VI.
''',
        'type': 'ViBoolean',
    },
    1150018: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Channel Configuration:Analog Bus Sharing Enable',
        'name': 'ANALOG_BUS_SHARING_ENABLE',
        'resettable': 'No',
        'short_description': '''
Enables or disables sharing of an analog bus line so that multiple
NI SwitchBlock devices may connect to it simultaneously. To enable
multiple NI SwitchBlock devices to share an analog bus line, set this
property to TRUE for each device on the channel that corresponds with
the shared analog bus line. The default value for all devices is FALSE,
which disables sharing of the analog bus.
''',
        'type': 'ViBoolean',
    },
    1150019: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Module Characteristics:Temperature',
        'name': 'TEMPERATURE',
        'resettable': 'No',
        'short_description': '''
Returns the temperature as read by the Switch module in degrees Celsius.
Refer to the device documentation for more information.
''',
        'type': 'ViReal64',
    },
    1250001: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Specifies whether to designate the channel as a source channel.

Set this property to TRUE when you connect the channel to a power
supply, a function generator, or an active measurement point on the unit
under test, and you do not want to connect the channel to another
source. The instrument driver prevents source channels from connecting
to each other: when you attempt to connect two source channels, the
niSwitch Connect Channels VI returns the Attempt To Connect Sources
error.
''',
        'lv_property': 'Channel Configuration:Is Source Channel',
        'name': 'IS_SOURCE_CHANNEL',
        'resettable': 'No',
        'short_description': '''
Specifies whether to designate the channel as a source channel.
''',
        'type': 'ViBoolean',
    },
    1250002: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Module Characteristics:Is Debounced',
        'name': 'IS_DEBOUNCED',
        'resettable': 'No',
        'short_description': '''
Indicates whether the entire switch module has settled since the last
switching command. A value of TRUE indicates that all signals going
through the switch module are valid.
''',
        'type': 'ViBoolean',
    },
    1250003: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Specifies whether to designate the channel as a configuration channel—a
channel reserved for internal path creation. The instrument driver uses
configuration channels to create paths between the channels you specify
in the niSwitch Connect Channels VI.

Set this property to TRUE to designate the channel as a configuration
channel. Set this property to FALSE to designate the channel as
available for external connections. Because you cannot use a
configuration channel for external connections, the niSwitch Connect
Channels VI returns the Is Configuration Channel error when you attempt
to establish a connection between a configuration channel and any other
channel.
''',
        'lv_property': 'Channel Configuration:Is Configuration Channel',
        'name': 'IS_CONFIGURATION_CHANNEL',
        'resettable': 'No',
        'short_description': '''
Specifies whether to designate the channel as a configuration channel—a
channel reserved for internal path creation. The instrument driver uses
configuration channels to create paths between the channels you specify
in the niSwitch Connect Channels VI.
''',
        'type': 'ViBoolean',
    },
    1250004: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Module Characteristics:Settling Time',
        'name': 'SETTLING_TIME',
        'resettable': 'No',
        'short_description': '''
Returns the maximum length of time in seconds from after you make a
connection until the signal flowing through the channel settles.
Settling time can vary depending on the switch module.
''',
        'type': 'ViReal64',
    },
    1250005: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Module Characteristics:Bandwidth',
        'name': 'BANDWIDTH',
        'resettable': 'No',
        'short_description': 'Returns the bandwidth for the channel in hertz.',
        'type': 'ViReal64',
    },
    1250006: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Module Characteristics:Maximum DC Voltage',
        'name': 'MAXIMUM_DC_VOLTAGE',
        'resettable': 'No',
        'short_description': '''
Returns the maximum DC voltage the channel can switch in volts.
''',
        'type': 'ViReal64',
    },
    1250007: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Module Characteristics:Maximum AC Voltage',
        'name': 'MAXIMUM_AC_VOLTAGE',
        'resettable': 'No',
        'short_description': '''
Returns the maximum AC voltage the channel can switch in volts RMS.
''',
        'type': 'ViReal64',
    },
    1250008: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Module Characteristics:Maximum Switching DC Current
''',
        'name': 'MAXIMUM_SWITCHING_DC_CURRENT',
        'resettable': 'No',
        'short_description': '''
Returns the maximum DC current the channel can switch in amperes.
''',
        'type': 'ViReal64',
    },
    1250009: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Module Characteristics:Maximum Switching AC Current
''',
        'name': 'MAXIMUM_SWITCHING_AC_CURRENT',
        'resettable': 'No',
        'short_description': '''
Returns the maximum AC current the channel can switch in amperes RMS.
''',
        'type': 'ViReal64',
    },
    1250010: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Module Characteristics:Maximum Carry DC Current',
        'name': 'MAXIMUM_CARRY_DC_CURRENT',
        'resettable': 'No',
        'short_description': '''
Returns the maximum DC current the channel can carry in amperes.
''',
        'type': 'ViReal64',
    },
    1250011: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Module Characteristics:Maximum Carry AC Current',
        'name': 'MAXIMUM_CARRY_AC_CURRENT',
        'resettable': 'No',
        'short_description': '''
Returns the maximum AC current the channel can carry in amperes RMS.
''',
        'type': 'ViReal64',
    },
    1250012: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Module Characteristics:Maximum Switching DC Power',
        'name': 'MAXIMUM_SWITCHING_DC_POWER',
        'resettable': 'No',
        'short_description': '''
Returns the maximum DC power the channel can switch in watts.
''',
        'type': 'ViReal64',
    },
    1250013: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Module Characteristics:Maximum Switching AC Power',
        'name': 'MAXIMUM_SWITCHING_AC_POWER',
        'resettable': 'No',
        'short_description': '''
Returns the maximum AC power the channel can switch in volt-amperes.
''',
        'type': 'ViReal64',
    },
    1250014: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Module Characteristics:Maximum Carry DC Power',
        'name': 'MAXIMUM_CARRY_DC_POWER',
        'resettable': 'No',
        'short_description': '''
Returns the maximum DC power the channel can carry in watts.
''',
        'type': 'ViReal64',
    },
    1250015: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Module Characteristics:Maximum Carry AC Power',
        'name': 'MAXIMUM_CARRY_AC_POWER',
        'resettable': 'No',
        'short_description': '''
Returns the maximum AC power the channel can carry in volt-amperes.
''',
        'type': 'ViReal64',
    },
    1250016: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Module Characteristics:Characteristic Impedance',
        'name': 'CHARACTERISTIC_IMPEDANCE',
        'resettable': 'No',
        'short_description': '''
Returns the characteristic impedance for the channel in ohms.
''',
        'type': 'ViReal64',
    },
    1250017: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Module Characteristics:Wire mode',
        'name': 'WIRE_MODE',
        'resettable': 'No',
        'short_description': '''
Returns the wire mode of the switch module. This property affects the
values of the Number of Rows and Number of Columns properties. The
actual number of input and output lines on the switch module does not
change, but the number of channels depends on how many lines constitute
each channel.
''',
        'type': 'ViInt32',
    },
    1250018: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Returns the number of channels on the row of a matrix or scanner. If the
switch module is a scanner, this property returns the number of output
channels.

The Wire mode property affects the number of available rows. For
example, if your switch module has eight input lines and you use the
2-wire mode, then the number of columns you have available is four.
''',
        'lv_property': 'Matrix Configuration:Number of Rows',
        'name': 'NUMBER_OF_ROWS',
        'resettable': 'No',
        'short_description': '''
Returns the number of channels on the row of a matrix or scanner. If the
switch module is a scanner, this property returns the number of output
channels.
''',
        'type': 'ViInt32',
    },
    1250019: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Returns the number of channels on the column of a matrix or scanner. If
the switch module is a scanner, this property returns the number of
input channels.

The Wire mode property affects the number of available columns. For
example, if your switch module has eight input lines and you use the
4-wire mode, then the number of columns available is two.
''',
        'lv_property': 'Matrix Configuration:Number of Columns',
        'name': 'NUMBER_OF_COLUMNS',
        'resettable': 'No',
        'short_description': '''
Returns the number of channels on the column of a matrix or scanner. If
the switch module is a scanner, this property returns the number of
input channels.
''',
        'type': 'ViInt32',
    },
    1250020: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Contains a scan list (a string that specifies channel connections and
trigger conditions). The niSwitch Initiate Scan VI makes or breaks
connections and waits for triggers according to the instructions in the
scan list. The scan list is comprised of channel names separated by
special characters that determine the operations the scanner performs on
the channels when it executes the scan list.

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
''',
        'lv_property': 'Scanning Configuration:Scan List',
        'name': 'SCAN_LIST',
        'resettable': 'No',
        'short_description': '''
Contains a scan list (a string that specifies channel connections and
trigger conditions). The niSwitch Initiate Scan VI makes or breaks
connections and waits for triggers according to the instructions in the
scan list. The scan list is comprised of channel names separated by
special characters that determine the operations the scanner performs on
the channels when it executes the scan list.
''',
        'type': 'ViString',
    },
    1250021: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'ScanMode',
        'long_description': '''
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
''',
        'lv_property': 'Scanning Configuration:Scan Mode',
        'name': 'SCAN_MODE',
        'resettable': 'No',
        'short_description': '''
Specifies how to handle existing connections that conflict with the
connections you make in a scan list. For example, if CH1 is already
connected to CH2 and the scan list instructs the switch module to
connect CH1 to CH3, this property specifies what happens to the
connection between CH1 and CH2.
''',
        'type': 'ViInt32',
    },
    1250022: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TriggerInput',
        'lv_property': 'Scanning Configuration:Trigger Input',
        'name': 'TRIGGER_INPUT',
        'resettable': 'No',
        'short_description': '''
Specifies the source of the trigger for which the switch module can wait
upon encountering a semi-colon (;) when processing a scan list. When the
trigger occurs, the switch module advances to the next entry in the scan
list.
''',
        'type': 'ViInt32',
    },
    1250023: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'ScanAdvancedOutput',
        'lv_property': 'Scanning Configuration:Scan Advanced Output',
        'name': 'SCAN_ADVANCED_OUTPUT',
        'resettable': 'No',
        'short_description': '''
Specifies the method to use to notify another instrument that all
signals through the switch module have settled following the processing
of one entry in the scan list.
''',
        'type': 'ViInt32',
    },
    1250024: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Scanning Configuration:Is Scanning',
        'name': 'IS_SCANNING',
        'resettable': 'No',
        'short_description': '''
Indicates whether the switch module has completed the scan operation.
TRUE indicates that the scan has completed.
''',
        'type': 'ViBoolean',
    },
    1250025: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Scanning Configuration:Scan Delay',
        'name': 'SCAN_DELAY',
        'resettable': 'No',
        'short_description': '''
Specifies the minimum amount of time the switch module waits before it
asserts the scan advanced output trigger after opening or closing the
switch. The switch module always waits for debounce before asserting the
trigger. Thus, the actual delay will always be the greater value of the
settling time and the value you specify as the switch delay, measured in
seconds. Settling time can vary depending on the switch module.
''',
        'type': 'ViReal64',
    },
}
