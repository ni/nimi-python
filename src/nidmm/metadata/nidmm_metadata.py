config = {
    'module_name' : 'nidmm',
    'c_function_prefix' : 'niDMM_',
    'session_description' : 'An NI-DMM session to a National Instruments Digital Multimeter',
    'library_windows':
    {
        '32': 'nidmm_32.dll',
        '64': 'nidmm_64.dll'
    },
    'library_linux':
    {
        '32': 'nidmm_32.so',
        '64': 'nidmm_64.so'
    },
}


attributes = {
    'RANGE_CHECK':
    {
        'id':1050002,
        'type':'ViBoolean',
        'enum':None,
        'access':'read-write'
    },
    'QUERY_INSTRUMENT_STATUS':
    {
        'id':1050003,
        'type':'ViBoolean',
        'enum':None,
        'access':'read-write'
    },
    'CACHE':
    {
        'id':1050004,
        'type':'ViBoolean',
        'enum':None,
        'access':'read-write'
    },
    'SIMULATE':
    {
        'id':1050005,
        'type':'ViBoolean',
        'enum':None,
        'access':'read-write'
    },
    'RECORD_COERCIONS':
    {
        'id':1050006,
        'type':'ViBoolean',
        'enum':None,
        'access':'read-write'
    },
    'INTERCHANGE_CHECK':
    {
        'id':1050021,
        'type':'ViBoolean',
        'enum':None,
        'access':'read-write'
    },
    'SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION':
    {
        'id':1050515,
        'type':'ViInt32',
        'enum':None,
        'access':'read only'
    },
    'SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION':
    {
        'id':1050516,
        'type':'ViInt32',
        'enum':None,
        'access':'read only'
    },
    'SPECIFIC_DRIVER_DESCRIPTION':
    {
        'id':1050514,
        'type':'ViString',
        'enum':None,
        'access':'read only'
    },
    'SPECIFIC_DRIVER_PREFIX':
    {
        'id':1050302,
        'type':'ViString',
        'enum':None,
        'access':'read only'
    },
    'SPECIFIC_DRIVER_VENDOR':
    {
        'id':1050513,
        'type':'ViString',
        'enum':None,
        'access':'read only'
    },
    'SPECIFIC_DRIVER_REVISION':
    {
        'id':1050551,
        'type':'ViString',
        'enum':None,
        'access':'read only'
    },
    'CLASS_DRIVER_CLASS_SPEC_MAJOR_VERSION':
    {
        'id':1050519,
        'type':'ViInt32',
        'enum':None,
        'access':'read only'
    },
    'CLASS_DRIVER_CLASS_SPEC_MINOR_VERSION':
    {
        'id':1050520,
        'type':'ViInt32',
        'enum':None,
        'access':'read only'
    },
    'CHANNEL_COUNT':
    {
        'id':1050203,
        'type':'ViInt32',
        'enum':None,
        'access':'read only'
    },
    'SUPPORTED_INSTRUMENT_MODELS':
    {
        'id':1050327,
        'type':'ViString',
        'enum':None,
        'access':'read only'
    },
    'GROUP_CAPABILITIES':
    {
        'id':1050401,
        'type':'ViString',
        'enum':None,
        'access':'read only'
    },
    'INSTRUMENT_MANUFACTURER':
    {
        'id':1050511,
        'type':'ViString',
        'enum':None,
        'access':'read only'
    },
    'INSTRUMENT_MODEL':
    {
        'id':1050512,
        'type':'ViString',
        'enum':None,
        'access':'read only'
    },
    'INSTRUMENT_FIRMWARE_REVISION':
    {
        'id':1050510,
        'type':'ViString',
        'enum':None,
        'access':'read only'
    },
    'LOGICAL_NAME':
    {
        'id':1050305,
        'type':'ViString',
        'enum':None,
        'access':'read only'
    },
    'IO_RESOURCE_DESCRIPTOR':
    {
        'id':1050304,
        'type':'ViString',
        'enum':None,
        'access':'read only'
    },
    'DRIVER_SETUP':
    {
        'id':1050007,
        'type':'ViString',
        'enum':None,
        'access':'read only'
    },
    'IO_SESSION':
    {
        'id':1050322,
        'type':'ViSession',
        'enum':None,
        'access':'read only'
    },
    'FUNCTION':
    {
        'id':1250001,
        'type':'ViInt32',
        'enum':'Function',
        'access':'read-write'
    },
    'RANGE':
    {
        'id':1250002,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'RESOLUTION_ABSOLUTE':
    {
        'id':1250008,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'RESOLUTION_DIGITS':
    {
        'id':1250003,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'TRIGGER_DELAY':
    {
        'id':1250005,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'TRIGGER_SOURCE':
    {
        'id':1250004,
        'type':'ViInt32',
        'enum':None,
        'access':'read-write'
    },
    'AC_MAX_FREQ':
    {
        'id':1250007,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'AC_MIN_FREQ':
    {
        'id':1250006,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'FREQ_VOLTAGE_RANGE':
    {
        'id':1250101,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'MEAS_COMPLETE_DEST':
    {
        'id':1250305,
        'type':'ViInt32',
        'enum':None,
        'access':'read-write'
    },
    'SAMPLE_COUNT':
    {
        'id':1250301,
        'type':'ViInt32',
        'enum':None,
        'access':'read-write'
    },
    'SAMPLE_INTERVAL':
    {
        'id':1250303,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'SAMPLE_TRIGGER':
    {
        'id':1250302,
        'type':'ViInt32',
        'enum':None,
        'access':'read-write'
    },
    'TRIGGER_COUNT':
    {
        'id':1250304,
        'type':'ViInt32',
        'enum':None,
        'access':'read-write'
    },
    'APERTURE_TIME':
    {
        'id':1250321,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'APERTURE_TIME_UNITS':
    {
        'id':1250322,
        'type':'ViInt32',
        'enum':'ApertureTimeUnits',
        'access':'read-write'
    },
    'AUTO_RANGE_VALUE':
    {
        'id':1250331,
        'type':'ViReal64',
        'enum':None,
        'access':'read only'
    },
    'AUTO_ZERO':
    {
        'id':1250332,
        'type':'ViInt32',
        'enum':'EnabledSetting',
        'access':'read-write'
    },
    'POWERLINE_FREQ':
    {
        'id':1250333,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'TRIGGER_SLOPE':
    {
        'id':1250334,
        'type':'ViInt32',
        'enum':'Slope',
        'access':'read-write'
    },
    'SAMPLE_TRIGGER_SLOPE':
    {
        'id':1150010,
        'type':'ViInt32',
        'enum':'Slope',
        'access':'read-write'
    },
    'MEAS_DEST_SLOPE':
    {
        'id':1150002,
        'type':'ViInt32',
        'enum':'Slope',
        'access':'read-write'
    },
    'ADC_CALIBRATION':
    {
        'id':1150022,
        'type':'ViInt32',
        'enum':'EnabledSetting',
        'access':'read-write'
    },
    'OFFSET_COMP_OHMS':
    {
        'id':1150023,
        'type':'ViInt32',
        'enum':'EnabledSetting',
        'access':'read-write'
    },
    'NUMBER_OF_AVERAGES':
    {
        'id':1150032,
        'type':'ViInt32',
        'enum':None,
        'access':'read-write'
    },
    'CURRENT_SOURCE':
    {
        'id':1150025,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'DC_NOISE_REJECTION':
    {
        'id':1150026,
        'type':'ViInt32',
        'enum':'DCNoiseRejectionMode',
        'access':'read-write'
    },
    'SETTLE_TIME':
    {
        'id':1150028,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'INPUT_RESISTANCE':
    {
        'id':1150029,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'LATENCY':
    {
        'id':1150034,
        'type':'ViInt32',
        'enum':None,
        'access':'read-write'
    },
    'BUFFER_SIZE':
    {
        'id':1150037,
        'type':'ViInt32',
        'enum':None,
        'access':'read-write'
    },
    'SHUNT_VALUE':
    {
        'id':1150003,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'OPERATION_MODE':
    {
        'id':1150014,
        'type':'ViInt32',
        'enum':'OperationMode',
        'access':'read-write'
    },
    'WAVEFORM_RATE':
    {
        'id':1150018,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'WAVEFORM_POINTS':
    {
        'id':1150019,
        'type':'ViInt32',
        'enum':None,
        'access':'read-write'
    },
    'WAVEFORM_COUPLING':
    {
        'id':1150027,
        'type':'ViInt32',
        'enum':'WaveformCouplingMode',
        'access':'read-write'
    },
    'FREQ_VOLTAGE_AUTO_RANGE_VALUE':
    {
        'id':1150044,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'CABLE_COMP_TYPE':
    {
        'id':1150045,
        'type':'ViInt32',
        'enum':'CableCompensationType',
        'access':'read-write'
    },
    'SHORT_CABLE_COMP_REACTANCE':
    {
        'id':1150046,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'SHORT_CABLE_COMP_RESISTANCE':
    {
        'id':1150047,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'OPEN_CABLE_COMP_SUSCEPTANCE':
    {
        'id':1150048,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'OPEN_CABLE_COMP_CONDUCTANCE':
    {
        'id':1150049,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'LC_CALCULATION_MODEL':
    {
        'id':1150052,
        'type':'ViInt32',
        'enum':'LCCalculationModel',
        'access':'read-write'
    },
    'DC_BIAS':
    {
        'id':1150053,
        'type':'ViInt32',
        'enum':None,
        'access':'read-write'
    },
    'LC_NUMBER_MEAS_TO_AVERAGE':
    {
        'id':1150055,
        'type':'ViInt32',
        'enum':None,
        'access':'read-write'
    },
    'SERIAL_NUMBER':
    {
        'id':1150054,
        'type':'ViString',
        'enum':None,
        'access':'read only'
    },
    'CONFIG_PRODUCT_NUMBER':
    {
        'id':1150061,
        'type':'ViInt32',
        'enum':None,
        'access':'read only'
    },
    'TEMP_TRANSDUCER_TYPE':
    {
        'id':1250201,
        'type':'ViInt32',
        'enum':'TemperatureTransducerType',
        'access':'read-write'
    },
    'TEMP_TC_REF_JUNC_TYPE':
    {
        'id':1250232,
        'type':'ViInt32',
        'enum':'TemperatureThermocoupleReferenceJunctionType',
        'access':'read-write'
    },
    'TEMP_TC_TYPE':
    {
        'id':1250231,
        'type':'ViInt32',
        'enum':'TemperatureThermocoupleType',
        'access':'read-write'     },
    'TEMP_TC_FIXED_REF_JUNC':

    {
        'id':1250233,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'TEMP_RTD_TYPE':
    {
        'id':1150120,
        'type':'ViInt32',
        'enum':'TemperatureRTDType',
        'access':'read-write'
    },
    'TEMP_RTD_RES':
    {
        'id':1250242,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'TEMP_RTD_A':
    {
        'id':1150121,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'TEMP_RTD_B':
    {
        'id':1150122,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'TEMP_RTD_C':
    {
        'id':1150123,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'TEMP_THERMISTOR_TYPE':
    {
        'id':1150124,
        'type':'ViInt32',
        'enum':'TemperatureThermistorType',
        'access':'read-write'
    },
    'TEMP_THERMISTOR_A':
    {
        'id':1150125,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'TEMP_THERMISTOR_B':
    {
        'id':1150126,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    },
    'TEMP_THERMISTOR_C':
    {
        'id':1150127,
        'type':'ViReal64',
        'enum':None,
        'access':'read-write'
    }
}

# TODO(marcoskirsch): Need to fill in enum information for those parameters that require it.
functions = [   {   'name': 'niDMM_init',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'resourceName', 'type': 'ViRsrc'},
                          {'direction': 'in', 'enum': None, 'name': 'IDQuery', 'type': 'ViBoolean'},
                          {'direction': 'in', 'enum': None, 'name': 'reset', 'type': 'ViBoolean'},
                          {'direction': 'out', 'enum': None, 'name': 'newVi', 'type': 'ViSession'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_InitWithOptions',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'resourceName', 'type': 'ViRsrc'},
                          {'direction': 'in', 'enum': None, 'name': 'IDQuery', 'type': 'ViBoolean'},
                          {'direction': 'in', 'enum': None, 'name': 'resetDevice', 'type': 'ViBoolean'},
                          {'direction': 'in', 'enum': None, 'name': 'optionsString', 'type': 'ViString'},
                          {'direction': 'out', 'enum': None, 'name': 'newVi', 'type': 'ViSession'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_close',
        'parameters': [{'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetError',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'out', 'enum': None, 'name': 'errorCode', 'type': 'ViStatus'},
                          {'direction': 'in', 'enum': None, 'name': 'bufferSize', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'description', 'type': 'ViChar'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetErrorMessage',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'errorCode', 'type': 'ViStatus'},
                          {'direction': 'in', 'enum': None, 'name': 'bufferSize', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'errMessage', 'type': 'ViChar'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ClearError',
        'parameters': [{'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_reset',
        'parameters': [{'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_self_test',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'out', 'enum': None, 'name': 'selfTestResult', 'type': 'ViInt16'},
                          {'direction': 'in', 'enum': None, 'name': 'selfTestMessage', 'type': 'ViChar'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_SelfCal',
        'parameters': [{'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_revision_query',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'driverRev', 'type': 'ViChar'},
                          {'direction': 'in', 'enum': None, 'name': 'instrRev', 'type': 'ViChar'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_InvalidateAllAttributes',
        'parameters': [{'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ResetWithDefaults',
        'parameters': [{'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_Disable',
        'parameters': [{'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetMeasurementPeriod',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'out', 'enum': None, 'name': 'period', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureTrigger',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'trigSource', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'triggerDelay', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_Read',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'maxTime', 'type': 'ViInt32'},
                          {'direction': 'out', 'enum': None, 'name': 'reading', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_Fetch',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'maxTime', 'type': 'ViInt32'},
                          {'direction': 'out', 'enum': None, 'name': 'reading', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_Abort',
        'parameters': [{'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_Initiate',
        'parameters': [{'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_IsOverRange',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'measurementValue', 'type': 'ViReal64'},
                          {'direction': 'out', 'enum': None, 'name': 'isOverRange', 'type': 'ViBoolean'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_IsUnderRange',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'measurementValue', 'type': 'ViReal64'},
                          {'direction': 'out', 'enum': None, 'name': 'isUnderRange', 'type': 'ViBoolean'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureACBandwidth',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'minFreq', 'type': 'ViReal64'},
                          {'direction': 'in', 'enum': None, 'name': 'maxFreq', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureFrequencyVoltageRange',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'frequencyVoltageRange', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureMeasCompleteDest',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'destination', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureMultiPoint',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'triggerCount', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'sampleCount', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'sampleTrigger', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'sampleInterval', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ReadMultiPoint',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'maxTime', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'arraySize', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'readingArray', 'type': 'ViReal64'},
                          {'direction': 'out', 'enum': None, 'name': 'actualPts', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_FetchMultiPoint',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'maxTime', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'arraySize', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'readingArray', 'type': 'ViReal64'},
                          {'direction': 'out', 'enum': None, 'name': 'actualPts', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureTriggerSlope',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'polarity', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_SendSoftwareTrigger',
        'parameters': [{'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetApertureTimeInfo',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'out', 'enum': None, 'name': 'apertureTime', 'type': 'ViReal64'},
                          {'direction': 'out', 'enum': 'ApertureTimeUnits', 'name': 'apertureTimeUnits', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetAutoRangeValue',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'out', 'enum': None, 'name': 'autoRangeValue', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureAutoZeroMode',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'autoZeroMode', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigurePowerLineFrequency',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'frequency', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureMeasurementDigits',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'measFunction', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'range', 'type': 'ViReal64'},
                          {'direction': 'in', 'enum': None, 'name': 'resolutionDigits', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureMeasurementAbsolute',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'measFunction', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'range', 'type': 'ViReal64'},
                          {'direction': 'in', 'enum': None, 'name': 'resolutionAbsolute', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureMeasCompleteSlope',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'polarity', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureSampleTriggerSlope',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'polarity', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ReadStatus',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'out', 'enum': None, 'name': 'acqBacklog', 'type': 'ViInt32'},
                          {'direction': 'out', 'enum': None, 'name': 'acqDone', 'type': 'ViInt16'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_Control',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'action', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureADCCalibration',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'adcGainComp', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureOffsetCompOhms',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'offsetCompOhms', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureCurrentSource',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'diodeCurrentSrc', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureCableCompType',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'typeOfCompensation', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_PerformOpenCableComp',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'out', 'enum': None, 'name': 'conductance', 'type': 'ViReal64'},
                          {'direction': 'out', 'enum': None, 'name': 'susceptance', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_PerformShortCableComp',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'out', 'enum': None, 'name': 'resistance', 'type': 'ViReal64'},
                          {'direction': 'out', 'enum': None, 'name': 'reactance', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureOpenCableCompValues',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'conductance', 'type': 'ViReal64'},
                          {'direction': 'in', 'enum': None, 'name': 'susceptance', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureShortCableCompValues',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'resistance', 'type': 'ViReal64'},
                          {'direction': 'in', 'enum': None, 'name': 'reactance', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_LockSession',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'out', 'enum': None, 'name': 'callerHasLock', 'type': 'ViBoolean'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_UnlockSession',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'out', 'enum': None, 'name': 'callerHasLock', 'type': 'ViBoolean'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureWaveformAcquisition',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'function', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'range', 'type': 'ViReal64'},
                          {'direction': 'in', 'enum': None, 'name': 'rate', 'type': 'ViReal64'},
                          {'direction': 'in', 'enum': None, 'name': 'waveformPoints', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureWaveformCoupling',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'coupling', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_FetchWaveform',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'maxTime', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'arraySize', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'waveformArray', 'type': 'ViReal64'},
                          {'direction': 'out', 'enum': None, 'name': 'actualPoints', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ReadWaveform',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'maxTime', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'arraySize', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'waveformArray', 'type': 'ViReal64'},
                          {'direction': 'out', 'enum': None, 'name': 'actualPoints', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetAttributeViInt32',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'channelName', 'type': 'ViConstString'},
                          {'direction': 'in', 'enum': None, 'name': 'attributeId', 'type': 'ViAttr'},
                          {'direction': 'out', 'enum': None, 'name': 'value', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_SetAttributeViInt32',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'channelName', 'type': 'ViConstString'},
                          {'direction': 'in', 'enum': None, 'name': 'attributeId', 'type': 'ViAttr'},
                          {'direction': 'in', 'enum': None, 'name': 'value', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_CheckAttributeViInt32',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'channelName', 'type': 'ViConstString'},
                          {'direction': 'in', 'enum': None, 'name': 'attributeId', 'type': 'ViAttr'},
                          {'direction': 'in', 'enum': None, 'name': 'value', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetAttributeViReal64',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'channelName', 'type': 'ViConstString'},
                          {'direction': 'in', 'enum': None, 'name': 'attributeId', 'type': 'ViAttr'},
                          {'direction': 'out', 'enum': None, 'name': 'value', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_SetAttributeViReal64',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'channelName', 'type': 'ViConstString'},
                          {'direction': 'in', 'enum': None, 'name': 'attributeId', 'type': 'ViAttr'},
                          {'direction': 'in', 'enum': None, 'name': 'value', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_CheckAttributeViReal64',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'channelName', 'type': 'ViConstString'},
                          {'direction': 'in', 'enum': None, 'name': 'attributeId', 'type': 'ViAttr'},
                          {'direction': 'in', 'enum': None, 'name': 'value', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetAttributeViString',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'channelName', 'type': 'ViConstString'},
                          {'direction': 'in', 'enum': None, 'name': 'attributeId', 'type': 'ViAttr'},
                          {'direction': 'in', 'enum': None, 'name': 'bufSize', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'value', 'type': 'ViChar'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_SetAttributeViString',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'channelName', 'type': 'ViConstString'},
                          {'direction': 'in', 'enum': None, 'name': 'attributeId', 'type': 'ViAttr'},
                          {'direction': 'in', 'enum': None, 'name': 'value', 'type': 'ViChar'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_CheckAttributeViString',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'channelName', 'type': 'ViConstString'},
                          {'direction': 'in', 'enum': None, 'name': 'attributeId', 'type': 'ViAttr'},
                          {'direction': 'in', 'enum': None, 'name': 'value', 'type': 'ViChar'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetAttributeViSession',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'channelName', 'type': 'ViConstString'},
                          {'direction': 'in', 'enum': None, 'name': 'attributeId', 'type': 'ViAttr'},
                          {'direction': 'out', 'enum': None, 'name': 'value', 'type': 'ViSession'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_SetAttributeViSession',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'channelName', 'type': 'ViConstString'},
                          {'direction': 'in', 'enum': None, 'name': 'attributeId', 'type': 'ViAttr'},
                          {'direction': 'in', 'enum': None, 'name': 'value', 'type': 'ViSession'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_CheckAttributeViSession',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'channelName', 'type': 'ViConstString'},
                          {'direction': 'in', 'enum': None, 'name': 'attributeId', 'type': 'ViAttr'},
                          {'direction': 'in', 'enum': None, 'name': 'value', 'type': 'ViSession'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetAttributeViBoolean',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'channelName', 'type': 'ViConstString'},
                          {'direction': 'in', 'enum': None, 'name': 'attributeId', 'type': 'ViAttr'},
                          {'direction': 'out', 'enum': None, 'name': 'value', 'type': 'ViBoolean'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_SetAttributeViBoolean',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'channelName', 'type': 'ViConstString'},
                          {'direction': 'in', 'enum': None, 'name': 'attributeId', 'type': 'ViAttr'},
                          {'direction': 'in', 'enum': None, 'name': 'value', 'type': 'ViBoolean'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_CheckAttributeViBoolean',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'channelName', 'type': 'ViConstString'},
                          {'direction': 'in', 'enum': None, 'name': 'attributeId', 'type': 'ViAttr'},
                          {'direction': 'in', 'enum': None, 'name': 'value', 'type': 'ViBoolean'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetNextCoercionRecord',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'bufferSize', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'record', 'type': 'ViChar'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetNextInterchangeWarning',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'bufferSize', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'warnString', 'type': 'ViChar'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ResetInterchangeCheck',
        'parameters': [{'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ClearInterchangeWarnings',
        'parameters': [{'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_4022Control',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'resourceName', 'type': 'ViRsrc'},
                          {'direction': 'in', 'enum': None, 'name': 'configuration', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetChannelName',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'index', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'bufferSize', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'name', 'type': 'ViChar'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_InitExtCal',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'resourceName', 'type': 'ViRsrc'},
                          {'direction': 'in', 'enum': None, 'name': 'password', 'type': 'ViChar'},
                          {'direction': 'out', 'enum': None, 'name': 'newVi', 'type': 'ViSession'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_CloseExtCal',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'action', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_CalAdjustLinearization',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'mode', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'range', 'type': 'ViReal64'},
                          {'direction': 'in', 'enum': None, 'name': 'inputR', 'type': 'ViReal64'},
                          {'direction': 'in', 'enum': None, 'name': 'expectedValue', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_CalAdjustGain',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'mode', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'range', 'type': 'ViReal64'},
                          {'direction': 'in', 'enum': None, 'name': 'inputR', 'type': 'ViReal64'},
                          {'direction': 'in', 'enum': None, 'name': 'expectedValue', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_CalAdjustOffset',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'mode', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'range', 'type': 'ViReal64'},
                          {'direction': 'in', 'enum': None, 'name': 'inputR', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_CalAdjustMisc',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'type', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_CalAdjustLC',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'type', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_CalAdjustACFilter',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'mode', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'range', 'type': 'ViReal64'},
                          {'direction': 'in', 'enum': None, 'name': 'frequency', 'type': 'ViReal64'},
                          {'direction': 'in', 'enum': None, 'name': 'expectedValue', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_RestoreLastExtCalConstants',
        'parameters': [{'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_SetCalPassword',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'oldPassword', 'type': 'ViChar'},
                          {'direction': 'in', 'enum': None, 'name': 'newPassword', 'type': 'ViChar'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetExtCalRecommendedInterval',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'out', 'enum': None, 'name': 'months', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_SetCalUserDefinedInfo',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'info', 'type': 'ViChar'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetCalUserDefinedInfoMaxSize',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'out', 'enum': None, 'name': 'infoSize', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetCalUserDefinedInfo',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'bufferSize', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'info', 'type': 'ViChar'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetSelfCalSupported',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'out', 'enum': None, 'name': 'selfCalSupported', 'type': 'ViBoolean'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetCalDateAndTime',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'calType', 'type': 'ViInt32'},
                          {'direction': 'out', 'enum': None, 'name': 'month', 'type': 'ViInt32'},
                          {'direction': 'out', 'enum': None, 'name': 'day', 'type': 'ViInt32'},
                          {'direction': 'out', 'enum': None, 'name': 'year', 'type': 'ViInt32'},
                          {'direction': 'out', 'enum': None, 'name': 'hour', 'type': 'ViInt32'},
                          {'direction': 'out', 'enum': None, 'name': 'minute', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetCalCount',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'calType', 'type': 'ViInt32'},
                          {'direction': 'out', 'enum': None, 'name': 'count', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetLastCalTemp',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'calType', 'type': 'ViInt32'},
                          {'direction': 'out', 'enum': None, 'name': 'temperature', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_GetDevTemp',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'reserved', 'type': 'ViString'},
                          {'direction': 'out', 'enum': None, 'name': 'temperature', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureTransducerType',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'transducerType', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureThermocouple',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'thermocoupleType', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'refJunctionType', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureFixedRefJunction',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'fixedRefJunction', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureRTDType',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'rtdType', 'type': 'ViInt32'},
                          {'direction': 'in', 'enum': None, 'name': 'resistance', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureRTDCustom',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'a', 'type': 'ViReal64'},
                          {'direction': 'in', 'enum': None, 'name': 'b', 'type': 'ViReal64'},
                          {'direction': 'in', 'enum': None, 'name': 'c', 'type': 'ViReal64'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureThermistorType',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'thermistorType', 'type': 'ViInt32'}],
        'returns': 'ViStatus'},
    {   'name': 'niDMM_ConfigureThermistorCustom',
        'parameters': [   {'direction': 'in', 'enum': None, 'name': 'vi', 'type': 'ViSession'},
                          {'direction': 'in', 'enum': None, 'name': 'a', 'type': 'ViReal64'},
                          {'direction': 'in', 'enum': None, 'name': 'b', 'type': 'ViReal64'},
                          {'direction': 'in', 'enum': None, 'name': 'c', 'type': 'ViReal64'}],
        'returns': 'ViStatus'}]


enums = {

    'ApertureTimeUnits': [
        {'name': 'SECONDS', 'value': 0},
        {'name': 'POWER_LINE_CYCLES', 'value': 1},
        {'name': 'RAW_SAMPLES', 'value': 2},
    ],

    'CableCompensationType': [
        {'name': 'CABLE_COMP_NONE'             , 'value': 0},
        {'name': 'CABLE_COMP_OPEN'             , 'value': 1},
        {'name': 'CABLE_COMP_SHORT'            , 'value': 2},
        {'name': 'CABLE_COMP_OPEN_AND_SHORT'   , 'value': 3},
    ],

    'DCNoiseRejectionMode': [
        {'name': 'DCNR_AUTO'           , 'value': -1},
        {'name': 'DCNR_NORMAL'         , 'value':  0},
        {'name': 'DCNR_SECOND_ORDERT'  , 'value':  1},
        {'name': 'DCNR_HIGH_ORDER'     , 'value':  2},
    ],

    'EnabledSetting': [
        {'name': 'AUTO' , 'value': -1},
        {'name': 'OFF'  , 'value':  0},
        {'name': 'ON'   , 'value':  1},
        {'name': 'ONCE' , 'value':  2},
    ],

    'Function': [
        {'name': 'DC_VOLTS'            , 'value':    1},
        {'name': 'AC_VOLTS'            , 'value':    2},
        {'name': 'DC_CURRENT'          , 'value':    3},
        {'name': 'AC_CURRENT'          , 'value':    4},
        {'name': 'RES_2_WIRE'          , 'value':    5}, # Had to put RES_ in front, rather than in back, so name doesn't start with number.
        {'name': 'RES_4_WIRE'          , 'value':  101}, # Had to put RES_ in front, rather than in back, so name doesn't start with number.
        {'name': 'FREQ'                , 'value':  104},
        {'name': 'PERIOD'              , 'value':  105},
        {'name': 'TEMPERATURE'         , 'value':  108},
        {'name': 'AC_VOLTS_DC_COUPLED' , 'value': 1001},
        {'name': 'DIODE'               , 'value': 1002},
        {'name': 'WAVEFORM_VOLTAGE'    , 'value': 1003},
        {'name': 'WAVEFORM_CURRENT'    , 'value': 1004},
        {'name': 'CAPACITANCE'         , 'value': 1005},
        {'name': 'INDUCTANCE'          , 'value': 1006},
    ],

    'LCCalculationModel': [
        {'name': 'CALC_MODEL_AUTO'     , 'value': -1},
        {'name': 'CALC_MODEL_SERIES'   , 'value':  0},
        {'name': 'CALC_MODEL_PARALLEL' , 'value':  1},
    ],

    'OperationMode': [
        {'name': 'DMM_MODE'        , 'value': 0},
        {'name': 'WAVEFORM_MODE'   , 'value': 1},
    ],

    'Slope': [
        {'name': 'POSITIVE' , 'value': 0},
        {'name': 'NEGATIVE' , 'value': 1},
    ],

    'TemperatureRTDType': [
        {'name': 'CustomRTD', 'value': 0},
        {'name': 'PT3750'   , 'value': 1},
        {'name': 'PT3851'   , 'value': 2},
        {'name': 'PT3911'   , 'value': 3},
        {'name': 'PT3916'   , 'value': 4},
        {'name': 'PT3920'   , 'value': 5},
        {'name': 'PT3928'   , 'value': 6},
    ],

    'TemperatureThermistorType': [
        {'name': 'THERMISTOR_CUSTOM', 'value': 0},
        {'name': 'THERMISTOR_44004' , 'value': 1},
        {'name': 'THERMISTOR_44006' , 'value': 2},
        {'name': 'THERMISTOR_44007' , 'value': 3},
    ],

    'TemperatureThermocoupleReferenceJunctionType': [
        {'name': 'Fixed', 'value': 2},
    ],

    'TemperatureThermocoupleType': [
        {'name': 'B', 'value':  1},
        {'name': 'E', 'value':  4},
        {'name': 'J', 'value':  6},
        {'name': 'K', 'value':  7},
        {'name': 'N', 'value':  8},
        {'name': 'R', 'value':  9},
        {'name': 'S', 'value': 10},
        {'name': 'T', 'value': 11},
    ],

    'TemperatureTransducerType': [
        {'name': 'THERMOCOUPLE', 'value':  1},
        {'name': 'THERMISTOR'  , 'value':  2},
        {'name': 'RTD_2_WIRE'  , 'value':  3}, # Had to put RTD in front, rather than in back, so name doesn't start with number.
        {'name': 'RTD_4_WIRE'  , 'value':  4}, # Had to put RTD in front, rather than in back, so name doesn't start with number.
    ],

    'WaveformCouplingMode': [
        {'name': 'WAVEFORM_COUPLING_AC', 'value':  0},
        {'name': 'WAVEFORM_COUPLING_DC', 'value':  1},
    ],

}


