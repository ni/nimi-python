
# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here.
#  If the generated information is not correct for python
#  changes can be made in attributes_addon.py and they will be
#  applied at build time.

attributes = {
    1050002: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'tBoolean',
        'lv_property': 'Inherent IVI Attributes:User Options:Range Check',
        'name': 'RANGE_CHECK',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to validate attribute values and function parameters.
If this attribute is enabled, NI-DCPower validates the parameter values that you pass to NI-DCPower functions.  Range checking parameters is useful for debugging. After you validate your program, you can set this  attribute to VI_FALSE to disable range checking and maximize performance.
Use the niDCPower_InitializeWithChannels function to override this value.
Default Value: VI_TRUE
''',
},
    },
    1050003: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'tBoolean',
        'lv_property': 'Inherent IVI Attributes:User Options:Query Instrument Status',
        'name': 'QUERY_INSTRUMENT_STATUS',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether NI-DCPower queries the device status after each operation.
Querying the device status is useful for debugging. After you validate your program, you can set this  attribute to VI_FALSE to disable status checking and maximize performance.
NI-DCPower ignores status checking for particular attributes regardless of the setting of this attribute.
Use the niDCPower_InitializeWithChannels function to override this value.
Default Value: VI_TRUE
''',
},
    },
    1050004: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'tBoolean',
        'lv_property': 'Inherent IVI Attributes:User Options:Cache',
        'name': 'CACHE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to cache the value of attributes.
When caching is enabled, NI-DCPower records the current power supply settings and avoids sending  redundant commands to the device. Enabling caching can significantly increase execution speed.
NI-DCPower might always cache or never cache particular attributes regardless of the setting of this attribute.
Use the niDCPower_InitializeWithChannels function to override this value.
Default Value: VI_TRUE
''',
},
    },
    1050005: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'tBoolean',
        'lv_property': 'Inherent IVI Attributes:User Options:Simulate',
        'name': 'SIMULATE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to simulate NI-DCPower I/O operations. VI_TRUE specifies that operation is simulated.
Default Value: VI_FALSE
''',
},
    },
    1050006: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'tBoolean',
        'lv_property': 'Inherent IVI Attributes:User Options:Record Value Coercions',
        'name': 'RECORD_COERCIONS',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the IVI engine records the value coercions it makes for ViInt32 and ViReal64 attributes.  Call the niDCPower_GetNextCoercionRecord function to read and delete the earliest coercion record from the list.
Default Value: The default value is VI_FALSE. Use the niDCPower_InitializeWithChannels function to override this value.
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
Indicates the Driver Setup string that you specified when initializing the driver.
Some cases exist where you must specify the instrument driver options at initialization  time. An example of this case is specifying a particular device model from among a family  of devices that the driver supports. This attribute is useful when simulating a device.  You can specify the driver-specific options through the DriverSetup keyword in the optionsString  parameter in the niDCPower_InitializeWithChannels function or through the  IVI Configuration Utility.
You can specify  driver-specific options through the DriverSetup keyword in the  optionsString parameter in the niDCPower_InitializeWithChannels function. If you do not specify a Driver Setup string, this attribute returns an empty string.
''',
},
    },
    1050021: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'tBoolean',
        'lv_property': 'Inherent IVI Attributes:User Options:Interchange Check',
        'name': 'INTERCHANGE_CHECK',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to perform interchangeability checking and log interchangeability warnings when you  call NI-DCPower functions. VI_TRUE specifies that interchangeability checking is enabled.
Interchangeability warnings indicate that using your application with a different power supply might  cause different behavior. Call the niDCPower_GetNextInterchangeWarning function to retrieve  interchange warnings.
Call the niDCPower_GetNextInterchangeWarning function to clear the list of interchangeability warnings  without reading them.
Interchangeability checking examines the attributes in a capability group only if you specify a value  for at least one attribute within that group. Interchangeability warnings can occur when an attribute  affects the behavior of the device and you have not set that attribute or when the attribute has been  invalidated since you set it.
Default Value: VI_FALSE
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
'description': 'Indicates the number of channels that NI-DCPower supports for the instrument that was chosen when  the current session was opened. For channel-based attributes, the IVI engine maintains a separate  cache value for each channel.',
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
'description': 'Contains the prefix for NI-DCPower. The name of each user-callable  function in NI-DCPower begins with this prefix.',
},
    },
    1050304: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Resource Descriptor',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Indicates the resource descriptor NI-DCPower uses to identify the physical device.
If you initialize NI-DCPower with a logical name, this attribute contains the resource descriptor  that corresponds to the entry in the IVI Configuration utility.
If you initialize NI-DCPower with the resource descriptor, this attribute contains that value.
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
Contains the logical name you specified when opening the current IVI session.
You can pass a logical name to the niDCPower_InitializeWithChannels function.  The IVI Configuration utility must contain an entry for the logical name. The logical name entry  refers to a function section in the IVI Configuration file. The function section specifies a physical  device and initial user options.
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
'description': 'Contains a comma-separated (,) list of supported NI-DCPower device models.',
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
'description': 'Contains a comma-separated list of class-extension groups that NI-DCPower implements.',
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
'description': 'Contains the firmware revision information for the device you are currently using.',
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
'description': 'Contains the name of the manufacturer for the device you are currently using.',
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
'description': 'Contains the model number or name of the device that you are currently using.',
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
'description': 'Contains the name of the vendor that supplies NI-DCPower.',
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
'description': 'Contains a brief description of the specific driver.',
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
'description': 'Contains the major version number of the class specification with which NI-DCPower is compliant.',
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
'description': 'Contains the minor version number of the class specification with which NI-DCPower is compliant.',
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
'description': 'Contains additional version information about NI-DCPower.',
},
    },
    1150000: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'PowerSource',
        'lv_property': 'Advanced:Power Source',
        'name': 'POWER_SOURCE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the power source to use. NI-DCPower switches the power source used by the  device to the specified value.
Default Value: NIDCPOWER_VAL_AUTOMATIC
is set to NIDCPOWER_VAL_AUTOMATIC. However, if the session is in the Committed or Uncommitted state  when you set this attribute, the power source selection only occurs after you call the  niDCPower_Initiate function.
''',
'note': 'Automatic selection is not persistent and occurs only at the time this attribute',
},
    },
    1150001: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': 'PowerSourceInUse',
        'lv_property': 'Advanced:Power Source In Use',
        'name': 'POWER_SOURCE_IN_USE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Indicates whether the device is using the internal or auxiliary power source to generate power.',
},
    },
    1150002: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': 'tBoolean',
        'lv_property': 'Advanced:Auxiliary Power Source Available',
        'name': 'AUXILIARY_POWER_SOURCE_AVAILABLE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Indicates whether an auxiliary power source is connected to the device.
A value of VI_FALSE may indicate that the auxiliary input fuse has blown.  Refer to the Detecting Internal/Auxiliary Power topic in the NI DC Power Supplies and SMUs Help for  more information about internal and auxiliary power.
power source to generate power. Use the NIDCPOWER_ATTR_POWER_SOURCE_IN_USE attribute to retrieve this information.
''',
'note': 'This attribute does not necessarily indicate if the device is using the auxiliary',
},
    },
    1150003: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Measurement:Samples To Average',
        'name': 'SAMPLES_TO_AVERAGE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of samples to average when you take a measurement.
Increasing the number of samples to average decreases measurement noise but increases the time required to take  a measurement. Refer to the NI PXI-4110, NI PXI-4130, NI PXI-4132, or NI PXIe-4154 Averaging topic for  optional attribute settings to improve immunity to certain noise types, or refer to the NI PXIe-4140/4141  DC Noise Rejection, NI PXIe-4142/4143 DC Noise Rejection, or NI PXIe-4144/4145 DC Noise Rejection topic for  information about improving noise immunity for those devices.
Default Value:
NI PXI-4110 or NI PXI-4130—10
NI PXI-4132—1
NI PXIe-4112—1
NI PXIe-4113—1
NI PXIe-4140/4141—1
NI PXIe-4142/4143—1
NI PXIe-4144/4145—1
NI PXIe-4154—500
''',
},
    },
    1150004: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:DC Voltage:Current Limit Range',
        'name': 'CURRENT_LIMIT_RANGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the current limit range, in amps, for the specified channel(s).
