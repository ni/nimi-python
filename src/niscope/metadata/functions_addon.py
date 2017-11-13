# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
    'InitWithOptions':                 { 'codegen_method': 'private',  },
    'InitiateAcquisition':             { 'codegen_method': 'private',  },
    'close':                           { 'codegen_method': 'private',  },
    'Abort':                           { 'codegen_method': 'private',  },
    '.etAttribute.+':                  { 'codegen_method': 'private',  },  # All Set/Get Attribute functions are private
    'init':                            { 'codegen_method': 'no',       },
    'error_message':                   { 'codegen_method': 'private',  },
    'GetError':                        { 'codegen_method': 'private',  },
    'ClearError':                      { 'codegen_method': 'no',       },
    'LockSession':                     { 'codegen_method': 'no',       },
    'UnlockSession':                   { 'codegen_method': 'no',       },
    '.+ExtCal':                        { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'CalAdjust.+':                     { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    '.+UserDefined.+':                 { 'codegen_method': 'no',       },
    'SetAttributeViSession':           { 'codegen_method': 'no',       },
    'GetAttributeViSession':           { 'codegen_method': 'no',       },
    'GetNextInterchangeWarning':       { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ResetInterchangeCheck':           { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ClearInterchangeWarnings':        { 'codegen_method': 'no',       },  # Not applicable to Python API
    'GetNextCoercionRecord':           { 'codegen_method': 'no',       },  # Not applicable to Python API
    'error_query':                     { 'codegen_method': 'no',       },
    'revision_query':                  { 'codegen_method': 'no',       },
    'SampleMode':                      { 'codegen_method': 'no',       },  # Equivalent attribute is available
    'GetNormalizationCoefficients':    { 'codegen_method': 'no',       },  # Has void param
    'GetScalingCoefficients':          { 'codegen_method': 'no',       },  # Has void param
    'Fetch':                           { 'codegen_method': 'no',       },  # Has niScope_wfmInfo param #543
    'FetchArrayMeasurement':           { 'codegen_method': 'no',       },  # Has niScope_wfmInfo param #543
    'FetchBinary16':                   { 'codegen_method': 'no',       },  # Has niScope_wfmInfo param #543
    'FetchBinary32':                   { 'codegen_method': 'no',       },  # Has niScope_wfmInfo param #543
    'FetchBinary8':                    { 'codegen_method': 'no',       },  # Has niScope_wfmInfo param #543
    'FetchComplex':                    { 'codegen_method': 'no',       },  # Has niScope_wfmInfo param #543
    'FetchComplexBinary16':            { 'codegen_method': 'no',       },  # Has niScope_wfmInfo param #543
    'Read':                            { 'codegen_method': 'no',       },  # Has niScope_wfmInfo param #543
}

# Attach the given parameter to the given enum from enums.py
functions_enums = {
    # @TODO add all enums
}

# This is the additional metadata needed by the code generator in order create code that can properly handle buffer allocation.
functions_buffer_info = {
    'GetError':                     { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'self_test':                    { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'GetAttributeViString':         { 'parameters': { 4: { 'size': {'mechanism':'ivi-dance', 'value':'bufSize'}, }, }, },
    'GetCalUserDefinedInfo':        { 'parameters': { 1: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From LabVIEW VI, even though niDMM_GetCalUserDefinedInfoMaxSize() exists.
    'error_message':                { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
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

