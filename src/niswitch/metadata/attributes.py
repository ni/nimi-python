
# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here.
#  If the generated information is not correct for python
#  changes can be made in attributes_addon.py and they will be
#  applied at build time.

attributes = {
    1050002: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:User Options:Range Check',
        'name': 'RANGE_CHECK',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to validate attribute values and function parameters.   If enabled, the instrument driver validates the parameter values that  you pass to driver functions.  Range checking  parameters is very useful for debugging.  After you validate your program,  you can set this attribute to VI_FALSE to disable range checking and  maximize performance.
The default value is VI_TRUE.   Use the niSwitch_InitWithOptions  function to override this value.
''',
},
    },
    1050003: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:User Options:Query Instrument Status',
        'name': 'QUERY_INSTRUMENT_STATUS',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the instrument driver queries the instrument status  after each operation.  Querying the instrument status is very useful for  debugging.  After you validate your program, you can set this attribute to  VI_FALSE to disable status checking and maximize performance
The instrument driver can choose to ignore status checking for  particular attributes regardless of the setting of this attribute.
The default value is VI_TRUE.   Use the niSwitch_InitWithOptions  function to override this value.
''',
},
    },
    1050004: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:User Options:Cache',
        'name': 'CACHE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to cache the value of attributes.  When caching is  enabled, the instrument driver keeps track of the current instrument  settings and avoids sending redundant commands to the instrument.
The instrument driver can choose always to cache or never to cache  particular attributes regardless of the setting of this attribute.
The default value is VI_TRUE.   Use the niSwitch_InitWithOptions  function to override this value.
''',
},
    },
    1050005: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:User Options:Simulate',
        'name': 'SIMULATE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether or not to simulate instrument driver I/O operations.  If  simulation is enabled, instrument driver functions perform range checking  and call Ivi_GetAttribute and Ivi_SetAttribute functions, but they do not  perform instrument I/O.  For output parameters that represent instrument  data, the instrument driver functions return calculated values.
The default value is VI_FALSE.   Use the niSwitch_InitWithOptions  function to override this value.
''',
},
    },
    1050006: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:User Options:Record Value Coercions',
        'name': 'RECORD_COERCIONS',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the IVI engine keeps a list of  the value coercions it makes for ViInt32 and ViReal64 attributes.   You call niSwitch_GetNextCoercionRecord to extract and delete the oldest  coercion record from the list.
The default value is VI_FALSE.   Use the  niSwitch_InitWithOptions function to override this value.
''',
},
    },
    1050007: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Driver Setup',
        'name': 'DRIVER_SETUP',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
This attribute indicates the Driver Setup string that the user  specified when initializing the driver.
Some cases exist where the end-user must specify instrument driver  options at initialization time.  An example of this is specifying  a particular instrument model from among a family of instruments  that the driver supports.  This is useful when using simulation.   The end-user can specify driver-specific options through  the DriverSetup keyword in the optionsString parameter to the  niSwitch_InitWithOptions function, or through the IVI Configuration Utility.
If the user does not specify a Driver Setup string, this attribute returns an empty string.
''',
},
    },
    1050021: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:User Options:Interchange Check',
        'name': 'INTERCHANGE_CHECK',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to perform interchangeability checking and retrieve  interchangeability warnings when you call  niSwitch_Connect, niSwitch_SetPath and niSwitch_InitiateScan functions.
The default value is VI_FALSE.
Interchangeability warnings indicate that using your application with a  different instrument might cause different behavior.   You call niSwitch_GetNextInterchangeWarning to extract interchange warnings.   Call the niSwitch_ClearInterchangeWarnings function to clear the list  of interchangeability warnings without reading them.
Interchangeability checking examines the attributes in a  capability group only if you specify a value for at least one  attribute within that group.  Interchangeability warnings can  occur when an attribute affects the behavior of the instrument and you  have not set that attribute, or the attribute has been invalidated since you set it.
''',
},
    },
    1050203: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Channel Count',
        'name': 'CHANNEL_COUNT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Indicates the number of channels that the specific instrument  driver supports.
''',
},
    },
    1050302: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Driver Prefix',
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
A string that contains the prefix for the instrument driver.  The name of each  user-callable function in this driver starts with this prefix.
''',
},
    },
    1050304: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:IO Resource Descriptor',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Indicates the resource descriptor the driver  uses to identify the physical device.
If you initialize the driver with a logical name, this  attribute contains the resource descriptor that corresponds  to the entry in the IVI Configuration utility.
If you initialize the instrument driver with the resource  descriptor, this attribute contains that value.
''',
},
    },
    1050305: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Logical Name',
        'name': 'LOGICAL_NAME',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
