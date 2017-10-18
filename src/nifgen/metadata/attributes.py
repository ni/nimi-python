
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
        'lv_property': 'Instrument:Inherent IVI Attributes:User Options:Range Check',
        'name': 'RANGE_CHECK',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to validate property values and VI parameters. Set
this property to TRUE to enable range-checking.

If enabled, in some cases, NI-FGEN does extra validation of parameter
values that you pass to NI-FGEN VIs. Range checking parameters is useful
for debugging. After you validate your program, you can set this
property to FALSE to disable range checking and maximize performance.

Use the `niFgen Initialize With
Options <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize_With_Options.html')>`__
VI to override the value of this property.

**Default Value**: TRUE
''',
},
    },
    1050003: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Inherent IVI Attributes:User Options:Query Instrument Status',
        'name': 'QUERY_INSTRUMENT_STATUS',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether NI-FGEN retains instrument status after each
operation. Set this property to TRUE to query the instrument status.

Querying the instrument status is very useful for debugging. After you
validate your program, you can set this property to FALSE to disable
status checking and maximize performance. However, the effect on NI-FGEN
is minor.

NI-FGEN can choose to ignore status checking for particular properties
regardless of the setting of this property. Use the `niFgen Initialize
With
Options <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize_With_Options.html')>`__
VI to override this value.

**Default Value**: TRUE
''',
},
    },
    1050004: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Inherent IVI Attributes:User Options:Cache',
        'name': 'CACHE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to cache the value of properties.

When caching is enabled (TRUE), NI-FGEN keeps track of the current
instrument settings and avoids sending redundant commands to the
instrument. Thus, you can significantly increase execution speed.
NI-FGEN can choose always to cache or never to cache particular
properties regardless of the setting of this property. Use the `niFgen
Initialize With
Options <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize_With_Options.html')>`__
VI to override this value.

**Default Value**: TRUE
''',
},
    },
    1050005: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Inherent IVI Attributes:User Options:Simulate',
        'name': 'SIMULATE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether or not to simulate NI-FGEN I/O operations. Set this
property to TRUE to enable simulation.

If simulation is enabled, NI-FGEN VIs perform range checking and can get
and set properties, but they do not perform instrument I/O. For output
parameters that represent instrument data, NI-FGEN VIs return calculated
values.

Use the `niFgen Initialize With
Options <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize_With_Options.html')>`__
VI to override the value of this property.

**Default Value**: FALSE
''',
},
    },
    1050006: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Inherent IVI Attributes:User Options:Record Value Coercions',
        'name': 'RECORD_COERCIONS',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the IVI engine keeps a list of the value coercions it
makes for ViInt32 and ViReal64 properties. Set this property to TRUE to
record the coercions. Use the `niFgen Initialize With
Options <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize_With_Options.html')>`__
VI to override this value.

**Default Value**: FALSE
''',
},
    },
    1050021: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Inherent IVI Attributes:User Options:Interchange Check',
        'name': 'INTERCHANGE_CHECK',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether to perform interchangeability checking and log
interchangeability warnings when you call VIs. Set this property to TRUE
to enable interchangeability checking.

Interchangeability warnings indicate that using your application with a
different instrument might cause different behavior. Interchangeability
checking examines the properties in a capability group only if you
specify a value for at least one property within that group.
Interchangeability warnings can occur when a property affects the
behavior of the instrument and you have not set that property or the
property has been invalidated since you set it.
''',
},
    },
    1050101: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Obsolete:Primary Error',
        'name': 'PRIMARY_ERROR',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Describes the first error that occurred since the last call to the
`niFgen Error
Message <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Error_Message.html')>`__
VI on the session.

The value follows the VXIplug&play completion code conventions. A
negative value (0x80000000 or higher in hex) describes an error
condition. A positive value describes a warning condition and indicates
that no error occurred. A zero indicates that no error or warning
occurred. The error and warning values can be status codes defined by
IVI, VISA, class drivers, or specific drivers.
''',
},
    },
    1050102: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Obsolete:Secondary Error',
        'name': 'SECONDARY_ERROR',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Provides an optional code with additional information concerning the
primary error condition. The error and warning values can be status
codes defined by IVI, VISA, class drivers, or specific drivers. Zero
indicates no additional information.
''',
},
    },
    1050103: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Obsolete:Error Elaboration',
        'name': 'ERROR_ELABORATION',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Contains an optional string with additional information concerning the
primary error condition.
''',
},
    },
    1050203: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Capabilities:Channel Count',
        'name': 'CHANNEL_COUNT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the number of channels that NI-FGEN supports. For each property
for which IVI\_VAL\_MULTI\_CHANNEL is set, the IVI engine maintains a
separate cache value for each channel.
''',
},
    },
    1050302: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Identification:Driver Prefix',
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Contains the prefix for NI-FGEN. The name of each user-callable VI in
NI-FGEN starts with this prefix.
''',
},
    },
    1050304: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Inherent IVI Attributes:Advanced Session Information:Resource Descriptor',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Returns the resource descriptor NI-FGEN uses to identify the physical
device.

If you initialize NI-FGEN with a logical name, this property contains
the resource descriptor that corresponds to the entry in the IVI
Configuration utility.

If you initialize NI-FGEN with the resource descriptor, this property
contains that value.
''',
},
    },
    1050305: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Inherent IVI Attributes:Advanced Session Information:Logical Name',
        'name': 'LOGICAL_NAME',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Returns the logical name you specified when opening the current IVI
session.

You may pass a logical name to the `niFgen
Initialize <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize.html')>`__
VI or the `niFgen Initialize With
Options <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initialize_With_Options.html')>`__
VI. The IVI Configuration utility must contain an entry for the logical
name. The logical name entry refers to a virtual instrument section in
the IVI Configuration file. The virtual instrument section specifies a
physical device and initial user options.
''',
},
    },
    1050327: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Returns a model code of the instrument. For drivers that support more
than one device, this property contains a comma-separated list of
supported instrument models.
''',
},
    },
    1050401: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities',
        'name': 'GROUP_CAPABILITIES',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Returns a comma-separated list of class-extension groups that NI-FGEN
implements.
''',
},
    },
    1050503: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Obsolete:Major Version',
        'name': 'MAJOR_VERSION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Returns the major version number of NI-FGEN.',
},
    },
    1050504: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Obsolete:Minor Version',
        'name': 'MINOR_VERSION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Returns the minor version number of NI-FGEN.',
},
    },
    1050510: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Inherent IVI Attributes:Instrument Identification:Firmware Revision',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Returns the firmware revision information for the instrument you are
currently using.
''',
},
    },
    1050511: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Inherent IVI Attributes:Instrument Identification:Manufacturer',
        'name': 'INSTRUMENT_MANUFACTURER',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': 'Returns the name of the instrument manufacturer you are currently using.',
},
    },
    1050512: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Inherent IVI Attributes:Instrument Identification:Model',
        'name': 'INSTRUMENT_MODEL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Returns the model number or name of the instrument that you are
currently using.
''',
},
    },
    1050513: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Identification:Driver Vendor',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': 'Contains the name of the vendor that supplies NI-FGEN.',
},
    },
    1050514: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Identification:Description',
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
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Identification:Class Specification Major Version',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the major version number of the class specification with which
NI-FGEN is compliant.
''',
},
    },
    1050516: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Identification:Class Specification Minor Version',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the minor version number of the class specification with which
NI-FGEN is compliant.
''',
},
    },
    1050551: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Identification:Revision',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': 'Contains additional version information about NI-FGEN.',
},
    },
    1150101: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Output:Advanced:Digital Pattern Enabled',
        'name': 'DIGITAL_PATTERN_ENABLED',
        'resettable': 'Yes',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the signal generator generates a digital pattern
corresponding to the output signal. Set this property to TRUE to
generate a digital pattern.
''',
},
    },
    1150102: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Output:Filters:Digital Filter Enabled',
        'name': 'DIGITAL_FILTER_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the signal generator applies a digital filter to the
output signal. Set this property to TRUE to use a digital filter. This
property is valid in Arbitrary Waveform, Arbitrary Sequence, and Script
output modes. You also can use this property in Standard Function and
Frequency List output modes for user-defined waveforms.

**Default Value**: FALSE
''',
},
    },
    1150103: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Output:Filters:Analog Filter Enabled',
        'name': 'ANALOG_FILTER_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the signal generator applies an analog filter to the
output signal. Set this property to TRUE to enable the filter. This
property is valid in Arbitrary Waveform, Arbitrary Sequence, and Script
output modes. You also can use this property in Standard Function and
Frequency List output modes for user-defined waveforms.

**Default Value**: FALSE
''',
},
    },
    1150104: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:5401/5411/5431:Filter Correction Frequency',
        'name': 'FILTER_CORRECTION_FREQUENCY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the filter correction frequency of the analog filter. This
property can correct for the ripples in the analog filter frequency
response at the frequency specified.

When using the Standard Waveform output mode, this property should be
set to the same frequency as the standard waveform. To disable filter
correction, set this property to 0.

**Units**: hertz (Hz)

**Default Value**: 0
''',
},
    },
    1150105: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Standard Function:Sync Duty Cycle High',
        'name': 'SYNC_DUTY_CYCLE_HIGH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the duty cycle of the square wave the signal generator
produces on the SYNC OUT connector. Specify this property as a
percentage of the time the square wave is high in each cycle.

**Units**: Percentage of time the waveform is high

**Default Value**: 50%
''',
},
    },
    1150106: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'UpdateClockSource',
        'lv_property': 'Instrument:Obsolete:Update Clock Source',
        'name': 'UPDATE_CLOCK_SOURCE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Controls the Update Clock source.',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150107: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocks:Reference Clock:Frequency',
        'name': 'REF_CLOCK_FREQUENCY',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the Reference Clock frequency. The signal generator uses the
Reference Clock to derive frequencies and sample rates when generating
output.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150108: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TriggerMode',
        'lv_property': 'Triggers:Trigger Mode',
        'name': 'TRIGGER_MODE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Controls the trigger mode.

