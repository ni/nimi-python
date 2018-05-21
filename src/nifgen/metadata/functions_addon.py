# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
    'init':                                 { 'codegen_method': 'no',       },
    'InitWithOptions':                      { 'codegen_method': 'no',       },
    'InitializeWithChannels':               { 'codegen_method': 'private', 'method_name_for_documentation': '__init__', },
    'close':                                { 'codegen_method': 'private',  },
    'CheckAttribute.*':                     { 'codegen_method': 'no',       },  # Not supported in Python API. Issue #529
    'InitiateGeneration':                   { 'codegen_method': 'private', 'method_name_for_documentation': 'initiate', },
    'Configure.*':                          { 'codegen_method': 'no',       },  # Use corresponding attribute instead
    'ConfigureArbSequence':                 { 'codegen_method': 'public',   },
    'ConfigureArbWaveform':                 { 'codegen_method': 'public',   },
    'ConfigureArbWaveform':                 { 'codegen_method': 'public',   },
    'ConfigureCustomFIRFilterCoefficients': { 'codegen_method': 'public',   },
    'ConfigureDigitalEdgeScriptTrigger':    { 'codegen_method': 'public',   },
    'ConfigureDigitalEdgeStartTrigger':     { 'codegen_method': 'public',   },
    'ConfigureDigitalLevelScriptTrigger':   { 'codegen_method': 'public',   },
    'ConfigureFreqList':                    { 'codegen_method': 'public',   },
    'ConfigureStandardWaveform':            { 'codegen_method': 'public',   },
    'ExportSignal':                         { 'codegen_method': 'no',       },  # remove export signal #828 - additional metadata removed #870
    'CreateWaveformF64':                    { 'codegen_method': 'private', 'method_name_for_documentation': 'create_waveform', },  # Called from public method create_waveform()
    'CreateWaveformI16':                    { 'codegen_method': 'private', 'method_name_for_documentation': 'create_waveform', },  # Called from public method create_waveform()
    'WriteBinary16Waveform':                { 'codegen_method': 'private', 'method_name_for_documentation': 'write_waveform', },  # Called from public method write_waveform()
    'WriteNamedWaveformF64':                { 'codegen_method': 'private', 'method_name_for_documentation': 'write_waveform', },  # Called from public method write_waveform()
    'WriteNamedWaveformI16':                { 'codegen_method': 'private', 'method_name_for_documentation': 'write_waveform', },  # Called from public method write_waveform()
    'WriteWaveform':                        { 'codegen_method': 'private', 'method_name_for_documentation': 'write_waveform', },  # Called from public method write_waveform()
    'Disable.+':                            { 'codegen_method': 'no',       },  # Use corresponding attribute instead
    'Enable.+':                             { 'codegen_method': 'no',       },  # Use corresponding attribute instead
    'P2P':                                  { 'codegen_method': 'no',       },  # P2P not supported in Python API
    'HWS':                                  { 'codegen_method': 'no',       },  # HWS is dead!
    'ResetAttribute':                       { 'codegen_method': 'no',       },  # Issue #531
    'RouteSignalOut':                       { 'codegen_method': 'no',       },  # Use string-based routing instead
    'WriteBinary16AnalogStaticValue':       { 'codegen_method': 'no',       },  # Use corresponding attribute instead
    'CreateArbWaveform':                    { 'codegen_method': 'no',       },  # Obsoleted before initial Python release
    'CreateBinary16ArbWaveform':            { 'codegen_method': 'no',       },  # Obsoleted before initial Python release
    'SendSoftwareTrigger':                  { 'codegen_method': 'no',       },  # Obsoleted before initial Python release
    '.etAttribute.+':                       { 'codegen_method': 'private',  },  # All Set/Get Attribute functions are private
    'error_message':                        { 'codegen_method': 'private',  },
    'GetError':                             { 'codegen_method': 'private',  },
    'ClearError':                           { 'codegen_method': 'no',       },
    'ErrorHandler':                         { 'codegen_method': 'no',       },
    'LockSession':                          { 'codegen_method': 'no',       },
    'UnlockSession':                        { 'codegen_method': 'no',       },
    'InitExtCal':                           { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'CloseExtCal':                          { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'RestoreLastExtCalConstants':           { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'ChangeExtCalPassword':                 { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'CalAdjust.+':                          { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'Initialize.+Calibration':              { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'ReadCalADC':                           { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    '.+UserDefined.+':                      { 'codegen_method': 'no',       },
    'SetAttributeViSession':                { 'codegen_method': 'no',       },
    'GetAttributeViSession':                { 'codegen_method': 'no',       },
    'GetNextInterchangeWarning':            { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ResetInterchangeCheck':                { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ClearInterchangeWarnings':             { 'codegen_method': 'no',       },  # Not applicable to Python API
    'GetNextCoercionRecord':                { 'codegen_method': 'no',       },  # Not applicable to Python API
    'error_query':                          { 'codegen_method': 'no',       },
    'revision_query':                       { 'codegen_method': 'no',       },
    '.+Complex.+':                          { 'codegen_method': 'no',       },
    'GetStreamEndpointHandle':              { 'codegen_method': 'no',       },
    'AdjustSampleClockRelativeDelay':       { 'codegen_method': 'no',       },  # This is used internally by NI-TClk, but not by end users.
    '.etAttributeViInt64':                  { 'codegen_method': 'no',       },  # NI-FGEN has no ViInt64 attributes.
    'GetExtCalLastDateAndTime':             { 'codegen_method': 'private', 'method_name_for_documentation': 'get_ext_cal_last_date_and_time',  },  # 'GetLastExtCalLastDateAndTime' Public wrapper to allow datetime
    'GetSelfCalLastDateAndTime':            { 'codegen_method': 'private', 'method_name_for_documentation': 'get_self_cal_last_date_and_time', },  # 'GetLastSelfCalLastDateAndTime' Public wrapper to allow datetime
    'self_test':                            { 'codegen_method': 'private', 'method_name_for_documentation': 'self_test',                       },  # 'fancy_self_test' Public wrapper that raises
}

# Attach the given parameter to the given enum from enums.py
functions_enums = {
    'CreateFreqList':                           { 'parameters': { 1: { 'enum': 'Waveform',                  }, }, },
    'CreateWaveformFromFileF64':                { 'parameters': { 3: { 'enum': 'ByteOrder',                 }, }, },
    'CreateWaveformFromFileI16':                { 'parameters': { 3: { 'enum': 'ByteOrder',                 }, }, },
    'ConfigureDigitalEdgeScriptTrigger':        { 'parameters': { 3: { 'enum': 'ScriptTriggerDigitalEdgeEdge', }, }, },
    'ConfigureDigitalEdgeStartTrigger':         { 'parameters': { 2: { 'enum': 'StartTriggerDigitalEdgeEdge', }, }, },
    'ConfigureStandardWaveform':                { 'parameters': { 2: { 'enum': 'Waveform' }, }, },
    'SetNamedWaveformNextWritePosition':        { 'parameters': { 3: { 'enum': 'RelativeTo',                }, }, },
    'SetWaveformNextWritePosition':             { 'parameters': { 3: { 'enum': 'RelativeTo',                }, }, },
    'GetHardwareState':                         { 'parameters': { 1: { 'enum': 'HardwareState',             }, }, },
    'SendSoftwareEdgeTrigger':                  { 'parameters': { 1: { 'enum': 'Trigger',                   }, }, },  # TODO: issue #538
    'ConfigureDigitalLevelScriptTrigger':       { 'parameters': { 3: { 'enum': 'TriggerWhen',               }, }, },
}

# Need to manually set some repeated capabilities
functions_rep_caps = {
    'ConfigureDigitalEdgeScriptTrigger':        { 'parameters': { 1: { 'is_repeated_capability': True, }, }, },
    'ConfigureDigitalLevelScriptTrigger':       { 'parameters': { 1: { 'is_repeated_capability': True, }, }, },
    # 'SendSoftwareEdgeTrigger':                  { 'parameters': { 2: { 'is_repeated_capability': True, }, }, }, # 850
}

functions_issues = {
    'GetFIRFilterCoefficients':             { 'parameters': { 3: { 'direction':'out'},  # TODO(marcoskirsch): Remove when #534 solved
                                                              4: { 'direction':'out', 'is_buffer': False, 'type':'ViInt32', }, }, },
}

# This is the additional metadata needed by the code generator in order create code that can properly handle buffer allocation.
functions_buffer_info = {
    'GetError':                             { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'errorDescriptionBufferSize'}, }, }, },
    'self_test':                            { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'GetAttributeViString':                 { 'parameters': { 4: { 'size': {'mechanism':'ivi-dance', 'value':'arraySize'}, }, }, },
    'GetCalUserDefinedInfo':                { 'parameters': { 1: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From LabVIEW VI, even though niDMM_GetCalUserDefinedInfoMaxSize() exists.
    'error_message':                        { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'ConfigureCustomFIRFilterCoefficients': { 'parameters': { 3: { 'size': {'mechanism':'len', 'value':'numberOfCoefficients'}, }, }, },
    'CreateWaveform(I16|F64)':              { 'parameters': { 3: { 'size': {'mechanism':'len', 'value':'waveformSize'}, }, }, },
    'DefineUserStandardWaveform':           { 'parameters': { 3: { 'size': {'mechanism':'len', 'value':'waveformSize'}, }, }, },
    'GetFIRFilterCoefficients':             { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'arraySize'}, }, }, },  # TODO(marcoskirsch): #537
    'Write.*Waveform':                      { 'parameters': { 4: { 'size': {'mechanism':'len', 'value':'Size'}, }, }, },
    'CreateAdvancedArbSequence':            { 'parameters': { 2: { 'size': {'mechanism':'len', 'value':'sequenceLength'}, },
                                                              3: { 'size': {'mechanism':'len', 'value':'sequenceLength'}, },
                                                              4: { 'size': {'mechanism':'len', 'value':'sequenceLength'}, },
                                                              5: { 'size': {'mechanism':'len', 'value':'sequenceLength'}, },
                                                              6: { 'size': {'mechanism':'python-code', 'value':'(0 if marker_location_array is None else len(marker_location_array))'}, }, }, },  # TODO(marcoskirsch): Suffers from #515
    'CreateArbSequence':                    { 'parameters': { 2: { 'size': {'mechanism':'len', 'value':'sequenceLength'}, }, }, },  # TODO(marcoskirsch): Suffers from #515
    'CreateFreqList':                       { 'parameters': { 3: { 'size': {'mechanism':'len', 'value':'frequencyListLength'}, }, }, },  # TODO(marcoskirsch): Suffers from #515
}

# These are functions we mark as "error_handling":True. The generator uses this information to
# change how error handling is done within those functions themselves - basically, if an error occurs,
# dont try to handle it, since the functions are only used within the context of error handling.
functions_is_error_handling = {
    'error_message':                { 'is_error_handling': True },
    'GetError':                     { 'is_error_handling': True },
}

# Default values for method parameters
functions_default_value = {
    'InitializeWithChannels':                       { 'parameters': { 1: { 'default_value': None, },
                                                                      2: { 'default_value': False, },
                                                                      3: { 'default_value': '""', }, }, },
    'ConfigureFreqList':                            { 'parameters': { 4: { 'default_value': 0.0, },
                                                                      5: { 'default_value': 0.0, }, }, },
    'ConfigureStandardWaveform':                    { 'parameters': { 4: { 'default_value': 0.0, },
                                                                      6: { 'default_value': 0.0, }, }, },
    'ConfigureDigitalEdgeScriptTrigger':            { 'parameters': { 3: { 'default_value': 'ScriptTriggerDigitalEdgeEdge.RISING', }, }, },
    'ConfigureDigitalEdgeStartTrigger':             { 'parameters': { 2: { 'default_value': 'StartTriggerDigitalEdgeEdge.RISING', }, }, },
    'CreateAdvancedArbSequence':                    { 'parameters': { 4: { 'default_value': None, },
                                                                      5: { 'default_value': None, }, }, },
    'WaitUntilDone':                                { 'parameters': { 1: { 'default_value': 'datetime.timedelta(seconds=10.0)', }, }, },
}

# Converted parameters
functions_converters = {
    'AdjustSampleClockRelativeDelay':               { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                           'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'WaitUntilDone':                                { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                                                                           'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'InitializeWithChannels':                       { 'parameters': { 3: { 'python_api_converter_name': 'convert_init_with_options_dictionary', 
                                                                           'type_in_documentation': 'dict', }, 
                                                                      1: { 'is_repeated_capability': False,
                                                                           'python_api_converter_name': 'convert_repeated_capabilities_from_init', 
                                                                           'type_in_documentation': 'str, list, range, tuple', }, }, },
    'GetExtCalRecommendedInterval':                 { 'parameters': { 1: { 'python_api_converter_name': 'convert_month_to_timedelta', 
                                                                           'type_in_documentation': 'datetime.timedelta', }, }, },
}

# Functions not in original metadata.
functions_additional_functions = {
    # Public function that wraps self_test and will raise on self test failure
    'fancy_self_test': {
        'returns': 'ViStatus',
        'codegen_method': 'python-only',
        'python_name': 'self_test',
        'method_templates': [
            { 'session_filename': 'fancy_self_test', 'documentation_filename': 'default_method', 'method_python_name_suffix': '', },
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies your instrument session. **vi** is obtained from the niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels functions and identifies a particular instrument session.',
                },
            },
        ],
        'documentation': {
            'description': '''
Runs the instrument self-test routine and returns the test result(s).

Raises `SelfTestError` on self test failure. Attributes on exception object:

- code - failure code from driver
- message - status message from driver
''',
            'note': '''
When used on some signal generators, the device is reset after the
niFgen_self_test function runs. If you use the niFgen_self_test
function, your device may not be in its previously configured state
after the function runs.
''',
            'table_body': [['0', 'Passed self-test'], ['1', 'Self-test failed']],
            'table_header': ['Self-Test Code', 'Description'],
        },
    },
    'CreateWaveformDispatcher': {
        'codegen_method': 'python-only',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
            },
            {
                'direction': 'in',
                'name': 'waveformDataArray',
                'type': 'ViReal64[]',  #TODO(marcoskirsch): Don't care, except for documentation
                'documentation': {
                    'description': 'Array of data for the new arbitrary waveform. This may be an iterable of float, or for best performance a numpy.ndarray of dtype int16 or float64.',
                },
            },
            {
                'direction': 'out',
                'name': 'waveformHandle',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'The handle that identifies the new waveform. This handle is used in other methods when referring to this waveform.',
                },
            },
        ],
        'documentation': {
            'description': 'Creates an onboard waveform for use in Arbitrary Waveform output mode or Arbitrary Sequence output mode.',
            'note': 'You must set NIFGEN_ATTR_OUTPUT_MODE to NIFGEN_VAL_OUTPUT_ARB or NIFGEN_VAL_OUTPUT_SEQ before calling this function.',
        },
    },

    'WriteWaveformDispatcher': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString',
            },
            {
                'direction': 'in',
                'name': 'waveformNameOrHandle',
                'type': 'ViInt32',  #TODO(marcoskirsch): Don't care, except for documentation
                'documentation': {
                    'description': 'The name (str) or handle (int) of an arbitrary waveform previously allocated with niFgen_AllocateNamedWaveform or niFgen_AllocateWaveform.',
                },
            },
            {
                'direction': 'in',
                'name': 'Size',
                'type': 'ViInt32',
            },
            {
                'direction': 'in',
                'name': 'Data',
                'type': 'ViReal64[]',  #TODO(marcoskirsch): Don't care, except for documentation
                'documentation': {
                    'description': 'Array of data to load into the waveform. This may be an iterable of float, or for best performance a numpy.ndarray of dtype int16 or float64.',
                },
            },
        ],
        'documentation': {
            'description': '''Writes data to the waveform in onboard memory.

By default, subsequent calls to this function
continue writing data from the position of the last sample written. You
can set the write position and offset by calling the nifgen_SetNamedWaveformNextWritePosition
nifgen_SetWaveformNextWritePosition function.''',
        },
    },
    # Public function that wraps driver function but returns datetime object instead of individual items
    'GetLastExtCalLastDateAndTime': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'python_name': 'get_ext_cal_last_date_and_time',
        'real_datetime_call': 'GetExtCalLastDateAndTime',
        'method_templates': [
            { 'session_filename': 'datetime_wrappers', 'documentation_filename': 'default_method', 'method_python_name_suffix': '', },
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies your instrument session. **vi** is obtained from the nifgen_init or the nifgen_InitExtCal function and identifies a particular instrument session.',
                },
            },
            {
                'direction': 'out',
                'name': 'Month',
                'type': 'datetime.datetime',
                'documentation': {
                    'description': 'Indicates date and time of the last calibration.',
                },
            },
        ],
        'documentation': {
            'description': 'Returns the date and time of the last successful external calibration. The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30 PM, this function returns 14 for the **hour** parameter and 30 for the **minute** parameter.',
        },
    },
    'GetLastSelfCalLastDateAndTime': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'python_name': 'get_self_cal_last_date_and_time',
        'real_datetime_call': 'GetSelfCalLastDateAndTime',
        'method_templates': [
            { 'session_filename': 'datetime_wrappers', 'documentation_filename': 'default_method', 'method_python_name_suffix': '', },
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies your instrument session. **vi** is obtained from the nifgen_init or the nifgen_InitExtCal function and identifies a particular instrument session.',
                },
            },
            {
                'direction': 'out',
                'name': 'Month',
                'type': 'datetime.datetime',
                'documentation': {
                    'description': 'Returns the date and time the device was last calibrated.',
                },
            },
        ],
        'documentation': 
        {
            'description': 'Returns the date and time of the last successful self-calibration.',
        },
    },
}