A string containing the logical name you specified when opening the  current IVI session.
You may pass a logical name to the niSwitch_init or  niSwitch_InitWithOptions functions.   The IVI Configuration utility must contain an entry for the logical name.   The logical name entry refers to a virtual instrument section in the  IVI Configuration file.  The virtual instrument section specifies a physical  device and initial user options.
''',
},
    },
    1050327: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Contains a comma-separated list of supported instrument models.
''',
},
    },
    1050401: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities',
        'name': 'GROUP_CAPABILITIES',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
A string that contains a comma-separated list of class-extention groups that  this driver implements.
''',
},
    },
    1050510: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Firmware Revision',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
A string that contains the firmware revision information  for the instrument you are currently using.
''',
},
    },
    1050511: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Manufacturer',
        'name': 'INSTRUMENT_MANUFACTURER',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
A string that contains the name of the instrument manufacturer you are currently  using.
''',
},
    },
    1050512: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Model',
        'name': 'INSTRUMENT_MODEL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
A string that contains the model number or name of the instrument that you  are currently using.
''',
},
    },
    1050513: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Driver Vendor',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
A string that contains the name of the vendor that supplies this driver.
''',
},
    },
    1050514: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Description',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
A string that contains a brief description of the specific  driver.
''',
},
    },
    1050515: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Class Specification Major Version',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
The major version number of the IviSwtch class specification.
''',
},
    },
    1050516: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Class Specification Minor Version',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
The minor version number of the class specification with which this driver is compliant.
''',
},
    },
    1050551: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Revision',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
A string that contains additional version information about this  instrument driver.
''',
},
    },
    1150001: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Obsolete Attributes:Serial Number',
        'name': 'SERIAL_NUMBER_I32',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'This attribute has been deprecated and may be removed from a future release of  NI-SWITCH.  Use the NISWITCH_ATTR_SERIAL_NUMBER (string flavor) instead.',
},
    },
    1150002: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Scanning Configuration:Continuous Scan',
        'name': 'CONTINUOUS_SCAN',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
When a switch device is scanning, the swich can either stop scanning when  the end of the scan (VI_FALSE) or continue scanning from the top of the  scan list again (VI_TRUE).
Notice that if you set the scan to continuous (VI_TRUE), the Wait For Scan  Complete operation will always time out and you must call Abort to stop  the scan.
''',
},
    },
    1150004: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Scanning Configuration:Is Waiting for Trigger?',
        'name': 'IS_WAITING_FOR_TRIG',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': 'In a scan list, a semi-colon (;) is used to indicate that at that point in  the scan list, the scan engine should pause until a trigger is received  from the trigger input.  If that trigger is user generated through either  a hardware pulse or the Send SW Trigger operation, it is necessary for the  user to know  when the scan engine has reached such a state.',
},
    },
    1150005: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Obsolete Attributes:Trigger Mode',
        'name': 'TRIGGER_MODE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
This attribute has been deprecated and may be removed from a future release of  NI-SWITCH.  Use the niSwitch_RouteTriggerInput and/or niSwitch_RouteScanAdvancedOutput  functions instead.
''',
},
    },
    1150006: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Obsolete Attributes:Master Slave Trigger Bus',
        'name': 'MASTER_SLAVE_TRIGGER_BUS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
This attribute has been deprecated and may be removed from a future release of  NI-SWITCH.  Use the niSwitch_RouteTriggerInput function instead.
''',
},
    },
    1150007: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Obsolete Attributes:Master Slave Scan Advanced Bus',
        'name': 'MASTER_SLAVE_SCAN_ADVANCED_BUS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
This attribute has been deprecated and may be removed from a future release of  NI-SWITCH.  Use the niSwitch_RouteScanAdvancedOutput function instead.
''',
},
    },
    1150008: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Obsolete Attributes:Cabled Module Trigger Bus',
        'name': 'CABLED_MODULE_TRIGGER_BUS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
This attribute has been deprecated and may be removed from a future release of  NI-SWITCH.  Use the niSwitch_RouteTriggerInput function instead.
''',
},
    },
    1150009: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Obsolete Attributes:Cabled Module Scan Advanced Bus',
        'name': 'CABLED_MODULE_SCAN_ADVANCED_BUS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