The range defines the valid value to which the current limit can be set. Use the NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE  attribute to enable automatic selection of the current limit range.
The NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute  is set to NIDCPOWER_VAL_DC_VOLTAGE.
NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.
For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.
''',
'note': 'The channel must be enabled for the specified current limit to take effect. Refer to the',
},
    },
    1150005: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:DC Voltage:Voltage Level Range',
        'name': 'VOLTAGE_LEVEL_RANGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the voltage level range, in volts, for the specified channel(s).
The range defines the valid values to which the voltage level can be set. Use the NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE  attribute to enable automatic selection of the voltage level range.
The NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is  set to NIDCPOWER_VAL_DC_VOLTAGE.
NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.
For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.
''',
'note': 'The channel must be enabled for the specified voltage level range to take effect. Refer to the',
},
    },
    1150006: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'tBoolean',
        'lv_property': 'Measurement:Advanced:Reset Average Before Measurement',
        'name': 'RESET_AVERAGE_BEFORE_MEASUREMENT',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the measurement returned from any measurement call starts with a new measurement call (VI_TRUE) or  returns a measurement that has already begun or completed(VI_FALSE).
for information about supported devices.
When you set the NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE attribute in the Running state, the output channel measurements might  move out of synchronization. While NI-DCPower automatically synchronizes measurements upon the initialization of a  session, you can force a synchronization in the running state before you run the niDCPower_MeasureMultiple function. To  force a synchronization in the running state, set this attribute to VI_TRUE, and then run the niDCPower_MeasureMultiple  function, specifying all channels in the channel name parameter. You can set the  NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT attribute to VI_FALSE after the niDCPower_MeasureMultiple function  completes.
Default Value: VI_TRUE
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150007: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'tBoolean',
        'lv_property': 'Source:Advanced:Overranging Enabled',
        'name': 'OVERRANGING_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether NI-DCPower allows setting the voltage level, current level, voltage limit and current limit outside the  device specification limits. VI_TRUE means that overranging is enabled.
Refer to the Ranges topic in the NI DC Power Supplies and SMUs Help for more information about overranging.
Default Value: VI_FALSE
''',
},
    },
    1150008: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'OutputFunction',
        'lv_property': 'Source:Output Function',
        'name': 'OUTPUT_FUNCTION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Configures the function to generate on the specified channel(s).
When NIDCPOWER_VAL_DC_VOLTAGE is selected, the device generates the desired voltage level on the output as long as the  output current is below the current limit. You can use the following attributes to configure the channel when  NIDCPOWER_VAL_DC_VOLTAGE is selected:
NIDCPOWER_ATTR_VOLTAGE_LEVEL
NIDCPOWER_ATTR_CURRENT_LIMIT
NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH
NIDCPOWER_ATTR_CURRENT_LIMIT_LOW
NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE
NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE
When NIDCPOWER_VAL_DC_CURRENT is selected, the device generates the desired current level on the output as long as the  output voltage is below the voltage limit. You can use the following attributes to configure the channel when  NIDCPOWER_VAL_DC_CURRENT is selected:
NIDCPOWER_ATTR_CURRENT_LEVEL
NIDCPOWER_ATTR_VOLTAGE_LIMIT
NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH
NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW
NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE
NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE
Default Value: NIDCPOWER_VAL_DC_VOLTAGE
''',
},
    },
    1150009: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:DC Current:Current Level',
        'name': 'CURRENT_LEVEL',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the current level, in amps, that the device attempts to generate on the specified channel(s).
This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_CURRENT.
NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.
Valid Values: The valid values for this attribute are defined by the values to which the  NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE attribute is set.
''',
'note': 'The channel must be enabled for the specified current level to take effect. Refer to the',
},
    },
    1150010: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:DC Current:Voltage Limit',
        'name': 'VOLTAGE_LIMIT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the voltage limit, in volts, that the output cannot exceed when generating the desired current level  on the specified channels.
This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_CURRENT  and the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY attribute is set to NIDCPOWER_VAL_SYMMETRIC.
NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.
Valid Values: The valid values for this attribute are defined by the values to which the  NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE attribute is set.
''',
'note': 'The channel must be enabled for the specified current level to take effect. Refer to the',
},
    },
    1150011: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:DC Current:Current Level Range',
        'name': 'CURRENT_LEVEL_RANGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the current level range, in amps, for the specified channel(s).
The range defines the valid value to which the current level can be set. Use the  NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE attribute to enable automatic selection of the current level range.
The NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is  set to NIDCPOWER_VAL_DC_CURRENT.
NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.
For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.
''',
'note': 'The channel must be enabled for the specified current level range to take effect. Refer to the',
},
    },
    1150012: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:DC Current:Voltage Limit Range',
        'name': 'VOLTAGE_LIMIT_RANGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the voltage limit range, in volts, for the specified channel(s).
The range defines the valid values to which the voltage limit can be set. Use the NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE  attribute to enable automatic selection of the voltage limit range.
The NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is  set to NIDCPOWER_VAL_DC_CURRENT.
NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.
For valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.
''',
'note': 'The channel must be enabled for the specified voltage limit range to take effect. Refer to the',
},
    },
    1150013: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'Sense',
        'lv_property': 'Measurement:Sense',
        'name': 'SENSE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Selects either local or remote sensing of the output voltage for the specified channel(s).
Refer to the Local and Remote Sense topic in the NI DC Power Supplies and SMUs Help for more  information about sensing voltage on supported channels and about devices that support local and/or remote sensing.
Default Value: The default value is NIDCPOWER_VAL_LOCAL if the device supports local sense.  Otherwise, the default and only supported value is NIDCPOWER_VAL_REMOTE.
''',
},
    },
    1150014: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'OutputCapacitance',
        'lv_property': 'Source:Advanced:Output Capacitance',
        'name': 'OUTPUT_CAPACITANCE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether to use a low or high capacitance on the output for the specified channel(s).
for information about supported devices.
Refer to the NI PXI-4130 Output Capacitance Selection topic in the NI DC Power Supplies and SMUs Help for more  information about capacitance.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150015: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'VoltageLevelAutorange',
        'lv_property': 'Source:DC Voltage:Voltage Level Autorange',
        'name': 'VOLTAGE_LEVEL_AUTORANGE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether NI-DCPower automatically selects the voltage level range based on the desired voltage level  for the specified channel(s).
If you set this attribute to NIDCPOWER_VAL_ON, NI-DCPower ignores any changes you make to the  NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE attribute. If you change the NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE attribute from  NIDCPOWER_VAL_ON to NIDCPOWER_VAL_OFF, NI-DCPower retains the last value the NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE  attribute was set to (or the default value if the attribute was never set) and uses that value as  the voltage level range.
Query the NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE attribute by using the niDCPower_GetAttributeViInt32 function for  information about which range NI-DCPower automatically selects.
The NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute  is set to NIDCPOWER_VAL_DC_VOLTAGE.
Default Value: NIDCPOWER_VAL_OFF
''',
},
    },
    1150016: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'CurrentLimitAutorange',
        'lv_property': 'Source:DC Voltage:Current Limit Autorange',
        'name': 'CURRENT_LIMIT_AUTORANGE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether NI-DCPower automatically selects the current limit range based on the desired current limit for the  specified channel(s).
