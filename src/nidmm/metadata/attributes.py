# -*- coding: utf-8 -*-
attributes = {
    1050002: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:User Options:Range Check',
        'name': 'RANGE_CHECK',
        'resettable': 'No',
        'short_description': '''
Specifies whether to validate property values and VI parameters. If
enabled, the instrument driver validates the parameter values passed to
driver VIs. Range checking parameters is very useful for debugging.
After the user program is validated, you can set this property to FALSE
(0) to disable range checking and maximize performance. The default
value is TRUE (1). Use niDMM Initialize With Options to override the
default setting.
''',
        'type': 'ViBoolean',
    },
    1050003: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:User Options:Query Instrument Status
''',
        'name': 'QUERY_INSTRUMENT_STATUS',
        'resettable': 'No',
        'short_description': '''
Specifies whether the instrument driver queries the instrument status
after each operation. Querying the instrument status is very useful for
debugging. After the user program is validated, this property can be set
to FALSE (0) to disable status checking and maximize performance. The
instrument driver can choose to ignore status checking for particular
properties regardless of the setting of this property. The default value
is TRUE (1). Use niDMM Initialize With Options to override the default
setting.
''',
        'type': 'ViBoolean',
    },
    1050004: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:User Options:Cache',
        'name': 'CACHE',
        'resettable': 'No',
        'short_description': '''
Specifies whether to cache the value of properties. When caching is
enabled, the instrument driver keeps track of the current instrument
settings and avoids sending redundant commands to the instrument. Thus,
it significantly increases execution speed. The instrument driver can
choose to always cache or to never cache particular properties
regardless of the setting of this property. The default value is TRUE
(1). Use niDMM Initialize With Options to override the default setting.
''',
        'type': 'ViBoolean',
    },
    1050005: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Specifies whether to simulate instrument driver I/O operations. If
simulation is enabled, instrument driver functions perform range
checking and call IVI Get and Set VIs, but they do not perform
instrument I/O. For output parameters that represent instrument data,
the instrument driver VIs return calculated values. The default value is
FALSE (0). Use niDMM Initialize With Options to override the default
setting.

.. note::
   Simulate can only be set within the niDMM Initialize With Options VI. The property value cannot be changed outside of the VI.
''',
        'lv_property': 'Inherent IVI Attributes:User Options:Simulate',
        'name': 'SIMULATE',
        'resettable': 'No',
        'short_description': '''
Specifies whether to simulate instrument driver I/O operations. If
simulation is enabled, instrument driver functions perform range
checking and call IVI Get and Set VIs, but they do not perform
instrument I/O. For output parameters that represent instrument data,
the instrument driver VIs return calculated values. The default value is
FALSE (0). Use niDMM Initialize With Options to override the default
setting.
''',
        'type': 'ViBoolean',
    },
    1050006: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:User Options:Record Value Coercions
''',
        'name': 'RECORD_VALUE_COERCIONS',
        'resettable': 'No',
        'short_description': '''
Specifies whether the IVI engine keeps a list of the value coercions it
makes for ViInt32 and ViReal64 properties. The default value is FALSE
(0). Use niDMM Initialize With Options to override the default setting.
Use niDMM Get Next Coercion Record to extract and delete the oldest
coercion record from the list.
''',
        'type': 'ViBoolean',
    },
    1050007: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Inherent IVI Attributes:User Options:Driver Setup',
        'name': 'DRIVER_SETUP',
        'resettable': 'No',
        'short_description': '''
This property indicates the Driver Setup string that the user specified
when initializing the driver. Some cases exist where the end-user must
specify instrument driver options at initialization time. An example of
this is specifying a particular instrument model from among a family of
instruments that the driver supports. This is useful when using
simulation. The end-user can specify driver-specific options through the
Driver Setup keyword in the Option String parameter in niDMM Initialize
With Options . If the user does not specify a Driver Setup string, this
property returns an empty string.
''',
        'type': 'ViString',
    },
    1050021: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Specifies whether to perform interchangeability checking and log
interchangeability warnings when you call niDMM VIs. Interchangeability
warnings indicate that using your application with a different
instrument might cause different behavior. Use niDMM Get Next
Interchange Warning to extract interchange warnings. Use niDMM Clear
Interchange Warnings to clear the list of interchangeability warnings
without reading them. Interchangeability checking examines the
properties in a capability group only if you specify a value for at
least one property within that group. Interchangeability warnings can
occur when a property affects the behavior of the instrument and you
have not set that property, or the property has been invalidated since
you set it.

+---------+-----+
| TRUE    | 1   |
+---------+-----+
| FALSE   | 0   |
+---------+-----+
''',
        'lv_property': '''
Inherent IVI Attributes:User Options:Interchange Check
''',
        'name': 'INTERCHANGE_CHECK',
        'resettable': 'No',
        'short_description': '''
Specifies whether to perform interchangeability checking and log
interchangeability warnings when you call niDMM VIs. Interchangeability
warnings indicate that using your application with a different
instrument might cause different behavior. Use niDMM Get Next
Interchange Warning to extract interchange warnings. Use niDMM Clear
Interchange Warnings to clear the list of interchangeability warnings
without reading them. Interchangeability checking examines the
properties in a capability group only if you specify a value for at
least one property within that group. Interchangeability warnings can
occur when a property affects the behavior of the instrument and you
have not set that property, or the property has been invalidated since
you set it.
''',
        'type': 'ViBoolean',
    },
    1050101: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Obsolete:Inherent IVI Attributes:Error Info:Primary Error
''',
        'name': 'PRIMARY_ERROR',
        'resettable': 'No',
        'short_description': '''
