# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.
#FRANKTODO

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
    'GetError':                     { 'parameters': { 2: { 'size': {'mechanism':'ivi-dance', 'value':'errorDescriptionSize'     }, }, }, },
    'FindRoute':                    { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'routeSpecSize'            }, }, }, },
    'ExpandRouteSpec':              { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'expandedRouteSpecSize'    }, }, }, },
    'GetAllConnections':            { 'parameters': { 1: { 'size': {'mechanism':'ivi-dance', 'value':'routeSpecSize'            }, }, }, },
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
                                                      4: { 'default_value': 'OperationOrder.BREAK_AFTER_MAKE',       },
                                                      5: { 'default_value': True,                                    }, }, },
    'WaitForDebounce':              { 'parameters': { 1: { 'default_value': -1,                                      }, }, },
    'ExpandRouteSpec':              { 'parameters': { 2: { 'default_value': 'ExpandAction.EXPAND_TO_ROUTES',         }, }, },
}
