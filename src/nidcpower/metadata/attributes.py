
# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here.
#  If the generated information is not correct for python
#  changes can be made in attributes_addon.py and they will be
#  applied at build time.

attributes = {
    1050002: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:User Options:Range Check',
        'name': 'RANGE_CHECK',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to validate property values and VI parameters.

If this property is enabled, NI-DCPower validates the parameter values
that you pass to NI-DCPower VIs. Range-checking parameters is useful for
debugging. After you validate your program, you can set this property to
FALSE to disable range checking and maximize performance.

Use the `niDCPower Initialize with
Options <NIDCPowerVIRef.chm::/niDCPower_Initialize_With_Options.html>`__
VI to override the default value.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
},
    },
    1050003: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:User Options:Query Instrument Status',
        'name': 'QUERY_INSTRUMENT_STATUS',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether NI-DCPower queries the device status after each
operation.

Querying the device status is useful for debugging. After you validate
your program, you can set this property to FALSE to disable status
checking and maximize performance.

NI-DCPower ignores status checking for particular properties regardless
of the setting of this property.

Use the `niDCPower Initialize with
Options <NIDCPowerVIRef.chm::/niDCPower_Initialize_With_Options.html>`__
VI to override this value.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
},
    },
    1050004: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:User Options:Cache',
        'name': 'CACHE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to cache the value of properties.

When caching is enabled, NI-DCPower records the current power supply
settings and avoids sending redundant commands to the device. Enabling
caching can significantly increase execution speed.

NI-DCPower might always cache or never cache particular properties
regardless of the setting of this property.

Use the `niDCPower Initialize With
Channels <NIDCPowerVIRef.chm::/niDCPower_Initialize_With_Channels.html>`__
VI to override this value.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
},
    },
    1050005: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:User Options:Simulate',
        'name': 'SIMULATE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to simulate NI-DCPower I/O operations. TRUE specifies
that operation is simulated.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
},
    },
    1050006: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:User Options:Record Value Coercions',
        'name': 'RECORD_COERCIONS',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the IVI engine records the value coercions it makes
for ViInt32 and ViReal64 properties.

Call the `niDCPower Get Next Coercion
Record <NIDCPowerVIRef.chm::/niDCPower_Get_Next_Coercion_Record.html>`__
VI to read and delete the earliest coercion record from the list.

Use the `niDCPower Initialize with
Options <NIDCPowerVIRef.chm::/niDCPower_Initialize_With_Options.html>`__
VI to override this value.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
},
    },
    1050007: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Driver Setup',
        'name': 'DRIVER_SETUP',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Indicates the Driver Setup string that you specified when initializing
the driver.

Some cases exist where you must specify the instrument driver options at
initialization time. An example of this case is specifying a particular
instrument model from among a family of instruments that the driver
supports. This property is useful when
`simulating <NI_DC_Power_Supplies_Help.chm::/simulate.html>`__ a device.
You can specify the driver-specific options through the Driver Setup
keyword in the **options string** parameter in the `niDCPower Initialize
with
Options <NIDCPowerVIRef.chm::/niDCPower_Initialize_With_Options.html>`__
VI or through the IVI Configuration Utility.

If you do not specify a Driver Setup string, this property returns an
empty string.
''',
},
    },
    1050021: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:User Options:Interchange Check',
        'name': 'INTERCHANGE_CHECK',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to perform interchangeability checking and log
interchangeability warnings when you call NI-DCPower VIs. TRUE specifies
that interchangeability checking is enabled.

Interchangeability warnings indicate that using your application with a
different power supply might cause different behavior. Call the
`niDCPower Get Next Interchange
Warning <NIDCPowerVIRef.chm::/niDCPower_Get_Next_Interchange_Warning.html>`__
VI to retrieve interchange warnings.

Call the `niDCPower Clear Interchange
Warnings <NIDCPowerVIRef.chm::/niDCPower_Clear_Interchange_Warnings.html>`__
VI to clear the list of interchangeability warnings without reading
them.

Interchangeability checking examines the properties in a capability
group only if you specify a value for at least one property within that
group. Interchangeability warnings can occur when a property affects the
behavior of the device and you have not set that property or when the
property has been invalidated since you set it.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
},
    },
    1050203: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Channel Count',
        'name': 'CHANNEL_COUNT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Indicates the number of channels that NI-DCPower supports for the
instrument that was chosen when the current session was opened. For
channel-based properties, the IVI engine maintains a separate cache
value for each channel.
''',
},
    },
    1050302: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Driver Prefix',
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Contains the prefix for NI-DCPower. The name of each user-callable VI in
NI-DCPower begins with this prefix.
''',
},
    },
    1050304: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Resource Descriptor',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Indicates the resource descriptor NI-DCPower uses to identify the
physical device.

If you initialize NI-DCPower with a logical name, this property contains
the resource descriptor that corresponds to the entry in the IVI
Configuration Utility. If you initialize NI-DCPower with the resource
descriptor, this property contains that value.
''',
},
    },
    1050305: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Logical Name',
        'name': 'LOGICAL_NAME',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Contains the logical name you specified when opening the current IVI
session.

You can pass a logical name to the `niDCPower
Initialize <NIDCPowerVIRef.chm::/niDCPower_Initialize.html>`__ or
`niDCPower Initialize with
Options <NIDCPowerVIRef.chm::/niDCPower_Initialize_With_Options.html>`__
VIs. The IVI Configuration Utility must contain an entry for the logical
name. The logical name entry refers to a virtual instrument section in
the IVI configuration file. The virtual instrument section specifies a
physical device and initial user settings.
''',
},
    },
    1050327: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Contains a comma-separated (,) list of supported NI-DCPower device
models.
''',
},
    },
    1050401: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities',
        'name': 'GROUP_CAPABILITIES',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Contains a comma-separated (,) list of class-extension groups that
NI-DCPower implements.
''',
},
    },
    1050510: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Firmware Revision',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Contains the firmware revision information for the device you are
currently using.
''',
},
    },
    1050511: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Manufacturer',
        'name': 'INSTRUMENT_MANUFACTURER',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Contains the name of the manufacturer for the device you are currently
using.
''',
},
    },
    1050512: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Model',
        'name': 'INSTRUMENT_MODEL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': 'Contains the model number or name of the device you are currently using.',
},
    },
    1050513: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
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
        'enum': None,
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
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Class Specification Major Version',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Contains the major version number of the class specification with which
NI-DCPower is compliant.
''',
},
    },
    1050516: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Class Specification Minor Version',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Contains the minor version number of the class specification with which