# Override the 'python' name for some functions.
functions_python_name = {
    'AbortGeneration':                      { 'python_name': 'abort',                   },
    'CreateWaveformDispatcher':             { 'python_name': 'create_waveform'          },
    'WriteWaveformDispatcher':              { 'python_name': 'write_waveform'           },
}

functions_method_templates = {
    'CreateWaveformDispatcher':     { 'method_templates': [
        { 'session_filename': 'create_waveform', 'documentation_filename': 'default_method', 'method_python_name_suffix': '_numpy', },
    ], },
    'CreateWaveformF64':            { 'method_templates': [
        { 'session_filename': 'default_method', 'method_python_name_suffix': '', },
        { 'session_filename': 'numpy_write_method', 'method_python_name_suffix': '_numpy', },
    ], },
    'CreateWaveformI16':            { 'method_templates': [
        { 'session_filename': 'numpy_write_method', 'method_python_name_suffix': '_numpy', },
    ], },
    'WriteWaveformDispatcher':      { 'method_templates': [
        { 'session_filename': 'write_waveform', 'documentation_filename': 'default_method', 'method_python_name_suffix': '', },
    ], },
    'WriteWaveform':                { 'method_templates': [
        { 'session_filename': 'default_method', 'method_python_name_suffix': '', },
        { 'session_filename': 'numpy_write_method', 'method_python_name_suffix': '_numpy', },
    ], },
    'WriteNamedWaveformF64':        { 'method_templates': [
        { 'session_filename': 'default_method', 'method_python_name_suffix': '', },
        { 'session_filename': 'numpy_write_method', 'method_python_name_suffix': '_numpy', },
    ], },
    'WriteBinary16Waveform':        { 'method_templates': [
        { 'session_filename': 'numpy_write_method', 'method_python_name_suffix': '_numpy', },
    ], },
    'WriteNamedWaveformI16':        { 'method_templates': [
        { 'session_filename': 'numpy_write_method', 'method_python_name_suffix': '_numpy', },
    ], },
}

functions_numpy = {
    'CreateWaveformF64':            { 'parameters': { 3: { 'numpy': True, }, }, },
    'CreateWaveformI16':            { 'parameters': { 3: { 'numpy': True, }, }, },
    'WriteWaveform':                { 'parameters': { 4: { 'numpy': True, }, }, },
    'WriteNamedWaveform':           { 'parameters': { 4: { 'numpy': True, }, }, },
    'WriteBinary16Waveform':        { 'parameters': { 4: { 'numpy': True, }, }, },
    'WriteNamedWaveformI16':        { 'parameters': { 4: { 'numpy': True, }, }, },
}

# Parameter that need to be array.array
functions_array = {
    'CreateWaveformF64':            { 'parameters': { 3: { 'use_array': True, }, }, },
    'CreateWaveformI16':            { 'parameters': { 3: { 'use_array': True, }, }, },
    'WriteWaveform':                { 'parameters': { 4: { 'use_array': True, }, }, },
    'WriteNamedWaveform':           { 'parameters': { 4: { 'use_array': True, }, }, },
    'WriteBinary16Waveform':        { 'parameters': { 4: { 'use_array': True, }, }, },
    'WriteNamedWaveformI16':        { 'parameters': { 4: { 'use_array': True, }, }, },
}