A code that describes the first error that occurred since the last call
to niDMM Get Error for the session. The value follows the VXIplug&play
conventions. A negative value describes an error condition. A positive
value describes a warning condition. A zero indicates that no error or
warning occurred. The error and warning values can be status codes
defined by IVI, VISA, class drivers, or specific drivers.
''',
        'type': 'ViInt32',
    },
    1050102: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Obsolete:Inherent IVI Attributes:Error Info:Secondary Error
''',
        'name': 'SECONDARY_ERROR',
        'resettable': 'No',
        'short_description': '''
An optional code that provides additional information concerning the
primary error condition. The error and warning values can be status
codes defined by IVI, VISA, class drivers, or specific drivers. Zero
indicates no additional information.
''',
        'type': 'ViInt32',
    },
    1050103: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Obsolete:Inherent IVI Attributes:Error Info:Error Elaboration
''',
        'name': 'ERROR_ELABORATION',
        'resettable': 'No',
        'short_description': '''
An optional string that contains additional information concerning the
primary error condition.
''',
        'type': 'ViString',
    },
    1050203: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Instrument Capabilities:Channel Count
''',
        'name': 'CHANNEL_COUNT',
        'resettable': 'No',
        'short_description': '''
Indicates the number of channels that the specific instrument driver
supports. For each property for which the IVI\_VAL\_MULTI\_CHANNEL flag
property is set, the IVI engine maintains a separate cache value for
each channel.
''',
        'type': 'ViInt32',
    },
    1050302: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Instrument Capabilities:Specific Driver Prefix
''',
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'resettable': 'No',
        'short_description': '''
The prefix for the specific instrument driver. The name of each
user-callable VI in this driver starts with this prefix. The prefix can
be up to a maximum of eight characters.
''',
        'type': 'ViString',
    },
    1050304: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Advanced Session Information:I/O Resource Descriptor
''',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'resettable': 'No',
        'short_description': '''
A string containing the resource descriptor of the instrument.
''',
        'type': 'ViString',
    },
    1050305: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Advanced Session Information:Logical Name
''',
        'name': 'LOGICAL_NAME',
        'resettable': 'No',
        'short_description': '''
A string containing the logical name of the instrument.
''',
        'type': 'ViString',
    },
    1050327: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Specific Driver Capabilities:Supported Instrument Models
''',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'resettable': 'No',
        'short_description': '''
A string containing the instrument models supported by the specific
driver.
''',
        'type': 'ViString',
    },
    1050401: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Specific Driver Capabilities:Group Capabilities
''',
        'name': 'GROUP_CAPABILITIES',
        'resettable': 'No',
        'short_description': '''
A string containing the capabilities and extension groups supported by
the specific driver.
''',
        'type': 'ViString',
    },
    1050501: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Obsolete:Inherent IVI Attributes:Version Info:Engine Major Version
''',
        'name': 'ENGINE_MAJOR_VERSION',
        'resettable': 'No',
        'short_description': 'The major version number of the IVI engine.',
        'type': 'ViInt32',
    },
    1050502: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Obsolete:Inherent IVI Attributes:Version Info:Engine Minor Version
''',
        'name': 'ENGINE_MINOR_VERSION',
        'resettable': 'No',
        'short_description': 'The minor version number of the IVI engine.',
        'type': 'ViInt32',
    },
    1050503: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Version Info:Specific Driver Major Version
''',
        'name': 'SPECIFIC_DRIVER_MAJOR_VERSION',
        'resettable': 'No',
        'short_description': '''
Returns the major version number of this instrument driver.
''',
        'type': 'ViInt32',
    },
    1050504: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Version Info:Specific Driver Minor Version
''',
        'name': 'SPECIFIC_DRIVER_MINOR_VERSION',
        'resettable': 'No',
        'short_description': '''
Returns the minor version number of this instrument driver.
''',
        'type': 'ViInt32',
    },
    1050510: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Instrument Identification:Instrument Firmware Revision
''',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'resettable': 'No',
        'short_description': '''
A string containing the instrument firmware revision number.
''',
        'type': 'ViString',
    },
    1050511: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Instrument Identification:Instrument Manufacturer
''',
        'name': 'INSTRUMENT_MANUFACTURER',
        'resettable': 'No',
        'short_description': '''
A string containing the manufacturer of the instrument.
''',
        'type': 'ViString',
    },
    1050512: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Instrument Identification:Instrument Model
''',
        'name': 'INSTRUMENT_MODEL',
        'resettable': 'No',
        'short_description': 'A string containing the instrument model.',
        'type': 'ViString',
    },
    1050513: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Specific Driver Identification:Specific Driver Vendor
''',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'resettable': 'No',
        'short_description': '''
A string containing the vendor of the specific driver.
''',
        'type': 'ViString',
    },
    1050514: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Specific Driver Identification:Specific Driver Description
''',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'resettable': 'No',
        'short_description': '''
A string containing a description of the specific driver.
''',
        'type': 'ViString',
    },
    1050515: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Specific Driver Identification:Specific Driver Class Spec Major Version
''',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'resettable': 'No',
        'short_description': '''
The major version number of the class specification for the specific
driver.
''',
        'type': 'ViInt32',
    },
    1050516: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Specific Driver Identification:Specific Driver Class Spec Minor Version
''',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'resettable': 'No',
        'short_description': '''
The minor version number of the class specification for the specific
driver.
''',
        'type': 'ViInt32',
    },
    1050551: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Version Info:Specific Driver Revision
''',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'resettable': 'No',
        'short_description': '''