NI-DCPower is compliant.
''',
},
    },
    1050551: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
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
Specifies the power source to use. NI-DCPower switches the power source
used by the device to the specified value.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`NI PXI-4110 Internal and Auxiliary
Power <NI_DC_Power_Supplies_Help.chm::/4110_Internal_Auxiliary_Power.html>`__

`NI PXI-4130 Internal and Auxiliary
Power <NI_DC_Power_Supplies_Help.chm::/4130_Internal_Auxiliary_Power.html>`__
''',
'note': '''
Automatic selection is not persistent and occurs only at the time this
property is set to **Automatic**. However, if the session is in the
`Committed or
Uncommitted <NI_DC_Power_Supplies_Help.chm::/programmingStates.html>`__
state when you set this property, the power source selection only occurs
after you call the `niDCPower
Initiate <NIDCPowerVIRef.chm::/niDCPower_Initiate.html>`__ VI.
''',
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
'description': '''
Indicates whether the device is using the internal or auxiliary power
source to generate power.
''',
},
    },
    1150002: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Advanced:Auxiliary Power Source Available',
        'name': 'AUXILIARY_POWER_SOURCE_AVAILABLE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Indicates whether an auxiliary power source is connected to the device.

A value of FALSE may indicate that the auxiliary input fuse has blown.
Refer to the `Detecting Internal/Auxiliary
Power <NI_DC_Power_Supplies_Help.chm::/Detecting_Internal_Auxiliary_Power.html>`__
topic in the *NI DC Power Supplies and SMUs Help* for more information
about internal and auxiliary power.

**Related topics:**

`NI PXI-4110 Internal and Auxiliary
Power <NI_DC_Power_Supplies_Help.chm::/4110_Internal_Auxiliary_Power.html>`__

`NI PXI-4130 Internal and Auxiliary
Power <NI_DC_Power_Supplies_Help.chm::/4130_Internal_Auxiliary_Power.html>`__
''',
'note': '''
This property does not necessarily indicate if the device is using the
auxiliary power source to generate power. Use the `Power Source In
Use <pniDCPower_PowerSourceInUse.html>`__ property to retrieve that
information.
''',
},
    },
    1150003: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Measurement:Samples To Average',
        'name': 'SAMPLES_TO_AVERAGE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of samples to average when you take a measurement.

Increasing the number of samples to average decreases measurement noise
but increases the time required to take a measurement. Refer to the `NI
PXI-4110 <NI_DC_Power_Supplies_Help.chm::/4110_Measure_Avg.html>`__, `NI
PXI-4130 <NI_DC_Power_Supplies_Help.chm::/4130_Measure_Avg.html>`__, `NI
PXI-4132 <NI_DC_Power_Supplies_Help.chm::/4132_Measure_Avg.html>`__, or
`NI PXIe-4154 <NI_DC_Power_Supplies_Help.chm::/4154_Measure_Avg.html>`__
averaging topic for optional property settings to improve immunity to
certain noise types. For information about improving noise immunity for
NI-DCPower devices that support DC noise rejection, refer to
`Measurement Noise
Rejection <NI_DC_Power_Supplies_Help.chm::/noiseRejectMeasure.html>`__

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Measurement Noise
Rejection <NI_DC_Power_Supplies_Help.chm::/NoiseRejectMeasure.html>`__
''',
'table_body': [['**Device**', '**Range of Samples to Average**'], ['NI PXI-4110 and NI PXI-4130', '1 to 511'], ['NI PXI-4132', '1 to 127'], ['NI PXIe-4112/4113', '1'], ['PXIe-4135', '1'], ['NI PXIe-4136/4137', '1'], ['NI PXIe-4138/4139', '1'], ['NI PXIe-4140/4141/4142/4143/4144/4145', '1'], ['NI PXIe-4154', '1 to 65,535'], ['PXIe-4162/4163', '1']],
},
    },
    1150004: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:DC Voltage:Current Limit Range',
        'name': 'CURRENT_LIMIT_RANGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the current limit range, in amps, for the specified
channel(s).

The range defines the valid values to which the current limit can be
set. Use the `Current Limit
Autorange <pniDCPower_CurrentLimitAutorange.html>`__ property to enable
automatic selection of the current limit range.

The Current Limit Range property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
Voltage**.

For valid ranges for your device, refer to
`Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.

**Related topics:**

`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
''',
'note': '''
The channel must be enabled for the specified current limit to take
effect. Refer to the `Output Enabled <pniDCPower_OutputEnabled.html>`__
property for more information about enabling the output channel.
''',
},
    },
    1150005: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:DC Voltage:Voltage Level Range',
        'name': 'VOLTAGE_LEVEL_RANGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the voltage level range, in volts, for the specified
channel(s).

The range defines the valid values to which the voltage level can be
set. Use the `Voltage Level
Autorange <pniDCPower_VoltageLevelAutorange.html>`__ property to enable
automatic selection of the voltage level range.

The Voltage Level Range property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
Voltage**.

For valid ranges for your device, refer to
`Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.

**Related topics:**

`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
''',
'note': '''
The channel must be enabled for the specified voltage level range to
take effect. Refer to the `Output
Enabled <pniDCPower_OutputEnabled.html>`__ property for more information
about enabling the output channel.
''',
},
    },
    1150006: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Measurement:Advanced:Reset Average Before Measurement',
        'name': 'RESET_AVERAGE_BEFORE_MEASUREMENT',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the measurement returned from any measurement call
starts with a new measurement call (TRUE) or returns a measurement that
has already begun or completed (FALSE).

When you set the `Samples to
Average <pniDCPower_SamplesToAverage.html>`__ property in the `Running
state <NI_DC_Power_Supplies_Help.chm::/programmingStates.html>`__, the
output channel measurements might move out of synchronization. While
NI-DCPower automatically synchronizes measurements upon the
initialization of a session, you can force a synchronization in the
running state before you run the `niDCPower Measure
Multiple <NIDCPowerVIRef.chm::/niDCPower_Measure_Multiple.html>`__ VI.
To force a synchronization in the running state, set the Reset Average
Before Measurement property to TRUE, and then run the niDCPower Measure
Multiple VI specifying all channels in the **channel name** parameter.
You can set the Reset Average Before Measurement property to FALSE after
the niDCPower Measure Multiple VI completes.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150007: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Advanced:Overranging Enabled',
        'name': 'OVERRANGING_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether NI-DCPower allows setting the `voltage
level <NIDCPowerVIRef.chm::/niDCPower_Configure_Voltage_Level.html>`__,
`current
level <NIDCPowerVIRef.chm::/niDCPower_Configure_Current_Level.html>`__,
`voltage
limit <NIDCPowerVIRef.chm::/niDCPower_Configure_Voltage_Limit.html>`__,
and `current
limit <NIDCPowerVIRef.chm::/niDCPower_Configure_Current_Limit.html>`__
outside the device specification limits. TRUE means that overranging is
enabled.

Refer to the `Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
topic in the *NI DC Power Supplies and SMUs Help* for more information
about overranging.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
''',
},
    },
    1150008: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'OutputFunction',
        'lv_property': 'Source:Output Function',
        'name': 'OUTPUT_FUNCTION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Configures the function to generate on the specified channel(s).

When **DC Voltage** is selected, the device generates the desired
voltage level on the output as long as the output current is below the
current limit. You can use the following properties to configure the
channel when **DC Voltage** is selected:

`Voltage Level <pniDCPower_VoltageLevel.html>`__ `Current
Limit <pniDCPower_CurrentLimit.html>`__ `Voltage Level
Range <pniDCPower_VoltageLevelRange.html>`__ `Current Limit
Range <pniDCPower_CurrentLimitRange.html>`__

When **DC Current** is selected, the device generates the desired
current level on the output as long as the output voltage is below the
voltage limit. You can use the following properties to configure the
channel when **DC Current** is selected:

`Current Level <pniDCPower_CurrentLevel.html>`__ `Voltage
Limit <pniDCPower_VoltageLimit.html>`__ `Current Level
Range <pniDCPower_CurrentLevelRange.html>`__ `Voltage Limit
Range <pniDCPower_VoltageLimitRange.html>`__

**Default Value**: Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Constant Voltage
Mode <NI_DC_Power_Supplies_Help.chm::/Constant_Voltage.html>`__

`Constant Current
Mode <NI_DC_Power_Supplies_Help.chm::/Constant_Current.html>`__
''',
},
    },
    1150009: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:DC Current:Current Level',
        'name': 'CURRENT_LEVEL',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the current level, in amps, that the device attempts to