**Default Value**: **NIFGEN\_VAL\_CONTINUOUS**
''',
},
    },
    1150109: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Obsolete:Actual Arb Sample Rate',
        'name': 'ACTUAL_ARB_SAMPLE_RATE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Returns the actual sample rate value of the signal generator after any
coercion or rounding.
''',
},
    },
    1150110: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'ClockMode',
        'lv_property': 'Clocks:Sample Clock:Mode',
        'name': 'CLOCK_MODE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the Sample Clock mode for the signal generator.

For signal generators that support it, this property allows switching
the Sample Clock to a high-resolution clocking mode. When in divide-down
sampling mode, the sample rate can be set only to certain frequencies,
based on dividing down the Sample Clock. However, in high-resolution
mode, the sample rate may be set to any value.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150111: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'SynchronizationSource',
        'lv_property': 'Instrument:5401/5411/5431:Synchronization Source',
        'name': 'SYNCHRONIZATION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the source of the synchronization signal to use.',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150112: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'SampleClockSource',
        'lv_property': 'Clocks:Sample Clock:Source',
        'name': 'SAMPLE_CLOCK_SOURCE',
        'resettable': 'Yes',
        'type': 'ViString',
'documentation': {
'description': 'Specifies the Sample Clock source.',
'note': '''
The signal generator must not be in the Generating state when you change
this property. To change the device configuration, call the `niFgen
Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150113: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'ReferenceClockSource',
        'lv_property': 'Clocks:Reference Clock:Source',
        'name': 'REFERENCE_CLOCK_SOURCE',
        'resettable': 'Yes',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the Reference Clock source used by the signal generator.

The signal generator derives the frequencies and sample rates that it
uses to generate waveforms from the source you specify. For example,
when you set this property to **Clock In**, the signal generator uses
the signal it receives at its CLK In front panel connector as its
Reference Clock.
''',
'note': '''
The signal generator must not be in the Generating state when you change
this property. To change the device configuration, call the `niFgen
Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150208: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Standard Function:Frequency List Mode:Frequency List Handle',
        'name': 'FREQ_LIST_HANDLE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Sets which frequency list the signal generator produces. You create a
frequency list using the `niFgen Create Frequency
List <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Create_Frequency_List.html')>`__
VI. The niFgen Create Frequency List VI returns a handle that you use to
identify the list.

**Default Value**: None
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150209: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Standard Function:Frequency List Mode:Maximum Number Of Frequency Lists',
        'name': 'MAX_NUM_FREQ_LISTS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the maximum number of frequency lists that the signal generator
allows.
''',
},
    },
    1150210: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Standard Function:Frequency List Mode:Minimum Frequency List Length',
        'name': 'MIN_FREQ_LIST_LENGTH',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the minimum number of frequency lists that the signal generator
allows.
''',
},
    },
    1150211: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Standard Function:Frequency List Mode:Maximum Frequency List Length',
        'name': 'MAX_FREQ_LIST_LENGTH',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Returns the maximum number of steps that can be in a frequency list.',
},
    },
    1150212: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Standard Function:Frequency List Mode:Minimum Frequency List Duration',
        'name': 'MIN_FREQ_LIST_DURATION',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Returns the minimum duration, in seconds, of any one step in a frequency
list.
''',
},
    },
    1150213: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Standard Function:Frequency List Mode:Maximum Frequency List Duration',
        'name': 'MAX_FREQ_LIST_DURATION',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Returns the maximum duration, in seconds, of any one step in the
frequency list.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150214: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Standard Function:Frequency List Mode:Frequency List Duration Quantum',
        'name': 'FREQ_LIST_DURATION_QUANTUM',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Returns the quantum that all durations must be a multiple of in a
frequency list.
''',
},
    },
    1150215: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': 'BusType',
        'lv_property': 'Instrument:Bus Type',
        'name': 'BUS_TYPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Returns the bus type of the signal generator.',
},
    },
    1150216: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'VideoWaveformType',
        'lv_property': 'Instrument:5401/5411/5431:Video Waveform Type',
        'name': 'VIDEO_WAVEFORM_TYPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the waveform type the NI 5431 generates. Setting this property
ensures the oscillator crystal is set to the proper frequency.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150218: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Output:Filters:Digital Filter Interpolation Factor',
        'name': 'DIGITAL_FILTER_INTERPOLATION_FACTOR',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the interpolation factor when the `Digital Filter
Enabled <pniFgen_DigitalFilterEnabled.html>`__ property is set to TRUE.

**Valid Values**: 2, 4, and 8
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150219: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocks:Sample Clock:Exported Sample Clock Divisor',
        'name': 'EXPORTED_SAMPLE_CLOCK_DIVISOR',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the factor by which to divide the update (Sample) Clock before
it is exported.

To export the Sample Clock, use the `niFgen Export
Signal <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Export_Signal.html')>`__
VI or the `Exported Sample Clock Output
Terminal <pniFgen_ExportedSampleClockOutputTerminal.html>`__ property.

**Valid Values**: 1 to 4,096

**Default Value**: 1
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150220: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Output:Load Impedance',
        'name': 'LOAD_IMPEDANCE',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the load impedance connected to the analog output of the
channel.

If the load impedance is set to -1.0, NI-FGEN matches the load impedance
to the `Output Impedance <pniFgen_OutputImpedance.html>`__ property
value. NI-FGEN compensates to give the desired peak-to-peak voltage
amplitude or arbitrary gain (relative to 1 V).
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150221: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Obsolete:DAQmx Task',
        'name': 'DAQMX_TASK',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Returns the NI-DAQmx task pointer.',
},
    },
    1150222: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'AnalogPath',
        'lv_property': 'Output:Analog Path',
        'name': 'ANALOG_PATH',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the analog signal path. The main path allows the user to
configure gain, offset, analog filter status, output impedance, and
output enable.

The direct path presents a much smaller gain range, and you cannot
adjust offset or the filter status. The direct path provides a smaller
output range but lower distortion. The main path has two amplifier
options, high and low gain. Setting this value to
**NIFGEN\_VAL\_MAIN\_ANALOG\_PATH** allows NI-FGEN to choose the
amplifier based on the user-specified gain.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150223: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Calibration:Gain DAC Value',
        'name': 'GAIN_DAC_VALUE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the value programmed to the Gain DAC. The value should be
treated as an unsigned, right-justified number.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150224: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Calibration:Offset DAC Value',
        'name': 'OFFSET_DAC_VALUE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the value programmed to the Offset DAC. The value should be
treated as an unsigned, right-justified number.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150225: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Calibration:Oscillator Freq DAC Value',
        'name': 'OSCILLATOR_FREQ_DAC_VALUE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the value programmed to the Oscillator DAC. The value should
be treated as an unsigned, right-justified number.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150227: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'CalADCInput',
        'lv_property': 'Instrument:Calibration:Cal ADC Input',
        'name': 'CAL_ADC_INPUT',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the input of the calibration ADC. The ADC can take a reading
from several inputs: the analog output, a 2.5 V reference, and ground.
The latter two inputs are used to calibrate the ADC itself.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150228: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Calibration:Pre-Amplifier Attenuation',
        'name': 'PRE_AMPLIFIER_ATTENUATION',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the amount of preamplifier attenuation to apply to the signal,
in dB.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150229: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Calibration:Post-Amplifier Attenuation',
        'name': 'POST_AMPLIFIER_ATTENUATION',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the amount of post-amplifier attenuation to apply to the
signal, in dB.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150230: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocks:Sample Clock Timebase:Exported Sample Clock Timebase Divisor',
        'name': 'EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the factor by which to divide the device clock (Sample Clock
timebase) before it is exported.

To export the Sample Clock timebase, use the `niFgen Export
Signal <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Export_Signal.html')>`__
VI or the `Exported Sample Clock Timebase Output
Terminal <pniFgen_ExportedSampleClockTimebaseOutputTerminal.html>`__
property.

**Valid Values**: 1 to 4,194,304
''',
'note': 'Not all devices support a divisor value of 1.',
},
    },
    1150231: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocks:Advanced:Sample Clock Absolute Delay',
        'name': 'SAMPLE_CLOCK_ABSOLUTE_DELAY',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the delay in seconds to apply to an external Sample Clock.
This property is useful when trying to align the output of two devices.
''',
'note': '''
For the NI 5421, absolute delay can only be applied when an external
Sample Clock is used.
''',
},
    },
    1150232: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocks:Advanced:Oscillator Phase DAC Value',
        'name': 'OSCILLATOR_PHASE_DAC_VALUE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the oscillator phase DAC value.',
},
    },
    1150233: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocks:Advanced:External Clock Delay Binary Value',
        'name': 'EXTERNAL_CLOCK_DELAY_BINARY_VALUE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the external clock delay binary value.',
},
    },
    1150234: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Output:Data Mask:Analog Data Mask',
        'name': 'ANALOG_DATA_MASK',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the mask to apply to the analog output data. The masked data
is replaced with the data in the `Analog Static
Value <pniFgen_AnalogStaticValue.html>`__ property.
''',
},
    },
    1150235: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Output:Data Mask:Analog Static Value',
        'name': 'ANALOG_STATIC_VALUE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the static value that replaces data masked by the `Analog Data
Mask <pniFgen_AnalogDataMask.html>`__ property.
''',
},
    },
    1150236: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Output:Data Mask:Digital Data Mask',
        'name': 'DIGITAL_DATA_MASK',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the mask to apply to the output on the digital connector. The
masked data is replaced with the data in the `Digital Static
Value <pniFgen_DigitalStaticValue.html>`__ property.
''',
},
    },
    1150237: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Output:Data Mask:Digital Static Value',
        'name': 'DIGITAL_STATIC_VALUE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the static value that replaces data masked by the `Digital
