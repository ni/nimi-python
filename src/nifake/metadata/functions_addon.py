# These dictionaries are applied to the generated functions dictionary at build time
# Any changes to the API should be made here. functions.py is code generated

# By default all functions in functions.py will be generated as a public function
# This will override that with private - add '_' to the beginning of the name, or
# don't generate at all

functions_codegen_method = {
    'InitWithOptions':          { 'codegen_method': 'private',  },
    'Initiate':                 { 'codegen_method': 'private',  },
    'close':                    { 'codegen_method': 'private',  },
    'Abort':                    { 'codegen_method': 'private',  },
    '.etAttribute.+':           { 'codegen_method': 'private',  },  # All Set/Get Attribute functions are private
    '.etAttributeViSession':    { 'codegen_method': 'no',       },  # Except ViSession ones that aren't applicable to Python
    'error_message':            { 'codegen_method': 'private',  },
    'GetError':                 { 'codegen_method': 'private',  },
    'GetErrorMessage':          { 'codegen_method': 'no',       },
    'ClearError':               { 'codegen_method': 'no',       },
}

# Attach the given parameter to the given enum from enums.py
functions_enums = {
    'GetEnumValue':                     { 'parameters': { 2: { 'enum': 'Turtle',    }, }, },
    'EnumInputFunctionWithDefaults':    { 'parameters': { 1: { 'enum': 'Turtle',    }, }, },
    'ReturnMultipleTypes':              { 'parameters': { 4: { 'enum': 'Turtle',    },
                                                          6: { 'enum': 'FloatEnum', }, }, },
    'EnumArrayOutputFunction':          { 'parameters': { 2: { 'enum': 'Turtle',    }, }, },
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
    'GetError':                              { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'ReadMultiPoint':                        { 'parameters': { 3: { 'size': {'mechanism':'passed-in', 'value':'arraySize'}, }, }, },
    'GetAttributeViString':                  { 'parameters': { 4: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'GetAStringWithSpecifiedMaximumSize':    { 'parameters': { 1: { 'size': {'mechanism':'passed-in', 'value':'bufferSize'}, }, }, },
    'ReturnANumberAndAString':               { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, },
    'GetAStringOfFixedMaximumSize':          { 'parameters': { 1: { 'size': {'mechanism':'fixed', 'value':256}, }, }, },
    'InitWithOptions':                       { 'parameters': { 0: { 'is_buffer': True, },
                                                               3: { 'is_buffer': True, }, }, },
    '.etAttribute.+':                        { 'parameters': { 1: { 'is_buffer': True, }, }, },
    'error_message':                         { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'ArrayInputFunction':                    { 'parameters': { 2: { 'size': {'mechanism':'len', 'value':'numberOfElements'}, }, }, },
    'GetAnIviDanceString':                   { 'parameters': { 2: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'ReturnMultipleTypes':                   { 'parameters': { 8: { 'size': {'mechanism':'passed-in', 'value':'arraySize'}, },
                                                              10: { 'size': {'mechanism':'ivi-dance', 'value':'stringSize'}, }, }, },
    'MultipleArrayTypes':                    { 'parameters': { 1: { 'size': {'mechanism':'passed-in', 'value':'passedInArraySize'}, },
                                                               2: { 'size': {'mechanism':'fixed', 'value':3}, },
                                                               4: { 'size': {'mechanism':'len', 'value':'lenArraySize'}, }, }, },
    'ParametersAreMultipleTypes':            { 'parameters': { 8: { 'size': {'mechanism':'len', 'value':'stringSize'}, }, }, },
    'BoolArrayOutputFunction':               { 'parameters': { 2: { 'size': {'mechanism':'passed-in', 'value':'numberOfElements'}, }, }, },
    'EnumArrayOutputFunction':               { 'parameters': { 2: { 'size': {'mechanism':'passed-in', 'value':'numberOfElements'}, }, }, },
    'GetArrayUsingIVIDance':                 { 'parameters': { 2: { 'size': {'mechanism':'ivi-dance', 'value':'arraySize'}, }, }, },

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
    'InitWithOptions':                 { 'parameters': { 1: { 'default_value': False, },
                                                         2: { 'default_value': False, },
                                                         3: { 'default_value': '', }, }, },
    'EnumInputFunctionWithDefaults':   { 'parameters': { 1: { 'default_value': 'Turtle.LEONARDO', }, }, },
}