generate on the specified channel(s).

This property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
Current**.

**Valid Values:** The valid values for this property are defined by the
values to which the `Current Level
Range <pniDCPower_CurrentLevelRange.html>`__ property is set.

**Related topics:**

`Constant Current
Mode <NI_DC_Power_Supplies_Help.chm::/Constant_Current.html>`__
''',
'note': '''
The channel must be enabled for the specified current level to take
effect. Refer to the `Output Enabled <pniDCPower_OutputEnabled.html>`__
property for more information about enabling the output channel.
''',
},
    },
    1150010: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:DC Current:Voltage Limit',
        'name': 'VOLTAGE_LIMIT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the voltage limit, in volts, that the output cannot exceed
when generating the desired current level on the specified channels.
Limit is specified as a positive value, but symmetric positive and
negative limits are enforced simultaneously.

This property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
Current**.

**Valid Values:** The valid values for this attribute are defined by the
values to which the `Voltage Limit
Range <pniDCPower_VoltageLimitRange.html>`__ property is set.

**Related topics:**

`Compliance <NI_DC_Power_Supplies_Help.chm::/compliance.html>`__
''',
'note': '''
The channel must be enabled for the specified current level to take
effect. Refer to the `Output Enabled <pniDCPower_OutputEnabled.html>`__
property for more information about enabling the output channel.
''',
},
    },
    1150011: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:DC Current:Current Level Range',
        'name': 'CURRENT_LEVEL_RANGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the current level range, in amps, for the specified
channel(s).

The range defines the valid values to which the current level can be
set. Use the `Current Level
Autorange <pniDCPower_CurrentLevelAutorange.html>`__ property to enable
automatic selection of the current level range.

The Current Level Range property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
Current**.

For valid ranges for your device, refer to
`Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.

**Related topics:**

`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
''',
'note': '''
The channel must be enabled for the specified current level range to
take effect. Refer to the `Output
Enabled <pniDCPower_OutputEnabled.html>`__ property for more information
about enabling the output channel.
''',
},
    },
    1150012: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:DC Current:Voltage Limit Range',
        'name': 'VOLTAGE_LIMIT_RANGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the voltage limit range, in volts, for the specified
channel(s).

The range defines the valid values to which the voltage limit can be
set. Use the `Voltage Limit
Autorange <pniDCPower_VoltageLimitAutorange.html>`__ property to enable
automatic selection of the voltage limit range.

The Voltage Limit Range property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
Current**.

For valid ranges for your device, refer to
`Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.

**Related topics:**

`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
''',
'note': '''
The channel must be enabled for the specified voltage limit range to
take effect. Refer to the `Output
Enabled <pniDCPower_OutputEnabled.html>`__ property for more information
about enabling the output channel.
''',
},
    },
    1150013: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'Sense',
        'lv_property': 'Measurement:Sense',
        'name': 'SENSE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Selects either local or remote sensing of the output voltage for the
specified channel(s).

