# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
    'InitWithTopology':                { 'codegen_method': 'private', 'method_name_for_documentation': '__init__', },
    'InitWithOptions':                 { 'codegen_method': 'no',       },
    'Initiate':                        { 'codegen_method': 'private', 'method_name_for_documentation': 'initiate', },
    'close':                           { 'codegen_method': 'private',  },
    'CheckAttribute.+':                { 'codegen_method': 'no',       },  # We do not include any Check Attribute functions
    '.etAttribute.+':                  { 'codegen_method': 'private',  },  # All Set/Get Attribute functions are private
    'init':                            { 'codegen_method': 'no',       },
    'error_message':                   { 'codegen_method': 'private',  },
    'GetError':                        { 'codegen_method': 'private',  },
    'ClearError':                      { 'codegen_method': 'no',       },
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
    'self_test':                       { 'codegen_method': 'private', 'method_name_for_documentation': 'self_test', },  # 'fancy_self_test' Public wrapper that raises
    'ConfigureScanList':               { 'codegen_method': 'no',       },  # Equivalent attribute is available - #881
    'ConfigureScanTrigger':            { 'codegen_method': 'no',       },  # Equivalent attribute is available - #881
    'SetContinuousScan':               { 'codegen_method': 'no',       },  # Equivalent attribute is available - #881
}

functions_locking = {
    'LockSession':                     { 'method_templates': [ { 'session_filename': 'lock', 'documentation_filename': 'lock', 'method_python_name_suffix': '', }, ],
                                         'render_in_session_base': True,
                                         'use_session_lock': False,
                                         'python_name': 'lock', },
    'UnlockSession':                   { 'method_templates': [ { 'session_filename': 'unlock', 'documentation_filename': 'unlock', 'method_python_name_suffix': '', }, ],
                                         'render_in_session_base': True,
                                         'use_session_lock': False,
                                         'python_name': 'unlock', },
    'InitWithTopology':                { 'use_session_lock': False,  },  # Session not valid during complete function call so cannot use session locking
    'close':                           { 'use_session_lock': False,  },  # Session not valid during complete function call so cannot use session locking
    'error_message':                   { 'use_session_lock': False,  },  # No Session for function call so cannot use session locking
    'GetError':                        { 'use_session_lock': False,  },  # Session may not be valid during function call so cannot use session locking
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
    'RouteScanAdvancedOutput':  { 'parameters': { 3: { 'default_value': False, }, }, },
    'RouteTriggerInput':        { 'parameters': { 3: { 'default_value': False, }, }, },
    'WaitForDebounce':          { 'parameters': { 1: { 'default_value': 'datetime.timedelta(milliseconds=5000)', }, }, },
    'WaitForScanComplete':      { 'parameters': { 1: { 'default_value': 'datetime.timedelta(milliseconds=5000)', }, }, },
}

functions_converters = {
    'WaitForDebounce':                   { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                                                                'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'WaitForScanComplete':               { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                                                                'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
}


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
                    'description': 'A particular NI-SWITCH session established with niSwitch_InitWithTopology, niSwitch_InitWithOptions, or niSwitch_init and used for all subsequent NI-SWITCH calls.',
                },
            },
        ],
        'documentation': {
            'description': '''
Verifies that the driver can communicate with the switch module.

Raises `SelfTestError` on self test failure. Attributes on exception object:

- code - failure code from driver
- message - status message from driver
''',
            'table_body': [['0', 'Passed self-test'], ['1', 'Self-test failed']],
            'table_header': ['Self-Test Code', 'Description'],
        },
    },
}


