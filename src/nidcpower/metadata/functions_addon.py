# These dictionaries are applied to the generated functions dictionary at build time
# Any changes to the API should be made here. functions.py is code generated

# By default all functions in functions.py will be generated as a public function
# This will override that with private - add '_' to the beginning of the name, or
# don't generate at all
functions_codegen_method = {
    'InitializeWithChannels':          { 'codegen_method': 'private',  },
    'InitWithOptions':                 { 'codegen_method': 'no',       },
    'Initiate':                        { 'codegen_method': 'private',  },
    'close':                           { 'codegen_method': 'private',  },
    'Abort':                           { 'codegen_method': 'private',  },
    '.etAttribute.+':                  { 'codegen_method': 'private',  },  # All Set/Get Attribute functions are private
    'init':                            { 'codegen_method': 'no',       },
    'error_message':                   { 'codegen_method': 'no',       },
    'GetError':                        { 'codegen_method': 'private',  },
    'ClearError':                      { 'codegen_method': 'no',       },
    'LockSession':                     { 'codegen_method': 'no',       },
    'UnlockSession':                   { 'codegen_method': 'no',       },
    '.+ExtCal':                        { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'CalAdjust.+':                     { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'CalSelfCalibrate':                { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'ConnectInternalReference':        { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    '.+UserDefined.+':                 { 'codegen_method': 'no',       },
    'SetAttributeViSession':           { 'codegen_method': 'no',       },
    'GetAttributeViSession':           { 'codegen_method': 'no',       },
    'GetNextInterchangeWarning':       { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ResetInterchangeCheck':           { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ClearInterchangeWarnings':        { 'codegen_method': 'no',       },  # Not applicable to Python API
    'GetNextCoercionRecord':           { 'codegen_method': 'no',       },  # Not applicable to Python API
    'GetChannelName':                  { 'codegen_method': 'no',       },
    'error_query':                     { 'codegen_method': 'no',       },
    'ConfigureAutoZero':               { 'codegen_method': 'no',       },
    'ConfigureCurrent.+':              { 'codegen_method': 'no',       },
    'ConfigureOutput.+':               { 'codegen_method': 'no',       },
    'ConfigurePowerLineFrequency':     { 'codegen_method': 'no',       },
    'ConfigurePulse.+':                { 'codegen_method': 'no',       },
    'ConfigureSense':                  { 'codegen_method': 'no',       },
    'ConfigureVoltageL.+':             { 'codegen_method': 'no',       },
    'ConfigureSourceMode':             { 'codegen_method': 'no',       },
    'ConfigureSoftwareEdge.+Trigger':  { 'codegen_method': 'no',       },
    'Disable.+Trigger':                { 'codegen_method': 'no',       },
}

# Attach the given parameter to the given enum from enums.py
functions_enums = {
    'ConfigureAutoZero':   { 'parameters': { 2: { 'enum': 'AutoZero',                  }, }, },
    # @TODO add all enums
}

# TODO(texasaggie97) can we get rid of this now that we are code generating the ivi-dance method of buffer retrieval? Issue #259
functions_params_types = {
    'GetAttributeViString':         { 'parameters': { 4: { 'type': 'ViString',                  }, }, },
    'SetAttributeViString':         { 'parameters': { 3: { 'type': 'ViString',                  }, }, },
    'GetError':                     { 'parameters': { 3: { 'type': 'ViString',                  }, }, },
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
    'GetError':                     { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'BufferSize'}, }, }, },
    'self_test':                    { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'GetAttributeViString':         { 'parameters': { 4: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'GetCalUserDefinedInfo':        { 'parameters': { 1: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From LabVIEW VI, even though niDMM_GetCalUserDefinedInfoMaxSize() exists.
    'init':                         { 'parameters': { 0: { 'is_buffer': True, }, }, },
    'InitWithOptions':              { 'parameters': { 0: { 'is_buffer': True, },
                                                      3: { 'is_buffer': True, }, }, },
    '.etAttribute.+':               { 'parameters': { 1: { 'is_buffer': True, }, }, },
    'GetDevTemp':                   { 'parameters': { 1: { 'is_buffer': True, }, }, },
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
    'InitWithOptions':  { 'parameters': { 1: { 'default_value': False, },
                                          2: { 'default_value': False, },
                                          3: { 'default_value': '', }, }, },
}