If you set this attribute to NIDCPOWER_VAL_ON, NI-DCPower ignores any changes you make to the  NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE attribute. If you change this attribute from NIDCPOWER_VAL_ON to  NIDCPOWER_VAL_OFF, NI-DCPower retains the last value the NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE attribute was set to  (or the default value if the attribute was never set) and uses that value as the current limit range.
Query the NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE attribute by using the niDCPower_GetAttributeViInt32 function for  information about which range NI-DCPower automatically selects.
The NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute  is set to NIDCPOWER_VAL_DC_VOLTAGE.
Default Value: NIDCPOWER_VAL_OFF
''',
},
    },
    1150017: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'CurrentLevelAutorange',
        'lv_property': 'Source:DC Current:Current Level Autorange',
        'name': 'CURRENT_LEVEL_AUTORANGE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether NI-DCPower automatically selects the current level range based on the desired current level for  the specified channels.
If you set this attribute to NIDCPOWER_VAL_ON, NI-DCPower ignores any changes you make to the  NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE attribute. If you change the NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE attribute from  NIDCPOWER_VAL_ON to NIDCPOWER_VAL_OFF, NI-DCPower retains the last value the NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE  attribute was set to (or the default value if the attribute was never set) and uses that value as the  current level range.
Query the NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE attribute by using the niDCPower_GetAttributeViInt32 function for  information about which range NI-DCPower automatically selects.
The NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute  is set to NIDCPOWER_VAL_DC_CURRENT.
Default Value: NIDCPOWER_VAL_OFF
''',
},
    },
    1150018: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'VoltageLimitAutorange',
        'lv_property': 'Source:DC Current:Voltage Limit Autorange',
        'name': 'VOLTAGE_LIMIT_AUTORANGE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether NI-DCPower automatically selects the voltage limit range based on the desired voltage limit for  the specified channel(s).
If this attribute is set to NIDCPOWER_VAL_ON, NI-DCPower ignores any changes you make to the  NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE attribute. If you change the NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE attribute from  NIDCPOWER_VAL_ON to NIDCPOWER_VAL_OFF, NI-DCPower retains the last value the NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE  attribute was set to (or the default value if the attribute was never set) and uses that value as the voltage limit  range.
Query the NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE attribute by using the niDCPower_GetAttributeViInt32 function to find out  which range NI-DCPower automatically selects.
The NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute  is set to NIDCPOWER_VAL_DC_CURRENT.
Default Value: NIDCPOWER_VAL_OFF
''',
},
    },
    1150020: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'PowerLineFrequency',
        'lv_property': 'Measurement:Power Line Frequency',
        'name': 'POWER_LINE_FREQUENCY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the power line frequency for specified channel(s). NI-DCPower uses this value to select a timebase for setting the  NIDCPOWER_ATTR_APERTURE_TIME attribute in power line cycles (PLCs).
in the NI DC Power Supplies and SMUs Help for information about supported devices.
Default Value: NIDCPOWER_VAL_60_HERTZ
''',
'note': 'This attribute is not supported by all devices. Refer to the Supported Attributes by Device topic',
},
    },
    1150021: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TriggerType',
        'lv_property': 'Triggers:Start Trigger:Trigger Type',
        'name': 'START_TRIGGER_TYPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the behavior of the Start trigger.
for information about supported devices.
Default Value: NIDCPOWER_VAL_NONE
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150022: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'DigitalEdge',
        'lv_property': 'Triggers:Start Trigger:Digital Edge:Edge',
        'name': 'DIGITAL_EDGE_START_TRIGGER_EDGE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether to configure the Start trigger to assert on the rising or falling edge.
for information about supported devices.
Default Value: NIDCPOWER_VAL_RISING
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150023: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Triggers:Start Trigger:Digital Edge:Input Terminal',
        'name': 'DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the input terminal for the Start trigger. Use this attribute only when the NIDCPOWER_ATTR_START_TRIGGER_TYPE  attribute is set to NIDCPOWER_VAL_DIGITAL_EDGE.
for information about supported devices.
You can specify any valid input terminal for this attribute. Valid terminals are listed in Measurement & Automation  Explorer under the Device Routes tab.
Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can  specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name,  PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal  on Dev1 to be /Dev2/SourceCompleteEvent.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150024: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Triggers:Start Trigger:Export Output Terminal',
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Start trigger.
Refer to the Device Routes tab in Measurement & Automation Explorer (MAX) for a list of the terminals available  on your device.
Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name,  PXI_Trig0.
for information about supported devices.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150025: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Source:Advanced:Sequence Loop Count',
        'name': 'SEQUENCE_LOOP_COUNT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of times a sequence is run after initiation.
Refer to the Sequence Source Mode topic in the NI DC Power Supplies and SMUs Help for more information about the sequence  loop count.
for information about supported devices. When the NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE attribute  is set to VI_FALSE, the NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT attribute is ignored.
Valid Range: 1 to 134217727
Default Value: 1
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150026: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TriggerType',
        'lv_property': 'Triggers:Sequence Advance Trigger:Trigger Type',
        'name': 'SEQUENCE_ADVANCE_TRIGGER_TYPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the behavior of the Sequence Advance trigger.
for information about supported devices.
Default Value: NIDCPOWER_VAL_NONE
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150027: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'DigitalEdge',
        'lv_property': 'Triggers:Sequence Advance Trigger:Digital Edge:Edge',
        'name': 'DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_EDGE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether to configure the Sequence Advance trigger to assert on the rising or falling edge.
for information about supported devices.
Default Value: NIDCPOWER_VAL_RISING
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150028: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal',
        'name': 'DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the input terminal for the Sequence Advance trigger. Use this attribute only when the  NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE attribute is set to NIDCPOWER_VAL_DIGITAL_EDGE.
the NI DC Power Supplies and SMUs Help for information about supported devices.
You can specify any valid input terminal for this attribute. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can  specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the  input terminal on Dev1 to be /Dev2/SourceCompleteEvent.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic in',
},
    },
    1150029: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Triggers:Sequence Advance Trigger:Export Output Terminal',
        'name': 'EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Sequence Advance trigger.
Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals  available on your device.
for information about supported devices.
Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150030: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TriggerType',
        'lv_property': 'Triggers:Source Trigger:Trigger Type',
        'name': 'SOURCE_TRIGGER_TYPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the behavior of the Source trigger.
for information about supported devices.
Default Value: NIDCPOWER_VAL_NONE
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150031: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'DigitalEdge',
        'lv_property': 'Triggers:Source Trigger:Digital Edge:Edge',
        'name': 'DIGITAL_EDGE_SOURCE_TRIGGER_EDGE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether to configure the Source trigger to assert on the rising or falling edge.
for information about supported devices.
Default Value: NIDCPOWER_VAL_RISING
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150032: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Triggers:Source Trigger:Digital Edge:Input Terminal',
        'name': 'DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the input terminal for the Source trigger. Use this attribute only when the  NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE attribute is set to NIDCPOWER_VAL_DIGITAL_EDGE.
for information about supported devices.
You can specify any valid input terminal for this attribute. Valid terminals are listed  in Measurement & Automation Explorer under the Device Routes tab.
Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input  terminal on Dev1 to be /Dev2/SourceCompleteEvent.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150033: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Triggers:Source Trigger:Export Output Terminal',
        'name': 'EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Source trigger.
Refer to the Device Routes tab in MAX for a list of the terminals available on your device.
for information about supported devices.
Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150034: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TriggerType',
        'lv_property': 'Triggers:Measure Trigger:Trigger Type',
        'name': 'MEASURE_TRIGGER_TYPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the behavior of the Measure trigger.
for information about supported devices.
Default Value: NIDCPOWER_VAL_DIGITAL_EDGE
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150035: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'DigitalEdge',
        'lv_property': 'Triggers:Measure Trigger:Digital Edge:Edge',
        'name': 'DIGITAL_EDGE_MEASURE_TRIGGER_EDGE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether to configure the Measure trigger to assert on the rising or falling edge.
NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE attribute is set to NIDCPOWER_VAL_DIGITAL_EDGE.
for information about supported devices.
Default Value: NIDCPOWER_VAL_RISING
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150036: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Triggers:Measure Trigger:Digital Edge:Input Terminal',
        'name': 'DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the input terminal for the Measure trigger. This attribute is used only when the  NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE attribute is set to NIDCPOWER_VAL_DIGITAL_EDGE.
