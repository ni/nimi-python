
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
Specifies whether to validate property values and function parameters.
If enabled, the instrument driver validates the parameter values that
you pass to driver functions. Range checking parameters is very useful
for debugging. After you validate your program, you can set this
property to FALSE to disable range checking and maximize performance.
The default value is TRUE. Use `niScope Initialize with
Options <scopeviref.chm::/niScope_Initialize_With_Options.html>`__ to
override this value.
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
Specifies whether the instrument driver queries the instrument status
after each operation. Querying the instrument status is very useful for
debugging. After you validate your program, you can set this property to
FALSE to disable status checking and maximize performance. The
instrument driver can choose to ignore status checking for particular
properties regardless of the setting of this property. The default value
is TRUE. Use `niScope Initialize with
Options <scopeviref.chm::/niScope_Initialize_With_Options.html>`__ to
override this value.
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
Specifies whether to cache the value of properties. When caching is
enabled, the instrument driver keeps track of the current instrument
settings and avoids sending redundant commands to the instrument. Thus,
you can significantly increase execution speed. The instrument driver
can choose always to cache or never to cache particular properties,
regardless of the setting of this property. The default value is TRUE.
Use `niScope Initialize with
Options <scopeviref.chm::/niScope_Initialize_With_Options.html>`__ to
override this value.
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
Specifies whether to simulate instrument driver I/O operations. The
default value is FALSE. Use `niScope Initialize with
Options <scopeviref.chm::/niScope_Initialize_With_Options.html>`__ to
override this value.
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
Specifies whether the IVI engine keeps a list of the value coercions it
makes for ViInt32 and DBL properties. The default value is FALSE. Use
`niScope Initialize with
Options <scopeviref.chm::/niScope_Initialize_With_Options.html>`__ to
override this value.
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
interchangeability warnings when you call VIs. Interchangeability
warnings indicate that using your application with a different
instrument might cause different behavior.
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
Indicates the number of channels that the specific instrument driver
supports. For channel based properties, the IVI engine maintains a
separate cache value for each channel.
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
A string that contains the prefix for the instrument driver. The name of
each user-callable function in this driver starts with this prefix.
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
Indicates the resource descriptor the driver uses to identify the
physical device. If you initialize the driver with a logical name, this
property contains the resource descriptor that corresponds to the entry
in the IVI Configuration utility. If you initialize the instrument
driver with the resource descriptor, this property contains that value.
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
A string that contains the logical name you specified when opening the
current IVI session.

You can pass a logical name to `niScope
Initialize <scopeviref.chm::/niScope_Initialize.html>`__ or `niScope
Initialize with
Options <scopeviref.chm::/niScope_Initialize_With_Options.html>`__. The
IVI Configuration utility must contain an entry for the logical name.
The logical name entry refers to a virtual instrument section in the IVI
Configuration file. The virtual instrument section specifies a physical
device and initial user options.
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
A string that contains a comma-separated list of the instrument model
numbers supported by this driver.
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
A string that contains a comma-separated list of class-extension groups
that this driver implements.
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
A string that contains the firmware revision information for the current
instrument.
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
A string that contains the name of the instrument manufacturer, for
example, "National Instruments".
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
'description': 'A string that contains the model number of the current instrument.',
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
'description': '''
A string that contains the name of the vendor that supplies this driver,
for example, "National Instruments".
''',
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
'description': 'A string that contains the description of the instrument.',
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
The major version number of the class specification with which this
driver is compliant.
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
The minor version number of the class specification with which this
driver is compliant.
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
'description': '''
The string that contains additional version information about this
instrument driver.
''',
},
    },
    1150001: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Horizontal:Number of Records',
        'name': 'HORZ_NUM_RECORDS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specify the number of records to acquire.

**Related topics:**

`Making Multiple-Record
Acquisitions <digitizers.chm::/Making_Multiple-Record_Acquisitions.html>`__
`Fetching Multiple-Record
Acquisitions <digitizers.chm::/Fetching_Multiple-Record_Acquisitions.html>`__
''',
},
    },
    1150002: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocking:Reference (Input) Clock Source',
        'name': 'INPUT_CLOCK_SOURCE',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the input source for the PLL reference clock for all boards
except the NI 5102. For the NI 5102 this property is the source of the
board clock.

**Defined Values**

VAL\_NO\_SOURCE

VAL\_PFI\_0

VAL\_PFI\_1

VAL\_PFI\_2

VAL\_PXI\_CLOCK

VAL\_CLK\_IN

VAL\_EXTERNAL

VAL\_RTSI\_CLOCK

**Related topics:**

`Reference Clock/Phase-Lock
Loop <digitizers.chm::/Reference_Clock.html>`__
''',
},
    },
    1150003: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocking:Output Clock Source',
        'name': 'OUTPUT_CLOCK_SOURCE',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the output source for the 10 MHz clock to which another
digitizer's sample clock can be phased-locked.

The NI 5102 uses a 20 MHz system clock.

**Defined Values**

None

VAL\_RTSI\_CLOCK

VAL\_PFI\_0

VAL\_PFI\_1

VAL\_PFI\_2

VAL\_CLK\_OUT

VAL\_RTSI\_0

VAL\_RTSI\_1

VAL\_RTSI\_2

VAL\_RTSI\_3

VAL\_RTSI\_4

VAL\_RTSI\_5

VAL\_RTSI\_6
''',
},
    },
    1150004: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'BoolEnableDisableRealtime',
        'lv_property': 'Horizontal:Enforce Realtime',
        'name': 'HORZ_ENFORCE_REALTIME',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Indicates whether the digitizer enforces real-time measurements or
allows equivalent-time measurements.

**Related topics:**

`Sampling Methods <digitizers.chm::/Sampling_Methods.html>`__ `Real-Time
Sampling <digitizers.chm::/Real-Time_Sampling.html>`__
''',
},
    },
    1150005: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Acquisition:Binary Sample Width',
        'name': 'BINARY_SAMPLE_WIDTH',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Indicates the bit width of the binary data in the acquired waveform,
which can help you determine which Binary Fetch to use.

To configure the device to store samples with a lower resolution than
the native, set this property to the desired binary width. This
configuration can be useful for streaming at faster speeds, but at the
cost of resolution. The least significant bits are lost with this
configuration. Compare to the `Resolution <pniScope_Resolution.html>`__
property.

Valid Values: 8, 16, 32
''',
},
    },
    1150006: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggering:Trigger Hysteresis',
        'name': 'TRIGGER_HYSTERESIS',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the size of the hysteresis window on either side of the
trigger level.

The digitizer triggers when the trigger signal passes through the
threshold you specify with the Trigger Level parameter, has the slope
you specify with the Trigger Slope parameter, and passes through the
hysteresis window that you specify with this parameter.

Units: Volts

Min Value: 0

Max Value for positive trigger slope:

*Hysteresis - trigger level >= -(vertical range/2) + vertical offset*

Max value for negative trigger slope:

*Hysteresis + trigger level <= (vertical range/2) + vertical offset*
''',
},
    },
    1150007: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocking:Clock Sync Pulse Source',
        'name': 'CLOCK_SYNC_PULSE_SOURCE',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
For the NI 5102, specifies the line on which the sample clock is sent or
received. For the NI 5112/5620/5621, specifies the line on which the
one-time sync pulse is sent or received.

This line should be the same for all devices to be synchronized.

**Defined Values**

VAL\_NO\_SOURCE

VAL\_RTSI\_0

VAL\_RTSI\_1

VAL\_RTSI\_2

VAL\_RTSI\_3

VAL\_RTSI\_4

VAL\_RTSI\_5

VAL\_RTSI\_6

VAL\_PFI\_1

VAL\_PFI\_2
''',
},
    },
    1150008: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:Master Enable',
        'name': 'MASTER_ENABLE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the device is a master or a slave.

The master device is typically the originator of the trigger signal and
clock sync pulse. For a stand-alone device, set this property to FALSE.

**Valid Range**

TRUE—Master

FALSE—Slave
''',
},
    },
    1150009: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Horizontal:Min Sample Rate',
        'name': 'MIN_SAMPLE_RATE',
        'resettable': 'Yes',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the sampling rate (in Samples/second) for the acquisition.
This attribute is invalid when the device is configured to use an
external sample clock timebase. When a DDC is enabled, this attribute
specifices the IQ rate. When both the `Time Per
Record <pniScope_TimePerRecord.html>`__ Property and the Min Sample Rate
Property are set, the attribute that was set first is ignored.

Valid Values: The combination of sampling rate and minimum record length
must allow the digitizer to sample at a valid sampling rate for the
acquisition type specified in the `niScope Configure
Acquisition <scopeviref.chm::/niScope_Configure_Acquisition.html>`__ VI
and not require more memory than the onboard memory module allows.

`Sample Rate <digitizers.chm::/Sample_Rate.html>`__ `Coercions of
Horizontal Parameters <digitizers.chm::/Horizontal_Parameters.html>`__
''',
},
    },
    1150012: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TriggerWindowMode',
        'lv_property': 'Triggering:Trigger Window:Window Mode',
        'name': 'TRIGGER_WINDOW_MODE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether to trigger when the signal enters or leaves the window
specified by the `Trigger Window Low
Level <pniScope_TriggerWindowLowLevel.html>`__ property or the `Trigger
Window High Level <pniScope_TriggerWindowHighLevel.html>`__ property.

**Related topics:**

`Window Triggers <digitizers.chm::/Window_Triggers.html>`__ `Trigger
Parameters <digitizers.chm::/Trigger_Parameters.html>`__
''',
},
    },
    1150013: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggering:Trigger Window:Low Level',
        'name': 'TRIGGER_WINDOW_LOW_LEVEL',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Pass the lower voltage threshold you want the digitizer to use for
window triggering.

The digitizer triggers when the trigger signal enters or leaves the
window you specify with this property and the `Trigger Window High
Level <pniScope_TriggerWindowHighLevel.html>`__ property.

The values of the `Vertical Range <pniScope_VerticalRange.html>`__
property and the `Vertical Offset <pniScope_VerticalOffset.html>`__
property determine the valid range for this property on the channel you
specify with the `Trigger Source <pniScope_TriggerSource.html>`__
property.

The value you pass for this parameter must meet the following
conditions:

*Low Trigger Level <= Vertical Range/2 + Vertical Offset*

*Low Trigger Level >= (-Vertical Range/2) + Vertical Offset*

*Low Trigger Level < High Trigger Level*

**Related topics:**

`Window Triggers <digitizers.chm::/Window_Triggers.html>`__
''',
},
    },
    1150014: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggering:Trigger Window:High Level',
        'name': 'TRIGGER_WINDOW_HIGH_LEVEL',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Pass the upper voltage threshold you want the digitizer to use for
window triggering.

The digitizer triggers when the trigger signal enters or leaves the
window you specify with the Trigger Window Low Level property and this
property.

The values of the `Vertical Range <pniScope_VerticalRange.html>`__
property and the `Vertical Offset <pniScope_VerticalOffset.html>`__
property determine the valid range for the Trigger Window Low Level
property on the channel you specify with the `Trigger
Source <pniScope_TriggerSource.html>`__ property.

The value you pass for this parameter must meet the following
conditions:

*High Trigger Level <= Vertical Range/2 + Vertical Offset*

*High Trigger Level >= (-Vertical Range/2) + Vertical Offset*

*High Trigger Level > Low Trigger Level*

**Related topics:**

`Window Triggers <digitizers.chm::/Window_Triggers.html>`__
''',
},
    },
    1150016: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'RefLevelUnits',
        'lv_property': 'Waveform Measurement:Reference Levels:Units',
        'name': 'MEAS_REF_LEVEL_UNITS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the units for the waveform measurement reference levels.

If you choose percentage, the measurement routine uses the `Percentage
Method <pniScope_PercentageMethod.html>`__ property to map the
percentage values to voltages. If you choose voltage units, you can set
the voltage thresholds directly and avoid extra calculations.
''',
},
    },
    1150018: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Waveform Measurement:Other Channel',
        'name': 'MEAS_OTHER_CHANNEL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the second channel for two-channel measurements, such as `Add
Channels <Digitizers.chm::/Add_Channels.html>`__. If processing steps
are registered with this channel, the processing happens before the
waveform is used in a two-channel measurement. The default value is 0.
''',
},
    },
    1150019: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Waveform Measurement:Hysteresis Percent',
        'name': 'MEAS_HYSTERESIS_PERCENT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Digital hysteresis that is used in several of the scalar waveform
