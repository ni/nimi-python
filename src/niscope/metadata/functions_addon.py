# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
    'InitWithOptions':                  { 'codegen_method': 'private',  },
    'InitiateAcquisition':              { 'codegen_method': 'private',  },
    'close':                            { 'codegen_method': 'private',  },
    'Abort':                            { 'codegen_method': 'private',  },
    'CheckAttribute.+':                 { 'codegen_method': 'no',       },  # We do not include any Check Attribute functions
    '.etAttribute.+':                   { 'codegen_method': 'private',  },  # All Set/Get Attribute functions are private
    'init':                             { 'codegen_method': 'no',       },
    'IsDeviceReady':                    { 'codegen_method': 'no',       },  # Used by SFP to address a very slow to come up digitizer.
    'error_message':                    { 'codegen_method': 'private',  },
    'GetError':                         { 'codegen_method': 'private',  },
    'ClearError':                       { 'codegen_method': 'no',       },
    'LockSession':                      { 'codegen_method': 'no',       },
    'UnlockSession':                    { 'codegen_method': 'no',       },
    '.+ExtCal':                         { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'CalAdjust.+':                      { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    '.+UserDefined.+':                  { 'codegen_method': 'no',       },
    'SetAttributeViSession':            { 'codegen_method': 'no',       },
    'GetAttributeViSession':            { 'codegen_method': 'no',       },
    'GetNextInterchangeWarning':        { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ResetInterchangeCheck':            { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ClearInterchangeWarnings':         { 'codegen_method': 'no',       },  # Not applicable to Python API
    'GetNextCoercionRecord':            { 'codegen_method': 'no',       },  # Not applicable to Python API
    'error_query':                      { 'codegen_method': 'no',       },
    'revision_query':                   { 'codegen_method': 'no',       },
    'SampleMode':                       { 'codegen_method': 'no',       },  # Equivalent attribute is available
    'GetNormalizationCoefficients':     { 'codegen_method': 'no',       },  # Has void param
    'GetScalingCoefficients':           { 'codegen_method': 'no',       },  # Has void param
    'ActualRecordLength':               { 'codegen_method': 'no',       },
    'AdjustSampleClockRelativeDelay':   { 'codegen_method': 'no',       },  # This is used internally by NI-TClk, but not by end users.
    'ConfigureAcquisition':             { 'codegen_method': 'no',       },
    'ConfigureAcquisitionRecord':       { 'codegen_method': 'no',       },
    'ConfigureChannel':                 { 'codegen_method': 'no',       },
    'ConfigureClock':                   { 'codegen_method': 'no',       },  # use export_signal
    'ConfigureEdgeTriggerSource':       { 'codegen_method': 'no',       },
    'ConfigureTVTriggerLineNumber':     { 'codegen_method': 'no',       },
    'ConfigureTVTriggerSource':         { 'codegen_method': 'no',       },
    'ConfigureTrigger':                 { 'codegen_method': 'no',       },
    'ConfigureTriggerCoupling':         { 'codegen_method': 'no',       },
    'ConfigureTriggerOutput':           { 'codegen_method': 'no',       },  # use export_signal
    'FetchWaveform':                    { 'codegen_method': 'no',       },
    'FetchWaveformMeasurement':         { 'codegen_method': 'no',       },
    'GetChannelName':                   { 'codegen_method': 'no',       },
    'GetErrorMessage':                  { 'codegen_method': 'no',       },
    'GetStreamEndpointHandle':          { 'codegen_method': 'no',       },
    'IsInvalidWfmElement':              { 'codegen_method': 'no',       },
    'ReadWaveform':                     { 'codegen_method': 'no',       },
    'ReadWaveformMeasurement':          { 'codegen_method': 'no',       },
    'SampleRate':                       { 'codegen_method': 'no',       },
    'SendSWTrigger':                    { 'codegen_method': 'no',       },
    'errorHandler':                     { 'codegen_method': 'no',       },
    'GetFrequencyResponse':             { 'codegen_method': 'no',       },  # TODO(marcoskirsch): add back when #606 is fixed
    'FetchComplex':                     { 'codegen_method': 'no',       },  # TODO(marcoskirsch): No support for complex numbers. Issue #514
    'FetchComplexBinary16':             { 'codegen_method': 'no',       },  # TODO(marcoskirsch):No support for complex numbers. Issue #514
    'FetchBinary8':                     { 'codegen_method': 'no',       },  # TODO(marcoskirsch):No support for fetching binary. Issue #511
    'FetchBinary16':                    { 'codegen_method': 'no',       },  # TODO(marcoskirsch):No support for fetching binary. Issue #511
    'FetchBinary32':                    { 'codegen_method': 'no',       },  # TODO(marcoskirsch):No support for fetching binary. Issue #511
}

# Attach the given parameter to the given enum from enums.py
functions_enums = {
    # @TODO add all enums
}

# This is the additional metadata needed by the code generator in order create code that can properly handle buffer allocation.
functions_buffer_info = {
    'GetError':                                 { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'self_test':                                { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'GetAttributeViString':                     { 'parameters': { 4: { 'size': {'mechanism':'ivi-dance', 'value':'bufSize'}, }, }, },
    'GetCalUserDefinedInfo':                    { 'parameters': { 1: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From LabVIEW VI, even though niDMM_GetCalUserDefinedInfoMaxSize() exists.
    'error_message':                            { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'ConfigureEqualizationFilterCoefficients':  { 'parameters': { 3: { 'size': {'mechanism':'len', 'value':'numberOfCoefficients'}, }, }, },
    'GetEqualizationFilterCoefficients':        { 'parameters': { 3: { 'size': {'mechanism':'python-code', 'value':'self.equalization_num_coefficients'}, }, }, },
    # TODO(marcoskirsch): Won't work until we fix #606
    # 'GetFrequencyResponse':                     { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, },
    #                                                               4: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, },
    #                                                               5: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'FetchMeasurement':                         { 'parameters': { 4: { 'size': {'mechanism':'python-code', 'value':'self.actual_num_waveforms()'}, }, }, },
    'FetchMeasurementStats':                    { 'parameters': { 4: { 'size': {'mechanism':'python-code', 'value':'self.actual_num_waveforms()'}, },
                                                                  5: { 'size': {'mechanism':'python-code', 'value':'self.actual_num_waveforms()'}, },
                                                                  6: { 'size': {'mechanism':'python-code', 'value':'self.actual_num_waveforms()'}, },
                                                                  7: { 'size': {'mechanism':'python-code', 'value':'self.actual_num_waveforms()'}, },
                                                                  8: { 'size': {'mechanism':'python-code', 'value':'self.actual_num_waveforms()'}, },
                                                                  9: { 'size': {'mechanism':'python-code', 'value':'self.actual_num_waveforms()'}, }, }, },
    'ReadMeasurement':                          { 'parameters': { 4: { 'size': {'mechanism':'python-code', 'value':'self.actual_num_waveforms()'}, }, }, },
    'Read':                                     { 'parameters': { 4: { 'size': {'mechanism':'python-code', 'value':'(num_samples * self.actual_num_wfms())'}, },
                                                                  5: { 'size': {'mechanism':'python-code', 'value':'self.actual_num_wfms()'}, }, }, },
    'Fetch':                                    { 'parameters': { 4: { 'size': {'mechanism':'python-code', 'value':'(num_samples * self.actual_num_wfms())'}, },
                                                                  5: { 'size': {'mechanism':'python-code', 'value':'self.actual_num_wfms()'}, }, }, },
    'FetchArrayMeasurement':                    { 'parameters': { 4: { 'size': {'mechanism':'python-code', 'value':'self.actual_meas_wfm_size()'}, },
                                                                  5: { 'size': {'mechanism':'python-code', 'value':'(self.actual_meas_wfm_size() * self.actual_num_wfms())'}, },
                                                                  6: { 'size': {'mechanism':'python-code', 'value':'self.actual_num_wfms()'}, }, }, },
}

# The extracted metadata is incorrect. Patch it here.
functions_bad_source_metadata = {
    'GetFrequencyResponse':                     { 'parameters': { 3: { 'direction': 'out'},
                                                                  4: { 'direction': 'out'},
                                                                  5: { 'direction': 'out'}, }, },


}

# These are functions we mark as "error_handling":True. The generator uses this information to
# change how error handling is done within those functions themselves - basically, if an error occurs,
# dont try to handle it, since the functions are only used within the context of error handling.
functions_is_error_handling = {
    'error_message':                { 'is_error_handling': True },
    'GetError':                     { 'is_error_handling': True },
}

# Default values for method parameters
function_default_value = {
}