Data Mask <pniFgen_DigitalDataMask.html>`__ property.
''',
},
    },
    1150238: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Standard Function:Standard Function Mode:Buffer Size',
        'name': 'FUNC_BUFFER_SIZE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Contains the number of samples used in the standard function waveform
buffer.

This property is valid only on devices that implement Standard Function
output mode in software, and it is read-only for all other devices.
''',
'note': '''
Refer to the `Standard Function
Mode <javascript:LaunchHelp('SigGenHelp.chm::/Function_Generation_Mode.html')>`__
topic in the *NI Signal Generators Help* for more information about the
implementation of Standard Function output mode on your device.
''',
},
    },
    1150239: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Standard Function:Standard Function Mode:Maximum Buffer Size',
        'name': 'FUNC_MAX_BUFFER_SIZE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Sets the maximum number of samples that can be used in the standard
function waveform buffer. Increasing this value may increase the quality
of the waveform but may also increase the amount of time required to
change the waveform while running.

This property is valid only on devices that implement Standard Function
output mode in software, and it is read-only for all other devices.
''',
'note': '''
Refer to the `Standard Function
Mode <javascript:LaunchHelp('SigGenHelp.chm::/Function_Generation_Mode.html')>`__
topic in the *NI Signal Generators Help* for more information about the
implementation of Standard Function output mode on your device.
''',
},
    },
    1150240: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Data Transfer:File Transfer Block Size',
        'name': 'FILE_TRANSFER_BLOCK_SIZE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the maximum number of samples to transfer at one time from the
device to host memory. This property is used in conjunction with the
`niFgen Create Waveform From
File <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Create_Waveform_poly.html')>`__
VI and the `niFgen Write Waveform From
File <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Write_Waveform_poly.html')>`__
VI.

If the requested value is not evenly divisible by the required
increment, this property is coerced up to the next 64-sample increment
(32-sample increment for complex samples).
''',
},
    },
    1150241: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Data Transfer:Data Transfer Block Size',
        'name': 'DATA_TRANSFER_BLOCK_SIZE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of samples at a time to download to onboard memory.
This property is useful when the total data to be transferred to onboard
memory is large.
''',
},
    },
    1150242: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Memory Size',
        'name': 'MEMORY_SIZE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Returns the amount of memory in bytes on the signal generator.',
},
    },
    1150243: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Serial Number',
        'name': 'SERIAL_NUMBER',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': 'Returns the serial number of the signal generator.',
},
    },
    1150244: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Data Transfer:Direct DMA:Direct DMA Enabled',
        'name': 'DIRECT_DMA_ENABLED',
        'resettable': 'Yes',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables the device for Direct DMA writes.

When enabled, all `niFgen Create
Waveform <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Create_Waveform_poly.html')>`__
VI and `niFgen Write
Waveform <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Write_Waveform_poly.html')>`__
VI calls that are given a data address in the Direct DMA window download
data residing on the Direct DMA device to the instrument onboard memory.
''',
},
    },
    1150245: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Data Transfer:Direct DMA:Window Size in Bytes',
        'name': 'DIRECT_DMA_WINDOW_SIZE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the size of the memory window provided by your Direct
DMA-compatible data source.
''',
},
    },
    1150246: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:OSP Enabled',
        'name': 'OSP_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables (TRUE) or disables (FALSE) the OSP block of the signal
generator. When the OSP block is disabled, all OSP-related properties
are disabled and have no effect on the generated signal.
''',
},
    },
    1150247: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'DataProcessingMode',
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Data Processing Mode',
        'name': 'OSP_DATA_PROCESSING_MODE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Controls the way that data is processed by the OSP block.',
'note': '''
When using the NI 5450/5451 with I/Q rates higher than 200 MS/s, NI-FGEN
restricts this property value to Complex.
''',
},
    },
    1150248: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:IQ Rate',
        'name': 'OSP_IQ_RATE',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the rate at which the user-provided waveform data is generated
when the `OSP Enabled <pniFgen_OSPEnabled.html>`__ property is set to
TRUE.

NI-FGEN sets the `Sample Rate <pniFgen_SampleRate.html>`__ property of
the signal generator to the product of the IQ Rate, `FIR Interpolation
Factor <pniFgen_FIRInterpolation.html>`__, and `CIC Interpolation
Factor <pniFgen_CICInterpolation.html>`__ properties. When the `Data
Processing Mode <pniFgen_DataProcessingMode.html>`__ property is set to
**Real**, the IQ Rate value is the rate at which the signal generator
processes real (I) data. When the Data Processing Mode property is set
to **Complex**, the IQ Rate value is the rate at which the signal
generator processes complex (I/Q) data.
''',
},
    },
    1150249: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Carrier Enabled',
        'name': 'OSP_CARRIER_ENABLED',
        'resettable': 'Yes',
        'type': 'ViBoolean',
'documentation': {
'description': 'Enables (TRUE) or disables (FALSE) generation of the carrier.',
},
    },
    1150250: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Carrier Frequency',
        'name': 'OSP_CARRIER_FREQUENCY',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': 'Specifies the frequency of the generated carrier.',
},
    },
    1150251: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Carrier Phase:Carrier Phase I',
        'name': 'OSP_CARRIER_PHASE_I',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the I carrier phase, in degrees, at the first point of the
generated signal.

**Default Value**: 0.0
''',
},
    },
    1150252: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Carrier Phase:Carrier Phase Q',
        'name': 'OSP_CARRIER_PHASE_Q',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the Q carrier phase, in degrees, at the first point of the
generated signal. This property is used only when the `Data Processing
Mode <pniFgen_DataProcessingMode.html>`__ property is set to
**Complex**.

**Default Value**: -90.0
''',
},
    },
    1150253: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'FilterType',
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Filter Type',
        'name': 'OSP_FIR_FILTER_TYPE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the pulse-shaping filter type for the FIR filter.',
},
    },
    1150254: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Output:Digital Gain',
        'name': 'DIGITAL_GAIN',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies a factor by which the signal generator digitally multiplies
generated data before converting it to an analog signal in the DAC. For
a digital gain greater than 1.0, the product of digital gain times the
generated data must be inside the range ±1.0, assuming floating point
data. If the product exceeds these limits, the signal generator clips
the output signal, and an error results.

Some signal generators support both digital gain and analog gain,
specified with the `Amplitude <pniFgen_Amplitude.html>`__ property or
`Arbitrary Waveform Gain <pniFgen_ArbitraryWaveformGain.html>`__
property. Digital gain can be changed during generation without the
glitches that may occur when changing analog gains, because of relay
switching. However, the DAC output resolution is a function of analog
gain, so only analog gain makes full use of the resolution of the DAC.

**Default Value**: 1
''',
},
    },
    1150255: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Advanced:FIR Filter Enabled',
        'name': 'OSP_FIR_FILTER_ENABLED',
        'resettable': 'Yes',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specify TRUE to enables the FIR filter. Specify FALSE to disable the FIR
filter.
''',
'note': '''
You must set the `CIC Filter Enabled <pniFgen_CICFilterEnabled.html>`__
property and the FIR Filter Enabled property to the same value.
''',
},
    },
    1150256: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Advanced:FIR Interpolation Factor',
        'name': 'OSP_FIR_FILTER_INTERPOLATION',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the interpolation factor for the FIR filter. If you do not set
this value, NI-FGEN calculates the appropriate value based on the value
of the `IQ Rate <pniFgen_IQRate.html>`__ property.
''',
},
    },
    1150257: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Advanced:CIC Filter Enabled',
        'name': 'OSP_CIC_FILTER_ENABLED',
        'resettable': 'Yes',
        'type': 'ViBoolean',
'documentation': {
'description': 'Enables (TRUE) or disables (FALSE) the CIC filter.',
'note': '''
You must set the CIC Filter Enabled and `FIR Filter
Enabled <pniFgen_FIRFilterEnabled.html>`__ properties to the same value.
''',
},
    },
    1150258: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Advanced:CIC Interpolation Factor',
        'name': 'OSP_CIC_FILTER_INTERPOLATION',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the interpolation factor for the CIC filter. If you do not set
this value, NI-FGEN calculates the appropriate value based on the value
of the `IQ Rate <pniFgen_IQRate.html>`__ property.
''',
},
    },
    1150259: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Root Raised Cosine:Alpha',
        'name': 'OSP_FIR_FILTER_ROOT_RAISED_COSINE_ALPHA',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the alpha value to use when calculating the pulse-shaping FIR
filter coefficients. This property is used only when the `Filter
Type <pniFgen_FilterType.html>`__ property is set to **Root Raised
Cosine**.
''',
},
    },
    1150260: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Raised Cosine:Alpha',
        'name': 'OSP_FIR_FILTER_RAISED_COSINE_ALPHA',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the alpha value to use when calculating the pulse-shaping FIR
filter coefficients. This property is used only when the `Filter
Type <pniFgen_FilterType.html>`__ property is set to **Raised Cosine**.
''',
},
    },
    1150261: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Flat:Passband',
        'name': 'OSP_FIR_FILTER_FLAT_PASSBAND',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the passband value to use when calculating the FIR filter
coefficients. The FIR filter is designed to be flat to passband × I/Q
rate. This property is used only when the `Filter
Type <pniFgen_FilterType.html>`__ property is set to **Flat**.
''',
},
    },
    1150262: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Gaussian:BT',
        'name': 'OSP_FIR_FILTER_GAUSSIAN_BT',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the BT value to use when calculating the pulse-shaping FIR
filter coefficients. The BT value is the product of the -3 dB bandwidth
and the symbol period. This property is used only when the `Filter
Type <pniFgen_FilterType.html>`__ property is set to **Gaussian**.
''',
},
    },
    1150263: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Advanced:CIC Filter Gain',
        'name': 'OSP_CIC_FILTER_GAIN',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the gain applied at the final stage of the CIC filter. This
property is commonly used to compensate for attenuation in the FIR
filter. If you set the `FIR Filter Type <pniFgen_FilterType.html>`__ to
a value other than **Custom**, NI-FGEN calculates the CIC gain to
achieve unity gain between the FIR and CIC filters. Setting this
property overrides the value set by NI-FGEN.
''',
},
    },
    1150264: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Gain:Pre-filter Gain I',
        'name': 'OSP_PRE_FILTER_GAIN_I',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the digital gain to apply to the I data stream before any
filtering by the OSP block.

**Valid Values**: -2.0 to 2.0

**Default Value**: 1.0
''',
},
    },
    1150265: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Gain:Pre-filter Gain Q',
        'name': 'OSP_PRE_FILTER_GAIN_Q',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the digital gain to apply to the Q data stream before any
filtering by the OSP block. This property is used only when the `Data
Processing Mode <pniFgen_DataProcessingMode.html>`__ property is set to
**Complex**.

**Valid Values**: -2.0 to 2.0