Refer to the `Local and Remote
Sense <NI_DC_Power_Supplies_Help.chm::/local_and_remote_sense.html>`__
topic in the *NI DC Power Supplies and SMUs Help* for more information
about sensing voltage on supported channels and about devices that
support local and/or remote sensing.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Local and Remote
Sense <NI_DC_Power_Supplies_Help.chm::/local_and_remote_sense.html>`__
''',
},
    },
    1150014: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'OutputCapacitance',
        'lv_property': 'Source:Advanced:Output Capacitance',
        'name': 'OUTPUT_CAPACITANCE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether to use a low or high capacitance on the output for the
specified channel(s).

Refer to the `NI PXI-4130 Output Capacitance
Selection <NI_DC_Power_Supplies_Help.chm::/4130_Output_Cap_Select.html>`__
topic in the *NI DC Power Supplies and SMUs Help* for more information
about capacitance.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Output
Capacitance <NI_DC_Power_Supplies_Help.chm::/Capacitance.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150015: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'VoltageLevelAutorange',
        'lv_property': 'Source:DC Voltage:Voltage Level Autorange',
        'name': 'VOLTAGE_LEVEL_AUTORANGE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether NI-DCPower automatically selects the voltage level
range based on the desired voltage level for the specified channel(s).

If you set this property to **On**, NI-DCPower ignores any changes you
make to the `Voltage Level Range <pniDCPower_VoltageLevelRange.html>`__
property. If you change the Voltage Level Autorange property from **On**
to **Off**, NI-DCPower retains the last value that the `Voltage Level
Range <pniDCPower_VoltageLevelRange.html>`__ property was set to (or the
default value if it was never set) and uses that value as the voltage
level range.

Refer to the `Voltage Level Range <pniDCPower_VoltageLevelRange.html>`__
property for information about which range NI-DCPower automatically
selects.

The Voltage Level Autorange property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
Voltage**.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
''',
},
    },
    1150016: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'CurrentLimitAutorange',
        'lv_property': 'Source:DC Voltage:Current Limit Autorange',
        'name': 'CURRENT_LIMIT_AUTORANGE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether NI-DCPower automatically selects the current limit
range based on the desired current limit for the specified channel(s).

If you set this property to **On**, NI-DCPower ignores any changes you
make to the `Current Limit Range <pniDCPower_CurrentLimitRange.html>`__
property. If you change the Current Limit Autorange property from **On**
to **Off**, NI-DCPower retains the last value the Current Limit Range
property was set to (or the default value if it was never set) and uses
that value as the current limit range.

Refer to the `Current Limit Range <pniDCPower_CurrentLimitRange.html>`__
property for information about which range NI-DCPower automatically
selects.

The Current Limit Autorange property is applicable only if the channel
is configured to **DC Voltage** in the `Output
Function <pniDCPower_OutputFunction.html>`__ property.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
''',
},
    },
    1150017: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'CurrentLevelAutorange',
        'lv_property': 'Source:DC Current:Current Level Autorange',
        'name': 'CURRENT_LEVEL_AUTORANGE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether NI-DCPower automatically selects the current level
range based on the desired current level for the specified channel(s).

If you set this property to **On**, NI-DCPower ignores any changes you
make to the `Current Level Range <pniDCPower_CurrentLevelRange.html>`__
property. If you change the Current Level Autorange property from **On**
to **Off**, NI-DCPower retains the last value the `Current Level
Range <pniDCPower_CurrentLevelRange.html>`__ property was set to (or the
default value if it was never set) and uses that value as the current
level range.

Refer to the `Current Level Range <pniDCPower_CurrentLevelRange.html>`__
property for information about which range NI-DCPower automatically
selects.

The Current Level Autorange property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
Current**.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
''',
},
    },
    1150018: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'VoltageLimitAutorange',
        'lv_property': 'Source:DC Current:Voltage Limit Autorange',
        'name': 'VOLTAGE_LIMIT_AUTORANGE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether NI-DCPower automatically selects the voltage limit
range based on the desired voltage limit for the specified channel(s).

If you set this property to **On**, NI-DCPower ignores any changes you
make to the `Voltage Limit Range <pniDCPower_VoltageLimitRange.html>`__
property. If you change the Voltage Limit Autorange property from **On**
to **Off**, NI-DCPower retains the last value that the `Voltage Limit
Range <pniDCPower_VoltageLimitRange.html>`__ property was set to (or the
default value if it was never set) and uses that value as the voltage
limit range.

Refer to the `Voltage Limit Range <pniDCPower_VoltageLimitRange.html>`__
property for information about which range NI-DCPower automatically
selects.

The Voltage Limit Autorange property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
Current**.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Ranges <NI_DC_Power_Supplies_Help.chm::/ranges.html>`__
''',
},
    },
    1150020: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'PowerLineFrequency',
        'lv_property': 'Measurement:Power Line Frequency',
        'name': 'POWER_LINE_FREQUENCY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the power line frequency for specified channel(s). NI-DCPower
uses this value to select a timebase for setting the `Aperture
Time <pniDCPower_ApertureTime.html>`__ property in power line cycles
(PLCs).

Refer to the following topics for more information about how to
configure your measurements:

`NI PXIe-4112 Measurement Configuration and
Timing <NI_DC_Power_Supplies_Help.chm::/4112_MeasureConfigTiming.html>`__
`NI PXIe-4113 Measurement Configuration and
Timing <NI_DC_Power_Supplies_Help.chm::/4113_MeasureConfigTiming.html>`__
`NI PXI-4132 Measurement Configuration and
Timing <NI_DC_Power_Supplies_Help.chm::/4132_MeasureConfigTiming.html>`__
`Measurement Noise
Rejection <NI_DC_Power_Supplies_Help.chm::/noiseRejectMeasure.html>`__

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Measurement Noise
Rejection <NI_DC_Power_Supplies_Help.chm::/NoiseRejectMeasure.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
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

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
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
Specifies whether to configure the Start trigger to assert on the rising
or falling edge.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150023: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggers:Start Trigger:Digital Edge:Input Terminal',
        'name': 'DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the input terminal for the Start trigger. This property is
used only when the `Start Trigger
Type <pniDCPower_StartTriggerType.html>`__ property is set to **Digital
Edge**.

You can specify any valid input terminal for this property. Valid
terminals are listed in Measurement & Automation Explorer under the
**Device Routes** tab.

Input terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
shortened terminal name, PXI\_Trig0. The input terminal can also be a
terminal from another device. For example, you can set the input
terminal on Dev1 to be /Dev2/SourceCompleteEvent.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150024: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggers:Start Trigger:Export Output Terminal',
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Start trigger.

Refer to the **Device Routes** tab in Measurement & Automation Explorer
for a list of the terminals available on your device.

Output terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
shortened terminal name, PXI\_Trig0.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150025: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Advanced:Sequence Loop Count',
        'name': 'SEQUENCE_LOOP_COUNT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of times a sequence is run after initiation.

Refer to the `Sequence Source
Mode <NI_DC_Power_Supplies_Help.chm::/Sequencing.html>`__ topic in the
*NI DC Power Supplies and SMUs Help* for more information about the
sequence loop count.

**Valid Range**: 1 to 134217727

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices. When the `Sequence Loop Count Is
Finite <pniDCPower_SequenceLoopCountIsFinite.html>`__ property is set to
FALSE, the Sequence Loop Count property is ignored.
''',
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

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
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
Specifies whether to configure the Sequence trigger to assert on the
rising or falling edge.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150028: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggers:Sequence Advance Trigger:Digital Edge:Input Terminal',
        'name': 'DIGITAL_EDGE_SEQUENCE_ADVANCE_TRIGGER_INPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the input terminal for the Sequence Advance trigger. This
property is used only when the `Sequence Advance Trigger
Type <pniDCPower_SequenceAdvanceTriggerType.html>`__ property is set to
**Digital Edge**.

You can specify any valid input terminal for this property. Valid
terminals are listed in Measurement & Automation Explorer under the
**Device Routes** tab.

Input terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
shortened terminal name, PXI\_Trig0. The input terminal can also be a
terminal from another device. For example, you can set the input
terminal on Dev1 to be /Dev2/SourceCompleteEvent.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150029: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggers:Sequence Advance Trigger:Export Output Terminal',
        'name': 'EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Sequence Advance
trigger.

Refer to the **Device Routes** tab in Measurement & Automation Explorer
for a list of the terminals available on your device.

Output terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
shortened terminal name, PXI\_Trig0.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
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

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
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
Specifies whether to configure the Source trigger to assert on the
rising or falling edge.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150032: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggers:Source Trigger:Digital Edge:Input Terminal',
        'name': 'DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the input terminal for the Source trigger. This property is
used only when the `Source Trigger
Type <pniDCPower_SourceTriggerType.html>`__ property is set to **Digital
Edge**.

You can specify any valid input terminal for this property. Valid
terminals are listed in Measurement & Automation Explorer under the
**Device Routes** tab.

Input terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
shortened terminal name, PXI\_Trig0. The input terminal can also be a
terminal from another device. For example, you can set the input
terminal on Dev1 to be /Dev2/SourceCompleteEvent.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150033: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggers:Source Trigger:Export Output Terminal',
        'name': 'EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Source trigger.

Refer to the **Device Routes** tab in Measurement & Automation Explorer
for a list of the terminals available on your device.

Output terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
shortened terminal name, PXI\_Trig0.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
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

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
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
Specifies whether to configure the Measure trigger to assert on the
rising or falling edge.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150036: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggers:Measure Trigger:Digital Edge:Input Terminal',
        'name': 'DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the input terminal for the Measure trigger. This property is
used only when the `Measure Trigger
Type <pniDCPower_MeasureTriggerType.html>`__ property is set to
**Digital Edge**.

You can specify any valid input terminal for this property. Valid
terminals are listed in Measurement & Automation Explorer under the
**Device Routes** tab.

Input terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
shortened terminal name, PXI\_Trig0. The input terminal can also be a
terminal from another device. For example, you can set the input
terminal on Dev1 to be /Dev2/SourceCompleteEvent.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150037: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggers:Measure Trigger:Export Output Terminal',
        'name': 'EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Measure trigger.

Refer to the **Device Routes** tab in Measurement & Automation Explorer
for a list of the terminals available on your device.