This attribute has been deprecated and may be removed from a future release of  NI-SWITCH.  Use the niSwitch_RouteScanAdvancedOutput function instead.
''',
},
    },
    1150010: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TriggerInputPolarity',
        'lv_property': 'Scanning Configuration:Trigger Input Polarity',
        'name': 'TRIGGER_INPUT_POLARITY',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Determines the behavior of the trigger Input.',
},
    },
    1150011: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'ScanAdvancedPolarity',
        'lv_property': 'Scanning Configuration:Scan Advanced Polarity',
        'name': 'SCAN_ADVANCED_POLARITY',
        'resettable': 'No',
        'type': 'ViInt32',

    },
    1150012: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Obsolete Attributes:Parsed Scan List',
        'name': 'PARSED_SCAN_LIST',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
This attribute has been deprecated and may be removed from a future release of  NI-SWITCH.
''',
},
    },
    1150013: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'HandshakingInitiation',
        'lv_property': 'Scanning Configuration:Handshaking Initiation',
        'name': 'HANDSHAKING_INITIATION',
        'resettable': 'No',
        'type': 'ViInt32',

    },
    1150014: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Module Characteristics:Number of Relays',
        'name': 'NUMBER_OF_RELAYS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'This attribute returns the number of relays.',
},
    },
    1150015: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Module Characteristics:Serial Number',
        'name': 'SERIAL_NUMBER',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': 'This read-only attribute returns the serial number for the switch device  controlled by this instrument driver.  If the device does not return a  serial number, the driver returns the IVI_ERROR_ATTRIBUTE_NOT_SUPPORTED error.',
},
    },
    1150016: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Scanning Configuration:Digital Filter Enable',
        'name': 'DIGITAL_FILTER_ENABLE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
This property specifies whether to apply the pulse width filter to the  Trigger Input. Enabling the Digital Filter (VI_TRUE) prevents the switch  module from being triggered by pulses that are less than 150 ns on PXI  trigger lines 0–7.
When Digital Filter is disabled (VI_FALSE), it is possible for the switch  module to be triggered by noise on the PXI trigger lines. If the device  triggering the switch is capable of sending pulses greater than 150 ns, you should not disable the Digital Filter.
''',
},
    },
    1150017: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Module Characteristics:Power Down Latching Relays After Debounce',
        'name': 'POWER_DOWN_LATCHING_RELAYS_AFTER_DEBOUNCE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
This property specifies whether to power down latching relays after  calling Wait For Debounce.
When Power Down Latching Relays After Debounce is enabled (VI_TRUE),  a call to Wait For Debounce ensures that the relays are settled  and the latching relays are powered down.
''',
},
    },
    1150018: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Channel Configuration:Analog Bus Sharing Enable',
        'name': 'ANALOG_BUS_SHARING_ENABLE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables or disables sharing of an analog bus line so that multiple  NI SwitchBlock devices may connect to it simultaneously. To enable  multiple NI SwitchBlock devices to share an analog bus line, set this  attribute to VI_TRUE for each device on the channel that corresponds  with the shared analog bus line. The default value for all devices is  VI_FALSE, which disables sharing of the analog bus.
Refer to the Using the Analog Bus on an NI SwitchBlock Carrier topic  in the NI Switches Help for more information about sharing the analog bus.
''',
},
    },
    1150019: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Module Characteristics:Temperature',
        'name': 'TEMPERATURE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
This attribute returns the temperature as read by the Switch module.     The units are degrees Celsius.
''',
},
    },
    1250001: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Channel Configuration:Is Source Channel',
        'name': 'IS_SOURCE_CHANNEL',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': 'This channel-based attribute specifies whether you want to identify the  channel as a source channel.  Typically, you set this attribute to VI_TRUE  when you attach the channel to a power supply, a function generator, or an  active measurement point on the unit under test, and you do not want to  connect the channel to another source.  The driver prevents source  channels from connecting to each other.  The niSwitch_Connect function  returns the NISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES when you attempt to  connect two channels that you identify as source channels.',
},
    },
    1250002: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Module Characteristics:Is Debounced',
        'name': 'IS_DEBOUNCED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
