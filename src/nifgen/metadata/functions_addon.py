# These dictionaries are applied to the generated functions dictionary at build time
# Any changes to the API should be made here. functions.py is code generated

# By default all functions in functions.py will be generated as a public function
# This will override that with private - add '_' to the beginning of the name, or
# don't generate at all
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
}

# Attach the given parameter to the given enum from enums.py
functions_enums = {
    'CreateFreqList':                           { 'parameters': { 1: { 'enum': 'Waveform',                  }, }, },
    'CreateWaveformFromFileF64':                { 'parameters': { 3: { 'enum': 'ByteOrder',                 }, }, },  # TODO: issue #538
    'CreateWaveformFromFileI16':                { 'parameters': { 3: { 'enum': 'ByteOrder',                 }, }, },  # TODO: issue #538
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

# This is the additional information needed by the code generator to properly generate the buffer retrieval mechanism
# {'is_buffer': True} is required for all parameters that are arrays. Some were able to be detected as an array when
#   generating functions.py. This sets 'is_buffer' for those parameters where the dectection didn't work
# {'size': <size information>} is required for all output buffers.
# <size information> is a dictionary with two keys: 'mechanism' and 'value'.
#   'mechanism' can be:
#       'fixed':        The size is known ahead of time, usually defined by the API.
#                       'value' should be an int.
#       'passed-in':    When the size comes from another parameter.
#                       'value' should be the name of the parameter through which this is specified.
#       'ivi-dance':    When the size is determined by calling into the function using a size of zero and
#                       interpreting the return value as a size rather than an error.
#                       'value' should be the name of the parameter through which the size (0, then the real
#                       one) is passed in. This parameter won't exist in the corresponding Python Session method.
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
    'CreateAdvancedArbSequence':            { 'parameters': { 2: { 'size': {'mechanism':'len', 'value':'sequenceLength'}, }, }, },  # TODO(marcoskirsch): Suffers from #515
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
    'ConfigureFreqList':                            { 'parameters': { 4: { 'default_value': 0,0, },
                                                                      5: { 'default_value': 0.0, }, }, },
    'ConfigureStandardWaveform':                    { 'parameters': { 4: { 'default_value': 0.0, },
                                                                      5: { 'default_value': 0.0, }, }, },
}

