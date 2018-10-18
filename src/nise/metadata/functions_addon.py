# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_codegen_method = {
    'OpenSession':                  { 'codegen_method': 'private', 'method_name_for_documentation': '__init__', },
    'CloseSession':                 { 'codegen_method': 'private', 'method_name_for_documentation': 'close',    },
    'GetError':                     { 'codegen_method': 'private',                                              },
    'ClearError':                   { 'codegen_method': 'no',                                                   },
    'GetIviDeviceSession':          { 'codegen_method': 'no',                                                   },  # There is no IVI Python API
}

functions_enums = {
    'Connect':                      { 'parameters': { 2: { 'enum': 'MulticonnectMode',                  }, }, },
    'ConnectAndDisconnect':         { 'parameters': { 3: { 'enum': 'MulticonnectMode',                  },
                                                      4: { 'enum': 'OperationOrder',                    }, }, },
    'FindRoute':                    { 'parameters': { 5: { 'enum': 'PathCapability',                    }, }, },
    'ExpandRouteSpec':              { 'parameters': { 2: { 'enum': 'ExpandAction',                      }, }, },
}

# NI Switch Executive uses outputs as inputs for size in string functions. We had to change the size function to be a pointer.
# The easiest way to do this was to use an array of size 1. We use the value in that array to set the size of the string.
# See test_find_route_different_length for how to change the length.
functions_buffer_info = {
    'GetError':                     { 'parameters': { 2: { 'size': {'mechanism':'python-code', 'value':'error_description_size[0]'     }, },
                                                      3: { 'size': {'mechanism':'fixed', 'value':1                                     }, }, }, },
    'FindRoute':                    { 'parameters': { 3: { 'size': {'mechanism':'python-code', 'value':'route_spec_size[0]'            }, },
                                                      4: { 'size': {'mechanism':'fixed', 'value':1                                     }, }, }, },
    'ExpandRouteSpec':              { 'parameters': { 3: { 'size': {'mechanism':'python-code', 'value':'expanded_route_spec_size[0]'   }, },
                                                      4: { 'size': {'mechanism':'fixed', 'value':1                                     }, }, }, },
    'GetAllConnections':            { 'parameters': { 1: { 'size': {'mechanism':'python-code', 'value':'route_spec_size[0]'            }, },
                                                      2: { 'size': {'mechanism':'fixed', 'value':1                                     }, }, }, },
}

functions_is_error_handling = {
    'GetError':                     { 'is_error_handling': True, },
}

functions_default_value = {
    'OpenSession':                  { 'parameters': { 1: { 'default_value': '""',                                    }, }, },
    'Connect':                      { 'parameters': { 2: { 'default_value': 'MulticonnectMode.DEFAULT',              },
                                                      3: { 'default_value': True,                                    }, }, },
    'ConnectAndDisconnect':         { 'parameters': { 3: { 'default_value': 'MulticonnectMode.DEFAULT',              },
                                                      4: { 'default_value': 'OperationOrder.AFTER',                  },
                                                      5: { 'default_value': True,                                    }, }, },
    'WaitForDebounce':              { 'parameters': { 1: { 'default_value': 'datetime.timedelta(milliseconds=-1)',   }, }, },
    'GetError':                     { 'parameters': { 3: { 'default_value': [1024],                                  }, }, }, # Match NI Switch Executive Examples
    'FindRoute':                    { 'parameters': { 4: { 'default_value': [1024],                                  }, }, }, # Match NI Switch Executive Examples
    'ExpandRouteSpec':              { 'parameters': { 2: { 'default_value': 'ExpandAction.ROUTES',                   },
                                                      4: { 'default_value': [1024],                                  }, }, }, # Match NI Switch Executive Examples
    'GetAllConnections':            { 'parameters': { 2: { 'default_value': [1024],                                  }, }, }, # Match NI Switch Executive Examples
}

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
