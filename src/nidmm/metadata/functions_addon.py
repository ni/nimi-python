# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
    'InitWithOptions':                 { 'codegen_method': 'private', 'method_name_for_documentation': '__init__', },
    'Initiate':                        { 'codegen_method': 'private',  },
    'close':                           { 'codegen_method': 'private',  },
    'CheckAttribute.+':                { 'codegen_method': 'no',       },  # We do not include any Check Attribute functions
    '.etAttribute.+':                  { 'codegen_method': 'private',  },  # All Set/Get Attribute functions are private
    'init':                            { 'codegen_method': 'no',       },
    'error_message':                   { 'codegen_method': 'private',  },
    'GetError':                        { 'codegen_method': 'private',  },
    'GetErrorMessage':                 { 'codegen_method': 'no',       },
    'ClearError':                      { 'codegen_method': 'no',       },
    'Control':                         { 'codegen_method': 'no',       },
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
    'GetCalDateAndTime':               { 'codegen_method': 'private', 'method_name_for_documentation': 'get_cal_date_and_time', },  # 'GetLastCalDateAndTime' Public wrapper to allow datetime
    'self_test':                       { 'codegen_method': 'private', 'method_name_for_documentation': 'self_test',             },  # 'fancy_self_test' Public wrapper that raises
    'ConfigureACBandwidth':            { 'codegen_method': 'no',       },  # Use corresponding attribute instead #875
    'ConfigureOpenCableCompValues':    { 'codegen_method': 'no',       },  # Use corresponding attribute instead #875
    'ConfigurePowerLineFrequency':     { 'codegen_method': 'no',       },  # Use corresponding attribute instead #875
    'ConfigureShortCableCompValues':   { 'codegen_method': 'no',       },  # Use corresponding attribute instead #875
    'GetApertureTimeInfo':             { 'codegen_method': 'no',       },  # Use corresponding attribute instead #875
    'GetAutoRangeValue':               { 'codegen_method': 'no',       },  # Use corresponding attribute instead #875
    'GetMeasurementPeriod':            { 'codegen_method': 'no',       },  # EOL hardware only #875
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
    'ConfigureMultiPoint':          { 'parameters': { 4: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                           'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'ConfigureTrigger':             { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                           'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'Fetch':                        { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                                                           'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'FetchMultiPoint':              { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                                                           'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'FetchWaveform':                { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                                                           'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'Read':                         { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                                                           'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'ReadMultiPoint':               { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                                                           'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'ReadWaveform':                 { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                                                           'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'InitWithOptions':              { 'parameters': { 3: { 'python_api_converter_name': 'convert_init_with_options_dictionary', 
                                                           'type_in_documentation': 'dict', }, }, },
    'GetExtCalRecommendedInterval': { 'parameters': { 1: { 'python_api_converter_name': 'convert_month_to_timedelta', 
                                                           'type_in_documentation': 'datetime.timedelta', }, }, },
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
            'description': '''
Performs a self-test on the DMM to ensure that the DMM is functioning
properly. Self-test does not calibrate the DMM. Zero
indicates success. 

On the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that
you should check the fuse and replace it, if necessary.

Raises `SelfTestError` on self test failure. Attributes on exception object:

- code - failure code from driver
- message - status message from driver
''',
            'note': [
                'Self-test does not check the fuse on the NI 4065, NI 4071, and NI 4081. Hence, even if the fuse is blown on the device, self-test does not return error code 1013.',
                'This function calls niDMM_reset, and any configurations previous to the call will be lost. All attributes will be set to their default values after the call returns.',
            ],
        },
    },
    # Public function that wraps driver function but returns datetime object instead of individual items
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