**Default Value**: 1.0
''',
},
    },
    1150266: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Offset:Pre-filter Offset I',
        'name': 'OSP_PRE_FILTER_OFFSET_I',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the digital offset to apply to the I data stream. This offset
is applied after the prefilter gain and before any filtering.

**Valid Values**: -1.0 to 1.0

**Default Value**: 0.9
''',
},
    },
    1150267: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Offset:Pre-filter Offset Q',
        'name': 'OSP_PRE_FILTER_OFFSET_Q',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the digital offset to apply to the Q data stream. This offset
is applied after the prefilter gain and before any filtering. This
property is only used when the `Data Processing
Mode <pniFgen_DataProcessingMode.html>`__ property is set to
**Complex**.

**Valid Values**: -1.0 to 1.0

**Default Value**: 0.0
''',
},
    },
    1150268: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'OSPOverflowErrorReporting',
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Advanced:OSP Overflow Error Reporting',
        'name': 'OSP_OVERFLOW_ERROR_REPORTING',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Configures error reporting when the OSP block detects an overflow in any
of its stages. Overflows lead to waveform clipping.

You can use the `OSP Overflow Status <pniFgen_OSPOverflowStatus.html>`__
property to query for overflow conditions regardless of the setting of
the OSP Overflow Error Reporting property. The device continues to
generate after an overflow regardless of the setting of the OSP Overflow
Error Reporting property.
''',
},
    },
    1150269: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Advanced:OSP Overflow Status',
        'name': 'OSP_OVERFLOW_STATUS',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns a bit field of the overflow status in any stage of the OSP
block. This property is functional regardless of the value for the `OSP
Overflow Error Reporting <pniFgen_OSPOverflowErrorReporting.html>`__
property.

Set this property to 0 to clear the current OSP overflow status.
''',
},
    },
    1150270: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Script Mode:Script to Generate',
        'name': 'SCRIPT_TO_GENERATE',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies which script the signal generator uses. To configure the
signal generator to run a particular script, set this property to the
name of the script.

Use the `niFgen Write
Script <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Write_Script.html')>`__
VI to create multiple scripts. Use this property when the `Output
Mode <pniFgen_OutputMode.html>`__ property is set to
**NIFGEN\_VAL\_OUTPUT\_SCRIPT**.
''',
'note': '''
The signal generator must not be in the Generating state when you change
this property. To change the device configuration, call the `niFgen
Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150271: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Marker Events Count',
        'name': 'MARKER_EVENTS_COUNT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the number of markers supported by the device. Use this property
when the `Output Mode <pniFgen_OutputMode.html>`__ property is set to
**NIFGEN\_VAL\_OUTPUT\_SCRIPT**.
''',
},
    },
    1150272: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Script Triggers Count',
        'name': 'SCRIPT_TRIGGERS_COUNT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the number of Script Triggers supported by the device. Use this
property when the `Output Mode <pniFgen_OutputMode.html>`__ property is
set to **NIFGEN\_VAL\_OUTPUT\_SCRIPT**.
''',
},
    },
    1150273: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Data Marker Events Count',
        'name': 'DATA_MARKER_EVENTS_COUNT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Returns the number of Data Marker Events supported by the device.',
},
    },
    1150274: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Data Transfer:Direct DMA:Window Address',
        'name': 'DIRECT_DMA_WINDOW_ADDRESS',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the window address (beginning of window) of the waveform data
source. This window address is specified by your Direct DMA-compatible
data source.
''',
},
    },
    1150280: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'StartTriggerType',
        'lv_property': 'Triggers:Start:Trigger Type',
        'name': 'START_TRIGGER_TYPE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the type of Start Trigger you want to use.',
},
    },
    1150281: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggers:Start:Digital Edge:Source',
        'name': 'DIGITAL_EDGE_START_TRIGGER_SOURCE',
        'resettable': 'Yes',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the source terminal for the Start Trigger. This property is
used only when the `Start Trigger
Type <pniFgen_StartTriggerType.html>`__ property is set to **Digital
Edge**.

You can specify any valid source terminal for this property. Valid
sources can be found in the Routes topic for your device or in
Measurement & Automation Explorer under the **Device Routes** tab.

Source terminals can be specified in two ways. If your device is named
Dev1 and your terminal is PFI0, then the terminal can be specified as a
fully qualified terminal name, "/Dev1/PFI0". You can also specify the
terminal using PFI 0.
''',
},
    },
    1150282: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'StartTriggerDigitalEdgeEdge',
        'lv_property': 'Triggers:Start:Digital Edge:Edge',
        'name': 'DIGITAL_EDGE_START_TRIGGER_EDGE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the active edge for the Start Trigger. This property is used
only when the `Start Trigger Type <pniFgen_StartTriggerType.html>`__
property is set to **Digital Edge**.
''',
},
    },
    1150283: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggers:Start:Output Terminal',
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'resettable': 'Yes',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the destination terminal for exporting the Start Trigger.

For a list of the terminals available on your device, refer to the
Routes topic for your device or the **Device Routes** tab in MAX.
''',
},
    },
    1150290: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'ScriptTriggerType',
        'lv_property': 'Triggers:Script:Trigger Type',
        'name': 'SCRIPT_TRIGGER_TYPE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the Script trigger type. Depending upon the value of this
property, additional properties may be needed to fully configure the
trigger.
''',
},
    },
    1150291: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggers:Script:Digital Edge:Source',
        'name': 'DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE',
        'resettable': 'Yes',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the source terminal for the Script Trigger. This property is
used when the `Script Trigger Type <pniFgen_ScriptTriggerType.html>`__
property is set to **Digital Edge**.
''',
},
    },
    1150292: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'ScriptTriggerDigitalEdgeEdge',
        'lv_property': 'Triggers:Script:Digital Edge:Edge',
        'name': 'DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the active edge for the Script Trigger. This property is used
when the `Script Trigger Type <pniFgen_ScriptTriggerType.html>`__
property is set to **Digital Edge**.
''',
},
    },
    1150293: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggers:Script:Digital Level:Source',
        'name': 'DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE',
        'resettable': 'Yes',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the source terminal for the Script Trigger. This property is
used when the `Script Trigger Type <pniFgen_ScriptTriggerType.html>`__
property is set to **Digital Level**.
''',
},
    },
    1150294: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'ScriptTriggerDigitalLevelActiveLevel',
        'lv_property': 'Triggers:Script:Digital Level:Active Level',
        'name': 'DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the active level for the Script Trigger. This property is used
when the `Script Trigger Type <pniFgen_ScriptTriggerType.html>`__
property is set to **Digital Level**.
''',
},
    },
    1150295: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggers:Script:Output Terminal',
        'name': 'EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL',
        'resettable': 'Yes',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output terminal for the exported Script Trigger.

Setting this property to an empty string means that when you commit the
session, the signal is removed from that terminal and, if possible, the
terminal is tristated.

For a list of the terminals available on your device, refer to the
Routes topic for your device or the **Device Routes** tab in MAX.
''',
},
    },
    1150310: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Ready For Start:Output Terminal',
        'name': 'READY_FOR_START_EVENT_OUTPUT_TERMINAL',
        'resettable': 'Yes',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the destination terminal for the Ready for Start Event. For a
list of the terminals available on your device, refer to the Routes
topic for your device or the **Device Routes** tab in MAX.
''',
},
    },
    1150311: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'ReadyForStartEventActiveLevel',
        'lv_property': 'Events:Ready For Start:Level:Active Level',
        'name': 'READY_FOR_START_EVENT_LEVEL_ACTIVE_LEVEL',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the output polarity of the Ready for Start Event.',
},
    },
    1150312: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Marker:Output Terminal',
        'name': 'MARKER_EVENT_OUTPUT_TERMINAL',
        'resettable': 'Yes',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the destination terminal for the Marker Event.

For a list of the terminals available on your device, refer to the
Routes topic for your device or the **Device Routes** tab in MAX.
''',
},
    },
    1150313: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'MarkerEventPulsePolarity',
        'lv_property': 'Events:Marker:Pulse:Polarity',
        'name': 'MARKER_EVENT_PULSE_POLARITY',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the output polarity of the Marker Event.',
},
    },
    1150314: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Started:Output Terminal',
        'name': 'STARTED_EVENT_OUTPUT_TERMINAL',
        'resettable': 'Yes',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the destination terminal for the Started Event. For a list of
the terminals available on your device, refer to the Routes topic for
your device or the **Device Routes** tab in MAX.
''',
},
    },
    1150315: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Done:Output Terminal',
        'name': 'DONE_EVENT_OUTPUT_TERMINAL',
        'resettable': 'Yes',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the destination terminal for the Done Event. For a list of the
terminals available on your device, refer to the Routes topic for your
device or the **Device Routes** tab in MAX.
''',
},
    },
    1150316: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'StartedEventActiveLevel',
        'lv_property': 'Events:Started:Level:Active Level',
        'name': 'STARTED_EVENT_LEVEL_ACTIVE_LEVEL',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the output polarity of the Started Event.',
},
    },
    1150317: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'DoneEventActiveLevel',
        'lv_property': 'Events:Done:Level:Active Level',
        'name': 'DONE_EVENT_LEVEL_ACTIVE_LEVEL',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the output polarity of the Done Event.',
},
    },
    1150318: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'StartedEventPulsePolarity',
        'lv_property': 'Events:Started:Pulse:Polarity',
        'name': 'STARTED_EVENT_PULSE_POLARITY',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the output polarity of the Started Event.',
},
    },
    1150319: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'DoneEventPulsePolarity',
        'lv_property': 'Events:Done:Pulse:Polarity',
        'name': 'DONE_EVENT_PULSE_POLARITY',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the output polarity of the Done Event.',
},
    },
    1150320: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocks:Sample Clock:Export Output Terminal',
        'name': 'EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL',
        'resettable': 'Yes',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the terminal at which to export the Sample Clock. If you
specify a divisor with the `Exported Sample Clock
Divisor <pniFgen_ExportedSampleClockDivisor.html>`__ property, the
Sample Clock exported with this property is the value of the Sample
Clock after it is divided-down.

For a list of the terminals available on your device, refer to the
Routes topic for your device or the **Device Routes** tab in MAX.
''',
'note': '''
The signal generator must not be in the Generating state when you change
this property. To change the device configuration, call the `niFgen
Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150321: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocks:Reference Clock:Export Output Terminal',
        'name': 'EXPORTED_REFERENCE_CLOCK_OUTPUT_TERMINAL',
        'resettable': 'Yes',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the terminal at which to export the Reference Clock.

For a list of the terminals available on your device, refer to the
Routes topic for your device or the **Device Routes** tab in MAX.
''',
},
    },
    1150322: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocks:Reference Clock:Onboard Reference Clock:Export Output Terminal',
        'name': 'EXPORTED_ONBOARD_REFERENCE_CLOCK_OUTPUT_TERMINAL',
        'resettable': 'Yes',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the terminal at which to export the onboard Reference Clock.

