# -*- coding: utf-8 -*-
# This file is generated from NI-DCPower API metadata version 22.0.0d216
attributes = {
    1050003: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether NI-DCPower queries the device status after each operation.\nQuerying the device status is useful for debugging. After you validate your program, you can set this attribute to VI_FALSE to disable status checking and maximize performance.\nNI-DCPower ignores status checking for particular attributes regardless of the setting of this attribute.\nUse the niDCPower_InitializeWithChannels function to override this value.\nDefault Value: VI_TRUE\n'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Query Instrument Status',
        'name': 'QUERY_INSTRUMENT_STATUS',
        'type': 'ViBoolean'
    },
    1050005: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether to simulate NI-DCPower I/O operations. VI_TRUE specifies that operation is simulated.\nDefault Value: VI_FALSE\n'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Simulate',
        'name': 'SIMULATE',
        'type': 'ViBoolean'
    },
    1050007: {
        'access': 'read only',
        'documentation': {
            'description': '\nIndicates the Driver Setup string that you specified when initializing the driver.\nSome cases exist where you must specify the instrument driver options at initialization time. An example of this case is specifying a particular device model from among a family of devices that the driver supports. This attribute is useful when simulating a device. You can specify the driver-specific options through the DriverSetup keyword in the optionsString parameter in the niDCPower_InitializeWithChannels function or through the IVI Configuration Utility.\nYou can specify driver-specific options through the DriverSetup keyword in the optionsString parameter in the niDCPower_InitializeWithChannels function. If you do not specify a Driver Setup string, this attribute returns an empty string.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Driver Setup',
        'name': 'DRIVER_SETUP',
        'type': 'ViString'
    },
    1050203: {
        'access': 'read only',
        'documentation': {
            'description': 'Indicates the number of channels that NI-DCPower supports for the instrument that was chosen when the current session was opened. For channel-based attributes, the IVI engine maintains a separate cache value for each channel.'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Channel Count',
        'name': 'CHANNEL_COUNT',
        'type': 'ViInt32'
    },
    1050302: {
        'access': 'read only',
        'documentation': {
            'description': 'Contains the prefix for NI-DCPower. The name of each user-callable function in NI-DCPower begins with this prefix.'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Driver Prefix',
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'type': 'ViString'
    },
    1050304: {
        'access': 'read only',
        'documentation': {
            'description': '\nIndicates the resource descriptor NI-DCPower uses to identify the physical device.\nIf you initialize NI-DCPower with a logical name, this attribute contains the resource descriptor that corresponds to the entry in the IVI Configuration utility.\nIf you initialize NI-DCPower with the resource descriptor, this attribute contains that value.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Resource Descriptor',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'type': 'ViString'
    },
    1050305: {
        'access': 'read only',
        'documentation': {
            'description': '\nContains the logical name you specified when opening the current IVI session.\nYou can pass a logical name to the niDCPower_InitializeWithChannels function. The IVI Configuration utility must contain an entry for the logical name. The logical name entry refers to a function section in the IVI Configuration file. The function section specifies a physical device and initial user options.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Logical Name',
        'name': 'LOGICAL_NAME',
        'type': 'ViString'
    },
    1050327: {
        'access': 'read only',
        'documentation': {
            'description': 'Contains a comma-separated (,) list of supported NI-DCPower device models.'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'type': 'ViString'
    },
    1050510: {
        'access': 'read only',
        'documentation': {
            'description': 'Contains the firmware revision information for the device you are currently using.'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Firmware Revision',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViString'
    },
    1050511: {
        'access': 'read only',
        'documentation': {
            'description': 'Contains the name of the manufacturer for the device you are currently using.'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Manufacturer',
        'name': 'INSTRUMENT_MANUFACTURER',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViString'
    },
    1050512: {
        'access': 'read only',
        'documentation': {
            'description': 'Contains the model number or name of the device that you are currently using.'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Model',
        'name': 'INSTRUMENT_MODEL',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViString'
    },
    1050513: {
        'access': 'read only',
        'documentation': {
            'description': 'Contains the name of the vendor that supplies NI-DCPower.'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Driver Vendor',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'type': 'ViString'
    },
    1050514: {
        'access': 'read only',
        'documentation': {
            'description': 'Contains a brief description of the specific driver.'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Description',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'type': 'ViString'
    },
    1050551: {
        'access': 'read only',
        'documentation': {
            'description': 'Contains additional version information about NI-DCPower.'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Revision',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'type': 'ViString'
    },
    1150000: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the power source to use. NI-DCPower switches the power source used by the device to the specified value.\nDefault Value: NIDCPOWER_VAL_AUTOMATIC\nis set to NIDCPOWER_VAL_AUTOMATIC. However, if the session is in the Committed or Uncommitted state when you set this attribute, the power source selection only occurs after you call the niDCPower_InitiateWithChannels function.\n',
            'note': 'Automatic selection is not persistent and occurs only at the time this attribute'
        },
        'enum': 'PowerSource',
        'lv_property': 'Advanced:Power Source',
        'name': 'POWER_SOURCE',
        'type': 'ViInt32'
    },
    1150001: {
        'access': 'read only',
        'documentation': {
            'description': 'Indicates whether the device is using the internal or auxiliary power source to generate power.'
        },
        'enum': 'PowerSourceInUse',
        'lv_property': 'Advanced:Power Source In Use',
        'name': 'POWER_SOURCE_IN_USE',
        'type': 'ViInt32'
    },
    1150002: {
        'access': 'read only',
        'documentation': {
            'description': '\nIndicates whether an auxiliary power source is connected to the device.\nA value of VI_FALSE may indicate that the auxiliary input fuse has blown. Refer to the Detecting Internal/Auxiliary Power topic in the NI DC Power Supplies and SMUs Help for more information about internal and auxiliary power.\npower source to generate power. Use the NIDCPOWER_ATTR_POWER_SOURCE_IN_USE attribute to retrieve this information.\n',
            'note': 'This attribute does not necessarily indicate if the device is using the auxiliary'
        },
        'lv_property': 'Advanced:Auxiliary Power Source Available',
        'name': 'AUXILIARY_POWER_SOURCE_AVAILABLE',
        'type': 'ViBoolean'
    },
    1150003: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the number of samples to average when you take a measurement.\nIncreasing the number of samples to average decreases measurement noise but increases the time required to take a measurement. Refer to the NI PXI-4110, NI PXI-4130, NI PXI-4132, or NI PXIe-4154 Averaging topic for optional attribute settings to improve immunity to certain noise types, or refer to the NI PXIe-4140/4141  DC Noise Rejection, NI PXIe-4142/4143 DC Noise Rejection, or NI PXIe-4144/4145 DC Noise Rejection topic for information about improving noise immunity for those devices.\nDefault Value:\nNI PXI-4110 or NI PXI-4130—10\nNI PXI-4132—1\nNI PXIe-4112—1\nNI PXIe-4113—1\nNI PXIe-4140/4141—1\nNI PXIe-4142/4143—1\nNI PXIe-4144/4145—1\nNI PXIe-4154—500\n'
        },
        'lv_property': 'Measurement:Samples To Average',
        'name': 'SAMPLES_TO_AVERAGE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150004: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the current limit range, in amps, for the specified channel(s).\nThe range defines the valid value to which the current limit can be set. Use the NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE attribute to enable automatic selection of the current limit range.\nThe NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_VOLTAGE.\nNIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.\nFor valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.\n',
            'note': 'The channel must be enabled for the specified current limit to take effect. Refer to the NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.'
        },
        'lv_property': 'Source:DC Voltage:Current Limit Range',
        'name': 'CURRENT_LIMIT_RANGE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150005: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the voltage level range, in volts, for the specified channel(s).\nThe range defines the valid values to which the voltage level can be set. Use the NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE attribute to enable automatic selection of the voltage level range.\nThe NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_VOLTAGE.\nNIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.\nFor valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.\n',
            'note': 'The channel must be enabled for the specified voltage level range to take effect. Refer to the NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.'
        },
        'lv_property': 'Source:DC Voltage:Voltage Level Range',
        'name': 'VOLTAGE_LEVEL_RANGE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150006: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether the measurement returned from any measurement call starts with a new measurement call (VI_TRUE) or returns a measurement that has already begun or completed(VI_FALSE).\nWhen you set the NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE attribute in the Running state, the output channel measurements might move out of synchronization. While NI-DCPower automatically synchronizes measurements upon the initialization of a session, you can force a synchronization in the running state before you run the niDCPower_MeasureMultiple function. To force a synchronization in the running state, set this attribute to VI_TRUE, and then run the niDCPower_MeasureMultiple function, specifying all channels in the channel name parameter. You can set the NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT attribute to VI_FALSE after the niDCPower_MeasureMultiple function completes.\nDefault Value: VI_TRUE\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Measurement:Advanced:Reset Average Before Measurement',
        'name': 'RESET_AVERAGE_BEFORE_MEASUREMENT',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1150007: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether NI-DCPower allows setting the voltage level, current level, voltage limit and current limit outside the device specification limits. VI_TRUE means that overranging is enabled.\nRefer to the Ranges topic in the NI DC Power Supplies and SMUs Help for more information about overranging.\nDefault Value: VI_FALSE\n'
        },
        'lv_property': 'Source:Advanced:Overranging Enabled',
        'name': 'OVERRANGING_ENABLED',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1150008: {
        'access': 'read-write',
        'documentation': {
            'description': '\nConfigures the function to generate on the specified channel(s).\nWhen NIDCPOWER_VAL_DC_VOLTAGE is selected, the device generates the desired voltage level on the output as long as the output current is below the current limit. You can use the following attributes to configure the channel when NIDCPOWER_VAL_DC_VOLTAGE is selected:\nNIDCPOWER_ATTR_VOLTAGE_LEVEL\nNIDCPOWER_ATTR_CURRENT_LIMIT\nNIDCPOWER_ATTR_CURRENT_LIMIT_HIGH\nNIDCPOWER_ATTR_CURRENT_LIMIT_LOW\nNIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE\nNIDCPOWER_ATTR_CURRENT_LIMIT_RANGE\nNIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY\nWhen NIDCPOWER_VAL_DC_CURRENT is selected, the device generates the desired current level on the output as long as the output voltage is below the voltage limit. You can use the following attributes to configure the channel when NIDCPOWER_VAL_DC_CURRENT is selected:\nNIDCPOWER_ATTR_CURRENT_LEVEL\nNIDCPOWER_ATTR_VOLTAGE_LIMIT\nNIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH\nNIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW\nNIDCPOWER_ATTR_CURRENT_LEVEL_RANGE\nNIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE\nNIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY\n'
        },
        'enum': 'OutputFunction',
        'lv_property': 'Source:Output Function',
        'name': 'OUTPUT_FUNCTION',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150009: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the current level, in amps, that the device attempts to generate on the specified channel(s).\nThis attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_CURRENT.\nNIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.\nValid Values: The valid values for this attribute are defined by the values to which the NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE attribute is set.\n',
            'note': 'The channel must be enabled for the specified current level to take effect. Refer to the NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.'
        },
        'lv_property': 'Source:DC Current:Current Level',
        'name': 'CURRENT_LEVEL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150010: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the voltage limit, in volts, that the output cannot exceed when generating the desired current level on the specified channels.\nThis attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_CURRENT and the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY attribute is set to NIDCPOWER_VAL_SYMMETRIC.\nNIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.\nValid Values: The valid values for this attribute are defined by the values to which the NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE attribute is set.\n',
            'note': 'The channel must be enabled for the specified current level to take effect. Refer to the NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.'
        },
        'lv_property': 'Source:DC Current:Voltage Limit',
        'name': 'VOLTAGE_LIMIT',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150011: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the current level range, in amps, for the specified channel(s).\nThe range defines the valid value to which the current level can be set. Use the NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE attribute to enable automatic selection of the current level range.\nThe NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_CURRENT.\nNIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.\nFor valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.\n',
            'note': 'The channel must be enabled for the specified current level range to take effect. Refer to the NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.'
        },
        'lv_property': 'Source:DC Current:Current Level Range',
        'name': 'CURRENT_LEVEL_RANGE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150012: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the voltage limit range, in volts, for the specified channel(s).\nThe range defines the valid values to which the voltage limit can be set. Use the NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE attribute to enable automatic selection of the voltage limit range.\nThe NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_CURRENT.\nNIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.\nFor valid ranges, refer to the Ranges topic for your device in the NI DC Power Supplies and SMUs Help.\n',
            'note': 'The channel must be enabled for the specified voltage limit range to take effect. Refer to the NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.'
        },
        'lv_property': 'Source:DC Current:Voltage Limit Range',
        'name': 'VOLTAGE_LIMIT_RANGE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150013: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSelects either local or remote sensing of the output voltage for the specified channel(s).\nRefer to the Local and Remote Sense topic in the NI DC Power Supplies and SMUs Help for more information about sensing voltage on supported channels and about devices that support local and/or remote sensing.\nDefault Value: The default value is NIDCPOWER_VAL_LOCAL if the device supports local sense. Otherwise, the default and only supported value is NIDCPOWER_VAL_REMOTE.\n'
        },
        'enum': 'Sense',
        'lv_property': 'Measurement:Sense',
        'name': 'SENSE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150014: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether to use a low or high capacitance on the output for the specified channel(s).\nRefer to the NI PXI-4130 Output Capacitance Selection topic in the NI DC Power Supplies and SMUs Help for more information about capacitance.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'OutputCapacitance',
        'lv_property': 'Source:Advanced:Output Capacitance',
        'name': 'OUTPUT_CAPACITANCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150015: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether NI-DCPower automatically selects the voltage level range based on the desired voltage level for the specified channel(s).\nIf you set this attribute to NIDCPOWER_VAL_ON, NI-DCPower ignores any changes you make to the NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE attribute. If you change the NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE attribute from NIDCPOWER_VAL_ON to NIDCPOWER_VAL_OFF, NI-DCPower retains the last value the NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE attribute was set to (or the default value if the attribute was never set) and uses that value as the voltage level range.\nQuery the NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE attribute by using the niDCPower_GetAttributeViInt32 function for information about which range NI-DCPower automatically selects.\nThe NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_VOLTAGE.\nDefault Value: NIDCPOWER_VAL_OFF\n'
        },
        'lv_property': 'Source:DC Voltage:Voltage Level Autorange',
        'name': 'VOLTAGE_LEVEL_AUTORANGE',
        'python_type': 'bool',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150016: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether NI-DCPower automatically selects the current limit range based on the desired current limit for the specified channel(s).\nIf you set this attribute to NIDCPOWER_VAL_ON, NI-DCPower ignores any changes you make to the NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE attribute. If you change this attribute from NIDCPOWER_VAL_ON to NIDCPOWER_VAL_OFF, NI-DCPower retains the last value the NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE attribute was set to (or the default value if the attribute was never set) and uses that value as the current limit range.\nQuery the NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE attribute by using the niDCPower_GetAttributeViInt32 function for information about which range NI-DCPower automatically selects.\nThe NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_VOLTAGE.\nDefault Value: NIDCPOWER_VAL_OFF\n'
        },
        'lv_property': 'Source:DC Voltage:Current Limit Autorange',
        'name': 'CURRENT_LIMIT_AUTORANGE',
        'python_type': 'bool',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150017: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether NI-DCPower automatically selects the current level range based on the desired current level for the specified channels.\nIf you set this attribute to NIDCPOWER_VAL_ON, NI-DCPower ignores any changes you make to the NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE attribute. If you change the NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE attribute from NIDCPOWER_VAL_ON to NIDCPOWER_VAL_OFF, NI-DCPower retains the last value the NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE attribute was set to (or the default value if the attribute was never set) and uses that value as the current level range.\nQuery the NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE attribute by using the niDCPower_GetAttributeViInt32 function for information about which range NI-DCPower automatically selects.\nThe NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_CURRENT.\nDefault Value: NIDCPOWER_VAL_OFF\n'
        },
        'lv_property': 'Source:DC Current:Current Level Autorange',
        'name': 'CURRENT_LEVEL_AUTORANGE',
        'python_type': 'bool',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150018: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether NI-DCPower automatically selects the voltage limit range based on the desired voltage limit for the specified channel(s).\nIf this attribute is set to NIDCPOWER_VAL_ON, NI-DCPower ignores any changes you make to the NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE attribute. If you change the NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE attribute from NIDCPOWER_VAL_ON to NIDCPOWER_VAL_OFF, NI-DCPower retains the last value the NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE attribute was set to (or the default value if the attribute was never set) and uses that value as the voltage limit range.\nQuery the NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE attribute by using the niDCPower_GetAttributeViInt32 function to find out which range NI-DCPower automatically selects.\nThe NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_CURRENT.\nDefault Value: NIDCPOWER_VAL_OFF\n'
        },
        'lv_property': 'Source:DC Current:Voltage Limit Autorange',
        'name': 'VOLTAGE_LIMIT_AUTORANGE',
        'python_type': 'bool',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150020: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the power line frequency for specified channel(s). NI-DCPower uses this value to select a timebase for setting the NIDCPOWER_ATTR_APERTURE_TIME attribute in power line cycles (PLCs).\nin the NI DC Power Supplies and SMUs Help for information about supported devices.\nDefault Value: NIDCPOWER_VAL_60_HERTZ\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Measurement:Power Line Frequency',
        'name': 'POWER_LINE_FREQUENCY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150021: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the behavior of the Start trigger.\nDefault Value: NIDCPOWER_VAL_NONE\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'TriggerType',
        'lv_property': 'Triggers:Start Trigger:Trigger Type',
        'name': 'START_TRIGGER_TYPE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150023: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the input terminal for the Start trigger. Use this attribute only when the NIDCPOWER_ATTR_START_TRIGGER_TYPE attribute is set to NIDCPOWER_VAL_DIGITAL_EDGE.\nYou can specify any valid input terminal for this attribute. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.\nInput terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name,  PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Triggers:Start Trigger:Digital Edge:Input Terminal',
        'name': 'DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString'
    },
    1150024: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the output terminal for exporting the Start trigger.\nRefer to the Device Routes tab in Measurement & Automation Explorer (MAX) for a list of the terminals available on your device.\nOutput terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name,  PXI_Trig0.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Triggers:Start Trigger:Export Output Terminal',
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString'
    },
    1150025: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the number of times a sequence is run after initiation.\nRefer to the Sequence Source Mode topic in the NI DC Power Supplies and SMUs Help for more information about the sequence loop count.\nWhen the NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE attribute is set to VI_FALSE, the NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT attribute is ignored.\nValid Range: 1 to 134217727\nDefault Value: 1\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Advanced:Sequence Loop Count',
        'name': 'SEQUENCE_LOOP_COUNT',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150026: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the behavior of the Sequence Advance trigger.\nDefault Value: NIDCPOWER_VAL_NONE\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'TriggerType',
        'lv_property': 'Triggers:Sequence Advance Trigger:Trigger Type',
        'name': 'SEQUENCE_ADVANCE_TRIGGER_TYPE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150028: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the input terminal for the Sequence Advance trigger. Use this attribute only when the NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE attribute is set to NIDCPOWER_VAL_DIGITAL_EDGE.\nthe NI DC Power Supplies and SMUs Help for information about supported devices.\nYou can specify any valid input terminal for this attribute. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.\nInput terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal',
        'name': 'DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString'
    },
    1150029: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the output terminal for exporting the Sequence Advance trigger.\nRefer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals available on your device.\nOutput terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Triggers:Sequence Advance Trigger:Export Output Terminal',
        'name': 'EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString'
    },
    1150030: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the behavior of the Source trigger.\nDefault Value: NIDCPOWER_VAL_NONE\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'TriggerType',
        'lv_property': 'Triggers:Source Trigger:Trigger Type',
        'name': 'SOURCE_TRIGGER_TYPE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150032: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the input terminal for the Source trigger. Use this attribute only when the NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE attribute is set to NIDCPOWER_VAL_DIGITAL_EDGE.\nYou can specify any valid input terminal for this attribute. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.\nInput terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Triggers:Source Trigger:Digital Edge:Input Terminal',
        'name': 'DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString'
    },
    1150033: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the output terminal for exporting the Source trigger.\nRefer to the Device Routes tab in MAX for a list of the terminals available on your device.\nOutput terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Triggers:Source Trigger:Export Output Terminal',
        'name': 'EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString'
    },
    1150034: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the behavior of the Measure trigger.\nDefault Value: NIDCPOWER_VAL_DIGITAL_EDGE\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'TriggerType',
        'lv_property': 'Triggers:Measure Trigger:Trigger Type',
        'name': 'MEASURE_TRIGGER_TYPE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150036: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the input terminal for the Measure trigger. This attribute is used only when the NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE attribute is set to NIDCPOWER_VAL_DIGITAL_EDGE.\nfor this attribute.\nYou can specify any valid input terminal for this attribute. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.\nInput terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Triggers:Measure Trigger:Digital Edge:Input Terminal',
        'name': 'DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString'
    },
    1150037: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the output terminal for exporting the Measure trigger.\nRefer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals available on your device.\nOutput terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Triggers:Measure Trigger:Export Output Terminal',
        'name': 'EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString'
    },
    1150038: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the behavior of the Sequence Iteration Complete event.\nDefault Value: NIDCPOWER_VAL_ACTIVE_HIGH\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'Polarity',
        'lv_property': 'Events:Sequence Iteration Complete Event:Pulse:Polarity',
        'name': 'SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150039: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the width of the Sequence Iteration Complete event, in seconds.\nThe minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns.\nThe maximum event pulse width value for all devices is 1.6 microseconds.\nthe NI DC Power Supplies and SMUs Help for information about supported devices.\nValid Values: 1.5e-7 to 1.6e-6 seconds\nDefault Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Events:Sequence Iteration Complete Event:Pulse:Width',
        'name': 'SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150040: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the output terminal for exporting the Sequence Iteration Complete event.\nOutput terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Events:Sequence Iteration Complete Event:Output Terminal',
        'name': 'SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString'
    },
    1150041: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the behavior of the Source Complete event.\nDefault Value: NIDCPOWER_VAL_ACTIVE_HIGH\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'Polarity',
        'lv_property': 'Events:Source Complete Event:Pulse:Polarity',
        'name': 'SOURCE_COMPLETE_EVENT_PULSE_POLARITY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150042: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the width of the Source Complete event, in seconds.\nThe minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns.\nThe maximum event pulse width value for all devices is 1.6 microseconds\nValid Values: 1.5e-7 to 1.6e-6 seconds\nDefault Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Events:Source Complete Event:Pulse:Width',
        'name': 'SOURCE_COMPLETE_EVENT_PULSE_WIDTH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150043: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the output terminal for exporting the Source Complete event.\nOutput terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Events:Source Complete Event:Output Terminal',
        'name': 'SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString'
    },
    1150044: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the behavior of the Measure Complete event.\nDefault Value: NIDCPOWER_VAL_ACTIVE_HIGH\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'Polarity',
        'lv_property': 'Events:Measure Complete Event:Pulse:Polarity',
        'name': 'MEASURE_COMPLETE_EVENT_PULSE_POLARITY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150045: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the width of the Measure Complete event, in seconds.\nThe minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns.\nThe maximum event pulse width value for all devices is 1.6 microseconds.\nValid Values: 1.5e-7 to 1.6e-6\nDefault Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Events:Measure Complete Event:Pulse:Width',
        'name': 'MEASURE_COMPLETE_EVENT_PULSE_WIDTH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150046: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nSpecifies the amount of time to delay the generation of the Measure Complete event, in seconds.\nValid Values: 0 to 167 seconds\nDefault Value: The NI PXI-4132 and NI PXIe-4140/4141/4142/4143/4144/4145/4154 supports values from  0 seconds to 167 seconds.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Events:Measure Complete Event:Event Delay',
        'name': 'MEASURE_COMPLETE_EVENT_DELAY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150047: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the output terminal for exporting the Measure Complete event.\nOutput terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Events:Measure Complete Event:Output Terminal',
        'name': 'MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString'
    },
    1150048: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the behavior of the Sequence Engine Done event.\nDefault Value: NIDCPOWER_VAL_ACTIVE_HIGH\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'Polarity',
        'lv_property': 'Events:Sequence Engine Done Event:Pulse:Polarity',
        'name': 'SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150049: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the width of the Sequence Engine Done event, in seconds.\nThe minimum event pulse width value for PXI devices is 150 ns, and the minimum event pulse width value for PXI Express devices is 250 ns.\nThe maximum event pulse width value for all devices is 1.6 microseconds.\nValid Values: 1.5e-7 to 1.6e-6 seconds\nDefault Value: The default value for PXI devices is 150 ns. The default value for PXI Express devices is 250 ns.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Events:Sequence Engine Done Event:Pulse:Width',
        'name': 'SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150050: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the output terminal for exporting the Sequence Engine Done Complete event.\nOutput terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Events:Sequence Engine Done Event:Output Terminal',
        'name': 'SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString'
    },
    1150051: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nDetermines when, in seconds, the device generates the Source Complete event, potentially starting a measurement if the NIDCPOWER_ATTR_MEASURE_WHEN attribute is set to NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE.\nRefer to the Single Point Source Mode and Sequence Source Mode topics for more information.\nValid Values: 0 to 167 seconds\nDefault Value: 0.01667 seconds\n',
            'note': '\n\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n\n'
        },
        'lv_property': 'Source:Advanced:Source Delay',
        'name': 'SOURCE_DELAY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150054: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether to run a single output point or a sequence. Refer to the Single Point Source Mode and Sequence Source Mode topics in the NI DC Power Supplies and SMUs Help for more information about source modes.\nDefault value: NIDCPOWER_VAL_SINGLE_POINT\n'
        },
        'enum': 'SourceMode',
        'lv_property': 'Source:Source Mode',
        'name': 'SOURCE_MODE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150055: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the auto-zero method to use on the device.\nRefer to the NI PXI-4132 Measurement Configuration and Timing and Auto Zero topics for more information about how to configure your measurements.\nDefault Value: The default value for the NI PXI-4132 is NIDCPOWER_VAL_ON. The default value for all other devices is NIDCPOWER_VAL_OFF, which is the only supported value for these devices.\n'
        },
        'enum': 'AutoZero',
        'lv_property': 'Measurement:Auto Zero',
        'name': 'AUTO_ZERO',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150056: {
        'access': 'read only',
        'documentation': {
            'description': 'Returns the number of measurements acquired that have not been fetched yet.'
        },
        'lv_property': 'Measurement:Fetch Backlog',
        'name': 'FETCH_BACKLOG',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150057: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies when the measure unit should acquire measurements. Unless this attribute is configured to NIDCPOWER_VAL_ON_MEASURE_TRIGGER, the NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE attribute is ignored.\nRefer to the Acquiring Measurements topic in the NI DC Power Supplies and SMUs Help for more information about how to configure your measurements.\nDefault Value: If the NIDCPOWER_ATTR_SOURCE_MODE attribute is set to NIDCPOWER_VAL_SINGLE_POINT, the default value is NIDCPOWER_VAL_ON_DEMAND. This value supports only the niDCPower_Measure function and niDCPower_MeasureMultiple function. If the NIDCPOWER_ATTR_SOURCE_MODE attribute is set to NIDCPOWER_VAL_SEQUENCE, the default value is NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE. This value supports only the niDCPower_FetchMultiple function.\n'
        },
        'enum': 'MeasureWhen',
        'lv_property': 'Measurement:Advanced:Measure When',
        'name': 'MEASURE_WHEN',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150058: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the measurement aperture time for the channel configuration. Aperture time is specified in the units set by the NIDCPOWER_ATTR_APERTURE_TIME_UNITS attribute.\nRefer to the Aperture Time topic in the NI DC Power Supplies and SMUs Help for more information about how to configure your measurements and for information about valid values.\nDefault Value: 0.01666666 seconds\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Measurement:Aperture Time',
        'name': 'APERTURE_TIME',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150059: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the units of the NIDCPOWER_ATTR_APERTURE_TIME attribute for the channel configuration.\nRefer to the Aperture Time topic in the NI DC Power Supplies and SMUs Help for more information about how to configure your measurements and for information about valid values.\nDefault Value: NIDCPOWER_VAL_SECONDS\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'ApertureTimeUnits',
        'lv_property': 'Measurement:Aperture Time Units',
        'name': 'APERTURE_TIME_UNITS',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150060: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether the output relay is connected (closed) or disconnected (open). The NIDCPOWER_ATTR_OUTPUT_ENABLED attribute does not change based on this attribute; they are independent of each other.\nabout supported devices.\nSet this attribute to VI_FALSE to disconnect the output terminal from the output.\nto the output terminal might discharge unless the relay is disconnected. Excessive connecting and disconnecting of the output can cause premature wear on the relay.\nDefault Value: VI_TRUE\n',
            'note': 'Only disconnect the output when disconnecting is necessary for your application. For example, a battery connected'
        },
        'lv_property': 'Source:Output Connected',
        'name': 'OUTPUT_CONNECTED',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1150061: {
        'access': 'read-write',
        'documentation': {
            'description': "\nSpecifies the output resistance that the device attempts to generate for the specified channel(s). This attribute is available only when you set the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute on a support device. Refer to a supported device's topic about output resistance for more information about selecting an output resistance.\nabout supported devices.\nDefault Value: 0.0\n",
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Output Resistance',
        'name': 'OUTPUT_RESISTANCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150062: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the transient response. Refer to the Transient Response topic in the NI DC Power Supplies and SMUs Help for more information about transient response.\nDefault Value: NIDCPOWER_VAL_NORMAL\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'TransientResponse',
        'lv_property': 'Source:Transient Response',
        'name': 'TRANSIENT_RESPONSE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150063: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies how many measurements compose a measure record. When this attribute is set to a value greater than 1, the NIDCPOWER_ATTR_MEASURE_WHEN attribute must be set to NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE or NIDCPOWER_VAL_ON_MEASURE_TRIGGER.\nValid Values: 1 to 16,777,216\nDefault Value: 1\n',
            'note': '\nThis attribute is not available in a session involving multiple channels.\n'
        },
        'lv_property': 'Measurement:Measure Record Length',
        'name': 'MEASURE_RECORD_LENGTH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150064: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether to take continuous measurements. Call the niDCPower_AbortWithChannels function to stop continuous measurements. When this attribute is set to VI_FALSE and the NIDCPOWER_ATTR_SOURCE_MODE attribute is set to NIDCPOWER_VAL_SINGLE_POINT, the NIDCPOWER_ATTR_MEASURE_WHEN attribute must be set to NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE or NIDCPOWER_VAL_ON_MEASURE_TRIGGER. When this attribute is set to VI_FALSE and the NIDCPOWER_ATTR_SOURCE_MODE attribute is set to NIDCPOWER_VAL_SEQUENCE, the NIDCPOWER_ATTR_MEASURE_WHEN attribute must be set to NIDCPOWER_VAL_ON_MEASURE_TRIGGER.\nDefault Value: VI_TRUE\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device. This attribute is not available in a session involving multiple channels.\n'
        },
        'lv_property': 'Measurement:Measure Record Length Is Finite',
        'name': 'MEASURE_RECORD_LENGTH_IS_FINITE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1150065: {
        'access': 'read only',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nQueries the amount of time, in seconds, between between the start of two consecutive measurements in a measure record. Only query this attribute after the desired measurement settings are committed.\ntwo measurements and the rest would differ.\n',
            'note': 'This attribute is not available when Auto Zero is configured to Once because the amount of time between the first'
        },
        'lv_property': 'Measurement:Measure Record Delta Time',
        'name': 'MEASURE_RECORD_DELTA_TIME',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150066: {
        'access': 'read-write',
        'documentation': {
            'description': '\nDetermines the relative weighting of samples in a measurement. Refer to the NI PXIe-4140/4141 DC Noise Rejection, NI PXIe-4142/4143 DC Noise Rejection, or NI PXIe-4144/4145 DC Noise Rejection topic in the NI DC Power Supplies and SMUs Help for more information about noise rejection.\nDefault Value: NIDCPOWER_VAL_NORMAL\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'DCNoiseRejection',
        'lv_property': 'Measurement:Advanced:DC Noise Rejection',
        'name': 'DC_NOISE_REJECTION',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150067: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThe frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This attribute takes effect when the channel is in Constant Voltage mode.\nDefault Value: Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Custom Transient Response:Voltage:Gain Bandwidth',
        'name': 'VOLTAGE_GAIN_BANDWIDTH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150068: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThe frequency at which a pole-zero pair is added to the system when the channel is in Constant Voltage mode.\nDefault value: Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Custom Transient Response:Voltage:Compensation Frequency',
        'name': 'VOLTAGE_COMPENSATION_FREQUENCY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150069: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThe ratio of the pole frequency to the zero frequency when the channel is in Constant Voltage mode.\nDefault value: Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Custom Transient Response:Voltage:Pole-Zero Ratio',
        'name': 'VOLTAGE_POLE_ZERO_RATIO',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150070: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThe frequency at which the unloaded loop gain extrapolates to 0 dB in the absence of additional poles and zeroes. This attribute takes effect when the channel is in Constant Current mode.\nDefault Value: Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Custom Transient Response:Current:Gain Bandwidth',
        'name': 'CURRENT_GAIN_BANDWIDTH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150071: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThe frequency at which a pole-zero pair is added to the system when the channel is in Constant Current mode.\nDefault Value: Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Custom Transient Response:Current:Compensation Frequency',
        'name': 'CURRENT_COMPENSATION_FREQUENCY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150072: {
        'access': 'read-write',
        'documentation': {
            'description': '\nThe ratio of the pole frequency to the zero frequency when the channel is in Constant Current mode.\nDefault Value: Determined by the value of the NIDCPOWER_VAL_NORMAL setting of the NIDCPOWER_ATTR_TRANSIENT_RESPONSE attribute.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Custom Transient Response:Current:Pole-Zero Ratio',
        'name': 'CURRENT_POLE_ZERO_RATIO',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150073: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether the values calculated during self-calibration should be written to hardware to be used until the next self-calibration or only used until the niDCPower_ResetDevice function is called or the machine is powered down.\nThis attribute affects the behavior of the niDCPower_CalSelfCalibrate function. When set to NIDCPOWER_VAL_KEEP_IN_MEMORY, the values calculated by the niDCPower_CalSelfCalibrate function are used in the existing session, as well as in all further sessions until you call the niDCPower_ResetDevice function or restart the machine. When you set this property to NIDCPOWER_VAL_WRITE_TO_EEPROM, the values calculated by the niDCPower_CalSelfCalibrate function are written to hardware and used in the existing session and in all subsequent sessions until another call to the niDCPower_CalSelfCalibrate function is made.\nabout supported devices.\nDefault Value: NIDCPOWER_VAL_KEEP_IN_MEMORY\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'SelfCalibrationPersistence',
        'lv_property': 'Advanced:Self-Calibration Persistence',
        'name': 'SELF_CALIBRATION_PERSISTENCE',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViInt32'
    },
    1150074: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the advanced sequence to configure or generate.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Advanced:Active Advanced Sequence',
        'name': 'ACTIVE_ADVANCED_SEQUENCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString'
    },
    1150075: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the advanced sequence step to configure.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Advanced:Active Advanced Sequence Step',
        'name': 'ACTIVE_ADVANCED_SEQUENCE_STEP',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt64'
    },
    1150077: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the number of samples that the active channel measurement buffer can hold.\nThe default value is the maximum number of samples that a device is capable of recording in one second.\nValid Values: 1000 to 2147483647\nDefault Value: Varies by device. Refer to Supported Attributes by Device topic in the NI DC Power Supplies and SMUs Help for more information about default values.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Measurement:Advanced:Measure Buffer Size',
        'name': 'MEASURE_BUFFER_SIZE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150078: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether a sequence should repeat indefinitely.\nRefer to the Sequence Source Mode topic in the NI DC Power Supplies and SMUs Help for more information about infinite sequencing.\nWhen the NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE attribute is set to VI_FALSE, the NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT attribute is ignored.\nDefault Value: VI_TRUE\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Advanced:Sequence Loop Count Is Finite',
        'name': 'SEQUENCE_LOOP_COUNT_IS_FINITE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1150080: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the pulse current limit, in amps, that the output cannot exceed when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse.\nThis attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.\nValid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE attribute.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Pulse Voltage:Pulse Voltage Level',
        'name': 'PULSE_VOLTAGE_LEVEL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150081: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the pulse current limit, in amps, that the output cannot exceed when generating the desired pulse voltage on the specified channel(s) during the on phase of a pulse.\nThis attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE and the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY attribute is set to NIDCPOWER_VAL_SYMMETRIC.\nValid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE attribute.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Pulse Voltage:Pulse Current Limit',
        'name': 'PULSE_CURRENT_LIMIT',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150082: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the pulse bias voltage level, in volts, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.\nThis attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.\nValid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE attribute.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Pulse Voltage:Pulse Bias Voltage Level',
        'name': 'PULSE_BIAS_VOLTAGE_LEVEL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150083: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the pulse bias current limit, in amps, that the output cannot exceed when generating the desired pulse bias voltage on the specified channel(s) during the off phase of a pulse.\nThis attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.\nValid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE property.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Pulse Voltage:Pulse Bias Current Limit',
        'name': 'PULSE_BIAS_CURRENT_LIMIT',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150084: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the pulse voltage level range, in volts, for the specified channel(s).\nThe range defines the valid values at which you can set the pulse voltage level and pulse bias voltage level.\nThis attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.\nFor valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Pulse Voltage:Pulse Voltage Level Range',
        'name': 'PULSE_VOLTAGE_LEVEL_RANGE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150085: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the pulse current limit range, in amps, for the specified channel(s).\nThe range defines the valid values to which you can set the pulse current limit and pulse bias current limit.\nThis attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.\nFor valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Pulse Voltage:Pulse Current Limit Range',
        'name': 'PULSE_CURRENT_LIMIT_RANGE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150086: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the pulse current level, in amps, that the device attempts to generate on the specified channel(s) during the on phase of a pulse.\nThis attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.\nValid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE attribute.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Pulse Current:Pulse Current Level',
        'name': 'PULSE_CURRENT_LEVEL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150087: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired pulse current on the specified channel(s) during the on phase of a pulse.\nThis attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT and the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY attribute is set to NIDCPOWER_VAL_SYMMETRIC.\nValid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE attribute.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Pulse Current:Pulse Voltage Limit',
        'name': 'PULSE_VOLTAGE_LIMIT',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150088: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the pulse bias current level, in amps, that the device attempts to generate on the specified channel(s) during the off phase of a pulse.\nThis attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.\nValid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE attribute.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Pulse Current:Pulse Bias Current Level',
        'name': 'PULSE_BIAS_CURRENT_LEVEL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150089: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the pulse voltage limit, in volts, that the output cannot exceed when generating the desired current on the specified channel(s) during the off phase of a pulse.\nThis attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.\nValid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE attribute.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Pulse Current:Pulse Bias Voltage Limit',
        'name': 'PULSE_BIAS_VOLTAGE_LIMIT',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150090: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the pulse current level range, in amps, for the specified channel(s).\nThe range defines the valid values to which you can set the pulse current level and pulse bias current level.\nThis attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.\nFor valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Pulse Current:Pulse Current Level Range',
        'name': 'PULSE_CURRENT_LEVEL_RANGE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150091: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the pulse voltage limit range, in volts, for the specified channel(s).\nThe range defines the valid values to which you can set the pulse voltage limit and pulse bias voltage limit.\nThis attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.\nFor valid ranges, refer to the ranges topic for your device in the NI DC Power Supplies and SMUs Help.\n',
            'note': 'The channel must be enabled for the specified current limit to take effect. Refer to the NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.'
        },
        'lv_property': 'Source:Pulse Current:Pulse Voltage Limit Range',
        'name': 'PULSE_VOLTAGE_LIMIT_RANGE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150092: {
        'access': 'read-write',
        'documentation': {
            'description': '\nDetermines when, in seconds, the device generates the Pulse Complete event after generating the off level of a pulse.\nValid Values: 0 to 167 seconds\nDefault Value: 16.67 milliseconds\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Advanced:Pulse Bias Delay',
        'name': 'PULSE_BIAS_DELAY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150093: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nDetermines the length, in seconds, of the on phase of a pulse.\nValid Values: 10 microseconds to 167 seconds\nDefault Value: 34 milliseconds\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Advanced:Pulse On Time',
        'name': 'PULSE_ON_TIME',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150094: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nDetermines the length, in seconds, of the off phase of a pulse.\nValid Values: 10 microseconds to 167 seconds\nDefault Value: 34 milliseconds\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Advanced:Pulse Off Time',
        'name': 'PULSE_OFF_TIME',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150095: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the behavior of the Pulse trigger.\nDefault Value: NIDCPOWER_VAL_NONE\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'TriggerType',
        'lv_property': 'Triggers:Pulse Trigger:Trigger Type',
        'name': 'PULSE_TRIGGER_TYPE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150097: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the input terminal for the Pulse trigger. This attribute is used only when the NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE attribute is set to digital edge.\nYou can specify any valid input terminal for this attribute. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.\nInput terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Triggers:Pulse Trigger:Digital Edge:Input Terminal',
        'name': 'DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString'
    },
    1150098: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the output terminal for exporting the Pulse trigger.\nRefer to the Device Routes tab in Measurement & Automation Explorer for a list of the terminals available on your device.\nOutput terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Triggers:Pulse Trigger:Export Output Terminal',
        'name': 'EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString'
    },
    1150099: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the output terminal for exporting the Pulse Complete event.\nOutput terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.\nDefault Value:The default value for PXI Express devices is 250 ns.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Events:Pulse Complete Event:Output Terminal',
        'name': 'PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString'
    },
    1150100: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the behavior of the Pulse Complete event.\nDefault Value: NIDCPOWER_VAL_ACTIVE_HIGH\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'Polarity',
        'lv_property': 'Events:Pulse Complete Event:Pulse:Polarity',
        'name': 'PULSE_COMPLETE_EVENT_PULSE_POLARITY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150101: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the width of the Pulse Complete event, in seconds.\nThe minimum event pulse width value for PXI Express devices is 250 ns.\nThe maximum event pulse width value for PXI Express devices is 1.6 microseconds.\nDefault Value: The default value for PXI Express devices is 250 ns.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Events:Pulse Complete Event:Pulse:Width',
        'name': 'PULSE_COMPLETE_EVENT_PULSE_WIDTH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150102: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the output terminal for exporting the Ready For Pulse Trigger event.\nOutput terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Events:Ready For Pulse Trigger Event:Output Terminal',
        'name': 'READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString'
    },
    1150103: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the behavior of the Ready For Pulse Trigger event.\nDefault Value: NIDCPOWER_VAL_ACTIVE_HIGH\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'Polarity',
        'lv_property': 'Events:Ready For Pulse Trigger Event:Pulse:Polarity',
        'name': 'READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150104: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the width of the Ready For Pulse Trigger event, in seconds.\nThe minimum event pulse width value for PXI Express devices is 250 ns.\nThe maximum event pulse width value for all devices is 1.6 microseconds.\nDefault Value: The default value for PXI Express devices is 250 ns\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Events:Ready For Pulse Trigger Event:Pulse:Width',
        'name': 'READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150105: {
        'access': 'read only',
        'documentation': {
            'description': '\nIndicates whether the safety interlock circuit is open.\nRefer to the Safety Interlock topic in the NI DC Power Supplies and SMUs Help for more information about the safety interlock circuit.\nabout supported devices.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Advanced:Interlock Input Open',
        'name': 'INTERLOCK_INPUT_OPEN',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViBoolean'
    },
    1150152: {
        'access': 'read only',
        'documentation': {
            'description': 'Contains the serial number for the device you are currently using.'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Serial Number',
        'name': 'SERIAL_NUMBER',
        'supported_rep_caps': [
            'instruments'
        ],
        'type': 'ViString'
    },
    1150184: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether compliance limits for current generation and voltage\ngeneration for the device are applied symmetrically about 0 V and 0 A or\nasymmetrically with respect to 0 V and 0 A.\nWhen set to NIDCPOWER_VAL_SYMMETRIC, voltage limits and current limits are set\nusing a single property with a positive value. The resulting range is\nbounded by this positive value and its opposite.\nWhen set to NIDCPOWER_VAL_ASYMMETRIC, you must separately set a limit high and a\nlimit low using distinct properties.\nFor asymmetric limits, the range bounded by the limit high and limit low\nmust include zero.\n**Default Value:** Symmetric\n**Related Topics:**\nCompliance;\nRanges;\nChanging Ranges;\nOverranging\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'ComplianceLimitSymmetry',
        'lv_property': 'Source:Advanced:Compliance Limit Symmetry',
        'name': 'COMPLIANCE_LIMIT_SYMMETRY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150185: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the maximum voltage, in volts, that the output can produce\nwhen generating the desired current on the specified channel(s).\nThis attribute is applicable only if the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY attribute is set to\nNIDCPOWER_VAL_ASYMMETRIC and the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_CURRENT.\nYou must also specify a NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW to complete the asymmetric\nrange.\n**Valid Values:** [1% of NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE, NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE]\nThe range bounded by the limit high and limit low must include zero.\n**Default Value:** Search ni.com for Supported Attributes by Device for the default value by device.\n**Related Topics:**\nRanges;\nChanging Ranges;\nOverranging\n',
            'note': '\nThe limit may be extended beyond the selected limit range if the\nNIDCPOWER_ATTR_OVERRANGING_ENABLED attribute is\nset to VI_TRUE.\n'
        },
        'lv_property': 'Source:DC Current:Voltage Limit High',
        'name': 'VOLTAGE_LIMIT_HIGH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150186: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the minimum voltage, in volts, that the output can produce\nwhen generating the desired current on the specified channel(s).\nThis attribute is applicable only if the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY attribute is set to\nNIDCPOWER_VAL_ASYMMETRIC and the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_CURRENT.\nYou must also specify a NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH to complete the asymmetric\nrange.\n**Valid Values:** [-NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE, -1% of NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE]\nThe range bounded by the limit high and limit low must include zero.\n**Default Value:** Search ni.com for Supported Attributes by Device for the default value by device.\n**Related Topics:**\nRanges;\nChanging Ranges;\nOverranging\n',
            'note': '\nThe limit may be extended beyond the selected limit range if the\nNIDCPOWER_ATTR_OVERRANGING_ENABLED attribute is\nset to VI_TRUE.\n'
        },
        'lv_property': 'Source:DC Current:Voltage Limit Low',
        'name': 'VOLTAGE_LIMIT_LOW',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150187: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the maximum current, in amps, that the output can produce when\ngenerating the desired voltage on the specified channel(s).\nThis attribute is applicable only if the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY attribute is set to\nNIDCPOWER_VAL_ASYMMETRIC and the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_VOLTAGE.\nYou must also specify a NIDCPOWER_ATTR_CURRENT_LIMIT_LOW to complete the asymmetric\nrange.\n**Valid Values:** [1% of NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE, NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE]\nThe range bounded by the limit high and limit low must include zero.\n**Default Value:** Search ni.com for Supported Attributes by Device for the default value by device.\n**Related Topics:**\nRanges;\nChanging Ranges;\nOverranging\n',
            'note': '\nThe limit may be extended beyond the selected limit range if the\nNIDCPOWER_ATTR_OVERRANGING_ENABLED attribute is\nset to VI_TRUE.\n'
        },
        'lv_property': 'Source:DC Voltage:Current Limit High',
        'name': 'CURRENT_LIMIT_HIGH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150188: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the minimum current, in amps, that the output can produce when\ngenerating the desired voltage on the specified channel(s).\nThis attribute is applicable only if the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY attribute is set to\nNIDCPOWER_VAL_ASYMMETRIC and the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_VOLTAGE.\nYou must also specify a NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH to complete the asymmetric\nrange.\n**Valid Values:** [-NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE, -1% of NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE]\nThe range bounded by the limit high and limit low must include zero.\n**Default Value:** Search ni.com for Supported Attributes by Device for the default value by device.\n**Related Topics:**\nRanges;\nChanging Ranges;\nOverranging\n',
            'note': '\nThe limit may be extended beyond the selected limit range if the\nNIDCPOWER_ATTR_OVERRANGING_ENABLED attribute is\nset to VI_TRUE.\n'
        },
        'lv_property': 'Source:DC Voltage:Current Limit Low',
        'name': 'CURRENT_LIMIT_LOW',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150189: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the maximum voltage, in volts, that the output can produce\nwhen generating the desired pulse current on the specified channel(s)\nduring the *on* phase of a pulse.\nThis attribute is applicable only if the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY attribute is set to\nNIDCPOWER_VAL_ASYMMETRIC and the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.\nYou must also specify a NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW to complete the asymmetric\nrange.\n**Valid Values:** [1% of NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE, NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE]\nThe range bounded by the limit high and limit low must include zero.\n**Default Value:** Search ni.com for Supported Attributes by Device for the default value by device.\n**Related Topics:**\nRanges;\nChanging Ranges;\nOverranging\n',
            'note': '\nThe limit may be extended beyond the selected limit range if the\nNIDCPOWER_ATTR_OVERRANGING_ENABLED attribute is\nset to VI_TRUE or if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to a\npulsing function.\n'
        },
        'lv_property': 'Source:Pulse Current:Pulse Voltage Limit High',
        'name': 'PULSE_VOLTAGE_LIMIT_HIGH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150190: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the minimum voltage, in volts, that the output can produce\nwhen generating the desired pulse current on the specified channel(s)\nduring the *on* phase of a pulse.\nThis attribute is applicable only if the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY attribute is set to\nNIDCPOWER_VAL_ASYMMETRIC and the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.\nYou must also specify a NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH to complete the\nasymmetric range.\n**Valid Values:** [-NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE, -1% of NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE]\nThe range bounded by the limit high and limit low must include zero.\n**Default Value:** Search ni.com for Supported Attributes by Device for the default value by device.\n**Related Topics:**\nRanges;\nChanging Ranges;\nOverranging\n',
            'note': '\nThe limit may be extended beyond the selected limit range if the\nNIDCPOWER_ATTR_OVERRANGING_ENABLED attribute is\nset to VI_TRUE or if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to a\npulsing function.\n'
        },
        'lv_property': 'Source:Pulse Current:Pulse Voltage Limit Low',
        'name': 'PULSE_VOLTAGE_LIMIT_LOW',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150191: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the maximum voltage, in volts, that the output can produce\nwhen generating the desired pulse current on the specified channel(s)\nduring the *off* phase of a pulse.\nThis attribute is applicable only if the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY attribute is set to\nNIDCPOWER_VAL_ASYMMETRIC and the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.\nYou must also specify a NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW to complete the\nasymmetric range.\n**Valid Values:** [1% of NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE, NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE]\nThe range bounded by the limit high and limit low must include zero.\n**Default Value:** Search ni.com for Supported Attributes by Device for the default value by device.\n**Related Topics:**\nRanges;\nChanging Ranges;\nOverranging\n',
            'note': '\nThe limit may be extended beyond the selected limit range if the\nNIDCPOWER_ATTR_OVERRANGING_ENABLED attribute is\nset to VI_TRUE or if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to a\npulsing function.\n'
        },
        'lv_property': 'Source:Pulse Current:Pulse Bias Voltage Limit High',
        'name': 'PULSE_BIAS_VOLTAGE_LIMIT_HIGH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150192: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the minimum voltage, in volts, that the output can produce\nwhen generating the desired pulse current on the specified channel(s)\nduring the *off* phase of a pulse.\nThis attribute is applicable only if the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY attribute is set to\nNIDCPOWER_VAL_ASYMMETRIC and the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_CURRENT.\nYou must also specify a NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH to complete the\nasymmetric range.\n**Valid Values:** [-NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE, -1% of NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE]\nThe range bounded by the limit high and limit low must include zero.\n**Default Value:** Search ni.com for Supported Attributes by Device for the default value by device.\n**Related Topics:**\nRanges;\nChanging Ranges;\nOverranging\n',
            'note': '\nThe limit may be extended beyond the selected limit range if the\nNIDCPOWER_ATTR_OVERRANGING_ENABLED attribute is\nset to VI_TRUE or if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to a\npulsing function.\n'
        },
        'lv_property': 'Source:Pulse Current:Pulse Bias Voltage Limit Low',
        'name': 'PULSE_BIAS_VOLTAGE_LIMIT_LOW',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150193: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the maximum current, in amps, that the output can produce when\ngenerating the desired pulse voltage on the specified channel(s) during\nthe *on* phase of a pulse.\nThis attribute is applicable only if the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY attribute is set to\nNIDCPOWER_VAL_ASYMMETRIC and the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.\nYou must also specify a NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW to complete the asymmetric\nrange.\n**Valid Values:** [1% of NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE, NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE]\nThe range bounded by the limit high and limit low must include zero.\n**Default Value:** Search ni.com for Supported Attributes by Device for the default value by device.\n**Related Topics:**\nRanges;\nChanging Ranges;\nOverranging\n',
            'note': '\nThe limit may be extended beyond the selected limit range if the\nNIDCPOWER_ATTR_OVERRANGING_ENABLED attribute is\nset to VI_TRUE or if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to a\npulsing function.\n'
        },
        'lv_property': 'Source:Pulse Voltage:Pulse Current Limit High',
        'name': 'PULSE_CURRENT_LIMIT_HIGH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150194: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the minimum current, in amps, that the output can produce when\ngenerating the desired pulse voltage on the specified channel(s) during\nthe *on* phase of a pulse.\nThis attribute is applicable only if the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY attribute is set to\nNIDCPOWER_VAL_ASYMMETRIC and the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.\nYou must also specify a NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH to complete the\nasymmetric range.\n**Valid Values:** [-NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE, -1% of NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE]\nThe range bounded by the limit high and limit low must include zero.\n**Default Value:** Search ni.com for Supported Attributes by Device for the default value by device.\n**Related Topics:**\nRanges;\nChanging Ranges;\nOverranging\n',
            'note': '\nThe limit may be extended beyond the selected limit range if the\nNIDCPOWER_ATTR_OVERRANGING_ENABLED attribute is\nset to VI_TRUE or if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to a\npulsing function.\n'
        },
        'lv_property': 'Source:Pulse Voltage:Pulse Current Limit Low',
        'name': 'PULSE_CURRENT_LIMIT_LOW',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150195: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the maximum current, in amps, that the output can produce when\ngenerating the desired pulse voltage on the specified channel(s) during\nthe *off* phase of a pulse.\nThis attribute is applicable only if the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY attribute is set to\nNIDCPOWER_VAL_ASYMMETRIC and the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.\nYou must also specify a NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW to complete the\nasymmetric range.\n**Valid Values:** [1% of NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE, NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE]\nThe range bounded by the limit high and limit low must include zero.\n**Default Value:** Search ni.com for Supported Attributes by Device for the default value by device.\n**Related Topics:**\nRanges;\nChanging Ranges;\nOverranging\n',
            'note': '\nThe limit may be extended beyond the selected limit range if the\nNIDCPOWER_ATTR_OVERRANGING_ENABLED attribute is\nset to VI_TRUE or if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to a\npulsing function.\n'
        },
        'lv_property': 'Source:Pulse Voltage:Pulse Bias Current Limit High',
        'name': 'PULSE_BIAS_CURRENT_LIMIT_HIGH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150196: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the minimum current, in amps, that the output can produce when\ngenerating the desired pulse voltage on the specified channel(s) during\nthe *off* phase of a pulse.\nThis attribute is applicable only if the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY attribute is set to\nNIDCPOWER_VAL_ASYMMETRIC and the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_PULSE_VOLTAGE.\nYou must also specify a NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH to complete the\nasymmetric range.\n**Valid Values:** [-NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE, -1% of NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE]\nThe range bounded by the limit high and limit low must include zero.\n**Default Value:** Search ni.com for Supported Attributes by Device for the default value by device.\n**Related Topics:**\nRanges;\nChanging Ranges;\nOverranging\n',
            'note': '\nThe limit may be extended beyond the selected limit range if the\nNIDCPOWER_ATTR_OVERRANGING_ENABLED attribute is\nset to VI_TRUE or if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to a\npulsing function.\n'
        },
        'lv_property': 'Source:Pulse Voltage:Pulse Bias Current Limit Low',
        'name': 'PULSE_BIAS_CURRENT_LIMIT_LOW',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150198: {
        'access': 'read-write',
        'name': 'SEQUENCE_STEP_DELTA_TIME',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150199: {
        'access': 'read-write',
        'name': 'SEQUENCE_STEP_DELTA_TIME_ENABLED',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1150205: {
        'access': 'read only',
        'documentation': {
            'description': '\nReturns the power, in watts, the device is sourcing on each active channel if the NIDCPOWER_ATTR_POWER_ALLOCATION_MODE attribute is set to NIDCPOWER_VAL_POWER_ALLOCATION_MODE_AUTOMATIC or NIDCPOWER_VAL_POWER_ALLOCATION_MODE_MANUAL.\n\n Valid Values: [0, device per-channel maximum power]\n\n Default Value: Refer to the Supported Attributes by Device topic for the default value by device.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n\n This attribute returns -1 when the NIDCPOWER_ATTR_POWER_ALLOCATION_MODE attribute is set to NIDCPOWER_VAL_POWER_ALLOCATION_MODE_DISABLED.\n\n'
        },
        'lv_property': 'Source:Advanced:Actual Power Allocation',
        'name': 'ACTUAL_POWER_ALLOCATION',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150206: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the power, in watts, to request the device to source from each active channel.\n This attribute defines the power to source from the device only if the NIDCPOWER_ATTR_POWER_ALLOCATION_MODE attribute is set to NIDCPOWER_VAL_POWER_ALLOCATION_MODE_MANUAL.\n\n The power you request with this attribute may be incompatible with the power a given source configuration requires or the power the device can provide:\n If the requested power is less than the power required for the source configuration, the device does not exceed the requested power, and NI-DCPower returns an error.\n If the requested power is greater than the maximum per-channel or overall sourcing power, the device does not exceed the allowed power, and NI-DCPower returns an error.\n\nValid Values: [0, device per-channel maximum power]\n Default Value: Refer to the Supported Attributes by Device topic for the default value by device.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Advanced:Requested Power Allocation',
        'name': 'REQUESTED_POWER_ALLOCATION',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150207: {
        'access': 'read-write',
        'documentation': {
            'description': '\nDetermines whether the device sources the power its source configuration requires or a specific wattage you request; determines whether NI-DCPower proactively checks that this sourcing power is within the maximum per-channel and overall sourcing power of the device.\n\n When this attribute configures NI-DCPower to perform a sourcing power check, a device is not permitted to source power in excess of its maximum per-channel or overall sourcing power. If the check determines a source configuration or power request would require the device to do so, NI-DCPower returns an error.\n\n When this attribute does not configure NI-DCPower to perform a sourcing power check, a device can attempt to fulfill source configurations that would require it to source power in excess of its maximum per-channel or overall sourcing power and may shut down to prevent damage.\n\n Default Value: Refer to the Supported Attributes by Device topic for the default value by device.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device. Devices that do not support this attribute behave as if this attribute were set to NIDCPOWER_VAL_POWER_ALLOCATION_MODE_DISABLED.\n\n'
        },
        'enum': 'PowerAllocationMode',
        'lv_property': 'Source:Advanced:Power Allocation Mode',
        'name': 'POWER_ALLOCATION_MODE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150208: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the mode of operation for an instrument channel for instruments that support multiple modes.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'InstrumentMode',
        'lv_property': 'LCR:Instrument Mode',
        'name': 'INSTRUMENT_MODE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150209: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the type of test signal to apply to the DUT for LCR measurements.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'LCRStimulusFunction',
        'lv_property': 'LCR:AC Stimulus:Function',
        'name': 'LCR_STIMULUS_FUNCTION',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150210: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the frequency of the AC test signal applied to the DUT for LCR measurements.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:AC Stimulus:Frequency',
        'name': 'LCR_FREQUENCY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150211: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the amplitude, in V RMS, of the AC voltage test signal applied to the DUT for LCR measurements.\nThis property applies when the NIDCPOWER_ATTR_LCR_STIMULUS_FUNCTION property is set to NIDCPOWER_VAL_AC_VOLTAGE.\n\nValid Values: 7.08e-4 V RMS to 7.07 V RMS\n\nInstrument specifications affect the valid values you can program. Refer to the specifications for your instrument for more information.',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:AC Stimulus:Voltage Amplitude',
        'name': 'LCR_VOLTAGE_AMPLITUDE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150212: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the amplitude, in amps RMS, of the AC current test signal applied to the DUT for LCR measurements.\nThis property applies when the NIDCPOWER_ATTR_LCR_STIMULUS_FUNCTION property is set to NIDCPOWER_VAL_AC_CURRENT.\n\nValid Values: 7.08e-9 A RMS to 0.707 A RMS\n\nInstrument specifications affect the valid values you can program. Refer to the specifications for your instrument for more information.',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:AC Stimulus:Current Amplitude',
        'name': 'LCR_CURRENT_AMPLITUDE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150213: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies how to apply DC bias for LCR measurements.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'LCRDCBiasSource',
        'lv_property': 'LCR:DC Bias:Source',
        'name': 'LCR_DC_BIAS_SOURCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150214: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the DC bias voltage level, in volts, when the NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE property is set to NIDCPOWER_VAL_DC_BIAS_VOLTAGE.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:DC Bias:Voltage Level',
        'name': 'LCR_DC_BIAS_VOLTAGE_LEVEL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150215: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the DC bias current level, in amps, when the NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE property is set to NIDCPOWER_VAL_DC_BIAS_CURRENT.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:DC Bias:Current Level',
        'name': 'LCR_DC_BIAS_CURRENT_LEVEL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150217: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the impedance range the channel uses for LCR measurements.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:Impedance Range:Impedance Range',
        'name': 'LCR_IMPEDANCE_RANGE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150218: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSelects a general aperture time profile for LCR measurements. The actual duration of each profile depends on the frequency of the LCR test signal.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'LCRMeasurementTime',
        'lv_property': 'LCR:Measurement Time',
        'name': 'LCR_MEASUREMENT_TIME',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150220: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether to apply open LCR compensation data to LCR measurements.\nUse the NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE property to define where the open compensation data that is applied to LCR measurements comes from.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:Compensation:Open:Enabled',
        'name': 'LCR_OPEN_COMPENSATION_ENABLED',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1150221: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether to apply short LCR compensation data to LCR measurements.\nUse the NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE property to define where the short compensation data that is applied to LCR measurements comes from.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:Compensation:Short:Enabled',
        'name': 'LCR_SHORT_COMPENSATION_ENABLED',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1150222: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether to apply load LCR compensation data to LCR measurements.\nBoth the NIDCPOWER_ATTR_LCR_OPEN_COMPENSATION_ENABLED and NIDCPOWER_ATTR_LCR_SHORT_COMPENSATION_ENABLED properties must be set to VI_TRUE in order to set this property to VI_TRUE.\n\nUse the NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE property to define where the load compensation data that is applied to LCR measurements comes from.\n',
            'note': '\nLoad compensation data are applied only for those specific frequencies you define with niDCPower_PerformLCRLoadCompensation;\nload compensation is not interpolated from the specific frequencies you define and applied to other frequencies.\n\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:Compensation:Load:Enabled',
        'name': 'LCR_LOAD_COMPENSATION_ENABLED',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1150223: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the source of the LCR compensation data NI-DCPower applies to LCR measurements.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'LCROpenShortLoadCompensationDataSource',
        'lv_property': 'LCR:Compensation:LCR Open/Short/Load Compensation Data Source',
        'name': 'LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150235: {
        'access': 'read-write',
        'documentation': {
            'description': '\nEnables or disables output cutoff functionality. If enabled, you can define output cutoffs that, if exceeded, cause the output of the specified channel(s) to be disconnected.\nWhen this attribute is disabled, all other output cutoff attributes are ignored.',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n Instruments that do not support this attribute behave as if this attribute were set to VI_FALSE.'
        },
        'lv_property': 'Source:Output Cutoff:Enabled',
        'name': 'OUTPUT_CUTOFF_ENABLED',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1150236: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies a high limit voltage value, in volts, for output cutoff.\nIf the voltage output exceeds this limit, the output is disconnected.\n\nTo find out whether an output has exceeded this limit, call the niDCPower_QueryLatchedOutputCutoffState function with NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_OUTPUT_HIGH as the output cutoff reason.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Output Cutoff:Voltage Output Limit High',
        'name': 'OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_HIGH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150237: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies a high limit current value, in amps, for output cutoff.\nIf the measured current exceeds this limit, the output is disconnected.\n\nTo find out whether an output has exceeded this limit, call the niDCPower_QueryLatchedOutputCutoffState function with NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_MEASURE_HIGH as the output cutoff reason.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Output Cutoff:Current Measure Limit High',
        'name': 'OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_HIGH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150238: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies a limit for negative voltage slew rate, in volts per microsecond, for output cutoff.\nIf the voltage decreases at a rate that exceeds this limit, the output is disconnected.\n\nTo find out whether an output has exceeded this limit, call the niDCPower_QueryLatchedOutputCutoffState with NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_CHANGE_LOW as the output cutoff reason.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Output Cutoff:Voltage Change Limit Low',
        'name': 'OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_LOW',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150239: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies a limit for negative current slew rate, in amps per microsecond, for output cutoff.\nIf the current decreases at a rate that exceeds this limit, the output is disconnected.\n\nTo find out whether an output has exceeded this limit, call the niDCPower_QueryLatchedOutputCutoffState function with NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_CHANGE_LOW as the output cutoff reason.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Output Cutoff:Current Change Limit Low',
        'name': 'OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_LOW',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150240: {
        'access': 'read-write',
        'documentation': {
            'description': '\nEnables or disables current overrange functionality for output cutoff. If enabled, the output is disconnected when the measured current saturates the current range.\n\nTo find out whether an output has exceeded this limit, call the niDCPower_QueryLatchedOutputCutoffState function with NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_OUTPUT_HIGH as the output cutoff reason.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Output Cutoff:Current Overrange Enabled',
        'name': 'OUTPUT_CUTOFF_CURRENT_OVERRANGE_ENABLED',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1150244: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether the hardware automatically selects the best range to measure the signal. Note the highest range the algorithm uses is dependent on the corresponding limit range property. The algorithm the hardware uses can be controlled using the NIDCPOWER_ATTR_AUTORANGE_APERTURE_TIME_MODE property.\n',
            'note': '\nAutoranging begins at module startup and remains active until the module is reconfigured or reset. This attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Measurement:Autorange',
        'name': 'AUTORANGE',
        'python_type': 'bool',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150245: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the algorithm the hardware uses for measurement autoranging.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'AutorangeBehavior',
        'lv_property': 'Measurement:Advanced:Autorange Behavior',
        'name': 'AUTORANGE_BEHAVIOR',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150246: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether the aperture time used for the measurement autorange algorithm is determined automatically or customized using the NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME property.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'AutorangeApertureTimeMode',
        'lv_property': 'Measurement:Advanced:Autorange Aperture Time Mode',
        'name': 'AUTORANGE_APERTURE_TIME_MODE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150247: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the measurement autorange aperture time used for the measurement autorange algorithm. The aperture time is specified in the units set by the NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME_UNITS property. This value will typically be smaller than the aperture time used for measurements.\n',
            'note': 'For smaller ranges, the value is scaled up to account for noise. The factor used to scale the value is derived from the module capabilities. This attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.'
        },
        'lv_property': 'Measurement:Advanced:Autorange Minimum Aperture Time',
        'name': 'AUTORANGE_MINIMUM_APERTURE_TIME',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150248: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the units of the NIDCPOWER_ATTR_AUTORANGE_MINIMUM_APERTURE_TIME property.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'ApertureTimeUnits',
        'lv_property': 'Measurement:Advanced:Autorange Minimum Aperture Time Units',
        'name': 'AUTORANGE_MINIMUM_APERTURE_TIME_UNITS',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150249: {
        'access': 'read-write',
        'attribute_class': 'AttributeViStringRepeatedCapability',
        'documentation': {
            'description': '\nSpecifies the channel(s) to merge with a designated primary channel of an SMU in order to increase the maximum current you can source from the SMU.\nThis attribute designates the merge channels to combine with a primary channel. To designate the primary channel, initialize the session to the primary channel only.\nNote: You cannot change the merge configuration with this attribute when the session is in the Running state.\nFor complete information on using merged channels with this attribute, refer to Merged Channels in the NI DC Power Supplies and SMUs Help.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device. Devices that do not support this property behave as if no channels were merged.\nDefault Value: Refer to the Supported Attributes by Device topic for the default value by device.\n'
        },
        'lv_property': 'Source:Advanced:Merged Channels',
        'name': 'MERGED_CHANNELS',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString'
    },
    1150255: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the lowest range used during measurement autoranging. Limiting the lowest range used during autoranging can improve the speed of the autoranging algorithm and minimize frequent and unpredictable range changes for noisy signals.\n',
            'note': 'The maximum range used is the range that includes the value specified in the compliance limit property, NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE property or NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE property, depending on the selected NIDCPOWER_ATTR_OUTPUT_FUNCTION. This attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.'
        },
        'lv_property': 'Measurement:Advanced:Autorange Minimum Current Range',
        'name': 'AUTORANGE_MINIMUM_CURRENT_RANGE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150256: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the lowest range used during measurement autoranging. The maximum range used is range that includes the value specified in the compliance limit property. Limiting the lowest range used during autoranging can improve the speed of the autoranging algorithm and/or minimize thrashing between ranges for noisy signals.\n',
            'note': 'The maximum range used is the range that includes the value specified in the compliance limit property, NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE property or NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE property, depending on the selected NIDCPOWER_ATTR_OUTPUT_FUNCTION. This attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.'
        },
        'lv_property': 'Measurement:Advanced:Autorange Minimum Voltage Range',
        'name': 'AUTORANGE_MINIMUM_VOLTAGE_RANGE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150257: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies thresholds used during autoranging to determine when range changing occurs.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'AutorangeThresholdMode',
        'lv_property': 'Measurement:Advanced:Autorange Threshold Mode',
        'name': 'AUTORANGE_THRESHOLD_MODE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150258: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nSpecifies the LCR measurement aperture time for a channel, in seconds, \nwhen the NIDCPOWER_ATTR_LCR_MEASUREMENT_TIME property is set to NIDCPOWER_VAL_MEASUREMENT_TIME_CUSTOM.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:Custom Measurement Time',
        'name': 'LCR_CUSTOM_MEASUREMENT_TIME',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150261: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the conductance, in siemens, of the circuit used for open LCR compensation.\nThis property applies when NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE is set to NIDCPOWER_VAL_AS_DEFINED.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:Compensation:Open:Conductance',
        'name': 'LCR_OPEN_CONDUCTANCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150262: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the susceptance, in siemens, of the circuit used for open LCR compensation.\nThis property applies when NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE is set to NIDCPOWER_VAL_AS_DEFINED.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:Compensation:Open:Susceptance',
        'name': 'LCR_OPEN_SUSCEPTANCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150263: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the resistance, in ohms, of the circuit used for short LCR compensation.\nThis property applies when NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE is set to NIDCPOWER_VAL_AS_DEFINED.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:Compensation:Short:Resistance',
        'name': 'LCR_SHORT_RESISTANCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150264: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the reactance, in ohms, of the circuit used for short LCR compensation.\nThis property applies when NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE is set to NIDCPOWER_VAL_AS_DEFINED.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:Compensation:Short:Reactance',
        'name': 'LCR_SHORT_REACTANCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150268: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the resistance, in ohms, of the load used for load LCR compensation as measured by the instrument.\nThis property applies when NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE is set to NIDCPOWER_VAL_AS_DEFINED.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:Compensation:Load:Measured Resistance',
        'name': 'LCR_MEASURED_LOAD_RESISTANCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150269: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the reactance, in ohms, of the load used for load LCR compensation as measured by the instrument.\nThis property applies when NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE is set to NIDCPOWER_VAL_AS_DEFINED.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:Compensation:Load:Measured Reactance',
        'name': 'LCR_MEASURED_LOAD_REACTANCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150270: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the actual resistance, in ohms, of the load used for load LCR compensation.\nThis property applies when NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE is set to NIDCPOWER_VAL_AS_DEFINED.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:Compensation:LCR Actual Load Resistance',
        'name': 'LCR_ACTUAL_LOAD_RESISTANCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150271: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the actual reactance, in ohms, of the load used for load LCR compensation.\nThis property applies when NIDCPOWER_ATTR_LCR_OPEN_SHORT_LOAD_COMPENSATION_DATA_SOURCE is set to NIDCPOWER_VAL_AS_DEFINED.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:Compensation:LCR Actual Load Reactance',
        'name': 'LCR_ACTUAL_LOAD_REACTANCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150275: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the behavior of the Shutdown trigger.\nDefault Value: NIDCPOWER_VAL_NONE\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'TriggerType',
        'lv_property': 'Triggers:Shutdown Trigger:Trigger Type',
        'name': 'SHUTDOWN_TRIGGER_TYPE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150277: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the input terminal for the Shutdown trigger. This attribute is used only when the NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE attribute is set to digital edge.\nYou can specify any valid input terminal for this attribute. Valid terminals are listed in Measurement & Automation Explorer under the Device Routes tab.\nInput terminals can be specified in one of two ways. If the device is named Dev1 and your terminal is PXI_Trig0, you can specify the terminal with the fully qualified terminal name, /Dev1/PXI_Trig0, or with the shortened terminal name, PXI_Trig0. The input terminal can also be a terminal from another device. For example, you can set the input terminal on Dev1 to be /Dev2/SourceCompleteEvent.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Triggers:Shutdown Trigger:Digital Edge:Input Terminal',
        'name': 'DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViString'
    },
    1150278: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies how to apply cable compensation data for instruments that support LCR functionality.\nSupported instruments use cable compensation for the following operations:\n\nSMU mode: to stabilize DC current sourcing in the two smallest current ranges.\nLCR mode: to compensate for the effects of cabling on LCR measurements.\n\nFor NI standard options, select the length of your NI cable to apply compensation data for a typical cable of that type.\nFor custom options, choose the source of the custom cable compensation data. You must then generate the custom cable compensation data.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'CableLength',
        'lv_property': 'Device Specific:LCR:Cable Length',
        'name': 'CABLE_LENGTH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150290: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether the channel actively attempts to maintain a constant test voltage or current across the DUT for LCR measurements.\nThe use of voltage or current depends on the test signal you configure with the NIDCPOWER_ATTR_LCR_STIMULUS_FUNCTION property.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:AC Stimulus:Automatic Level Control',
        'name': 'LCR_AUTOMATIC_LEVEL_CONTROL',
        'python_type': 'bool',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150291: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether the channel actively maintains a constant DC bias voltage or current across the DUT for LCR measurements.\nTo use this property, you must configure a DC bias with the NIDCPOWER_ATTR_LCR_DC_BIAS_SOURCE property.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:DC Bias:Automatic Level Control',
        'name': 'LCR_DC_BIAS_AUTOMATIC_LEVEL_CONTROL',
        'python_type': 'bool',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150292: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies a low limit voltage value, in volts, for output cutoff.\nIf the voltage output falls below this limit, the output is disconnected.\n\nTo find out whether an output has fallen below this limit, call the niDCPower_QueryLatchedOutputCutoffState function with NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_OUTPUT_LOW as the output cutoff reason.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Output Cutoff:Voltage Output Limit Low',
        'name': 'OUTPUT_CUTOFF_VOLTAGE_OUTPUT_LIMIT_LOW',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150293: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies a low limit current value, in amps, for output cutoff.\nIf the measured current falls below this limit, the output is disconnected.\n\nTo find out whether an output has fallen below this limit, call the niDCPower_QueryLatchedOutputCutoffState function with NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_MEASURE_LOW as the output cutoff reason.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Output Cutoff:Current Measure Limit Low',
        'name': 'OUTPUT_CUTOFF_CURRENT_MEASURE_LIMIT_LOW',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150294: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies a limit for positive voltage slew rate, in volts per microsecond, for output cutoff.\nIf the voltage increases at a rate that exceeds this limit, the output is disconnected.\n\nTo find out whether an output has exceeded this limit, call the niDCPower_QueryLatchedOutputCutoffState with NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_VOLTAGE_CHANGE_HIGH as the output cutoff reason.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Output Cutoff:Voltage Change Limit High',
        'name': 'OUTPUT_CUTOFF_VOLTAGE_CHANGE_LIMIT_HIGH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150295: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies a limit for positive current slew rate, in amps per microsecond, for output cutoff.\nIf the current increases at a rate that exceeds this limit, the output is disconnected.\n\nTo find out whether an output has exceeded this limit, call the niDCPower_QueryLatchedOutputCutoffState function with NIDCPOWER_VAL_OUTPUT_CUTOFF_REASON_CURRENT_CHANGE_HIGH as the output cutoff reason.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Output Cutoff:Current Change Limit High',
        'name': 'OUTPUT_CUTOFF_CURRENT_CHANGE_LIMIT_HIGH',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150299: {
        'access': 'read-write',
        'documentation': {
            'description': '\nDefines how to apply short custom cable compensation in LCR mode when NIDCPOWER_ATTR_CABLE_LENGTH property is set to NIDCPOWER_VAL_CUSTOM_ONBOARD_STORAGE or NIDCPOWER_VAL_CUSTOM_AS_CONFIGURED.\n\nLCR custom cable compensation uses compensation data for both an open and short configuration.\nFor open custom cable compensation, you must supply your own data from a call to niDCPower_PerformLCROpenCustomCableCompensation.\nFor short custom cable compensation, you can supply your own data from a call to niDCPower_PerformLCRShortCustomCableCompensation or NI-DCPower can apply a default set of short compensation data.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n',
            'table_body': [
                [
                    'VI_FALSE',
                    'Uses default short compensation data.'
                ],
                [
                    'VI_TRUE',
                    'Uses short custom cable compensation data generated by niDCPower_PerformLCRShortCustomCableCompensation.'
                ]
            ]
        },
        'lv_property': 'LCR:Compensation:LCR Short Custom Cable Compensation Enabled',
        'name': 'LCR_SHORT_CUSTOM_CABLE_COMPENSATION_ENABLED',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1150300: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nDelays disconnecting the output by the time you specify, in seconds, when a limit is exceeded.',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Output Cutoff:Delay',
        'name': 'OUTPUT_CUTOFF_DELAY',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1150302: {
        'access': 'read-write',
        'attribute_class': 'AttributeIsolationState',
        'documentation': {
            'description': '\nDefines whether the channel is isolated.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Advanced:Isolation State',
        'name': 'ISOLATION_STATE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32',
        'type_in_documentation': 'bool'
    },
    1150314: {
        'access': 'read-write',
        'documentation': {
            'description': '\nAutomatically optimizes the measurement aperture time according to the actual current range when measurement autorange is enabled.\nOptimization accounts for power line frequency when the NIDCPOWER_ATTR_APERTURE_TIME_UNITS attribute is set to NIDCPOWER_VAL_POWER_LINE_CYCLES.\n\nThis attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_VOLTAGE and the NIDCPOWER_ATTR_AUTORANGE attribute is enabled.',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'ApertureTimeAutoMode',
        'lv_property': 'Measurement:Aperture Time Auto Mode',
        'name': 'APERTURE_TIME_AUTO_MODE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150315: {
        'access': 'read-write',
        'documentation': {
            'description': '\nFor instruments in LCR mode, determines whether NI-DCPower automatically calculates and applies the source delay or applies a source delay you set manually.\n\nYou can return the source delay duration for either option by reading NIDCPOWER_ATTR_SOURCE_DELAY.\n\nWhen you use this property to manually set the source delay, it is possible to set source delays short enough to unbalance the bridge and affect measurement accuracy. LCR measurement functions report whether the bridge is unbalanced.\n\nDefault Value: NIDCPOWER_VAL_LCR_SOURCE_DELAY_MODE_AUTOMATIC\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'LCRSourceDelayMode',
        'lv_property': 'LCR:Source Delay Mode',
        'name': 'LCR_SOURCE_DELAY_MODE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150318: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the load resistance, in ohms and assuming a series model, of the DUT in order to compute the impedance range when the NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE property is set to NIDCPOWER_VAL_LCR_LOAD_CONFIGURATION.',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:Impedance Range:Advanced:Load Resistance',
        'name': 'LCR_LOAD_RESISTANCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150319: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the load inductance, in henrys and assuming a series model, of the DUT in order to compute the impedance range when the NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE property is set to NIDCPOWER_VAL_LCR_LOAD_CONFIGURATION.',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:Impedance Range:Advanced:Load Inductance',
        'name': 'LCR_LOAD_INDUCTANCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150320: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the load capacitance, in farads and assuming a series model, of the DUT in order to compute the impedance range when the NIDCPOWER_ATTR_LCR_IMPEDANCE_RANGE_SOURCE property is set to NIDCPOWER_VAL_LCR_LOAD_CONFIGURATION.',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'LCR:Impedance Range:Advanced:Load Capacitance',
        'name': 'LCR_LOAD_CAPACITANCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1150321: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies how the impedance range for LCR measurements is determined.',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'enum': 'LCRImpedanceRangeSource',
        'lv_property': 'LCR:Impedance Range:Advanced:Impedance Range Source',
        'name': 'LCR_IMPEDANCE_RANGE_SOURCE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1150322: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'documentation': {
            'description': '\nBalances between settling time and maximum measurement time by specifying the maximum time delay between when a range change occurs and when measurements resume.\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Measurement:Advanced:Autorange Maximum Delay After Range Change',
        'name': 'AUTORANGE_MAXIMUM_DELAY_AFTER_RANGE_CHANGE',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64',
        'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
    },
    1250001: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the voltage level, in volts, that the device attempts to generate on the specified channel(s).\nThis attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_VOLTAGE.\nNIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.\nValid Values: The valid values for this attribute are defined by the values you specify for the NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE attribute.\n',
            'note': 'The channel must be enabled for the specified voltage level to take effect. Refer to the NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.'
        },
        'lv_property': 'Source:DC Voltage:Voltage Level',
        'name': 'VOLTAGE_LEVEL',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250002: {
        'access': 'read-write',
        'documentation': {
            'description': '\nEnables (VI_TRUE) or disables (VI_FALSE) overvoltage protection (OVP).\nRefer to the Output Overvoltage Protection topic in the NI DC Power Supplies and SMUs Help for more information about overvoltage protection.\nDefault Value: VI_FALSE\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Advanced:OVP Enabled',
        'name': 'OVP_ENABLED',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    },
    1250003: {
        'access': 'read-write',
        'documentation': {
            'description': '\nDetermines the voltage limit, in volts, beyond which overvoltage protection (OVP) engages.\nValid Values: 2 V to 210 V\nDefault Value: 210 V\n',
            'note': '\nThis attribute is not supported on all devices. For more information about supported devices, search ni.com for Supported Attributes by Device.\n'
        },
        'lv_property': 'Source:Advanced:OVP Limit',
        'name': 'OVP_LIMIT',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250004: {
        'access': 'read-write',
        'name': 'CURRENT_LIMIT_BEHAVIOR',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViInt32'
    },
    1250005: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies the current limit, in amps, that the output cannot exceed when generating the desired voltage level on the specified channel(s).\nThis attribute is applicable only if the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute is set to NIDCPOWER_VAL_DC_VOLTAGE and the NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY attribute is set to NIDCPOWER_VAL_SYMMETRIC.\nNIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.\nValid Values: The valid values for this attribute are defined by the values to which NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE attribute is set.\n',
            'note': 'The channel must be enabled for the specified current limit to take effect. Refer to the NIDCPOWER_ATTR_OUTPUT_ENABLED attribute for more information about enabling the output channel.'
        },
        'lv_property': 'Source:DC Voltage:Current Limit',
        'name': 'CURRENT_LIMIT',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViReal64'
    },
    1250006: {
        'access': 'read-write',
        'documentation': {
            'description': '\nSpecifies whether the output is enabled (VI_TRUE) or disabled (VI_FALSE).\nDepending on the value you specify for the NIDCPOWER_ATTR_OUTPUT_FUNCTION attribute, you also must set the voltage level or current level in addition to enabling the output\nthe niDCPower_InitiateWithChannels function. Refer to the Programming States topic in the NI DC Power Supplies and SMUs Help for more information about NI-DCPower programming states.\nDefault Value: The default value is VI_TRUE if you use the niDCPower_InitializeWithChannels function to open the session. Otherwise the default value is VI_FALSE, including when you use a calibration session or the deprecated programming model.\n',
            'note': 'If the session is in the Committed or Uncommitted states, enabling the output does not take effect until you call'
        },
        'lv_property': 'Source:Output Enabled',
        'name': 'OUTPUT_ENABLED',
        'supported_rep_caps': [
            'channels'
        ],
        'type': 'ViBoolean'
    }
}