This attribute indicates whether the entire switch device has settled  since the last switching command.  A value of VI_TRUE indicates that all  signals going through the switch device are valid.
''',
},
    },
    1250003: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Channel Configuration:Is Configuration Channel',
        'name': 'IS_CONFIGURATION_CHANNEL',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
This channel-based attribute specifies whether to reserve the channel for  internal path creation.  A channel that is available for internal path  creation is called a configuration channel.  The driver may use  configuration channels to create paths between two channels you specify in  the niSwitch_Connect function.  Configuration channels are not available  for external connections.
Set this attribute to VI_TRUE to mark the channel as a configuration  channel.  Set this attribute to VI_FALSE to mark the channel as available  for external connections.
After you identify a channel as a configuration channel, you cannot  use that channel for external connections.  The niSwitch_Connect function  returns the NISWITCH_ERROR_IS_CONFIGURATION_CHANNEL error when you attempt  to establish a connection between a configuration channel and any other  channel.
''',
},
    },
    1250004: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Module Characteristics:Settling Time',
        'name': 'SETTLING_TIME',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
This channel-based attribute returns the maximum length of time from after  you make a connection until the signal flowing through the channel  settles. The units are seconds.
the greater value of the settling time and the value you specify as the  scan delay.
''',
'note': 'NI PXI-2501/2503/2565/2590/2591 Users--the actual delay will always be',
},
    },
    1250005: {
        'access': 'read only',
        'channel_based': 'True',
        'lv_property': 'Module Characteristics:Bandwidth',
        'name': 'BANDWIDTH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
This channel-based attribute returns the bandwidth for the channel.
The units are hertz.
''',
},
    },
    1250006: {
        'access': 'read only',
        'channel_based': 'True',
        'lv_property': 'Module Characteristics:Maximum DC Voltage',
        'name': 'MAX_DC_VOLTAGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
This channel-based attribute returns the maximum DC voltage the channel  can switch.
The units are volts.
''',
},
    },
    1250007: {
        'access': 'read only',
        'channel_based': 'True',
        'lv_property': 'Module Characteristics:Maximum AC Voltage',
        'name': 'MAX_AC_VOLTAGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
This channel-based attribute returns the maximum AC voltage the channel  can switch.
The units are volts RMS.
''',
},
    },
    1250008: {
        'access': 'read only',
        'channel_based': 'True',
        'lv_property': 'Module Characteristics:Maximum Switching DC Current',
        'name': 'MAX_SWITCHING_DC_CURRENT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
This channel-based attribute returns the maximum DC current the channel  can switch.
The units are amperes.
''',
},
    },
    1250009: {
        'access': 'read only',
        'channel_based': 'True',
        'lv_property': 'Module Characteristics:Maximum Switching AC Current',
        'name': 'MAX_SWITCHING_AC_CURRENT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
This channel-based attribute returns the maximum AC current the channel  can switch.
The units are amperes RMS.
''',
},
    },
    1250010: {
        'access': 'read only',
        'channel_based': 'True',
        'lv_property': 'Module Characteristics:Maximum Carry DC Current',
        'name': 'MAX_CARRY_DC_CURRENT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
This channel-based attribute returns the maximum DC current the channel  can carry.
The units are amperes.
''',
},
    },
    1250011: {
        'access': 'read only',
        'channel_based': 'True',
        'lv_property': 'Module Characteristics:Maximum Carry AC Current',
        'name': 'MAX_CARRY_AC_CURRENT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
This channel-based attribute returns the maximum AC current the channel  can carry.
The units are amperes RMS.
''',
},
    },
    1250012: {
        'access': 'read only',
        'channel_based': 'True',
        'lv_property': 'Module Characteristics:Maximum Switching DC Power',
        'name': 'MAX_SWITCHING_DC_POWER',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
This channel-based attribute returns the maximum DC power the channel can  switch.
The units are watts.
''',
},
    },
    1250013: {
        'access': 'read only',
        'channel_based': 'True',
        'lv_property': 'Module Characteristics:Maximum Switching AC Power',
        'name': 'MAX_SWITCHING_AC_POWER',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
This channel-based attribute returns the maximum AC power the channel can  switch.
The units are volt-amperes.
''',
},
    },
    1250014: {
        'access': 'read only',
        'channel_based': 'True',
        'lv_property': 'Module Characteristics:Maximum Carry DC Power',
        'name': 'MAX_CARRY_DC_POWER',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
This channel-based attribute returns the maximum DC power the channel can  carry.
The units are watts.
''',
},
    },
    1250015: {
        'access': 'read only',
        'channel_based': 'True',
        'lv_property': 'Module Characteristics:Maximum Carry AC Power',
        'name': 'MAX_CARRY_AC_POWER',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
This channel-based attribute returns the maximum AC power the channel can  carry.
The units are volt-amperes.
''',
},
    },
    1250016: {
        'access': 'read only',
        'channel_based': 'True',
        'lv_property': 'Module Characteristics:Characteristic Impedance',
        'name': 'CHARACTERISTIC_IMPEDANCE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
This channel-based attribute returns the characteristic impedance for the  channel.
The units are ohms.
''',
},
    },
    1250017: {
        'access': 'read only',
        'channel_based': 'True',
        'lv_property': 'Module Characteristics:Wire mode',
        'name': 'WIRE_MODE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
This attribute returns the wire mode of the switch device.
This attribute affects the values of the NISWITCH_ATTR_NUM_OF_ROWS and  NISWITCH_ATTR_NUM_OF_COLUMNS attributes.   The actual number of input and  output lines on the switch device is fixed, but the number of channels  depends on how many lines constitute each channel.
''',
},
    },
    1250018: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Matrix Configuration:Number of Rows',
        'name': 'NUM_OF_ROWS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