For a list of the terminals available on your device, refer to the
Routes topic for your device or the **Device Routes** tab in MAX.
''',
},
    },
    1150323: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Output:Filters:Flatness Correction Enabled',
        'name': 'FLATNESS_CORRECTION_ENABLED',
        'resettable': 'Yes',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specify a value of TRUE to enable flatness correction. When flatness
correction is enabled, the signal generator applies a flatness
correction factor to the generated sine wave to ensure the same output
power level at all frequencies.

Set this property to FALSE when performing flatness calibration.
''',
},
    },
    1150324: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Data Transfer:Streaming:Streaming Waveform Handle',
        'name': 'STREAMING_WAVEFORM_HANDLE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the waveform handle of the waveform used to continuously
stream data during generation.

This property is used in conjunction with the `Space Available in
Streaming Waveform <pniFgen_SpaceAvailInStreamingWfm.html>`__ property.

**Default Value**: -1
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150325: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Data Transfer:Streaming:Space Available in Streaming Waveform',
        'name': 'STREAMING_SPACE_AVAILABLE_IN_WAVEFORM',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the space available in the streaming waveform for writing new
data.

Use this property in conjunction with the `Streaming Waveform
Handle <pniFgen_StreamingWaveformHandle.html>`__ property or the
`Streaming Waveform Name <pniFgen_StreamingWaveformName.html>`__
property.
''',
},
    },
    1150326: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Data Transfer:Streaming:Streaming Waveform Name',
        'name': 'STREAMING_WAVEFORM_NAME',
        'resettable': 'Yes',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the name of the waveform used to continuously stream data
during generation. This property defaults to an empty string when no
streaming waveform is specified.

Use this property in conjunction with the `Space Available in Streaming
Waveform <pniFgen_SpaceAvailInStreamingWfm.html>`__ property.

**Default Value**: ""
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150327: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Arbitrary Waveform Mode:Marker Position',
        'name': 'ARB_MARKER_POSITION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the position for a marker to be asserted in the arbitrary
waveform.

Use this property when the `Output Mode <pniFgen_OutputMode.html>`__
property is set to **NIFGEN\_VAL\_OUTPUT\_ARB**. Use the `niFgen Export
Signal <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Export_Signal.html')>`__
VI to export the marker signal.

**Default Value**: -1
''',
},
    },
    1150328: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Arbitrary Waveform Mode:Repeat Count',
        'name': 'ARB_REPEAT_COUNT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of times to repeat the arbitrary waveform when the
**Trigger Mode** parameter in the `niFgen Configure Trigger
Mode <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Configure_Trigger_Mode.html')>`__
VI is set to **Single** or **Stepped**.

This property is ignored if the **Trigger Mode** parameter is set to
**Continuous** or **Burst**. Use this property when the `Output
Mode <pniFgen_OutputMode.html>`__ property is set to
**NIFGEN\_VAL\_OUTPUT\_ARB**.

When used during
`streaming <javascript:LaunchHelp('SigGenHelp.chm::/streaming.html')>`__
operations, this property specifies the number of times to repeat the
streaming waveform (the onboard memory allocated for streaming).

**Default Value**: 1
''',
},
    },
    1150329: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocks:Sample Clock Timebase:Export Output Terminal',
        'name': 'EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL',
        'resettable': 'Yes',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the terminal at which to export the Sample Clock Timebase.

For a list of the terminals available on your device, refer to the
Routes topic for your device or the **Device Routes** tab in MAX.

If you specify a divisor with the `Exported Sample Clock Timebase
Divisor <pniFgen_ExportedSampleClockTimebaseDivisor.html>`__ property,
the Sample Clock timebase exported with the Exported Sample Clock
Timebase Output Terminal property is the value of the Sample Clock
timebase after it is divided down.
''',
'note': '''
The signal generator must not be in the Generating state when you change
this property. To change the device configuration, call the `niFgen
Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150330: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Standard Function:Sync Out Output Terminal',
        'name': 'SYNC_OUT_OUTPUT_TERMINAL',
        'resettable': 'Yes',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the terminal at which to export the SYNC OUT signal. This
property is not supported for all devices. For a list of the terminals
available on your device, refer to the Routes topic for your device or
the **Device Routes** tab in MAX.
''',
},
    },
    1150331: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'StartedEventOutputBehavior',
        'lv_property': 'Events:Started:Output Behavior',
        'name': 'STARTED_EVENT_OUTPUT_BEHAVIOR',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the output behavior for the Started Event.',
},
    },
    1150332: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'DoneEventOutputBehavior',
        'lv_property': 'Events:Done:Output Behavior',
        'name': 'DONE_EVENT_OUTPUT_BEHAVIOR',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the output behavior for the Done Event.',
},
    },
    1150333: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'StartedEventPulseWidthUnits',
        'lv_property': 'Events:Started:Pulse:Width Units',
        'name': 'STARTED_EVENT_PULSE_WIDTH_UNITS',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the pulse width units for the Started Event.',
},
    },
    1150334: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'DoneEventPulseWidthUnits',
        'lv_property': 'Events:Done:Pulse:Width Units',
        'name': 'DONE_EVENT_PULSE_WIDTH_UNITS',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the pulse width units for the Done Event.',
},
    },
    1150335: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Started:Pulse:Width Value',
        'name': 'STARTED_EVENT_PULSE_WIDTH',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': 'Specifies the pulse width value for the Started Event.',
},
    },
    1150336: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Done:Pulse:Width Value',
        'name': 'DONE_EVENT_PULSE_WIDTH',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': 'Specifies the pulse width for the Done Event.',
},
    },
    1150337: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Data Marker:Data Bit Number',
        'name': 'DATA_MARKER_EVENT_DATA_BIT_NUMBER',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the bit number to assign to the Data Marker Event.',
},
    },
    1150338: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'DataMarkerEventLevelPolarity',
        'lv_property': 'Events:Data Marker:Level:Active Level',
        'name': 'DATA_MARKER_EVENT_LEVEL_POLARITY',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the output polarity of the Data Marker Event. Refer to `Data
Marker
Events <javascript:LaunchHelp('SigGenHelp.chm::/events_data_markers.html')>`__
topic for more information about Data Marker Event polarity.
''',
},
    },
    1150339: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Data Marker:Output Terminal',
        'name': 'DATA_MARKER_EVENT_OUTPUT_TERMINAL',
        'resettable': 'Yes',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the destination terminal for the Data Marker Event. For a list
of the terminals available on your device, refer to the Routes topic for
your device or the **Device Routes** tab in MAX.
''',
'note': '''
NI recommends using a data sample rate of less than 200 MS/s for data
markers routed to RTSI. Faster sample rates may lead to unwanted
behavior.
''',
},
    },
    1150340: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Marker:Pulse:Width Value',
        'name': 'MARKER_EVENT_PULSE_WIDTH',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the pulse width value of the Marker Event. Set the units for
the values with the `Marker Event Pulse Width
Units <pniFgen_MarkerEventPulseWidthUnits.html>`__ property.
''',
},
    },
    1150341: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'MarkerEventPulseWidthUnits',
        'lv_property': 'Events:Marker:Pulse:Width Units',
        'name': 'MARKER_EVENT_PULSE_WIDTH_UNITS',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the pulse width units of the Marker Event.',
},
    },
    1150342: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'MarkerEventOutputBehavior',
        'lv_property': 'Events:Marker:Output Behavior',
        'name': 'MARKER_EVENT_OUTPUT_BEHAVIOR',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the output behavior for the Marker Event.',
},
    },
    1150343: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'MarkerEventToggleInitialState',
        'lv_property': 'Events:Marker:Toggle:Initial State',
        'name': 'MARKER_EVENT_TOGGLE_INITIAL_STATE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the initial state of the Marker Event.',
},
    },
    1150344: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Marker:Advanced:All Marker Events Live Status',
        'name': 'ALL_MARKER_EVENTS_LIVE_STATUS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Returns a bit field of the live status of all Marker Events.',
},
    },
    1150345: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Marker:Advanced:Live Status',
        'name': 'MARKER_EVENT_LIVE_STATUS',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Returns TRUE if the status of the specified Marker Event is live, and
FALSE otherwise.
''',
},
    },
    1150348: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Ready For Start:Advanced:Live Status',
        'name': 'READY_FOR_START_EVENT_LIVE_STATUS',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Returns TRUE if the status of the specified Ready for Start Event is
live, and FALSE otherwise.
''',
},
    },
    1150349: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Marker:Advanced:All Marker Events Latched Status',
        'name': 'ALL_MARKER_EVENTS_LATCHED_STATUS',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns a bit field of the latched status of all Marker Events. Set this
property to 0 to clear the latched status of all Marker Events.
''',
},
    },
    1150350: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Marker:Advanced:Latched Status',
        'name': 'MARKER_EVENT_LATCHED_STATUS',
        'resettable': 'Yes',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies the latched status of the specified Marker Event. Set this