Output terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
shortened terminal name, PXI\_Trig0.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
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

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150039: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Sequence Iteration Complete Event:Pulse:Width',
        'name': 'SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the width of the Sequence Iteration Complete event, in
seconds.

The minimum event pulse width value for the NI PXI-4132 is 150 ns, and
the minimum event pulse width value for PXI Express devices is 250 ns.

The maximum event pulse width value for all devices is 1.6 microseconds.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150040: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Sequence Iteration Complete Event:Output Terminal',
        'name': 'SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Sequence Iteration
Complete event.

Output terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
shortened terminal name, PXI\_Trig0.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
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

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150042: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Source Complete Event:Pulse:Width',
        'name': 'SOURCE_COMPLETE_EVENT_PULSE_WIDTH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the width of the Source Complete event, in seconds.

The minimum event pulse width value for the NI PXI-4132 is 150 ns, and
the minimum event pulse width value for PXI Express devices is 250 ns.

The maximum event pulse width value for all devices is 1.6 microseconds.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150043: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Source Complete Event:Output Terminal',
        'name': 'SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Source Complete event.

Output terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
shortened terminal name, PXI\_Trig0.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
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

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150045: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Measure Complete Event:Pulse:Width',
        'name': 'MEASURE_COMPLETE_EVENT_PULSE_WIDTH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the width of the Measure Complete event, in seconds.

The minimum event pulse width value for the NI PXI-4132 is 150 ns, and
the minimum event pulse width value for PXI Express devices is 250 ns.

The maximum event pulse width value for all devices is 1.6 microseconds.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150046: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Measure Complete Event:Event Delay',
        'name': 'MEASURE_COMPLETE_EVENT_DELAY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the amount of time to delay the generation of the Measure
Complete event, in seconds.

The NI PXI-4132 and NI PXIe-4140/4141/4142/4143/4144/4145/4154 support
values from 0 seconds to 167 seconds.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150047: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Measure Complete Event:Output Terminal',
        'name': 'MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Measure Complete event.

Output terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
shortened terminal name, PXI\_Trig0.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
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

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150049: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Sequence Engine Done Event:Pulse:Width',
        'name': 'SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the width of the Sequence Engine Done event, in seconds.

The minimum event pulse width value for the NI PXI-4132 is 150 ns, and
the minimum event pulse width value for PXI Express devices is 250 ns.

The maximum event pulse width value for all devices is 1.6 microseconds.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150050: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Sequence Engine Done Event:Output Terminal',
        'name': 'SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Sequence Engine Done
Complete event.

Output terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
shortened terminal name, PXI\_Trig0.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150051: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Advanced:Source Delay',
        'name': 'SOURCE_DELAY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Determines when, in seconds, the device generates the Source Complete
event, potentially starting a measurement if the `Measure
When <pniDCPower_MeasureWhen.html>`__ property is set to **Automatically
After Source Complete**.

Refer to the `Single Point source
mode <NI_DC_Power_Supplies_Help.chm::/Singlept.html>`__ and `Sequence
source mode <NI_DC_Power_Supplies_Help.chm::/Sequencing.html>`__ topics
in the *NI DC Power Supplies and SMUs Help* for more information.

**Valid Values**: For PXIe-4162/4163, 0-10 seconds, for all other
supported devices, 0 to 167 seconds

**Default Value**: Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Settling Time <NI_DC_Power_Supplies_Help.chm::/SettlingTime.html>`__
''',
'note': '''
Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
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
Specifies whether to run a single output point or a sequence. Refer to
the `Single Point source
mode <NI_DC_Power_Supplies_Help.chm::/Singlept.html>`__ and `Sequence
source mode <NI_DC_Power_Supplies_Help.chm::/Sequencing.html>`__ topics
in the *NI DC Power Supplies and SMUs Help* for more information about
source modes.

**Default Value**: Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
},
    },
    1150055: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'AutoZero',
        'lv_property': 'Measurement:Auto Zero',
        'name': 'AUTO_ZERO',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the auto-zero method to use on the device.

Refer to the `NI PXI-4132 Measurement Configuration and
Timing <NI_DC_Power_Supplies_Help.chm::/4132_MeasureConfigTiming.html>`__
and `Auto Zero <NI_DC_Power_Supplies_Help.chm::/AutoZero.html>`__ topics
in the *NI DC Power Supplies and SMUs Help* for more information about
how to configure your measurements.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Auto Zero <NI_DC_Power_Supplies_Help.chm::/AutoZero.html>`__
''',
},
    },
    1150056: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Measurement:Fetch Backlog',
        'name': 'FETCH_BACKLOG',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the number of measurements acquired that have not been fetched
yet.
''',
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
Specifies when the measure unit should acquire measurements. Unless this
property is configured to **On Measure Trigger**, the `Measure Trigger
Type <pniDCPower_MeasureTriggerType.html>`__ property is ignored.

Refer to the `Acquiring
Measurements <NI_DC_Power_Supplies_Help.chm::/AcquiringMeasurements.html>`__
topic in the *NI DC Power Supplies and SMUs Help* for more information
about how to configure your measurements.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
},
    },
    1150058: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Measurement:Aperture Time',
        'name': 'APERTURE_TIME',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the measurement aperture time for the channel configuration.
Aperture time is specified in the units set by the `Aperture Time
Units <pniDCPower_ApertureTimeUnits.html>`__ property.

Refer to the `Aperture
Time <NI_DC_Power_Supplies_Help.chm::/Aperture.html>`__ topic in the *NI
DC Power Supplies and SMUs Help* for more information about how to
configure your measurements and for information about valid values.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Aperture Time <NI_DC_Power_Supplies_Help.chm::/Aperture.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150059: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'ApertureTimeUnits',
        'lv_property': 'Measurement:Aperture Time Units',
        'name': 'APERTURE_TIME_UNITS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the units of the `Aperture
Time <pniDCPower_ApertureTime.html>`__ property for the channel
configuration.

Refer to the `Aperture
Time <NI_DC_Power_Supplies_Help.chm::/Aperture.html>`__ topic in the *NI
DC Power Supplies and SMUs Help* for more information about how to
configure your measurements and for information about valid values.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Aperture Time <NI_DC_Power_Supplies_Help.chm::/Aperture.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150060: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Output Connected',
        'name': 'OUTPUT_CONNECTED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the output relay is connected (closed) or disconnected
(open). The `Output Enabled <pniDCPower_OutputEnabled.html>`__ property
does not change based on this property; they are independent of each
other.

Set this property to FALSE to disconnect the output terminal from the
output.

**Default Value**: Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
Only disconnect the output when disconnecting is necessary for your
application. For example, a battery connected to the output terminal
might discharge unless the relay is disconnected. Excessive connecting
and disconnecting of the output can cause premature wear on
electromechanical relays, such as those used by the NI PXI-4132 or NI
PXIe-4138/39.
''',
},
    },
    1150061: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Output Resistance',
        'name': 'OUTPUT_RESISTANCE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the output resistance that the device attempts to generate for
the specified channel(s). This property is available only when you set
the `Output Function <pniDCPower_OutputFunction.html>`__ property to
**DC Voltage**. Refer to `NI PXIe-4154 Programmable Output
Resistance <NI_DC_Power_Supplies_Help.chm::/4154_Prog_Output_Resist.html>`__
for more information about selecting an output resistance.

**Valid Values**: Vary by device. Refer to the device specifications or
the Programmable Output Resistance topic for your device for more
information about supported values.

**Default Value**: Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150062: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TransientResponse',
        'lv_property': 'Source:Transient Response',
        'name': 'TRANSIENT_RESPONSE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the transient response. Refer to the `Transient