A string that contains additional version information about this
instrument driver.
''',
        'type': 'ViString',
    },
    1050553: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Obsolete:Inherent IVI Attributes:Version Info:Engine Revision
''',
        'name': 'ENGINE_REVISION',
        'resettable': 'No',
        'short_description': '''
A string that contains additional version information about the IVI
engine.
''',
        'type': 'ViString',
    },
    1150001: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Obsolete:Misc:IDQuery response',
        'name': 'IDQUERY_RESPONSE',
        'resettable': 'No',
        'short_description': '''
A string containing the type of instrument used in the current session.
''',
        'type': 'ViString',
    },
    1150002: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'MeasurementDestinationSlope',
        'lv_property': 'Trigger:Measurement Destination Slope',
        'name': 'MEASUREMENT_DESTINATION_SLOPE',
        'resettable': 'No',
        'short_description': '''
Specifies the polarity of the generated measurement complete signal.
''',
        'type': 'ViInt32',
    },
    1150003: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
For the NI 4050 only, specifies the shunt resistance value.

.. note::
   The NI 4050 requires an external shunt resistor for current measurements. This property should be set to the value of the shunt resistor.
''',
        'lv_property': 'Configuration:Measurement Options:Shunt Value',
        'name': 'SHUNT_VALUE',
        'resettable': 'No',
        'short_description': '''
For the NI 4050 only, specifies the shunt resistance value.
''',
        'type': 'ViReal64',
    },
    1150010: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'SampleTrigSlope',
        'lv_property': 'Multi Point Acquisition:Sample Trig Slope',
        'name': 'SAMPLE_TRIG_SLOPE',
        'resettable': 'No',
        'short_description': '''
Specifies the edge of the signal from the specified sample trigger
source on which the DMM is triggered.
''',
        'type': 'ViInt32',
    },
    1150014: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'OperationMode',
        'lv_property': 'Configuration:Advanced:Operation Mode',
        'name': 'OPERATION_MODE',
        'resettable': 'No',
        'short_description': '''
Specifies how the DMM acquires data.

.. note::
   The NI 4050 and NI 4060 are not supported.  

When you call niDMM Config Measurement , NI-DMM sets this property to
IVIDMM Mode. When you call niDMM Configure Waveform Acquisition , NI-DMM
sets this property to Waveform Mode. If you are programming properties
directly, you must set this property before setting other configuration
properties.
''',
        'type': 'ViInt32',
    },
    1150018: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Waveform Acquisition:Waveform Rate',
        'name': 'WAVEFORM_RATE',
        'resettable': 'No',
        'short_description': '''
Specifies the rate of the waveform acquisition in samples per second
(S/s). The valid rate is calculated by dividing 1,800,000 by an integer
divisor, and the rate falls between 10 and 1,800,000 samples per second.
The waveform rate is coerced upwards to the next valid rate. The default
value is 1,800,000 samples per second. Not supported by NI 4065.
''',
        'type': 'ViReal64',
    },
    1150019: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Waveform Acquisition:Waveform Points',
        'name': 'WAVEFORM_POINTS',
        'resettable': 'No',
        'short_description': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the number of
points to acquire in a waveform acquisition.
''',
        'type': 'ViInt32',
    },
    1150022: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'ADCCalibration',
        'lv_property': 'Configuration:Measurement Options:ADC Calibration',
        'name': 'ADC_CALIBRATION',
        'resettable': 'No',
        'short_description': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the ADC
calibration mode.
''',
        'type': 'ViInt32',
    },
    1150023: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'OffsetCompensatedOhms',
        'lv_property': '''
Configuration:Measurement Options:Offset Compensated Ohms
''',
        'name': 'OFFSET_COMPENSATED_OHMS',
        'resettable': 'No',
        'short_description': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, enables or disables
offset compensated ohms.
''',
        'type': 'ViInt32',
    },
    1150025: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'CurrentSource',
        'lv_property': 'Configuration:Measurement Options:Current Source',
        'name': 'CURRENT_SOURCE',
        'resettable': 'No',
        'short_description': '''
Specifies the current source provided during diode measurements.

The NI 4050 and NI 4060 are not supported.
''',
        'type': 'ViReal64',
    },
    1150026: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'DCNoiseRejection',
        'long_description': '''
Specifies the DC noise rejection mode.

.. note::
   The NI 4050 and NI 4060 are not supported.
''',
        'lv_property': '''
Configuration:Measurement Options:DC Noise Rejection
''',
        'name': 'DC_NOISE_REJECTION',
        'resettable': 'No',
        'short_description': 'Specifies the DC noise rejection mode.',
        'type': 'ViInt32',
    },
    1150027: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'WaveformCoupling',
        'lv_property': 'Waveform Acquisition:Waveform Coupling',
        'name': 'WAVEFORM_COUPLING',
        'resettable': 'No',
        'short_description': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072 only, specifies the
coupling during a waveform acquisition.
''',
        'type': 'ViInt32',
    },
    1150028: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Specifies the settling time in seconds. Use this property to override
the default settling time. To return to the default, set this property
to Auto (-1).

.. note::
   The NI 4050 and NI 4060 are not supported.
''',
        'lv_property': 'Configuration:Advanced:Settle Time',
        'name': 'SETTLE_TIME',
        'resettable': 'No',
        'short_description': '''
Specifies the settling time in seconds. Use this property to override
the default settling time. To return to the default, set this property
to Auto (-1).
''',
        'type': 'ViReal64',
    },
    1150029: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'InputResistance',
        'long_description': '''
Specifies the input resistance of the instrument.

.. note::
   The NI 4050 and NI 4060 are not supported.
''',
        'lv_property': '''
Configuration:Measurement Options:Input Resistance
''',
        'name': 'INPUT_RESISTANCE',
        'resettable': 'No',
        'short_description': '''
Specifies the input resistance of the instrument.
''',
        'type': 'ViReal64',
    },
    1150031: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
