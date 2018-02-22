# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
    'InitWithOptions':                 { 'codegen_method': 'private',  },
    'Initiate':                        { 'codegen_method': 'private',  },
    'close':                           { 'codegen_method': 'private',  },
    'CheckAttribute.+':                { 'codegen_method': 'no',       },  # We do not include any Check Attribute functions
    '.etAttribute.+':                  { 'codegen_method': 'private',  },  # All Set/Get Attribute functions are private
    'init':                            { 'codegen_method': 'no',       },
    'error_message':                   { 'codegen_method': 'private',  },
    'GetError':                        { 'codegen_method': 'private',  },
    'GetErrorMessage':                 { 'codegen_method': 'no',  },
    'ClearError':                      { 'codegen_method': 'no',       },
    'Control':                         { 'codegen_method': 'no',       },
    'LockSession':                     { 'codegen_method': 'no',       },
    'UnlockSession':                   { 'codegen_method': 'no',       },
    '.+ExtCal':                        { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'GetExtCalRecommendedInterval':    { 'codegen_method': 'public',   },  # This function is useful on regular (not only calibration) sessions.
    'CalAdjust.+':                     { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    '.+UserDefined.+':                 { 'codegen_method': 'no',       },
    'SetCalPassword':                  { 'codegen_method': 'no',       },
    'SetAttributeViSession':           { 'codegen_method': 'no',       },
    'GetAttributeViSession':           { 'codegen_method': 'no',       },
    'GetNextInterchangeWarning':       { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ResetInterchangeCheck':           { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ClearInterchangeWarnings':        { 'codegen_method': 'no',       },  # Not applicable to Python API
    'GetNextCoercionRecord':           { 'codegen_method': 'no',       },  # Not applicable to Python API
    'error_query':                     { 'codegen_method': 'no',       },  # Not applicable to Python API
    'GetChannelName':                  { 'codegen_method': 'no',       },  # IVI Function not used by National Instrument DMMs
    'GetCalCount':                     { 'codegen_method': 'no',       },  # Calibration function not exposed in Python API
    'FormatMeasAbsolute':              { 'codegen_method': 'no',       },  # Utility function for C customers
    'IsUnderRange':                    { 'codegen_method': 'no',       },  # Utility function for C customers
    'IsOverRange':                     { 'codegen_method': 'no',       },  # Utility function for C customers
    'ConfigureThermistorType':         { 'codegen_method': 'no',       },
    'ConfigureTransducerType':         { 'codegen_method': 'no',       },
    'ConfigureTriggerSlope':           { 'codegen_method': 'no',       },
    'ConfigureSampleTriggerSlope':     { 'codegen_method': 'no',       },
    'ConfigureMeasCompleteDest':       { 'codegen_method': 'no',       },
    'ConfigureMeasCompleteSlope':      { 'codegen_method': 'no',       },
    'ConfigureAutoZeroMode':           { 'codegen_method': 'no',       },
    'ConfigureCableCompType':          { 'codegen_method': 'no',       },
    'ConfigureCurrentSource':          { 'codegen_method': 'no',       },
    'ConfigureFixedRefJunction':       { 'codegen_method': 'no',       },
    'ConfigureFrequencyVoltageRange':  { 'codegen_method': 'no',       },
    'ConfigureOffsetCompOhms':         { 'codegen_method': 'no',       },
    'ConfigureWaveformCoupling':       { 'codegen_method': 'no',       },
    'ConfigureADCCalibration':         { 'codegen_method': 'no',       },
    'revision_query':                  { 'codegen_method': 'no',       },
    'GetCalDateAndTime':               { 'codegen_method': 'private',  },  # Public wrapper to allow datetime
}

# Attach the given parameter to the given enum from enums.py
functions_enums = {
    'ConfigureTrigger':             { 'parameters': { 1: { 'enum': 'TriggerSource',                     }, }, },
    'ConfigureMultiPoint':          { 'parameters': { 3: { 'enum': 'SampleTrigger',                     }, }, },
    'GetApertureTimeInfo':          { 'parameters': { 2: { 'enum': 'ApertureTimeUnits',                 }, }, },
    'ConfigureMeasurementDigits':   { 'parameters': { 1: { 'enum': 'Function',                          }, }, },
    'ConfigureMeasurementAbsolute': { 'parameters': { 1: { 'enum': 'Function',                          }, }, },
    'ReadStatus':                   { 'parameters': { 2: { 'enum': 'AcquisitionStatus',                 }, }, },
    'ConfigureWaveformAcquisition': { 'parameters': { 1: { 'enum': 'Function',                          }, }, },
    'ConfigureThermocouple':        { 'parameters': { 1: { 'enum': 'ThermocoupleType',                  },
                                                      2: { 'enum': 'ThermocoupleReferenceJunctionType', },    }, },
    'ConfigureRTDType':             { 'parameters': { 1: { 'enum': 'RTDType',                           }, }, },

}

# This is the additional metadata needed by the code generator in order create code that can properly handle buffer allocation.
functions_buffer_info = {
    'GetError':                     { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'self_test':                    { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'ReadMultiPoint':               { 'parameters': { 3: { 'size': {'mechanism':'passed-in', 'value':'arraySize'}, }, }, },
    'FetchMultiPoint':              { 'parameters': { 3: { 'size': {'mechanism':'passed-in', 'value':'arraySize'}, }, }, },
    'FetchWaveform':                { 'parameters': { 3: { 'size': {'mechanism':'passed-in', 'value':'arraySize'}, }, }, },
    'ReadWaveform':                 { 'parameters': { 3: { 'size': {'mechanism':'passed-in', 'value':'arraySize'}, }, }, },
    'GetAttributeViString':         { 'parameters': { 4: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'GetCalUserDefinedInfo':        { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From LabVIEW VI, even though niDMM_GetCalUserDefinedInfoMaxSize() exists.
    'error_message':                { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
}

# These are functions we mark as "error_handling":True. The generator uses this information to
# change how error handling is done within those functions themselves - basically, if an error occurs,
# dont try to handle it, since the functions are only used within the context of error handling.
functions_is_error_handling = {
    'error_message':                { 'is_error_handling': True, },
    'GetError':                     { 'is_error_handling': True, },
}

# There are some parameters that are needed in the C function call we use under the hood, but that we do not want in the Python API
functions_remove_from_python_api = {
    'FetchWaveform':                { 'parameters': { 4: { 'use_in_python_api': False, }, }, },
    'FetchMultiPoint':              { 'parameters': { 4: { 'use_in_python_api': False, }, }, },
    'ReadMultiPoint':               { 'parameters': { 4: { 'use_in_python_api': False, }, }, },
    'ReadWaveform':                 { 'parameters': { 4: { 'use_in_python_api': False, }, }, },
}

# Default values for method parameters
functions_default_value = {
    'InitWithOptions':           { 'parameters': { 1: { 'default_value': False, },
                                                   2: { 'default_value': False, },
                                                   3: { 'default_value': '""', }, }, },
    'ConfigureMultiPoint':       { 'parameters': { 3: { 'default_value': 'SampleTrigger.IMMEDIATE', },
                                                   4: { 'default_value': 'datetime.timedelta(seconds=-1)', }, }, },
    'ConfigureThermocouple':     { 'parameters': { 2: { 'default_value': 'ThermocoupleReferenceJunctionType.FIXED', }, }, },
    'ConfigureTrigger':          { 'parameters': { 2: { 'default_value': 'datetime.timedelta(seconds=-1)', }, }, },
    'Fetch':                     { 'parameters': { 1: { 'default_value': 'datetime.timedelta(milliseconds=-1)', }, }, },
    'FetchMultiPoint':           { 'parameters': { 1: { 'default_value': 'datetime.timedelta(milliseconds=-1)', }, }, },
    'FetchWaveform':             { 'parameters': { 1: { 'default_value': 'datetime.timedelta(milliseconds=-1)', }, }, },
    'GetDevTemp':                { 'parameters': { 1: { 'default_value': '""', }, }, },
    'Read':                      { 'parameters': { 1: { 'default_value': 'datetime.timedelta(milliseconds=-1)', }, }, },
    'ReadMultiPoint':            { 'parameters': { 1: { 'default_value': 'datetime.timedelta(milliseconds=-1)', }, }, },
    'ReadWaveform':              { 'parameters': { 1: { 'default_value': 'datetime.timedelta(milliseconds=-1)', }, }, },
}

functions_method_template_filenames = {
    'FetchWaveform':                        {
        'method_templates': [
            { 'session_filename': 'default_method', 'documentation_filename': 'default_method', 'method_python_name_suffix': '',  },
            { 'session_filename': 'numpy_read_method', 'documentation_filename': 'numpy_method', 'method_python_name_suffix': '_into', },
        ],
    },
}

functions_numpy = {
    'FetchWaveform':                        { 'parameters': { 3: { 'numpy': True, }, }, },
}

# Don't need ID_Query in the python API since they don't do anything
functions_remove_parameters_from_python = {
    'InitWithOptions':                      { 'parameters': { 1: { 'use_in_python_api': False, }, }, },
}

# Converted parameters
functions_converters = {
    'ConfigureMultiPoint':      { 'parameters': { 4: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                       'python_api_converter_type': 'datetime.timedelta', }, }, },
    'ConfigureTrigger':         { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                       'python_api_converter_type': 'datetime.timedelta', }, }, },
    'Fetch':                    { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                                                       'python_api_converter_type': 'datetime.timedelta', }, }, },
    'FetchMultiPoint':          { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                                                       'python_api_converter_type': 'datetime.timedelta', }, }, },
    'FetchWaveform':            { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                                                       'python_api_converter_type': 'datetime.timedelta', }, }, },
    'Read':                     { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                                                       'python_api_converter_type': 'datetime.timedelta', }, }, },
    'ReadMultiPoint':           { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                                                       'python_api_converter_type': 'datetime.timedelta', }, }, },
    'ReadWaveform':             { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                                                       'python_api_converter_type': 'datetime.timedelta', }, }, },
    'InitWithOptions':          { 'parameters': { 3: { 'python_api_converter_name': 'convert_init_with_options_dictionary', 
                                                       'python_api_converter_type': 'dict', }, }, },
}