Response <NI_DC_Power_Supplies_Help.chm::/Transient_Response.html>`__
topic in the *NI DC Power Supplies and SMUs Help* for more information
about transient response.

**Default Value**: Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Transient
Response <NI_DC_Power_Supplies_Help.chm::/Transient_Response.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150063: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Measurement:Measure Record Length',
        'name': 'MEASURE_RECORD_LENGTH',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies how many measurements compose a measure record. When this
property is set to a value greater than 1, the `Measure
When <pniDCPower_MeasureWhen.html>`__ property must be set to
**Automatically after Source Complete** or **On Measure Trigger**.

**Valid Values**: 1 to 16,777,216

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': 'This property is not available in a session involving multiple channels.',
},
    },
    1150064: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Measurement:Measure Record Length Is Finite',
        'name': 'MEASURE_RECORD_LENGTH_IS_FINITE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to take continuous measurements. Call the `niDCPower
Abort <NIDCPowerVIRef.chm::/niDCPower_Abort.html>`__ VI to stop
continuous measurements. When this property is set to FALSE and the
`Source Mode <pniDCPower_SourceMode.html>`__ property is set to **Single
Point**, the `Measure When <pniDCPower_MeasureWhen.html>`__ property
must be set to **Automatically after Source Complete** or **On Measure
Trigger**. When this property is set to FALSE and the Source Mode
property is set to **Sequence**, the Measure When property must be set
to **On Measure Trigger**.

**Default Value**: TRUE
''',
'note': 'This property is not available in a session involving multiple channels.',
},
    },
    1150065: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Measurement:Measure Record Delta Time',
        'name': 'MEASURE_RECORD_DELTA_TIME',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Queries the amount of time, in seconds, between the start of two
consecutive measurements in a measure record. Only query this property
after the desired measurement settings are committed.
''',
'note': '''
This property is not available when the `Auto
Zero <pniDCPower_AutoZero.html>`__ property is set to **Once** because
the amount of time between the first two measurements and the rest would
differ.
''',
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
Determines the relative weighting of samples in a measurement.

For information about improving noise immunity for NI-DCPower devices
that support DC noise rejection, refer to `Measurement Noise
Rejection <NI_DC_Power_Supplies_Help.chm::/noiseRejectMeasure.html>`__

**Default Value**: **Normal**

**Related topics:**

`Measurement Noise
Rejection <NI_DC_Power_Supplies_Help.chm::/NoiseRejectMeasure.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150067: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Custom Transient Response:Voltage:Gain Bandwidth',
        'name': 'VOLTAGE_GAIN_BANDWIDTH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
The frequency at which the unloaded loop gain extrapolates to 0 dB in
the absence of additional poles and zeroes. This property takes effect
when the channel is in `Constant
Voltage <NI_DC_Power_Supplies_Help.chm::/Constant_Voltage.html>`__ mode.

**Default Value**: Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150068: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Custom Transient Response:Voltage:Compensation Frequency',
        'name': 'VOLTAGE_COMPENSATION_FREQUENCY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
The frequency at which a pole-zero pair is added to the system when the
channel is in `Constant
Voltage <NI_DC_Power_Supplies_Help.chm::/Constant_Voltage.html>`__ mode.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150069: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Custom Transient Response:Voltage:Pole-Zero Ratio',
        'name': 'VOLTAGE_POLE_ZERO_RATIO',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
The ratio of the pole frequency to the zero frequency when the channel
is in `Constant
Voltage <NI_DC_Power_Supplies_Help.chm::/Constant_Voltage.html>`__ mode.

**Default Value**: Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150070: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Custom Transient Response:Current:Gain Bandwidth',
        'name': 'CURRENT_GAIN_BANDWIDTH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
The frequency at which the unloaded loop gain extrapolates to 0 dB in
the absence of additional poles and zeroes. This property takes effect
when the channel is in `Constant
Current <NI_DC_Power_Supplies_Help.chm::/Constant_Current.html>`__ mode.

**Default Value**: Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150071: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Custom Transient Response:Current:Compensation Frequency',
        'name': 'CURRENT_COMPENSATION_FREQUENCY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
The frequency at which a pole-zero pair is added to the system when the
channel is in `Constant
Current <NI_DC_Power_Supplies_Help.chm::/Constant_Current.html>`__ mode.

**Default Value**: Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150072: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Custom Transient Response:Current:Pole-Zero Ratio',
        'name': 'CURRENT_POLE_ZERO_RATIO',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
The ratio of the pole frequency to the zero frequency when the channel
is in `Constant
Current <NI_DC_Power_Supplies_Help.chm::/Constant_Current.html>`__ mode.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
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
Specifies whether the values calculated during self-calibration should
be written to hardware to be used until the next self-calibration or
only used until the `niDCPower Reset
Device <NIDCPowerVIRef.chm::/niDCPower_Reset_Device.html>`__ VI is
called or the machine is powered down.

This property affects the behavior of the `niDCPower Cal Self
Calibrate <NIDCPowerVIRef.chm::/niDCPower_Cal_Self_Calibrate.html>`__
VI. When set to **Keep in Memory**, the values calculated by the
niDCPower Cal Self Calibrate VI are used in the existing session, as
well as in all further sessions until you call the niDCPower Reset
Device VI or restart the machine. When you set this property to **Write
to EEPROM**, the values calculated by the niDCPower Cal Self Calibrate
VI are written to hardware and used in the existing session and in all
subsequent sessions until another call to the niDCPower Cal Self
Calibrate VI is made.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Self-Calibration <NI_DC_Power_Supplies_Help.chm::/selfcal.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150074: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Advanced:Active Advanced Sequence',
        'name': 'ACTIVE_ADVANCED_SEQUENCE',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': 'Specifies the advanced sequence to configure or generate.',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150075: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Advanced:Active Advanced Sequence Step',
        'name': 'ACTIVE_ADVANCED_SEQUENCE_STEP',
        'resettable': 'No',
        'type': 'ViInt64',
'documentation': {
'description': '''
Specifies the advanced sequence step to configure.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150077: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Measurement:Advanced:Measure Buffer Size',
        'name': 'MEASURE_BUFFER_SIZE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of samples that the active channel measurement
buffer can hold.

**The Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Valid Range**: 1000 to 2147483647

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150078: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Advanced:Sequence Loop Count Is Finite',
        'name': 'SEQUENCE_LOOP_COUNT_IS_FINITE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether a sequence should repeat indefinitely.

Refer to the `Sequence Source
Mode <NI_DC_Power_Supplies_Help.chm::/Sequencing.html>`__ topic in the
*NI DC Power Supplies and SMUs Help* for more information about infinite
sequencing.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices. When the Sequence Loop Count Is
Finite property is set to FALSE, the `Sequence Loop
Count <pniDCPower_SequenceLoopCount.html>`__ property is ignored.
''',
},
    },
    1150080: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Pulse Voltage:Pulse Voltage Level',
        'name': 'PULSE_VOLTAGE_LEVEL',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse voltage level, in volts, that the device attempts to