For the NI 4060 only, specifies a delay interval after a sample trigger.

+-----+---------------------+-----------------------------------------------------------------------------------------+
| 0   | IVI compliant       | The Sample Interval property is only used when the Sample Trigger is set to Interval.   |
+-----+---------------------+-----------------------------------------------------------------------------------------+
| 1   | Not IVI compliant   | The Sample Interval property is used as a delay after any type of Sample Trigger.       |
+-----+---------------------+-----------------------------------------------------------------------------------------+
''',
        'lv_property': 'Multi Point Acquisition:Sample Delay Mode',
        'name': 'SAMPLE_DELAY_MODE',
        'resettable': 'No',
        'short_description': '''
For the NI 4060 only, specifies a delay interval after a sample trigger.
''',
        'type': 'ViInt32',
    },
    1150032: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Configuration:Advanced:Number Of Averages',
        'name': 'NUMBER_OF_AVERAGES',
        'resettable': 'No',
        'short_description': '''
Specifies the number of averages to perform in a measurement. For the NI
4080/4081/4082 and NI 4070/4071/4072, applies only when the aperture
time is not set to Auto and Auto Zero is ON. The Number of Averages
Property will be ignored otherwise. The default is 4 for 7 1/2 digits;
otherwise, the default is 1.

The NI 4050 and NI 4060 are not supported.
''',
        'type': 'ViInt32',
    },
    1150034: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Multi Point Acquisition:Advanced:Latency',
        'name': 'LATENCY',
        'resettable': 'No',
        'short_description': '''
Specifies the number of measurements transferred at a time from the
instrument to an internal buffer. When set to Auto (-1), NI-DMM chooses
the transfer size.
''',
        'type': 'ViInt32',
    },
    1150037: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Multi Point Acquisition:Advanced:Buffer Size',
        'name': 'BUFFER_SIZE',
        'resettable': 'No',
        'short_description': '''
Specifies the size in samples of the internal data buffer. Maximum size
is 134,217,727 (0X7FFFFFF) samples. When set to Auto (-1), NI-DMM
chooses the buffer size.
''',
        'type': 'ViInt32',
    },
    1150044: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Configuration:Measurement Options:Frequency Voltage Auto Range Value
''',
        'name': 'FREQUENCY_VOLTAGE_AUTO_RANGE_VALUE',
        'resettable': 'No',
        'short_description': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the value of
the frequency voltage range. If auto ranging is enabled, shows the
actual value of the active frequency voltage range. If not Auto Ranging,
the value is the same as that of the Frequency Voltage Range property.
''',
        'type': 'ViReal64',
    },
    1150045: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'CableCompensationType',
        'long_description': '''
For the NI 4081 and NI 4072 only, specifies the type of cable
compensation that is applied to the current capacitance or inductance
measurement for the current range.

.. note::
   Changing the function or the range using property nodes or through niDMM Config Measurement resets this property to the default value.
''',
        'lv_property': '''
Configuration:Measurement Options:Capacitance and Inductance:Cable Compensation Type
''',
        'name': 'CABLE_COMPENSATION_TYPE',
        'resettable': 'No',
        'short_description': '''
For the NI 4081 and NI 4072 only, specifies the type of cable
compensation that is applied to the current capacitance or inductance
measurement for the current range.
''',
        'type': 'ViInt32',
    },
    1150046: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
For the NI 4082 and NI 4072 only, represents the reactive part
(reactance) of the short cable compensation. The valid range is any real
number >0. The default value (-1) indicates that compensation has not
taken place.

.. note::
   Changing the VI or the range through this property or through niDMM Config Measurement resets this property to the default value.
''',
        'lv_property': '''
Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Reactance
''',
        'name': 'REACTANCE',
        'resettable': 'No',
        'short_description': '''
For the NI 4082 and NI 4072 only, represents the reactive part
(reactance) of the short cable compensation. The valid range is any real
number >0. The default value (-1) indicates that compensation has not
taken place.
''',
        'type': 'ViReal64',
    },
    1150047: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
For the NI 4082 and NI 4072 only, represents the active part
(resistance) of the short cable compensation. The valid range is any
real number >0. The default value (-1) indicates that compensation has
not taken place.

.. note::
   Changing the VI or the range through this property or through niDMM Config Measurement resets this property to the default value.
''',
        'lv_property': '''
Configuration:Measurement Options:Capacitance and Inductance:Short Cable Compensation Values:Resistance
''',
        'name': 'RESISTANCE',
        'resettable': 'No',
        'short_description': '''
For the NI 4082 and NI 4072 only, represents the active part
(resistance) of the short cable compensation. The valid range is any
real number >0. The default value (-1) indicates that compensation has
not taken place.
''',
        'type': 'ViReal64',
    },
    1150048: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
For the NI 4082 and NI 4072 only, specifies the reactive part
(susceptance) of the open cable compensation. The valid range is any
real number >0. The default value (-1.0) indicates that compensation has
not taken place.

.. note::
   Changing the function or the range using property nodes or through niDMM Config Measurement resets this property to the default value.
''',
        'lv_property': '''
Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Susceptance
''',
        'name': 'SUSCEPTANCE',
        'resettable': 'No',
        'short_description': '''
For the NI 4082 and NI 4072 only, specifies the reactive part
(susceptance) of the open cable compensation. The valid range is any
real number >0. The default value (-1.0) indicates that compensation has
not taken place.
''',
        'type': 'ViReal64',
    },
    1150049: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
For the NI 4082 and NI 4072 only, specifies the active part
(conductance) of the open cable compensation. The valid range is any
real number >0. The default value (-1.0) indicates that compensation has
not taken place.

