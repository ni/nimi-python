# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.
#FRANKTODO

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
    'OpenSession':                     { 'codegen_method': 'private', 'method_name_for_documentation': '__init__', },#1
    'CloseSession':                    { 'codegen_method': 'private',  },#1
    'GetError':                        { 'codegen_method': 'private',  },#1
    'ClearError':                      { 'codegen_method': 'no',       },#1
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
#    'GetError':                     { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
#    'self_test':                    { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
#    'ReadMultiPoint':               { 'parameters': { 3: { 'size': {'mechanism':'passed-in', 'value':'arraySize'}, }, }, },
}

# These are functions we mark as "error_handling":True. The generator uses this information to
# change how error handling is done within those functions themselves - basically, if an error occurs,
# dont try to handle it, since the functions are only used within the context of error handling.
functions_is_error_handling = {
    'GetError':                     { 'is_error_handling': True, },
}

# Default values for method parameters
functions_default_value = {
#    'InitWithOptions':           { 'parameters': { 1: { 'default_value': False, },
#                                                   2: { 'default_value': False, },
#                                                   3: { 'default_value': '""', }, }, },
#    'ConfigureMultiPoint':       { 'parameters': { 3: { 'default_value': 'SampleTrigger.IMMEDIATE', },
#                                                   4: { 'default_value': 'datetime.timedelta(seconds=-1)', }, }, },
#    'ConfigureThermocouple':     { 'parameters': { 2: { 'default_value': 'ThermocoupleReferenceJunctionType.FIXED', }, }, },
}
