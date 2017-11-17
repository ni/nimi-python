# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
    'init':                                 { 'codegen_method': 'no',       },
    'InitWithOptions':                      { 'codegen_method': 'no',       },
    'InitializeWithChannels':               { 'codegen_method': 'private',  },
    'close':                                { 'codegen_method': 'private',  },
    'CheckAttribute.*':                     { 'codegen_method': 'no',       },  # Not supported in Python API. Issue #529
    'InitiateGeneration':                   { 'codegen_method': 'private',  },
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
    'Abort':                                { 'codegen_method': 'private',  },
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
}

# Attach the given parameter to the given enum from enums.py
functions_enums = {
    'CreateFreqList':                           { 'parameters': { 1: { 'enum': 'Waveform',                  }, }, },
    'CreateWaveformFromFileF64':                { 'parameters': { 3: { 'enum': 'ByteOrder',                 }, }, },  # TODO: issue #538
    'CreateWaveformFromFileI16':                { 'parameters': { 3: { 'enum': 'ByteOrder',                 }, }, },  # TODO: issue #538
    'ConfigureDigitalEdgeScriptTrigger':        { 'parameters': { 3: { 'enum': 'ScriptTriggerDigitalEdgeEdge', }, }, },
    'ConfigureDigitalEdgeStartTrigger':         { 'parameters': { 2: { 'enum': 'StartTriggerDigitalEdgeEdge', }, }, },
    'ConfigureStandardWaveform':                { 'parameters': { 2: { 'enum': 'Waveform' }, }, },
    'ExportSignal':                             { 'parameters': { 1: { 'enum': 'Signal',                    }, }, },  # TODO: issue #538
    'SetNamedWaveformNextWritePosition':        { 'parameters': { 3: { 'enum': 'RelativeTo',                }, }, },  # TODO: issue #538
    'SetWaveformNextWritePosition':             { 'parameters': { 3: { 'enum': 'RelativeTo',                }, }, },  # TODO: issue #538
    'GetHardwareState':                         { 'parameters': { 1: { 'enum': 'HardwareState',             }, }, },  # TODO: issue #538
    'SendSoftwareEdgeTrigger':                  { 'parameters': { 1: { 'enum': 'Trigger',                   }, }, },  # TODO: issue #538
}

functions_issues = {
    'GetFIRFilterCoefficients':             { 'parameters': { 3: {'direction':'out'},  # TODO(marcoskirsch): Remove when #534 solved
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
    'InitializeWithChannels':                       { 'parameters': { 1: { 'default_value': '', },
                                                                      2: { 'default_value': False, },
                                                                      3: { 'default_value': '', }, }, },
    'ConfigureFreqList':                            { 'parameters': { 4: { 'default_value': 0.0, },
                                                                      5: { 'default_value': 0.0, }, }, },
    'ConfigureStandardWaveform':                    { 'parameters': { 4: { 'default_value': 0.0, },
                                                                      6: { 'default_value': 0.0, }, }, },
    'ConfigureDigitalEdgeScriptTrigger':            { 'parameters': { 3: { 'default_value': 'ScriptTriggerDigitalEdgeEdge.RISING', }, }, },
    'ConfigureDigitalEdgeStartTrigger':             { 'parameters': { 2: { 'default_value': 'StartTriggerDigitalEdgeEdge.RISING', }, }, },
    'CreateAdvancedArbSequence':                    { 'parameters': { 4: { 'default_value': None, },
                                                                      5: { 'default_value': None, }, }, },
    'WaitUntilDone':                                { 'parameters': { 1: { 'default_value': 10000, }, }, },
}