measurements. This property specifies the percentage of the full-scale
vertical range for the hysteresis window size. The default value is 2%.
''',
},
    },
    1150020: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Waveform Measurement:Last Acq. Histogram Size',
        'name': 'MEAS_LAST_ACQ_HISTOGRAM_SIZE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the size (that is, the number of bins) in the last acquisition
histogram. This histogram is used to determine several scalar
measurements, most importantly voltage low and voltage high. The default
value is 256.
''',
},
    },
    1150021: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Waveform Measurement:Voltage Histogram:Size',
        'name': 'MEAS_VOLTAGE_HISTOGRAM_SIZE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of bins in the running voltage histogram. The
default value is 256.

This value is used during the first running voltage histogram
measurement, and it is not updated until you call `niScope Clear
Waveform Measurement
Stats <scopeviref.chm::/niScope_Clear_Waveform_Measurement_Stats.html>`__.
''',
},
    },
    1150022: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Waveform Measurement:Voltage Histogram:Low Volts',
        'name': 'MEAS_VOLTAGE_HISTOGRAM_LOW_VOLTS',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the minimum voltage value in the running voltage histogram.
The default value is -10.0.

This value is used during the first running voltage histogram
measurement, and it is not updated until you call `niScope Clear
Waveform Measurement
Stats <scopeviref.chm::/niScope_Clear_Waveform_Measurement_Stats.html>`__.
''',
},
    },
    1150023: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Waveform Measurement:Voltage Histogram:High Volts',
        'name': 'MEAS_VOLTAGE_HISTOGRAM_HIGH_VOLTS',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the maximum voltage value in the running voltage histogram.
The default value is 10.0.

This value is used during the first running voltage histogram
measurement, and it is not updated until you call `niScope Clear
Waveform Measurement
Stats <scopeviref.chm::/niScope_Clear_Waveform_Measurement_Stats.html>`__.
''',
},
    },
    1150024: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Waveform Measurement:Time Histogram:Size',
        'name': 'MEAS_TIME_HISTOGRAM_SIZE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Determines the multiple acquisition time histogram size. The size is set
during the first call to a time histogram measurement after you clear
the measurement history with `niScope Clear Waveform Measurement
Stats <scopeviref.chm::/niScope_Clear_Waveform_Measurement_Stats.html>`__.
''',
},
    },
    1150025: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Waveform Measurement:Time Histogram:Low Volts',
        'name': 'MEAS_TIME_HISTOGRAM_LOW_VOLTS',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the low voltage limit for the multi-acquisition time
histogram. Only points in the waveform between the low and high voltage
limits are included in the histogram. The default value is -10.0.

This value is used during the first running time histogram measurement,
and it is not updated until you call `niScope Clear Waveform Measurement
Stats <scopeviref.chm::/niScope_Clear_Waveform_Measurement_Stats.html>`__.
''',
},
    },
    1150026: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Waveform Measurement:Time Histogram:High Volts',
        'name': 'MEAS_TIME_HISTOGRAM_HIGH_VOLTS',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the high voltage limit for the Multi-Acquisition time
histogram. Only points in the waveform between the low and high voltage
limits are included in the histogram. The default value is 10.0 V.

This value is used during the first time histogram measurement, and it
is not updated until you call `niScope Clear Waveform Measurement
Stats <scopeviref.chm::/niScope_Clear_Waveform_Measurement_Stats.html>`__.
''',
},
    },
    1150027: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Waveform Measurement:Time Histogram:Low Time',
        'name': 'MEAS_TIME_HISTOGRAM_LOW_TIME',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the minimum time limit (in seconds) of the multi-acquisition
time histogram, where the time is in seconds relative to the trigger
position. Only points in the waveform between the low and high time
limits are included in the histogram. The default value is -5.0e-4 .

This value is used during the first time histogram measurement, and it
is not updated until you call `niScope Clear Waveform Measurement
Stats <scopeviref.chm::/niScope_Clear_Waveform_Measurement_Stats.html>`__.
''',
},
    },
    1150028: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Waveform Measurement:Time Histogram:High Time',
        'name': 'MEAS_TIME_HISTOGRAM_HIGH_TIME',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the maximum time limit (in seconds) of the Multi-Acquisition
time histogram, where the time is in seconds relative to the trigger
position. Only points in the waveform between the low and high time
limits are included in the histogram. The default value is 5.0e-4 .

This value is used during the first time histogram measurement, and it
is not updated until you call `niScope Clear Waveform Measurement
Stats <scopeviref.chm::/niScope_Clear_Waveform_Measurement_Stats.html>`__.
''',
},
    },
    1150029: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Waveform Measurement:Interpolation:Polynomial Interpolation Order',
        'name': 'MEAS_POLYNOMIAL_INTERPOLATION_ORDER',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the order of the polynomial used during the polynomial
interpolation array measurement. For example, an order of 1 is linear
interpolation whereas an order of 2 specifies parabolic interpolation.
Any positive integer is valid. The default value is 1 (linear
interpolation).
''',
},
    },
    1150030: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Waveform Measurement:Interpolation:Sampling Factor',
        'name': 'MEAS_INTERPOLATION_SAMPLING_FACTOR',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
The new number of points for polynomial interpolation is the sampling
factor times the input number of points. The default value is 0.0.

For example, if you acquire 1,000 points with the digitizer and set this
property to 2.5, calling the `niScope Fetch Measurement
(poly) <scopeviref.chm::/niScope_Fetch_Measurement_(poly).html>`__ VI
(Measurement Scalar DBL instance), with the Polynomial Interpolation
measurement resamples the waveform to 2,500 points.
''',
},
    },
    1150031: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Waveform Measurement:Filter:Cutoff Frequency',
        'name': 'MEAS_FILTER_CUTOFF_FREQ',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the cutoff frequency in hertz for filters of type lowpass and
highpass. The cutoff frequency definition varies depending on the
filter. The default value is 1.0e6 Hz.
''',
},
    },
    1150032: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Waveform Measurement:Filter:Center Frequency',
        'name': 'MEAS_FILTER_CENTER_FREQ',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
The center frequency in hertz for filters of type bandpass and bandstop.
The width of the filter is specified by Filter Width, where the cutoff
frequencies are the center width. The default value is 1.0e6 Hz.
''',
},
    },
    1150033: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Waveform Measurement:Filter:Ripple',
        'name': 'MEAS_FILTER_RIPPLE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the amount of passband ripple (in dB) for Chebyshev filters.
More ripple gives a sharper cutoff for a given filter order. The default
value is 0.1.

Valid Values: >0.0
''',
},
    },
    1150034: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Waveform Measurement:Filter:Percent Waveform Transient',
        'name': 'MEAS_FILTER_TRANSIENT_WAVEFORM_PERCENT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
The percentage (0 - 100%) of the infinite impulse response (IIR)
filtered waveform to eliminate from the beginning of the waveform. This
action allows eliminating the transient portion of the waveform that is
undefined due to the assumptions necessary at the boundary condition.
The default value is 20.0%.

Valid Range: 0.0 - 100.0%
''',
},
    },
    1150035: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'FilterType',
        'lv_property': 'Waveform Measurement:Filter:Type',
        'name': 'MEAS_FILTER_TYPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the type of digital filter. The default value is lowpass.',
},
    },
    1150036: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Waveform Measurement:Filter:IIR Order',
        'name': 'MEAS_FILTER_ORDER',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the order of the infinite impulse response filter. The default
value is 2.

Valid Values: >0
''',
},
    },
    1150037: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Waveform Measurement:Filter:FIR Taps',
        'name': 'MEAS_FILTER_TAPS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of taps for the finite impulse response filter.
This value must be odd if the filter type is highpass or bandstop.
Otherwise, the magnitude response goes to zero as the frequency goes to
half the sampling rate. The default value is 25.

Valid Values: >0
''',
},
    },
    1150038: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Waveform Measurement:Reference Levels:Channel Based Low Ref Level',
        'name': 'MEAS_CHAN_LOW_REF_LEVEL',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the low reference level used in many scalar measurements. The
default value is 10.0%.

Units: Percentage of the signal based on the selected `Percentage Units
Method <pniScope_PercentageMethod.html>`__ property.
''',
},
    },
    1150039: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Waveform Measurement:Reference Levels:Channel Based Mid Ref Level',
        'name': 'MEAS_CHAN_MID_REF_LEVEL',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the mid reference level used in many scalar measurements. The
default value is 50%.

Units: Percentage of the signal based on the selected `Percentage Units
Method <pniScope_PercentageMethod.html>`__ property.
''',
},
    },
    1150040: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Waveform Measurement:Reference Levels:Channel Based High Ref Level',
        'name': 'MEAS_CHAN_HIGH_REF_LEVEL',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the high reference level used in many scalar measurements. The
default value is 90%.

Units: Percentage of the signal based on the selected `Percentage Units
Method <pniScope_PercentageMethod.html>`__ property.
''',
},
    },
    1150041: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Waveform Measurement:Filter:Width',
        'name': 'MEAS_FILTER_WIDTH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the width (in Hz) of a bandpass or bandstop filter. The cutoff
frequencies are the (center frequency property ± 0.5 × filter width).
The default value is 1.0e3.
''',
},
    },
    1150042: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'FIRFilterWindow',
        'lv_property': 'Waveform Measurement:Filter:FIR Window',
        'name': 'MEAS_FIR_FILTER_WINDOW',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the FIR window type. The symmetric windows are applied to the
FIR filter coefficients to limit passband ripple in FIR filters. The
default value is None (0).
''',
},
    },
    1150043: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Waveform Measurement:Array Gain',
        'name': 'MEAS_ARRAY_GAIN',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Every element of an array is multiplied by this scalar value during the
array gain measurement. The default value is 1.0.
''',
},
    },
    1150044: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Waveform Measurement:Array Offset',
        'name': 'MEAS_ARRAY_OFFSET',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Every element of an array is added to this scalar value during the array
offset measurement. The default value is 0.0.
''',
},
    },
    1150045: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'PercentageMethod',
        'lv_property': 'Waveform Measurement:Reference Levels:Percentage Units Method',
        'name': 'MEAS_PERCENTAGE_METHOD',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the method used to map percentage reference units to voltages.
The default value is BaseTop.
''',
},
    },
    1150046: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:Trigger Calibration Delay:Slave Trigger Delay',
        'name': 'SLAVE_TRIGGER_DELAY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the delay in seconds for the trigger from the master to the
slave.

This value adjusts the **initial X** value of the slave digitizer to
correct for the propagation delay between the master trigger output and
slave trigger input.
''',
},
    },
    1150047: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:Trigger Calibration Delay:Trigger to Star Delay',
        'name': 'TRIGGER_TO_STAR_DELAY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
A factory-programmed value that specifies the delay in seconds for the
trigger to the PXI Star Trigger line.

By itself, this property has no effect on the acquired data. However,
depending on how the trigger lines are routed between the master and
slave boards, you can use this value as a starting point to set the
`Slave Trigger Delay <pniScope_SlaveTriggerDelay.html>`__ property.

**Related topics:**

`PXI Star Trigger Line <digitizers.chm::/PXI_Star_Trigger_Line.html>`__
''',
},
    },
    1150048: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:Trigger Calibration Delay:Trigger to RTSI Delay',
        'name': 'TRIGGER_TO_RTSI_DELAY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
A factory-programmed value that specifies the delay in seconds for the
trigger to the RTSI bus.

By itself, this property has no effect on the acquired data. However,
depending on how the trigger lines are routed between the master and
slave digitizers, you can use this value as a starting point to set the
`Slave Trigger Delay <pniScope_SlaveTriggerDelay.html>`__ property.

**Related topics:**

`PXI Trigger Lines <digitizers.chm::/PXI_Trigger_Lines.html>`__
''',
},
    },
    1150049: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:Trigger Calibration Delay:Trigger to PFI Delay',
        'name': 'TRIGGER_TO_PFI_DELAY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
A factory-programmed value that specifies the delay in seconds for the
trigger to the PFI lines. By itself, this property has no effect on the
acquired data.

Depending on how the trigger lines are routed between the master and
slave digitizers, you can use this value as a starting point to set the
`Slave Trigger Delay <pniScope_SlaveTriggerDelay.html>`__ property.

**Related topics:**

`PFI Lines <digitizers.chm::/PFI_Lines.html>`__
''',
},
    },
    1150050: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:Trigger Calibration Delay:Trigger from Star Delay',
        'name': 'TRIGGER_FROM_STAR_DELAY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
A factory-programmed value that specifies the delay in seconds for PXI
Star Trigger line to the trigger input. By itself, this property has no
effect on the acquired data.

Depending on how the trigger lines are routed between the master and
slave digitizers, you can use this value as a starting point to set the
`Slave Trigger Delay <pniScope_SlaveTriggerDelay.html>`__ property.

**Related topics:**

