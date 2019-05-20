# -*- coding: utf-8 -*-
# This file is generated from API metadata for NI-SCOPE version 19.1.0d28
attributes = {
    1050002: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies whether to validate attribute values and function parameters.   If enabled, the instrument driver validates the parameters values that you  pass to driver functions.  Range checking parameters is very useful for  debugging.  After you validate your program, you can set this attribute to  VI_FALSE to disable range checking and maximize performance.\nThe default value is VI_TRUE.   Use the niScope_InitWithOptions  function to override this value.\n'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Range Check',
        'name': 'RANGE_CHECK',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050003: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies whether the instrument driver queries the instrument status  after each operation.  Querying the instrument status is very useful for  debugging.  After you validate your program, you can set this attribute to  VI_FALSE to disable status checking and maximize performance\nThe instrument driver can choose to ignore status checking for  particular attributes regardless of the setting of this attribute.\nThe default value is VI_TRUE.   Use the niScope_InitWithOptions  function to override this value.\n'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Query Instrument Status',
        'name': 'QUERY_INSTRUMENT_STATUS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050004: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies whether to cache the value of attributes.  When caching is  enabled, the instrument driver keeps track of the current instrument  settings and avoids sending redundant commands to the instrument.  Thus,  you can significantly increase execution speed.\nThe instrument driver can choose to always cache or to never cache  particular attributes regardless of the setting of this attribute.\nThe default value is VI_TRUE.   Use niScope_InitWithOptions  to override this value.\n'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Cache',
        'name': 'CACHE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050005: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies whether or not to simulate instrument driver I/O operations.  If  simulation is enabled, instrument driver functions perform range checking  and call Ivi_GetAttribute and Ivi_SetAttribute functions, but they do not  perform instrument I/O.  For output parameters that represent instrument  data, the instrument driver functions return calculated values.\nThe default value is VI_FALSE.   Use the niScope_InitWithOptions  function to override this value.\n'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Simulate',
        'name': 'SIMULATE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050006: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies whether the IVI engine keeps a list of the value coercions it  makes for ViInt32 and ViReal64 attributes.  You call  Ivi_GetNextCoercionInfo to extract and delete the oldest coercion record  from the list.\nThe default value is VI_FALSE.   Use the niScope_InitWithOptions  function to override this value.\n'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Record Value Coercions',
        'name': 'RECORD_COERCIONS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050007: {
        'access': 'read only',
        'channel_based': True,
        'documentation': {
            'description': '\nThis attribute indicates the Driver Setup string that the user  specified when initializing the driver.\nSome cases exist where the end-user must specify instrument driver  options at initialization.  An example of this is specifying  a particular instrument model from among a family of instruments  that the driver supports.  This is useful when using simulation.   The end-user can specify driver-specific options through  the DriverSetup keyword in the optionsString parameter in  niScope_InitWithOptions, or through the IVI Configuration Utility.\nIf the user does not specify a Driver Setup string, this attribute returns an empty string.\n'
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
            'description': '\nNI-SCOPE does not generate interchange warnings and therefore ignores this attribute.\n'
        },
        'lv_property': 'Inherent IVI Attributes:User Options:Interchange Check',
        'name': 'INTERCHANGE_CHECK',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1050203: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nIndicates the number of channels that the specific instrument driver  supports.\nFor channel-based properties, the IVI engine maintains a separate cache value for each channel.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Channel Count',
        'name': 'CHANNEL_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050302: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nA string that contains the prefix for the instrument driver. The name of each user-callable  function in this driver starts with this prefix.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Driver Prefix',
        'name': 'SPECIFIC_DRIVER_PREFIX',
        'resettable': False,
        'type': 'ViString'
    },
    1050304: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nIndicates the resource descriptor the driver uses to identify the physical device.  If you initialize the driver with a logical name, this attribute contains the resource descriptor  that corresponds to the entry in the IVI Configuration utility.\nIf you initialize the instrument driver with the resource descriptor, this attribute contains that  value.You can pass a logical name to niScope_Init or niScope_InitWithOptions. The IVI Configuration  utility must contain an entry for the logical name. The logical name entry refers to a virtual  instrument section in the IVI Configuration file. The virtual instrument section specifies a physical  device and initial user options.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Resource Descriptor',
        'name': 'IO_RESOURCE_DESCRIPTOR',
        'resettable': False,
        'type': 'ViString'
    },
    1050305: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nA string containing the logical name you specified when opening the current IVI session.  You can pass a logical name to niScope_Init or niScope_InitWithOptions. The IVI Configuration  utility must contain an entry for the logical name. The logical name entry refers to a virtual  instrument section in the IVI Configuration file. The virtual instrument section specifies a physical  device and initial user options.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Advanced Session Information:Logical Name',
        'name': 'LOGICAL_NAME',
        'resettable': False,
        'type': 'ViString'
    },
    1050327: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nA string that contains a comma-separated list of the instrument model numbers supported by this driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Supported Instrument Models',
        'name': 'SUPPORTED_INSTRUMENT_MODELS',
        'resettable': False,
        'type': 'ViString'
    },
    1050401: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nA string that contains a comma-separated list of class extension groups that this driver implements.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Capabilities:Class Group Capabilities',
        'name': 'GROUP_CAPABILITIES',
        'resettable': False,
        'type': 'ViString'
    },
    1050510: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nA string that contains the firmware revision information  for the instrument you are currently using.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Firmware Revision',
        'name': 'INSTRUMENT_FIRMWARE_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1050511: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nA string that contains the name of the instrument manufacturer.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Manufacturer',
        'name': 'INSTRUMENT_MANUFACTURER',
        'resettable': False,
        'type': 'ViString'
    },
    1050512: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nA string that contains the model number of the current instrument.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Instrument Identification:Model',
        'name': 'INSTRUMENT_MODEL',
        'resettable': False,
        'type': 'ViString'
    },
    1050513: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nA string that contains the name of the vendor that supplies this driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Driver Vendor',
        'name': 'SPECIFIC_DRIVER_VENDOR',
        'resettable': False,
        'type': 'ViString'
    },
    1050514: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nA string that contains a brief description of the specific  driver\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Description',
        'name': 'SPECIFIC_DRIVER_DESCRIPTION',
        'resettable': False,
        'type': 'ViString'
    },
    1050515: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThe major version number of the class specification with which this driver is compliant.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Class Specification Major Version',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050516: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThe minor version number of the class specification with which this driver is compliant.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Class Specification Minor Version',
        'name': 'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1050551: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nA string that contains additional version information about this  instrument driver.\n'
        },
        'lv_property': 'Inherent IVI Attributes:Driver Identification:Revision',
        'name': 'SPECIFIC_DRIVER_REVISION',
        'resettable': False,
        'type': 'ViString'
    },
    1150001: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the number of records to acquire. Can be used for multi-record acquisition  and single-record acquisitions. Setting this to 1 indicates a single-record acquisition.\n'
        },
        'lv_property': 'Horizontal:Number of Records',
        'name': 'HORZ_NUM_RECORDS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150002: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the input source for the PLL reference clock (the 1 MHz to 20 MHz clock on the NI 5122, the 10 MHz clock  for the NI 5112/5620/5621/5911) to which the digitizer will be phase-locked; for the NI 5102, this is the source  of the board clock.\n'
        },
        'lv_property': 'Clocking:Reference (Input) Clock Source',
        'name': 'INPUT_CLOCK_SOURCE',
        'resettable': False,
        'type': 'ViString'
    },
    1150003: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': "\nSpecifies the output source for the 10 MHz clock to which another digitizer's sample clock can be phased-locked.\n"
        },
        'lv_property': 'Clocking:Output Clock Source',
        'name': 'OUTPUT_CLOCK_SOURCE',
        'resettable': False,
        'type': 'ViString'
    },
    1150004: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nIndicates whether the digitizer enforces real-time measurements  or allows equivalent-time measurements.\n'
        },
        'lv_property': 'Horizontal:Enforce Realtime',
        'name': 'HORZ_ENFORCE_REALTIME',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150005: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nIndicates the bit width of the binary data in the acquired waveform.  Useful for determining which Binary Fetch function to use. Compare to NISCOPE_ATTR_RESOLUTION.\nTo configure the device to store samples with a lower resolution that the native, set this attribute to the desired binary width.\nThis can be useful for streaming at faster speeds at the cost of resolution. The least significant bits will be lost with this configuration.\nValid Values: 8, 16, 32\n'
        },
        'lv_property': 'Acquisition:Binary Sample Width',
        'name': 'BINARY_SAMPLE_WIDTH',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150006: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': 'Specifies the size of the hysteresis window on either side of the trigger level.  The digitizer triggers when the trigger signal passes through the threshold you specify  with the Trigger Level parameter, has the slope you specify with the Trigger Slope parameter,  and passes through the hysteresis window that you specify with this parameter.'
        },
        'lv_property': 'Triggering:Trigger Hysteresis',
        'name': 'TRIGGER_HYSTERESIS',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150007: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nFor the NI 5102, specifies the line on which the sample clock is sent or received. For the NI 5112/5620/5621/5911,  specifies the line on which the one-time sync pulse is sent or received. This line should be the same for all devices to be synchronized.\n'
        },
        'lv_property': 'Clocking:Clock Sync Pulse Source',
        'name': 'CLOCK_SYNC_PULSE_SOURCE',
        'resettable': False,
        'type': 'ViString'
    },
    1150008: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies whether you want the device to be a master or a slave. The master typically originates  the trigger signal and clock sync pulse. For a standalone device, set this attribute to VI_FALSE.\n'
        },
        'lv_property': 'Synchronization:Master Enable',
        'name': 'MASTER_ENABLE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150009: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecify the sampling rate for the acquisition in Samples per second.\nValid Values:\nThe combination of sampling rate and min record length must allow the  digitizer to sample at a valid sampling rate for the acquisition type specified  in niScope_ConfigureAcquisition and not require more memory than the  onboard memory module allows.\n'
        },
        'lv_property': 'Horizontal:Min Sample Rate',
        'name': 'MIN_SAMPLE_RATE',
        'resettable': True,
        'type': 'ViReal64'
    },
    1150012: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies whether you want a trigger to occur when the signal enters or leaves the window specified by  NISCOPE_ATTR_TRIGGER_WINDOW_LOW_LEVEL, or NISCOPE_ATTR_TRIGGER_WINDOW_HIGH_LEVEL.\n'
        },
        'enum': 'TriggerWindowMode',
        'lv_property': 'Triggering:Trigger Window:Window Mode',
        'name': 'TRIGGER_WINDOW_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150013: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nPass the lower voltage threshold you want the digitizer to use for  window triggering.\nThe digitizer triggers when the trigger signal enters or leaves  the window you specify with NISCOPE_ATTR_TRIGGER_WINDOW_LOW_LEVEL and NISCOPE_ATTR_TRIGGER_WINDOW_HIGH_LEVEL.\nUnits: Volts\nValid Values:\nThe values of the Vertical Range and Vertical Offset parameters in  niScope_ConfigureVertical determine the valid range for the  Low Window Level on the channel you use as the Trigger Source parameter  in niScope_ConfigureTriggerSource.  The value you pass for this parameter  must meet the following conditions.\nLow Trigger Level <= Vertical Range/2 + Vertical Offset\nLow Trigger Level >= (-Vertical Range/2) + Vertical Offset\nLow Trigger Level < High Trigger Level\n'
        },
        'lv_property': 'Triggering:Trigger Window:Low Level',
        'name': 'TRIGGER_WINDOW_LOW_LEVEL',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150014: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nPass the upper voltage threshold you want the digitizer to use for  window triggering.\nThe digitizer triggers when the trigger signal enters or leaves  the window you specify with NISCOPE_ATTR_TRIGGER_WINDOW_LOW_LEVEL and NISCOPE_ATTR_TRIGGER_WINDOW_HIGH_LEVEL\nValid Values:\nThe values of the Vertical Range and Vertical Offset parameters in  niScope_ConfigureVertical determine the valid range for the  High Window Level on the channel you use as the Trigger Source parameter  in niScope_ConfigureTriggerSource.  The value you pass for this parameter  must meet the following conditions.\nHigh Trigger Level <= Vertical Range/2 + Vertical Offset\nHigh Trigger Level >= (-Vertical Range/2) + Vertical Offset\nHigh Trigger Level > Low Trigger Level\n'
        },
        'lv_property': 'Triggering:Trigger Window:High Level',
        'name': 'TRIGGER_WINDOW_HIGH_LEVEL',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150016: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSpecifies the units of the reference levels.\nNISCOPE_VAL_MEAS_VOLTAGE--Specifies that the reference levels are given in units of volts\nNISCOPE_VAL_MEAS_PERCENTAGE--Percentage units, where the measurements voltage low and voltage high represent 0% and 100%, respectively.\nDefault: NISCOPE_VAL_MEAS_PERCENTAGE\n'
        },
        'enum': 'RefLevelUnits',
        'lv_property': 'Waveform Measurement:Reference Levels:Units',
        'name': 'MEAS_REF_LEVEL_UNITS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150018: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'private',
        'documentation': {
            'description': "\nSpecifies the second channel for two-channel measurements, such as NISCOPE_VAL_ADD_CHANNELS. If processing steps are registered with this channel, the processing is done before the waveform is used in a two-channel measurement.\nDefault: '0'\n"
        },
        'lv_property': 'Waveform Measurement:Other Channel',
        'name': 'MEAS_OTHER_CHANNEL',
        'resettable': False,
        'type': 'ViString'
    },
    1150019: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nDigital hysteresis that is used in several of the scalar waveform measurements. This attribute specifies the percentage of the full-scale vertical range for the hysteresis window size.\nDefault: 2%\n'
        },
        'lv_property': 'Waveform Measurement:Hysteresis Percent',
        'name': 'MEAS_HYSTERESIS_PERCENT',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150020: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSpecifies the size (that is, the number of bins) in the last acquisition histogram. This histogram is used to determine several scalar measurements, most importantly voltage low and voltage high.\nDefault: 256\n'
        },
        'lv_property': 'Waveform Measurement:Last Acq. Histogram Size',
        'name': 'MEAS_LAST_ACQ_HISTOGRAM_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150021: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nDetermines the multiple acquisition voltage histogram size. The size is set the first time a voltage histogram measurement is called after clearing the measurement history with the function niScope_ClearWaveformMeasurementStats.\nDefault: 256\n'
        },
        'lv_property': 'Waveform Measurement:Voltage Histogram:Size',
        'name': 'MEAS_VOLTAGE_HISTOGRAM_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150022: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSpecifies the lowest voltage value included in the multiple-acquisition voltage histogram. The units are always volts.\nDefault: -10.0 V\n'
        },
        'lv_property': 'Waveform Measurement:Voltage Histogram:Low Volts',
        'name': 'MEAS_VOLTAGE_HISTOGRAM_LOW_VOLTS',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150023: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSpecifies the highest voltage value included in the multiple acquisition voltage histogram. The units are always volts.\nDefault: 10.0 V\n'
        },
        'lv_property': 'Waveform Measurement:Voltage Histogram:High Volts',
        'name': 'MEAS_VOLTAGE_HISTOGRAM_HIGH_VOLTS',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150024: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nDetermines the multiple acquisition voltage histogram size. The size is set during the first call to a time histogram measurement after clearing the measurement history with niScope_ClearWaveformMeasurementStats.\nDefault: 256\n'
        },
        'lv_property': 'Waveform Measurement:Time Histogram:Size',
        'name': 'MEAS_TIME_HISTOGRAM_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150025: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSpecifies the lowest voltage value included in the multiple acquisition time histogram. The units are always volts.\nDefault: -10.0 V\n'
        },
        'lv_property': 'Waveform Measurement:Time Histogram:Low Volts',
        'name': 'MEAS_TIME_HISTOGRAM_LOW_VOLTS',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150026: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSpecifies the highest voltage value included in the multiple-acquisition time histogram. The units are always volts.\nDefault: 10.0 V\n'
        },
        'lv_property': 'Waveform Measurement:Time Histogram:High Volts',
        'name': 'MEAS_TIME_HISTOGRAM_HIGH_VOLTS',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150027: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSpecifies the lowest time value included in the multiple-acquisition time histogram. The units are always seconds.\nDefault: -5.0e-4 seconds\n'
        },
        'lv_property': 'Waveform Measurement:Time Histogram:Low Time',
        'name': 'MEAS_TIME_HISTOGRAM_LOW_TIME',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150028: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSpecifies the highest time value included in the multiple acquisition time histogram. The units are always seconds.\nDefault: 5.0e-4 seconds\n'
        },
        'lv_property': 'Waveform Measurement:Time Histogram:High Time',
        'name': 'MEAS_TIME_HISTOGRAM_HIGH_TIME',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150029: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSpecifies the polynomial order used for the polynomial interpolation measurement. For example, an order of 1 is linear interpolation whereas an order of 2 specifies parabolic interpolation. Any positive integer is valid.\nDefault: 1\n'
        },
        'lv_property': 'Waveform Measurement:Interpolation:Polynomial Interpolation Order',
        'name': 'MEAS_POLYNOMIAL_INTERPOLATION_ORDER',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150030: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThe new number of points for polynomial interpolation is the sampling factor times the input number of points. For example, if you acquire 1,000 points with the digitizer and set this attribute to 2.5, calling niScope_FetchWaveformMeasurementArray with the NISCOPE_VAL_POLYNOMIAL_INTERPOLATION measurement resamples the waveform to 2,500 points.\nDefault: 2.0\n'
        },
        'lv_property': 'Waveform Measurement:Interpolation:Sampling Factor',
        'name': 'MEAS_INTERPOLATION_SAMPLING_FACTOR',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150031: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSpecifies the cutoff frequency in hertz for filters of type lowpass and highpass. The cutoff frequency definition varies depending on the filter.\nDefault: 1.0e6 Hz\n'
        },
        'lv_property': 'Waveform Measurement:Filter:Cutoff Frequency',
        'name': 'MEAS_FILTER_CUTOFF_FREQ',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150032: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThe center frequency in hertz for filters of type bandpass and bandstop. The width of the filter is specified by NISCOPE_ATTR_MEAS_FILTER_WIDTH, where the cutoff frequencies are the center ± width.\nDefault: 1.0e6 Hz\n'
        },
        'lv_property': 'Waveform Measurement:Filter:Center Frequency',
        'name': 'MEAS_FILTER_CENTER_FREQ',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150033: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSpecifies the amount of ripple in the passband in units of decibels (positive values). Used only for Chebyshev filters. The more ripple allowed gives a sharper cutoff for a given filter order.\nDefault: 0.1 dB\n'
        },
        'lv_property': 'Waveform Measurement:Filter:Ripple',
        'name': 'MEAS_FILTER_RIPPLE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150034: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThe percentage (0 - 100%) of the IIR filtered waveform to eliminate from the beginning of the waveform. This allows eliminating the transient portion of the waveform that is undefined due to the assumptions necessary at the boundary condition.\nDefault: 20.0%\n'
        },
        'lv_property': 'Waveform Measurement:Filter:Percent Waveform Transient',
        'name': 'MEAS_FILTER_TRANSIENT_WAVEFORM_PERCENT',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150035: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSpecifies the type of filter, for both IIR and FIR filters. The allowed values are the following:\n·  NISCOPE_VAL_MEAS_LOWPASS\n·  NISCOPE_VAL_MEAS_HIGHPASS\n·  NISCOPE_VAL_MEAS_BANDPASS\n·  NISCOPE_VAL_MEAS_BANDSTOP\nDefault: NISCOPE_VAL_MEAS_LOWPASS\n'
        },
        'enum': 'FilterType',
        'lv_property': 'Waveform Measurement:Filter:Type',
        'name': 'MEAS_FILTER_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150036: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSpecifies the order of an IIR filter. All positive integers are valid.\nDefault: 2\n'
        },
        'lv_property': 'Waveform Measurement:Filter:IIR Order',
        'name': 'MEAS_FILTER_ORDER',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150037: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nDefines the number of taps (coefficients) for an FIR filter.\nDefault: 25\n'
        },
        'lv_property': 'Waveform Measurement:Filter:FIR Taps',
        'name': 'MEAS_FILTER_TAPS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150038: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nStores the low reference level used in many scalar measurements. Different channels  may have different reference levels. Do not use the IVI-defined, nonchannel-based attributes such as  NISCOPE_ATTR_MEAS_LOW_REF if you use this attribute to set various channels to different values.\nDefault: 10%\n'
        },
        'lv_property': 'Waveform Measurement:Reference Levels:Channel Based Low Ref Level',
        'name': 'MEAS_CHAN_LOW_REF_LEVEL',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150039: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nStores the mid reference level used in many scalar measurements. Different channels  may have different reference levels. Do not use the IVI-defined, nonchannel-based attributes such as  NISCOPE_ATTR_MEAS_MID_REF if you use this attribute to set various channels to different values.\nDefault: 50%\n'
        },
        'lv_property': 'Waveform Measurement:Reference Levels:Channel Based Mid Ref Level',
        'name': 'MEAS_CHAN_MID_REF_LEVEL',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150040: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nStores the high reference level used in many scalar measurements. Different channels may have different reference  levels. Do not use the IVI-defined, nonchannel-based attributes such as NISCOPE_ATTR_MEAS_HIGH_REF if you use  this attribute to set various channels to different values.\nDefault: 90%\n'
        },
        'lv_property': 'Waveform Measurement:Reference Levels:Channel Based High Ref Level',
        'name': 'MEAS_CHAN_HIGH_REF_LEVEL',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150041: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSpecifies the width of bandpass and bandstop type filters in hertz. The cutoff frequencies occur at NISCOPE_ATTR_MEAS_FILTER_CENTER_FREQ ± one-half width.\nDefault: 1.0e3 Hz\n'
        },
        'lv_property': 'Waveform Measurement:Filter:Width',
        'name': 'MEAS_FILTER_WIDTH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150042: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSpecifies the FIR window type. The possible choices are:\nNISCOPE_VAL_NONE\nNISCOPE_VAL_HANNING_WINDOW\nNISCOPE_VAL_HAMMING_WINDOW\nNISCOPE_VAL_TRIANGLE_WINDOW\nNISCOPE_VAL_FLAT_TOP_WINDOW\nNISCOPE_VAL_BLACKMAN_WINDOW\nThe symmetric windows are applied to the FIR filter coefficients to limit passband ripple in FIR filters.\nDefault: NISCOPE_VAL_NONE\n'
        },
        'enum': 'FIRFilterWindow',
        'lv_property': 'Waveform Measurement:Filter:FIR Window',
        'name': 'MEAS_FIR_FILTER_WINDOW',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150043: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nEvery element of an array is multiplied by this scalar value during the Array Gain measurement.  Refer to NISCOPE_VAL_ARRAY_GAIN for more information.\nDefault: 1.0\n'
        },
        'lv_property': 'Waveform Measurement:Array Gain',
        'name': 'MEAS_ARRAY_GAIN',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150044: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nEvery element of an array is added to this scalar value during the Array Offset measurement. Refer to NISCOPE_VAL_ARRAY_OFFSET for more information.\nDefault: 0.0\n'
        },
        'lv_property': 'Waveform Measurement:Array Offset',
        'name': 'MEAS_ARRAY_OFFSET',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150045: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSpecifies the method used to map percentage reference units to voltages for the reference. Possible values are:\nNISCOPE_VAL_MEAS_LOW_HIGH\nNISCOPE_VAL_MEAS_MIN_MAX\nNISCOPE_VAL_MEAS_BASE_TOP\nDefault: NISCOPE_VAL_MEAS_BASE_TOP\n'
        },
        'enum': 'PercentageMethod',
        'lv_property': 'Waveform Measurement:Reference Levels:Percentage Units Method',
        'name': 'MEAS_PERCENTAGE_METHOD',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150046: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the delay for the trigger from the master to the slave in seconds.  This value adjusts the initial X value of the slave devices to correct for the  propagation delay between the master trigger output and slave trigger input.\n'
        },
        'lv_property': 'Synchronization:Trigger Calibration Delay:Slave Trigger Delay',
        'name': 'SLAVE_TRIGGER_DELAY',
        'resettable': False,
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1150047: {
        'access': 'read only',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis is a factory-programmed value that specifies the delay for the trigger  to the PXI Star Trigger line in seconds.  By itself, this attribute has no  effect on the acquired data.  However, depending on how the trigger lines  are routed between the master and slave devices, you can use this value as  a starting point to set NISCOPE_ATTR_SLAVE_TRIGGER_DELAY.\n'
        },
        'lv_property': 'Synchronization:Trigger Calibration Delay:Trigger to Star Delay',
        'name': 'TRIGGER_TO_STAR_DELAY',
        'resettable': False,
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1150048: {
        'access': 'read only',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis is a factory-programmed value that specifies the delay for the trigger  to the RTSI bus in seconds.  By itself, this attribute has no effect on the  acquired data.  However, depending on how the trigger lines are routed between  the master and slave devices, you can use this value as a starting point to set   NISCOPE_ATTR_SLAVE_TRIGGER_DELAY.\n'
        },
        'lv_property': 'Synchronization:Trigger Calibration Delay:Trigger to RTSI Delay',
        'name': 'TRIGGER_TO_RTSI_DELAY',
        'resettable': False,
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1150049: {
        'access': 'read only',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis is a factory-programmed value that specifies the delay for the trigger  to the PFI lines in seconds.  By itself, this attribute has no effect on the  acquired data.  However, depending on how the trigger lines are routed between  the master and slave devices, you can use this value as a starting point to set  NISCOPE_ATTR_SLAVE_TRIGGER_DELAY.\n'
        },
        'lv_property': 'Synchronization:Trigger Calibration Delay:Trigger to PFI Delay',
        'name': 'TRIGGER_TO_PFI_DELAY',
        'resettable': False,
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1150050: {
        'access': 'read only',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis is a factory-programmed value that specifies the delay for PXI Star  Trigger line to the trigger input in seconds.  By itself, this attribute  has no effect on the acquired data.  However, depending on how the trigger  lines are routed between the master and slave devices, you can use this value  as a starting point to set NISCOPE_ATTR_SLAVE_TRIGGER_DELAY.\n'
        },
        'lv_property': 'Synchronization:Trigger Calibration Delay:Trigger from Star Delay',
        'name': 'TRIGGER_FROM_STAR_DELAY',
        'resettable': False,
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1150051: {
        'access': 'read only',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis is a factory-programmed value that specifies the delay for the RTSI bus  to the trigger input in seconds.  By itself, this attribute has no effect on  the acquired data.  However, depending on how the trigger lines are routed  between the master and slave devices, you can use this value as a starting point  to set NISCOPE_ATTR_SLAVE_TRIGGER_DELAY.\n'
        },
        'lv_property': 'Synchronization:Trigger Calibration Delay:Trigger from RTSI Delay',
        'name': 'TRIGGER_FROM_RTSI_DELAY',
        'resettable': False,
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1150052: {
        'access': 'read only',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis is a factory-programmed value that specifies the delay for the PFI lines  to the trigger input in seconds.  By itself, this attribute has no effect on  the acquired data.  However, depending on how the trigger lines are routed  between the master and slave devices, you can use this value as a starting  point to set NISCOPE_ATTR_SLAVE_TRIGGER_DELAY.\n'
        },
        'lv_property': 'Synchronization:Trigger Calibration Delay:Trigger from PFI Delay',
        'name': 'TRIGGER_FROM_PFI_DELAY',
        'resettable': False,
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1150053: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': "\nSpecifies the source the digitizer monitors for a start (acquisition arm) trigger.   When the start trigger is received, the digitizer begins acquiring pretrigger  samples.\nValid Values:\nNISCOPE_VAL_IMMEDIATE     ('VAL_IMMEDIATE')    - Triggers immediately\nNISCOPE_VAL_RTSI_0        ('VAL_RTSI_0')       - RTSI 0\nNISCOPE_VAL_RTSI_1        ('VAL_RTSI_1')       - RTSI 1\nNISCOPE_VAL_RTSI_2        ('VAL_RTSI_2')       - RTSI 2\nNISCOPE_VAL_RTSI_3        ('VAL_RTSI_3')       - RTSI 3\nNISCOPE_VAL_RTSI_4        ('VAL_RTSI_4')       - RTSI 4\nNISCOPE_VAL_RTSI_5        ('VAL_RTSI_5')       - RTSI 5\nNISCOPE_VAL_RTSI_6        ('VAL_RTSI_6')       - RTSI 6\nNISCOPE_VAL_PFI_0         ('VAL_PFI_0')        - PFI 0\nNISCOPE_VAL_PFI_1         ('VAL_PFI_1')        - PFI 1\nNISCOPE_VAL_PFI_2         ('VAL_PFI_2')        - PFI 2\nNISCOPE_VAL_PXI_STAR      ('VAL_PXI_STAR')     - PXI Star Trigger\n"
        },
        'lv_property': 'Synchronization:Start Trigger (Acq. Arm):Source',
        'name': 'ACQ_ARM_SOURCE',
        'resettable': False,
        'type': 'ViString'
    },
    1150065: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the record arm source.\n'
        },
        'lv_property': 'Synchronization:Record Arm Source',
        'name': 'RECORD_ARM_SOURCE',
        'resettable': False,
        'type': 'ViString'
    },
    1150068: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nIndicates whether more records can be configured with niScope_ConfigureHorizontalTiming  than fit in the onboard memory. If this attribute is set to VI_TRUE, it is necessary  to fetch records while the acquisition is in progress.  Eventually, some of  the records will be overwritten.  An error is returned from the fetch function  if you attempt to fetch a record that has been overwritten.\n'
        },
        'lv_property': 'Horizontal:Enable Records > Memory',
        'name': 'ALLOW_MORE_RECORDS_THAN_MEMORY',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150069: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nReturns the total combined amount of onboard memory for all channels in bytes.\n'
        },
        'lv_property': 'Horizontal:Memory Size',
        'name': 'ONBOARD_MEMORY_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150070: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nThe number of averages for each bin in an RIS acquisition.  The number of averages  times the oversampling factor is the minimum number of real-time acquisitions  necessary to reconstruct the RIS waveform.  Averaging is useful in RIS because  the trigger times are not evenly spaced, so adjacent points in the reconstructed  waveform not be accurately spaced.  By averaging, the errors in both time and  voltage are smoothed.\n'
        },
        'lv_property': 'Horizontal:RIS Num Avg',
        'name': 'RIS_NUM_AVERAGES',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150071: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the algorithm for random-interleaved sampling, which is used if the sample rate exceeds the  value of NISCOPE_ATTR_MAX_REAL_TIME_SAMPLING_RATE.\n'
        },
        'enum': 'RISMethod',
        'lv_property': 'Horizontal:RIS Method',
        'name': 'RIS_METHOD',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150072: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSet to VI_TRUE to retrieve one array with alternating values on the NI 5620/5621.  For example, this attribute can be used to retrieve a single array with I and Q interleaved  instead of two separate arrays. If set to VI_TRUE, the resulting array will be twice the size of the actual record length.\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Fetch Interleaved Data',
        'name': 'FETCH_INTERLEAVED_DATA',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150073: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nReturns the maximum real time sample rate in Hz.\n'
        },
        'lv_property': 'Horizontal:Maximum Real Time Sample Rate',
        'name': 'MAX_REAL_TIME_SAMPLING_RATE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150074: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nReturns the maximum sample rate in RIS mode in Hz.\n'
        },
        'lv_property': 'Horizontal:Maximum RIS Rate',
        'name': 'MAX_RIS_RATE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150075: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the input impedance for the external analog trigger channel in Ohms.\nValid Values:\n50      - 50 ohms\n1000000 - 1 mega ohm\n'
        },
        'lv_property': 'Triggering:Trigger Impedance',
        'name': 'TRIGGER_IMPEDANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150076: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Indicates the device number associated with the current session.'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Device Number',
        'name': 'DEVICE_NUMBER',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150077: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nPosition to start fetching within one record.\nDefault Value: NISCOPE_VAL_PRETRIGGER\n'
        },
        'enum': 'FetchRelativeTo',
        'lv_property': 'Fetch:Fetch Relative To',
        'name': 'FETCH_RELATIVE_TO',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150078: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nOffset in samples to start fetching data within each record. The offset is applied relative to  NISCOPE_ATTR_FETCH_RELATIVE_TO.The offset can be positive or negative.\nDefault Value: 0\n'
        },
        'lv_property': 'Fetch:Fetch Offset',
        'name': 'FETCH_OFFSET',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150079: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nZero-based index of the first record to fetch.  Use NISCOPE_FETCH_NUM_RECORDS to set the number of records to fetch.\nDefault Value: 0.\n'
        },
        'lv_property': 'Fetch:Fetch Record Number',
        'name': 'FETCH_RECORD_NUMBER',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150080: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nNumber of records to fetch. Use -1 to fetch all configured records.\nDefault Value: -1\n'
        },
        'lv_property': 'Fetch:Fetch Number of Records',
        'name': 'FETCH_NUM_RECORDS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150081: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'private',
        'documentation': {
            'description': '\nNumber of samples to fetch when performing a measurement. Use -1 to fetch the actual record length.\nDefault Value: -1\n'
        },
        'lv_property': 'Fetch:Fetch Meas Num Samples',
        'name': 'FETCH_MEAS_NUM_SAMPLES',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150082: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nActual number of samples acquired in the record specified by NISCOPE_ATTR_FETCH_RECORD_NUMBER from the NISCOPE_ATTR_FETCH_RELATIVE_TO and NISCOPE_ATTR_FETCH_OFFSET attributes.\n'
        },
        'lv_property': 'Fetch:Points Done',
        'name': 'POINTS_DONE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150083: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the number of records that have been completely acquired.\n'
        },
        'lv_property': 'Fetch:Records Done',
        'name': 'RECORDS_DONE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150084: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nReturns the number of samples (NISCOPE_ATTR_POINTS_DONE) that have been acquired but not fetched  for the record specified by NISCOPE_ATTR_FETCH_RECORD_NUMBER.\n'
        },
        'lv_property': 'Fetch:Fetch Backlog',
        'name': 'BACKLOG',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150085: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nWhen set to true and the digitizer is set to master, the number of pretrigger samples  and total samples are adjusted to be able to synchronize a master and slave 5102.\n'
        },
        'lv_property': 'Horizontal:Advanced:5102 Adjust Pretrigger Samples',
        'name': '5102_ADJUST_PRETRIGGER_SAMPLES',
        'python_name': 'adjust_pretrigger_samples_5102',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150086: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nReturns the temperature of the device in degrees Celsius from the onboard sensor.\n'
        },
        'lv_property': 'Device:Temperature',
        'name': 'DEVICE_TEMPERATURE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150087: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the source of the sample clock timebase, which is the timebase used to control waveform sampling.  The actual sample rate may be the timebase itself or a divided version of the timebase, depending on the  NISCOPE_ATTR_MIN_SAMPLE_RATE (for internal sources) or the NISCOPE_ATTR_SAMP_CLK_TIMEBASE_DIV (for external sources).\n'
        },
        'lv_property': 'Clocking:Sample Clock Timebase Source',
        'name': 'SAMP_CLK_TIMEBASE_SRC',
        'resettable': False,
        'type': 'ViString'
    },
    1150088: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nIf NISCOPE_ATTR_SAMP_CLK_TIMEBASE_SRC is an external source, specifies the frequency in hertz of the external clock used as the timebase source.\n'
        },
        'lv_property': 'Clocking:Sample Clock Timebase Rate',
        'name': 'SAMP_CLK_TIMEBASE_RATE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150089: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nIf NISCOPE_ATTR_SAMP_CLK_TIMEBASE_SRC is an external source, specifies the ratio between the sample clock timebase rate and the actual sample rate, which can be slower.\n'
        },
        'lv_property': 'Clocking:Sample Clock Timebase Divisor',
        'name': 'SAMP_CLK_TIMEBASE_DIV',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150090: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nIf NISCOPE_ATTR_INPUT_CLOCK_SOURCE is an external source, this attribute specifies the frequency of the input,  or reference clock, to which the internal sample clock timebase is synchronized. The frequency is in hertz.\n'
        },
        'lv_property': 'Clocking:Reference Clock Rate',
        'name': 'REF_CLK_RATE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150091: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Exports the sample clock to a specified terminal.'
        },
        'lv_property': 'Clocking:Exported Sample Clock Output Terminal',
        'name': 'EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150093: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': "\nRestores the video-triggered data retrieved by the digitizer to the video signal's zero reference point.\nValid Values:\nVI_TRUE - Enable DC restore\nVI_FALSE - Disable DC restore\n"
        },
        'lv_property': 'Triggering:Trigger Video:Enable DC Restore',
        'name': 'ENABLE_DC_RESTORE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150094: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the source the digitizer monitors for an advance trigger.   When the advance trigger is received, the digitizer begins acquiring pretrigger  samples.\n'
        },
        'lv_property': 'Synchronization:Advance Trigger:Source',
        'name': 'ADV_TRIG_SRC',
        'resettable': False,
        'type': 'ViString'
    },
    1150095: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the source the digitizer monitors for an arm reference trigger.   When the arm reference trigger is received, the digitizer begins looking for a  reference (stop) trigger from the user-configured trigger source.\n'
        },
        'lv_property': 'Synchronization:Arm Reference Trigger:Source',
        'name': 'ARM_REF_TRIG_SRC',
        'resettable': False,
        'type': 'ViString'
    },
    1150096: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nThis attribute controls whether the TDC is used to compute an accurate trigger.\n'
        },
        'lv_property': 'Horizontal:Advanced:Enable TDC',
        'name': 'REF_TRIG_TDC_ENABLE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150097: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the destination to export the Start trigger.   When the start trigger is received, the digitizer begins acquiring  samples.\nConsult your device documentation for a specific list of valid destinations.\n'
        },
        'lv_property': 'Synchronization:Start Trigger (Acq. Arm):Output Terminal',
        'name': 'EXPORTED_START_TRIGGER_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150098: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the destination export for the reference (stop) trigger.\nConsult your device documentation for a specific list of valid destinations.\n'
        },
        'lv_property': 'Triggering:Trigger Output Terminal',
        'name': 'EXPORTED_REF_TRIGGER_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150099: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the destination for the End of Record Event.    When this event is asserted, the digitizer has completed sampling for the current record.\nConsult your device documentation for a specific list of valid destinations.\n'
        },
        'lv_property': 'Synchronization:End of Record:Output Terminal',
        'name': 'END_OF_RECORD_EVENT_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150100: {
        'access': 'read-write',
        'channel_based': True,
        'documentation': {
            'description': '\nSpecifies the poll interval in milliseconds to use during RIS acquisitions to check  whether the acquisition is complete.\n'
        },
        'lv_property': '',
        'name': 'POLL_INTERVAL',
        'resettable': True,
        'type': 'ViInt32'
    },
    1150101: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the destination for the End of Acquisition Event.    When this event is asserted, the digitizer has completed sampling for all records.\nConsult your device documentation for a specific list of valid destinations.\n'
        },
        'lv_property': 'Synchronization:End of Acquisition:Output Terminal',
        'name': 'END_OF_ACQUISITION_EVENT_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150102: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nIndicates the bit width of valid data (as opposed to padding bits) in the acquired waveform. Compare to NISCOPE_ATTR_BINARY_SAMPLE_WIDTH.\n'
        },
        'lv_property': 'Acquisition:Resolution',
        'name': 'RESOLUTION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150103: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'channel_based': True,
        'documentation': {
            'description': '\nPass the length of time you want the digitizer to wait after it starts acquiring  data until the digitizer enables the trigger system to detect a reference (stop) trigger.\nUnits: Seconds\nValid Values: 0.0 - 171.8\n'
        },
        'lv_property': 'Triggering:Start To Ref Trigger Holdoff',
        'name': 'START_TO_REF_TRIGGER_HOLDOFF',
        'resettable': False,
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1150104: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nReturns the serial number of the device.\n'
        },
        'lv_property': 'Device:Serial Number',
        'name': 'SERIAL_NUMBER',
        'resettable': False,
        'type': 'ViString'
    },
    1150105: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Gets or sets the binary phase DAC value that controls the delay added to the Phase Locked Loop (PLL) of the sample clock.',
            'note': 'if this value is set, sample clock adjust and TClk will not be able to do any sub-sample adjustment of the timebase sample clock.'
        },
        'lv_property': 'Clocking:Advanced:Oscillator Phase DAC Value',
        'name': 'OSCILLATOR_PHASE_DAC_VALUE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150106: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nIndicates whether the digitizer should use RIS sample rates when searching for a frequency in autosetup.\nValid Values:\nVI_TRUE  (1) - Use RIS sample rates in autosetup\nVI_FALSE (0) - Do not use RIS sample rates in autosetup\n'
        },
        'lv_property': 'Acquisition:Advanced:Enable RIS in Auto Setup',
        'name': 'RIS_IN_AUTO_SETUP_ENABLE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150107: {
        'access': 'read-write',
        'channel_based': True,
        'documentation': {
            'description': '\nSpecifies the terminal configuration for the channel.\n'
        },
        'enum': 'TerminalConfiguration',
        'lv_property': 'Vertical:Channel Terminal Configuration',
        'name': 'CHANNEL_TERMINAL_CONFIGURATION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150109: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the destination to export the advance trigger.   When the advance trigger is received, the digitizer begins acquiring  samples for the Nth record.\nConsult your device documentation for a specific list of valid destinations.\n'
        },
        'lv_property': 'Synchronization:Advance Trigger:Output Terminal',
        'name': 'EXPORTED_ADVANCE_TRIGGER_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150110: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the destination for the Ready for Start Event.   When this event is asserted, the digitizer is ready to receive a start trigger.\nConsult your device documentation for a specific list of valid destinations.\n'
        },
        'lv_property': 'Synchronization:Ready for Start:Output Terminal',
        'name': 'READY_FOR_START_EVENT_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150111: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the destination for the Ready for Reference Event.   When this event is asserted, the digitizer is ready to receive a reference trigger.\nConsult your device documentation for a specific list of valid destinations.\n'
        },
        'lv_property': 'Synchronization:Ready for Reference:Output Terminal',
        'name': 'READY_FOR_REF_EVENT_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150112: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the destination for the Ready for Advance Event.    When this event is asserted, the digitizer is ready to receive an advance trigger.\nConsult your device documentation for a specific list of valid destinations.\n'
        },
        'lv_property': 'Synchronization:Ready for Advance:Output Terminal',
        'name': 'READY_FOR_ADVANCE_EVENT_OUTPUT_TERMINAL',
        'resettable': False,
        'type': 'ViString'
    },
    1150128: {
        'access': 'read-write',
        'channel_based': True,
        'documentation': {
            'description': "\nSpecifies whether the digitizer acquires the waveform using multiple ADCs for the channel  enabling a higher maximum real-time sampling rate.\nValid Values:\nVI_TRUE  (1) - Use multiple interleaved ADCs on this channel\nVI_FALSE (0) - Use only this channel's ADC to acquire data for this channel\n"
        },
        'lv_property': 'Horizontal:Enable Time Interleaved Sampling',
        'name': 'ENABLE_TIME_INTERLEAVED_SAMPLING',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150129: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the destination for the 5 Volt signal.\nConsult your device documentation for a specific list of valid destinations.\n'
        },
        'lv_property': 'Synchronization:5 Volt Power:Output Terminal',
        'name': '5V_OUT_OUTPUT_TERMINAL',
        'python_name': 'five_v_out_output_terminal',
        'resettable': False,
        'type': 'ViString'
    },
    1150271: {
        'access': 'read-write',
        'channel_based': True,
        'documentation': {
            'description': '\nThe NI 5922 flexible-resolution digitizer uses an onboard FIR lowpass antialias filter.\nUse this attribute to select from several types of filters to achieve desired filtering characteristics.\n'
        },
        'enum': 'FlexFIRAntialiasFilterType',
        'lv_property': 'Vertical:Advanced:Flex FIR Antialias Filter Type',
        'name': 'FLEX_FIR_ANTIALIAS_FILTER_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150278: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies if the last acquisition was auto triggered.   You can use the Auto Triggered attribute to find out if the last acquisition was triggered.\n'
        },
        'lv_property': 'Triggering:Auto Triggered',
        'name': 'TRIGGER_AUTO_TRIGGERED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150279: {
        'access': 'read only',
        'channel_based': True,
        'documentation': {
            'description': '\nReturns the calibration gain for the current device configuration.\n\n**Related topics:**\n`NI 5122/5124/5142 Calibration <digitizers.chm::/5122_Calibration.html>`__\n',
            'note': '\nThis property is supported only by the NI PXI-5900 differential amplifier.\n'
        },
        'name': 'SIGNAL_COND_GAIN',
        'python_name': 'accessory_gain',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150280: {
        'access': 'read only',
        'channel_based': True,
        'documentation': {
            'description': '\nReturns the calibration offset for the current device configuration.\n\n**Related topics:**\n`NI 5122/5124/5142 Calibration <digitizers.chm::/5122_Calibration.html>`__\n',
            'note': '\nThis property is supported only by the NI PXI-5900 differential amplifier.\n'
        },
        'name': 'SIGNAL_COND_OFFSET',
        'python_name': 'accessory_offset',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150300: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEnables/disables the Digital Down Converter (DDC) block of the digitizer.  When the DDC block is disabled, all DDC-related properties are disabled and  have no effect on the acquired signal.\nDefault Value: VI_FALSE\n'
        },
        'lv_property': 'Onboard Signal Processing:DDC:DDC Enabled',
        'name': 'DDC_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150302: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEnables/disables frequency translating the data around the user-selected center  frequency down to baseband.\nDefault Value: VI_TRUE\n'
        },
        'lv_property': 'Onboard Signal Processing:DDC:Frequency Translation Enabled',
        'name': 'DDC_FREQUENCY_TRANSLATION_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150303: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThe frequency at which the DDC block frequency translates the input data.\nDefault Value: 10 MHz\n'
        },
        'lv_property': 'Onboard Signal Processing:DDC:Center Frequency',
        'name': 'DDC_CENTER_FREQUENCY',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150304: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThe way in which data is processed by the DDC block.\nValid Values:\nReal (0)\nComplex (1)\nDefault Value: Complex\n'
        },
        'enum': 'DataProcessingMode',
        'lv_property': 'Onboard Signal Processing:DDC:Data Processing Mode',
        'name': 'DDC_DATA_PROCESSING_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150305: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThe I center frequency phase in degrees at the first point of the acquisition.\nDefault Value: 0\n'
        },
        'lv_property': 'Onboard Signal Processing:DDC:Signal Adjustments:Frequency Translation:Frequency Translation Phase I',
        'name': 'DDC_FREQUENCY_TRANSLATION_PHASE_I',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150306: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThe Q center frequency phase in degrees at the first point of the acquisition.  Use this attribute only when NISCOPE_ATTR_DDC_DATA_PROCESSING_MODE is set to Complex.\nDefault Value: 90\n'
        },
        'lv_property': 'Onboard Signal Processing:DDC:Signal Adjustments:Frequency Translation:Frequency Translation Phase Q',
        'name': 'DDC_FREQUENCY_TRANSLATION_PHASE_Q',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150307: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nApplies gain to the specified channel in hardware before any onboard processing.\nValid Values:\n-1.5 to 1.5\n'
        },
        'lv_property': 'Vertical:Advanced:Digital Gain',
        'name': 'DIGITAL_GAIN',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150308: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nApplies offset to the specified channel in hardware before any onboard processing.\nValid Values:\n-1.5 to 1.5 V\n'
        },
        'lv_property': 'Vertical:Advanced:Digital Offset',
        'name': 'DIGITAL_OFFSET',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150309: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures error reporting when the DDC block detects an overflow in any of its  stages. Overflows lead to clipping of the waveform.\nValid Values:\nWarning (0)\nError (1)\nDisabled (2)\nDefault Value: Warning\n'
        },
        'enum': 'OverflowErrorReporting',
        'lv_property': 'Onboard Signal Processing:OSP Overflow Error Reporting',
        'name': 'OVERFLOW_ERROR_REPORTING',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150310: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nIndicates the channel that is the input of the Q path of the DDC.\nDefault Value: The channel that the attribute is configured off of.\n'
        },
        'lv_property': 'Onboard Signal Processing:DDC:Q Source',
        'name': 'DDC_Q_SOURCE',
        'resettable': False,
        'type': 'ViString'
    },
    1150311: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEnables/disables interleaving of the I and Q data.  When disabled, the traditional  niScope_Fetch() functions will return the I waveform for each acquisition followed by  the Q waveform.  When enabled, the I and Q  data are interleaved into a single waveform.  In the interleaving case, you must  allocate twice as many elements in the array as number of samples being fetched (since each  sample contains an I and a Q component).\nDefault Value: VI_TRUE\n'
        },
        'enum': 'BoolEnableDisableIq',
        'lv_property': 'Onboard Signal Processing:DDC:Fetch Interleaved IQ Data',
        'name': 'FETCH_INTERLEAVED_IQ_DATA',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150312: {
        'access': 'read only',
        'channel_based': True,
        'documentation': {
            'description': 'Returns the number of coefficients that the FIR filter can accept.  This filter is designed  to compensate the input signal for artifacts introduced to the signal outside of the digitizer.   However, since this is a generic FIR filter any coefficients are valid.  Coefficients should be  between +1 and -1 in value.'
        },
        'lv_property': 'Onboard Signal Processing:Equalization:Equalization Num Coefficients',
        'name': 'EQUALIZATION_NUM_COEFFICIENTS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150313: {
        'access': 'read-write',
        'channel_based': True,
        'documentation': {
            'description': 'Enables the onboard signal processing FIR block. This block is connected directly to the input signal.  This filter is designed to compensate the input signal for artifacts introduced to the signal outside  of the digitizer. However, since this is a generic FIR filter any coefficients are valid.  Coefficients  should be between +1 and -1 in value.'
        },
        'lv_property': 'Onboard Signal Processing:Equalization:Equalization Filter Enabled',
        'name': 'EQUALIZATION_FILTER_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150314: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nIndicates which analog compare circuitry to use on the device.\n'
        },
        'enum': 'RefTriggerDetectorLocation',
        'lv_property': 'Triggering:Onboard Signal Processing:Ref Trigger Detection Location',
        'name': 'REF_TRIGGER_DETECTOR_LOCATION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150315: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'channel_based': False,
        'documentation': {
            'description': '\nThe amount of time the trigger circuit must not detect a signal above the trigger level before  the trigger is armed.  This attribute is useful for triggering at the beginning and not in the  middle of signal bursts.\n'
        },
        'lv_property': 'Triggering:Onboard Signal Processing:Ref Trigger Min Quiet Time',
        'name': 'REF_TRIGGER_MINIMUM_QUIET_TIME',
        'resettable': False,
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1150316: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the maximum number of samples to transfer at one time from the device to host memory. Increasing this number should result in better fetching performance because the driver does not need to restart the transfers as often. However, increasing this number may also increase the amount of page-locked memory required from the system.\n'
        },
        'lv_property': 'Fetch:Data Transfer Block Size',
        'name': 'DATA_TRANSFER_BLOCK_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150318: {
        'access': 'read-write',
        'channel_based': True,
        'documentation': {
            'description': '\nEnables the bandpass filter on the specificed channel.  The default value is FALSE.\n'
        },
        'lv_property': 'Vertical:Advanced:Bandpass Filter Enabled',
        'name': 'BANDPASS_FILTER_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150319: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEnables or Disables the analog dither on the device.  The default value is FALSE.\nUsing dither can improve the spectral performance of the device by reducing the effects of quantization.  However, adding dither increases the power level to the ADC, so you may need to either decrease the signal level or increase your vertical range.\n'
        },
        'lv_property': 'Vertical:Advanced:Dither Enabled',
        'name': 'DITHER_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150320: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Enables the onboard signal processing block that resamples the input waveform to the user desired sample rate.  The default value is FALSE.'
        },
        'lv_property': 'Onboard Signal Processing:Fractional Resample:Fractional Resample Enabled',
        'name': 'FRACTIONAL_RESAMPLE_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150321: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nThis property specifies the maximum bandwidth that the device is allowed to consume.\n'
        },
        'lv_property': 'Fetch:Advanced:Maximum Bandwidth',
        'name': 'DATA_TRANSFER_MAXIMUM_BANDWIDTH',
        'resettable': False,
        'type': 'ViReal64'
    },
    1150322: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nThis property specifies the size of (read request|memory write) data payload. Due to alignment of the data buffers, the hardware may not always generate a packet of this size.\n'
        },
        'lv_property': 'Fetch:Advanced:Preferred Packet Size',
        'name': 'DATA_TRANSFER_PREFERRED_PACKET_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150328: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the current number of samples available to stream from a peer-to-peer endpoint.\n',
            'note': 'This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.'
        },
        'lv_property': 'Peer-to-Peer:Samples Available In Endpoint',
        'name': 'P2P_SAMPLES_AVAIL_IN_ENDPOINT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150329: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the address of a hardware register used to grant permisison for the peer-to-peer endpoint to write  data to another peer.. The type of this address is determined by the  NISCOPE_ATTR_P2P_DATA_TRANS_PERMISSION_ADDR_TYPE attribute. Permission is granted in bytes and the register  is additive.\n',
            'note': 'This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.'
        },
        'lv_property': 'Peer-to-Peer:Manual:Configuration:Data Transfer Permission Address',
        'name': 'P2P_DATA_TRANS_PERMISSION_ADDR',
        'resettable': False,
        'type': 'ViInt64'
    },
    1150330: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the type of address returned from the NISCOPE_ATTR_P2P_DATA_TRANS_PERMISSION_ADDR attribute.\nValid Values:\nPhysical (0)\nVirtual (1)\nDefault Value: Virtual\n',
            'note': 'This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.'
        },
        'enum': 'AddressType',
        'lv_property': 'Peer-to-Peer:Manual:Configuration:Data Transfer Permission Address Type',
        'name': 'P2P_DATA_TRANS_PERMISSION_ADDR_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150331: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the destination for data written by the peer-to-peer endpoint. The type of this address is specified  by the NISCOPE_ATTR_P2P_DESTINATION_WINDOW_ADDR_TYPE attribute.\nValid Values: A valid, non-NULL physical or virtual address.\n',
            'note': 'This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.'
        },
        'lv_property': 'Peer-to-Peer:Manual:Configuration:Destination Window Address',
        'name': 'P2P_DESTINATION_WINDOW_ADDR',
        'resettable': False,
        'type': 'ViInt64'
    },
    1150332: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the type of the NISCOPE_ATTR_P2P_DESTINATION_WINDOW_ADDR attribute.\nValid Values:\nPhysical (0)\nVirtual (1)\nDefault Value: Virtual\n',
            'note': 'This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.'
        },
        'enum': 'AddressType',
        'lv_property': 'Peer-to-Peer:Manual:Configuration:Destination Window Address Type',
        'name': 'P2P_DESTINATION_WINDOW_ADDR_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150333: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the size, in bytes, of the destination window determined by the  NISCOPE_ATTR_P2P_DESTINATION_WINDOW_ADDRESS and the NISCOPE_ATTR_P2P_DESTINATION_WINDOW_ADDRESS_TYPE  attributes.\nValid Values: Any non-NULL value.\n',
            'note': 'This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.'
        },
        'lv_property': 'Peer-to-Peer:Manual:Configuration:Destination Window Size',
        'name': 'P2P_DESTINATION_WINDOW_SIZE',
        'resettable': False,
        'type': 'ViInt64'
    },
    1150334: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the event to push the NISCOPE_ATTR_P2P_NOTIFY_MESSAGE_PUSH_VALUE attribute to the  NISCOPE_ATTR_P2P_NOTIFY_MESSAGE_PUSH_ADDR attribute. Setting this attribute to NISCOPE_VAL_NOTIFY_DONE pushes  the message when the acquisition has completed.\nValid Values:\nNever (0)\nDone (1)\nDefault Value: Done\n',
            'note': 'This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.'
        },
        'enum': 'NotificationType',
        'lv_property': 'Peer-to-Peer:Manual:Notification:Push Message On',
        'name': 'P2P_NOTIFY_PUSH_MESSAGE_ON',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150335: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the address to Push Message push Value to on the event specified by the  NISCOPE_ATTR_P2P_NOTIFY_PUSH_MESSAGE_ON attribute.\n',
            'note': 'This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.'
        },
        'lv_property': 'Peer-to-Peer:Manual:Notification:Message Push Address',
        'name': 'P2P_NOTIFY_MESSAGE_PUSH_ADDR',
        'resettable': False,
        'type': 'ViInt64'
    },
    1150336: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the type of the NISCOPE_ATTR_P2P_NOTIFY_MESSAGE_PUSH_ADDR attribute.\nValid Values:\nPhysical (0)\nVirtual (1)\nDefault Value: Virtual\n',
            'note': 'This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.'
        },
        'enum': 'AddressType',
        'lv_property': 'Peer-to-Peer:Manual:Notification:Message Push Address Type',
        'name': 'P2P_NOTIFY_MESSAGE_PUSH_ADDR_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150337: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the value to be pushed to the NISCOPE_ATTR_P2P_NOTIFY_MESSAGE_PUSH_ADDR attribute on the event specified  by the NISCOPE_ATTR_MESSAGE_PUSH_ON attribute.',
            'note': 'This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.'
        },
        'lv_property': 'Peer-to-Peer:Manual:Notification:Message Push Value',
        'name': 'P2P_NOTIFY_MESSAGE_PUSH_VALUE',
        'resettable': False,
        'type': 'ViInt64'
    },
    1150338: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies whether the digitizer writes data to the peer-to-peer endpoint.\nDefault Value: VI_FALSE\n',
            'note': 'This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.'
        },
        'enum': 'BoolEnableDisable',
        'lv_property': 'Peer-to-Peer:P2P Enabled',
        'name': 'P2P_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150339: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies which channels are written to a peer-to-peer endpoint. If multiple channels are specified,  the channels are interleaved by sample.\nDefault Value: 0\n',
            'note': 'This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.'
        },
        'lv_property': 'Peer-to-Peer:Channels to Stream',
        'name': 'P2P_CHANNELS_TO_STREAM',
        'resettable': False,
        'type': 'ViString'
    },
    1150340: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the number of samples transferred through the peer-to-peer endpoint since it was last reset.\n',
            'note': 'This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.'
        },
        'lv_property': 'Peer-to-Peer:Samples Transferred',
        'name': 'P2P_SAMPLES_TRANSFERRED',
        'resettable': False,
        'type': 'ViInt64'
    },
    1150341: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the most number of samples available to stream from a peer-to-peer endpoint since the last  time this attribute was read.\n',
            'note': 'This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.'
        },
        'lv_property': 'Peer-to-Peer:Most Samples Available in Endpoint',
        'name': 'P2P_MOST_SAMPLES_AVAIL_IN_ENDPOINT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150342: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the size in samples of the peer-to-peer endpoint.\n',
            'note': 'This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.'
        },
        'lv_property': 'Peer-to-Peer:Endpoint Size',
        'name': 'P2P_ENDPOINT_SIZE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150343: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEnables/disables the advanced attributes for a peer-to-peer endpoint. These attributes cannot be used if  an endpoint is being configured by NI-P2P, or a resource reservation error will occur.\nDefault Value: VI_FALSE\n',
            'note': 'This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.'
        },
        'enum': 'BoolEnableDisable',
        'lv_property': 'Peer-to-Peer:Manual:Manual Configuration Enabled',
        'name': 'P2P_ADVANCED_ATTRIBUTES_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150344: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns TRUE if the endpoint FIFO has overflowed. Reset the endpoint to clear the overflow condition.\n',
            'note': 'This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.'
        },
        'lv_property': 'Peer-to-Peer:Endpoint Overflow',
        'name': 'P2P_ENDPOINT_OVERFLOW',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150345: {
        'access': 'read only',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the number of FIFO-based peer-to-peer endpoints this device supports.\n',
            'note': 'This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.'
        },
        'lv_property': 'Peer-to-Peer:FIFO Endpoint Count',
        'name': 'P2P_FIFO_ENDPOINT_COUNT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150354: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies whether the digitizer writes data to onboard memory when a peer-to-peer endpoint is enabled.\nDefault Value: VI_FALSE\n',
            'note': 'This attribute can be used only with high-speed digitizers that support peer-to-peer streaming.'
        },
        'enum': 'BoolEnableDisable',
        'lv_property': 'Peer-to-Peer:Onboard Memory Enabled',
        'name': 'P2P_ONBOARD_MEMORY_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150366: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'channel_based': False,
        'documentation': {
            'description': '\nEnd of Record to Advance Trigger Holdoff is the length of time (in\nseconds) that a device waits between the completion of one record and\nthe acquisition of pre-trigger samples for the next record. During this\ntime, the acquisition engine state delays the transition to the Wait for\nAdvance Trigger state, and will not store samples in onboard memory,\naccept an Advance Trigger, or trigger on the input signal..\n**Supported Devices**: NI 5185/5186\n'
        },
        'lv_property': 'Triggering:End of Record to Advance Trigger Holdoff',
        'name': 'END_OF_RECORD_TO_ADVANCE_TRIGGER_HOLDOFF',
        'resettable': False,
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1150367: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nIf NISCOPE_ATTR_SAMP_CLK_TIMEBASE_SRC is an external source, this property specifies the ratio between the NISCOPE_ATTR_SAMP_CLK_TIMEBASE_RATE and the actual sample rate, which can be higher. This property can be used in conjunction with NISCOPE_ATTR_SAMP_CLK_TIMEBASE_DIV.\nSome devices use multiple ADCs to sample the same channel at an effective sample rate that is greater than the specified clock rate. When providing an external sample clock use this property to indicate when you want a higher sample rate. Valid values for this property vary by device and current configuration.\n\n**Related topics:**\n`Sample Clock <digitizers.chm::/Sample_Clock.html>`__\n'
        },
        'name': 'SAMP_CLK_TIMEBASE_MULT',
        'python_name': 'sample_clock_timebase_multiplier',
        'resettable': False,
        'type': 'ViInt32'
    },
    1150374: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'channel_based': False,
        'documentation': {
            'description': '\nGets or sets the absolute time offset of the sample clock relative to\nthe reference clock in terms of seconds.\n',
            'note': '\nConfigures the sample clock relationship with respect to the reference\nclock. This parameter is factored into NI-TClk adjustments and is\ntypically used to improve the repeatability of NI-TClk Synchronization.\nWhen this parameter is read, the currently programmed value is returned.\nThe range of the absolute sample clock offset is [-.5 sample clock\nperiods, .5 sample clock periods]. The default absolute sample clock\noffset is 0s.\n'
        },
        'lv_property': 'Clocking:Advanced:Absolute Sample Clock Offset',
        'name': 'ABSOLUTE_SAMPLE_CLOCK_OFFSET',
        'resettable': False,
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1150375: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': 'Gets the absolute file path to the bitfile loaded on the FPGA.',
            'note': 'Gets the absolute file path to the bitfile loaded on the FPGA.'
        },
        'lv_property': 'Device:FPGA Bitfile Path',
        'name': 'FPGA_BITFILE_PATH',
        'resettable': False,
        'type': 'ViString'
    },
    1150376: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nEnables the interleaving offset correction on the specified channel. The\ndefault value is TRUE.\n**Related topics:**\n`Timed Interleaved\nSampling <digitizers.chm::/TimeInterleavedSampling.html>`__\n',
            'note': 'If disabled, warranted specifications are not guaranteed.'
        },
        'lv_property': 'Vertical:Advanced:Interleaving Offset Correction Enabled',
        'name': 'INTERLEAVING_OFFSET_CORRECTION_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1150377: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the frequency for the highpass filter in Hz. The device uses\none of the valid values listed below. If an invalid value is specified,\nno coercion occurs. The default value is 0.\n**(PXIe-5164) Valid Values:**\n0 90 450\n**Related topics:**\n`Digital Filtering <digitizers.chm::/Digital_Filtering_Overview.html>`__\n'
        },
        'lv_property': 'Vertical:Advanced:High Pass Filter Frequency',
        'name': 'HIGH_PASS_FILTER_FREQUENCY',
        'resettable': False,
        'type': 'ViReal64'
    },
    1151000: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the Carrier NCO Center Frequency. The coerced value can be read back..\nDefault Value: 15.0e6\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Carrier Mixer:NCO Center Frequency',
        'name': 'DDC_NCO_FREQUENCY',
        'resettable': False,
        'type': 'ViReal64'
    },
    1151001: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the Carrier Phase Offset. The coerced value can be read back.\nDefault Value: 0.0\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Carrier Mixer:Phase Offset',
        'name': 'DDC_NCO_PHASE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1151003: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSet this to VI_FALSE to disable programming of the DDC.\nDefault Value: VI_TRUE\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Enable DDC',
        'name': 'DDC_ENABLE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1151010: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nControls the decimation in the CIC filter. The CIC filter reduces the sample rate  of a wideband signal to a rate that other filters in the DDC can process.\nDefault Value: 4\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):CIC Filter:Decimation',
        'name': 'DDC_CIC_DECIMATION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151011: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nControls the shift gain at the input to the CIC filter. The CIC filter reduces  the sample rate of a wideband signal to a rate that other filters in the DDC can process.\nDefault Value: 0\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):CIC Filter:Shift Gain',
        'name': 'DDC_CIC_SHIFT_GAIN',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151020: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSet this to VI_TRUE to enable the frequency discriminator.\nDefault Value: VI_FALSE\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:Enable',
        'name': 'DDC_DISCRIMINATOR_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1151021: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the amount of decimation, from 1 to 8.\nDefault Value: 1\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:FIR Decimation',
        'name': 'DDC_DISCRIMINATOR_FIR_DECIMATION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151022: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the discriminator FIR symmetry to symmetric or asymmetric.\nDefault Value: Symmetric\n'
        },
        'enum': 'DiscriminatorFIRSymmetry',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:FIR Symmetry',
        'name': 'DDC_DISCRIMINATOR_FIR_SYMMETRY',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151023: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the discriminator FIR symmetry type to even or odd.\nDefault Value: Even\n'
        },
        'enum': 'DiscriminatorFIRSymmetryType',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:FIR Symmetry Type',
        'name': 'DDC_DISCRIMINATOR_FIR_SYMMETRY_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151024: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the discriminator FIR number of taps.\nValid Values:\n1 to 63.\nDefault Value: 1\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:FIR Taps',
        'name': 'DDC_DISCRIMINATOR_FIR_NUM_TAPS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151025: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the number of delays in the discriminator, from 1 to 8.\nDefault Value: 1\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:Delay',
        'name': 'DDC_DISCRIMINATOR_DELAY',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151026: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the discriminator FIR input source to phase, magnitude, or resampler.\nDefault Value: Phase\n'
        },
        'enum': 'DiscriminatorFIRInputSource',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:FIR Input Source',
        'name': 'DDC_DISCRIMINATOR_FIR_INPUT_SOURCE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151027: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nPrograms the coordinate converter to multiply the phase output by 1, 2, 4, or 8. Multiplying the phase output  removes phase modulation before the frequency is measured.\nDefault Value: 0\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Frequency Discriminator:Phase Multiplier',
        'name': 'DDC_DISCRIMINATOR_PHASE_MULTIPLIER',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151030: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the programmable FIR filter decimation.\nDefault Value: 1\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Programmable FIR Filter:Decimation',
        'name': 'DDC_PFIR_DECIMATION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151031: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets either a symmetric or asymmetric filter.\nValid Values:\nNISCOPE_VAL_SYMMETRIC (0)\nNISCOPE_VAL_ASYMMETRIC (1)\nDefault Value: Symmetric\n'
        },
        'enum': 'ProgFIRFilterSymmetry',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Programmable FIR Filter:Symmetry',
        'name': 'DDC_PFIR_SYMMETRY',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151032: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets either even or odd symmetry.\nValid Values:\nNISCOPE_VAL_EVEN (0)\nNISCOPE_VAL_ODD (1)\nDefault Value: Even\n'
        },
        'enum': 'ProgFIRFilterSymmetryType',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Programmable FIR Filter:Symmetry Type',
        'name': 'DDC_PFIR_SYMMETRY_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151033: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nNumber of taps in the FIR filter, from 1 to 255.\nDefault Value: 1\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Programmable FIR Filter:Taps',
        'name': 'DDC_PFIR_NUM_TAPS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151034: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets either a complex filter or a dual real filter.\nValid Values:\nNISCOPE_VAL_REAL (0)\nNISCOPE_VAL_COMPLEX (1)\nDefault Value: Real\n'
        },
        'enum': 'ProgFIRFilterRealComplex',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Programmable FIR Filter:Real/Complex',
        'name': 'DDC_PFIR_REAL_OR_COMPLEX',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151040: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the maximum gain and minimum signal levels in the AGC.\nDefault Value: 6.020600\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):AGC:Upper Gain Limit',
        'name': 'DDC_AGC_UPPER_GAIN_LIMIT',
        'resettable': False,
        'type': 'ViReal64'
    },
    1151041: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the minimum gain and maximum signal levels in the AGC.\nDefault Value: 6.020600\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):AGC:Lower Gain Limit',
        'name': 'DDC_AGC_LOWER_GAIN_LIMIT',
        'resettable': False,
        'type': 'ViReal64'
    },
    1151042: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nAlong with NISCOPE_ATTR_DDC_AGC_LOOP_GAIN_0_MANTISSA, sets the loop gain for the AGC.\nDefault Value: 0\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):AGC:Loop Gain 0 Exponent',
        'name': 'DDC_AGC_LOOP_GAIN_0_EXPONENT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151043: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nAlong with NISCOPE_ATTR_DDC_AGC_LOOP_GAIN_0_EXPONENT, sets the loop gain for the AGC.\nDefault Value: 0\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):AGC:Loop Gain 0 Mantissa',
        'name': 'DDC_AGC_LOOP_GAIN_0_MANTISSA',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151044: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nAlong with NISCOPE_ATTR_DDC_AGC_LOOP_GAIN_1_MANTISSA, sets the loop gain for the AGC.\nDefault Value: 0\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):AGC:Loop Gain 1 Exponent',
        'name': 'DDC_AGC_LOOP_GAIN_1_EXPONENT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151045: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nAlong with NISCOPE_ATTR_DDC_AGC_LOOP_GAIN_1_EXPONENT, sets the loop gain for the AGC.\nDefault Value: 0\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):AGC:Loop Gain 1 Mantissa',
        'name': 'DDC_AGC_LOOP_GAIN_1_MANTISSA',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151046: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the gain error in the AGC.\nDefault Value: 0x034D\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):AGC:Threshold',
        'name': 'DDC_AGC_THRESHOLD',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151047: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nAverages the AGC values.\nValid Values:\n0 - Mean\n1 - Median\nDefault Value: 0\n'
        },
        'enum': 'AgcAverageControl',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):AGC:Average Control',
        'name': 'DDC_AGC_AVERAGE_CONTROL',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151050: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEnables or bypasses the halfband filters. If set to VI_TRUE, halfband filters are bypassed.\nDefault Value: VI_TRUE\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):HalfBand Filter:Bypass',
        'name': 'DDC_HALFBAND_BYPASSED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1151051: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEnables halfband filter 1.\nDefault Value: VI_TRUE\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):HalfBand Filter:Filter 1 Enable',
        'name': 'DDC_HALFBAND_1_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1151052: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEnables halfband filter 2.\nDefault Value: VI_FALSE\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):HalfBand Filter:Filter 2 Enable',
        'name': 'DDC_HALFBAND_2_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1151053: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEnables halfband filter 3.\nDefault Value: VI_FALSE\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):HalfBand Filter:Filter 3 Enable',
        'name': 'DDC_HALFBAND_3_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1151054: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEnables halfband filter 4.\nDefault Value: VI_FALSE\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):HalfBand Filter:Filter 4 Enable',
        'name': 'DDC_HALFBAND_4_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1151055: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEnables halfband filter 5.\nDefault Value: VI_FALSE\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):HalfBand Filter:Filter 5 Enable',
        'name': 'DDC_HALFBAND_5_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1151070: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the source for the AOUT parallel output from the DDC.\nValid Values:\nNISCOPE_VAL_I_DATA (0)\nNISCOPE_VAL_MAGNITUDE_DATA (1)\nNISCOPE_VAL_FREQ_DATA (2)\nDefault Value: I Data\n'
        },
        'enum': 'AoutParallelOutputSource',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Output Configuration:Parallel:AOUT Source',
        'name': 'DDC_AOUT_PARALLEL_OUTPUT_SOURCE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151071: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the source for the BOUT parallel output from the DDC.\nValid Values:\nNISCOPE_VAL_MAGNITUDE_DATA (1)\nNISCOPE_VAL_Q_DATA (3)\nNISCOPE_VAL_PHASE_DATA (4)\nDefault Value: Q Data\n'
        },
        'enum': 'BoutParallelOutputSource',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Output Configuration:Parallel:BOUT Source',
        'name': 'DDC_BOUT_PARALLEL_OUTPUT_SOURCE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151072: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEnables the special test mode where the carrier NCO outputs are set to 0x7FFF.\nDefault Value: VI_FALSE\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Test Mode Sin/Cos',
        'name': 'DDC_TEST_SINE_COSINE',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1151073: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSelects the source for the input to the coordinate converter, either the HB filter or the programmable FIR.\nValid Values:\n0 - Resampler HB 1 - Programmable FIR Default Value: 1\n'
        },
        'enum': 'CoordinateConverterInput',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Coordinate Converter Input',
        'name': 'DDC_COORDINATE_CONVERTER_INPUT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151074: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEither enables or zeros out the Q input to coordinate converter.\nDefault Value: I and Q\n'
        },
        'enum': 'QInputToCoordConverter',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Q Input to Coord. Converter',
        'name': 'DDC_Q_INPUT_TO_COORD_CONVERTER_INPUT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151080: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSource for Syncout CLK.\nValid Values:\n0 - CLKIN\n1 - PROCCLK\nDefault Value: CLKIN\n'
        },
        'enum': 'SyncoutClkSelect',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Syncout CLK Select',
        'name': 'DDC_SYNCOUT_CLK_SELECT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151120: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nWhen TRUE, updates the timing NCO frequency to zero the feedback of the phase accumulator as well as  update the phase and frequency.\nDefault Value: VI_TRUE\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Timing NCO:Phase Accum. Load on Update',
        'name': 'DDC_TIMING_NCO_PHASE_ACCUM_LOAD',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1151121: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nIf set to FALSE, enables the accumulator in the timing NCO. If set to TRUE, zeros out feedback  in the accumulator.\nDefault Value: VI_FALSE\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Timing NCO:Clear Phase Accum.',
        'name': 'DDC_TIMING_NCO_CLEAR_PHASE_ACCUM',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1151122: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nIf set to TRUE, enables offset frequency in the timing NCO. If set to FALSE, applies no offset frequency.\nDefault Value: VI_FALSE\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Timing NCO:Enable Offset Freq.',
        'name': 'DDC_TIMING_NCO_ENABLE_OFFSET_FREQ',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1151123: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the number of offset bits in the timing NCO.\nValid Values:\n0 - 8 bits\n1 - 16 bits\n2 - 24 bits\n3 - 32 bits\nDefault Value: 8 bits\n'
        },
        'enum': 'TimingNcoFreqOffsetBits',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Timing NCO:Frequency Offset Bits',
        'name': 'DDC_TIMING_NCO_NUM_OFFSET_FREQ_BITS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151124: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nControls the frequency of the timing NCO. Specifies the timing NCO center frequency in binary format:\nN = (Fout / Fresampler) X 2^32\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Timing NCO:Center Frequency',
        'name': 'DDC_TIMING_NCO_CENTER_FREQUENCY',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151125: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nOffsets the phase of the timing NCO in binary format.  The value is transfered to the Active Register during the next initiate acquisition operation.\nDefault Value: 0\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Timing NCO:Phase Offset',
        'name': 'DDC_TIMING_NCO_PHASE_OFFSET',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151126: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSelects the resampling filter mode.\nValid Values:\n1 - Resampler Enabled 2 - HB 1 Enabled 3 - Resampler and HB 1 6 - Both HB Filters 7 - Resampler and Both HB Filters Default Value: 1\n'
        },
        'enum': 'ResamplerFilterMode',
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Resampler:Filter Mode',
        'name': 'DDC_RESAMPLER_FILTER_MODE_SELECT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151127: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEither enables or bypasses the resampler filter in the DDC.  Set to VI_TRUE to bypass the resampling filter section.\nDefault Value: VI_TRUE\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Resampler:Bypass',
        'name': 'DDC_RESAMPLER_BYPASS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1151128: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nPrograms the delay between output samples when interpolating. These outputs can be delayed from 2 to 255 clocks.\nDefault Value: 16\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Resampler:Output Pulse Delay',
        'name': 'DDC_RESAMPLER_OUTPUT_PULSE_DELAY',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151129: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nDivides down the Resampler NCO output by the value loaded into the register plus one.\nDefault Value: 2\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Resampler:NCO Divide',
        'name': 'DDC_NCO_DIVIDE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151130: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nDivides down the reference clock by the value loaded into the register plus one.  Load with a value that is one less than the desired period.\nDefault Value: 2\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Resampler:Reference Divide',
        'name': 'DDC_REFERENCE_DIVIDE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151300: {
        'access': 'read-write',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSet to VI_TRUE to enable the analog dither on the NI 5620/5621.\nDefault Value: VI_FALSE\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Enable Dither',
        'name': 'ENABLE_DITHER',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1151301: {
        'access': 'read only',
        'channel_based': True,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the combined DDC decimation.\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Combined Decimation',
        'name': 'DDC_COMBINED_DECIMATION',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151302: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nVoltage of the DAC that controls the oscillator, used for external calibration.\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:Serial DAC Cal Voltage',
        'name': 'SERIAL_DAC_CAL_VOLTAGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1151303: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nIf TRUE, the PLL has remained locked to the external reference clock since it was last checked. If FALSE,  the PLL has become unlocked from the external reference clock since it was last checked.\n'
        },
        'lv_property': 'Clocking:PLL Lock Status',
        'name': 'PLL_LOCK_STATUS',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1151304: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the delay in seconds that is used by niScope_InitiateAcquisition to allow additional  delay between programming of the vertical range, trigger level, DDC, and the start of the acquisition.  This attribute is only supported for the NI 5112 and the NI 5620/5621.\n'
        },
        'lv_property': 'Acquisition:Delay before Initiate',
        'name': 'DELAY_BEFORE_INITIATE',
        'resettable': False,
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1151305: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nUsed for directly accessing the\n`DDC <Digitizers.chm::/Glossary.html#DDC>`__ registers.\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:DDC Direct Register Address',
        'name': 'DDC_DIRECT_REGISTER_ADDRESS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1151306: {
        'access': 'read-write',
        'channel_based': False,
        'codegen_method': 'no',
        'documentation': {
            'description': '\nUsed for directly accessing the\n`DDC <Digitizers.chm::/Glossary.html#DDC>`__ registers. The default\nvalue is 0.\n'
        },
        'lv_property': 'Device Specific:IF Digitizer (5620 and 5621):Advanced:DDC Direct Register Data',
        'name': 'DDC_DIRECT_REGISTER_DATA',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250001: {
        'access': 'read-write',
        'channel_based': True,
        'documentation': {
            'description': '\nSpecifies the absolute value of the input range for a channel in volts.  For example, to acquire a sine wave that spans between -5 and +5 V, set this attribute to 10.0 V.\nRefer to the NI High-Speed Digitizers Help for a list of supported vertical ranges for each device.  If the specified range is not supported by a device, the value is coerced  up to the next valid range.\n'
        },
        'lv_property': 'Vertical:Vertical Range',
        'name': 'VERTICAL_RANGE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250002: {
        'access': 'read-write',
        'channel_based': True,
        'documentation': {
            'description': '\nSpecifies the location of the center of the range. The value is with respect to ground and is in volts.  For example, to acquire a sine wave that spans between 0.0 and 10.0 V, set this attribute to 5.0 V.\n',
            'note': 'This attribute is not supported by all digitizers.Refer to the NI High-Speed Digitizers Help for a list of vertical offsets supported for each device.'
        },
        'lv_property': 'Vertical:Vertical Offset',
        'name': 'VERTICAL_OFFSET',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250003: {
        'access': 'read-write',
        'channel_based': True,
        'documentation': {
            'description': '\nSpecifies how the digitizer couples the input signal for the channel.  When input coupling changes, the input stage takes a finite amount of time to settle.\n'
        },
        'enum': 'VerticalCoupling',
        'lv_property': 'Vertical:Vertical Coupling',
        'name': 'VERTICAL_COUPLING',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250004: {
        'access': 'read-write',
        'channel_based': True,
        'documentation': {
            'description': '\nSpecifies the probe attenuation for the input channel. For example, for a 10:1 probe,  set this attribute to 10.0.\nValid Values:\nAny positive real number. Typical values are 1, 10, and 100.\n'
        },
        'lv_property': 'Vertical:Probe Attenuation',
        'name': 'PROBE_ATTENUATION',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250005: {
        'access': 'read-write',
        'channel_based': True,
        'documentation': {
            'description': "\nSpecifies whether the digitizer acquires a waveform for the channel.\nValid Values:\nVI_TRUE  (1) - Acquire data on this channel\nVI_FALSE (0) - Don't acquire data on this channel\n"
        },
        'lv_property': 'Vertical:Channel Enabled',
        'name': 'CHANNEL_ENABLED',
        'resettable': False,
        'type': 'ViBoolean'
    },
    1250006: {
        'access': 'read-write',
        'channel_based': True,
        'documentation': {
            'description': '\nSpecifies the bandwidth of the channel. Express this value as the frequency at which the input  circuitry attenuates the input signal by 3 dB. The units are hertz.\nDefined Values:\nNISCOPE_VAL_BANDWIDTH_FULL (-1.0)\nNISCOPE_VAL_BANDWIDTH_DEVICE_DEFAULT (0.0)\nNISCOPE_VAL_20MHZ_BANDWIDTH (20000000.0)\nNISCOPE_VAL_100MHZ_BANDWIDTH (100000000.0)\nNISCOPE_VAL_20MHZ_MAX_INPUT_FREQUENCY (20000000.0)\nNISCOPE_VAL_100MHZ_MAX_INPUT_FREQUENCY (100000000.0)\n'
        },
        'lv_property': 'Vertical:Maximum Input Frequency',
        'name': 'MAX_INPUT_FREQUENCY',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250007: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the length of time that corresponds to the record length.\nUnits: Seconds\n'
        },
        'lv_property': 'Horizontal:Advanced:Time Per Record',
        'name': 'HORZ_TIME_PER_RECORD',
        'resettable': False,
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1250008: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nReturns the actual number of points the digitizer acquires for each channel.  The value is equal to or greater than the minimum number of points you specify with  NISCOPE_ATTR_HORZ_MIN_NUM_PTS.\nAllocate a ViReal64 array of this size or greater to pass as the WaveformArray parameter of  the Read and Fetch functions. This attribute is only valid after a call to the one of the  Configure Horizontal functions.\n'
        },
        'lv_property': 'Horizontal:Actual Record Length',
        'name': 'HORZ_RECORD_LENGTH',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250009: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the minimum number of points you require in the waveform record for each channel.  NI-SCOPE uses the value you specify to configure the record length that the digitizer uses  for waveform acquisition. NISCOPE_ATTR_HORZ_RECORD_LENGTH returns the actual record length.\nValid Values: 1 - available onboard memory\n'
        },
        'lv_property': 'Horizontal:Min Number of Points',
        'name': 'HORZ_MIN_NUM_PTS',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250010: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nReturns the effective sample rate using the current configuration. The units are samples per second.  This attribute is only valid after a call to the one of the Configure Horizontal functions.\nUnits: Hertz (Samples / Second)\n'
        },
        'lv_property': 'Horizontal:Actual Sample Rate',
        'name': 'HORZ_SAMPLE_RATE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250011: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the position of the Reference Event in the waveform record.  When the digitizer detects a trigger, it waits the length of time the  NISCOPE_ATTR_TRIGGER_DELAY_TIME attribute specifies. The event that occurs when  the delay time elapses is the Reference Event. The Reference Event is relative to the  start of the record and is a percentage of the record length. For example, the value 50.0  corresponds to the center of the waveform record and 0.0 corresponds to the first element in the waveform record.\nValid Values: 0.0 - 100.0\n'
        },
        'lv_property': 'Horizontal:Reference Position',
        'name': 'HORZ_RECORD_REF_POSITION',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250012: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the type of trigger to use.\n'
        },
        'enum': 'TriggerType',
        'lv_property': 'Triggering:Trigger Type',
        'name': 'TRIGGER_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250013: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the source the digitizer monitors for the trigger event.\n'
        },
        'lv_property': 'Triggering:Trigger Source',
        'name': 'TRIGGER_SOURCE',
        'resettable': False,
        'type': 'ViString'
    },
    1250014: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies how the digitizer couples the trigger source. This attribute affects instrument operation only when  NISCOPE_ATTR_TRIGGER_TYPE is set to NISCOPE_VAL_EDGE_TRIGGER, NISCOPE_VAL_HYSTERESIS_TRIGGER, or NISCOPE_VAL_WINDOW_TRIGGER.\n'
        },
        'enum': 'TriggerCoupling',
        'lv_property': 'Triggering:Trigger Coupling',
        'name': 'TRIGGER_COUPLING',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250015: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the trigger delay time in seconds. The trigger delay time is the length of time the digitizer waits  after it receives the trigger. The event that occurs when the trigger delay elapses is the Reference Event.\nValid Values: 0.0 - 171.8\n'
        },
        'lv_property': 'Triggering:Trigger Delay',
        'name': 'TRIGGER_DELAY_TIME',
        'resettable': False,
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1250016: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the length of time (in seconds) the digitizer waits after detecting a trigger before  enabling the trigger subsystem to detect another trigger. This attribute affects instrument operation  only when the digitizer requires multiple acquisitions to build a complete waveform. The digitizer requires  multiple waveform acquisitions when it uses equivalent-time sampling or when the digitizer is configured for a  multi-record acquisition through a call to niScope_ConfigureHorizontalTiming.\nValid Values: 0.0 - 171.8\n'
        },
        'lv_property': 'Triggering:Trigger Holdoff',
        'name': 'TRIGGER_HOLDOFF',
        'resettable': False,
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1250017: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the voltage threshold for the trigger subsystem. The units are volts.  This attribute affects instrument behavior only when the NISCOPE_ATTR_TRIGGER_TYPE is set to  NISCOPE_VAL_EDGE_TRIGGER, NISCOPE_VAL_HYSTERESIS_TRIGGER, or NISCOPE_VAL_WINDOW_TRIGGER.\nValid Values:\nThe values of the range and offset parameters in niScope_ConfigureVertical determine the valid range for the trigger level  on the channel you use as the Trigger Source. The value you pass for this parameter must meet the following conditions:\n'
        },
        'lv_property': 'Triggering:Trigger Level',
        'name': 'TRIGGER_LEVEL',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250018: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies if a rising or a falling edge triggers the digitizer.  This attribute affects instrument operation only when NISCOPE_ATTR_TRIGGER_TYPE is set to  NISCOPE_VAL_EDGE_TRIGGER, NISCOPE_VAL_HYSTERESIS_TRIGGER, or NISCOPE_VAL_WINDOW_TRIGGER.\n'
        },
        'enum': 'TriggerSlope',
        'lv_property': 'Triggering:Trigger Slope',
        'name': 'TRIGGER_SLOPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250101: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies how the digitizer acquires data and fills the waveform record.\n'
        },
        'enum': 'AcquisitionType',
        'lv_property': 'Acquisition:Acquisition Type',
        'name': 'ACQUISITION_TYPE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250102: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nConfigures the device to automatically complete an acquisition if a trigger has not been received.\nValid Values:\nNone (1)         - Normal triggering\nAuto Trigger (2) - Auto trigger acquisition if no trigger arrives\n'
        },
        'enum': 'TriggerModifier',
        'lv_property': 'Triggering:Trigger Modifier',
        'name': 'TRIGGER_MODIFIER',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250103: {
        'access': 'read-write',
        'channel_based': True,
        'documentation': {
            'description': '\nSpecifies the input impedance for the channel in Ohms.\n'
        },
        'lv_property': 'Vertical:Input Impedance',
        'name': 'INPUT_IMPEDANCE',
        'resettable': False,
        'type': 'ViReal64'
    },
    1250106: {
        'access': 'read only',
        'channel_based': False,
        'documentation': {
            'description': '\nIndicates the sample mode the digitizer is currently using.\n'
        },
        'lv_property': 'Acquisition:Sample Mode',
        'name': 'SAMPLE_MODE',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250109: {
        'access': 'read-write',
        'attribute_class': 'AttributeViReal64TimeDeltaSeconds',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the length of time from the trigger event to the first point in  the waveform record in seconds.  If the value is positive, the first point  in the waveform record occurs after the trigger event (same as specifying  NISCOPE_ATTR_TRIGGER_DELAY_TIME).  If the value is negative, the first point  in the waveform record occurs before the trigger event (same as specifying  NISCOPE_ATTR_HORZ_RECORD_REF_POSITION).\n'
        },
        'lv_property': 'Horizontal:Advanced:Acquisition Start Time',
        'name': 'ACQUISITION_START_TIME',
        'resettable': False,
        'type': 'ViReal64',
        'type_in_documentation': 'float in seconds or datetime.timedelta'
    },
    1250201: {
        'access': 'read-write',
        'channel_based': True,
        'documentation': {
            'description': '\nSpecifies the type of video signal, such as NTSC, PAL, or SECAM.\n'
        },
        'enum': 'VideoSignalFormat',
        'lv_property': 'Triggering:Trigger Video:Signal Format',
        'name': 'TV_TRIGGER_SIGNAL_FORMAT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250204: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies whether the video signal sync is positive or negative.\n'
        },
        'enum': 'VideoPolarity',
        'lv_property': 'Triggering:Trigger Video:Polarity',
        'name': 'TV_TRIGGER_POLARITY',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250205: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the condition in the video signal that causes the digitizer to trigger.\n'
        },
        'enum': 'VideoTriggerEvent',
        'lv_property': 'Triggering:Trigger Video:Event',
        'name': 'TV_TRIGGER_EVENT',
        'resettable': False,
        'type': 'ViInt32'
    },
    1250206: {
        'access': 'read-write',
        'channel_based': False,
        'documentation': {
            'description': '\nSpecifies the line on which to trigger, if NISCOPE_ATTR_TV_TRIGGER_EVENT is set to line number. The  valid ranges of the attribute depend on the signal format selected.  M-NTSC has a valid range of 1 to 525.  B/G-PAL, SECAM, 576i, and 576p have a valid range of  1 to 625. 720p has a valid range of 1 to 750. 1080i and 1080p have a valid range of 1125.\n'
        },
        'lv_property': 'Triggering:Trigger Video:Line Number',
        'name': 'TV_TRIGGER_LINE_NUMBER',
        'resettable': False,
        'type': 'ViInt32'
    }
}