.. note::
   Changing the function or the range using property nodes or through niDMM Config Measurement resets this property to the default value.
''',
        'lv_property': '''
Configuration:Measurement Options:Capacitance and Inductance:Open Cable Compensation Values:Conductance
''',
        'name': 'CONDUCTANCE',
        'resettable': 'No',
        'short_description': '''
For the NI 4082 and NI 4072 only, specifies the active part
(conductance) of the open cable compensation. The valid range is any
real number >0. The default value (-1.0) indicates that compensation has
not taken place.
''',
        'type': 'ViReal64',
    },
    1150052: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'LCCalculationModel',
        'lv_property': '''
Configuration:Measurement Options:Capacitance and Inductance:Advanced:Calculation Model
''',
        'name': 'LC_CALCULATION_MODEL',
        'resettable': 'No',
        'short_description': '''
For the NI 4082 and NI 4072 only, specifies the type of algorithm that
the measurement processing uses for capacitance and inductance
measurements.
''',
        'type': 'ViInt32',
    },
    1150053: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'DCBias',
        'lv_property': '''
Configuration:Measurement Options:Capacitance and Inductance:Advanced:DC Bias
''',
        'name': 'DC_BIAS',
        'resettable': 'No',
        'short_description': '''
For the NI 4082 and NI 4072 only, controls the available DC bias for
capacitance measurements.
''',
        'type': 'ViInt32',
    },
    1150054: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Instrument Identification:Instrument Serial Number
''',
        'name': 'INSTRUMENT_SERIAL_NUMBER',
        'resettable': 'No',
        'short_description': '''
A string containing the serial number of the instrument. This property
corresponds to the serial number label that is attached to most
products.
''',
        'type': 'ViString',
    },
    1150055: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Configuration:Measurement Options:Capacitance and Inductance:Number of LC Measurements To Average
''',
        'name': 'NUMBER_OF_LC_MEASUREMENTS_TO_AVERAGE',
        'resettable': 'No',
        'short_description': '''
For the NI 4082 and NI 4072 only, specifies the number of LC
measurements that are averaged to produce one reading.
''',
        'type': 'ViInt32',
    },
    1150061: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Inherent IVI Attributes:Instrument Identification:Instrument Product ID
''',
        'name': 'INSTRUMENT_PRODUCT_ID',
        'resettable': 'No',
        'short_description': 'The PCI product ID.',
        'type': 'ViInt32',
    },
    1150120: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'RTDType',
        'lv_property': '''
Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Type
''',
        'name': 'RTD_TYPE',
        'resettable': 'No',
        'short_description': 'Specifies the RTD type.',
        'type': 'ViInt32',
    },
    1150121: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD A
''',
        'name': 'RTD_A',
        'resettable': 'No',
        'short_description': '''
Specifies the Callendar-Van Dusen A coefficient for RTD scaling when the
**RTD Type property** is set to Custom.
''',
        'type': 'ViReal64',
    },
    1150122: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD B
''',
        'name': 'RTD_B',
        'resettable': 'No',
        'short_description': '''
Specifies the Callendar-Van Dusen B coefficient for RTD scaling when the
**RTD Type property** is set to Custom.
''',
        'type': 'ViReal64',
    },
    1150123: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD C
''',
        'name': 'RTD_C',
        'resettable': 'No',
        'short_description': '''
Specifies the Callendar-Van Dusen C coefficient for RTD scaling when the
**RTD Type property** is set to Custom.
''',
        'type': 'ViReal64',
    },
    1150124: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'ThermistorType',
        'lv_property': '''
Configuration:Measurement Options:Temperature:Thermistor:Thermistor Type
''',
        'name': 'THERMISTOR_TYPE',
        'resettable': 'No',
        'short_description': 'Specifies the thermistor type.',
        'type': 'ViInt32',
    },
    1150125: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Configuration:Measurement Options:Temperature:Thermistor:Thermistor A
''',
        'name': 'THERMISTOR_A',
        'resettable': 'No',
        'short_description': '''
Specifies the Steinhart-Hart A coefficient for thermistor scaling when
the **Thermistor Type property** is set to Custom.
''',
        'type': 'ViReal64',
    },
    1150126: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Configuration:Measurement Options:Temperature:Thermistor:Thermistor B
''',
        'name': 'THERMISTOR_B',
        'resettable': 'No',
        'short_description': '''
Specifies the Steinhart-Hart B coefficient for thermistor scaling when
the **Thermistor Type property** is set to Custom.
''',
        'type': 'ViReal64',
    },
    1150127: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Configuration:Measurement Options:Temperature:Thermistor:Thermistor C
''',
        'name': 'THERMISTOR_C',
        'resettable': 'No',
        'short_description': '''
Specifies the Steinhart-Hart C coefficient for thermistor scaling when
the **Thermistor Type property** is set to Custom.
''',
        'type': 'ViReal64',
    },
    1250001: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'Function',
        'lv_property': 'Configuration:Function',
        'name': 'FUNCTION',
        'resettable': 'No',
        'short_description': '''
Specifies the measurement function. If you are setting this property
directly, you must also set the Operation Mode property, which controls
whether the DMM takes standard single or multipoint measurements, or
acquires a waveform. If you are programming properties directly, you
must set the Operation Mode property before setting other configuration
properties. If the Operation Mode property is set to Waveform Mode, the
only valid function types are Waveform Voltage and Waveform Current. Set
the Operation Mode property to IVIDMM Mode to set all other function
values.
''',
        'type': 'ViInt32',
    },
    1250002: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Specifies the measurement range. Use positive values to represent the