`PXI Star Trigger Line <digitizers.chm::/PXI_Star_Trigger_Line.html>`__
''',
},
    },
    1150051: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:Trigger Calibration Delay:Trigger from RTSI Delay',
        'name': 'TRIGGER_FROM_RTSI_DELAY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
A factory-programmed value that specifies the delay in seconds for the
RTSI bus to the trigger input. By itself, this property has no effect on
the acquired data.

Depending on how the trigger lines are routed between the master and
slave digitizers, you can use this value as a starting point to set the
`Slave Trigger Delay <pniScope_SlaveTriggerDelay.html>`__ property.

**Related topics:**

`PXI Trigger Lines <digitizers.chm::/PXI_Trigger_Lines.html>`__
''',
},
    },
    1150052: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:Trigger Calibration Delay:Trigger from PFI Delay',
        'name': 'TRIGGER_FROM_PFI_DELAY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
A factory-programmed value that specifies the delay in seconds for the
PFI lines to the trigger input. By itself, this property has no effect
on the acquired data.

Depending on how the trigger lines are routed between the master and
slave digitizers, you can use this value as a starting point to set the
`Slave Trigger Delay <pniScope_SlaveTriggerDelay.html>`__ property.

**Related topics:**

`PFI Lines <digitizers.chm::/PFI_Lines.html>`__
''',
},
    },
    1150053: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:Start Trigger (Acq. Arm):Source',
        'name': 'ACQ_ARM_SOURCE',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the source the digitizer monitors for an acquisition arm
trigger. When an acquisition arm trigger is received, the digitizer
begins acquiring pretrigger samples.

**Defined Values**

VAL\_IMMEDIATE

VAL\_RTSI\_0

VAL\_RTSI\_1

VAL\_RTSI\_2

VAL\_RTSI\_3

VAL\_RTSI\_4

VAL\_RTSI\_5

VAL\_RTSI\_6

VAL\_PFI\_0

VAL\_PFI\_1

VAL\_PFI\_2

VAL\_PXI\_STAR

VAL\_SW\_TRIG\_FUNC
''',
},
    },
    1150065: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:Record Arm Source',
        'name': 'RECORD_ARM_SOURCE',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the source for the record arm. This property is only
applicable to Traditional NI-DAQ (Legacy) devices. For SMC-based or USB
devices, use the Synchronization:Advance Trigger:Source Property.

**Defined Values**

VAL\_IMMEDIATE

VAL\_RTSI\_0

VAL\_RTSI\_1

VAL\_RTSI\_2

VAL\_RTSI\_3

VAL\_RTSI\_4

VAL\_RTSI\_5

VAL\_RTSI\_6

VAL\_PFI\_0

VAL\_PFI\_1

VAL\_PFI\_2
''',
},
    },
    1150068: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Horizontal:Enable Records > Memory',
        'name': 'ALLOW_MORE_RECORDS_THAN_MEMORY',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Allows you to acquire more records than fit in onboard memory.

TRUE—Enables NI-SCOPE to fetch more records than fit in memory

FALSE—Disables NI-SCOPE from fetching more records than fit in memory

**Related topics:**

`Time Interleaved
Sampling <digitizers.chm::/TimeInterleavedSampling.html>`__
''',
'note': '''
The property can be used only in digitizers that support continuous
acquisition. Refer to `Features Supported by
Device <Digitizers.chm::/Features_Supported_Main.html>`__ to find out if
your digitizer supports continuous acquisition.
''',
},
    },
    1150069: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Horizontal:Memory Size',
        'name': 'ONBOARD_MEMORY_SIZE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the total combined amount of onboard memory for all channels in
bytes.
''',
},
    },
    1150070: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Horizontal:RIS Num Avg',
        'name': 'RIS_NUM_AVERAGES',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of averages in each RIS bin.

Averaging is useful in RIS because the trigger times are not evenly
spaced, so adjacent points in the reconstructed waveform cannot be
accurately spaced. By averaging, the errors in both time and voltage are
smoothed, minimizing the noise in the reconstructed waveform.

Valid Values: Greater than or equal to 0

**Related topics:**

`Sampling Methods <digitizers.chm::/Sampling_Methods.html>`__
`Equivalent-Time Sampling and Random Interleaved
Sampling <digitizers.chm::/ris.html>`__
''',
},
    },
    1150071: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'RISMethod',
        'lv_property': 'Horizontal:RIS Method',
        'name': 'RIS_METHOD',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the algorithm for random-interleaved sampling, which is used
if the sample rate exceeds the `Max Realtime Sample
Rate <pniScope_MaximumRealtimeSampleRate.html>`__.
''',
},
    },
    1150072: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Fetch Interleaved Data',
        'name': 'FETCH_INTERLEAVED_DATA',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Set to TRUE to retrieve one array with alternating values on the NI
5620/5621. This property can be used to retrieve a single array with I
and Q interleaved instead of two separate arrays. If set to TRUE, the
resulting array is twice the size of the actual record length. The
default value is FALSE.
''',
},
    },
    1150073: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Horizontal:Maximum Real Time Sample Rate',
        'name': 'MAX_REAL_TIME_SAMPLING_RATE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Returns the maximum real-time sample rate in hertz.

**Related topics:**

`Sampling Methods <digitizers.chm::/Sampling_Methods.html>`__ `Real-Time
Sampling <digitizers.chm::/Real-Time_Sampling.html>`__
''',
},
    },
    1150074: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Horizontal:Maximum RIS Rate',
        'name': 'MAX_RIS_RATE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Returns the maximum RIS sampling rate in hertz.

**Related topics:**

`Sampling Methods <digitizers.chm::/Sampling_Methods.html>`__
`Equivalent-Time Sampling and Random Interleaved
Sampling <digitizers.chm::/ris.html>`__
''',
},
    },
    1150075: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggering:Trigger Impedance',
        'name': 'TRIGGER_IMPEDANCE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Sets the impedance for the trigger channel (NI 5112 only).

**Defined Values**

1 M Ohm

50 Ohm
''',
},
    },
    1150076: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Device Number',
        'name': 'DEVICE_NUMBER',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Indicates the device number associated with the current session.',
},
    },
    1150077: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'FetchRelativeTo',
        'lv_property': 'Fetch:Fetch Relative To',
        'name': 'FETCH_RELATIVE_TO',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies which point in the acquired waveform is the first to be
fetched. This property specifies what the 'Fetch Offset' is relative to.
''',
},
    },
    1150078: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Fetch:Fetch Offset',
        'name': 'FETCH_OFFSET',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Sets the offset in samples; the samples returned also depend on the
`Fetch Relative To <pniScope_FetchRelativeTo.html>`__ property. The
default value is 0.

Valid Values: All integers
''',
},
    },
    1150079: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Fetch:Fetch Record Number',
        'name': 'FETCH_RECORD_NUMBER',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Sets the record to fetch. The record is from a channel you specify. The
default value is 0.

Valid Values: Values greater than or equal to 0
''',
},
    },
    1150080: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Fetch:Fetch Number of Records',
        'name': 'FETCH_NUM_RECORDS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Fetches multiple records. If you want to fetch all records from the
record you specify in the `Fetch Record
Number <pniScope_FetchRecordNumber.html>`__ property to the last record
configured, use -1. The default value is -1.

**Related topics:**

`Making Multiple-Record
Acquisitions <digitizers.chm::/Making_Multiple-Record_Acquisitions.html>`__
`Fetching Multiple-Record
Acquisitions <digitizers.chm::/Fetching_Multiple-Record_Acquisitions.html>`__
''',
},
    },
    1150081: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Fetch:Fetch Meas Num Samples',
        'name': 'FETCH_MEAS_NUM_SAMPLES',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Determines the number of samples to fetch from a digitizer when
performing a measurement. -1 means fetch all samples from the `Fetch
Offset <pniScope_FetchOffset.html>`__ property to the end of the current
record. The default value is -1.
''',
},
    },
    1150082: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Fetch:Points Done',
        'name': 'POINTS_DONE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Actual number of samples acquired since the last fetch, relative to the
configured value for `Fetch Relative
To <pniScope_FetchRelativeTo.html>`__, including `Fetch
Offset <pniScope_FetchOffset.html>`__, and for the current configured
`Fetch Record Number <pniScope_FetchRecordNumber.html>`__.
''',
},
    },
    1150083: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Fetch:Records Done',
        'name': 'RECORDS_DONE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Returns the number of records your digitizer has acquired.',
},
    },
    1150084: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Fetch:Fetch Backlog',
        'name': 'BACKLOG',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the number of points acquired that have not been fetched yet.

**Related topics:**

`Fetching Data <digitizers.chm::/Fetching_Data.html>`__
''',
},
    },
    1150085: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Horizontal:Advanced:5102 Adjust Pretrigger Samples',
        'name': '5102_ADJUST_PRETRIGGER_SAMPLES',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
When set to TRUE and the digitizer is set to master, the number of
pretrigger samples and total number of samples are adjusted to enable
synchronizing a master and slave NI 5102.
''',
},
    },
    1150086: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Device:Temperature',
        'name': 'DEVICE_TEMPERATURE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Returns the temperature of the device in degrees Celsius from the
onboard sensor.

**Related topics:**

`Thermal Shutdown <digitizers.chm::/Thermal_Shutdown.html>`__ `PXI/PXIe
Chassis Cooling <digitizers.chm::/chassis_with_PXIe.html>`__
''',
},
    },
    1150087: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocking:Sample Clock Timebase Source',
        'name': 'SAMP_CLK_TIMEBASE_SRC',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the source of the sample clock timebase, which is the timebase
used to control waveform sampling.

The actual sample rate may be the timebase itself or a scaled version of
the timebase, depending on the `Min Sample
Rate <pniScope_MinSampleRate.html>`__ property (for internal sources) or
the `Sample Clock Timebase
Divisor <pniScope_SampleClockTimebaseDivisor.html>`__ and `Sample Clock
Timebase Multiplier <pniScope_SampleClockTimebaseMultiplier.html>`__
properties (for external sources).

**Defined Values**

VAL\_CLK\_IN

VAL\_PXI\_STAR

VAL\_PFI\_0

VAL\_PFI\_1

VAL\_NO\_SOURCE

**Related topics:**

`Sample Clock <digitizers.chm::/Sample_Clock.html>`__
''',
},
    },
    1150088: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocking:Sample Clock Timebase Rate',
        'name': 'SAMP_CLK_TIMEBASE_RATE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the frequency in hertz of the external clock used as the
timebase source if the `Sample Clock Timebase
Source <pniScope_SampleClockTimebaseSource.html>`__ is an external
source.
''',
},
    },
    1150089: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocking:Sample Clock Timebase Divisor',
        'name': 'SAMP_CLK_TIMEBASE_DIV',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
If `Sample Clock Timebase
Source <pniScope_SampleClockTimebaseSource.html>`__ is an external
source, specifies the ratio between the sample clock timebase rate and
the actual sample rate, which can be slower.

**Related topics:**

`Sample Clock <digitizers.chm::/Sample_Clock.html>`__
''',
},
    },
    1150090: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocking:Reference Clock Rate',
        'name': 'REF_CLK_RATE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
If `Reference Clock Source <pniScope_ReferenceClockSource.html>`__ is an
external source, specifies the frequency (in hertz) of the input clock
(reference clock) to which the internal sample clock timebase is
synchronized.

**Related topics:**

`Reference Clock/Phase-Lock
Loop <digitizers.chm::/Reference_Clock.html>`__
''',
'note': '''
Refer to `Features Supported by
Device <Digitizers.chm::/Features_Supported_Main.html>`__ for valid
values.
''',
},
    },
    1150091: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocking:Exported Sample Clock Output Terminal',
        'name': 'EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Exports the sample clock to a specified terminal. This property is not
supported by all digitizers.

The full sample clock rate can be exported to the CLK\_OUT connector. If
decimating, the divided down sample clock rate can be exported to any of
the valid destinations.

**Defined Values**

VAL\_CLK\_OUT

VAL\_RTSI\_0

VAL\_RTSI\_1

VAL\_RTSI\_2

VAL\_RTSI\_3

VAL\_RTSI\_4

VAL\_RTSI\_5

VAL\_RTSI\_6

VAL\_PXI\_STAR

VAL\_PFI\_0

VAL\_PFI\_1

VAL\_PFI\_2
''',
},
    },
    1150093: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggering:Trigger Video:Enable DC Restore',
        'name': 'ENABLE_DC_RESTORE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Restores the video-triggered data retrieved by the digitizer to the
video signal's zero reference point. The default value is FALSE.
''',
},
    },
    1150094: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:Advance Trigger:Source',
        'name': 'ADV_TRIG_SRC',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the source the digitizer monitors for an advance trigger. When
