# These dictionaries are applied to the generated functions dictionary at build time
# Any changes to the API should be made here. functions.py is code generated

# By default all functions in functions.py will be generated as a public function
# This will override that with private - add '_' to the beginning of the name, or
# don't generate at all
functions_codegen_method = {
    'InitWithOptions':  { 'codegen_method': 'private',  },
    'Initiate':         { 'codegen_method': 'private',  },
    'close':            { 'codegen_method': 'private',  },
    'Abort':            { 'codegen_method': 'private',  },
    'CheckAttribute.+': { 'codegen_method': 'no',       },  # We do not include any Check Attribute functions
    '.etAttribute.+':   { 'codegen_method': 'private',  },  # All Set/Get Attribute functions are private
    'init':             { 'codegen_method': 'no',       },
    'GetError':         { 'codegen_method': 'private',  },
    'GetErrorMessage':  { 'codegen_method': 'private',  },
    'ClearError':       { 'codegen_method': 'private',  },
    'LockSession':      { 'codegen_method': 'private',  },
    'UnlockSession':    { 'codegen_method': 'private',  },
}

# TODO(texasaggie97) can we get rid of this now that we are code generating the ivi-dance method of buffer retrieval?
functions_params_types = {
    'GetError':                     { 'parameters': { 3: { 'type': 'ViString',                  }, }, },
    'error_message':                { 'parameters': { 2: { 'type': 'ViString',                  }, }, },
    'error_query':                  { 'parameters': { 2: { 'type': 'ViString',                  }, }, },
    'revision_query':               { 'parameters': { 1: { 'type': 'ViString',                  }, }, },
    'GetAttributeViString':         { 'parameters': { 4: { 'type': 'ViString',                  }, }, },
    'GetNextInterchangeWarning':    { 'parameters': { 2: { 'type': 'ViString',                  }, }, },
    'GetNextCoercionRecord':        { 'parameters': { 2: { 'type': 'ViString',                  }, }, },
    'GetChannelName':               { 'parameters': { 3: { 'type': 'ViString',                  }, }, },
    'GetRelayName':                 { 'parameters': { 3: { 'type': 'ViString',                  }, }, },
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
    'GetError':                     { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'buffersize'}, }, }, },
    'error_message':                { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'error_query':                  { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'revision_query':               { 'parameters': { 1: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'self_test':                    { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'GetAttributeViString':         { 'parameters': { 4: { 'size': {'mechanism':'ivi-dance', 'value':'arraySize'}, }, }, },
    'GetNextInterchangeWarning':    { 'parameters': { 2: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'GetNextCoercionRecord':        { 'parameters': { 2: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'GetChannelName':               { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'GetRelayName':                 { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'relayNameBufferSize'}, }, }, },
    'GetPath':                      { 'parameters': { 4: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
}