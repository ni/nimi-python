# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
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

# This is the additional metadata needed by the code generator in order create code that can properly handle buffer allocation.
functions_buffer_info = {
    'GetError':                              { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'ReadMultiPoint':                        { 'parameters': { 3: { 'size': {'mechanism':'passed-in', 'value':'arraySize'}, }, }, },
    'GetAttributeViString':                  { 'parameters': { 4: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'GetAStringWithSpecifiedMaximumSize':    { 'parameters': { 1: { 'size': {'mechanism':'passed-in', 'value':'bufferSize'}, }, }, },
    'ReturnANumberAndAString':               { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, },
    'GetAStringOfFixedMaximumSize':          { 'parameters': { 1: { 'size': {'mechanism':'fixed', 'value':256}, }, }, },
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
    'SetCustomTypeArray':                    { 'parameters': { 2: { 'size': {'mechanism':'len', 'value':'numberOfElements'}, }, }, },
    'GetCustomTypeArray':                    { 'parameters': { 2: { 'size': {'mechanism':'passed-in', 'value':'numberOfElements'}, }, }, },
    'GetArrayForPythonCodeDouble':           { 'parameters': { 1: { 'size': {'mechanism':'python-code', 'value':'self.get_array_size_for_python_code()'}, },
                                                               2: { 'size': {'mechanism':'python-code', 'value':'self.get_array_size_for_python_code()'}, }, }, },
    'GetArrayForPythonCodeCustomType':       { 'parameters': { 1: { 'size': {'mechanism':'python-code', 'value':'self.get_array_size_for_python_code()'}, },
                                                               2: { 'size': {'mechanism':'python-code', 'value':'self.get_array_size_for_python_code()'}, }, }, },
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