for this attribute.
You can specify any valid input terminal for this attribute. Valid terminals are listed in  Measurement & Automation Explorer under the Device Routes tab.
Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input  terminal on Dev1 to be /Dev2/SourceCompleteEvent.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150037: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Triggers:Measure Trigger:Export Output Terminal',
        'name': 'EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Measure trigger.
Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals  available on your device.
for information about supported devices.
Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150038: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'Polarity',
        'lv_property': 'Events:Sequence Iteration Complete Event:Pulse:Polarity',
        'name': 'SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the behavior of the Sequence Iteration Complete event.
for information about supported devices.
Default Value: NIDCPOWER_VAL_ACTIVE_HIGH
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150039: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Events:Sequence Iteration Complete Event:Pulse:Width',
        'name': 'SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the width of the Sequence Iteration Complete event, in seconds.
The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width  value for PXI Express devices is 250 ns.
The maximum event pulse width value for all devices is 1.6 microseconds.
the NI DC Power Supplies and SMUs Help for information about supported devices.
Valid Values: 1.5e-7 to 1.6e-6 seconds
Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic in',
},
    },
    1150040: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Events:Sequence Iteration Complete Event:Output Terminal',
        'name': 'SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Sequence Iteration Complete event.
for information about supported devices.
Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal  is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or  with the shortened terminal name, PXI_Trig0.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150041: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'Polarity',
        'lv_property': 'Events:Source Complete Event:Pulse:Polarity',
        'name': 'SOURCE_COMPLETE_EVENT_PULSE_POLARITY',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the behavior of the Source Complete event.
for information about supported devices.
Default Value: NIDCPOWER_VAL_ACTIVE_HIGH
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150042: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Events:Source Complete Event:Pulse:Width',
        'name': 'SOURCE_COMPLETE_EVENT_PULSE_WIDTH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the width of the Source Complete event, in seconds.
for information about supported devices.
The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value  for PXI Express devices is 250 ns.
The maximum event pulse width value for all devices is 1.6 microseconds
Valid Values: 1.5e-7 to 1.6e-6 seconds
Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150043: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Events:Source Complete Event:Output Terminal',
        'name': 'SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Source Complete event.
for information about supported devices.
Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you  can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal  name, PXI_Trig0.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150044: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'Polarity',
        'lv_property': 'Events:Measure Complete Event:Pulse:Polarity',
        'name': 'MEASURE_COMPLETE_EVENT_PULSE_POLARITY',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the behavior of the Measure Complete event.
for information about supported devices.
Default Value: NIDCPOWER_VAL_ACTIVE_HIGH
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150045: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Events:Measure Complete Event:Pulse:Width',
        'name': 'MEASURE_COMPLETE_EVENT_PULSE_WIDTH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the width of the Measure Complete event, in seconds.
The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse  width value for PXI Express devices is 250 ns.
The maximum event pulse width value for all devices is 1.6 microseconds.
for information about supported devices.
Valid Values: 1.5e-7 to 1.6e-6
Default Value: The default value for PXI devices is 150 ns. The default value  for PXI Express devices is 250 ns.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150046: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Events:Measure Complete Event:Event Delay',
        'name': 'MEASURE_COMPLETE_EVENT_DELAY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the amount of time to delay the generation of the Measure Complete event, in seconds.
for information about supported devices.
Valid Values: 0 to 167 seconds
Default Value: The NI PXI-4132 and NI PXIe-4140/4141/4142/4143/4144/4145/4154 supports values from  0 seconds to 167 seconds.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150047: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Events:Measure Complete Event:Output Terminal',
        'name': 'MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Measure Complete event.
for information about supported devices.
Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal  is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or  with the shortened terminal name, PXI_Trig0.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150048: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'Polarity',
        'lv_property': 'Events:Sequence Engine Done Event:Pulse:Polarity',
        'name': 'SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the behavior of the Sequence Engine Done event.
for information about supported devices.
Default Value: NIDCPOWER_VAL_ACTIVE_HIGH
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150049: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Events:Sequence Engine Done Event:Pulse:Width',
        'name': 'SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the width of the Sequence Engine Done event, in seconds.
The minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value  for PXI Express devices is 250 ns.
The maximum event pulse width value for all devices is 1.6 microseconds.
for information about supported devices.
Valid Values: 1.5e-7 to 1.6e-6 seconds
Default Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150050: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Events:Sequence Engine Done Event:Output Terminal',
        'name': 'SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Sequence Engine Done Complete event.
for information about supported devices.
Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal  is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or  with the shortened terminal name, PXI_Trig0.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150051: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Advanced:Source Delay',
        'name': 'SOURCE_DELAY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Determines when, in seconds, the device generates the Source Complete event, potentially starting a measurement if the  NIDCPOWER_ATTR_MEASURE_WHEN attribute is set to NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE.
Refer to the Single Point Source Mode and Sequence Source Mode topics for more information.
Valid Values: 0 to 167 seconds
Default Value: 0.01667 seconds
''',
'note': '''
Refer to Supported Attributes by Device for information about supported devices.
''',
},
    },
    1150054: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'SourceMode',
        'lv_property': 'Source:Source Mode',
        'name': 'SOURCE_MODE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether to run a single output point or a sequence. Refer to the Single Point Source Mode and Sequence Source  Mode topics in the NI DC Power Supplies and SMUs Help for more information about source modes.
Default value: NIDCPOWER_VAL_SINGLE_POINT
''',
},
    },
    1150055: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'AutoZero',
        'lv_property': 'Measurement:Auto Zero',
        'name': 'AUTO_ZERO',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the auto-zero method to use on the device.
Refer to the NI PXI-4132 Measurement Configuration and Timing and Auto Zero topics for more information  about how to configure your measurements.
Default Value: The default value for the NI PXI-4132 is NIDCPOWER_VAL_ON. The default value for  all other devices is NIDCPOWER_VAL_OFF, which is the only supported value for these devices.
''',
},
    },
    1150056: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Measurement:Fetch Backlog',
        'name': 'FETCH_BACKLOG',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Returns the number of measurements acquired that have not been fetched yet.',
},
    },
    1150057: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'MeasureWhen',
        'lv_property': 'Measurement:Advanced:Measure When',
        'name': 'MEASURE_WHEN',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies when the measure unit should acquire measurements. Unless this attribute is configured to  NIDCPOWER_VAL_ON_MEASURE_TRIGGER, the NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE attribute is ignored.
Refer to the Acquiring Measurements topic in the NI DC Power Supplies and SMUs Help for more information about how to  configure your measurements.
Default Value: If the NIDCPOWER_ATTR_SOURCE_MODE attribute is set to NIDCPOWER_VAL_SINGLE_POINT, the default value is  NIDCPOWER_VAL_ON_DEMAND. This value supports only the niDCPower_Measure function and niDCPower_MeasureMultiple  function. If the NIDCPOWER_ATTR_SOURCE_MODE attribute is set to NIDCPOWER_VAL_SEQUENCE, the default value is  NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE. This value supports only the niDCPower_FetchMultiple function.
''',
},
    },
    1150058: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Measurement:Aperture Time',
        'name': 'APERTURE_TIME',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the measurement aperture time for the channel configuration. Aperture time is specified in the units set by  the NIDCPOWER_ATTR_APERTURE_TIME_UNITS attribute.
for information about supported devices.
Refer to the Aperture Time topic in the NI DC Power Supplies and SMUs Help for more information about how to configure  your measurements and for information about valid values.
Default Value: 0.01666666 seconds
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150059: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'ApertureTimeUnits',
        'lv_property': 'Measurement:Aperture Time Units',
        'name': 'APERTURE_TIME_UNITS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the units of the NIDCPOWER_ATTR_APERTURE_TIME attribute for the channel configuration.
for information about supported devices.
Refer to the Aperture Time topic in the NI DC Power Supplies and SMUs Help for more information about  how to configure your measurements and for information about valid values.
Default Value: NIDCPOWER_VAL_SECONDS
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150060: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'tBoolean',
        'lv_property': 'Source:Output Connected',
        'name': 'OUTPUT_CONNECTED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the output relay is connected (closed) or disconnected (open). The NIDCPOWER_ATTR_OUTPUT_ENABLED  attribute does not change based on this attribute; they are independent of each other.
