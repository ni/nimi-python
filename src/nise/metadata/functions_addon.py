# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
    'OpenSession':                  { 'codegen_method': 'private', 'method_name_for_documentation': '__init__', },
    'CloseSession':                 { 'codegen_method': 'private',                                              },
    'GetError':                     { 'codegen_method': 'private',                                              },
    'ClearError':                   { 'codegen_method': 'no',                                                   },
}

# Attach the given parameter to the given enum from enums.py
functions_enums = {
    'Connect':                      { 'parameters': { 2: { 'enum': 'MulticonnectMode',                  }, }, },
    'ConnectAndDisconnect':         { 'parameters': { 3: { 'enum': 'MulticonnectMode',                  },
                                                      4: { 'enum': 'OperationOrder',                    }, }, },
    'FindRoute':                    { 'parameters': { 5: { 'enum': 'PathCapability',                    }, }, },
    'ExpandRouteSpec':              { 'parameters': { 2: { 'enum': 'ExpandAction',                      }, }, },
}

# This is the additional metadata needed by the code generator in order create code that can properly handle buffer allocation.
functions_buffer_info = {
    'GetError':                     { 'parameters': { 2: { 'size': {'mechanism':'python-code', 'value':'error_description_size[0]'     }, }, # Match NI Switch Executive Examples
                                                      3: { 'size': {'mechanism':'fixed', 'value':1                                     }, }, }, },
    'FindRoute':                    { 'parameters': { 3: { 'size': {'mechanism':'python-code', 'value':'route_spec_size[0]'            }, }, # Match NI Switch Executive Examples
                                                      4: { 'size': {'mechanism':'fixed', 'value':1                                     }, }, }, },
    'ExpandRouteSpec':              { 'parameters': { 3: { 'size': {'mechanism':'python-code', 'value':'expanded_route_spec_size[0]'   }, }, # Match NI Switch Executive Examples
                                                      4: { 'size': {'mechanism':'fixed', 'value':1                                     }, }, }, },
    'GetAllConnections':            { 'parameters': { 1: { 'size': {'mechanism':'python-code', 'value':'route_spec_size[0]'            }, }, # Match NI Switch Executive Examples
                                                      2: { 'size': {'mechanism':'fixed', 'value':1                                     }, }, }, },
}

# These are functions we mark as "error_handling":True. The generator uses this information to
# change how error handling is done within those functions themselves - basically, if an error occurs,
# dont try to handle it, since the functions are only used within the context of error handling.
functions_is_error_handling = {
    'GetError':                     { 'is_error_handling': True, },
}

# Default values for method parameters
functions_default_value = {
    'OpenSession':                  { 'parameters': { 1: { 'default_value': '""',                                    }, }, },
    'Connect':                      { 'parameters': { 2: { 'default_value': 'MulticonnectMode.DEFAULT',              },
                                                      3: { 'default_value': True,                                    }, }, },
    'ConnectAndDisconnect':         { 'parameters': { 3: { 'default_value': 'MulticonnectMode.DEFAULT',              },
                                                      4: { 'default_value': 'OperationOrder.AFTER',                  },
                                                      5: { 'default_value': True,                                    }, }, },
    'WaitForDebounce':              { 'parameters': { 1: { 'default_value': 'datetime.timedelta(milliseconds=-1)',   }, }, },
    'GetError':                     { 'parameters': { 3: { 'default_value': [1024],                                  }, }, },
    'FindRoute':                    { 'parameters': { 4: { 'default_value': [1024],                                  }, }, },
    'ExpandRouteSpec':              { 'parameters': { 2: { 'default_value': 'ExpandAction.ROUTES',                   },
                                                      4: { 'default_value': [1024],                                  }, }, },
    'GetAllConnections':            { 'parameters': { 2: { 'default_value': [1024],                                  }, }, },
}

functions_locking = {
    'ClearError':                   { 'use_session_lock': False,  },  # Issue #896 No locking in this API
    'CloseSession':                 { 'use_session_lock': False,  },  # Issue #896 No locking in this API
    'Connect':                      { 'use_session_lock': False,  },  # Issue #896 No locking in this API
    'ConnectAndDisconnect':         { 'use_session_lock': False,  },  # Issue #896 No locking in this API
    'Disconnect':                   { 'use_session_lock': False,  },  # Issue #896 No locking in this API
    'DisconnectAll':                { 'use_session_lock': False,  },  # Issue #896 No locking in this API
    'ExpandRouteSpec':              { 'use_session_lock': False,  },  # Issue #896 No locking in this API
    'FindRoute':                    { 'use_session_lock': False,  },  # Issue #896 No locking in this API
    'GetAllConnections':            { 'use_session_lock': False,  },  # Issue #896 No locking in this API
    'GetIviDeviceSession':          { 'use_session_lock': False,  },  # Issue #896 No locking in this API
    'IsConnected':                  { 'use_session_lock': False,  },  # Issue #896 No locking in this API
    'IsDebounced':                  { 'use_session_lock': False,  },  # Issue #896 No locking in this API
    'OpenSession':                  { 'use_session_lock': False,  },  # Issue #896 No locking in this API
    'WaitForDebounce':              { 'use_session_lock': False,  },  # Issue #896 No locking in this API
    'GetError':                     { 'use_session_lock': False,  },  # Issue #896 No locking in this API
}

# We want to use a common name for close across all drivers Issue #898
functions_name = {
    'CloseSession': { 'python_name': '_close', },
}

# Converted parameters
functions_converters = {
    'WaitForDebounce':              { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                                                           'type_in_documentation': 'float in seconds or datetime.timedelta',       }, }, },
    'OpenSession':                  { 'parameters': { 1: { 'python_api_converter_name': 'convert_init_with_options_dictionary', 
                                                           'type_in_documentation': 'dict',                                         }, }, },
}

# Switch executive is bad and uses an output as an input. Need to create pointer (array) to use API, but it needs to be input so it can be set by the user.
functions_bad_source_metadata = {
    'GetError':                     { 'parameters': { 3: { 'direction': 'in', 'type': 'ViInt32[]',  }, }, },
    'FindRoute':                    { 'parameters': { 4: { 'direction': 'in', 'type': 'ViInt32[]',  }, }, },
    'ExpandRouteSpec':              { 'parameters': { 4: { 'direction': 'in', 'type': 'ViInt32[]',  }, }, },
    'GetAllConnections':            { 'parameters': { 2: { 'direction': 'in', 'type': 'ViInt32[]',  }, }, },
}
