# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
    'InitWithOptions':          { 'codegen_method': 'private',  },
    'Initiate':                 { 'codegen_method': 'private',  },
    'close':                    { 'codegen_method': 'private',  },
    '.etAttribute.+':           { 'codegen_method': 'private',  },  # All Set/Get Attribute functions are private
    '.etAttributeViSession':    { 'codegen_method': 'no',       },  # Except ViSession ones that aren't applicable to Python
    'error_message':            { 'codegen_method': 'private',  },
    'GetCalDateAndTime':        { 'codegen_method': 'private',  },  # 'GetLastCalDateAndTime' Public wrapper to allow datetime
    'GetError':                 { 'codegen_method': 'private',  },
    'GetErrorMessage':          { 'codegen_method': 'no',       },
    'ClearError':               { 'codegen_method': 'no',       },
    'self_test':                { 'codegen_method': 'private',  },  # 'fancy_self_test' Public wrapper that raises
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
    'InitWithOptions':                 { 'use_session_lock': False,  },  # Session not valid during complete function call so cannot use session locking
    'close':                           { 'use_session_lock': False,  },  # Session not valid during complete function call so cannot use session locking
    'error_message':                   { 'use_session_lock': False,  },  # No Session for function call so cannot use session locking
    'GetError':                        { 'use_session_lock': False,  },  # Session may not be valid during function call so cannot use session locking
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
    'GetAttributeViString':                  { 'parameters': { 4: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'GetAStringWithSpecifiedMaximumSize':    { 'parameters': { 1: { 'size': {'mechanism':'passed-in', 'value':'bufferSize'}, }, }, },
    'ReturnANumberAndAString':               { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, },
    'GetAStringOfFixedMaximumSize':          { 'parameters': { 1: { 'size': {'mechanism':'fixed', 'value':256}, }, }, },
    'error_message':                         { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'GetAnIviDanceString':                   { 'parameters': { 2: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'ReturnMultipleTypes':                   { 'parameters': { 8: { 'size': {'mechanism':'passed-in', 'value':'arraySize'}, },
                                                              10: { 'size': {'mechanism':'ivi-dance', 'value':'stringSize'}, }, }, },
    'MultipleArrayTypes':                    { 'parameters': { 2: { 'size': {'mechanism':'passed-in', 'value':'outputArraySize'}, },
                                                               3: { 'size': {'mechanism':'fixed', 'value':3}, },
                                                               5: { 'size': {'mechanism':'len', 'value':'inputArraySizes'}, },
                                                               6: { 'size': {'mechanism':'len', 'value':'inputArraySizes'}, }, }, },
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
    'FetchWaveform':                         { 'parameters': { 2: { 'size': {'mechanism':'passed-in', 'value':'numberOfSamples'}, }, }, },
    'WriteWaveform':                         { 'parameters': { 2: { 'size': {'mechanism':'len', 'value':'numberOfSamples'}, }, }, },
    'self_test':                             { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'MultipleArraysSameSize':                { 'parameters': { 1: { 'size': {'mechanism':'len', 'value':'Size'}, },
                                                               2: { 'size': {'mechanism':'len', 'value':'Size'}, },
                                                               3: { 'size': {'mechanism':'len', 'value':'Size'}, },
                                                               4: { 'size': {'mechanism':'len', 'value':'Size'}, }, }, },
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
    'InitWithOptions':                  { 'parameters': { 1: { 'default_value': False, },
                                                          2: { 'default_value': False, }, }, },
    'MultipleArrayTypes':               { 'parameters': { 6: { 'default_value': None, }, }, },
    'EnumInputFunctionWithDefaults':    { 'parameters': { 1: { 'default_value': 'Turtle.LEONARDO', }, }, },
}

# Converted parameters
functions_converters = {
    'Read':                             { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_seconds', 
                                                               'type_in_documentation': 'datetime.timedelta', }, }, },
    'ReadFromChannel':                  { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_microseconds', 
                                                               'type_in_documentation': 'datetime.timedelta', }, }, },
    'InitWithOptions':                  { 'parameters': { 3: { 'python_api_converter_name': 'convert_init_with_options_dictionary', 
                                                               'type_in_documentation': 'dict', }, }, },
    'GetCalInterval':                   { 'parameters': { 1: { 'python_api_converter_name': 'convert_month_to_timedelta', 
                                                               'type_in_documentation': 'datetime.timedelta', }, }, },
}

# Manually provided Python names for methods, rather than deriving from original names.
functions_custom_python_name = {
    'PoorlyNamedSimpleFunction':            { 'python_name': 'simple_function' },
}

# There are some parameters that are needed in the C function call we use under the hood, but that we do not want in the Python API
functions_remove_from_python_api = {
    'FetchWaveform':                { 'parameters': { 3: { 'use_in_python_api': False, }, }, },
    'InitWithOptions':              { 'parameters': { 1: { 'use_in_python_api': False, }, }, },  # Don't need ID_Query in the python API since they don't do anything
}

functions_method_templates = {
    'FetchWaveform':                        {
        'method_templates': [
            { 'session_filename': 'default_method', 'documentation_filename': 'default_method', 'method_python_name_suffix': '',  },
            { 'session_filename': 'numpy_read_method', 'documentation_filename': 'numpy_method', 'method_python_name_suffix': '_into', },
        ], 
    },
    'WriteWaveform':                        {
        'method_templates': [
            { 'session_filename': 'default_method', 'documentation_filename': 'default_method', 'method_python_name_suffix': '', },
            { 'session_filename': 'numpy_write_method', 'documentation_filename': 'numpy_method', 'method_python_name_suffix': '_numpy', },
        ],
    },
}

functions_numpy = {
    'FetchWaveform':                        { 'parameters': { 2: { 'numpy': True, }, }, },
    'WriteWaveform':                        { 'parameters': { 2: { 'numpy': True, }, }, },
}

# Parameter that need to be array.array
functions_array = {
    'FetchWaveform':                        { 'parameters': { 2: { 'use_array': True, }, }, },
    'WriteWaveform':                        { 'parameters': { 2: { 'use_array': True, }, }, },
}

# Functions not in original metadata.
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
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niDMM_init or niDMM_InitWithOptions.',
                },
            },
        ],
        'documentation': {
            'description': 'Performs a self-test',
        },
    },
    'GetLastCalDateAndTime': {
        'codegen_method': 'python-only',
        'returns': 'ViStatus',
        'python_name': 'get_cal_date_and_time',
        'real_datetime_call': 'GetCalDateAndTime',
        'method_templates': [
            { 'session_filename': 'datetime_wrappers', 'documentation_filename': 'default_method', 'method_python_name_suffix': '', },
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'name': 'calType',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Specifies the type of calibration performed (external or self-calibration).',
                },
            },
            {
                'direction': 'out',
                'name': 'Month',
                'type': 'datetime.datetime',
                'documentation': {
                    'description': 'Indicates date and time of the last calibration.',
                },
            },
        ],
        'documentation': {
            'description': 'Returns the date and time of the last calibration performed.',
        },
    },
}