generate on the specified channel(s) during the on phase of a pulse.

This property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Voltage**.

**Valid Values:** The valid values for this property are defined by the
values you specify for the `Pulse Voltage Level
Range <pniDCPower_PulseVoltageLevelRange.html>`__ property.
''',
'note': '''
Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150081: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Pulse Voltage:Pulse Current Limit',
        'name': 'PULSE_CURRENT_LIMIT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse current limit, in amps, that the output cannot
exceed when generating the desired pulse voltage on the specified
channel(s) during the on phase of a pulse. Limit is specified as a
positive value, but symmetric positive and negative limits are enforced
simultaneously.

This property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Voltage**.

**Valid Values:** The valid values for this property are defined by the
values you specify for the `Pulse Current Limit
Range <pniDCPower_PulseCurrentLimitRange.html>`__ property.
''',
'note': '''
Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150082: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Pulse Voltage:Pulse Bias Voltage Level',
        'name': 'PULSE_BIAS_VOLTAGE_LEVEL',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse bias voltage level, in volts, that the device
attempts to generate on the specified channel(s) during the off phase of
a pulse.

This property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Voltage**.

**Valid Values:** The valid values for this property are defined by the
values you specify for the `Pulse Voltage Level
Range <pniDCPower_PulseVoltageLevelRange.html>`__ property.
''',
'note': '''
Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150083: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Pulse Voltage:Pulse Bias Current Limit',
        'name': 'PULSE_BIAS_CURRENT_LIMIT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse bias current limit, in amps, that the output cannot
exceed when generating the desired pulse bias voltage on the specified
channel(s) during the off phase of a pulse. Limit is specified as a
positive value, but symmetric positive and negative limits are enforced
simultaneously.

This property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Voltage**.

**Valid Values:** The valid values for this property are defined by the
values you specify for the `Pulse Current Limit
Range <pniDCPower_PulseCurrentLimitRange.html>`__ property.
''',
'note': '''
Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150084: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Pulse Voltage:Pulse Voltage Level Range',
        'name': 'PULSE_VOLTAGE_LEVEL_RANGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse voltage level range, in volts, for the specified
channel(s).

The range defines the valid values at which you can set the **pulse
voltage level** and **pulse bias voltage level**.

This property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Voltage**.

For valid ranges for your device, refer to
`Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.
''',
'note': '''
Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150085: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Pulse Voltage:Pulse Current Limit Range',
        'name': 'PULSE_CURRENT_LIMIT_RANGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse current limit range, in amps, for the specified
channel(s).

The range defines the valid values to which you can set the **pulse
current limit** and **pulse bias current limit**.

This property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Voltage**.

For valid ranges for your device, refer to
`Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.
''',
'note': '''
Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150086: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Pulse Current:Pulse Current Level',
        'name': 'PULSE_CURRENT_LEVEL',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse current level, in amps, that the device attempts to
generate on the specified channel(s) during the on phase of a pulse.

This property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Current**.

**Valid Values:** The valid values for this property are defined by the
values you specify for the `Pulse Current Level
Range <pniDCPower_PulseCurrentLevelRange.html>`__ property.
''',
'note': '''
Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150087: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Pulse Current:Pulse Voltage Limit',
        'name': 'PULSE_VOLTAGE_LIMIT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse voltage limit, in volts, that the output cannot
exceed when generating the desired pulse current on the specified
channel(s) during the on phase of a pulse. Limit is specified as a
positive value, but symmetric positive and negative limits are enforced
simultaneously.

This property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Current**.

**Valid Values:** The valid values for this property are defined by the
values you specify for the `Pulse Voltage Limit
Range <pniDCPower_PulseVoltageLimitRange.html>`__ property.
''',
'note': '''
Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150088: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Pulse Current:Pulse Bias Current Level',
        'name': 'PULSE_BIAS_CURRENT_LEVEL',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse bias current level, in amps, that the device
attempts to generate on the specified channel(s) during the off phase of
a pulse.

This property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Current**.

**Valid Values:** The valid values for this property are defined by the
values you specify for the `Pulse Current Level
Range <pniDCPower_PulseCurrentLevelRange.html>`__ property.
''',
'note': '''
Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150089: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Pulse Current:Pulse Bias Voltage Limit',
        'name': 'PULSE_BIAS_VOLTAGE_LIMIT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse voltage limit, in volts, that the output cannot
exceed when generating the desired current on the specified channel(s)
during the off phase of a pulse. Limit is specified as a positive value,
but symmetric positive and negative limits are enforced simultaneously.

This property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Current**.

**Valid Values:** The valid values for this property are defined by the
values you specify for the `Pulse Voltage Limit
Range <pniDCPower_PulseVoltageLimitRange.html>`__ property.
''',
'note': '''
Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150090: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Pulse Current:Pulse Current Level Range',
        'name': 'PULSE_CURRENT_LEVEL_RANGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse current level range, in amps, for the specified
channel(s).

The range defines the valid values to which you can set the **pulse
current level** and **pulse bias current level**.

The Pulse Current Level Range property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Current**.

For valid ranges for your device, refer to
`Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.
''',
'note': '''
Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150091: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Pulse Current:Pulse Voltage Limit Range',
        'name': 'PULSE_VOLTAGE_LIMIT_RANGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse voltage limit range, in volts, for the specified
channel(s).

The range defines the valid values to which you can set the **pulse
voltage limit** and **pulse bias voltage limit**.

This property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **Pulse
Current**.

For valid ranges for your device, refer to
`Ranges <NI_DC_Power_Supplies_Help.chm::/Ranges.html>`__.
''',
'note': '''
The channel must be enabled for the specified pulse current limit to
take effect. Refer to the `Output
Enabled <pniDCPower_OutputEnabled.html>`__ property for more information
about enabling the output channel.
''',
},
    },
    1150092: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Advanced:Pulse Bias Delay',
        'name': 'PULSE_BIAS_DELAY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Determines when, in seconds, the device generates the Pulse Complete
event after generating the off level of a pulse.

**Valid Values**: 0 to 167 seconds

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150093: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Advanced:Pulse On Time',
        'name': 'PULSE_ON_TIME',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Determines the length, in seconds, of the on phase of a pulse.

**Valid Values**:50 microseconds to 167 seconds

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150094: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Advanced:Pulse Off Time',
        'name': 'PULSE_OFF_TIME',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Determines the length, in seconds, of the off phase of a pulse.

**Valid Values**: 50 microseconds to 167 seconds

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
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

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
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
Specifies whether to configure the Pulse trigger to assert on the rising
or falling edge.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150097: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggers:Pulse Trigger:Digital Edge:Input Terminal',
        'name': 'DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the input terminal for the Pulse trigger. This property is
used only when the `Pulse Trigger
Type <pniDCPower_StartTriggerType.html>`__ property is set to **Digital
Edge**.

You can specify any valid input terminal for this property. Valid
terminals are listed in Measurement & Automation Explorer under the
**Device Routes** tab.

Input terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
shortened terminal name, PXI\_Trig0. The input terminal can also be a
terminal from another device. For example, you can set the input
terminal on Dev1 to be /Dev2/SourceCompleteEvent.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150098: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggers:Pulse Trigger:Export Output Terminal',
        'name': 'EXPORTED_PULSE_TRIGGER_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Pulse trigger.

Refer to the **Device Routes** tab in Measurement & Automation Explorer
for a list of the terminals available on your device.

Output terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
shortened terminal name, PXI\_Trig0.

**Related topics:**

`Triggers <NI_DC_Power_Supplies_Help.chm::/trigger.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150099: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Pulse Complete Event:Output Terminal',
        'name': 'PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Pulse Complete event.

