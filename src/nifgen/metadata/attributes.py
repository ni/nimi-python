# -*- coding: utf-8 -*-
# This file is generated from API metadata for NI-FGEN version 19.1.0d0
attributes = {
    1050002: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies whether to validate attribute values and function parameters.  If enabled, NI-FGEN validates the parameter values that  you pass to the functions. Range-checking  parameters is very useful for debugging. After you validate your program,  you can set this attribute to VI_FALSE to disable range checking and  maximize performance.\nDefault Value: VI_TRUE\nUse niFgen_InitWithOptions to override the default value.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:User Options:Range Check',
        'name': 'RANGE_CHECK',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050003: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies whether NI-FGEN queries the device status  after each operation. Querying the device status is very useful  for debugging. After you validate your program, you can set this  attribute to VI_FALSE to disable status checking and maximize  performance.\nNI-FGEN can choose to ignore status checking for  particular attributes regardless of the setting of this attribute.\nUse niFgen_InitWithOptions to override the default value.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:User Options:Query Instrument Status',
        'name': 'QUERY_INSTRUMENT_STATUS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050004: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies whether to cache the value of attributes.   When caching is enabled, NI-FGEN keeps track of  the current device settings and avoids sending redundant commands to  the device. Thus, you can significantly increase execution speed.\nNI-FGEN can choose to always cache or to never cache  particular attributes regardless of the setting of this attribute.  Use niFgen_InitWithOptions to override the default value.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:User Options:Cache',
        'name': 'CACHE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050005: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies whether to simulate NI-FGEN I/O  operations. If simulation is enabled, NI-FGEN  functions perform range checking and call Ivi_GetAttribute and  Ivi_SetAttribute, but they do not perform device I/O.   For output parameters that represent device data, NI-FGEN  functions return calculated values.\nDefault Value: VI_FALSE\nUse niFgen_InitWithOptions to override default value.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:User Options:Simulate',
        'name': 'SIMULATE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050006: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies whether the IVI Engine keeps a list of  the value coercions it makes for ViInt32 and ViReal64 attributes.   Call niFgen_GetNextCoercionRecord to extract and delete the oldest  coercion record from the list.\nDefault Value: VI_FALSE\nUse niFgen_InitWithOptions to override default value.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:User Options:Record Value Coercions',
        'name': 'RECORD_COERCIONS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050007: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the driver setup portion of the option string that was passed into the niFgen_InitWithOptions function.'
        },
        'lv_property': '',
        'name': 'DRIVER_SETUP',
        'resettable': True,
        'type': 'ViString'
    },
    1050021: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies whether to perform interchangeability checking and retrieve  interchangeability warnings when you call  niFgen_InitiateGeneration.\nInterchangeability warnings indicate that using your application with a  different device might cause different behavior.   Call niFgen_GetNextInterchangeWarning to extract interchange warnings.   Call niFgen_ClearInterchangeWarnings to clear the list  of interchangeability warnings without reading them.\nInterchangeability checking examines the attributes in a  capability group only if you specify a value for at least one  attribute within that group. Interchangeability warnings can  occur when an attribute affects the behavior of the device and you  have not set that attribute, or the attribute has been invalidated since you set it.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:User Options:Interchange Check',
        'name': 'INTERCHANGE_CHECK',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050101: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies a code that describes the first error that occurred since the last  call to niFgen_GetErrorInfo on the session. The value follows the  VXI plug&play completion code conventions. A negative value describes  an error condition. A positive value describes a warning condition  and indicates that no error occurred. A zero indicates that no error  or warning occurred. The error and warning values can be status codes  defined by IVI, VISA, class drivers, or specific drivers.\n'
        },
        'lv_property': 'Instrument:Obsolete:Primary Error',
        'name': 'PRIMARY_ERROR',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050102: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies an optional code that provides additional information concerning the  primary error condition. The error and warning values can be status codes  defined by IVI, VISA, class drivers, or specific drivers.  A value of zero indicates  no additional information.\n'
        },
        'lv_property': 'Instrument:Obsolete:Secondary Error',
        'name': 'SECONDARY_ERROR',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050103: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies an optional string that contains additional information concerning the  primary error condition.\n'
        },
        'lv_property': 'Instrument:Obsolete:Error Elaboration',
        'name': 'ERROR_ELABORATION',
        'resettable': False,
        'type': 'ViString'
    },
    1050203: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nIndicates the number of channels that the specific instrument  driver supports.\nFor each attribute for which IVI_VAL_MULTI_CHANNEL is set, the IVI Engine maintains a separate cache value for each channel.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Capabilities:Channel Count',
        'name': 'NUM_CHANNELS',
        'python_name': 'channel_count',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050302: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nA string that contains the prefix for NI-FGEN. The name of each  user-callable function in NI-FGEN starts with this prefix.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Identification:Driver Prefix',
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'resettable': False,
        'type': 'ViString'
    },
    1050304: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nIndicates the resource descriptor that NI-FGEN uses to identify the physical device.\nIf you initialize NI-FGEN with a logical name, this  attribute contains the resource descriptor that corresponds  to the entry in the IVI Configuration Utility.\nIf you initialize NI-FGEN with the resource  descriptor, this attribute contains that value.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Advanced Session Information:Resource Descriptor',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'resettable': False,
        'type': 'ViString'
    },
    1050305: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nA string containing the logical name that you specified when opening the  current IVI session.\nYou may pass a logical name to niFgen_init or  niFgen_InitWithOptions.  The IVI Configuration Utility must contain an entry for the logical name.   The logical name entry refers to a virtual instrument section in the  IVI Configuration file. The virtual instrument section specifies a physical  device and initial user options.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Advanced Session Information:Logical Name',
        'name': 'LOGICAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1050322: {
        'access': 'read only',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the I/O session that NI-FGEN uses  to communicate with the instrument.\n'
        },
        'lv_property': '',
        'name': 'IO_SESSION',
        'resettable': True,
        'type': 'ViSession'
    },
    1050327: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nReturns a model code of the device. For NI-FGEN versions that support more than one device, this  attribute contains a comma-separated list of supported device  models.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'resettable': False,
        'type': 'ViString'
    },
    1050401: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns a string that contains a comma-separated list of class-extention groups that  NI-FGEN implements.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities',
        'name': 'GROUP_CAPABILITIES',
        'resettable': False,
        'type': 'ViString'
    },
    1050503: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the major version number of NI-FGEN.'
        },
        'lv_property': 'Instrument:Obsolete:Major Version',
        'name': 'SPECIFIC_DRIVER_MAJOR_VERSION',
        'python_name': 'major_version',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050504: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the minor version number of NI-FGEN.'
        },
        'lv_property': 'Instrument:Obsolete:Minor Version',
        'name': 'SPECIFIC_DRIVER_MINOR_VERSION',
        'python_name': 'minor_version',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050510: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nA string that contains the firmware revision information  for the device that you are currently using.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Instrument Identification:Firmware Revision',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1050511: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nA string that contains the name of the device manufacturer you are currently  using.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Instrument Identification:Manufacturer',
        'name': 'INSTRUMENT_MANUFACTURER',
        'resettable': False,
        'type': 'ViString'
    },
    1050512: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nA string that contains the model number or name of the device that you  are currently using.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Instrument Identification:Model',
        'name': 'INSTRUMENT_MODEL',
        'resettable': False,
        'type': 'ViString'
    },
    1050513: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nA string that contains the name of the vendor that supplies NI-FGEN.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Identification:Driver Vendor',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'resettable': False,
        'type': 'ViString'
    },
    1050514: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nReturns a brief description of NI-FGEN.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Identification:Description',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'resettable': False,
        'type': 'ViString'
    },
    1050515: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the major version number of the class specification with which NI-FGEN is compliant.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Identification:Class Specification Major Version',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050516: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the minor version number of the class specification with which NI-FGEN is compliant.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Identification:Class Specification Minor Version',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050551: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nA string that contains additional version information about  NI-FGEN.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Driver Identification:Revision',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1150001: {
        'access': 'read only',
        'channel_based': True,
        'codegen_method': 'no',
        'lv_property': '',
        'name': 'ID_QUERY_RESPONSE',
        'resettable': True,
        'type': 'ViString'
    },
    1150101: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Controls whether the signal generator generates a digital pattern of the output signal.'
        },
        'lv_property': 'Output:Advanced:Digital Pattern Enabled',
        'name': 'DIGITAL_PATTERN_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150102: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Controls whether the signal generator applies a digital filter to the output signal. This attribute is valid in arbitrary waveform, arbitrary sequence, and script modes. This attribute can also be used in standard function and frequency list modes for user-defined waveforms.'
        },
        'lv_property': 'Output:Filters:Digital Filter Enabled',
        'name': 'DIGITAL_FILTER_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150103: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Controls whether the signal generator applies to an analog filter to the output signal. This attribute is valid in arbitrary waveform, arbitrary sequence, and script modes. This attribute can also be used in standard function and frequency list modes for user-defined waveforms.'
        },
        'lv_property': 'Output:Filters:Analog Filter Enabled',
        'name': 'ANALOG_FILTER_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150104: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Controls the filter correction frequency of the analog filter. This attribute corrects for the ripples in the analog filter frequency response at the frequency specified. For standard waveform output, the filter correction frequency should be set to be the same as the frequency of the standard waveform. To have no filter correction, set this attribute to 0 Hz.'
        },
        'lv_property': 'Instrument:5401/5411/5431:Filter Correction Frequency',
        'name': 'FILTER_CORRECTION_FREQUENCY',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150105: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nControls the duty cycle of the square wave the signal generator  produces on the SYNC out line.  Specify this attribute as a  percentage of the time the square wave is high in each cycle.\nUnits: Percentage of time the waveform is high\n'
        },
        'lv_property': 'Standard Function:Sync Duty Cycle High',
        'name': 'SYNC_DUTY_CYCLE_HIGH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150106: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nControls the update clock source.\n'
        },
        'enum': 'UpdateClockSource',
        'lv_property': 'Instrument:Obsolete:Update Clock Source',
        'name': 'UPDATE_CLOCK_SOURCE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150107: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Sets the frequency of the signal generator reference  clock. The signal generator uses the reference clock to derive  frequencies and sample rates when generating output.'
        },
        'lv_property': 'Clocks:Reference Clock:Frequency',
        'name': 'REF_CLOCK_FREQUENCY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150108: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Controls the trigger mode.'
        },
        'enum': 'TriggerMode',
        'lv_property': 'Triggers:Trigger Mode',
        'name': 'TRIGGER_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150109: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'The actual sample rate value of the signal generator.'
        },
        'lv_property': 'Instrument:Obsolete:Actual Arb Sample Rate',
        'name': 'ACTUAL_ARB_SAMPLE_RATE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150110: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nControls which clock mode is used for the signal generator.\nFor signal generators that support it, this attribute allows switching the sample  clock to High-Resolution mode. When in Divide-Down  mode, the sample rate can only be set to certain frequences, based on  dividing down the update clock. However, in High-Resolution mode, the  sample rate may be set to any value.\n'
        },
        'enum': 'ClockMode',
        'lv_property': 'Clocks:Sample Clock:Mode',
        'name': 'CLOCK_MODE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150111: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecify the source of the synchronization signal that you want to use.\n'
        },
        'enum': 'SynchronizationSource',
        'lv_property': 'Instrument:5401/5411/5431:Synchronization Source',
        'name': 'SYNCHRONIZATION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150112: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the Sample clock source. If you specify a divisor with the NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_DIVISOR  attribute, the Sample clock exported with the NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL attribute is the  value of the Sample clock after it is divided-down. For a list of the terminals available on your device, refer  to the Device Routes tab in MAX.\nTo change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.\n',
            'note': 'The signal generator must not be in the Generating state when you change this attribute.'
        },
        'enum': 'SampleClockSource',
        'lv_property': 'Clocks:Sample Clock:Source',
        'name': 'SAMPLE_CLOCK_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150113: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the reference clock source used by the signal generator.\nThe signal generator derives the frequencies and sample rates that it uses  to generate waveforms from the source you specify.  For example, when you set this attribute to ClkIn, the signal  generator uses the signal it receives at the CLK IN front  panel connector as the Reference clock.\nTo change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.\n',
            'note': 'The signal generator must not be in the Generating state when you change this attribute.'
        },
        'enum': 'ReferenceClockSource',
        'lv_property': 'Clocks:Reference Clock:Source',
        'name': 'REFERENCE_CLOCK_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150208: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Sets which frequency list the signal generator  produces. Create a frequency list using niFgen_CreateFreqList.  niFgen_CreateFreqList returns a handle that you can  use to identify the list.'
        },
        'lv_property': 'Standard Function:Frequency List Mode:Frequency List Handle',
        'name': 'FREQ_LIST_HANDLE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150209: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the maximum number of frequency lists the signal generator allows.'
        },
        'lv_property': 'Standard Function:Frequency List Mode:Maximum Number Of Frequency Lists',
        'name': 'MAX_NUM_FREQ_LISTS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150210: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the minimum number of frequency lists that the signal generator allows.'
        },
        'lv_property': 'Standard Function:Frequency List Mode:Minimum Frequency List Length',
        'name': 'MIN_FREQ_LIST_LENGTH',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150211: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the maximum number of steps that can be in a frequency  list.'
        },
        'lv_property': 'Standard Function:Frequency List Mode:Maximum Frequency List Length',
        'name': 'MAX_FREQ_LIST_LENGTH',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150212: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the minimum number of steps that can be in a frequency  list.'
        },
        'lv_property': 'Standard Function:Frequency List Mode:Minimum Frequency List Duration',
        'name': 'MIN_FREQ_LIST_DURATION',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150213: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the maximum duration of any one step in the frequency  list.'
        },
        'lv_property': 'Standard Function:Frequency List Mode:Maximum Frequency List Duration',
        'name': 'MAX_FREQ_LIST_DURATION',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150214: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the quantum of which all durations must be a multiple in a  frequency list.'
        },
        'lv_property': 'Standard Function:Frequency List Mode:Frequency List Duration Quantum',
        'name': 'FREQ_LIST_DURATION_QUANTUM',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150215: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'The bus type of the signal generator.'
        },
        'enum': 'BusType',
        'lv_property': 'Instrument:Bus Type',
        'name': 'BUS_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150216: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Selects which waveform type that the NI 5431 generates. Setting this attribute ensures that the crystal is set to the proper frequency.'
        },
        'enum': 'VideoWaveformType',
        'lv_property': 'Instrument:5401/5411/5431:Video Waveform Type',
        'name': 'VIDEO_WAVEFORM_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150218: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'This attribute only affects the device when NIFGEN_ATTR_DIGITAL_FILTER_ENABLED is set to VI_TRUE. If you do not set this attribute directly, NI-FGEN automatically selects the maximum interpolation factor allowed for the current sample rate. Valid values are 2, 4, and 8.'
        },
        'lv_property': 'Output:Filters:Digital Filter Interpolation Factor',
        'name': 'DIGITAL_FILTER_INTERPOLATION_FACTOR',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150219: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the factor by which to divide the Sample clock, also known as the Update clock, before it is exported.  To export the Sample clock, use the niFgen_ExportSignal function or the  NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL attribute.'
        },
        'lv_property': 'Clocks:Sample Clock:Exported Sample Clock Divisor',
        'name': 'EXPORTED_SAMPLE_CLOCK_DIVISOR',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150220: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'This channel-based attribute specifies the load impedance connected to the analog output of the channel. If you set this attribute to NIFGEN_VAL_MATCHED_LOAD_IMPEDANCE (-1.0), NI-FGEN assumes that the load impedance matches the output impedance. NI-FGEN compensates to give the desired peak-to-peak voltage amplitude or arbitrary gain (relative to 1 V).'
        },
        'lv_property': 'Output:Load Impedance',
        'name': 'LOAD_IMPEDANCE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150221: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'The NI-DAQmx task that NI-FGEN uses for the NI 5421.  For internal use only.'
        },
        'lv_property': 'Instrument:Obsolete:DAQmx Task',
        'name': 'DAQMX_TASK',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150222: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the analog signal path that should be used. The main path allows you to configure gain, offset, analog filter status, output impedance, and output enable. The main path has two amplifier options, high- and low-gain.\nThe direct path presents a much smaller gain range, and you cannot adjust offset or the filter status. The direct path also provides a smaller output range but also lower distortion. NI-FGEN normally chooses the amplifier based on the user-specified gain.\n'
        },
        'enum': 'AnalogPath',
        'lv_property': 'Output:Analog Path',
        'name': 'ANALOG_PATH',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150223: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the value programmed to the gain DAC. The value should be treated as an unsigned, right-justified number.'
        },
        'lv_property': 'Instrument:Calibration:Gain DAC Value',
        'name': 'GAIN_DAC_VALUE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150224: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the value programmed to the offset DAC. The value should be treated as an unsigned, right-justified number.'
        },
        'lv_property': 'Instrument:Calibration:Offset DAC Value',
        'name': 'OFFSET_DAC_VALUE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150225: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the value programmed to the oscillator frequency DAC. The value should be treated as an unsigned, right-justified number.'
        },
        'lv_property': 'Instrument:Calibration:Oscillator Freq DAC Value',
        'name': 'OSCILLATOR_FREQ_DAC_VALUE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150227: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the input of the calibration ADC. The ADC can take a reading from several inputs: the analog output, a 2.5 V reference, and ground.'
        },
        'lv_property': 'Instrument:Calibration:Cal ADC Input',
        'name': 'CAL_ADC_INPUT',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150228: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the amount of pre-amplifier attenuation that should be applied to the signal (in dB).'
        },
        'lv_property': 'Instrument:Calibration:Pre-Amplifier Attenuation',
        'name': 'PRE_AMPLIFIER_ATTENUATION',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150229: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the amount of post-amplifier attenuation that should be applied to the signal (in dB).'
        },
        'lv_property': 'Instrument:Calibration:Post-Amplifier Attenuation',
        'name': 'POST_AMPLIFIER_ATTENUATION',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150230: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the factor by which to divide the sample clock timebase (board clock) before it is exported.  To export the Sample clock timebase, use the niFgen_ExportSignal function or the  NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL attribute.'
        },
        'lv_property': 'Clocks:Sample Clock Timebase:Exported Sample Clock Timebase Divisor',
        'name': 'EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150231: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the absolute delay adjustment of the sample clock. The  sample clock delay adjustment is expressed in seconds.\ncan only be applied when an external sample clock is used.\n',
            'note': 'For the NI 5421, absolute delay'
        },
        'lv_property': 'Clocks:Advanced:Sample Clock Absolute Delay',
        'name': 'SAMPLE_CLOCK_ABSOLUTE_DELAY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150232: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'The value of the oscillator phase DAC.'
        },
        'lv_property': 'Clocks:Advanced:Oscillator Phase DAC Value',
        'name': 'OSCILLATOR_PHASE_DAC_VALUE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150233: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Binary value of the external clock delay.'
        },
        'lv_property': 'Clocks:Advanced:External Clock Delay Binary Value',
        'name': 'EXTERNAL_CLOCK_DELAY_BINARY_VALUE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150234: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the mask to apply to the analog output. The masked data is replaced with the data in NIFGEN_ATTR_ANALOG_STATIC_VALUE.'
        },
        'lv_property': 'Output:Data Mask:Analog Data Mask',
        'name': 'ANALOG_DATA_MASK',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150235: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the static value that replaces data masked by NIFGEN_ATTR_ANALOG_DATA_MASK.'
        },
        'lv_property': 'Output:Data Mask:Analog Static Value',
        'name': 'ANALOG_STATIC_VALUE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150236: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the mask to apply to the output on the digital connector. The masked data is replaced with the data in NIFGEN_ATTR_DIGITAL_STATIC_VALUE.'
        },
        'lv_property': 'Output:Data Mask:Digital Data Mask',
        'name': 'DIGITAL_DATA_MASK',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150237: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the static value that replaces data masked by NIFGEN_ATTR_DIGITAL_DATA_MASK.'
        },
        'lv_property': 'Output:Data Mask:Digital Static Value',
        'name': 'DIGITAL_STATIC_VALUE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150238: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nThis attribute contains the number of samples used in the standard function waveform  buffer. This attribute is only valid on devices that implement standard function mode  in software, and is read-only for all other devices.\nimplementation of Standard Function Mode on your device.\n',
            'note': 'Refer to the Standard Function Mode topic for more information on the'
        },
        'lv_property': 'Standard Function:Standard Function Mode:Buffer Size',
        'name': 'FUNC_BUFFER_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150239: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nThis attribute sets the maximum number of samples that can be used in the standard  function waveform buffer. Increasing this value may increase the quality of  the waveform. This attribute is only valid on devices that implement standard  function mode in software, and is read-only for all other devices.\nimplementation of Standard Function Mode on your device.\n',
            'note': 'Refer to the Standard Function Mode topic for more information on the'
        },
        'lv_property': 'Standard Function:Standard Function Mode:Maximum Buffer Size',
        'name': 'FUNC_MAX_BUFFER_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150240: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'The number of samples at a time to read from the file and download to onboard memory. Used in conjunction with the Create From File and Write From File functions.'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:File Transfer Block Size',
        'name': 'FILE_TRANSFER_BLOCK_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150241: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'The number of samples at a time to download to onboard memory. Useful when the total data to be transferred to onboard memory is large.'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Data Transfer Block Size',
        'name': 'DATA_TRANSFER_BLOCK_SIZE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150242: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'The total amount of memory, in bytes, on the signal generator.'
        },
        'lv_property': 'Instrument:Memory Size',
        'name': 'MEMORY_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150243: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': "\nThe signal generator's serial number.\n"
        },
        'lv_property': 'Instrument:Serial Number',
        'name': 'SERIAL_NUMBER',
        'resettable': False,
        'type': 'ViString'
    },
    1150244: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': "\nEnable the device for Direct DMA writes. When enabled, all Create Waveform and Write Waveform function calls that are given a data address in the Direct DMA Window will download data residing on the Direct DMA device to the instrument's onboard memory.\n"
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Direct DMA:Direct DMA Enabled',
        'name': 'DIRECT_DMA_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150245: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the size of the memory window in bytes (not samples) provided by your Direct DMA-compatible data source.'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Direct DMA:Window Size in Bytes',
        'name': 'DIRECT_DMA_WINDOW_SIZE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150246: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Enables or disables the OSP block of the signal generator. When the OSP block is disabled, all OSP-related attributes are disabled and have no effect on the generated signal.'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:OSP Enabled',
        'name': 'OSP_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150247: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'The way in which data is processed by the OSP block.'
        },
        'enum': 'DataProcessingMode',
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Data Processing Mode',
        'name': 'OSP_DATA_PROCESSING_MODE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150248: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThe rate at which the user-provided waveform data is generated when the NIFGEN_ATTR_OSP_ENABLED attribute is set to VI_TRUE.\nNI-FGEN sets the NIFGEN_ATTR_ARB_SAMPLE_RATE attribute of the signal generator to the product of the values of the NIFGEN_ATTR_OSP_IQ_RATE, NIFGEN_ATTR_OSP_FIR_FILTER_INTERPOLATION, and NIFGEN_ATTR_OSP_CIC_FILTER_INTERPOLATION attributes. When the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute is set to NIFGEN_VAL_OSP_REAL, the NIFGEN_ATTR_OSP_IQ_RATE attribute is the rate at which the signal generator processes real (I) data. When the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute is set to NIFGEN_VAL_OSP_COMPLEX, the NIFGEN_ATTR_OSP_IQ_RATE is the rate at which the signal generator processes complex (IQ) data.\n'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:IQ Rate',
        'name': 'OSP_IQ_RATE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150249: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Enables or disables generation of the carrier.'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Carrier Enabled',
        'name': 'OSP_CARRIER_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150250: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'The frequency of the generated carrier.'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Carrier Frequency',
        'name': 'OSP_CARRIER_FREQUENCY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150251: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'I Carrier Phase in degrees at the first point of the generation.'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Carrier Phase:Carrier Phase I',
        'name': 'OSP_CARRIER_PHASE_I',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150252: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Q Carrier Phase in degrees at the first point of the generation.  This attribute is only used when the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE  attribute is set to NIFGEN_VAL_OSP_COMPLEX.'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Carrier Phase:Carrier Phase Q',
        'name': 'OSP_CARRIER_PHASE_Q',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150253: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Pulse-shaping filter type for the FIR filter.'
        },
        'enum': 'FilterType',
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Filter Type',
        'name': 'OSP_FIR_FILTER_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150254: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies a factor by which the signal generator digitally multiplies generated data before converting it to an analog signal in the DAC. For a digital gain greater than 1.0, the product of digital gain times the generated data must be inside the range plus or minus 1.0 (assuming floating point data).  If the product exceeds these limits, the signal generator clips the output signal, and an error results.\nSome signal generators support both digital gain and an analog gain (analog gain is specified with the NIFGEN_ATTR_FUNC_AMPLITUDE attribute or the NIFGEN_ATTR_ARB_GAIN attribute). Digital gain can be changed during generation without the glitches that may occur when changing analog gains, due to relay switching. However, the DAC output resolution is a function of analog gain, so only analog gain makes full use of the resolution of the DAC.\n'
        },
        'lv_property': 'Output:Digital Gain',
        'name': 'DIGITAL_GAIN',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150255: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEnables or disables the FIR filter.\nThe NIFGEN_ATTR_OSP_CIC_FILTER_ENABLED and NIFGEN_ATTR_OSP_FIR_FILTER_ENABLED  attributes must have the same enable/disable setting.\n'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Advanced:FIR Filter Enabled',
        'name': 'OSP_FIR_FILTER_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150256: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Interpolation factor for the FIR filter. If you do not set this value,  NI-FGEN calculates the appropriate value based on the value of the NIFGEN_ATTR_OSP_IQ_RATE attribute.'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Advanced:FIR Interpolation Factor',
        'name': 'OSP_FIR_FILTER_INTERPOLATION',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150257: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEnables or disables the CIC filter.\nThe NIFGEN_ATTR_OSP_CIC_FILTER_ENABLED and NIFGEN_ATTR_OSP_FIR_FILTER_ENABLED  attributes must have the same enable/disable setting.\n'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Advanced:CIC Filter Enabled',
        'name': 'OSP_CIC_FILTER_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150258: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Interpolation factor for the CIC filter. If you do not set this value, NI-FGEN  calculates the appropriate value based on the value of the NIFGEN_ATTR_OSP_IQ_RATE attribute.'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Advanced:CIC Interpolation Factor',
        'name': 'OSP_CIC_FILTER_INTERPOLATION',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150259: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Alpha value to use when calculating the pulse-shaping FIR filter  coefficients. This attribute is used only when the NIFGEN_ATTR_OSP_FIR_FILTER_TYPE  attribute is set to NIFGEN_VAL_OSP_ROOT_RAISED_COSINE.'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Root Raised Cosine:Alpha',
        'name': 'OSP_FIR_FILTER_ROOT_RAISED_COSINE_ALPHA',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150260: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Alpha value to use when calculating the pulse shaping FIR filter  coefficients. Only used when the NIFGEN_ATTR_OSP_FIR_FILTER_TYPE  attribute is set to NIFGEN_VAL_OSP_RAISED_COSINE.'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Raised Cosine:Alpha',
        'name': 'OSP_FIR_FILTER_RAISED_COSINE_ALPHA',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150261: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Passband value to use when calculating the FIR filter coefficients.  The FIR filter is designed to be flat to passband × IQ rate.  This attribute is used only when the NIFGEN_ATTR_OSP_FIR_FILTER_TYPE  attribute is set to NIFGEN_VAL_OSP_FLAT.'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Flat:Passband',
        'name': 'OSP_FIR_FILTER_FLAT_PASSBAND',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150262: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'BT value to use when calculating the pulse-shaping FIR filter coefficients.  Only used when the NIFGEN_ATTR_OSP_FIR_FILTER_TYPE attribute is set to  NIFGEN_VAL_OSP_GAUSSIAN.'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Gaussian:BT',
        'name': 'OSP_FIR_FILTER_GAUSSIAN_BT',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150263: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Gain applied at the final stage of the CIC filter. Commonly used to compensate  for attenuation in the FIR filter. For FIR filter types other than Custom,  NI-FGEN calculates the CIC gain in order to achieve unity gain between the FIR  and CIC filters. Setting this attribute overrides the value set by NI-FGEN.'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Advanced:CIC Filter Gain',
        'name': 'OSP_CIC_FILTER_GAIN',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150264: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Digital gain to apply to the I data stream before any filtering by the OSP block.'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Gain:Pre-filter Gain I',
        'name': 'OSP_PRE_FILTER_GAIN_I',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150265: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Digital gain to apply to the Q data stream before any filtering by the OSP block.  This attribute is only used when the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute  is set to NIFGEN_VAL_OSP_COMPLEX.'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Gain:Pre-filter Gain Q',
        'name': 'OSP_PRE_FILTER_GAIN_Q',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150266: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Digital offset to apply to the I data stream. This offset is applied after  the Pre-Filter Gain and before any filtering.'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Offset:Pre-filter Offset I',
        'name': 'OSP_PRE_FILTER_OFFSET_I',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150267: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Digital offset to apply to the Q data stream. This offset is applied after  the Pre-Filter Gain and before any filtering. This attribute is used only when  the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute is set to NIFGEN_VAL_OSP_COMPLEX.'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:IQ Signal Adjustments:Offset:Pre-filter Offset Q',
        'name': 'OSP_PRE_FILTER_OFFSET_Q',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150268: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures error reporting when the OSP block detects an overflow in any of its stages.  Overflows lead to clipping of the waveform.\nYou can use the NIFGEN_ATTR_OSP_OVERFLOW_STATUS attribute to query for overflow  conditions whether or not the NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING attribute is  enabled. The device will continue to generate after an overflow whether or not the  NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING attribute is enabled.\n'
        },
        'enum': 'OspOverflowErrorReporting',
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Advanced:OSP Overflow Error Reporting',
        'name': 'OSP_OVERFLOW_ERROR_REPORTING',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150269: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns a bit field of the overflow status in any stage of the OSP block.  This attribute is functional regardless of the value for the  NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING attribute.\nWrite 0 to this attribute to clear the current NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING value.\n'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Advanced:OSP Overflow Status',
        'name': 'OSP_OVERFLOW_STATUS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150270: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies which script the generator produces. To configure the generator to run a particular script, set this attribute to the name of the script. Use niFgen_WriteScript to create multiple scripts. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_SCRIPT.\n',
            'note': 'The signal generator must not be in the Generating state when you change this attribute. To change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.'
        },
        'lv_property': 'Arbitrary Waveform:Script Mode:Script to Generate',
        'name': 'SCRIPT_TO_GENERATE',
        'resettable': False,
        'type': 'ViString'
    },
    1150271: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the number of markers supported by the device. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_SCRIPT.'
        },
        'lv_property': 'Instrument:Marker Events Count',
        'name': 'MARKER_EVENTS_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150272: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the number of Script triggers supported by the device. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_SCRIPT.'
        },
        'lv_property': 'Instrument:Script Triggers Count',
        'name': 'SCRIPT_TRIGGERS_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150273: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the number of Data Marker Events supported by the device.'
        },
        'lv_property': 'Instrument:Data Marker Events Count',
        'name': 'DATA_MARKER_EVENTS_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150274: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the window address (beginning of window) of the waveform data source. This window address is specified by your Direct DMA-compatible data source.'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Direct DMA:Window Address',
        'name': 'DIRECT_DMA_WINDOW_ADDRESS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150280: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies whether you want the Start trigger to be a Digital Edge, or Software trigger. You can also choose None as the value for this attribute.'
        },
        'enum': 'StartTriggerType',
        'lv_property': 'Triggers:Start:Trigger Type',
        'name': 'START_TRIGGER_TYPE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150281: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the source terminal for the Start trigger. This attribute is used only when NIFGEN_ATTR_START_TRIGGER_TYPE is set to Digital Edge.'
        },
        'lv_property': 'Triggers:Start:Digital Edge:Source',
        'name': 'DIGITAL_EDGE_START_TRIGGER_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150282: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the active edge for the Start trigger. This attribute is used only when NIFGEN_ATTR_START_TRIGGER_TYPE is set to Digital Edge.'
        },
        'enum': 'StartTriggerDigitalEdgeEdge',
        'lv_property': 'Triggers:Start:Digital Edge:Edge',
        'name': 'DIGITAL_EDGE_START_TRIGGER_EDGE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150283: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the destination terminal for exporting the Start trigger.'
        },
        'lv_property': 'Triggers:Start:Output Terminal',
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150290: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the Script trigger type. Depending upon the value of this attribute, additional attributes may need to be configured to fully configure the trigger.'
        },
        'enum': 'ScriptTriggerType',
        'lv_property': 'Triggers:Script:Trigger Type',
        'name': 'SCRIPT_TRIGGER_TYPE',
        'repeated_capability_type': 'script_triggers',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150291: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the source terminal for the Script trigger. This attribute is used when NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE is set to Digital Edge.'
        },
        'lv_property': 'Triggers:Script:Digital Edge:Source',
        'name': 'DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE',
        'repeated_capability_type': 'script_triggers',
        'resettable': True,
        'type': 'ViString'
    },
    1150292: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the active edge for the Script trigger. This attribute is used when NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE is set to Digital Edge.'
        },
        'enum': 'ScriptTriggerDigitalEdgeEdge',
        'lv_property': 'Triggers:Script:Digital Edge:Edge',
        'name': 'DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE',
        'repeated_capability_type': 'script_triggers',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150293: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the source terminal for the Script trigger. This attribute is used when NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE is set to Digital Level.'
        },
        'lv_property': 'Triggers:Script:Digital Level:Source',
        'name': 'DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE',
        'repeated_capability_type': 'script_triggers',
        'resettable': True,
        'type': 'ViString'
    },
    1150294: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the active level for the Script trigger. This attribute is used when NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE is set to Digital Level.'
        },
        'enum': 'ScriptTriggerDigitalLevelActiveLevel',
        'lv_property': 'Triggers:Script:Digital Level:Active Level',
        'name': 'DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL',
        'repeated_capability_type': 'script_triggers',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150295: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the output terminal for the exported Script trigger.\nSetting this attribute to an empty string means that when you commit the session, the signal is removed from that terminal and, if possible, the terminal is tristated.\n'
        },
        'lv_property': 'Triggers:Script:Output Terminal',
        'name': 'EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL',
        'repeated_capability_type': 'script_triggers',
        'resettable': True,
        'type': 'ViString'
    },
    1150310: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the destination terminal for the Ready for Start Event.'
        },
        'lv_property': 'Events:Ready For Start:Output Terminal',
        'name': 'READY_FOR_START_EVENT_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150311: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the output polarity of the Ready for Start Event.'
        },
        'enum': 'ReadyForStartEventActiveLevel',
        'lv_property': 'Events:Ready For Start:Level:Active Level',
        'name': 'READY_FOR_START_EVENT_LEVEL_ACTIVE_LEVEL',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150312: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the destination terminal for the Marker Event.'
        },
        'lv_property': 'Events:Marker:Output Terminal',
        'name': 'MARKER_EVENT_OUTPUT_TERMINAL',
        'repeated_capability_type': 'markers',
        'resettable': True,
        'type': 'ViString'
    },
    1150313: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the output polarity of the Marker Event.'
        },
        'enum': 'MarkerEventPulsePolarity',
        'lv_property': 'Events:Marker:Pulse:Polarity',
        'name': 'MARKER_EVENT_PULSE_POLARITY',
        'repeated_capability_type': 'markers',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150314: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the destination terminal for the Started Event.'
        },
        'lv_property': 'Events:Started:Output Terminal',
        'name': 'STARTED_EVENT_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150315: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the destination terminal for the Done Event.'
        },
        'lv_property': 'Events:Done:Output Terminal',
        'name': 'DONE_EVENT_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150316: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the output polarity of the Started Event.'
        },
        'enum': 'StartedEventActiveLevel',
        'lv_property': 'Events:Started:Level:Active Level',
        'name': 'STARTED_EVENT_LEVEL_ACTIVE_LEVEL',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150317: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the output polarity of the Done Event.'
        },
        'enum': 'DoneEventActiveLevel',
        'lv_property': 'Events:Done:Level:Active Level',
        'name': 'DONE_EVENT_LEVEL_ACTIVE_LEVEL',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150318: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the output polarity of the Started Event.'
        },
        'enum': 'StartedEventPulsePolarity',
        'lv_property': 'Events:Started:Pulse:Polarity',
        'name': 'STARTED_EVENT_PULSE_POLARITY',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150319: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the output polarity of the Done Event.'
        },
        'enum': 'DoneEventPulsePolarity',
        'lv_property': 'Events:Done:Pulse:Polarity',
        'name': 'DONE_EVENT_PULSE_POLARITY',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150320: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the terminal to which to export the Sample Clock.'
        },
        'lv_property': 'Clocks:Sample Clock:Export Output Terminal',
        'name': 'EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150321: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the terminal to which to export the Reference Clock.'
        },
        'lv_property': 'Clocks:Reference Clock:Export Output Terminal',
        'name': 'EXPORTED_REFERENCE_CLOCK_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150322: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the terminal to which to export the Onboard Reference Clock.'
        },
        'lv_property': 'Clocks:Reference Clock:Onboard Reference Clock:Export Output Terminal',
        'name': 'EXPORTED_ONBOARD_REFERENCE_CLOCK_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150323: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nWhen VI_TRUE, the signal generator applies a flatness correction factor to the generated sine wave in order to ensure the same output power level at all frequencies.\nThis attribute should be set to VI_FALSE when performing Flatness Calibration.\n'
        },
        'lv_property': 'Output:Filters:Flatness Correction Enabled',
        'name': 'FLATNESS_CORRECTION_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150324: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the waveform handle of the waveform used to continuously stream data during generation. This attribute defaults to -1 when no streaming waveform is specified.\nUsed in conjunction with NIFGEN_ATTR_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM.\n'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Streaming:Streaming Waveform Handle',
        'name': 'STREAMING_WAVEFORM_HANDLE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150325: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nIndicates the space available (in samples) in the streaming waveform for writing new data. During generation, this available space may be in multiple locations with, for example, part of the available space at the end of the streaming waveform and the rest at the beginning. In this situation, writing a block of waveform data the size of the  total space available in the streaming waveform causes NI-FGEN to return an error, as  NI-FGEN will not wrap the data from the end of the waveform to the beginning and cannot write data past the end of the waveform buffer.\nTo avoid writing data past the end of the waveform, write new data to the waveform in a fixed size that is an integer divisor of the total size of the streaming waveform.\nUsed in conjunction with the NIFGEN_ATTR_STREAMING_WAVEFORM_HANDLE or NIFGEN_ATTR_STREAMING_WAVEFORM_NAME attributes.\n'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Streaming:Space Available in Streaming Waveform',
        'name': 'STREAMING_SPACE_AVAILABLE_IN_WAVEFORM',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150326: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the name of the waveform used to continuously stream data during generation. This attribute defaults to // when no streaming waveform is specified.\nUse in conjunction with NIFGEN_ATTR_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM.\n'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Streaming:Streaming Waveform Name',
        'name': 'STREAMING_WAVEFORM_NAME',
        'resettable': True,
        'type': 'ViString'
    },
    1150327: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the position for a marker to be asserted in the arbitrary waveform. This attribute defaults to -1 when no marker position is specified. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB.\nUse niFgen_ExportSignal to export the marker signal.\n'
        },
        'lv_property': 'Arbitrary Waveform:Arbitrary Waveform Mode:Marker Position',
        'name': 'ARB_MARKER_POSITION',
        'repeated_capability_type': 'markers',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150328: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies number of times to repeat the arbitrary waveform when the triggerMode parameter of nifgen_ConfigureTriggerMode is set to NIFGEN_VAL_SINGLE or NIFGEN_VAL_STEPPED. This attribute is ignored if the triggerMode parameter is set to NIFGEN_VAL_CONTINUOUS or NIFGEN_VAL_BURST. Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB.\nWhen used during streaming, this attribute specifies the number of times to repeat the streaming waveform (the onboard memory allocated for streaming).  For more information about streaming, refer to the Streaming topic.\n'
        },
        'lv_property': 'Arbitrary Waveform:Arbitrary Waveform Mode:Repeat Count',
        'name': 'ARB_REPEAT_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150329: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the terminal to which to export the Sample clock timebase. If you specify a divisor with the NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR attribute,   the Sample clock exported with the NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL  attribute is the value of the Sample clock timebase after it is divided-down.  For a list of the terminals available on your device, refer to the Device Routes tab in MAX.\nTo change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.\n',
            'note': 'The signal generator must not be in the Generating state when you change this attribute.'
        },
        'lv_property': 'Clocks:Sample Clock Timebase:Export Output Terminal',
        'name': 'EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150330: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the terminal to which to export the SYNC OUT signal. This attribute is not supported for all devices.'
        },
        'lv_property': 'Standard Function:Sync Out Output Terminal',
        'name': 'SYNC_OUT_OUTPUT_TERMINAL',
        'resettable': True,
        'type': 'ViString'
    },
    1150331: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the output behavior for the Started Event.'
        },
        'enum': 'StartedEventOutputBehavior',
        'lv_property': 'Events:Started:Output Behavior',
        'name': 'STARTED_EVENT_OUTPUT_BEHAVIOR',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150332: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the output behavior for the Done Event.'
        },
        'enum': 'DoneEventOutputBehavior',
        'lv_property': 'Events:Done:Output Behavior',
        'name': 'DONE_EVENT_OUTPUT_BEHAVIOR',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150333: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the pulse width units for the Started Event.'
        },
        'enum': 'StartedEventPulseWidthUnits',
        'lv_property': 'Events:Started:Pulse:Width Units',
        'name': 'STARTED_EVENT_PULSE_WIDTH_UNITS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150334: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the pulse width units for the Done Event.'
        },
        'enum': 'DoneEventPulseWidthUnits',
        'lv_property': 'Events:Done:Pulse:Width Units',
        'name': 'DONE_EVENT_PULSE_WIDTH_UNITS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150335: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the pulse width for the Started Event.'
        },
        'lv_property': 'Events:Started:Pulse:Width Value',
        'name': 'STARTED_EVENT_PULSE_WIDTH',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150336: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the pulse width for the Done Event.'
        },
        'lv_property': 'Events:Done:Pulse:Width Value',
        'name': 'DONE_EVENT_PULSE_WIDTH',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150337: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the bit number to assign to the Data Marker Event.'
        },
        'lv_property': 'Events:Data Marker:Data Bit Number',
        'name': 'DATA_MARKER_EVENT_DATA_BIT_NUMBER',
        'repeated_capability_type': 'markers',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150338: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the output polarity of the Data marker event.'
        },
        'enum': 'DataMarkerEventLevelPolarity',
        'lv_property': 'Events:Data Marker:Level:Active Level',
        'name': 'DATA_MARKER_EVENT_LEVEL_POLARITY',
        'repeated_capability_type': 'markers',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150339: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the destination terminal for the Data Marker Event.'
        },
        'lv_property': 'Events:Data Marker:Output Terminal',
        'name': 'DATA_MARKER_EVENT_OUTPUT_TERMINAL',
        'repeated_capability_type': 'markers',
        'resettable': True,
        'type': 'ViString'
    },
    1150340: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the pulse width for the Marker Event.'
        },
        'lv_property': 'Events:Marker:Pulse:Width Value',
        'name': 'MARKER_EVENT_PULSE_WIDTH',
        'repeated_capability_type': 'markers',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150341: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the pulse width units for the Marker Event.'
        },
        'enum': 'MarkerEventPulseWidthUnits',
        'lv_property': 'Events:Marker:Pulse:Width Units',
        'name': 'MARKER_EVENT_PULSE_WIDTH_UNITS',
        'repeated_capability_type': 'markers',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150342: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the output behavior for the Marker Event.'
        },
        'enum': 'MarkerEventOutputBehavior',
        'lv_property': 'Events:Marker:Output Behavior',
        'name': 'MARKER_EVENT_OUTPUT_BEHAVIOR',
        'repeated_capability_type': 'markers',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150343: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the output polarity of the Marker Event.'
        },
        'enum': 'MarkerEventToggleInitialState',
        'lv_property': 'Events:Marker:Toggle:Initial State',
        'name': 'MARKER_EVENT_TOGGLE_INITIAL_STATE',
        'repeated_capability_type': 'markers',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150344: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns a bit field of the live status of all Marker Events.'
        },
        'lv_property': 'Events:Marker:Advanced:All Marker Events Live Status',
        'name': 'ALL_MARKER_EVENTS_LIVE_STATUS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150345: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Returns the live status of the specified Marker Event.'
        },
        'lv_property': 'Events:Marker:Advanced:Live Status',
        'name': 'MARKER_EVENT_LIVE_STATUS',
        'repeated_capability_type': 'markers',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150348: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Returns the live status of the specified Ready For Start Event.'
        },
        'lv_property': 'Events:Ready For Start:Advanced:Live Status',
        'name': 'READY_FOR_START_EVENT_LIVE_STATUS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150349: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Returns a bit field of the latched status of all Marker Events.  Write 0 to this attribute to clear the latched status of all Marker Events.'
        },
        'lv_property': 'Events:Marker:Advanced:All Marker Events Latched Status',
        'name': 'ALL_MARKER_EVENTS_LATCHED_STATUS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150350: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the latched status of the specified Marker Event.\nWrite VI_TRUE to this attribute to clear the latched status of the Marker Event.\n'
        },
        'lv_property': 'Events:Marker:Advanced:Latched Status',
        'name': 'MARKER_EVENT_LATCHED_STATUS',
        'repeated_capability_type': 'markers',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150351: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Returns the latched status of the specified Done Event.'
        },
        'lv_property': 'Events:Done:Advanced:Latched Status',
        'name': 'DONE_EVENT_LATCHED_STATUS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150352: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the latched status of the Started Event.'
        },
        'lv_property': 'Events:Started:Advanced:Latched Status',
        'name': 'STARTED_EVENT_LATCHED_STATUS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150354: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the amount of delay applied to a Marker Event with respect to the  analog output of the signal generator. A positive delay value indicates that  the Marker Event will come out after the analog data, while a negative delay  value indicates that the Marker Event will come out before the analog data.  The default value is zero, which will align the Marker Event with the  analog output. You can specify the units of the delay value by setting the NIFGEN_ATTR_MARKER_EVENT_DELAY attribute.'
        },
        'lv_property': 'Events:Marker:Advanced:Delay Value',
        'name': 'MARKER_EVENT_DELAY',
        'repeated_capability_type': 'markers',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150355: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the units applied to the value of the NIFGEN_ATTR_MARKER_EVENT_DELAY attribute.  Valid units are seconds and sample clock periods.'
        },
        'enum': 'MarkerEventDelayUnits',
        'lv_property': 'Events:Marker:Advanced:Delay Units',
        'name': 'MARKER_EVENT_DELAY_UNITS',
        'repeated_capability_type': 'markers',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150356: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the amount of delay applied to a Started Event with respect to the  analog output of the signal generator. A positive delay value specifies that  the Started Event occurs after the analog data, and a negative delay  value specifies that the Started Event occurs before the analog data.  The default value is zero, which will align the Started event with the analog output.\nYou can specify the units of the delay value by setting the NIFGEN_ATTR_STARTED_EVENT_DELAY attribute.\n'
        },
        'lv_property': 'Events:Started:Advanced:Delay Value',
        'name': 'STARTED_EVENT_DELAY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150357: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the units applied to the value of the NIFGEN_ATTR_STARTED_EVENT_DELAY\nattribute.  Valid units are seconds and sample clock periods.\n'
        },
        'enum': 'StartedEventDelayUnits',
        'lv_property': 'Events:Started:Advanced:Delay Units',
        'name': 'STARTED_EVENT_DELAY_UNITS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150358: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the amount of delay applied to a Done Event with respect to the  analog output of the signal generator. A positive delay value indicates that  the Done Event will come out after the analog data, while a negative delay  value indicates that the Done Event will come out before the analog data.  The default value is zero, which will align the Done Event with the analog output.  You can specify the units of the delay value by setting the  NIFGEN_ATTR_DONE_EVENT_DELAY attribute.'
        },
        'lv_property': 'Events:Done:Advanced:Delay Value',
        'name': 'DONE_EVENT_DELAY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150359: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the units applied to the value of the NIFGEN_ATTR_DONE_EVENT_DELAY attribute. Valid units are seconds and sample clock periods.'
        },
        'enum': 'DoneEventDelayUnits',
        'lv_property': 'Events:Done:Advanced:Delay Units',
        'name': 'DONE_EVENT_DELAY_UNITS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150362: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nControls whether or not NI-FGEN allows performance optimizations for DMA transfers.\nThis attribute is only valid for PCI and PXI SMC-based devices.\nThis attribute is enabled (VI_TRUE) by default, and NI recommends leaving it enabled.\n'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Advanced:PCI DMA Optimizations Enabled',
        'name': 'PCI_DMA_OPTIMIZATIONS_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150365: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies whether gain and offset values will be analyzed based on single-ended or differential operation.'
        },
        'enum': 'TerminalConfiguration',
        'lv_property': 'Output:Terminal Configuration',
        'name': 'TERMINAL_CONFIGURATION',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150366: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies, in volts, the value the signal generator adds to or subtracts from the arbitrary waveform data. This attribute applies only when you set the NIFGEN_ATTR_TERMINAL_CONFIGURATION attribute to NIFGEN_VAL_DIFFERENTIAL. Common mode offset is applied to the signals generated at each differential output terminal.'
        },
        'lv_property': 'Output:Common Mode Offset',
        'name': 'COMMON_MODE_OFFSET',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150367: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the Sample Clock Timebase source.\nTo change the device configuration, call the niFgen_AbortGeneration function or wait for the generation to complete.\n',
            'note': 'The signal generator must not be in the Generating state when you change this attribute.'
        },
        'enum': 'SampleClockTimebaseSource',
        'lv_property': 'Clocks:Sample Clock Timebase:Source',
        'name': 'SAMPLE_CLOCK_TIMEBASE_SOURCE',
        'resettable': True,
        'type': 'ViString'
    },
    1150368: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the Sample clock timebase rate. This attribute applies only to external Sample clock timebases.\nTo change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.\n',
            'note': 'The signal generator must not be in the Generating state when you change this attribute.'
        },
        'lv_property': 'Clocks:Sample Clock Timebase:Rate',
        'name': 'SAMPLE_CLOCK_TIMEBASE_RATE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150369: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies, in seconds, the delay to apply to the analog output of the channel specified by the channel string. You can use the channel delay to configure the timing relationship between channels on a multichannel device. Values for this attribute can be zero or positive. A value of zero indicates that the channels are aligned. A positive value delays the analog output by the specified number of seconds.'
        },
        'lv_property': 'Output:Channel Delay',
        'name': 'CHANNEL_DELAY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150370: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the generation mode of the OSP, which determines the type of data contained in the output signal.'
        },
        'enum': 'OspMode',
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:OSP Mode',
        'name': 'OSP_MODE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150371: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the amount of frequency shift applied to the baseband signal.'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Frequency Shift',
        'name': 'OSP_FREQUENCY_SHIFT',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150373: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the maximum amount of bus bandwidth (in bytes per second) to use for data transfers. The signal generator limits data transfer speeds on the PCIe bus to the value you specify for this attribute. Set this attribute to optimize bus bandwidth usage for multi-device streaming applications by preventing the signal generator from consuming all of the available bandwidth on a PCI express link when waveforms are being written to the onboard memory of the device.'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Maximum Bandwidth',
        'name': 'DATA_TRANSFER_MAXIMUM_BANDWIDTH',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150374: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the preferred size of the data field in a PCI Express read request packet. In general, the larger the packet size, the more efficiently the device uses the bus. By default, NI signal generators use the largest packet size allowed by the system. However, due to different system implementations, some systems may perform better with smaller packet sizes.\nRecommended values for this attribute are powers of two between 64 and 512.\nIn some cases, the signal generator generates packets smaller than  the preferred size you set with this attribute.\nYou cannot change this attribute while the device is generating a waveform. If you want to change the device configuration, call the niFgen_AbortGeneration function or wait for the generation to complete.\n',
            'note': '\n:\n'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Advanced:Preferred Packet Size',
        'name': 'DATA_TRANSFER_PREFERRED_PACKET_SIZE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150375: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the maximum number of concurrent PCI Express read requests the signal generator can issue.\nWhen transferring data from computer memory to device onboard memory across the PCI Express bus, the signal generator can issue multiple memory reads at the same time. In general, the larger the number of read requests, the more efficiently the device uses the bus because the multiple read requests keep the data flowing, even in a PCI Express topology that has high latency due to PCI Express switches in the data path. Most NI devices can issue a large number of read requests (typically 8 or 16). By default, this attribute is set to the highest value the signal generator supports.\nIf other devices in your system cannot tolerate long data latencies, it may be helpful to decrease the number of in-flight read requests the NI signal generator issues. This helps to reduce the amount of data the signal generator reads at one time.\n'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Advanced:Maximum In-Flight Read Requests',
        'name': 'DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150376: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies a multiplication factor to use to obtain a desired sample rate from an external Sample clock.  The resulting sample rate is equal to this factor multiplied by the external Sample clock rate.  You can use this attribute to generate samples at a rate higher than your external clock rate.  When using this attribute, you do not need to explicitly set the external clock rate.'
        },
        'lv_property': 'Clocks:Advanced:External Sample Clock Multiplier',
        'name': 'EXTERNAL_SAMPLE_CLOCK_MULTIPLIER',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150377: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the behavior of the output during the Idle state.  The output can be configured to hold the last generated voltage before entering the Idle state or jump to the Idle Value.'
        },
        'enum': 'IdleBehavior',
        'lv_property': 'Output:Advanced:Idle Behavior',
        'name': 'IDLE_BEHAVIOR',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150378: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the value to generate in the Idle state.  The Idle Behavior must be configured to jump to this value.'
        },
        'lv_property': 'Output:Advanced:Idle Value',
        'name': 'IDLE_VALUE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150379: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the behavior of the output while waiting for a script trigger or during a wait instruction.  The output can be configured to hold the last generated voltage before waiting or jump to the Wait Value.'
        },
        'enum': 'WaitBehavior',
        'lv_property': 'Output:Advanced:Wait Behavior',
        'name': 'WAIT_BEHAVIOR',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150380: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the value to generate while waiting.  The Wait Behavior must be configured to jump to this value.'
        },
        'lv_property': 'Output:Advanced:Wait Value',
        'name': 'WAIT_VALUE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150389: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Compensate for OSP Filter Group Delay. If this is enabled, the Event Outputs will be aligned  with the Analog Output. The Analog output will also be aligned between synchronized devices  (using NI-TClk).'
        },
        'lv_property': 'Arbitrary Waveform:Onboard Signal Processing:Advanced:Compensate for Filter Group Delay',
        'name': 'OSP_COMPENSATE_FOR_FILTER_GROUP_DELAY',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150390: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nA string that contains the module revision  for the device that you are currently using.\n'
        },
        'lv_property': 'Instrument:Inherent IVI Attributes:Instrument Identification:Module Revision',
        'name': 'MODULE_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1150391: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies whether the signal generator reads data from the peer-to-peer endpoint, as opposed to  the typical method of reading it from the onboard memory. This attribute is endpoint based.\n'
        },
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:P2P Enabled',
        'name': 'P2P_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150392: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies which channels will be written to by a peer-to-peer endpoint. If multiple channels are specified,  data is deinterleaved to each channel. The default value is an empty string, which means all configured channels.  Channels are configured using the niFgen_ConfigureChannels function. This attribute is endpoint based.\n'
        },
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Destination Channels',
        'name': 'P2P_DESTINATION_CHANNELS',
        'resettable': False,
        'type': 'ViString'
    },
    1150393: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the size, in samples per channel, of the peer-to-peer endpoint. This attribute is endpoint based.\n'
        },
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Endpoint Size',
        'name': 'P2P_ENDPOINT_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150394: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the current space available in the endpoint in samples per channel. You can use this attribute when  priming the endpoint with initial data through the niFgen_WriteP2PEndpointI16 function to determine how many  samples you can write. You can also use this attribute to characterize the performance and measure the latency  of the peer-to-peer stream as data moves across the bus. This attribute is endpoint based.\n'
        },
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Space Available In Endpoint',
        'name': 'P2P_SPACE_AVAILABLE_IN_ENDPOINT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150395: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the largest number of samples per channel available in the endpoint since this attribute was last read.  Use this attribute to determine how much endpoint space to use as a buffer against PCI Express bus traffic  latencies by reading the attribute and keeping track of the largest value returned. This attribute is endpoint based.\nIf you wish to minimize the latency for data to move through the endpoint and be generated by the signal generator,  use the NIFGEN_ATTR_P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS attribute to grant fewer initial credits than the  default of the entire endpoint size.\n'
        },
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Most Space Available In Endpoint',
        'name': 'P2P_MOST_SPACE_AVAILABLE_IN_ENDPOINT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150396: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the number of peer-to-peer FIFO endpoints supported by the device.\n'
        },
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Endpoint Count',
        'name': 'P2P_ENDPOINT_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150397: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEnables/disables manual configuration for a peer-to-peer endpoint. Enabling this attribute disables  automatic NI-P2P stream manager flow control and Done Notifications.\n'
        },
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Manual:Manual Configuration Enabled',
        'name': 'P2P_MANUAL_CONFIGURATION_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150398: {
        'access': 'write only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nIndicates the address in the writer peer to which the signal generator should send data transfer permission credits.  This attribute is endpoint based.\n',
            'note': '\nYou can only use this attribute when the NIFGEN_ATTR_P2P_MANUAL_CONFIGURATION_ENABLED attribute is set to VI_TRUE.\n'
        },
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Manual:Configuration:Data Transfer Permission Address',
        'name': 'P2P_DATA_TRANSFER_PERMISSION_ADDRESS',
        'resettable': False,
        'type': 'ViInt64'
    },
    1150399: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nIndicates the address in the writer peer to which the signal generator should send data transfer permission credits.  This attribute is endpoint based.\n',
            'note': '\nYou can only use this attribute when the NIFGEN_ATTR_P2P_MANUAL_CONFIGURATION_ENABLED attribute is set to VI_TRUE.\n'
        },
        'enum': 'P2PAddressType',
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Manual:Configuration:Data Transfer Permission Address Type',
        'name': 'P2P_DATA_TRANSFER_PERMISSION_ADDRESS_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150400: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the interval, in samples per channel, at which the signal generator issues credits to allow the writer  peer to transfer data over the bus into the configured endpoint. Refer to the Flow Control topic in the NI Signal  Generators Help for more information. This attribute is coerced up by NI-FGEN to the nearest 128 byte boundary.  This attribute is endpoint based.\nDefault Value: 1,024 samples per channel\n'
        },
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Data Transfer Permission Interval',
        'name': 'P2P_DATA_TRANSFER_PERMISSION_INTERVAL',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150401: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the signal generator address where endpoint data is sent by the writer peer. The type of this address is specified  by the NIFGEN_ATTR_P2P_ENDPOINT_WINDOW_ADDRESS_TYPE attribute. This attribute is endpoint based.\n',
            'note': '\nYou can only use this attribute when the NIFGEN_ATTR_P2P_MANUAL_CONFIGURATION_ENABLED attribute is set to VI_TRUE.\n'
        },
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Manual:Configuration:Endpoint Window Address',
        'name': 'P2P_ENDPOINT_WINDOW_ADDRESS',
        'resettable': False,
        'type': 'ViInt64'
    },
    1150402: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the type of the NIFGEN_ATTR_P2P_ENDPOINT_WINDOW_ADDRESS attribute. This attribute is endpoint based.\n',
            'note': '\nYou can only use this attribute when the NIFGEN_ATTR_P2P_MANUAL_CONFIGURATION_ENABLED attribute is set to VI_TRUE.\n'
        },
        'enum': 'P2PAddressType',
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Manual:Configuration:Endpoint Window Address Type',
        'name': 'P2P_ENDPOINT_WINDOW_ADDRESS_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150403: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the type of the NIFGEN_ATTR_P2P_ENDPOINT_WINDOW_ADDRESS attribute. This attribute is endpoint based.\n',
            'note': '\nYou can only use this attribute when the NIFGEN_ATTR_P2P_MANUAL_CONFIGURATION_ENABLED attribute is set to VI_TRUE.\n'
        },
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Manual:Configuration:Endpoint Window Size',
        'name': 'P2P_ENDPOINT_WINDOW_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150405: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the signal generator address to which the writer peer sends the NIFGEN_ATTR_P2P_DONE_NOTIFICATION_VALUE.  This attribute is endpoint based. Refer to the Stopping a Peer-to-Peer Generation topic in the NI Signal Generators Help  for more information.\n',
            'note': '\nYou can use this attribute only when the NIFGEN_ATTR_P2P_MANUAL_CONFIGURATION_ENABLED attribute is set to VI_TRUE.\n'
        },
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Manual:Notification:Done Notification Address',
        'name': 'P2P_DONE_NOTIFICATION_ADDRESS',
        'resettable': False,
        'type': 'ViInt64'
    },
    1150406: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the address type of the NIFGEN_ATTR_P2P_DONE_NOTIFICATION_ADDRESS attribute. This attribute is endpoint based.  Refer to the Stopping a Peer-to-Peer Generation topic in the NI Signal Generators Help for more information.\n',
            'note': '\nYou can only use this attribute when the NIFGEN_ATTR_P2P_MANUAL_CONFIGURATION_ENABLED attribute is set to VI_TRUE.\n'
        },
        'enum': 'P2PAddressType',
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Manual:Notification:Done Notification Address Type',
        'name': 'P2P_DONE_NOTIFICATION_ADDRESS_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150407: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the value the writer peer should write to the address specified by the NIFGEN_ATTR_P2P_DONE_NOTIFICATION_ADDRESS  attribute. This attribute is endpoint based. Refer to the Stopping a Peer-to-Peer Generation topic in the NI Signal Generators Help  for more information.\n',
            'note': '\nYou can only use this attribute when the NIFGEN_ATTR_P2P_MANUAL_CONFIGURATION_ENABLED attribute is set to VI_TRUE.\n'
        },
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Manual:Notification:Done Notification Value',
        'name': 'P2P_DONE_NOTIFICATION_VALUE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150408: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the initial amount of data, in samples per channel, that the writer peer is allowed to transfer over the bus  into the configured endpoint when the peer-to-peer data stream is enabled. If you do not set this property and the endpoint  is empty, credits equal to the full size of the endpoint are issued to the writer peer. If data has been written to the  endpoint using the niFgen_WriteP2PEndpointI16 function prior to enabling the stream, credits equal to the remaining space  available in the endpoint are issued to the writer peer. This attribute is coerced up by NI-FGEN to 8-byte boundaries.\n'
        },
        'lv_property': 'Arbitrary Waveform:Peer-to-Peer:Data Transfer Permission Initial Credits',
        'name': 'P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150409: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the maximum amount of time allowed to complete a streaming write operation.'
        },
        'lv_property': 'Arbitrary Waveform:Data Transfer:Streaming:Streaming Write Timeout',
        'name': 'STREAMING_WRITE_TIMEOUT',
        'resettable': True,
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1150410: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the Endpoint threshold for the Start trigger. This attribute is used only when NIFGEN_ATTR_START_TRIGGER_TYPE is set to P2P Endpoint Fullness.'
        },
        'lv_property': 'Triggers:Start:P2P Endpoint Fullness:Level',
        'name': 'P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150411: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Controls the specified auxiliary power pin. Setting this attribute to TRUE energizes the auxiliary power when the session is committed. When this attribute is FALSE, the power pin of the connector outputs no power.'
        },
        'lv_property': 'Output:Advanced:AUX Power Enabled',
        'name': 'AUX_POWER_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1150412: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Gets the absolute file path to the bitfile loaded on the FPGA.'
        },
        'lv_property': 'Instrument:FPGA Bitfile Path',
        'name': 'FPGA_BITFILE_PATH',
        'resettable': False,
        'type': 'ViString'
    },
    1150413: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the sub-Sample Clock delay, in seconds, to apply to the\nwaveform. Use this property to reduce the trigger jitter when\nsynchronizing multiple devices with NI-TClk. This property can also help\nmaintain synchronization repeatability by writing the absolute delay\nvalue of a previous measurement to the current session.\nTo set this property, the waveform generator must be in the Idle\n(Configuration) state.\n**Units**: seconds (s)\n**Valid Values**: Plus or minus half of one Sample Clock period\n**Default Value**: 0.0\n**Supported Waveform Generators**: PXIe-5413/5423/5433\n',
            'note': '\nIf this property is set, NI-TClk cannot perform any sub-Sample Clock\nadjustment.\n'
        },
        'lv_property': 'Output:Absolute Delay',
        'name': 'ABSOLUTE_DELAY',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250001: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Sets which output mode the signal generator will use. The value you specify determines which functions and attributes you use to configure the waveform the signal generator produces.',
            'note': 'The signal generator must not be in the Generating state when you change this attribute. To change the device configuration, call niFgen_AbortGeneration or wait for the generation to complete.'
        },
        'enum': 'OutputMode',
        'lv_property': 'Output:Output Mode',
        'name': 'OUTPUT_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250002: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nControls the reference clock source that the signal generator uses.\nThe signal generator derives the frequencies and sample rates that it  uses to generate waveforms from the source you specify. For example, when you set this parameter to NIFGEN_VAL_EXTERNAL, the signal generator uses the signal it receives at its external clock connector as its reference  clock.\nspecify.\n',
            'note': 'All of the signal generator channels use the clock source that you'
        },
        'lv_property': 'Instrument:Obsolete:Ref Clock Source',
        'name': 'REF_CLOCK_SOURCE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1250003: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'This channel-based attribute specifies whether the signal that the signal generator produces appears at the output connector.'
        },
        'lv_property': 'Output:Output Enabled',
        'name': 'OUTPUT_ENABLED',
        'resettable': True,
        'type': 'ViBoolean'
    },
    1250004: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'This channel-based attribute specifies the signal generator output impedance at the output connector. NI signal sources modules have an output impedance of 50 ohms and an optional 75 ohms on select modules. If the load impedance matches the output impedance, then the voltage at the signal output connector is at the needed level. The voltage at the signal output connector varies with load output impedance, up to doubling the voltage for a high-impedance load.'
        },
        'lv_property': 'Output:Output Impedance',
        'name': 'OUTPUT_IMPEDANCE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250005: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies how the signal generator produces waveforms.  Currently only continuous mode is valid for NI signal generators.  To control trigger mode, use NIFGEN_ATTR_TRIGGER_MODE instead.\n'
        },
        'enum': 'OperationMode',
        'lv_property': 'Instrument:Obsolete:Operation Mode',
        'name': 'OPERATION_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250101: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nThis channel-based attribute specifies which standard waveform the signal generator produces.\nUse this attribute only when NIFGEN_ATTR_OUTPUT_MODE is set to  NIFGEN_VAL_OUTPUT_FUNC.\nNIFGEN_VAL_WFM_SINE      - Sinusoid waveform\nNIFGEN_VAL_WFM_SQUARE    - Square waveform\nNIFGEN_VAL_WFM_TRIANGLE  - Triangle waveform\nNIFGEN_VAL_WFM_RAMP_UP   - Positive ramp waveform\nNIFGEN_VAL_WFM_RAMP_DOWN - Negative ramp waveform\nNIFGEN_VAL_WFM_DC        - Constant voltage\nNIFGEN_VAL_WFM_NOISE     - White noise\nNIFGEN_VAL_WFM_USER      - User-defined waveform as defined with\nniFgen_DefineUserStandardWaveform\n'
        },
        'enum': 'Waveform',
        'lv_property': 'Standard Function:Waveform',
        'name': 'FUNC_WAVEFORM',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250102: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nControls the amplitude of the standard waveform that the  signal generator produces. This value is the amplitude at the  output terminal.\nFor example, to produce a waveform ranging from -5.00 V to +5.00 V, set  the amplitude to 10.00 V.\nset the Waveform parameter to NIFGEN_VAL_WFM_DC.\nUnits: Vpk-pk\n',
            'note': 'This parameter does not affect signal generator behavior when you'
        },
        'lv_property': 'Standard Function:Amplitude',
        'name': 'FUNC_AMPLITUDE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250103: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nControls the DC offset of the standard waveform that the  signal generator produces.  This value is the offset at the output  terminal. The value is the offset from ground to the center of the  waveform that you specify with the Waveform parameter.\nFor example, to configure a waveform with an amplitude of 10.00 V to  range from 0.00 V to +10.00 V, set DC Offset to 5.00 V.\nUnits: volts\n'
        },
        'lv_property': 'Standard Function:DC Offset',
        'name': 'FUNC_DC_OFFSET',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250104: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nControls the frequency of the standard waveform that the  signal generator produces.\nUnits: hertz\n(1) This parameter does not affect signal generator behavior when you  set the Waveform parameter of the niFgen_ConfigureStandardWaveform function  to NIFGEN_VAL_WFM_DC.\n(2) For NIFGEN_VAL_WFM_SINE, the range is between 0 MHz and 16 MHz, but the  range is between 0 MHz and 1 MHz for all other waveforms.\n',
            'note': '\n:\n'
        },
        'lv_property': 'Standard Function:Standard Function Mode:Frequency',
        'name': 'FUNC_FREQUENCY',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250105: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nControls horizontal offset of the standard waveform the  signal generator produces. Specify this attribute in degrees of  one waveform cycle.\nA start phase of 180 degrees means output generation begins halfway  through the waveform. A start phase of 360 degrees offsets the output by  an entire waveform cycle, which is identical to a start phase of 0  degrees.\nset the Waveform parameter to NIFGEN_VAL_WFM_DC.\nUnits: Degrees of one cycle\n',
            'note': 'This parameter does not affect signal generator behavior when you'
        },
        'lv_property': 'Standard Function:Start Phase',
        'name': 'FUNC_START_PHASE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250106: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nControls the duty cycle of the square wave the signal generator  produces. Specify this attribute as a percentage of  the time the square wave is high in a cycle.\nset the Waveform parameter to NIFGEN_VAL_WFM_SQUARE.\nUnits: Percentage of time the waveform is high\n',
            'note': 'This parameter only affects signal generator behavior when you'
        },
        'lv_property': 'Standard Function:Duty Cycle High',
        'name': 'FUNC_DUTY_CYCLE_HIGH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250201: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSelects which arbitrary waveform the signal generator produces. You can create multiple arbitrary waveforms using one of the following niFgen Create Waveform functions:\nniFgen_CreateWaveformF64\nniFgen_CreateWaveformI16\nniFgen_CreateWaveformFromFileI16\nniFgen_CreateWaveformFromFileF64\nniFgen_CreateWaveformFromFileHWS\nThese functions return a handle that you can use to identify the particular waveform. To configure the signal generator to produce a particular waveform, set this attribute to the waveform handle.\nUse this attribute only when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB.\n'
        },
        'lv_property': 'Arbitrary Waveform:Arbitrary Waveform Mode:Arbitrary Waveform Handle',
        'name': 'ARB_WAVEFORM_HANDLE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250202: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the factor by which the signal generator scales the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this attribute to scale the arbitrary waveform to other ranges.\nFor example, when you set this attribute to 2.0, the output signal ranges from -2.0 V to +2.0 V.\nUse this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB or NIFGEN_VAL_OUTPUT_SEQ.\n'
        },
        'lv_property': 'Arbitrary Waveform:Gain',
        'name': 'ARB_GAIN',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250203: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the value that the signal generator adds to the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this attribute to shift the arbitrary waveform range.\nFor example, when you set this attribute to 1.0, the output signal ranges from 2.0 V to 0.0 V.\nUse this attribute when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_ARB or NIFGEN_VAL_OUTPUT_SEQ.\nUnits: Volts\n'
        },
        'lv_property': 'Arbitrary Waveform:Offset',
        'name': 'ARB_OFFSET',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250204: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the rate at which the signal generator outputs the points in arbitrary waveforms.  Use this attribute when NIFGEN_ATTR_OUTPUT_MODE is set  to NIFGEN_VAL_OUTPUT_ARB or NIFGEN_VAL_OUTPUT_SEQ.\nUnits: Samples/s\n'
        },
        'lv_property': 'Clocks:Sample Clock:Rate',
        'name': 'ARB_SAMPLE_RATE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1250205: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the maximum number of arbitrary waveforms that the signal generator allows. Typically, this value is constant for the signal generator.'
        },
        'lv_property': 'Arbitrary Waveform:Capabilities:Max Number of Waveforms',
        'name': 'MAX_NUM_WAVEFORMS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250206: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nThe size of each arbitrary waveform must be a multiple of a quantum value. This attribute returns the quantum value that the signal generator allows.\nFor example, when this attribute returns a value of 8, all waveform sizes must be a multiple of 8. Typically, this value is constant for the signal generator.\n'
        },
        'lv_property': 'Arbitrary Waveform:Capabilities:Waveform Quantum',
        'name': 'WAVEFORM_QUANTUM',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250207: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the minimum number of points that the signal generator allows in an arbitrary waveform. Typically, this value is constant for the signal generator.'
        },
        'lv_property': 'Arbitrary Waveform:Capabilities:Min Waveform Size',
        'name': 'MIN_WAVEFORM_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250208: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the size, in samples, of the largest waveform that can be created. This attribute reflects the space currently available, taking into account previously allocated waveforms and instructions.'
        },
        'lv_property': 'Arbitrary Waveform:Capabilities:Max Waveform Size',
        'name': 'MAX_WAVEFORM_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250211: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nThis channel-based attribute identifies which sequence the signal generator produces. You can create multiple sequences using niFgen_CreateArbSequence. niFgen_CreateArbSequence returns a handle that you can use to identify the particular sequence. To configure the signal generator to produce a particular sequence, set this attribute to the sequence handle.\nUse this attribute only when NIFGEN_ATTR_OUTPUT_MODE is set to NIFGEN_VAL_OUTPUT_SEQ.\n'
        },
        'lv_property': 'Arbitrary Waveform:Arbitrary Sequence Mode:Arbitrary Sequence Handle',
        'name': 'ARB_SEQUENCE_HANDLE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250212: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the maximum number of arbitrary sequences that the signal generator allows. Typically, this value is constant for the signal generator.'
        },
        'lv_property': 'Arbitrary Waveform:Arbitrary Sequence Mode:Max Number of Sequences',
        'name': 'MAX_NUM_SEQUENCES',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250213: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the minimum number of arbitrary waveforms that the signal generator allows in a sequence. Typically, this value is constant for the signal generator.'
        },
        'lv_property': 'Arbitrary Waveform:Arbitrary Sequence Mode:Min Sequence Length',
        'name': 'MIN_SEQUENCE_LENGTH',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250214: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the maximum number of arbitrary waveforms that the signal generator allows in a sequence. Typically, this value is constant for the signal generator.'
        },
        'lv_property': 'Arbitrary Waveform:Arbitrary Sequence Mode:Max Sequence Length',
        'name': 'MAX_SEQUENCE_LENGTH',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250215: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Returns the maximum number of times that the signal generator can repeat a waveform in a sequence. Typically, this value is constant for the signal generator.'
        },
        'lv_property': 'Arbitrary Waveform:Arbitrary Sequence Mode:Max Loop Count',
        'name': 'MAX_LOOP_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250302: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nControls which trigger source the signal generator uses.\nAfter you call the niFgen_InitiateGeneration function, the signal generator waits for the trigger that you specify in the triggerSource parameter. After the signal generator receives a trigger, it produces the number of cycles that you specify in the NIFGEN_ATTR_CYCLE_COUNT attribute.\nThis attribute is also the source for the trigger in the other trigger modes as specified by the NIFGEN_ATTR_TRIGGER_MODE attribute.\n'
        },
        'enum': 'TriggerSource',
        'lv_property': 'Instrument:5401/5411/5431:Trigger Source',
        'name': 'TRIGGER_SOURCE',
        'resettable': True,
        'type': 'ViInt32'
    },
    1250350: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the number of cycles that you want the signal generator to produce after it receives a trigger./n For standard and arbitrary waveforms, a cycle is one period of the waveform./n An arbitrary sequence consists of multiple arbitrary waveforms in a sequence. Each waveform can be repeated a discrete number of times before the next waveform is produced. For arbitrary sequences, a cycle is one complete progression through the generation of all iterations of all waveforms in the sequence./n/n',
            'note': 'The NI 5411/5421 arbitrary waveform generators support only continuous generation./n'
        },
        'lv_property': '',
        'name': 'CYCLE_COUNT',
        'resettable': True,
        'type': 'ViInt32'
    }
}