the advance trigger is received, the digitizer begins acquiring
pretrigger samples for the next record.

**Defined Values**

VAL\_IMMEDIATE

VAL\_RTSI\_0

VAL\_RTSI\_1

VAL\_RTSI\_2

VAL\_RTSI\_3

VAL\_RTSI\_4

VAL\_RTSI\_5

VAL\_RTSI\_6

VAL\_PFI\_0

VAL\_PFI\_1

VAL\_PFI\_2

VAL\_PXI\_STAR

VAL\_SW\_TRIG\_FUNC
''',
},
    },
    1150095: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:Arm Reference Trigger:Source',
        'name': 'ARM_REF_TRIG_SRC',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the source the digitizer monitors for an arm reference
trigger. When the arm reference trigger is received, the digitizer
begins searching for the reference (stop) trigger from the
user-configured trigger source.

**Defined Values**

VAL\_IMMEDIATE

VAL\_RTSI\_0

VAL\_RTSI\_1

VAL\_RTSI\_2

VAL\_RTSI\_3

VAL\_RTSI\_4

VAL\_RTSI\_5

VAL\_RTSI\_6

VAL\_PFI\_0

VAL\_PFI\_1

VAL\_PFI\_2

VAL\_PXI\_STAR

VAL\_SW\_TRIG\_FUNC
''',
},
    },
    1150096: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Horizontal:Advanced:Enable TDC',
        'name': 'REF_TRIG_TDC_ENABLE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies that the digitizer should record the trigger position
precisely using time-digital conversion (TDC).

**Related topics:**

`TDC <digitizers.chm::/TDC.html>`__
''',
},
    },
    1150097: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:Start Trigger (Acq. Arm):Output Terminal',
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the destination to export the Start trigger. When the start
trigger is received, the digitizer begins acquiring data. Refer to the
device specifications document for a list of valid destinations.
''',
},
    },
    1150098: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggering:Trigger Output Terminal',
        'name': 'EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the destination to export the Reference (Stop) Trigger Refer
to the device specifications document for a list of valid destinations.

**Defined Values**

VAL\_EXTERNAL

VAL\_RTSI\_0

VAL\_RTSI\_1

VAL\_RTSI\_2

VAL\_RTSI\_3

VAL\_RTSI\_4

VAL\_RTSI\_5

VAL\_RTSI\_6

VAL\_PFI\_0

VAL\_PFI\_1

VAL\_PFI\_2

VAL\_PXI\_STAR
''',
},
    },
    1150099: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:End of Record:Output Terminal',
        'name': 'END_OF_RECORD_EVENT_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the destination for the End of Record event. When this event
is asserted, the digitizer has completed sampling a record. Refer to the
device specifications document for a list of valid destinations.

**Defined Values**

VAL\_RTSI\_0

VAL\_RTSI\_1

VAL\_RTSI\_2

VAL\_RTSI\_3

VAL\_RTSI\_4

VAL\_RTSI\_5

VAL\_RTSI\_6

VAL\_PFI\_0

VAL\_PFI\_1

VAL\_PFI\_2

VAL\_PXI\_STAR
''',
},
    },
    1150101: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:End of Acquisition:Output Terminal',
        'name': 'END_OF_ACQUISITION_EVENT_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the destination for the End of Acquisition event. When this
event is asserted, the digitizer has completed sampling all records.
Refer to the device specifications document for a list of valid
destinations.

**Defined Values**

VAL\_RTSI\_0

VAL\_RTSI\_1

VAL\_RTSI\_2

VAL\_RTSI\_3

VAL\_RTSI\_4

VAL\_RTSI\_5

VAL\_RTSI\_6

VAL\_PFI\_0

VAL\_PFI\_1

VAL\_PFI\_2

VAL\_PXI\_STAR
''',
},
    },
    1150102: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Acquisition:Resolution',
        'name': 'RESOLUTION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Indicates the actual resolution in bits of valid data (as opposed to
padding bits) in the acquired waveform. Compare to the `Binary Sample
Width <pniScope_BinarySampleWidth.html>`__ property.

Valid Values: 8 to 32
''',
},
    },
    1150103: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Triggering:Start To Ref Trigger Holdoff',
        'name': 'START_TO_REF_TRIGGER_HOLDOFF',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Pass the length of time (in seconds) you want the digitizer to wait
after it starts acquiring data until the digitizer enables the trigger
system to detect a reference (stop) trigger.

Valid Values: 0.0 - 171.8
''',
},
    },
    1150104: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Device:Serial Number',
        'name': 'SERIAL_NUMBER',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': 'Returns the serial number of the device.',
},
    },
    1150105: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocking:Advanced:Oscillator Phase DAC Value',
        'name': 'OSCILLATOR_PHASE_DAC_VALUE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Gets or sets the binary phase DAC value that controls the delay added to
the Phase Locked Loop (PLL) of the sample clock. The default value is "
".
''',
'note': '''
If this value is set, sample clock adjustments and TClk cannot do any
subsample adjustment of the timebase sample clock.
''',
},
    },
    1150106: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Acquisition:Advanced:Enable RIS in Auto Setup',
        'name': 'RIS_IN_AUTO_SETUP_ENABLE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Indicates whether the digitizer should use RIS sample rates when
searching for a frequency in autosetup.
''',
},
    },
    1150107: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'TerminalConfiguration',
        'lv_property': 'Vertical:Channel Terminal Configuration',
        'name': 'CHANNEL_TERMINAL_CONFIGURATION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies how the digitizer configures the channel terminal.

**Related topics:**

`NI 5922 Channel Terminal
Configuration <digitizers.chm::/5922_Chan_Terminal_Configuration.html>`__
''',
},
    },
    1150109: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:Advance Trigger:Output Terminal',
        'name': 'EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the destination for the advance trigger. When the advance
trigger is received, the digitizer begins acquiring pretrigger samples.
''',
},
    },
    1150110: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:Ready for Start:Output Terminal',
        'name': 'READY_FOR_START_EVENT_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the destination to export the Start trigger. When the start
trigger is received, the digitizer begins acquiring data. Refer to the
device specifications document for a list of valid destinations.

**Defined Values**

VAL\_RTSI\_0

VAL\_RTSI\_1

VAL\_RTSI\_2

VAL\_RTSI\_3

VAL\_RTSI\_4

VAL\_RTSI\_5

VAL\_RTSI\_6

VAL\_PFI\_0

VAL\_PFI\_1

VAL\_PFI\_2

VAL\_PXI\_STAR
''',
},
    },
    1150111: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:Ready for Reference:Output Terminal',
        'name': 'READY_FOR_REF_EVENT_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the destination for the Ready for Reference Event. When this
event is asserted, the digitizer is ready to receive a reference
trigger. Refer to the device-specific documentation in the *NI
High-Speed Digitizers Help* for a list of valid destinations for your
device.
''',
},
    },
    1150112: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:Ready for Advance:Output Terminal',
        'name': 'READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the destination for the advance trigger. When the advance
trigger is received, the digitizer begins acquiring pretrigger samples.

**Defined Values**

VAL\_RTSI\_0

VAL\_RTSI\_1

VAL\_RTSI\_2

VAL\_RTSI\_3

VAL\_RTSI\_4

VAL\_RTSI\_5

VAL\_RTSI\_6

VAL\_PFI\_0

VAL\_PFI\_1

VAL\_PFI\_2

VAL\_PXI\_STAR
''',
},
    },
    1150128: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'BoolEnableDisableTIS',
        'lv_property': 'Horizontal:Enable Time Interleaved Sampling',
        'name': 'ENABLE_TIME_INTERLEAVED_SAMPLING',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Extends the maximum sample rate on the specified Active Channel for some
devices that support Time Interleaved Sampling (TIS). TIS enables the
device to use multiple ADCs to sample the same waveform at a higher
effective real-time rate. NI 5152/5153/5154 devices fully support
Read/Write ability for this property. For other devices that use TIS
mode, such as the NI 5185/5186, this property is Read Only.

**Related topics:**

`Time Interleaved
Sampling <digitizers.chm::/TimeInterleavedSampling.html>`__ `Configuring
the Horizontal
Settings <digitizers.chm::/Configuring_Horizontal.html>`__
''',
},
    },
    1150129: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Synchronization:5 Volt Power:Output Terminal',
        'name': '5V_OUT_OUTPUT_TERMINAL',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the destination for the 5 Volt power signal. Refer to the
device specifications document for a list of valid destinations.

**Defined Values**

VAL\_RTSI\_0

VAL\_RTSI\_1

VAL\_RTSI\_2

VAL\_RTSI\_3

VAL\_RTSI\_4

VAL\_RTSI\_5

VAL\_RTSI\_6

VAL\_PFI\_0

VAL\_PFI\_1

VAL\_PFI\_2

VAL\_PXI\_STAR
''',
'note': 'This property is supported only for NI 5152/5153/5154 devices.',
},
    },
    1150271: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'FlexFIRAntialiasFilterType',
        'lv_property': 'Vertical:Advanced:Flex FIR Antialias Filter Type',
        'name': 'FLEX_FIR_ANTIALIAS_FILTER_TYPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
The NI 5922 flexible-resolution digitizer uses an onboard FIR lowpass
antialias filter. Use this property to select from several types of
filters to achieve desired filtering characteristics. For most
applications, the default value of this property is recommended. The
other available filters are useful for optimizing settling time
measurements of step responses. The default value is 48 Tap Standard.

**Related topics:**

`Aliasing <digitizers.chm::/Aliasing.html>`__ `FIR
Filters <digitizers.chm::/FIR_Filters.html>`__
''',
'note': '''
Settling time values refer to the FIR filter only and do not take into
account settling time caused by the analog front end. Refer to the *NI
PXI-5922 Specifications* for combined digital and analog settling times.
''',
},
    },
    1150278: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggering:Auto Triggered',
        'name': 'TRIGGER_AUTO_TRIGGERED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the acquisition was triggered automatically. Auto
triggering occurs if the Trigger Modifier property is set to Auto
Trigger and no trigger has been received for a certain amount of time.

**Related topics:**

`Trigger Types <digitizers.chm::/Trigger_Types.html>`__
''',
},
    },
    1150279: {
        'access': 'read only',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device:Accessory:Gain',
        'name': 'SIGNAL_COND_GAIN',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Returns the calibration gain for the current device configuration.

**Related topics:**

`NI 5122/5124/5142
Calibration <digitizers.chm::/5122_Calibration.html>`__
''',
'note': '''
This property is only supported by the NI PXI-5900 differential
amplifier.
''',
},
    },
    1150280: {
        'access': 'read only',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device:Accessory:Offset',
        'name': 'SIGNAL_COND_OFFSET',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Returns the calibration offset for the current device configuration.

**Related topics:**

`NI 5122/5124/5142
Calibration <digitizers.chm::/5122_Calibration.html>`__
''',
'note': '''
This property is supported only by the NI PXI-5900 differential
amplifier.
''',
},
    },
    1150300: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Onboard Signal Processing:DDC:DDC Enabled',
        'name': 'DDC_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables/disables the digital downconverter (DDC) block of the digitizer.
When the DDC block is disabled, all DDC-related properties are disabled
and have no effect on the acquired signal. The default value is FALSE.
''',
'note': '''
This property can be used only with high-speed digitizers that support
onboard signal processing (OSP). NI-SCOPE returns an error if you use
this property with a device that does not support OSP. For NI 5620/5621
digitizers, use `Enable DDC <pniScope_EnableDDC.html>`__.
''',
},
    },
    1150302: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Onboard Signal Processing:DDC:Frequency Translation Enabled',
        'name': 'DDC_FREQUENCY_TRANSLATION_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables/disables frequency translating the data around the user-selected
center frequency down to baseband. The default value is TRUE.
''',
'note': '''
This property can be used only with high-speed digitizers that support
onboard signal processing (OSP). NI-SCOPE returns an error if you use
this property with a device that does not support OSP.
''',
},
    },
    1150303: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Onboard Signal Processing:DDC:Center Frequency',
        'name': 'DDC_CENTER_FREQUENCY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
The frequency at which the `DDC <Digitizers.chm::/Glossary.html#DDC>`__
block frequency translates the input data. The default value is 10 MHz.

**Valid Values**