absolute value of the maximum expected measurement. The value is in
units appropriate for the current value of the Function property. For
example, if the Function property is set to DC Volts, the units are
volts.

.. note::
   The NI 4050, NI 4060, and NI 4065 only support Auto Range when the trigger and sample trigger are set to Immediate.  

+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| (-1.0)   | Auto Range On     | NI-DMM performs an Auto Range before acquiring the measurement.                                                                                                                                |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| (-2.0)   | Auto Range Off    | NI-DMM sets the Range to the current Auto Range Value and uses this range for all subsequent measurements until the measurement configuration is changed.                                      |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| (-3.0)   | Auto Range Once   | NI-DMM performs an Auto Range before acquiring the next measurement. The Auto Range Value is stored and used for all subsequent measurements until the measurement configuration is changed.   |
+----------+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
''',
        'lv_property': 'Configuration:Range',
        'name': 'RANGE',
        'resettable': 'No',
        'short_description': '''
Specifies the measurement range. Use positive values to represent the
absolute value of the maximum expected measurement. The value is in
units appropriate for the current value of the Function property. For
example, if the Function property is set to DC Volts, the units are
volts.
''',
        'type': 'ViReal64',
    },
    1250003: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'DigitsResolution',
        'long_description': '''
Specifies the measurement resolution in digits. Setting this property to
higher values increases the measurement accuracy. Setting this property
to lower values increases the measurement speed.

.. note::
   NI-DMM ignores this property for capacitance and inductance measurements on the NI 4082 and NI 4072. To achieve better resolution for such measurements, use the Number of LC Measurements to Average property.
''',
        'lv_property': 'Configuration:Digits Resolution',
        'name': 'DIGITS_RESOLUTION',
        'resettable': 'No',
        'short_description': '''
Specifies the measurement resolution in digits. Setting this property to
higher values increases the measurement accuracy. Setting this property
to lower values increases the measurement speed.
''',
        'type': 'ViReal64',
    },
    1250004: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TriggerSource',
        'lv_property': 'Trigger:Trigger Source',
        'name': 'TRIGGER_SOURCE',
        'resettable': 'No',
        'short_description': '''
Specifies the trigger source. When niDMM Initiate is called, the DMM
waits for the trigger specified with this property. After it receives
the trigger, the DMM waits the length of time specified with the Trigger
Delay property. The DMM then takes a measurement.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.
''',
        'type': 'ViInt32',
    },
    1250005: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Trigger:Trigger Delay',
        'name': 'TRIGGER_DELAY',
        'resettable': 'No',
        'short_description': '''
Specifies the time (in seconds) that the DMM waits after it has received
a trigger before taking a measurement. The default value is Auto Delay
(-1), which means that the DMM waits an appropriate settling time before
taking the measurement.

The NI 4080/4081/4082 uses the value specified in this property as
additional settling time. The valid range for Trigger Delay is Auto
Delay (-1) or 0.0 - 150.0 seconds, and the onboard timing resolution is
10.0 ns.

The NI 4065 and NI 4070/4071/4072 use the value specified in this
property as additional settling time. For these devices, the valid range
for Trigger Delay is Auto Delay (-1) or 0.0 - 149.0 seconds and the
onboard timing resolution is 34.72 ns.

On the NI 4060, if this property is set to 0, the DMM does not settle
before taking the measurement. On the NI 4060, the valid range for
Trigger Delay (-1) is 0.0-12.0 seconds and the onboard timing resolution
is 100 ms.

When using the NI 4050, this property must be set to Auto Delay (-1).

Use positive values to set the trigger delay in seconds.

Valid Range: Auto Delay (-1.0), 0.0-12.0 seconds (NI 4060 only),
0.0-149.0 seconds (NI 4065 and NI 4070/4071/4072)

Default Value: Auto Delay
''',
        'type': 'ViReal64',
    },
    1250006: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Configuration:Measurement Options:Min Frequency',
        'name': 'MIN_FREQUENCY',
        'resettable': 'No',
        'short_description': '''
Specifies the minimum frequency component of the input signal for AC
measurements. This property affects the DMM only when you set the
Function property to AC measurements. The valid range is 1 Hz-300 kHz
for the NI 4080/4081/4082 and NI 4070/4071/4072, 10 Hz-100 Hz for the NI
4065, and 20 Hz-25 kHz for the NI 4050 and NI 4060.
''',
        'type': 'ViReal64',
    },
    1250007: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Specifies the maximum frequency component of the input signal for AC
measurements. This property is used only for error checking and verifies
that the value of this parameter is less than the maximum frequency of
the device. This property affects the DMM only when you set the Function
property to AC measurements.

The valid ranges are shown in the following table.

+----------------------------------------+----------------+
| NI 4080/4081/4082, NI 4070/4071/4072   | 1 Hz-300 kHz   |
+----------------------------------------+----------------+
| NI 4065                                | 10 Hz-100 Hz   |
+----------------------------------------+----------------+
| NI 4050/4060                           | 20 Hz-25 kHz   |
+----------------------------------------+----------------+
''',
        'lv_property': 'Configuration:Measurement Options:Max Frequency',
        'name': 'MAX_FREQUENCY',
        'resettable': 'No',
        'short_description': '''
Specifies the maximum frequency component of the input signal for AC
measurements. This property is used only for error checking and verifies
that the value of this parameter is less than the maximum frequency of
the device. This property affects the DMM only when you set the Function
property to AC measurements.
''',
        'type': 'ViReal64',
    },
    1250008: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Specifies the measurement resolution in absolute units. Setting this
property to higher values increases the measurement accuracy. Setting
this property to lower values increases the measurement speed.