about supported devices.
Set this attribute to VI_FALSE to disconnect the output terminal from the output.
to the output terminal might discharge unless the relay is disconnected. Excessive connecting and disconnecting of the  output can cause premature wear on the relay.
Default Value: VI_TRUE
''',
'note': 'Only disconnect the output when disconnecting is necessary for your application. For example, a battery connected',
},
    },
    1150061: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Output Resistance',
        'name': 'OUTPUT_RESISTANCE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the output resistance that the device attempts to generate for the specified channel(s). This attribute is  available only when you set the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute on a support device. Refer to a supported device's topic about output resistance for more information about selecting an output resistance.
about supported devices.
Default Value: 0.0
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic for information',
},
    },
    1150062: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'TransientResponse',
        'lv_property': 'Source:Transient Response',
        'name': 'TRANSIENT_RESPONSE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the transient response. Refer to the Transient Response topic in the NI DC Power Supplies and SMUs Help  for more information about transient response.
for information about supported devices.
Default Value: NIDCPOWER_VAL_NORMAL
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150063: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Measurement:Measure Record Length',
        'name': 'MEASURE_RECORD_LENGTH',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies how many measurements compose a measure record. When this attribute is set to a value greater than 1, the  NIDCPOWER_ATTR_MEASURE_WHEN attribute must be set to NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE or  NIDCPOWER_VAL_ON_MEASURE_TRIGGER.
for information about supported devices.
Valid Values: 1 to 16,777,216
Default Value: 1
''',
'note': '''
This attribute is not available in a session involving multiple channels.
''',
},
    },
    1150064: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'tBoolean',
        'lv_property': 'Measurement:Measure Record Length Is Finite',
        'name': 'MEASURE_RECORD_LENGTH_IS_FINITE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to take continuous measurements. Call the niDCPower_Abort function to stop continuous measurements.  When this attribute is set to VI_FALSE and the NIDCPOWER_ATTR_SOURCE_MODE attribute is set to  NIDCPOWER_VAL_SINGLE_POINT, the NIDCPOWER_ATTR_MEASURE_WHEN attribute must be set to  NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE or NIDCPOWER_VAL_ON_MEASURE_TRIGGER. When this attribute is set to  VI_FALSE and the NIDCPOWER_ATTR_SOURCE_MODE attribute is set to NIDCPOWER_VAL_SEQUENCE, the NIDCPOWER_ATTR_MEASURE_WHEN  attribute must be set to NIDCPOWER_VAL_ON_MEASURE_TRIGGER.
for information about supported devices.
Default Value: VI_TRUE
''',
'note': '''
This attribute is not available in a session involving multiple channels.
''',
},
    },
    1150065: {
        'access': 'read only',
        'channel_based': 'False',
        'lv_property': 'Measurement:Measure Record Delta Time',
        'name': 'MEASURE_RECORD_DELTA_TIME',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Queries the amount of time, in seconds, between between the start of two consecutive measurements in a measure record.  Only query this attribute after the desired measurement settings are committed.
for information about supported devices.
two measurements and the rest would differ.
''',
'note': 'This attribute is not available when Auto Zero is configured to Once because the amount of time between the first',
},
    },
    1150066: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'DCNoiseRejection',
        'lv_property': 'Measurement:Advanced:DC Noise Rejection',
        'name': 'DC_NOISE_REJECTION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Determines the relative weighting of samples in a measurement. Refer to the NI PXIe-4140/4141 DC Noise Rejection,  NI PXIe-4142/4143 DC Noise Rejection, or NI PXIe-4144/4145 DC Noise Rejection topic in the NI DC Power Supplies  and SMUs Help for more information about noise rejection.
for information about supported devices.
Default Value: NIDCPOWER_VAL_NORMAL
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150067: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Custom Transient Response:Voltage:Gain Bandwidth',
        'name': 'VOLTAGE_GAIN_BANDWIDTH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This attribute takes effect when the channel is in Constant Voltage mode.
for information about supported devices.
Default Value: Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the  NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150068: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Custom Transient Response:Voltage:Compensation Frequency',
        'name': 'VOLTAGE_COMPENSATION_FREQUENCY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
The frequency at which a pole-zero pair is added to the system when the channel is in  Constant Voltage mode.
for information about supported devices.
Default value: Determined by the value of the NIDCPOWER_VAL_NORMAL setting of  the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150069: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Custom Transient Response:Voltage:Pole-Zero Ratio',
        'name': 'VOLTAGE_POLE_ZERO_RATIO',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
The ratio of the pole frequency to the zero frequency when the channel is in  Constant Voltage mode.
for information about supported devices.
Default value: Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the  NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150070: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Custom Transient Response:Current:Gain Bandwidth',
        'name': 'CURRENT_GAIN_BANDWIDTH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
The frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes.  This attribute takes effect when the channel is in Constant Current mode.
for information about supported devices.
Default Value: Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the  NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150071: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Custom Transient Response:Current:Compensation Frequency',
        'name': 'CURRENT_COMPENSATION_FREQUENCY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
The frequency at which a pole-zero pair is added to the system when the channel is in  Constant Current mode.
for information about supported devices.
Default Value: Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the  NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150072: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Custom Transient Response:Current:Pole-Zero Ratio',
        'name': 'CURRENT_POLE_ZERO_RATIO',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
The ratio of the pole frequency to the zero frequency when the channel is in  Constant Current mode.
for information about supported devices.
Default Value: Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150073: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'SelfCalibrationPersistence',
        'lv_property': 'Advanced:Self-Calibration Persistence',
        'name': 'SELF_CALIBRATION_PERSISTENCE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether the values calculated during self-calibration should be written to hardware to be used until the  next self-calibration or only used until the niDCPower_ResetDevice function is called or the machine  is powered down.
This attribute affects the behavior of the niDCPower_CalSelfCalibrate function. When set to  NIDCPOWER_VAL_KEEP_IN_MEMORY, the values calculated by the niDCPower_CalSelfCalibrate function are used in  the existing session, as well as in all further sessions until you call the niDCPower_ResetDevice function  or restart the machine. When you set this property to NIDCPOWER_VAL_WRITE_TO_EEPROM, the values calculated  by the niDCPower_CalSelfCalibrate function are written to hardware and used in the existing session and  in all subsequent sessions until another call to the niDCPower_CalSelfCalibrate function is made.
about supported devices.
Default Value: NIDCPOWER_VAL_KEEP_IN_MEMORY
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information',
},
    },
    1150074: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Advanced:Active Advanced Sequence',
        'name': 'ACTIVE_ADVANCED_SEQUENCE',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the advanced sequence to configure or generate.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic.',
},
    },
    1150075: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Advanced:Active Advanced Sequence Step',
        'name': 'ACTIVE_ADVANCED_SEQUENCE_STEP',
        'resettable': 'No',
        'type': 'ViInt64',
'documentation': {
'description': '''
Specifies the advanced sequence step to configure.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic.',
},
    },
    1150077: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Measurement:Advanced:Measure Buffer Size',
        'name': 'MEASURE_BUFFER_SIZE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of samples that the active channel measurement buffer can hold.
The default value is the maximum number of samples that a device is capable of recording in one second.
for information about supported devices.
Valid Values: 1000 to 2147483647
Default Value: Varies by device. Refer to Supported Attributes by Device topic in  the NI DC Power Supplies and SMUs Help for more information about default values.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1150078: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'tBoolean',
        'lv_property': 'Source:Advanced:Sequence Loop Count Is Finite',
        'name': 'SEQUENCE_LOOP_COUNT_IS_FINITE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether a sequence should repeat indefinitely.
Refer to the Sequence Source Mode topic in the NI DC Power Supplies and SMUs Help for more information about  infinite sequencing.
NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE attribute is set to VI_FALSE,  the NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT attribute is ignored.
Default Value: VI_TRUE
''',
'note': 'This attribute is not supported by all devices. When the',
},
    },
    1150080: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Voltage:Pulse Voltage Level',
        'name': 'PULSE_VOLTAGE_LEVEL',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse current limit, in amps, that the output cannot exceed when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse.