0 - (0.5 × Sample Clock Timebase Rate for digitizer)
''',
'note': '''
This property can be used only with high-speed digitizers that support
onboard signal processing (OSP). NI-SCOPE returns an error if you use
this property with a device that does not support OSP.
''',
},
    },
    1150304: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'DataProcessingMode',
        'lv_property': 'Onboard Signal Processing:DDC:Data Processing Mode',
        'name': 'DDC_DATA_PROCESSING_MODE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
The way in which data is processed by the DDC block. The default value
is Complex.
''',
'note': '''
This property can be used only with high-speed digitizers that support
onboard signal processing (OSP). NI-SCOPE returns an error if you use
this property with a device that does not support OSP.
''',
},
    },
    1150305: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Onboard Signal Processing:DDC:Signal Adjustments:Frequency Translation:Frequency Translation Phase I',
        'name': 'DDC_FREQUENCY_TRANSLATION_PHASE_I',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
The I oscillator phase in degrees at the first point acquired. The
default value is 0.

**Valid Values**

-360 to 360
''',
'note': '''
This property can be used only with high-speed digitizers that support
onboard signal processing (OSP). NI-SCOPE returns an error if you use
this property with a device that does not support OSP.
''',
},
    },
    1150306: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Onboard Signal Processing:DDC:Signal Adjustments:Frequency Translation:Frequency Translation Phase Q',
        'name': 'DDC_FREQUENCY_TRANSLATION_PHASE_Q',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
The Q oscillator phase in degrees at the first point acquired. Use this
property only when the `Data Processing
Mode <pniScope_DataProcessingMode.html>`__ property is set to Complex.
The default value is 90.

**Valid Values**

-360 to 360
''',
'note': '''
This property can be used only with high-speed digitizers that support
onboard signal processing (OSP). NI-SCOPE returns an error if you use
this property with a device that does not support OSP.
''',
},
    },
    1150307: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Vertical:Advanced:Digital Gain',
        'name': 'DIGITAL_GAIN',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Applies gain to the specified channel in hardware before any onboard
signal processing occurs. The default value is 1.

The output of the digital gain/offset block is as follows:

(*ADC value* × *digital gain*) + *digital offset*

Units: Unitless

Valid Values: -1.5 to 1.5

**Related topics:**

`NI 5622 Onboard Signal Processing
(OSP) <digitizers.chm::/5622_OSP_diagram.html>`__
''',
'note': '''
This property can be used only with high-speed digitizers that support
onboard signal processing (OSP). NI-SCOPE returns an error if you use
this property with a device that does not support OSP.
''',
},
    },
    1150308: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Vertical:Advanced:Digital Offset',
        'name': 'DIGITAL_OFFSET',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Applies offset to the specified channel in hardware before any onboard
signal processing occurs. The default value is 0.

Units: Volts

**Valid Values**

±(Vertical Range × 0.4)

The output of the digital gain/offset block is as follows:

(*ADC value* × *digital gain*) + *digital offset*

**Related topics:**

`NI 5622 Onboard Signal Processing
(OSP) <digitizers.chm::/5622_OSP_diagram.html>`__
''',
'note': '''
This property can be used only with high-speed digitizers that support
onboard signal processing (OSP). NI-SCOPE returns an error if you use
this property with a device that does not support OSP.
''',
},
    },
    1150309: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'OverflowErrorReporting',
        'lv_property': 'Onboard Signal Processing:OSP Overflow Error Reporting',
        'name': 'OVERFLOW_ERROR_REPORTING',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Configures error reporting when the onboard signal processing block
detects an overflow in any of its stages. Overflows lead to clipping of
the waveform. The default value is Warning.
''',
},
    },
    1150310: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Onboard Signal Processing:DDC:Q Source',
        'name': 'DDC_Q_SOURCE',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the channel that is the input to the Q data stream of the
`DDC <Digitizers.chm::/Glossary.html#DDC>`__. The default value is the
channel to which the property is registered.

Valid Values: All valid channels for the device.
''',
'note': '''
This property can be used only with high-speed digitizers that support
onboard signal processing (OSP). NI-SCOPE returns an error if you use
this property with a device that does not support OSP.
''',
},
    },
    1150311: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'BoolEnableDisableIQ',
        'lv_property': 'Onboard Signal Processing:DDC:Fetch Interleaved IQ Data',
        'name': 'FETCH_INTERLEAVED_IQ_DATA',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether a fetch call retrieves a single waveform with I and Q
interleaved, or two separate waveforms. If enabled, the number of
elements returned by scalar fetch types (such as 16-bit integer) is
twice the requested number of samples. If disabled during DDC
acquisitions in Complex mode, two noninterleaved arrays of data are
returned per channel, per record.
''',
'note': '''
This property can be used only with high-speed digitizers that support
onboard signal processing (OSP). NI-SCOPE returns an error if you use
this property with a device that does not support OSP.
''',
},
    },
    1150312: {
        'access': 'read only',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Onboard Signal Processing:Equalization:Equalization Num Coefficients',
        'name': 'EQUALIZATION_NUM_COEFFICIENTS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the number of coefficients that the equalization FIR filter can
accept. This filter is designed to compensate the input signal for
artifacts introduced to the signal outside of the digitizer. Because
this filter is a generic FIR filter, any coefficients are valid.
Coefficient values should be between +1 and -1.
''',
'note': '''
This property can be used only with high-speed digitizers that support
onboard signal processing (OSP). NI-SCOPE returns an error if you use
this property with a device that does not support OSP.
''',
},
    },
    1150313: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Onboard Signal Processing:Equalization:Equalization Filter Enabled',
        'name': 'EQUALIZATION_FILTER_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables the onboard signal processing equalization FIR block, which is
connected directly to the input signal. The equalization filter is
designed to compensate the input signal for artifacts introduced to the
signal outside of the digitizer. Because this filter is a generic FIR
filter, any coefficients are valid. Coefficient values should be between
+1 and -1. The default value is FALSE.
''',
'note': '''
This property can be used only with high-speed digitizers that support
onboard signal processing (OSP). NI-SCOPE returns an error if you use
this property with a device that does not support OSP.
''',
},
    },
    1150314: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'RefTriggerDetectorLocation',
        'lv_property': 'Triggering:Onboard Signal Processing:Ref Trigger Detection Location',
        'name': 'REF_TRIGGER_DETECTOR_LOCATION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies which reference trigger detection circuitry to use on the
device.
''',
'note': '''
This property can be used only with high-speed digitizers that support
onboard signal processing (OSP). NI-SCOPE returns an error if you use
this property with a device that does not support OSP.
''',
},
    },
    1150315: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggering:Onboard Signal Processing:Ref Trigger Min Quiet Time',
        'name': 'REF_TRIGGER_MINIMUM_QUIET_TIME',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the amount of time (in seconds) the trigger circuit must not
detect a signal above the `trigger level <pniScope_TriggerLevel.html>`__
(or below the trigger level if the trigger slope is negative) before the
trigger is armed. This property is useful for triggering at the
beginning of signal bursts instead of in the middle of signal bursts.
The default value is 0.

**Valid Values**

Any value greater than or equal to 0.
''',
'note': '''
This property can be used only with high-speed digitizers that support
onboard signal processing (OSP). NI-SCOPE returns an error if you use
this property with a device that does not support OSP.
''',
},
    },
    1150316: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Fetch:Data Transfer Block Size',
        'name': 'DATA_TRANSFER_BLOCK_SIZE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the maximum number of samples to transfer at one time from the
device to host memory. Increasing this number should result in better
fetching performance because the driver does not need to restart the
transfers as often. However, increasing this number may also increase
the amount of page-locked memory required from the system.
''',
},
    },
    1150318: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Vertical:Advanced:Bandpass Filter Enabled',
        'name': 'BANDPASS_FILTER_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables the bandpass filter on the specified channel. For the NI
PXIe-5622, set the value to TRUE to enable the IF filtered path 50MHz
bandpass filter centered at 187MHz. The default value is FALSE.

**Related topics:**

`Bandwidth <digitizers.chm::/Analog_Bandwidth.html>`__
''',
},
    },
    1150319: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Vertical:Advanced:Dither Enabled',
        'name': 'DITHER_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables or disables the analog dither on the device. Using dither can
improve the spectral performance of the device by reducing the effects
of quantization. However, adding dither increases the power level to the
ADC, so you may need to either decrease the signal level or increase the
vertical range. The default value is FALSE.

**Related topics:**

`NI 5620/5621 Signal
Conditioning <digitizers.chm::/562x_Signal_Cond.html>`__
''',
},
    },
    1150320: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Onboard Signal Processing:Fractional Resample:Fractional Resample Enabled',
        'name': 'FRACTIONAL_RESAMPLE_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables the onboard signal processing block that resamples the input
waveform to the user desired sample rate. The default value is FALSE.
''',
'note': '''
This property can be used only with high-speed digitizers that support
onboard signal processing (OSP). NI-SCOPE returns an error if you use
this property with a device that does not support OSP.
''',
},
    },
    1150321: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Fetch:Advanced:Maximum Bandwidth',
        'name': 'DATA_TRANSFER_MAXIMUM_BANDWIDTH',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the maximum bandwidth that the device is allowed to consume.
The NI device limits itself to transfer fewer bytes per second on the
PCIe bus than the value you specify for this property.

**Related topics:**

`Bandwidth <digitizers.chm::/Analog_Bandwidth.html>`__
''',
},
    },
    1150322: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Fetch:Advanced:Preferred Packet Size',
        'name': 'DATA_TRANSFER_PREFERRED_PACKET_SIZE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the preferred size of the data field in the PCI Express
packet. In general, the larger the packet size, the more efficiently the
device uses the bus. However, some systems, because of their
implementation, perform better with smaller packet sizes. The value of
this property must be a power of two (64, 128, ... , 512).
''',
},
    },
    1150328: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Peer-to-Peer:Samples Available In Endpoint',
        'name': 'P2P_SAMPLES_AVAIL_IN_ENDPOINT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the current number of samples available to stream from a
peer-to-peer endpoint. This property is endpoint-based.
''',
'note': '''
This property can be used only with high-speed digitizers that support
peer-to-peer streaming.
''',
},
    },
    1150329: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Peer-to-Peer:Manual:Configuration:Data Transfer Permission Address',
        'name': 'P2P_DATA_TRANS_PERMISSION_ADDR',
        'resettable': 'No',
        'type': 'ViInt64',
'documentation': {
'description': '''
Returns the address of a hardware register used to grant permission for
the peer-to-peer endpoint to write data to another peer. The type of
this address is determined by the `Data Transfer Permission Address
Type <pniScope_P2PDataTransferPermissionAddressType.html>`__ property.
Permission is granted in bytes and the register is additive. This
property is endpoint-based.
''',
'note': '''
This property can be used only with high-speed digitizers that support
peer-to-peer streaming.
''',
},
    },
    1150330: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'AddressType',
        'lv_property': 'Peer-to-Peer:Manual:Configuration:Data Transfer Permission Address Type',
        'name': 'P2P_DATA_TRANS_PERMISSION_ADDR_TYPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the type of address returned to the user from the `Data
Transfer Permission
Address <pniScope_P2PDataTransferPermissionAddress.html>`__ property.
This property is endpoint-based.
''',
'note': '''
This property can be used only with high-speed digitizers that support
peer-to-peer streaming.
''',
},
    },
    1150331: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Peer-to-Peer:Manual:Configuration:Destination Window Address',
        'name': 'P2P_DESTINATION_WINDOW_ADDR',
        'resettable': 'No',
        'type': 'ViInt64',
'documentation': {
'description': '''
Specifies the destination for data written by the peer-to-peer endpoint.
The type of this address is specified by the `Destination Window Address
Type <pniScope_P2PDestinationWindowAddressType.html>`__ property. This
property is endpoint-based.

**Valid Values**

A valid, non-NULL, physical or virtual address.
''',
'note': '''
This property can be used only with high-speed digitizers that support
peer-to-peer streaming.
''',
},
    },
    1150332: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'AddressType',
        'lv_property': 'Peer-to-Peer:Manual:Configuration:Destination Window Address Type',
        'name': 'P2P_DESTINATION_WINDOW_ADDR_TYPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the type of the `Destination Window
Address <pniScope_P2PDestinationWindowAddress.html>`__ property. This
property is endpoint-based.
''',
'note': '''
This property can be used only with high-speed digitizers that support
peer-to-peer streaming.
''',
},
    },
    1150333: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Peer-to-Peer:Manual:Configuration:Destination Window Size',
        'name': 'P2P_DESTINATION_WINDOW_SIZE',
        'resettable': 'No',
        'type': 'ViInt64',
'documentation': {
'description': '''
Specifies the size, in bytes, of the destination window determined by
the `Destination Window
Address <pniScope_P2PDestinationWindowAddress.html>`__ and `Destination
Window Address Type <pniScope_P2PDestinationWindowAddressType.html>`__
properties. This property is endpoint-based.
''',
'note': '''
This property can be used only with high-speed digitizers that support
peer-to-peer streaming.
''',
},
    },
    1150334: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'NotificationType',
        'lv_property': 'Peer-to-Peer:Manual:Notification:Push Message On',
        'name': 'P2P_NOTIFY_PUSH_MESSAGE_ON',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the event to push the `Message Push
