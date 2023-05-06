# -*- coding: utf-8 -*-
# This file is generated from NI-SWITCH API metadata version 23.0.0f167
attributes = {
    1050005: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether or not to simulate instrument driver I/O operations.  If  simulation is enabled, instrument driver functions perform range checking  and call Ivi_GetAttribute and Ivi_SetAttribute functions, but they do not  perform instrument I/O.  For output parameters that represent instrument  data, the instrument driver functions return calculated values.\nThe default value is VI_FALSE.   Use the niSwitch_InitWithOptions  function to override this value.\n'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Simulate',
        'name': 'SIMULATE',
        'type': 'ViBoolean'
    },
    1050007: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis attribute indicates the Driver Setup string that the user  specified when initializing the driver.\nSome cases exist where the end-user must specify instrument driver  options at initialization time.  An example of this is specifying  a particular instrument model from among a family of instruments  that the driver supports.  This is useful when using simulation.   The end-user can specify driver-specific options through  the DriverSetup keyword in the optionsString parameter to the  niSwitch_InitWithOptions function, or through the IVI Configuration Utility.\nIf the user does not specify a Driver Setup string, this attribute returns an empty string.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Driver Setup',
        'name': 'DRIVER_SETUP',
        'type': 'ViString'
    },
    1050203: {
        'access': 'read only',
        'documentation': {
            'description': '\nIndicates the number of channels that the specific instrument  driver supports.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Channel Count',
        'name': 'CHANNEL_COUNT',
        'type': 'ViInt32'
    },
    1050304: {
        'access': 'read only',
        'documentation': {
            'description': '\nIndicates the resource descriptor the driver  uses to identify the physical device.\nIf you initialize the driver with a logical name, this  attribute contains the resource descriptor that corresponds  to the entry in the IVI Configuration utility.\nIf you initialize the instrument driver with the resource  descriptor, this attribute contains that value.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:IO Resource Descriptor',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'type': 'ViString'
    },
    1050305: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string containing the logical name you specified when opening the  current IVI session.\nYou may pass a logical name to the niSwitch_init or  niSwitch_InitWithOptions functions.   The IVI Configuration utility must contain an entry for the logical name.   The logical name entry refers to a virtual instrument section in the  IVI Configuration file.  The virtual instrument section specifies a physical  device and initial user options.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Logical Name',
        'name': 'LOGICAL_NAME',
        'type': 'ViString'
    },
    1050327: {
        'access': 'read only',
        'documentation': {
            'description': '\nContains a comma-separated list of supported instrument models.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'type': 'ViString'
    },
    1050510: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains the firmware revision information  for the instrument you are currently using.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Firmware Revision',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'type': 'ViString'
    },
    1050511: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains the name of the instrument manufacturer you are currently  using.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Manufacturer',
        'name': 'INSTRUMENT_MANUFACTURER',
        'type': 'ViString'
    },
    1050512: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains the model number or name of the instrument that you  are currently using.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Model',
        'name': 'INSTRUMENT_MODEL',
        'type': 'ViString'
    },
    1050513: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains the name of the vendor that supplies this driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Driver Vendor',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'type': 'ViString'
    },
    1050514: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains a brief description of the specific  driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Description',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'type': 'ViString'
    },
    1050551: {
        'access': 'read only',
        'documentation': {
            'description': '\nA string that contains additional version information about this  instrument driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Revision',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'type': 'ViString'
    },
    1150004: {
        'access': 'read only',
        'documentation': {
            'description': 'In a scan list, a semi-colon (;) is used to indicate that at that point in  the scan list, the scan engine should pause until a trigger is received  from the trigger input.  If that trigger is user generated through either  a hardware pulse or the Send SW Trigger operation, it is necessary for the  user to know  when the scan engine has reached such a state.'
        },
        'lv_property': 'Scanning Configuration:Is Waiting for Trigger?',
        'name': 'IS_WAITING_FOR_TRIG',
        'type': 'ViBoolean'
    },
    1150010: {
        'access': 'read-write',
        'documentation': {
            'description': 'Determines the behavior of the trigger Input.'
        },
        'enum': 'TriggerInputPolarity',
        'lv_property': 'Scanning Configuration:Trigger Input Polarity',
        'name': 'TRIGGER_INPUT_POLARITY',
        'type': 'ViInt32'
    },
    1150011: {
        'access': 'read-write',
        'enum': 'ScanAdvancedPolarity',
        'lv_property': 'Scanning Configuration:Scan Advanced Polarity',
        'name': 'SCAN_ADVANCED_POLARITY',
        'type': 'ViInt32'
    },
    1150013: {
        'access': 'read-write',
        'enum': 'HandshakingInitiation',
        'lv_property': 'Scanning Configuration:Handshaking Initiation',
        'name': 'HANDSHAKING_INITIATION',
        'type': 'ViInt32'
    },
    1150014: {
        'access': 'read only',
        'documentation': {
            'description': 'This attribute returns the number of relays.'
        },
        'lv_property': 'Module Characteristics:Number of Relays',
        'name': 'NUMBER_OF_RELAYS',
        'type': 'ViInt32'
    },
    1150015: {
        'access': 'read only',
        'documentation': {
            'description': 'This read-only attribute returns the serial number for the switch device  controlled by this instrument driver.  If the device does not return a  serial number, the driver returns the IVI_ERROR_ATTRIBUTE_NOT_SUPPORTED error.'
        },
        'lv_property': 'Module Characteristics:Serial Number',
        'name': 'SERIAL_NUMBER',
        'type': 'ViString'
    },
    1150016: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThis property specifies whether to apply the pulse width filter to the  Trigger Input. Enabling the Digital Filter (VI_TRUE) prevents the switch  module from being triggered by pulses that are less than 150 ns on PXI  trigger lines 0–7.\nWhen Digital Filter is disabled (VI_FALSE), it is possible for the switch  module to be triggered by noise on the PXI trigger lines. If the device  triggering the switch is capable of sending pulses greater than 150 ns, you should not disable the Digital Filter.\n'
        },
        'lv_property': 'Scanning Configuration:Digital Filter Enable',
        'name': 'DIGITAL_FILTER_ENABLE',
        'type': 'ViBoolean'
    },
    1150017: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThis property specifies whether to power down latching relays after  calling Wait For Debounce.\nWhen Power Down Latching Relays After Debounce is enabled (VI_TRUE),  a call to Wait For Debounce ensures that the relays are settled  and the latching relays are powered down.\n'
        },
        'lv_property': 'Module Characteristics:Power Down Latching Relays After Debounce',
        'name': 'POWER_DOWN_LATCHING_RELAYS_AFTER_DEBOUNCE',
        'type': 'ViBoolean'
    },
    1150018: {
        'access': 'read-write',
        'documentation': {
            'description': '\nEnables or disables sharing of an analog bus line so that multiple  NI SwitchBlock devices may connect to it simultaneously. To enable  multiple NI SwitchBlock devices to share an analog bus line, set this  attribute to VI_TRUE for each device on the channel that corresponds  with the shared analog bus line. The default value for all devices is  VI_FALSE, which disables sharing of the analog bus.\nRefer to the Using the Analog Bus on an NI SwitchBlock Carrier topic  in the NI Switches Help for more information about sharing the analog bus.\n'
        },
        'lv_property': 'Channel Configuration:Analog Bus Sharing Enable',
        'name': 'ANALOG_BUS_SHARING_ENABLE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1150019: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis attribute returns the temperature as read by the Switch module.     The units are degrees Celsius.\n'
        },
        'lv_property': 'Module Characteristics:Temperature',
        'name': 'TEMPERATURE',
        'type': 'ViReal64'
    },
    1250001: {
        'access': 'read-write',
        'documentation': {
            'description': 'This channel-based attribute specifies whether you want to identify the  channel as a source channel.  Typically, you set this attribute to VI_TRUE  when you attach the channel to a power supply, a function generator, or an  active measurement point on the unit under test, and you do not want to  connect the channel to another source.  The driver prevents source  channels from connecting to each other.  The niSwitch_Connect function  returns the NISWITCH_ERROR_ATTEMPT_TO_CONNECT_SOURCES when you attempt to  connect two channels that you identify as source channels.'
        },
        'lv_property': 'Channel Configuration:Is Source Channel',
        'name': 'IS_SOURCE_CHANNEL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1250002: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis attribute indicates whether the entire switch device has settled  since the last switching command.  A value of VI_TRUE indicates that all  signals going through the switch device are valid.\n'
        },
        'lv_property': 'Module Characteristics:Is Debounced',
        'name': 'IS_DEBOUNCED',
        'type': 'ViBoolean'
    },
    1250003: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThis channel-based attribute specifies whether to reserve the channel for  internal path creation.  A channel that is available for internal path  creation is called a configuration channel.  The driver may use  configuration channels to create paths between two channels you specify in  the niSwitch_Connect function.  Configuration channels are not available  for external connections.\nSet this attribute to VI_TRUE to mark the channel as a configuration  channel.  Set this attribute to VI_FALSE to mark the channel as available  for external connections.\nAfter you identify a channel as a configuration channel, you cannot  use that channel for external connections.  The niSwitch_Connect function  returns the NISWITCH_ERROR_IS_CONFIGURATION_CHANNEL error when you attempt  to establish a connection between a configuration channel and any other  channel.\n'
        },
        'lv_property': 'Channel Configuration:Is Configuration Channel',
        'name': 'IS_CONFIGURATION_CHANNEL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1250004: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum length of time from after  you make a connection until the signal flowing through the channel  settles. The units are seconds.\nthe greater value of the settling time and the value you specify as the  scan delay.\n',
            'note': 'NI PXI-2501/2503/2565/2590/2591 Users--the actual delay will always be'
        },
        'lv_property': 'Module Characteristics:Settling Time',
        'name': 'SETTLING_TIME',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1250005: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the bandwidth for the channel.\nThe units are hertz.\n'
        },
        'lv_property': 'Module Characteristics:Bandwidth',
        'name': 'BANDWIDTH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250006: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum DC voltage the channel  can switch.\nThe units are volts.\n'
        },
        'lv_property': 'Module Characteristics:Maximum DC Voltage',
        'name': 'MAX_DC_VOLTAGE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250007: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum AC voltage the channel  can switch.\nThe units are volts RMS.\n'
        },
        'lv_property': 'Module Characteristics:Maximum AC Voltage',
        'name': 'MAX_AC_VOLTAGE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250008: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum DC current the channel  can switch.\nThe units are amperes.\n'
        },
        'lv_property': 'Module Characteristics:Maximum Switching DC Current',
        'name': 'MAX_SWITCHING_DC_CURRENT',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250009: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum AC current the channel  can switch.\nThe units are amperes RMS.\n'
        },
        'lv_property': 'Module Characteristics:Maximum Switching AC Current',
        'name': 'MAX_SWITCHING_AC_CURRENT',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250010: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum DC current the channel  can carry.\nThe units are amperes.\n'
        },
        'lv_property': 'Module Characteristics:Maximum Carry DC Current',
        'name': 'MAX_CARRY_DC_CURRENT',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250011: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum AC current the channel  can carry.\nThe units are amperes RMS.\n'
        },
        'lv_property': 'Module Characteristics:Maximum Carry AC Current',
        'name': 'MAX_CARRY_AC_CURRENT',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250012: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum DC power the channel can  switch.\nThe units are watts.\n'
        },
        'lv_property': 'Module Characteristics:Maximum Switching DC Power',
        'name': 'MAX_SWITCHING_DC_POWER',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250013: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum AC power the channel can  switch.\nThe units are volt-amperes.\n'
        },
        'lv_property': 'Module Characteristics:Maximum Switching AC Power',
        'name': 'MAX_SWITCHING_AC_POWER',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250014: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum DC power the channel can  carry.\nThe units are watts.\n'
        },
        'lv_property': 'Module Characteristics:Maximum Carry DC Power',
        'name': 'MAX_CARRY_DC_POWER',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250015: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the maximum AC power the channel can  carry.\nThe units are volt-amperes.\n'
        },
        'lv_property': 'Module Characteristics:Maximum Carry AC Power',
        'name': 'MAX_CARRY_AC_POWER',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250016: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis channel-based attribute returns the characteristic impedance for the  channel.\nThe units are ohms.\n'
        },
        'lv_property': 'Module Characteristics:Characteristic Impedance',
        'name': 'CHARACTERISTIC_IMPEDANCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250017: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis attribute returns the wire mode of the switch device.\nThis attribute affects the values of the NISWITCH_ATTR_NUM_OF_ROWS and  NISWITCH_ATTR_NUM_OF_COLUMNS attributes.   The actual number of input and  output lines on the switch device is fixed, but the number of channels  depends on how many lines constitute each channel.\n'
        },
        'grpc_enum': 'WireMode',
        'lv_property': 'Module Characteristics:Wire mode',
        'name': 'WIRE_MODE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1250018: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis attribute returns the number of channels on the row of a matrix or  scanner.  If the switch device is a scanner, this value is the number of  output channels.\nThe NISWITCH_ATTR_WIRE_MODE attribute affects the number of available  rows.  For example, if your device has 8 input lines and you use the  two-wire mode, then the number of columns you have available is 4.\n'
        },
        'lv_property': 'Matrix Configuration:Number of Rows',
        'name': 'NUM_OF_ROWS',
        'type': 'ViInt32'
    },
    1250019: {
        'access': 'read only',
        'documentation': {
            'description': '\nThis attribute returns the number of channels on the column of a matrix or  scanner.  If the switch device is a scanner, this value is the number of  input channels.\nThe NISWITCH_ATTR_WIRE_MODE attribute affects the number of available  columns.  For example, if your device has 8 input lines and you use the  four-wire mode, then the number of columns you have available is 2.\n'
        },
        'lv_property': 'Matrix Configuration:Number of Columns',
        'name': 'NUM_OF_COLUMNS',
        'type': 'ViInt32'
    },
    1250020: {
        'access': 'read-write',
        'documentation': {
            'description': "\nThis attribute contains a scan list, which is a string that specifies  channel connections and trigger conditions.  The niSwitch_InitiateScan  function makes or breaks connections and waits for triggers according to  the instructions in the scan list.\nThe scan list is comprised of channel names that you separate with  special characters.  These special characters determine the operations the  scanner performs on the channels when it executes this scan list.\nTo create a path between two channels, use the following character between  the two channel names:\n-> (a dash followed by a '>' sign)\nExample:  'CH1->CH2' tells the switch to make a path from channel CH1 to channel  CH2.\nTo break or clear a path, use the following character as a prefix before  the path:\n~ (tilde)\nExample:  '~CH1->CH2' tells the switch to break the path from channel CH1 to  channel CH2.\nTo tell the switch device to wait for a trigger event, use the following  character as a separator between paths:\n; (semi-colon)\nExample:  'CH1->CH2;CH3->CH4' tells the switch to make the path from channel CH1  to channel CH2, wait for a trigger, and then make the path from CH3 to  CH4.\n"
        },
        'lv_property': 'Scanning Configuration:Scan List',
        'name': 'SCAN_LIST',
        'type': 'ViString'
    },
    1250021: {
        'access': 'read-write',
        'documentation': {
            'description': "\nThis attribute specifies what happens to existing connections that  conflict with the connections you make in a scan list.  For example, if  CH1 is already connected to CH2 and the scan list instructs the switch  device to connect CH1 to CH3, this attribute specifies what happens to the  connection between CH1 and CH2.\nIf the value of this attribute is NISWITCH_VAL_NONE, the switch device  takes no action on existing paths.  If the value is  NISWITCH_VAL_BREAK_BEFORE_MAKE, the switch device breaks conflicting paths  before making new ones.  If the value is NISWITCH_VAL_BREAK_AFTER_MAKE,  the switch device breaks conflicting paths after making new ones.\nMost switch devices support only one of the possible values.  In such  cases, this attribute serves as an indicator of the device's behavior.\n"
        },
        'enum': 'ScanMode',
        'lv_property': 'Scanning Configuration:Scan Mode',
        'name': 'SCAN_MODE',
        'type': 'ViInt32'
    },
    1250022: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThis attribute specifies the source of the trigger for which the switch  device can wait when processing a scan list.  The switch device waits for  a trigger when it encounters a semi-colon in a scan list.  When the trigger  occurs, the switch device advances to the next entry in the scan list.\n'
        },
        'enum': 'TriggerInput',
        'lv_property': 'Scanning Configuration:Trigger Input',
        'name': 'TRIGGER_INPUT',
        'type': 'ViInt32'
    },
    1250023: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThis attribute specifies the method you want to use to notify another  instrument that all signals going through the switch device have settled  following the processing of one entry in the scan list.\n'
        },
        'enum': 'ScanAdvancedOutput',
        'lv_property': 'Scanning Configuration:Scan Advanced Output',
        'name': 'SCAN_ADVANCED_OUTPUT',
        'type': 'ViInt32'
    },
    1250024: {
        'access': 'read only',
        'documentation': {
            'description': 'If VI_TRUE, the switch module is currently scanning through the scan list  (i.e. it is not in the Idle state). If VI_FALSE, the switch module is not  currently scanning through the scan list (i.e. it is in the Idle state).'
        },
        'lv_property': 'Scanning Configuration:Is Scanning',
        'name': 'IS_SCANNING',
        'type': 'ViBoolean'
    },
    1250025: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nThis attribute specifies the minimum amount of time the switch device  waits before it asserts the scan advanced output trigger after opening or  closing the switch.  The switch device always waits for debounce before  asserting the trigger. The units are seconds.\nthe greater value of the settling time and the value you specify as the  scan delay.\n',
            'note': 'NI PXI-2501/2503/2565/2590/2591 Users--the actual delay will always be'
        },
        'lv_property': 'Scanning Configuration:Scan Delay',
        'name': 'SCAN_DELAY',
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1250026: {
        'access': 'read-write',
        'documentation': {
            'description': '\nWhen a switch device is scanning, the swich can either stop scanning when  the end of the scan (VI_FALSE) or continue scanning from the top of the  scan list again (VI_TRUE).\nNotice that if you set the scan to continuous (VI_TRUE), the Wait For Scan  Complete operation will always time out and you must call Abort to stop  the scan.\n'
        },
        'lv_property': 'Scanning Configuration:Continuous Scan',
        'name': 'CONTINUOUS_SCAN',
        'type': 'ViBoolean'
    }
}