This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.
Valid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE attribute.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150081: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Voltage:Pulse Current Limit',
        'name': 'PULSE_CURRENT_LIMIT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse current limit, in amps, that the output cannot exceed when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse.
This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE and the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY  attribute is set to NIDCPOWER_VAL_SYMMETRIC.
Valid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE attribute.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150082: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Voltage:Pulse Bias Voltage Level',
        'name': 'PULSE_BIAS_VOLTAGE_LEVEL',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse bias voltage level, in volts, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.
This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.
Valid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE attribute.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150083: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Voltage:Pulse Bias Current Limit',
        'name': 'PULSE_BIAS_CURRENT_LIMIT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse bias current limit, in amps, that the output cannot exceed when generating the desired pulse bias voltage on the specified channel(s) during the off phase of a pulse.
This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.
Valid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE property.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150084: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Voltage:Pulse Voltage Level Range',
        'name': 'PULSE_VOLTAGE_LEVEL_RANGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse voltage level range, in volts, for the specified channel(s).
The range defines the valid values at which you can set the pulse voltage level and pulse bias voltage level.
This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.
For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150085: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Voltage:Pulse Current Limit Range',
        'name': 'PULSE_CURRENT_LIMIT_RANGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse current limit range, in amps, for the specified channel(s).
The range defines the valid values to which you can set the pulse current limit and pulse bias current limit.
This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.
For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150086: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Current:Pulse Current Level',
        'name': 'PULSE_CURRENT_LEVEL',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse current level, in amps, that the device attempts to generate on the specified channel(s) during the on phase of a pulse.
This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.
Valid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE attribute.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150087: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Current:Pulse Voltage Limit',
        'name': 'PULSE_VOLTAGE_LIMIT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired pulse current on the specified channel(s) during the on phase of a pulse.
This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT and the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY attribute  is set to NIDCPOWER_VAL_SYMMETRIC.
Valid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE attribute.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150088: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Current:Pulse Bias Current Level',
        'name': 'PULSE_BIAS_CURRENT_LEVEL',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse bias current level, in amps, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.
This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.
Valid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE attribute.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150089: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Current:Pulse Bias Voltage Limit',
        'name': 'PULSE_BIAS_VOLTAGE_LIMIT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired current on the specified channel(s) during the off phase of a pulse.
This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.
Valid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE attribute.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150090: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Current:Pulse Current Level Range',
        'name': 'PULSE_CURRENT_LEVEL_RANGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse current level range, in amps, for the specified channel(s).
The range defines the valid values to which you can set the pulse current level and pulse bias current level.
This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.
For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150091: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Current:Pulse Voltage Limit Range',
        'name': 'PULSE_VOLTAGE_LIMIT_RANGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse voltage limit range, in volts, for the specified channel(s).
The range defines the valid values to which you can set the pulse voltage limit and pulse bias voltage limit.
This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.
For valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.
''',
'note': 'The channel must be enabled for the specified current limit to take effect. Refer to the NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.',
},
    },
    1150092: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Advanced:Pulse Bias Delay',
        'name': 'PULSE_BIAS_DELAY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Determines when, in seconds, the device generates the Pulse Complete event after generating the off level of a pulse.
Valid Values: 0 to 167 seconds
Default Value: 16.67 milliseconds
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150093: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Advanced:Pulse On Time',
        'name': 'PULSE_ON_TIME',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Determines the length, in seconds, of the on phase of a pulse.
Valid Values: 10 microseconds to 167 seconds
Default Value: 34 milliseconds
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150094: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Advanced:Pulse Off Time',
        'name': 'PULSE_OFF_TIME',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Determines the length, in seconds, of the off phase of a pulse.
Valid Values: 10 microseconds to 167 seconds
Default Value: 34 milliseconds
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150095: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TriggerType',
        'lv_property': 'Triggers:Pulse Trigger:Trigger Type',
        'name': 'PULSE_TRIGGER_TYPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the behavior of the Pulse trigger.
Default Value: NIDCPOWER_VAL_NONE
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150096: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'DigitalEdge',
        'lv_property': 'Triggers:Pulse Trigger:Digital Edge:Edge',
        'name': 'DIGITAL_EDGE_PULSE_TRIGGER_EDGE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether to configure the Pulse trigger to assert on the rising or falling edge.
Default Value: NIDCPOWER_VAL_RISING
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150097: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Triggers:Pulse Trigger:Digital Edge:Input Terminal',
        'name': 'DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the input terminal for the Pulse trigger. This attribute is used only when the NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE attribute is set to digital edge.
You can specify any valid input terminal for this attribute. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.
Input terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150098: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Triggers:Pulse Trigger:Export Output Terminal',
        'name': 'EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Pulse trigger.
Refer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals available on your device.
Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150099: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Events:Pulse Complete Event:Output Terminal',
        'name': 'PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Pulse Complete event.
Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.
Default Value:The default value for PXI Express devices is 250 ns.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150100: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'Polarity',
        'lv_property': 'Events:Pulse Complete Event:Pulse:Polarity',
        'name': 'PULSE_COMPLETE_EVENT_PULSE_POLARITY',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the behavior of the Pulse Complete event.
Default Value: NIDCPOWER_VAL_ACTIVE_HIGH
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150101: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Events:Pulse Complete Event:Pulse:Width',
        'name': 'PULSE_COMPLETE_EVENT_PULSE_WIDTH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the width of the Pulse Complete event, in seconds.
The minimum event pulse width value for PXI Express devices is 250 ns.
The maximum event pulse width value for PXI Express devices is 1.6 microseconds.
Default Value: The default value for PXI Express devices is 250 ns.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150102: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Events:Ready For Pulse Trigger Event:Output Terminal',
        'name': 'READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Ready For Pulse Trigger event.
Output terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150103: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'Polarity',
        'lv_property': 'Events:Ready For Pulse Trigger Event:Pulse:Polarity',
        'name': 'READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the behavior of the Ready For Pulse Trigger event.
Default Value: NIDCPOWER_VAL_ACTIVE_HIGH
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150104: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Events:Ready For Pulse Trigger Event:Pulse:Width',
        'name': 'READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the width of the Ready For Pulse Trigger event, in seconds.
The minimum event pulse width value for PXI Express devices is 250 ns.
The maximum event pulse width value for all devices is 1.6 microseconds.
Default Value: The default value for PXI Express devices is 250 ns
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information about supported devices.',
},
    },
    1150105: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': 'tBoolean',
        'lv_property': 'Advanced:Interlock Input Open',
        'name': 'INTERLOCK_INPUT_OPEN',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Indicates whether the safety interlock circuit is open.
Refer to the Safety Interlock topic in the NI DC Power Supplies and SMUs Help for more information about  the safety interlock circuit.
about supported devices.
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device for information',
},
    },
    1150184: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'ComplianceLimitSymmetry',
        'lv_property': 'Source:Advanced:Compliance Limit Symmetry',
        'name': 'COMPLIANCE_LIMIT_SYMMETRY',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether compliance limits for current generation and voltage
generation for the device are applied symmetrically about 0 V and 0 A or
asymmetrically with respect to 0 V and 0 A.
When set to **Symmetric**, voltage limits and current limits are set
using a single property with a positive value. The resulting range is
bounded by this positive value and its opposite.
When set to **Asymmetric**, you must separately set a limit high and a
limit low using distinct properties.
For asymmetric limits, the range bounded by the limit high and limit low
must include zero.
**Default Value:** Symmetric
**Related Topics:**
`Compliance <NI_DC_Power_Supplies_Help.chm::/compliance.html>`__
`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
`Changing
Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
`Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__
''',
'note': '''
Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150185: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:DC Current:Voltage Limit High',
        'name': 'VOLTAGE_LIMIT_HIGH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the maximum voltage, in volts, that the output can produce
when generating the desired current on the specified channel(s).
This property is applicable only if the `Compliance Limit
Symmetry <pniDCPower_ComplianceLimitSymmetry.html>`__ property is set to
**Asymmetric** and the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
Current**.
You must also specify a `Voltage Limit
Low <pniDCPower_VoltageLimitLow.html>`__ to complete the asymmetric
range.
**Valid Values:** [1% of `Voltage Limit
Range <pniDCPower_VoltageLimitRange.html>`__, `Voltage Limit
Range <pniDCPower_VoltageLimitRange.html>`__]
The range bounded by the limit high and limit low must include zero.
**Default Value:** Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
**Related Topics:**
`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
`Changing
Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
`Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__
''',
'note': '''
The limit may be extended beyond the selected limit range if the
`Overranging Enabled <pniDCPower_OverrangingEnabled.html>`__ property is
set to TRUE.
''',
},
    },
    1150186: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:DC Current:Voltage Limit Low',
        'name': 'VOLTAGE_LIMIT_LOW',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the minimum voltage, in volts, that the output can produce