Value <pniScope_P2PMessagePushValue.html>`__ property to the `Message
Push Address <pniScope_P2PMessagePushAddress.html>`__ property.
Specifying Done will push the message when the acquisition has
completed. This property is endpoint-based.
''',
'note': '''
This property can be used only with high-speed digitizers that support
peer-to-peer streaming.
''',
},
    },
    1150335: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Peer-to-Peer:Manual:Notification:Message Push Address',
        'name': 'P2P_NOTIFY_MESSAGE_PUSH_ADDR',
        'resettable': 'No',
        'type': 'ViInt64',
'documentation': {
'description': '''
Specifies the address to push the `Message Push
Value <pniScope_P2PMessagePushValue.html>`__ to on the event specified
by the `Push Message On <pniScope_P2PPushMessageOn.html>`__ property.
This property is endpoint-based.
''',
'note': '''
This property can be used only with high-speed digitizers that support
peer-to-peer streaming.
''',
},
    },
    1150336: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'AddressType',
        'lv_property': 'Peer-to-Peer:Manual:Notification:Message Push Address Type',
        'name': 'P2P_NOTIFY_MESSAGE_PUSH_ADDR_TYPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the type of the `Message Push
Address <pniScope_P2PMessagePushAddress.html>`__ property. This property
is endpoint-based.
''',
'note': '''
This property can be used only with high-speed digitizers that support
peer-to-peer streaming.
''',
},
    },
    1150337: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Peer-to-Peer:Manual:Notification:Message Push Value',
        'name': 'P2P_NOTIFY_MESSAGE_PUSH_VALUE',
        'resettable': 'No',
        'type': 'ViInt64',
'documentation': {
'description': '''
Specifies the value to be pushed to the `Message Push
Address <pniScope_P2PMessagePushAddress.html>`__ property on the event
specified in the `Push Message On <pniScope_P2PPushMessageOn.html>`__
property. This property is endpoint-based.
''',
'note': '''
This property can be used only with high-speed digitizers that support
peer-to-peer streaming.
''',
},
    },
    1150338: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'BoolEnableDisable',
        'lv_property': 'Peer-to-Peer:P2P Enabled',
        'name': 'P2P_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the digitizer writes data to the peer-to-peer
endpoint. This property is endpoint-based.
''',
'note': '''
This property can be used only with high-speed digitizers that support
peer-to-peer streaming.
''',
},
    },
    1150339: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Peer-to-Peer:Channels to Stream',
        'name': 'P2P_CHANNELS_TO_STREAM',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies which channels will be written to a peer-to-peer endpoint. If
multiple channels are specified, they will be interleaved by sample.
This property is endpoint-based. The default value is 0.
''',
'note': '''
This property must either be unused or set to all enabled channels on NI
5160/5162 digitizers.
''',
},
    },
    1150340: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Peer-to-Peer:Samples Transferred',
        'name': 'P2P_SAMPLES_TRANSFERRED',
        'resettable': 'No',
        'type': 'ViInt64',
'documentation': {
'description': '''
Returns the number of samples transferred through the peer-to-peer
endpoint since the endpoint was last reset. This property is
endpoint-based.
''',
'note': '''
This property can be used only with high-speed digitizers that support
peer-to-peer streaming.
''',
},
    },
    1150341: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Peer-to-Peer:Most Samples Available in Endpoint',
        'name': 'P2P_MOST_SAMPLES_AVAIL_IN_ENDPOINT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the most number of samples available to stream from a
peer-to-peer endpoint since the last time this property was read. This
property is endpoint-based.
''',
'note': '''
This property can be used only with high-speed digitizers that support
peer-to-peer streaming.
''',
},
    },
    1150342: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Peer-to-Peer:Endpoint Size',
        'name': 'P2P_ENDPOINT_SIZE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the size, in samples, of the peer-to-peer endpoint. This
property is endpoint-based.
''',
'note': '''
This property can be used only with high-speed digitizers that support
peer-to-peer streaming.
''',
},
    },
    1150343: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'BoolEnableDisable',
        'lv_property': 'Peer-to-Peer:Manual:Manual Configuration Enabled',
        'name': 'P2P_MANUAL_CONFIGURATION_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables and disables manual configuration of a peer-to-peer endpoint.
These attributes cannot be used if an endpoint is being configured by
NI-P2P, or a resource reservation error will result. This property is
endpoint-based.
''',
'note': '''
This property can be used only with high-speed digitizers that support
peer-to-peer streaming.
''',
},
    },
    1150344: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Peer-to-Peer:Endpoint Overflow',
        'name': 'P2P_ENDPOINT_OVERFLOW',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Returns TRUE if the peer-to-peer endpoint has overflowed. Reset the
endpoint to clear the overflow condition. This property is
endpoint-based.
''',
'note': '''
This property can be used only with high-speed digitizers that support
peer-to-peer streaming.
''',
},
    },
    1150345: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Peer-to-Peer:FIFO Endpoint Count',
        'name': 'P2P_FIFO_ENDPOINT_COUNT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the number of FIFO-based peer-to-peer endpoints this device
supports.
''',
'note': '''
This property can be used only with high-speed digitizers that support
peer-to-peer streaming.
''',
},
    },
    1150354: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'BoolEnableDisable',
        'lv_property': 'Peer-to-Peer:Onboard Memory Enabled',
        'name': 'P2P_ONBOARD_MEMORY_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Specifies whether the digitizer writes data to onboard memory when a
peer-to-peer endpoint is enabled.
''',
'note': 'This property is not supported on NI 5160/5162 digitizers.',
},
    },
    1150366: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggering:End of Record to Advance Trigger Holdoff',
        'name': 'END_OF_RECORD_TO_ADVANCE_TRIGGER_HOLDOFF',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
End of Record to Advance Trigger Holdoff is the length of time (in
seconds) that a device waits between the completion of one record and
the acquisition of pre-trigger samples for the next record. During this
time, the acquisition engine state delays the transition to the Wait for
Advance Trigger state, and will not store samples in onboard memory,
accept an Advance Trigger, or trigger on the input signal..

**Supported Devices**: NI 5185/5186
''',
},
    },
    1150367: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocking:Sample Clock Timebase Multiplier',
        'name': 'SAMP_CLK_TIMEBASE_MULT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
If `Sample Clock Timebase
Source <pniScope_SampleClockTimebaseSource.html>`__ is an external
source, this property specifies the ratio between the `Sample Clock
Timebase Rate <pniScope_SampleClockTimebaseRate.html>`__ and the actual
sample rate, which can be higher. This property can be used in
conjunction with the `Sample Clock Timebase Divisor
Property <pniscope_SampleClockTimebaseDivisor.html>`__.

Some devices use multiple ADCs to sample the same channel at an
effective sample rate that is greater than the specified clock rate.
When providing an external sample clock use this property to indicate
when you want a higher sample rate. Valid values for this property vary
by device and current configuration.

**Related topics:**

`Sample Clock <digitizers.chm::/Sample_Clock.html>`__
''',
},
    },
    1150373: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'StreamingPositionType',
        'lv_property': 'Peer-to-Peer:Stream Relative To',
        'name': 'P2P_STREAM_RELATIVE_TO',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Determines which trigger peer-to-peer data is streamed relative to. The
default value is **Start Trigger**.
''',
'note': 'On the NI 5122/5622, only **Start Trigger** is valid for this property.',
},
    },
    1150374: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocking:Advanced:Absolute Sample Clock Offset',
        'name': 'ABSOLUTE_SAMPLE_CLOCK_OFFSET',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Gets or sets the absolute time offset of the sample clock relative to
the reference clock in terms of seconds.
''',
'note': '''
Configures the sample clock relationship with respect to the reference
clock. This parameter is factored into NI-TClk adjustments and is
typically used to improve the repeatability of NI-TClk Synchronization.
When this parameter is read, the currently programmed value is returned.
The range of the absolute sample clock offset is [-.5 sample clock
periods, .5 sample clock periods]. The default absolute sample clock
offset is 0s.
''',
},
    },
    1150375: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Device:FPGA Bitfile Path',
        'name': 'FPGA_BITFILE_PATH',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': 'Gets the absolute file path to the bitfile loaded on the FPGA.',
'note': 'Gets the absolute file path to the bitfile loaded on the FPGA.',
},
    },
    1150376: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Vertical:Advanced:Interleaving Offset Correction Enabled',
        'name': 'INTERLEAVING_OFFSET_CORRECTION_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables the interleaving offset correction on the specified channel. The
default value is TRUE.

**Related topics:**

`Timed Interleaved
Sampling <digitizers.chm::/TimeInterleavedSampling.html>`__
''',
'note': 'If disabled, warranted specifications are not guaranteed.',
},
    },
    1150377: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Vertical:Advanced:High Pass Filter Frequency',
        'name': 'HIGH_PASS_FILTER_FREQUENCY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the frequency for the highpass filter in Hz. The device uses
one of the valid values listed below. If an invalid value is specified,
no coercion occurs. The default value is 0.

**(PXIe-5164) Valid Values:**

0 90 450

**Related topics:**

`Digital Filtering <digitizers.chm::/Digital_Filtering_Overview.html>`__
''',
},
    },
    1150380: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Peer-to-Peer:Samples Transferred Per Record',
        'name': 'P2P_SAMPLES_TRANSFERRED_PER_RECORD',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the number of samples transferred per record when you set the
`Stream Relative To <pniScope_P2PStreamRelativeTo.html>`__ property to
**Reference Trigger** or **Sync Trigger**.
''',
'note': 'This property is only supported on NI 5160/5162 digitizers.',
},
    },
    1151000: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Carrier Mixer:NCO Center Frequency',
        'name': 'CARRIER_NCO_CENTER_FREQUENCY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Controls the frequency of the timing NCO. The default value is
0X8000000.

Specifies the timing NCO center frequency in binary format as follows:

N = ( *:sub:`out`* / *F\ :sub:`resampler`* ) & 2\ :sup:`32`

where *F\ :sub:`out`* is the output frequency and *F\ :sub:`resampler`*
is the resampled frequency.

The value is transferred to the active register during the next initiate
acquisition operation.
''',
},
    },
    1151001: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Carrier Mixer:Phase Offset',
        'name': 'CARRIER_PHASE_OFFSET',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Offsets the phase of the timing NCO in binary format. The value is
transferred to the active register during the next initiate acquisition.
The default value is 0.

Valid Range: 0 to 6.283185307179586476925286766558
''',
},
    },
    1151002: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Mux Mode',
        'name': 'MUX_MODE_REGISTER',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '',
},
    },
    1151003: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Enable DDC',
        'name': 'ENABLE_DDC',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Disables programming the DDC when set to FALSE. The default value is
TRUE.

This property is supported for NI 5620/5621 digitizers only. For NI
5142/5622 digitizers, use the `DDC Enabled <pniScope_DDCEnabled.html>`__
property.

Custom programming of the DDC using NI-SCOPE property nodes is not
supported by National Instruments.

National Instruments supports using the DDC only when the Modulation
Toolkit and/or Spectral Measurements Toolkit are used, because they make
use of the DDC automatically (that is, without user intervention) when
configuration settings allow.
''',
},
    },
    1151010: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):CIC Filter:Decimation',
        'name': 'CIC_DECIMATION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Controls the decimation in the CIC filter. The CIC filter reduces the
sample rate of a wideband signal to a rate that other filters in the DDC
can process. The default value is 4.

Valid Range: 4 to 32
''',
},
    },
    1151011: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):CIC Filter:Shift Gain',
        'name': 'CIC_SHIFT_GAIN',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Controls the shift gain at the input to the CIC filter. The CIC filter
reduces the sample rate of a wideband signal to a rate that other
filters in the DDC can process. The default value is 0.

Valid Range: 0 to 15
''',
},
    },
    1151020: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:Enable',
        'name': 'DISCR._ENABLE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables or disables the discriminator. If set to TRUE, frequency
discriminator is enabled. The default value is FALSE.
''',
},
    },
    1151021: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:FIR Decimation',
        'name': 'DISCRIMINATOR_FIR_DECIMATION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Sets the amount of decimation. The default value is 1.

Valid Range: 1 to 8
''',
},
    },
    1151022: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'DiscriminatorFIRSymmetry',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:FIR Symmetry',
        'name': 'DISCRIMINATOR_FIR_SYMMETRY',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Sets the discriminator FIR symmetry to symmetric or asymmetric. The
default value is Symmetric.
''',
},
    },
    1151023: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'DiscriminatorFIRSymmetryType',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:FIR Symmetry Type',
        'name': 'DISCRIMINATOR_FIR_SYMMETRY_TYPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Sets the discriminator FIR symmetry type to even or odd. The default
value is even.
''',
},
    },
    1151024: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:FIR Taps',
        'name': 'DISCRIMINATOR_FIR_TAPS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Sets the discriminator FIR number of taps. The default value is 1.

Valid Range: 1 to 63
''',
},
    },
    1151025: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:Delay',
        'name': 'DISCRIMINATOR_DELAY',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Sets the number of delays in the discriminator. The default value is 1.

Valid Range: 1 to 8
''',
},
    },
    1151026: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'DiscriminatorFIRInputSource',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:FIR Input Source',
        'name': 'DISCRIMINATOR_FIR_INPUT_SOURCE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Sets the discriminator FIR input source to Phase, Magnitude, or
Resampler. The default value is Phase.
''',
},
    },
    1151027: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:Phase Multiplier',
        'name': 'DISCRIMINATOR_PHASE_MULTIPLIER',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Programs the coordinate converter to multiply the phase output by 1, 2,
4, or 8. Multiplying the phase output removes phase modulation before
the frequency is measured. The default value is 0.
''',
},
    },
    1151030: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Programmable FIR Filter:Decimation',
        'name': 'PROG._FIR_FILTER_DECIMATION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the programmable FIR filter decimation. The default value is
1.
''',
},
    },
    1151031: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'ProgFIRFilterSymmetry',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Programmable FIR Filter:Symmetry',
        'name': 'PROG._FIR_FILTER_SYMMETRY',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Sets either a Symmetric or Asymmetric filter. The default value is
Symmetric.
''',
},
    },
    1151032: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'ProgFIRFilterSymmetryType',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Programmable FIR Filter:Symmetry Type',
        'name': 'PROG._FIR_FILTER_SYMMETRY_TYPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Sets either even or odd symmetry. The default value is Even.',
},
    },
    1151033: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Programmable FIR Filter:Taps',
        'name': 'PROG._FIR_FILTER_TAPS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Defines the number of taps (in other words, coefficients) for a FIR
filter. The default value is 25.
''',
},
    },
    1151034: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'ProgFIRFilterRealComplex',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Programmable FIR Filter:Real/Complex',
        'name': 'PROG._FIR_FILTER_REALCOMPLEX',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Sets either a Complex filter or a dual Real filter. The default value is
Real.
''',
},
    },
    1151040: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):AGC:Upper Gain Limit',
        'name': 'AGC_UPPER_GAIN_LIMIT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Sets the maximum gain and minimum signal levels in the
`AGC <Digitizers.chm::/Glossary.html#AGC>`__. The default value is
6.020600.
''',
},
    },
    1151041: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):AGC:Lower Gain Limit',
        'name': 'AGC_LOWER_GAIN_LIMIT',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Sets the minimum gain and maximum signal levels in the
`AGC <Digitizers.chm::/Glossary.html#AGC>`__. The default value is
6.020600.
''',
},
    },
    1151042: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):AGC:Loop Gain 0 Exponent',
        'name': 'AGC_LOOP_GAIN_0_EXPONENT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Along with the `AGC Loop Gain 0
