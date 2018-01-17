# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
    'OpenInstalledDevicesSession':          { 'codegen_method': 'private',  },
    'GetExtendedErrorInfo':                 { 'codegen_method': 'private',  },
    'GetInstalledDeviceAttributeViInt32':   { 'codegen_method': 'private',  },
    'GetInstalledDeviceAttributeViString':  { 'codegen_method': 'private',  },
    'CloseInstalledDevicesSession':         { 'codegen_method': 'private',  },
}


# This is the additional metadata needed by the code generator in order create code that can properly handle buffer allocation.
functions_buffer_info = {
    'GetInstalledDeviceAttributeViString':  { 'parameters': { 4: { 'size': {'mechanism':'ivi-dance', 'value':'attributeValueBufferSize'}, }, }, },
    'GetExtendedErrorInfo':                 { 'parameters': { 1: { 'size': {'mechanism':'ivi-dance', 'value':'errorInfoBufferSize'}, }, }, },
}

# These are functions we mark as "error_handling":True. The generator uses this information to
# change how error handling is done within those functions themselves - basically, if an error occurs,
# dont try to handle it, since the functions are only used within the context of error handling.
functions_is_error_handling = {
    'GetExtendedErrorInfo': { 'is_error_handling': True },
}

# Default values for method parameters
functions_default_value = {
    'InitWithOptions':  { 'parameters': { 1: { 'default_value': False, },
                                          2: { 'default_value': False, },
                                          3: { 'default_value': '""', }, }, },
}