when generating the desired current on the specified channel(s).
This property is applicable only if the `Compliance Limit
Symmetry <pniDCPower_ComplianceLimitSymmetry.html>`__ property is set to
**Asymmetric** and the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
Current**.
You must also specify a `Voltage Limit
High <pniDCPower_VoltageLimitHigh.html>`__ to complete the asymmetric
range.
**Valid Values:** [-`Voltage Limit
Range <pniDCPower_VoltageLimitRange.html>`__, -1% of `Voltage Limit
Range <pniDCPower_VoltageLimitRange.html>`__]
The range bounded by the limit high and limit low must include zero.
**Default Value:** Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
**Related Topics:**
`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
`Changing
Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
`Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__
''',
'note': '''
The limit may be extended beyond the selected limit range if the
`Overranging Enabled <pniDCPower_OverrangingEnabled.html>`__ property is
set to TRUE.
''',
},
    },
    1150187: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:DC Voltage:Current Limit High',
        'name': 'CURRENT_LIMIT_HIGH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the maximum current, in amps, that the output can produce when
generating the desired voltage on the specified channel(s).
This property is applicable only if the `Compliance Limit
Symmetry <pniDCPower_ComplianceLimitSymmetry.html>`__ property is set to
**Asymmetric** and the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
Voltage**.
You must also specify a `Current Limit
Low <pniDCPower_CurrentLimitLow.html>`__ to complete the asymmetric
range.
**Valid Values:** [1% of `Current Limit
Range <pniDCPower_CurrentLimitRange.html>`__, `Current Limit
Range <pniDCPower_CurrentLimitRange.html>`__]
The range bounded by the limit high and limit low must include zero.
**Default Value:** Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
**Related Topics:**
`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
`Changing
Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
`Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__
''',
'note': '''
The limit may be extended beyond the selected limit range if the
`Overranging Enabled <pniDCPower_OverrangingEnabled.html>`__ property is
set to TRUE.
''',
},
    },
    1150188: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:DC Voltage:Current Limit Low',
        'name': 'CURRENT_LIMIT_LOW',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the minimum current, in amps, that the output can produce when
generating the desired voltage on the specified channel(s).
This property is applicable only if the `Compliance Limit
Symmetry <pniDCPower_ComplianceLimitSymmetry.html>`__ property is set to
**Asymmetric** and the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
Voltage**.
You must also specify a `Current Limit
High <pniDCPower_CurrentLimitHigh.html>`__ to complete the asymmetric
range.
**Valid Values:** [-`Current Limit
Range <pniDCPower_CurrentLimitRange.html>`__, -1% of `Current Limit
Range <pniDCPower_CurrentLimitRange.html>`__]
The range bounded by the limit high and limit low must include zero.
**Default Value:** Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
**Related Topics:**
`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
`Changing
Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
`Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__
''',
'note': '''
The limit may be extended beyond the selected limit range if the
`Overranging Enabled <pniDCPower_OverrangingEnabled.html>`__ property is
set to TRUE.
''',
},
    },
    1150189: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Current:Pulse Voltage Limit High',
        'name': 'PULSE_VOLTAGE_LIMIT_HIGH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the maximum voltage, in volts, that the output can produce
when generating the desired pulse current on the specified channel(s)
during the *on* phase of a pulse.
This property is applicable only if the `Compliance Limit
Symmetry <pniDCPower_ComplianceLimitSymmetry.html>`__ property is set to
**Asymmetric** and the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Current**.
You must also specify a `Pulse Voltage Limit
Low <pniDCPower_PulseVoltageLimitLow.html>`__ to complete the asymmetric
range.
**Valid Values:** [1% of `Pulse Voltage Limit
Range <pniDCPower_PulseVoltageLimitRange.html>`__, `Pulse Voltage Limit
Range <pniDCPower_PulseVoltageLimitRange.html>`__]
The range bounded by the limit high and limit low must include zero.
**Default Value:** Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
**Related Topics:**
`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
`Changing
Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
`Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__
''',
'note': '''
The limit may be extended beyond the selected limit range if the
`Overranging Enabled <pniDCPower_OverrangingEnabled.html>`__ property is
set to TRUE or if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to a
pulsing function.
''',
},
    },
    1150190: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Current:Pulse Voltage Limit Low',
        'name': 'PULSE_VOLTAGE_LIMIT_LOW',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the minimum voltage, in volts, that the output can produce
when generating the desired pulse current on the specified channel(s)
during the *on* phase of a pulse.
This property is applicable only if the `Compliance Limit
Symmetry <pniDCPower_ComplianceLimitSymmetry.html>`__ property is set to
**Asymmetric** and the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Current**.
You must also specify a `Pulse Voltage Limit
High <pniDCPower_PulseVoltageLimitHigh.html>`__ to complete the
asymmetric range.
**Valid Values:** [-`Pulse Voltage Limit
Range <pniDCPower_PulseVoltageLimitRange.html>`__, -1% of `Pulse Voltage
Limit Range <pniDCPower_PulseVoltageLimitRange.html>`__]
The range bounded by the limit high and limit low must include zero.
**Default Value:** Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
**Related Topics:**
`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
`Changing
Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
`Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__
''',
'note': '''
The limit may be extended beyond the selected limit range if the
`Overranging Enabled <pniDCPower_OverrangingEnabled.html>`__ property is
set to TRUE or if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to a
pulsing function.
''',
},
    },
    1150191: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Current:Pulse Bias Voltage Limit High',
        'name': 'PULSE_BIAS_VOLTAGE_LIMIT_HIGH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the maximum voltage, in volts, that the output can produce
when generating the desired pulse current on the specified channel(s)
during the *off* phase of a pulse.
This property is applicable only if the `Compliance Limit
Symmetry <pniDCPower_ComplianceLimitSymmetry.html>`__ property is set to
**Asymmetric** and the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Current**.
You must also specify a `Pulse Bias Voltage Limit
Low <pniDCPower_PulseBiasVoltageLimitLow.html>`__ to complete the
asymmetric range.
**Valid Values:** [1% of `Pulse Voltage Limit
Range <pniDCPower_PulseVoltageLimitRange.html>`__, `Pulse Voltage Limit
Range <pniDCPower_PulseVoltageLimitRange.html>`__]
The range bounded by the limit high and limit low must include zero.
**Default Value:** Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
**Related Topics:**
`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
`Changing
Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
`Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__
''',
'note': '''
The limit may be extended beyond the selected limit range if the
`Overranging Enabled <pniDCPower_OverrangingEnabled.html>`__ property is
set to TRUE or if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to a
pulsing function.
''',
},
    },
    1150192: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Current:Pulse Bias Voltage Limit Low',
        'name': 'PULSE_BIAS_VOLTAGE_LIMIT_LOW',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the minimum voltage, in volts, that the output can produce