Mantissa <pniScope_AGCLoopGain0Mantissa.html>`__ property, sets the loop
gain for the `AGC <Digitizers.chm::/Glossary.html#AGC>`__. The default
value is 0.
''',
},
    },
    1151043: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):AGC:Loop Gain 0 Mantissa',
        'name': 'AGC_LOOP_GAIN_0_MANTISSA',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Along with the `AGC Loop Gain 0
Exponent <pniScope_AGCLoopGain0Exponent.html>`__ property, sets the loop
gain for the `AGC <Digitizers.chm::/Glossary.html#AGC>`__. The default
value is 0.
''',
},
    },
    1151044: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):AGC:Loop Gain 1 Exponent',
        'name': 'AGC_LOOP_GAIN_1_EXPONENT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Along with `AGC Loop Gain 1
Mantissa <pniScope_AGCLoopGain1Mantissa.html>`__ property, sets the loop
gain for the `AGC <Digitizers.chm::/Glossary.html#AGC>`__. The default
value is 0.
''',
},
    },
    1151045: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):AGC:Loop Gain 1 Mantissa',
        'name': 'AGC_LOOP_GAIN_1_MANTISSA',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Along with `AGC Loop Gain 1
Exponent <pniScope_AGCLoopGain1Exponent.html>`__ property, sets the loop
gain for the `AGC <Digitizers.chm::/Glossary.html#AGC>`__. The default
value is 0.
''',
},
    },
    1151046: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):AGC:Threshold',
        'name': 'AGC_THRESHOLD',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Sets the gain error in the `AGC <Digitizers.chm::/Glossary.html#AGC>`__.
The default value is 0x034D.
''',
},
    },
    1151047: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'AGCAverageControl',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):AGC:Average Control',
        'name': 'AGC_AVERAGE_CONTROL',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Averages the `AGC <Digitizers.chm::/Glossary.html#AGC>`__ values. The
default value is Mean.
''',
},
    },
    1151050: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):HalfBand Filter:Bypass',
        'name': 'HALFBAND_FILTER_BYPASS',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables or bypasses the halfband filters. If set to TRUE, halfband
filters are bypassed. The default is TRUE.
''',
},
    },
    1151051: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):HalfBand Filter:Filter 1 Enable',
        'name': 'HALFBAND_FILTER_1_ENABLE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables halfband filter 1. If TRUE, filter is enabled. The default is
TRUE.
''',
},
    },
    1151052: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):HalfBand Filter:Filter 2 Enable',
        'name': 'HALFBAND_FILTER_2_ENABLE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables halfband filter 2. If TRUE, filter is enabled. The default is
FALSE.
''',
},
    },
    1151053: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):HalfBand Filter:Filter 3 Enable',
        'name': 'HALFBAND_FILTER_3_ENABLE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables halfband filter 3. If TRUE, filter is enabled. The default is
FALSE.
''',
},
    },
    1151054: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):HalfBand Filter:Filter 4 Enable',
        'name': 'HALFBAND_FILTER_4_ENABLE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables halfband filter 4. If TRUE, filter is enabled. The default is
FALSE.
''',
},
    },
    1151055: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):HalfBand Filter:Filter 5 Enable',
        'name': 'HALFBAND_FILTER_5_ENABLE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables halfband filter 5. If TRUE, filter is enabled. The default is
FALSE.
''',
},
    },
    1151070: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'AOUTParallelOutputSource',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Output Configuration:Parallel:AOUT Source',
        'name': 'AOUT_PARALLEL_OUTPUT_SOURCE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the source for the AOUT parallel output from the
`DDC <Digitizers.chm::/Glossary.html#DDC>`__. The default is I Data.
''',
},
    },
    1151071: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'BOUTParallelOutputSource',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Output Configuration:Parallel:BOUT Source',
        'name': 'BOUT_PARALLEL_OUTPUT_SOURCE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the source for the BOUT parallel output from the
`DDC <Digitizers.chm::/Glossary.html#DDC>`__. The default is Q Data.
''',
},
    },
    1151072: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Test Mode Sin/Cos',
        'name': 'TEST_MODE_SINCOS',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Enables the special test mode where the carrier NCO outputs are set to
0x7FFF. The default is FALSE.
''',
},
    },
    1151073: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'CoordinateConverterInput',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Coordinate Converter Input',
        'name': 'COORDINATE_CONVERTER_INPUT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Selects the source for the input to the coordinate converter, either the
HB filter or the Programmable FIR. the default value is Programmable
FIR.
''',
},
    },
    1151074: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'QInputtoCoordConverter',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Q Input to Coord. Converter',
        'name': 'Q_INPUT_TO_COORD._CONVERTER',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Either enables or zeros out the Q input to coordinate converter. The
default value is I and Q.
''',
},
    },
    1151080: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'SyncoutCLKSelect',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Syncout CLK Select',
        'name': 'SYNCOUT_CLK_SELECT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Source for Syncout CLK. The default value is CLK IN.',
},
    },
    1151120: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Timing NCO:Phase Accum. Load on Update',
        'name': 'TIMING_NCO_PHASE_ACCUM._LOAD_ON_UPDATE',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
When TRUE, updates the `timing
NCO <Digitizers.chm::/Glossary.html#timingNCO>`__ frequency to zero the
feedback of the phase accumulator as well as update the phase and
frequency. The default value is TRUE.
''',
},
    },
    1151121: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Timing NCO:Clear Phase Accum.',
        'name': 'TIMING_NCO_CLEAR_PHASE_ACCUM.',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
If FALSE, enables the accumulator in the `timing
NCO <Digitizers.chm::/Glossary.html#timingNCO>`__. If TRUE, zeros out
feedback in the accumulator. The default value is FALSE.
''',
},
    },
    1151122: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Timing NCO:Enable Offset Freq.',
        'name': 'TIMING_NCO_ENABLE_OFFSET_FREQ.',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
If TRUE, enables offset frequency in the `timing
NCO <Digitizers.chm::/Glossary.html#timingNCO>`__. If FALSE, applies no
offset frequency. The default value is FALSE.
''',
},
    },
    1151123: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'TimingNCOFreqOffsetBits',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Timing NCO:Frequency Offset Bits',
        'name': 'TIMING_NCO_FREQ._OFFSET_BITS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the number of offset bits in the `timing
NCO <Digitizers.chm::/Glossary.html#timingNCO>`__. The default value is
8 bits.
''',
},
    },
    1151124: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Timing NCO:Center Frequency',
        'name': 'TIMING_NCO_CENTER_FREQ.',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Controls the frequency of the timing NCO. Specifies the timing NCO
center frequency in binary format:

*N = (F:sub:`out` / F\ :sub:`resampler`) & 2\ :sup:`32`*

where *F\ :sub:`out`* is the output frequency and *F\ :sub:`resampler`*
is the resampled frequency.

The value is transferred to the active register during the next initiate
acquisition operation. The default value is 0X8000000.
''',
},
    },
    1151125: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Timing NCO:Phase Offset',
        'name': 'TIMING_NCO_PHASE_OFFSET',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Offsets the phase of the `timing
NCO <Digitizers.chm::/Glossary.html#timingNCO>`__ in binary format. The
value is transferred to the active register during the next initiate
acquisition. The default value is 0.

Valid Range: 0 to 6.283185307179586476925286766558
''',
},
    },
    1151126: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'ResamplerFilterMode',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Resampler:Filter Mode',
        'name': 'RESAMPLER_FILTER_MODE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Selects the resampling filter mode.',
},
    },
    1151127: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Resampler:Bypass',
        'name': 'RESAMPLER_BYPASS',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Either enables or bypasses the resampler filter in the DDC. The
resampler is a polyphase filter that allows the output sample rate to
have a non-integer relationship to the input sample rate. In essence, it
acts as a fixed interpolation filter followed by an NCO controlled
decimator. The default value is TRUE.
''',
},
    },
    1151128: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Resampler:Output Pulse Delay',
        'name': 'RESAMPLER_OUTPUT_PULSE_DELAY',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Programs the delay between output samples when interpolating. These
outputs can be delayed from 2 to 255 clocks. The default value is 16.
''',
},
    },
    1151129: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Resampler:NCO Divide',
        'name': 'RESAMPLER_NCO_DIVIDE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Divides down the
`resampler <Digitizers.chm::/Glossary.html#resampler>`__ NCO output by
the value loaded into the register plus one. The default value is 2.
''',
},
    },
    1151130: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Resampler:Reference Divide',
        'name': 'RESAMPLER_REFERENCE_DIVIDE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Divides down the reference clock by the value loaded into the register
plus one. Load with a value that is one less than the desired period.
The default value is 2.

**Related topics:**

`Reference Clock/Phase-Lock
Loop <digitizers.chm::/Reference_Clock.html>`__
''',
},
    },
    1151300: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Enable Dither',
        'name': 'ENABLE_DITHER',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
Applies dither at the input of the ADC. Set this property to TRUE to
enable dither. The default value is FALSE.
''',
},
    },
    1151301: {
        'access': 'read only',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Combined Decimation',
        'name': 'COMBINED_DECIMATION',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the combined `DDC <Digitizers.chm::/Glossary.html#DDC>`__
decimation.
''',
},
    },
    1151302: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Serial DAC Cal Voltage',
        'name': 'SERIAL_DAC_CAL_VOLTAGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '',
},
    },
    1151303: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Clocking:PLL Lock Status',
        'name': 'PLL_LOCK_STATUS',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': '''
If TRUE, the PLL has remained locked to the external reference clock
since it was last checked. If FALSE, the PLL has become unlocked from
the external reference clock since it was last checked.
''',
},
    },
    1151304: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Acquisition:Delay before Initiate',
        'name': 'DELAY_BEFORE_INITIATE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies a delay in seconds that is used by `niScope\_Initiate
Acquisition <scopeviref.chm::/niScope_Initiate_Acquisition.html>`__ to
allow additional delay between programming of the vertical range,
trigger level, DDC, and the start of the acquisition. This property is
supported only on the NI 5112 and the NI 5620/5621. The default value is
0.0.
''',
},
    },
    1151305: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:DDC Direct Register Address',
        'name': 'DDC_DIRECT_REGISTER_ADDRESS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Used for directly accessing the