# Functions not in original metadata.
functions_additional_functions = {
    # Public function that wraps driver function but returns datetime object instead of individual items
    'GetLastCalDateAndTime': {
        'codegen_method': 'public',
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
                'documentation': 
                {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niDMM_init or niDMM_InitWithOptions. The default is None.',
                },
            },
            {
                'direction': 'in',
                'name': 'calType',
                'type': 'ViInt32',
                'documentation': 
                {
                    'description': 'Specifies the type of calibration performed (external or self-calibration).',
                    'note': 'The NI 4065 does not support self-calibration.',
                    'table_body': [['NIDMM_VAL_INTERNAL_AREA (default)', '0', 'Self-Calibration'], ['NIDMM_VAL_EXTERNAL_AREA', '1', 'External Calibration']],
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
            'note': 'The NI 4050 and NI 4060 are not supported.',
        },
    },
}

# Parameter that need to be array.array
functions_array = {
    'ReadMultiPoint':                      { 'parameters': { 3: { 'use_array': True, }, }, },
    'ReadWaveform':                        { 'parameters': { 3: { 'use_array': True, }, }, },
    'FetchMultiPoint':                     { 'parameters': { 3: { 'use_array': True, }, }, },
    'FetchWaveform':                       { 'parameters': { 3: { 'use_array': True, }, }, },
}