This attribute returns the number of channels on the row of a matrix or  scanner.  If the switch device is a scanner, this value is the number of  output channels.
The NISWITCH_ATTR_WIRE_MODE attribute affects the number of available  rows.  For example, if your device has 8 input lines and you use the  two-wire mode, then the number of columns you have available is 4.
''',
},
    },
    1250019: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Matrix Configuration:Number of Columns',
        'name': 'NUM_OF_COLUMNS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
This attribute returns the number of channels on the column of a matrix or  scanner.  If the switch device is a scanner, this value is the number of  input channels.
The NISWITCH_ATTR_WIRE_MODE attribute affects the number of available  columns.  For example, if your device has 8 input lines and you use the  four-wire mode, then the number of columns you have available is 2.
''',
},
    },
    1250020: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Scanning Configuration:Scan List',
        'name': 'SCAN_LIST',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
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
''',
},
    },
    1250021: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'ScanMode',
        'lv_property': 'Scanning Configuration:Scan Mode',
        'name': 'SCAN_MODE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
This attribute specifies what happens to existing connections that  conflict with the connections you make in a scan list.  For example, if  CH1 is already connected to CH2 and the scan list instructs the switch  device to connect CH1 to CH3, this attribute specifies what happens to the  connection between CH1 and CH2.
If the value of this attribute is NISWITCH_VAL_NONE, the switch device  takes no action on existing paths.  If the value is  NISWITCH_VAL_BREAK_BEFORE_MAKE, the switch device breaks conflicting paths  before making new ones.  If the value is NISWITCH_VAL_BREAK_AFTER_MAKE,  the switch device breaks conflicting paths after making new ones.
Most switch devices support only one of the possible values.  In such  cases, this attribute serves as an indicator of the device's behavior.
''',
},
    },
    1250022: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TriggerInput',
        'lv_property': 'Scanning Configuration:Trigger Input',
        'name': 'TRIGGER_INPUT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
This attribute specifies the source of the trigger for which the switch  device can wait when processing a scan list.  The switch device waits for  a trigger when it encounters a semi-colon in a scan list.  When the trigger  occurs, the switch device advances to the next entry in the scan list.
''',
},
    },
    1250023: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'ScanAdvancedOutput',
        'lv_property': 'Scanning Configuration:Scan Advanced Output',
        'name': 'SCAN_ADVANCED_OUTPUT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
This attribute specifies the method you want to use to notify another  instrument that all signals going through the switch device have settled  following the processing of one entry in the scan list.
''',
},
    },
    1250024: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Scanning Configuration:Is Scanning',
        'name': 'IS_SCANNING',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': 'If VI_TRUE, the switch module is currently scanning through the scan list  (i.e. it is not in the Idle state). If VI_FALSE, the switch module is not  currently scanning through the scan list (i.e. it is in the Idle state).',
},
    },
    1250025: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Scanning Configuration:Scan Delay',
        'name': 'SCAN_DELAY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
This attribute specifies the minimum amount of time the switch device  waits before it asserts the scan advanced output trigger after opening or  closing the switch.  The switch device always waits for debounce before  asserting the trigger. The units are seconds.
the greater value of the settling time and the value you specify as the  scan delay.
''',
'note': 'NI PXI-2501/2503/2565/2590/2591 Users--the actual delay will always be',
},
    },
}