property to FALSE to clear the latched status of the Marker Event.
''',
},
    },
    1150351: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Done:Advanced:Latched Status',
        'name': 'DONE_EVENT_LATCHED_STATUS',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': 'Returns the latched status of the specified Done Event.',
},
    },
    1150352: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Started:Advanced:Latched Status',
        'name': 'STARTED_EVENT_LATCHED_STATUS',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': 'Returns the latched status of the specified Started Event.',
},
    },
    1150354: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Marker:Advanced:Delay Value',
        'name': 'MARKER_EVENT_DELAY',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the amount of delay applied to a Marker Event with respect to
the analog output of the signal generator.

A positive delay value indicates that the Marker Event occurs after the
analog data, while a negative delay value indicates that the Marker
Event occurs before the analog data. The default value is zero, which
aligns the Marker Event with the analog output.

You can specify the units of the delay value using the `Marker Event
Delay Units <pniFgen_MarkerEventDelayUnits.html>`__ property.

**Default Value**: 0
''',
},
    },
    1150355: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'MarkerEventDelayUnits',
        'lv_property': 'Events:Marker:Advanced:Delay Units',
        'name': 'MARKER_EVENT_DELAY_UNITS',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the units used for the `Marker Event Delay
Value <pniFgen_MarkerEventDelayValue.html>`__ property.
''',
},
    },
    1150356: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Started:Advanced:Delay Value',
        'name': 'STARTED_EVENT_DELAY',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the amount of delay applied to a Started Event with respect to
the analog output of the signal generator.

A positive delay value indicates that the Started Event occurs after the
analog data, while a negative delay value indicates that the Started
Event occurs before the analog data. The default value is zero, which
aligns the Started Event with the analog output.

You can specify the units of the delay value by setting the `Started
Event Delay Units <pniFgen_StartedEventDelayUnits.html>`__ property.

**Default Value**: 0
''',
},
    },
    1150357: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'StartedEventDelayUnits',
        'lv_property': 'Events:Started:Advanced:Delay Units',
        'name': 'STARTED_EVENT_DELAY_UNITS',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the units used for the `Started Event Delay
Value <pniFgen_StartedEventDelayValue.html>`__ property.
''',
},
    },
    1150358: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Events:Done:Advanced:Delay Value',
        'name': 'DONE_EVENT_DELAY',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the amount of delay applied to a Done Event with respect to
the analog output of the signal generator.

A positive delay value indicates that the Done Event occurs after the
analog data, while a negative delay value indicates that the Done Event
occurs before the analog data. A value of zero aligns the Done Event
with the analog output.

You can specify the units of the delay value by setting the `Delay
Units <pniFgen_DoneEventDelayUnits.html>`__ property.

**Default Value**: 0
''',
},
    },
    1150359: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'DoneEventDelayUnits',
        'lv_property': 'Events:Done:Advanced:Delay Units',
        'name': 'DONE_EVENT_DELAY_UNITS',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the units used for the `Done Event Delay
Value <pniFgen_DoneEventDelayValue.html>`__ property.
''',
},
    },
    1150362: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Data Transfer:Advanced:PCI DMA Optimizations Enabled',
        'name': 'PCI_DMA_OPTIMIZATIONS_ENABLED',
        'resettable': 'Yes',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Controls whether NI-FGEN allows performance optimizations for DMA
transfers. This property is only valid for PCI and PXI SMC-based
devices. This property is enabled (TRUE) by default, and NI recommends
leaving it enabled.

**Default Value**: TRUE
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150365: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TerminalConfiguration',
        'lv_property': 'Output:Terminal Configuration',
        'name': 'TERMINAL_CONFIGURATION',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether to analyze gain and offset values based on
single-ended or
`differential <javascript:LaunchHelp('SigGenHelp.chm::/fund_differential_output.html')>`__
operation.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150366: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Output:Common Mode Offset',
        'name': 'COMMON_MODE_OFFSET',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the value the signal generator adds to or subtracts from the
arbitrary waveform data. This property applies only when set the
`Terminal Configuration <pniFgen_TerminalConfiguration.html>`__ property
to **Differential**. Common-mode offset is applied to the signals
generated at each differential output terminal.
''',
},
    },
    1150367: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'SampleClockTimebaseSource',
        'lv_property': 'Clocks:Sample Clock Timebase:Source',
        'name': 'SAMPLE_CLOCK_TIMEBASE_SOURCE',
        'resettable': 'Yes',
        'type': 'ViString',
'documentation': {
'description': 'Specifies the Sample Clock Timebase source.',
'note': '''
The signal generator must not be in the Generating state when you change
this property. To change the device configuration, call the `niFgen
Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150368: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocks:Sample Clock Timebase:Rate',
        'name': 'SAMPLE_CLOCK_TIMEBASE_RATE',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the Sample Clock Timebase rate. This property applies only to
external Sample Clock timebases.
''',
'note': '''
The signal generator must not be in the Generating state when you change
this property. To change the device configuration, call the `niFgen
Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150369: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Output:Channel Delay',
        'name': 'CHANNEL_DELAY',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the delay to apply to the analog output of the channel
specified by the `Active Channel <pniFgen_ActiveChannel.html>`__
property.

You can use the output delay to configure the timing relationship
between channels on a multichannel device. Values for this property can
be zero or positive. A value of zero indicates that the channels are
aligned. A positive value delays the analog output by the specified
number of seconds.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150370: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'OSPMode',
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:OSP Mode',
        'name': 'OSP_MODE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the generation mode of the OSP, which determines the type of
data contained in the output signal.

For more information about the OSP modes your device supports, refer to
`Devices <javascript:LaunchHelp('SigGenHelp.chm::/device_specific.html')>`__
section of the *NI Signal Generators Help*.
''',
'note': '''
When using the NI 5450/5451 with I/Q rates higher than 200 MS/s, NI-FGEN
restricts this property value to BaseBand.
''',
},
    },
    1150371: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Frequency Shift',
        'name': 'OSP_FREQUENCY_SHIFT',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': 'Specifies the amount of frequency shift applied to the baseband signal.',
'note': '''
When using the NI 5450/5451 with I/Q rates higher than 200 MS/s, NI-FGEN
restricts this property value to 0.
''',
},
    },
    1150373: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Data Transfer:Maximum Bandwidth',
        'name': 'DATA_TRANSFER_MAXIMUM_BANDWIDTH',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the maximum amount of bus bandwidth to use for data transfers.

The signal generator limits data transfer speeds on the PCI Express bus
to the value you specify for this property. Set this property to
optimize bus bandwidth usage for multidevice streaming applications by
preventing the signal generator from consuming all the available
bandwidth on a PCI Express link when waveforms are being written to the
onboard memory of the device.
''',
},
    },
    1150374: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Data Transfer:Advanced:Preferred Packet Size',
        'name': 'DATA_TRANSFER_PREFERRED_PACKET_SIZE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the preferred size of the data field in a PCI Express read
request packet.

In general, the larger the packet size, the more efficiently the device
uses the bus. By default, NI signal generators use the largest packet
size allowed by the system. However, due to different system
implementations, some systems may perform better with smaller packet
sizes.

Recommended values for this property are powers of two between 64 and
512.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150375: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Data Transfer:Advanced:Maximum In-Flight Read Requests',
        'name': 'DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the maximum number of concurrent PCI Express read requests the
signal generator can issue.

When transferring data from computer memory to device onboard memory
across the PCI Express bus, the signal generator can issue multiple
memory reads at the same time. In general, the larger the number of read
requests, the more efficiently the device uses the bus because the
multiple read requests keep the data flowing, even in a PCI Express
topology that has high latency due to PCI Express switches in the data
path. Most NI devices can issue a large number of read requests
(typically 8 or 16). By default, this property is set to the highest
value the signal generator supports.

If other devices in your system cannot tolerate long data latencies, it
may be helpful to decrease the number of in-flight read requests the NI
signal generator issues. This change helps to reduce the amount of data
the signal generator reads at one time.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150376: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocks:Advanced:External Sample Clock Multiplier',
        'name': 'EXTERNAL_SAMPLE_CLOCK_MULTIPLIER',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies a multiplication factor to use to obtain a desired sample rate
from an external Sample Clock.

The resulting sample rate is equal to this factor multiplied by the
external Sample Clock rate. You can use this property to generate
samples at a rate higher than your external clock rate. When using this
property, you do not need to explicitly set the external clock rate.
''',
},
    },
    1150377: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'IdleBehavior',
        'lv_property': 'Output:Advanced:Idle Behavior',
        'name': 'IDLE_BEHAVIOR',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the behavior of the output during the Idle state.',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150378: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Output:Advanced:Idle Value',
        'name': 'IDLE_VALUE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the value to generate in the Idle state. You must set the
`Idle Behavior <pniFgen_IdleBehavior.html>`__ property to **Jump To
Value** to use this property.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150379: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'WaitBehavior',
        'lv_property': 'Output:Advanced:Wait Behavior',
        'name': 'WAIT_BEHAVIOR',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the behavior of the output while waiting for a Script Trigger
or during a wait instruction.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150380: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Output:Advanced:Wait Value',
        'name': 'WAIT_VALUE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the value to generate while waiting. You must set the `Wait
Behavior <pniFgen_WaitBehavior.html>`__ property to **Jump To Value** to
use this property.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1150389: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Advanced:Compensate for Filter Group Delay',
        'name': 'OSP_COMPENSATE_FOR_FILTER_GROUP_DELAY',
        'resettable': 'Yes',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Adjusts for OSP filter group delay when aligning analog outputs and
events in OSP mode. If you set this property to TRUE, event outputs
align more closely with the analog output. The analog output also aligns
more closely between two devices synchronized using NI-TClk.
''',
'note': '''
Group delay is the delay that occurs as a result of passing through a
FIR filter. At a low I/Q rate, the group delay can become so large that
some devices may not be able to align the events with the output. In
this case, you must increase the I/Q rate or disable this property.
''',
},
    },
    1150390: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Inherent IVI Attributes:Instrument Identification:Module Revision',
        'name': 'MODULE_REVISION',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': 'Returns the revision letter of the module you are using.',
},
    },
    1150391: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:P2P Enabled',
        'name': 'P2P_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the signal generator reads data from the peer-to-peer
endpoint (TRUE) instead of reading it from the onboard memory. This
property is `endpoint
based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

**Default Value**: FALSE
''',
},
    },
    1150392: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Destination Channels',
        'name': 'P2P_DESTINATION_CHANNELS',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies which channels are written to by a peer-to-peer endpoint. If
multiple channels are specified, data is deinterleaved to each channel.
Channels are configured using the `niFgen Configure
Channels <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Configure_Channels.html')>`__
VI. This property is `endpoint
based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

**Default Value**: "" (empty string), all channels are configured
''',
},
    },
    1150393: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Endpoint Size',
        'name': 'P2P_ENDPOINT_SIZE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the size, in samples per channel, of the peer-to-peer endpoint.
