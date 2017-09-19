# These dictionaries are applied to the generated functions dictionary at build time
# Any changes to the API should be made here. functions.py is code generated

# By default all functions in functions.py will be generated as a public function
# This will override that with private - add '_' to the beginning of the name, or
# don't generate at all
functions_codegen_method = {
    'OpenInstalledDevicesSession':          { 'codegen_method': 'private',  },
    'GetExtendedErrorInfo':                 { 'codegen_method': 'private',  },
    'GetInstalledDeviceAttributeViInt32':   { 'codegen_method': 'private',  },
    'GetInstalledDeviceAttributeViString':  { 'codegen_method': 'private',  },
    'CloseInstalledDevicesSession':         { 'codegen_method': 'private',  },
}


# TODO(texasaggie97) can we get rid of this now that we are code generating the ivi-dance method of buffer retrieval? Issue #259
functions_params_types = {
    'GetInstalledDeviceAttributeViString':  { 'parameters': { 4: { 'type': 'ViString',                  }, }, },
    'GetExtendedErrorInfo':                 { 'parameters': { 1: { 'type': 'ViString',                  }, }, },
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
function_default_value = {
    'InitWithOptions':  { 'parameters': { 1: { 'default_value': False, },
                                          2: { 'default_value': False, },
                                          3: { 'default_value': '', }, }, },
}