`DDC <Digitizers.chm::/Glossary.html#DDC>`__ registers.
''',
},
    },
    1151306: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:DDC Direct Register Data',
        'name': 'DDC_DIRECT_REGISTER_DATA',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Used for directly accessing the
`DDC <Digitizers.chm::/Glossary.html#DDC>`__ registers. The default
value is 0.
''',
},
    },
    1250001: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Vertical:Vertical Range',
        'name': 'VERTICAL_RANGE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the absolute value of the input range for a channel. The units
are volts. For example, to acquire a sine wave that spans between -5 and
+5 V, set this property to 10.0 V.
''',
},
    },
    1250002: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Vertical:Vertical Offset',
        'name': 'VERTICAL_OFFSET',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the location of the center of the range. The value is with
respect to ground and is in volts. For example, to acquire a sine wave
that spans between 0.0 and 10.0 V, set this property to 5.0 V. This
property is not supported by all digitizers.
''',
},
    },
    1250003: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'VerticalCoupling',
        'lv_property': 'Vertical:Vertical Coupling',
        'name': 'VERTICAL_COUPLING',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies how the digitizer couples the input signal for the channel.
When you change input coupling, the input stage takes a finite amount of
time to settle.

**Related topics:**

`Input Coupling <digitizers.chm::/Input_Coupling.html>`__
''',
},
    },
    1250004: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Vertical:Probe Attenuation',
        'name': 'PROBE_ATTENUATION',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the probe attenuation for the input channel. For example, for
a 10:1 probe, you would set this property to 10.0.

**Related topics:**

`Probes and Their Effects <digitizers.chm::/Probes.html>`__
''',
},
    },
    1250005: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'BoolEnableDisableChan',
        'lv_property': 'Vertical:Channel Enabled',
        'name': 'CHANNEL_ENABLED',
        'resettable': 'No',
        'type': 'ViBoolean',
'documentation': {
'description': 'Specifies whether the digitizer acquires a waveform for the channel.',
},
    },
    1250006: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Vertical:Maximum Input Frequency',
        'name': 'MAX_INPUT_FREQUENCY',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the bandwidth of the channel in hertz. Express this value as
the frequency at which the input circuitry attenuates the input signal
by 3 dB.

Special Values:

(-1) Full bandwidth

(0) Device default

**Related topics:**

`Bandwidth <digitizers.chm::/Analog_Bandwidth.html>`__ `Probes and Their
Effects <digitizers.chm::/Probes.html>`__
''',
},
    },
    1250007: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Horizontal:Advanced:Time Per Record',
        'name': 'HORZ_TIME_PER_RECORD',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the length of time (in seconds) that corresponds to the record
length. This attribute is invalid when the device is configured to use
an external sample clock timebase. This attribute is also invalid when a
DDC is enabled. When both the Time Per Record Property and the `Min
Sample Rate <pniScope_MinSampleRate.html>`__ Property are set, the
attribute that was set first is ignored.

**Related topics:**

`Record Length <digitizers.chm::/Record_Length.html>`__ `Sample
Rate <digitizers.chm::/Sample_Rate.html>`__
''',
},
    },
    1250008: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Horizontal:Actual Record Length',
        'name': 'HORZ_RECORD_LENGTH',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the actual number of points the digitizer acquires for each
channel. The value is equal to or greater than the value you specify in
the `niScope Configure Horizontal
Timing <scopeviref.chm::/niScope_Configure_Horizontal_Timing.html>`__
VI.

Valid Values: 1 to the maximum memory size

`Record Length <digitizers.chm::/Record_Length.html>`__ `Coercions of
Horizontal Parameters <digitizers.chm::/Horizontal_Parameters.html>`__
''',
},
    },
    1250009: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Horizontal:Min Number of Points',
        'name': 'HORZ_MIN_NUM_PTS',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the minimum number of points you require in the waveform
record for each channel.

NI-SCOPE uses the value you specify to configure the record length that
the digitizer uses for waveform acquisition. The `Actual Record
Length <pniScope_ActualRecordLength.html>`__ property returns the actual
record length.

**Related topics:**

`Record Length <digitizers.chm::/Record_Length.html>`__ `Sample
Rate <digitizers.chm::/Sample_Rate.html>`__
''',
},
    },
    1250010: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Horizontal:Actual Sample Rate',
        'name': 'HORZ_SAMPLE_RATE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Returns the actual sample rate used for the acquisition.

Units: hertz (Samples / Second)

**Related topics:**

`Sample Clock <digitizers.chm::/Sample_Clock.html>`__
''',
},
    },
    1250011: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Horizontal:Reference Position',
        'name': 'HORZ_RECORD_REF_POSITION',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the position of the Reference Event in the waveform record as
a percentage of the record.

When the digitizer detects a trigger, it waits the length of time the
`Trigger Delay <pniScope_TriggerDelay.html>`__ property specifies. The
event that occurs when the delay time elapses is the Reference Event.
The Reference Event is relative to the start of the record and is a
percentage of the record length. For example, the value 50.0 corresponds
to the center of the waveform record and 0.0 corresponds to the first
element in the waveform record.
''',
},
    },
    1250012: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TriggerType',
        'lv_property': 'Triggering:Trigger Type',
        'name': 'TRIGGER_TYPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the type of trigger to use.',
},
    },
    1250013: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggering:Trigger Source',
        'name': 'TRIGGER_SOURCE',
        'resettable': 'No',
        'type': 'ViString',
'documentation': {
'description': '''
Specifies the source the digitizer monitors for the trigger event. The
value must be selected from one of the following valid values.
''',
'table_body': [['0..\\ *n*', '*n* is the number of channels on the device'], ['VAL\\_EXTERNAL', 'External TRIG input'], ['VAL\\_IMMEDIATE', 'Triggers immediately'], ['VAL\\_RTSI\\_0', 'RTSI 0'], ['VAL\\_RTSI\\_1', 'RTSI 1'], ['VAL\\_RTSI\\_2', 'RTSI 2'], ['VAL\\_RTSI\\_3', 'RTSI 3'], ['VAL\\_RTSI\\_4', 'RTSI 4'], ['VAL\\_RTSI\\_5', 'RTSI 5'], ['VAL\\_RTSI\\_6', 'RTSI 6'], ['VAL\\_PFI\\_0', 'PFI 0'], ['VAL\\_PFI\\_1', 'PFI 1'], ['VAL\\_PFI\\_2', 'PFI 2'], ['VAL\\_PXI\\_STAR', 'PXI Star trigger'], ['VAL\\_SW\\_TRIG\\_FUNC', 'Waits for niScope Send Software Trigger Edge']],
},
    },
    1250014: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TriggerCoupling',
        'lv_property': 'Triggering:Trigger Coupling',
        'name': 'TRIGGER_COUPLING',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies how the digitizer couples the trigger source.

This property affects instrument operation only when the `Trigger
Type <pniScope_TriggerType.html>`__ property is set to Edge, Hysteresis,
Window, or Video. If the trigger source is an input channel, the
coupling of that channel is used for the trigger.
''',
},
    },
    1250015: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggering:Trigger Delay',
        'name': 'TRIGGER_DELAY_TIME',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the trigger delay time in seconds.

The trigger delay time is the length of time the digitizer waits after
it receives the trigger. The event that occurs when the trigger delay
elapses is the Reference Event.
''',
},
    },
    1250016: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggering:Trigger Holdoff',
        'name': 'TRIGGER_HOLDOFF',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the length of time the digitizer waits after detecting a
trigger before enabling the trigger subsystem to detect another trigger.
The units are seconds.

This property affects instrument operation only when the digitizer
requires multiple acquisitions to build a complete waveform. The
digitizer requires multiple waveform acquisitions when it uses
equivalent-time sampling or when the digitizer is configured for a
multirecord acquisition through a call to `niScope Configure Horizontal
Timing <scopeviref.chm::/niScope_Configure_Horizontal_Timing.html>`__.
''',
},
    },
    1250017: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggering:Trigger Level',
        'name': 'TRIGGER_LEVEL',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the voltage threshold for the trigger. The units are volts.

This property affects instrument behavior only when the `Trigger
Type <pniScope_TriggerType.html>`__ is set to Edge, Hysteresis, or
Window.

The values of the **range** and **offset** parameters in `niScope
Configure Vertical <scopeviref.chm::/niScope_Configure_Vertical.html>`__
determine the valid range for the trigger level on the channel you use
as the **trigger source**. The value you pass for this parameter must
meet the following conditions:

*Trigger Level <= Vertical Range/2 + Vertical Offset*

*Trigger Level >= (-Vertical Range/2) + Vertical Offset*
''',
},
    },
    1250018: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TriggerSlope',
        'lv_property': 'Triggering:Trigger Slope',
        'name': 'TRIGGER_SLOPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies whether a rising or a falling edge triggers the digitizer.

This property affects instrument operation only when the `Trigger
Type <pniScope_TriggerType.html>`__ property is set to edge, hysteresis,
window, or video.
''',
},
    },
    1250101: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'AcquisitionType',
        'lv_property': 'Acquisition:Acquisition Type',
        'name': 'ACQUISITION_TYPE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies how the digitizer acquires data and fills the waveform record.',
'note': '''
Acquisition type DDC applies to the NI 5620/5621 only. To use DDC mode
in the NI 5142 and NI 5622, leave acquisition type set to Normal and set
`DDC Enabled <pniScope_DDCEnabled.html>`__ to TRUE.
''',
},
    },
    1250102: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TriggerModifier',
        'lv_property': 'Triggering:Trigger Modifier',
        'name': 'TRIGGER_MODIFIER',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Configures the device to automatically complete an acquisition if a
trigger has not been received.
''',
},
    },
    1250103: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': None,
        'lv_property': 'Vertical:Input Impedance',
        'name': 'INPUT_IMPEDANCE',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the input impedance for the channel in ohms.

**Defined Values**

50 Ohm

1 M Ohm

**Related topics:**

`Impedance and Impedance
Matching <digitizers.chm::/Impedance_and_Impedance_Matching.html>`__
''',
},
    },
    1250106: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Acquisition:Sample Mode',
        'name': 'SAMPLE_MODE',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Returns the sample mode the digitizer is currently using.

**Defined Values**

Real Time (0)

Equivalent Time (1)
''',
},
    },
    1250109: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Horizontal:Advanced:Acquisition Start Time',
        'name': 'ACQUISITION_START_TIME',
        'resettable': 'No',
        'type': 'ViReal64',
'documentation': {
'description': '''
Specifies the length of time (in seconds) from the trigger event to the
first point in the waveform record.

If the value is positive, the first point in the waveform record occurs
after the trigger event (same as specifying a trigger delay). If the
value is negative, the first point in the waveform record occurs before
the trigger event (same as specifying Reference Position).
''',
},
    },
    1250201: {
        'access': 'read-write',
        'channel_based': 'True',
        'enum': 'VideoSignalFormat',
        'lv_property': 'Triggering:Trigger Video:Signal Format',
        'name': 'TV_TRIGGER_SIGNAL_FORMAT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the video signal format to use.',
},
    },
    1250204: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'VideoPolarity',
        'lv_property': 'Triggering:Trigger Video:Polarity',
        'name': 'TV_TRIGGER_POLARITY',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies whether the video signal is positive or negative.',
},
    },
    1250205: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'VideoTriggerEvent',
        'lv_property': 'Triggering:Trigger Video:Event',
        'name': 'TV_TRIGGER_EVENT',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': 'Specifies the event to trigger on.',
},
    },
    1250206: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Triggering:Trigger Video:Line Number',
        'name': 'TV_TRIGGER_LINE_NUMBER',
        'resettable': 'No',
        'type': 'ViInt32',
'documentation': {
'description': '''
Specifies the line number to trigger on.

This property is only used if the video trigger
`Event <pniScope_VideoTriggerEvent.html>`__ property is set as Line
Number. Valid values depend on the video signal format selected.
''',
},
    },
}