.. note::
   NI-DMM ignores this property for capacitance and inductance measurements on the NI 4082 and NI 4072. To achieve better resolution for such measurements, use the Number of LC Measurements to Average property.
''',
        'lv_property': 'Configuration:Absolute Resolution',
        'name': 'ABSOLUTE_RESOLUTION',
        'resettable': 'No',
        'short_description': '''
Specifies the measurement resolution in absolute units. Setting this
property to higher values increases the measurement accuracy. Setting
this property to lower values increases the measurement speed.
''',
        'type': 'ViReal64',
    },
    1250101: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the maximum
amplitude of the input signal for frequency measurements.

+------------------+--------+------------------------------------------------------------------------------------------------------------------------------------+
| Auto Range On    | -1.0   | Configures the DMM to take an Auto Range measurement to calculate the voltage range before each frequency or period measurement.   |
+------------------+--------+------------------------------------------------------------------------------------------------------------------------------------+
| Auto Range Off   | -2.0   | Disables Auto Ranging. NI-DMM sets the voltage range to the last calculated voltage range.                                         |
+------------------+--------+------------------------------------------------------------------------------------------------------------------------------------+
''',
        'lv_property': '''
Configuration:Measurement Options:Frequency Voltage Range
''',
        'name': 'FREQUENCY_VOLTAGE_RANGE',
        'resettable': 'No',
        'short_description': '''
For the NI 4080/4081/4082 and NI 4070/4071/4072, specifies the maximum
amplitude of the input signal for frequency measurements.
''',
        'type': 'ViReal64',
    },
    1250201: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TransducerType',
        'lv_property': '''
Configuration:Measurement Options:Temperature:Transducer Type
''',
        'name': 'TRANSDUCER_TYPE',
        'resettable': 'No',
        'short_description': 'Specifies the transducer type.',
        'type': 'ViInt32',
    },
    1250231: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'ThermocoupleType',
        'lv_property': '''
Configuration:Measurement Options:Temperature:Thermocouple:Thermocouple Type
''',
        'name': 'THERMOCOUPLE_TYPE',
        'resettable': 'No',
        'short_description': 'Specifies the thermocouple type.',
        'type': 'ViInt32',
    },
    1250232: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'ThermocoupleReferenceJunctionType',
        'lv_property': '''
Configuration:Measurement Options:Temperature:Thermocouple:Reference Junction Type
''',
        'name': 'TC_REF_JUNCTION_TYPE',
        'resettable': 'No',
        'short_description': '''
Specifies the thermocouple reference junction type.
''',
        'type': 'ViInt32',
    },
    1250233: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Configuration:Measurement Options:Temperature:Thermocouple:Fixed Reference Junction
''',
        'name': 'TC_FIXED_REF_JUNCTION',
        'resettable': 'No',
        'short_description': '''
Specifies the value of the fixed reference junction temperature for a
thermocouple in degrees Celsius.
''',
        'type': 'ViReal64',
    },
    1250242: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': '''
Configuration:Measurement Options:Temperature:Resistance Temperature Detector:RTD Resistance
''',
        'name': 'RTD_RESISTANCE',
        'resettable': 'No',
        'short_description': '''
Specifies the RTD resistance at 0 degrees Celsius.
''',
        'type': 'ViReal64',
    },
    1250301: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Multi Point Acquisition:Sample Count',
        'name': 'SAMPLE_COUNT',
        'resettable': 'No',
        'short_description': '''
Specifies the number of measurements the DMM takes each time it receives
a trigger in a multiple point acquisition. Setting Sample Count to 0 on
the NI 4050 and NI 4060 causes the device to take continuous
measurements. Otherwise, setting Sample Count to 0 causes the
conditional statement "Measurements equal to Sample Count" to always
evaluate to False, and causes the DMM to continue taking measurements in
the inner loop.
''',
        'type': 'ViInt32',
    },
    1250302: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'SampleTrigger',
        'lv_property': 'Multi Point Acquisition:Sample Trigger',
        'name': 'SAMPLE_TRIGGER',
        'resettable': 'No',
        'short_description': '''