This property is
`endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.
''',
},
    },
    1150394: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Space Available In Endpoint',
        'name': 'P2P_SPACE_AVAILABLE_IN_ENDPOINT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the current space available in the endpoint in samples per
channel. You can use this property when priming the endpoint with
initial data through the `niFgen Write P2P Endpoint
I16 <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Write_P2P_Endpoint_I16.html')>`__
VI to determine how many samples you can write. You also can use this
property to characterize the performance and measure the latency of the
peer-to-peer stream as data moves across the bus. This property is
`endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.
''',
},
    },
    1150395: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Most Space Available In Endpoint',
        'name': 'P2P_MOST_SPACE_AVAILABLE_IN_ENDPOINT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the largest number of samples per channel available in the
endpoint since this property was last read. This property can be used to
determine how much endpoint space to use as a buffer against PCI Express
bus traffic latencies by reading the property and keeping track of the
largest value returned. This property is
`endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

If you want to minimize the latency for data to move through the
endpoint and be generated by the signal generator, use the `Data
Transfer Permission Initial
Credits <pniFgen_DataTransferPermissionInitialCredits.html>`__ property
to grant fewer initial credits than the default of the entire endpoint
size.
''',
},
    },
    1150396: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Endpoint Count',
        'name': 'P2P_ENDPOINT_COUNT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the number of peer-to-peer FIFO endpoints supported by the
device.
''',
},
    },
    1150397: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Manual:Manual Configuration Enabled',
        'name': 'P2P_MANUAL_CONFIGURATION_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables (TRUE) or disables (FALSE) manual configuration for a
peer-to-peer endpoint. Enabling this property disables automatic NI-P2P
stream manager flow control and Done Notifications.
''',
},
    },
    1150398: {
        'access': 'write only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Manual:Configuration:Data Transfer Permission Address',
        'name': 'P2P_DATA_TRANSFER_PERMISSION_ADDRESS',
        'resettable': 'No',
        'type': 'ViInt64',
'documentation': {
'description': '''
Indicates the address in the writer peer to which the signal generator
sends data transfer permission credits. This property is
`endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.
''',
'note': '''
You can use this property only when the `Manual Configuration
Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
TRUE.
''',
},
    },
    1150399: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'P2PAddressType',
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Manual:Configuration:Data Transfer Permission Address Type',
        'name': 'P2P_DATA_TRANSFER_PERMISSION_ADDRESS_TYPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the type of address for the `Data Transfer Permission
Address <pniFgen_DataTransferPermissionAddress.html>`__ property. This
property is
`endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

**Default Value**: **Virtual**
''',
'note': '''
You can only use this property when the `Manual Configuration
Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
TRUE.
''',
},
    },
    1150400: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Data Transfer Permission Interval',
        'name': 'P2P_DATA_TRANSFER_PERMISSION_INTERVAL',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the interval, in samples per channel, at which the signal
generator issues credits to allow the writer peer to transfer data over
the bus into the configured endpoint. Refer to the `Flow
Control <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Flow_Control.html')>`__
topic in the *NI Signal Generators Help* for more information. This
property is coerced up by NI-FGEN to the nearest 128-byte boundary. This
property is
`endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

**Default Value**: 1,024
''',
},
    },
    1150401: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Manual:Configuration:Endpoint Window Address',
        'name': 'P2P_ENDPOINT_WINDOW_ADDRESS',
        'resettable': 'No',
        'type': 'ViInt64',
'documentation': {
'description': '''
Returns the signal generator address where endpoint data is sent by the
writer peer. The type of this address is specified by the `Endpoint
Window Address Type <pniFgen_EndpointWindowAddressType.html>`__
property. This property is
`endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.
''',
'note': '''
You can only use this property when the `Manual Configuration
Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
TRUE.
''',
},
    },
    1150402: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'P2PAddressType',
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Manual:Configuration:Endpoint Window Address Type',
        'name': 'P2P_ENDPOINT_WINDOW_ADDRESS_TYPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the type of the `Endpoint Window
Address <pniFgen_EndpointWindowAddress.html>`__ property. This property
is
`endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.

**Default Value**: **Virtual**
''',
'note': '''
You can only use this property when the `Manual Configuration
Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
TRUE.
''',
},
    },
    1150403: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Manual:Configuration:Endpoint Window Size',
        'name': 'P2P_ENDPOINT_WINDOW_SIZE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the size, in bytes, of the endpoint window. The endpoint window
is also described by the `Endpoint Window
Address <pniFgen_EndpointWindowAddress.html>`__ property and the
`Endpoint Window Address
Type <pniFgen_EndpointWindowAddressType.html>`__ property. This property
is
`endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.
''',
'note': '''
You can only use this property when the `Manual Configuration
Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
TRUE.
''',
},
    },
    1150405: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Manual:Notification:Done Notification Address',
        'name': 'P2P_DONE_NOTIFICATION_ADDRESS',
        'resettable': 'No',
        'type': 'ViInt64',
'documentation': {
'description': '''
Returns the signal generator address to which the writer peer sends the
`Done Notification Value <pniFgen_DoneNotificationValue.html>`__. This
property is
`endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.
Refer to the `Stopping a Peer-to-Peer
Generation <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Stopping_Generation.html')>`__
topic in the *NI Signal Generators Help* for more information about
using Done Notifications.
''',
'note': '''
You can only use this property when the `Manual Configuration
Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
TRUE.
''',
},
    },
    1150406: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'P2PAddressType',
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Manual:Notification:Done Notification Address Type',
        'name': 'P2P_DONE_NOTIFICATION_ADDRESS_TYPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the address type of the `Done Notification
Address <pniFgen_DoneNotificationAddress.html>`__ property. This
property is
`endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.
Refer to the `Stopping a Peer-to-Peer
Generation <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Stopping_Generation.html')>`__
topic in the *NI Signal Generators Help* for more information about
using Done Notifications.

Default Value: **Virtual**
''',
'note': '''
You can only use this property when the `Manual Configuration
Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
TRUE.
''',
},
    },
    1150407: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Manual:Notification:Done Notification Value',
        'name': 'P2P_DONE_NOTIFICATION_VALUE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the value the writer peer writes to the address specified by the
`Done Notification Address <pniFgen_DoneNotificationAddress.html>`__
property. This property is
`endpoint-based <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Configuring_an_Endpoint.html')>`__.
Refer to the `Stopping a Peer-to-Peer
Generation <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Stopping_Generation.html')>`__
topic in the *NI Signal Generators Help* for more information about
using Done Notifications.
''',
'note': '''
You can only use this property when the `Manual Configuration
Enabled <pniFgen_ManualConfigurationEnabled.html>`__ property is set to
TRUE.
''',
},
    },
    1150408: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Data Transfer Permission Initial Credits',
        'name': 'P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the initial amount of data, in samples per channel, that the
writer peer is allowed to transfer over the bus into the configured
endpoint when the peer-to-peer data stream is enabled. If you do not set
this property and the endpoint is empty, credits equal to the full size
of the endpoint are issued to the writer peer. If data has been written
to the endpoint using the `niFgen Write P2P Endpoint
I16 <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Write_P2P_Endpoint_I16.html')>`__
VI prior to enabling the stream, credits equal to the remaining space
available in the endpoint are issued to the writer peer. This property
is coerced up by NI-FGEN to 8-byte boundaries.
''',
},
    },
    1150409: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Data Transfer:Streaming:Streaming Write Timeout',
        'name': 'STREAMING_WRITE_TIMEOUT',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the maximum amount of time allowed to complete a streaming
write operation.

**Units**: seconds (s)
''',
},
    },
    1150410: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggers:Start:P2P Endpoint Fullness:Level',
        'name': 'P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of samples the endpoint needs to receive before the
signal generator starts generation. This property applies only when the
`Start Trigger Type <pniFgen_StartTriggerType.html>`__ property is set
to **P2P Endpoint Fullness**. Refer to the `Flow
Control <javascript:LaunchHelp('SigGenHelp.chm::/P2P_Flow_Control.html')>`__
topic in the *NI Signal Generators Help* for more information about
peer-to-peer operations. This property is coerced down to 8-byte
boundaries.
''',
'note': '''
Due to an additional internal FIFO in the signal generator, the writer
peer actually must write 2,304 bytes more than the quantity of data
specified by this property to satisfy the trigger level.
''',
},
    },
    1150411: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Output:Advanced:AUX Power Enabled',
        'name': 'AUX_POWER_ENABLED',
        'resettable': 'Yes',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Controls the specified auxiliary power pin. Setting this property to
TRUE energizes the auxiliary power when the session is committed. When
this property is FALSE, the power pin of the connector outputs no power.

**Default Value**: FALSE
''',
},
    },
    1150412: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:FPGA Bitfile Path',
        'name': 'FPGA_BITFILE_PATH',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': 'Gets the absolute file path to the bitfile loaded on the FPGA.',
},
    },
    1250001: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'OutputMode',
        'lv_property': 'Output:Output Mode',
        'name': 'OUTPUT_MODE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the output mode the signal generator uses. The output mode you
specify determines which VIs and properties you use to configure the
waveform the signal generator produces.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1250002: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Instrument:Obsolete:Ref Clock Source',
        'name': 'REF_CLOCK_SOURCE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Controls the Reference Clock source the signal generator uses.

The signal generator derives the frequencies and sample rates that it
uses to generate waveforms from the source you specify. For example,
when you set this attribute to **Clock In**, the signal generator uses
the signal it receives at the Clk In front panel connector as its
Reference Clock.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1250003: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Output:Output Enabled',
        'name': 'OUTPUT_ENABLED',
        'resettable': 'Yes',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the signal that the signal generator produces appears
at the output connector.
''',
},
    },
    1250004: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Output:Output Impedance',
        'name': 'OUTPUT_IMPEDANCE',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the output impedance of the signal generator at the output
connector. NI signal generators have an output impedance of 50 ohms and
an optional 75 ohms on select modules.

If the `Load Impedance <pniFgen_LoadImpedance.html>`__ property value
matches the output impedance, the voltage at the signal output connector
is at the necessary level. The voltage at the signal output connector
varies with load output impedance, up to doubling the voltage for a
high-impedance load.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1250005: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'OperationMode',
        'lv_property': 'Instrument:Obsolete:Operation Mode',
        'name': 'OPERATION_MODE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies how the signal generator produces waveforms. NI signal
