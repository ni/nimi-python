# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
    'InitWithTopology':                { 'codegen_method': 'private',       },
    'InitWithOptions':                 { 'codegen_method': 'no',       },
    'Initiate':                        { 'codegen_method': 'private',  },
    'close':                           { 'codegen_method': 'private',  },
    'CheckAttribute.+':                { 'codegen_method': 'no',       },  # We do not include any Check Attribute functions
    '.etAttribute.+':                  { 'codegen_method': 'private',  },  # All Set/Get Attribute functions are private
    'init':                            { 'codegen_method': 'no',       },
    'error_message':                   { 'codegen_method': 'private',  },
    'GetError':                        { 'codegen_method': 'private',  },
    'ClearError':                      { 'codegen_method': 'no',       },
    'LockSession':                     { 'codegen_method': 'no',       },
    'UnlockSession':                   { 'codegen_method': 'no',       },
    'SetAttributeViSession':           { 'codegen_method': 'no',       },
    'GetAttributeViSession':           { 'codegen_method': 'no',       },
    'Scan':                            { 'codegen_method': 'no',       },  # Not exposed in LabVIEW API.
    'GetNextInterchangeWarning':       { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ResetInterchangeCheck':           { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ClearInterchangeWarnings':        { 'codegen_method': 'no',       },  # Not applicable to Python API
    'GetNextCoercionRecord':           { 'codegen_method': 'no',       },  # Not applicable to Python API
    'error_query':                     { 'codegen_method': 'no',       },
    'revision_query':                  { 'codegen_method': 'no',       },
    'IsDebounced':                     { 'codegen_method': 'no',       },  # Equivalent attribute is available
    'IsScanning':                      { 'codegen_method': 'no',       },  # Equivalent attribute is available
}

# Override the 'python' name for some functions.
functions_python_name = {
    'AbortScan':                    { 'python_name': 'abort',    },
}

# Attach the given parameter to the given enum from enums.py
functions_enums = {
    'GetRelayPosition':             { 'parameters': { 2: { 'enum': 'RelayPosition',            }, }, },
    'RelayControl':                 { 'parameters': { 2: { 'enum': 'RelayAction',              }, }, },
    'CanConnect':                   { 'parameters': { 3: { 'enum': 'PathCapability',           }, }, },
    'RouteScanAdvancedOutput':      { 'parameters': { 1: { 'enum': 'ScanAdvancedOutput',       },
                                                      2: { 'enum': 'ScanAdvancedOutput',       }, }, },
    'RouteTriggerInput':            { 'parameters': { 1: { 'enum': 'TriggerInput',             },
                                                      2: { 'enum': 'TriggerInput',             }, }, },
    'ConfigureScanList':            { 'parameters': { 2: { 'enum': 'ScanMode',                 }, }, },
    'ConfigureScanTrigger':         { 'parameters': { 2: { 'enum': 'TriggerInput',             },
                                                      3: { 'enum': 'ScanAdvancedOutput',       }, }, },
}

# This is the additional metadata needed by the code generator in order create code that can properly handle buffer allocation.
functions_buffer_info = {
    'GetError':                     { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'BufferSize'}, }, }, },
    'error_message':                { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'self_test':                    { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'GetAttributeViString':         { 'parameters': { 4: { 'size': {'mechanism':'ivi-dance', 'value':'arraySize'}, }, }, },
    'GetChannelName':               { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'GetRelayName':                 { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'relayNameBufferSize'}, }, }, },
    'GetPath':                      { 'parameters': { 4: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'error_message':                { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
}

# These are functions we mark as "error_handling":True. The generator uses this information to
# change how error handling is done within those functions themselves - basically, if an error occurs,
# dont try to handle it, since the functions are only used within the context of error handling.
functions_is_error_handling = {
    'error_message':                { 'is_error_handling': True, },
    'GetError':                     { 'is_error_handling': True, },
}

# Default values for method parameters
functions_default_value = {
    'InitWithTopology':         { 'parameters': { 1: { 'default_value': '"Configured Topology"', },
                                                  2: { 'default_value': False, },
                                                  3: { 'default_value': False, },
                                                  4: { 'default_value': '""', }, }, },
    'ConfigureScanList':        { 'parameters': { 2: { 'default_value': 'enums.ScanMode.BREAK_BEFORE_MAKE', }, }, },
    'ConfigureScanTrigger':     { 'parameters': { 1: { 'default_value': 0.0, }, }, },
    'RouteScanAdvancedOutput':  { 'parameters': { 3: { 'default_value': False, }, }, },
    'RouteTriggerInput':        { 'parameters': { 3: { 'default_value': False, }, }, },
    'WaitForDebounce':          { 'parameters': { 1: { 'default_value': 5000, }, }, },
    'WaitForScanComplete':      { 'parameters': { 1: { 'default_value': 5000, }, }, },
}