when generating the desired pulse current on the specified channel(s)
during the *off* phase of a pulse.
This property is applicable only if the `Compliance Limit
Symmetry <pniDCPower_ComplianceLimitSymmetry.html>`__ property is set to
**Asymmetric** and the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Current**.
You must also specify a `Pulse Bias Voltage Limit
High <pniDCPower_PulseBiasVoltageLimitHigh.html>`__ to complete the
asymmetric range.
**Valid Values:** [-`Pulse Voltage Limit
Range <pniDCPower_PulseVoltageLimitRange.html>`__, -1% of `Pulse Voltage
Limit Range <pniDCPower_PulseVoltageLimitRange.html>`__]
The range bounded by the limit high and limit low must include zero.
**Default Value:** Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
**Related Topics:**
`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
`Changing
Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
`Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__
''',
'note': '''
The limit may be extended beyond the selected limit range if the
`Overranging Enabled <pniDCPower_OverrangingEnabled.html>`__ property is
set to TRUE or if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to a
pulsing function.
''',
},
    },
    1150193: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Voltage:Pulse Current Limit High',
        'name': 'PULSE_CURRENT_LIMIT_HIGH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the maximum current, in amps, that the output can produce when
generating the desired pulse voltage on the specified channel(s) during
the *on* phase of a pulse.
This property is applicable only if the `Compliance Limit
Symmetry <pniDCPower_ComplianceLimitSymmetry.html>`__ property is set to
**Asymmetric** and the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Voltage**.
You must also specify a `Pulse Current Limit
Low <pniDCPower_PulseCurrentLimitLow.html>`__ to complete the asymmetric
range.
**Valid Values:** [1% of `Pulse Current Limit
Range <pniDCPower_PulseCurrentLimitRange.html>`__, `Pulse Current Limit
Range <pniDCPower_PulseCurrentLimitRange.html>`__]
The range bounded by the limit high and limit low must include zero.
**Default Value:** Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
**Related Topics:**
`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
`Changing
Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
`Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__
''',
'note': '''
The limit may be extended beyond the selected limit range if the
`Overranging Enabled <pniDCPower_OverrangingEnabled.html>`__ property is
set to TRUE or if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to a
pulsing function.
''',
},
    },
    1150194: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Voltage:Pulse Current Limit Low',
        'name': 'PULSE_CURRENT_LIMIT_LOW',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the minimum current, in amps, that the output can produce when
generating the desired pulse voltage on the specified channel(s) during
the *on* phase of a pulse.
This property is applicable only if the `Compliance Limit
Symmetry <pniDCPower_ComplianceLimitSymmetry.html>`__ property is set to
**Asymmetric** and the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Voltage**.
You must also specify a `Pulse Current Limit
High <pniDCPower_PulseCurrentLimitHigh.html>`__ to complete the
asymmetric range.
**Valid Values:** [-`Pulse Current Limit
Range <pniDCPower_PulseCurrentLimitRange.html>`__, -1% of `Pulse Current
Limit Range <pniDCPower_PulseCurrentLimitRange.html>`__]
The range bounded by the limit high and limit low must include zero.
**Default Value:** Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
**Related Topics:**
`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
`Changing
Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
`Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__
''',
'note': '''
The limit may be extended beyond the selected limit range if the
`Overranging Enabled <pniDCPower_OverrangingEnabled.html>`__ property is
set to TRUE or if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to a
pulsing function.
''',
},
    },
    1150195: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Voltage:Pulse Bias Current Limit High',
        'name': 'PULSE_BIAS_CURRENT_LIMIT_HIGH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the maximum current, in amps, that the output can produce when
generating the desired pulse voltage on the specified channel(s) during
the *off* phase of a pulse.
This property is applicable only if the `Compliance Limit
Symmetry <pniDCPower_ComplianceLimitSymmetry.html>`__ property is set to
**Asymmetric** and the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Voltage**.
You must also specify a `Pulse Bias Current Limit
Low <pniDCPower_PulseBiasCurrentLimitLow.html>`__ to complete the
asymmetric range.
**Valid Values:** [1% of `Pulse Current Limit
Range <pniDCPower_PulseCurrentLimitRange.html>`__, `Pulse Current Limit
Range <pniDCPower_PulseCurrentLimitRange.html>`__]
The range bounded by the limit high and limit low must include zero.
**Default Value:** Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
**Related Topics:**
`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
`Changing
Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
`Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__
''',
'note': '''
The limit may be extended beyond the selected limit range if the
`Overranging Enabled <pniDCPower_OverrangingEnabled.html>`__ property is
set to TRUE or if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to a
pulsing function.
''',
},
    },
    1150196: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:Pulse Voltage:Pulse Bias Current Limit Low',
        'name': 'PULSE_BIAS_CURRENT_LIMIT_LOW',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the minimum current, in amps, that the output can produce when
generating the desired pulse voltage on the specified channel(s) during
the *off* phase of a pulse.
This property is applicable only if the `Compliance Limit
Symmetry <pniDCPower_ComplianceLimitSymmetry.html>`__ property is set to
**Asymmetric** and the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Voltage**.
You must also specify a `Pulse Bias Current Limit
High <pniDCPower_PulseBiasCurrentLimitHigh.html>`__ to complete the
asymmetric range.
**Valid Values:** [-`Pulse Current Limit
Range <pniDCPower_PulseCurrentLimitRange.html>`__, -1% of `Pulse Current
Limit Range <pniDCPower_PulseCurrentLimitRange.html>`__]
The range bounded by the limit high and limit low must include zero.
**Default Value:** Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
**Related Topics:**
`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
`Changing
Ranges <NI_DC_Power_Supplies_Help.chm::/changing_ranges.html>`__
`Overranging <NI_DC_Power_Supplies_Help.chm::/overranging.html>`__
''',
'note': '''
The limit may be extended beyond the selected limit range if the
`Overranging Enabled <pniDCPower_OverrangingEnabled.html>`__ property is
set to TRUE or if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to a
pulsing function.
''',
},
    },
    1250001: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:DC Voltage:Voltage Level',
        'name': 'VOLTAGE_LEVEL',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the voltage level, in volts, that the device attempts to generate on the specified channel(s).
This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_VOLTAGE.
NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.
Valid Values: The valid values for this attribute are defined by the values you specify for the  NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE attribute.
''',
'note': 'The channel must be enabled for the specified voltage level to take effect. Refer to the',
},
    },
    1250002: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'tBoolean',
        'lv_property': 'Source:Advanced:OVP Enabled',
        'name': 'OVP_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables (VI_TRUE) or disables (VI_FALSE) overvoltage protection (OVP).
Refer to the Output Overvoltage Protection topic in the NI DC Power Supplies and SMUs Help for more information about  overvoltage protection.
for information about supported devices.
Default Value: VI_FALSE
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1250003: {
        'access': 'read-write',
        'channel_based': 'False',
        'lv_property': 'Source:Advanced:OVP Limit',
        'name': 'OVP_LIMIT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Determines the voltage limit, in volts, beyond which overvoltage protection (OVP) engages.
for information about supported devices.
Valid Values: 2 V to 210 V
Default Value: 210 V
''',
'note': 'This attribute is not supported by all devices. Refer to Supported Attributes by Device topic',
},
    },
    1250005: {
        'access': 'read-write',
        'channel_based': 'True',
        'lv_property': 'Source:DC Voltage:Current Limit',
        'name': 'CURRENT_LIMIT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the current limit, in amps, that the output cannot exceed when generating the desired voltage level  on the specified channel(s).
This attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to  NIDCPOWER_VAL_DC_VOLTAGE and the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY attribute is set to  NIDCPOWER_VAL_SYMMETRIC.
NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.
Valid Values: The valid values for this attribute are defined by the values to which  NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE attribute is set.
''',
'note': 'The channel must be enabled for the specified current limit to take effect. Refer to the',
},
    },
    1250006: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'tBoolean',
        'lv_property': 'Source:Output Enabled',
        'name': 'OUTPUT_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the output is enabled (VI_TRUE) or disabled (VI_FALSE).
Depending on the value you specify for the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute, you also must set the  voltage level or current level in addition to  enabling the output
the niDCPower_Initiate function. Refer to the Programming States topic in the NI DC Power Supplies and SMUs Help for  more information about NI-DCPower programming states.
Default Value: The default value is VI_TRUE if you use the niDCPower_InitializeWithChannels function to open  the session. Otherwise the default value is VI_FALSE, including when you use a calibration session or the deprecated programming model.
''',
'note': 'If the session is in the Committed or Uncommitted states, enabling the output does not take effect until you call',
},
    },
}