generators currently support only one value:
**NIFGEN\_VAL\_OPERATE\_CONTINUOUS**. To control trigger mode, set the
`Trigger Mode <pniFgen_TriggerMode.html>`__ property.
''',
},
    },
    1250101: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'Waveform',
        'lv_property': 'Standard Function:Waveform',
        'name': 'FUNC_WAVEFORM',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies which standard waveform the signal generator produces. Use
this property only when the `Output Mode <pniFgen_OutputMode.html>`__
property is set to **NIFGEN\_VAL\_OUTPUT\_FUNC**.

**Default Value**: **NIFGEN\_VAL\_WFM\_DC**
''',
},
    },
    1250102: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Standard Function:Amplitude',
        'name': 'FUNC_AMPLITUDE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Controls the amplitude of the standard waveform that the signal
generator produces. This value is the amplitude at the output terminal.

For example, to produce a waveform ranging from -5.00 V to +5.00 V, set
Amplitude property to 10.00 V.

**Units**: volts peak-to-peak (Vpk-pk)

**Default Value**: None
''',
'note': '''
This parameter does not affect signal generator behavior when you set
the `Waveform <pniFgen_Waveform.html>`__ property to
**NIFGEN\_VAL\_WFM\_DC**.
''',
},
    },
    1250103: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Standard Function:DC Offset',
        'name': 'FUNC_DC_OFFSET',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Controls the DC offset of the standard waveform that the signal
generator produces.

This value is the offset at the output terminal. The value is the offset
from ground to the center of the waveform you specify with the
`Waveform <pniFgen_Waveform.html>`__ property.

For example, to configure a waveform with an amplitude of 10.00 V to
range from 0.00 V to +10.00 V, set this property to 5.00 V.

**Units**: volts (V)

**Default Value**: None
''',
},
    },
    1250104: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Standard Function:Standard Function Mode:Frequency',
        'name': 'FUNC_FREQUENCY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Controls the frequency of the standard waveform that the signal
generator produces.

**Units**: hertz (Hz)

**Default Value**: None
''',
'note': '''
This parameter does not affect signal generator behavior when you set
the `Waveform <pniFgen_Waveform.html>`__ property to
**NIFGEN\_VAL\_WFM\_DC**. For **NIFGEN\_VAL\_WFM\_SINE** , the range is
between 0 MHz and 16 MHz, but the range is between 0 MHz and 1 MHz for
all other waveforms.
''',
},
    },
    1250105: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Standard Function:Start Phase',
        'name': 'FUNC_START_PHASE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Controls horizontal offset of the standard waveform the signal generator
produces. Specify this property in degrees of one waveform cycle.

A start phase of 180 degrees means output generation begins halfway
through the waveform. A start phase of 360 degrees offsets the output by
an entire waveform cycle, which is identical to a start phase of 0
degrees.

**Units**: Degrees of one cycle

**Default Value**: None
''',
'note': '''
This property does not affect signal generator behavior when you set the
`Waveform <pniFgen_Waveform.html>`__ property to
**NIFGEN\_VAL\_WFM\_DC**.
''',
},
    },
    1250106: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Standard Function:Duty Cycle High',
        'name': 'FUNC_DUTY_CYCLE_HIGH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the duty cycle of the square wave the signal generator is
producing. Specify this property as a percentage of the time the square
wave is high in a cycle.

**Units**: Percentage of time the waveform is high

**Default Value**: 50%
''',
'note': '''
This parameter only affects signal generator behavior when you set the
`Waveform <pniFgen_Waveform.html>`__ property to
**NIFGEN\_VAL\_WFM\_SQUARE**.
''',
},
    },
    1250201: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Arbitrary Waveform Mode:Arbitrary Waveform Handle',
        'name': 'ARB_WAVEFORM_HANDLE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Selects which arbitrary waveform the signal generator produces. You can
create multiple arbitrary waveforms using the `niFgen Create
Waveform <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Create_Waveform_poly.html')>`__
VI.

The `niFgen Create
Waveform <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Create_Waveform_poly.html')>`__
VI, `niFgen Allocate
Waveform <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Allocate_Waveform.html')>`__
VI, and similar VIs return a **Waveform Handle** that you use to
identify the particular waveform. To configure the signal generator to
produce a particular waveform, set this property to the **Waveform
Handle** value.

Use this property only when the `Output
Mode <pniFgen_OutputMode.html>`__ property is set to
**NIFGEN\_VAL\_OUTPUT\_ARB**.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1250202: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Gain',
        'name': 'ARB_GAIN',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the factor by which the signal generator scales the arbitrary
waveform data. When you create arbitrary waveforms, you must first
normalize the data points to the range -1.0 to +1.0. Use this property
to scale the arbitrary waveform to other ranges.

For example, when you set this property to 2.0, the output signal ranges
from -2.0 V to +2.0 V.

Use this property when the `Output Mode <pniFgen_OutputMode.html>`__
property is set to **NIFGEN\_VAL\_OUTPUT\_ARB** or
**NIFGEN\_VAL\_OUTPUT\_SEQ**.
''',
},
    },
    1250203: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Offset',
        'name': 'ARB_OFFSET',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the value the signal generator adds to the arbitrary waveform
data. When you create arbitrary waveforms, you must first normalize the
data points to the range -1.0 to +1.0. Use this property to shift the
arbitrary waveform range.

For example, when you set this property to 1.0, the output signal ranges
from 0.0 V to 2.0 V.

Use this property when the `Output Mode <pniFgen_OutputMode.html>`__
property is set to **NIFGEN\_VAL\_OUTPUT\_ARB** or
**NIFGEN\_VAL\_OUTPUT\_SEQ**.
''',
},
    },
    1250204: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocks:Sample Clock:Rate',
        'name': 'ARB_SAMPLE_RATE',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the rate, in samples per second, at which the signal generator
generates the points in arbitrary waveforms.

Use this property when the `Output Mode <pniFgen_OutputMode.html>`__
property is set to **NIFGEN\_VAL\_OUTPUT\_ARB** or
**NIFGEN\_VAL\_OUTPUT\_SEQ**.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1250205: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Capabilities:Max Number of Waveforms',
        'name': 'MAX_NUM_WAVEFORMS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the maximum number of arbitrary waveforms that the signal
generator allows. On some signal generators, this value may vary with
remaining onboard memory.
''',
},
    },
    1250206: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Capabilities:Waveform Quantum',
        'name': 'WAVEFORM_QUANTUM',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the quantum value the signal generator allows. The size of each
arbitrary waveform must be a multiple of this quantum value.

For example, when this property returns a value of 8, all waveform sizes
must be a multiple of 8. Typically, this value is constant for the
signal generator.
''',
},
    },
    1250207: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Capabilities:Min Waveform Size',
        'name': 'MIN_WAVEFORM_SIZE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the minimum number of points the signal generator allows in an
arbitrary waveform. Typically, this value is constant for the signal
generator.
''',
'note': '''
In some cases, you may need to supply a larger waveform than the value
specified by this property. Refer to the "Features Supported" topic for
your device in the *NI Signal Generators Help* for a table of minimum
waveform sizes.
''',
},
    },
    1250208: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Capabilities:Max Waveform Size',
        'name': 'MAX_WAVEFORM_SIZE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the maximum number of points the signal generator allows in an
arbitrary waveform. On some signal generators, this value may vary with
remaining onboard memory.
''',
},
    },
    1250211: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Arbitrary Sequence Mode:Arbitrary Sequence Handle',
        'name': 'ARB_SEQUENCE_HANDLE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Selects which sequence the signal generator produces. You can create
multiple sequences using the `niFgen Create Arbitrary
Sequence <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Create_Arbitrary_Sequence.html')>`__
VI.

The niFgen Create Arbitrary Sequence VI returns a **Sequence Handle**
that you use to identify the particular sequence. To configure the
signal generator to produce a particular sequence, set this property to
the **Sequence Handle** value. Use this property when the `Output
Mode <pniFgen_OutputMode.html>`__ property is set to
**NIFGEN\_VAL\_OUTPUT\_SEQ**.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
    1250212: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Arbitrary Sequence Mode:Max Number of Sequences',
        'name': 'MAX_NUM_SEQUENCES',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the maximum number of arbitrary sequences the signal generator
allows.
''',
},
    },
    1250213: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Arbitrary Sequence Mode:Min Sequence Length',
        'name': 'MIN_SEQUENCE_LENGTH',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the minimum number of arbitrary waveforms the signal generator
allows in a sequence. Typically, this value is constant for the signal
generator.
''',
},
    },
    1250214: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Arbitrary Sequence Mode:Max Sequence Length',
        'name': 'MAX_SEQUENCE_LENGTH',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the maximum number of arbitrary waveforms the signal generator
allows in a sequence.
''',
},
    },
    1250215: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Arbitrary Waveform:Arbitrary Sequence Mode:Max Loop Count',
        'name': 'MAX_LOOP_COUNT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the maximum number of times the signal generator can repeat a
waveform in a sequence. Typically, this value is constant for the signal
generator.
''',
},
    },
    1250302: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TriggerSource',
        'lv_property': 'Instrument:5401/5411/5431:Trigger Source',
        'name': 'TRIGGER_SOURCE',
        'resettable': 'Yes',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies which trigger source the signal generator uses.

After you call the `niFgen Initiate
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Initiate_Generation.html')>`__
VI, the signal generator waits for the trigger you specify in this
parameter. After it receives a trigger, the signal generator produces
the number of cycles you specify in the `Repeat
Count <pniFgen_ArbWfm.RepeatCount.html>`__ property.

The value you select for this property is also the source for the
trigger in the other trigger modes as specified by the `Trigger
Mode <pniFgen_TriggerMode.html>`__ property.
''',
'note': '''
You cannot change this property while the device is generating a
waveform. If you want to change the device configuration, call the
`niFgen Abort
Generation <javascript:LaunchMergedHelp('SigGenHelp.chm',%20'nifgenlv.chm',%20'niFgen_Abort_Generation.html')>`__
VI or wait for the generation to complete.
''',
},
    },
}