Output terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
shortened terminal name, PXI\_Trig0.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
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

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150101: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Pulse Complete Event:Pulse:Width',
        'name': 'PULSE_COMPLETE_EVENT_PULSE_WIDTH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the width of the Pulse Complete event, in seconds.

The minimum event pulse width value for PXI Express devices is 250 ns.

The maximum event pulse width value for all devices is 1.6 microseconds.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150102: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Ready For Pulse Trigger Event:Output Terminal',
        'name': 'READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for exporting the Ready For Pulse Trigger
event.

Output terminals can be specified in one of two ways. If the device is
named Dev1 and your terminal is PXI\_Trig0, you can specify the terminal
with the fully qualified terminal name, /Dev1/PXI\_Trig0, or with the
shortened terminal name, PXI\_Trig0.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
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

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150104: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Ready For Pulse Trigger Event:Pulse:Width',
        'name': 'READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the width of the Ready For Pulse Trigger event, in seconds.

The minimum event pulse width value for PXI Express devices is 250 ns.

The maximum event pulse width value for all devices is 1.6 microseconds.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1150105: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Advanced:Interlock Input Open',
        'name': 'INTERLOCK_INPUT_OPEN',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Indicates whether the safety interlock circuit is open.

Refer to the `Safety
Interlock <NI_DC_Power_Supplies_Help.chm::/Interlock.html>`__ topic in
the *NI DC Power Supplies and SMUs Help* for more information about the
interlock circuit.

**Defined Values**
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
'table_body': [['FALSE', 'Safety interlock input is closed.'], ['TRUE', 'Safety interlock input is open.']],
},
    },
    1250001: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:DC Voltage:Voltage Level',
        'name': 'VOLTAGE_LEVEL',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the voltage level, in volts, that the device attempts to
generate on the specified channel(s).

This property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
Voltage**.

**Valid Values:** The valid values for this property are defined by the
values you specify for the `Voltage Level
Range <pniDCPower_VoltageLevelRange.html>`__ property.

**Related topics:**

`Constant Voltage
Mode <NI_DC_Power_Supplies_Help.chm::/Constant_Voltage.html>`__
''',
'note': '''
The channel must be enabled for the specified voltage level to take
effect. Refer to the `Output Enabled <pniDCPower_OutputEnabled.html>`__
property for more information about enabling the output channel.
''',
},
    },
    1250002: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Advanced:OVP Enabled',
        'name': 'OVP_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables (TRUE) or disables (FALSE) overvoltage protection (OVP).

Refer to `Output Overvoltage
Protection <NI_DC_Power_Supplies_Help.chm::/OutputOvervoltageProtection.html>`__
for more information about overvoltage protection.

**Defined Values**

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`NI PXIe-4154
Protection <NI_DC_Power_Supplies_Help.chm::/4154_Protection.html>`__

`PXIe-4135
Protection <NI_DC_Power_Supplies_Help.chm::/4135_Protection.html>`__

`NI PXIe-4136/4137
Protection <NI_DC_Power_Supplies_Help.chm::/4136_4137_Protection.html>`__

`Output Overvoltage
Protection <NI_DC_Power_Supplies_Help.chm::/OutputOvervoltageProtection.html>`__
''',
'note': '''
This property is not supported by all devices. Refer to `Supported
Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
'table_body': [['FALSE', 'Overvoltage protection is disabled.'], ['TRUE', 'Overvoltage protection is enabled.']],
},
    },
    1250003: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Advanced:OVP Limit',
        'name': 'OVP_LIMIT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Determines the voltage limit, in volts, beyond which overvoltage
protection (OVP) engages. Limit is specified as a positive value, but
symmetric positive and negative limits are enforced simultaneously. For
example, setting the OVP Limit to 65 will configure the OVP feature to
trigger an OVP error if the output exceeds ±65 V.

**Valid Values**:Vary by device.

**Default Value**:Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.

**Related topics:**

`PXIe-4135
Protection <NI_DC_Power_Supplies_Help.chm:://4135_Protection.html>`__

`NI PXIe-4136/4137
Protection <NI_DC_Power_Supplies_Help.chm::/4136_4137_Protection.html>`__
''',
'note': '''
Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
information about supported devices.
''',
},
    },
    1250005: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:DC Voltage:Current Limit',
        'name': 'CURRENT_LIMIT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the current limit, in amps, that the output cannot exceed when
generating the desired voltage on the specified channel(s). Limit is
specified as a positive value, but symmetric positive and negative
limits are enforced simultaneously.

This property is applicable only if the `Output
Function <pniDCPower_OutputFunction.html>`__ property is set to **DC
Voltage**.

**Valid Values:** The valid values for this property are defined by the
values to which the `Current Limit
Range <pniDCPower_CurrentLimitRange.html>`__ property is set.

**Related topics:**

`Compliance <NI_DC_Power_Supplies_Help.chm::/compliance.html>`__
''',
'note': '''
The channel must be enabled for the specified current limit to take
effect. Refer to the `Output Enabled <pniDCPower_OutputEnabled.html>`__
property for more information about enabling the output channel.
''',
},
    },
    1250006: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Source:Output Enabled',
        'name': 'OUTPUT_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the output is enabled (TRUE) or disabled (FALSE).

Depending on the value you specify for the `Output
Function <pniDCPower_OutputFunction.html>`__ property, you also must set
the voltage level or current level in addition to enabling the output.

This property has no effect on the output disconnect relay. To toggle
the relay, use the `Output
Connected <pniDCPower_OutputConnected.html>`__ property.

**Default Value**: Refer to `Supported Properties by
Device <NI_DC_Power_Supplies_Help.chm::/SupportedProperties.html>`__ for
the default value by device.
''',
'note': '''
If the session is in the Committed or Uncommitted states, enabling the
output does not take effect until you call the `niDCPower
Initiate <NIDCPowerVIRef.chm::/niDCPower_Initiate.html>`__ VI. Refer to
the `Programming
States <NI_DC_Power_Supplies_Help.chm::/programmingStates.html>`__ topic
in the *NI DC Power Supplies and SMUs Help* for more information about
NI-DCPower programming states.
''',
},
    },
}