Specifies the sample trigger source.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.
''',
        'type': 'ViInt32',
    },
    1250303: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Specifies the amount of time in seconds the DMM waits between
measurement cycles. This property only applies when the Sample Trigger
property is set to INTERVAL. The default value (-1) ensures that the DMM
settles for a recommended time, which is the same as using an immediate
trigger.

The NI 4065 and NI 4070/4071/4072 use the value specified in this
property as additional delay. On these devices, the onboard timing
resolution is 34.72 ns and the valid range is 0-149 s.

On the NI 4060, the value for this property is used as the settling
time. When this property is set to 0, the NI 4060 does not settle
between measurement cycles. The onboard timing resolution is 1 micro s
on the NI 4060.

Only positive values are valid when setting the sample interval.

.. note::
   The NI 4080/4081/4082 and NI 4050 are not supported.
''',
        'lv_property': 'Multi Point Acquisition:Sample Interval',
        'name': 'SAMPLE_INTERVAL',
        'resettable': 'No',
        'short_description': '''
Specifies the amount of time in seconds the DMM waits between
measurement cycles. This property only applies when the Sample Trigger
property is set to INTERVAL. The default value (-1) ensures that the DMM
settles for a recommended time, which is the same as using an immediate
trigger.
''',
        'type': 'ViReal64',
    },
    1250304: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Multi Point Acquisition:Trigger Count',
        'name': 'TRIGGER_COUNT',
        'resettable': 'No',
        'short_description': '''
Specifies the number of triggers the DMM receives before returning to
the Idle state. This property can be set to any positive ViInt32 value
for the NI 4065, NI 4070/4071/4072, and NI 4080/4081/4082.

The NI 4050/4060 only support this property being set to 1.

Refer to Multiple Point Acquisitions in the *NI Digital Multimeters
Help* for more information.
''',
        'type': 'ViInt32',
    },
    1250305: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'MeasurementCompleteDest',
        'long_description': '''
Specifies the destination of the measurement complete (MC) signal.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.

.. note::
   The NI 4050 is not supported.
''',
        'lv_property': 'Trigger:Measurement Complete Dest',
        'name': 'MEASUREMENT_COMPLETDEST',
        'resettable': 'No',
        'short_description': '''
Specifies the destination of the measurement complete (MC) signal.

To determine which values are supported by each device, refer to the
LabVIEW Trigger Routing section in the *NI Digital Multimeters Help*.
''',
        'type': 'ViInt32',
    },
    1250321: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': None,
        'long_description': '''
Specifies the measurement aperture time for the current configuration.
Aperture time is specified in units set by the Aperture Time Units
property. To override the default aperture, set this property to the
desired aperture time after calling niDMM Config Measurement . To return
to the default, set this property to Aperture Time Auto (-1).

Any number of powerline cycles (PLCs) within the minimum and maximum
ranges is allowed on the NI 4080/4081/4082 and NI 4070/4071/4072.

On the NI 4065 the minimum aperture time is 333 micro s and the maximum
aperture time is 78.2 s. If setting the number of averages directly, the
total measurement time is aperture time X the number of averages, which
must be less than 72.8 s. The aperture times allowed are 333 micro s,
667 micro s, or multiples of 1.11 ms—for example 1.11 ms, 2.22 ms, 3.33
ms, and so on. If you set an aperture time other than 333 micro s, 667
micro s, or multiples of 1.11 ms, the value will be coerced up to the
next supported aperture time.

On the NI 4060, when the powerline frequency is 60 Hz, the PLCs allowed
are 1 PLC, 6 PLC, 12 PLC, and 120 PLC. When the powerline frequency is
50 Hz, the PLCs allowed are 1 PLC, 5 PLC, 10 PLC, and 100 PLC.
''',
        'lv_property': 'Configuration:Advanced:Aperture Time',
        'name': 'APERTURE_TIME',
        'resettable': 'No',
        'short_description': '''
Specifies the measurement aperture time for the current configuration.
Aperture time is specified in units set by the Aperture Time Units
property. To override the default aperture, set this property to the
desired aperture time after calling niDMM Config Measurement . To return
to the default, set this property to Aperture Time Auto (-1).
''',
        'type': 'ViReal64',
    },
    1250322: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'ApertureTimeUnits',
        'long_description': '''
Specifies the units of aperture time for the current configuration.

.. note::
   The NI 4060 does not support an aperture time set in seconds.
''',
        'lv_property': 'Configuration:Advanced:Aperture Time Units',
        'name': 'APERTURE_TIME_UNITS',
        'resettable': 'No',
        'short_description': '''
Specifies the units of aperture time for the current configuration.
''',
        'type': 'ViInt32',
    },
    1250331: {
        'access': 'read only',
        'channel_based': 'False',
        'enum': None,
        'lv_property': 'Configuration:Auto Range Value',
        'name': 'AUTO_RANGE_VALUE',
        'resettable': 'No',
        'short_description': '''
Specifies the value of the range. If auto ranging is enabled, shows the
actual value of the active range. The value of this property is set
during a read operation.
''',
        'type': 'ViReal64',
    },
    1250332: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'AutoZero',
        'lv_property': 'Configuration:Measurement Options:Auto Zero',
        'name': 'AUTO_ZERO',
        'resettable': 'No',
        'short_description': '''
Specifies the AutoZero mode. This property is not supported for the NI
4050.
''',
        'type': 'ViInt32',
    },
    1250333: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'PowerlineFrequency',
        'long_description': '''
Specifies the powerline frequency. The NI 4060 and NI 4050 use this
value to select an aperture time to reject powerline noise by selecting
the appropriate internal sample clock and filter. The NI 4065, NI
4070/4071/4072, and NI 4080/4081/4082 use this value to select timebases
for setting the Aperture Time property in powerline cycles.

After configuring powerline frequency, set the Aperture Time Units
property to PLCs. When setting the Aperture Time property, select the
number of PLCs for the powerline frequency. For example, if powerline
frequency = 50 Hz (or 20 ms) and aperture time in PLCs = 5, then
aperture time in seconds = 20 ms \* 5 PLCs = 100 ms. Similarly, if
powerline frequency = 60 Hz (or 16.667 ms) and aperture time in PLCs =
6, then aperture time in seconds = 16.667 ms \* 6 PLCs = 100 ms.

.. note::
   For 400 Hz powerline frequency, use the 50 Hz setting.
''',
        'lv_property': '''
Configuration:Measurement Options:Powerline Frequency
''',
        'name': 'POWERLINE_FREQUENCY',
        'resettable': 'No',
        'short_description': '''
Specifies the powerline frequency. The NI 4060 and NI 4050 use this
value to select an aperture time to reject powerline noise by selecting
the appropriate internal sample clock and filter. The NI 4065, NI
4070/4071/4072, and NI 4080/4081/4082 use this value to select timebases
for setting the Aperture Time property in powerline cycles.
''',
        'type': 'ViReal64',
    },
    1250334: {
        'access': 'read-write',
        'channel_based': 'False',
        'enum': 'TriggerSlope',
        'lv_property': 'Trigger:Trigger Slope',
        'name': 'TRIGGER_SLOPE',
        'resettable': 'No',
        'short_description': '''
Specifies the edge of the signal from the specified trigger source on
which the DMM is triggered.
''',
        'type': 'ViInt32',
    },
}
