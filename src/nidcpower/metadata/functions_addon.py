# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
    'InitializeWithChannels':                     { 'codegen_method': 'private', 'method_name_for_documentation': '__init__', },
    'InitWithOptions':                            { 'codegen_method': 'no',       },
    'Initiate':                                   { 'codegen_method': 'private', 'method_name_for_documentation': 'initiate', },
    'close':                                      { 'codegen_method': 'private',  },
    '.etAttribute.+':                             { 'codegen_method': 'private',  },  # All Set/Get Attribute functions are private
    'init':                                       { 'codegen_method': 'no',       },
    'error_message':                              { 'codegen_method': 'private',  },
    'GetError':                                   { 'codegen_method': 'private',  },
    'ClearError':                                 { 'codegen_method': 'no',       },
    'ChangeExtCalPassword':                       { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'CloseExtCal':                                { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'InitExtCal':                                 { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'CalAdjust.+':                                { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'ConnectInternalReference':                   { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    '.+UserDefined.+':                            { 'codegen_method': 'no',       },
    'SetAttributeViSession':                      { 'codegen_method': 'no',       },
    'GetAttributeViSession':                      { 'codegen_method': 'no',       },
    'GetNextInterchangeWarning':                  { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ResetInterchangeCheck':                      { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ClearInterchangeWarnings':                   { 'codegen_method': 'no',       },  # Not applicable to Python API
    'GetNextCoercionRecord':                      { 'codegen_method': 'no',       },  # Not applicable to Python API
    'error_query':                                { 'codegen_method': 'no',       },
    'ConfigureAutoZero':                          { 'codegen_method': 'no',       },
    'ConfigureCurrent.+':                         { 'codegen_method': 'no',       },
    'ConfigureOutput.+':                          { 'codegen_method': 'no',       },
    'ConfigurePowerLineFrequency':                { 'codegen_method': 'no',       },
    'ConfigurePulse.+':                           { 'codegen_method': 'no',       },
    'ConfigureSense':                             { 'codegen_method': 'no',       },
    'ConfigureVoltageL.+':                        { 'codegen_method': 'no',       },
    'ConfigureSourceMode':                        { 'codegen_method': 'no',       },
    'ConfigureSoftwareEdge.+Trigger':             { 'codegen_method': 'no',       },
    'Disable.+Trigger':                           { 'codegen_method': 'no',       },
    'revision_query':                             { 'codegen_method': 'no',       },
    'ExportSignal':                               { 'codegen_method': 'no',       },  # remove export signal #828
    'GetExtCalLastDateAndTime':                   { 'codegen_method': 'private', 'method_name_for_documentation': 'get_ext_cal_last_date_and_time',  },  # 'GetLastExtCalLastDateAndTime' Public wrapper to allow datetime
    'GetSelfCalLastDateAndTime':                  { 'codegen_method': 'private', 'method_name_for_documentation': 'get_self_cal_last_date_and_time', },  # 'GetLastSelfCalLastDateAndTime' Public wrapper to allow datetime
    'FetchMultiple':                              { 'codegen_method': 'private', 'method_name_for_documentation': 'fetch_multiple',                  },  # 'FancyFetchMultiple' Public wrapper
    'MeasureMultiple':                            { 'codegen_method': 'private', 'method_name_for_documentation': 'measure_multiple',                },  # 'FancyMeasureMultiple' Public wrapper
    'self_test':                                  { 'codegen_method': 'private', 'method_name_for_documentation': 'self_test',                       },  # 'fancy_self_test' Public wrapper that raises
    'CreateAdvancedSequence':                     { 'codegen_method': 'private',  },  # Advanced sequence private until #504 has a fix
    'CreateAdvancedSequenceStep':                 { 'codegen_method': 'private',  },  # Advanced sequence private until #504 has a fix
    'DeleteAdvancedSequence':                     { 'codegen_method': 'private',  },  # Advanced sequence private until #504 has a fix
    'ConfigureDigitalEdgeMeasureTrigger':         { 'codegen_method': 'no',       },  # Removed - use attributes session.digital_edge_measure_trigger_edge & session.digital_edge_measure_trigger_input_terminal #860
    'ConfigureDigitalEdgePulseTrigger':           { 'codegen_method': 'no',       },  # Removed - use attributes session.digital_edge_pulse_trigger_edge & session.digital_edge_pulse_trigger_input_terminal #860
    'ConfigureDigitalEdgeSequenceAdvanceTrigger': { 'codegen_method': 'no',       },  # Removed - use attributes session.digital_edge_sequence_advance_trigger_edge & session.digital_edge_sequence_advance_trigger_input_terminal #860
    'ConfigureDigitalEdgeSourceTrigger':          { 'codegen_method': 'no',       },  # Removed - use attributes session.digital_edge_source_trigger_edge & session.digital_edge_source_trigger_input_terminal #860
    'ConfigureDigitalEdgeStartTrigger':           { 'codegen_method': 'no',       },  # Removed - use attributes session.digital_edge_start_trigger_edge & session.digital_edge_start_trigger_input_terminal #860
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
    'InitializeWithChannels':          { 'use_session_lock': False,  },  # Session not valid during complete function call so cannot use session locking
    'close':                           { 'use_session_lock': False,  },  # Session not valid during complete function call so cannot use session locking
    'error_message':                   { 'use_session_lock': False,  },  # No Session for function call so cannot use session locking
    'GetError':                        { 'use_session_lock': False,  },  # Session may not be valid during function call so cannot use session locking
}

# Attach the given parameter to the given enum from enums.py
functions_enums = {
    'ConfigureAutoZero':                            { 'parameters': { 2: { 'enum': 'AutoZero',                    }, }, },
    'ConfigureApertureTime':                        { 'parameters': { 3: { 'enum': 'ApertureTimeUnits',           }, }, },
    'SendSoftwareEdgeTrigger':                      { 'parameters': { 1: { 'enum': 'SendSoftwareEdgeTriggerType', }, }, },
    'WaitForEvent':                                 { 'parameters': { 1: { 'enum': 'Event',                       }, }, },
    'Measure':                                      { 'parameters': { 2: { 'enum': 'MeasurementTypes',            }, }, },
    'QueryOutputState':                             { 'parameters': { 2: { 'enum': 'OutputStates',                }, }, },
    'ExportSignal':                                 { 'parameters': { 1: { 'enum': 'ExportSignal',                }, }, },
	# @TODO add all enums
}

# This is the additional metadata needed by the code generator in order create code that can properly handle buffer allocation.
functions_buffer_info = {
    'GetError':                     { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'BufferSize'}, }, }, },
    'self_test':                    { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'GetAttributeViString':         { 'parameters': { 4: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'GetCalUserDefinedInfo':        { 'parameters': { 1: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From LabVIEW VI, even though niDMM_GetCalUserDefinedInfoMaxSize() exists.
    'error_message':                { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'GetChannelName':               { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'SetSequence':                  { 'parameters': { 2: { 'size': {'mechanism':'len', 'value':'Size'}, },
                                                      3: { 'size': {'mechanism':'len', 'value':'Size'}, }, }, },
    'CreateAdvancedSequence':       { 'parameters': { 3: { 'size': {'mechanism':'len', 'value':'attributeIdCount'}, }, }, },
    'FetchMultiple':                { 'parameters': { 4: { 'size': {'mechanism':'passed-in', 'value':'Count'}, },
                                                      5: { 'size': {'mechanism':'passed-in', 'value':'Count'}, },
                                                      6: { 'size': {'mechanism':'passed-in', 'value':'Count'}, }, }, },
    'MeasureMultiple':              { 'parameters': { 2: { 'size': {'mechanism':'python-code', 'value':'self._parse_channel_count()'}, },
                                                      3: { 'size': {'mechanism':'python-code', 'value':'self._parse_channel_count()'}, }, }, }
}

# These are functions we mark as "error_handling":True. The generator uses this information to
# change how error handling is done within those functions themselves - basically, if an error occurs,
# dont try to handle it, since the functions are only used within the context of error handling.
functions_is_error_handling = {
    'error_message':                { 'is_error_handling': True },
    'GetError':                     { 'is_error_handling': True },
}

# There are some parameters that are needed in the C function call we use under the hood, but that we do not want in the Python API
functions_remove_from_python_api = {
    'FetchMultiple':                { 'parameters': { 7: { 'use_in_python_api': False, }, }, },
}

# Default values for method parameters
functions_default_value = {
    'InitializeWithChannels':                        { 'parameters': { 1: { 'default_value': None, },
                                                                       2: { 'default_value': False, },
                                                                       3: { 'default_value': '""', }, }, },
    'ConfigureApertureTime':                         { 'parameters': { 3: { 'default_value': 'ApertureTimeUnits.SECONDS', }, }, },
    'CreateAdvancedSequence':                        { 'parameters': { 4: { 'default_value': True, }, }, },
    'CreateAdvancedSequenceStep':                    { 'parameters': { 1: { 'default_value': True, }, }, },
    'ExportSignal':                                  { 'parameters': { 2: { 'default_value': '""', }, }, },
    'WaitForEvent':                                  { 'parameters': { 2: { 'default_value': 'datetime.timedelta(seconds=10.0)', },}, },
    'FancyFetchMultiple':                            { 'parameters': { 3: { 'default_value': 'datetime.timedelta(seconds=1.0)', }, }, },
}

# Parameter that need to be array.array
functions_array = {
    'FetchMultiple':                        { 'parameters': { 4: { 'use_array': True, },
                                                              5: { 'use_array': True, }, }, },
    'MeasureMultiple':                      { 'parameters': { 2: { 'use_array': True, },
                                                              3: { 'use_array': True, }, }, },
}

# We want to use a common name for self_cal across all drivers
functions_name = {
    'CalSelfCalibrate': { 'python_name': 'self_cal', },
}

# Functions not in original metadata.
functions_additional_functions = {
    # What is this function? I've never seen it in niDCPower.h!
    # It's a secret, undocumented NI-DCPower function and the key to the Python API figuring out how many points to return from nidcpower.Session.measure_multiple.
    # Don't tell anyone about it, and don't ever use it directly in your programs. Thank you.
    'ParseChannelCount': {
        'codegen_method': 'private',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
            },
            {
                'direction': 'in',
                'name': 'channelsString',
                'type': 'ViConstString',
            },
            {
                'direction': 'out',
                'name': 'numberOfChannels',
                'type': 'ViUInt32',
            },
        ],
        'documentation': {
            'description': 'Returns the number of channels.',
        },
    },
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
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitializeWithChannels function.',
                },
            },
        ],
        'documentation': {
            'description': '''
Performs the device self-test routine and returns the test result(s).
Calling this function implicitly calls the niDCPower_reset function.

When calling niDCPower_self_test with the PXIe-4162/4163, specify all
channels of your PXIe-4162/4163 with the channels input of
niDCPower_InitializeWithChannels. You cannot self test a subset of
PXIe-4162/4163 channels.

Raises `SelfTestError` on self test failure. Attributes on exception object:

- code - failure code from driver
- message - status message from driver
''',
            'table_body': [['0', 'Self test passed.'], ['1', 'Self test failed.']],
            'table_header': ['Self-Test Code', 'Description'],
        },
    },
    'FancyFetchMultiple': {
        'returns': 'ViStatus',
        'codegen_method': 'python-only',
        'python_name': 'fetch_multiple',
        'method_templates': [
            { 'session_filename': 'fancy_fetch', 'documentation_filename': 'default_method', 'method_python_name_suffix': '', },
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitializeWithChannels function.',
                },
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
                'documentation': {
                    'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
                },
            },
            {
                'direction': 'in',
                'name': 'Count',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Specifies the number of measurements to fetch.',
                },
            },
            {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'ViReal64',
                'documentation': {
                    'description': 'Specifies the maximum time allowed for this function to complete. If the function does not complete within this time interval, NI-DCPower returns an error.',
                    'note': 'When setting the timeout interval, ensure you take into account any triggers so that the timeout interval is long enough for your application.',
                },
            },
            {
                'direction': 'out',
                'name': 'measurements',
                'type': 'ViReal64[]',
                'python_type': 'Measurement',
                'documentation': {
                    'description': '''
List of named tuples with fields:

- **voltage** (float)
- **current** (float)
- **in_compliance** (bool)
''',
                },
            },
        ],
        'documentation': {
            'description': '''
Returns a list of named tuples (Measurement) that were
previously taken and are stored in the NI-DCPower buffer. This function
should not be used when the NIDCPOWER_ATTR_MEASURE_WHEN attribute is
set to NIDCPOWER_VAL_ON_DEMAND. You must first call
niDCPower_Initiate before calling this function.

Fields in Measurement:

- **voltage** (float)
- **current** (float)
- **in_compliance** (bool)

''',
            'note': 'This function is not supported on all devices. Refer to `Supported Functions by Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm, supportedfunctions)>`__ for more information about supported devices.',
        },
    },
    'FancyMeasureMultiple': {
        'returns': 'ViStatus',
        'codegen_method': 'python-only',
        'python_name': 'measure_multiple',
        'method_templates': [
            { 'session_filename': 'fancy_fetch', 'documentation_filename': 'default_method', 'method_python_name_suffix': '', },
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitializeWithChannels function.',
                },
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViChar[]',
                'documentation': {
                    'description': '''
Specifies the output channel(s) to which this configuration value
applies. Specify multiple channels by using a channel list or a channel
range. A channel list is a comma (,) separated sequence of channel names
(for example, 0,2 specifies channels 0 and 2). A channel range is a
lower bound channel followed by a hyphen (-) or colon (:) followed by an
upper bound channel (for example, 0-2 specifies channels 0, 1, and 2).
In the Running state, multiple output channel configurations are
performed sequentially based on the order specified in this parameter.
''',
                },
            },
            {
                'direction': 'out',
                'name': 'measurements',
                'type': 'ViReal64[]',
                'python_type': 'Measurement',
                'documentation': {
                    'description': '''
List of named tuples with fields:

- **voltage** (float)
- **current** (float)
- **in_compliance** (bool) - Always None
''',
                },
            },
        ],
        'documentation': {
            'description': '''
Returns a list of named tuples (Measurement) containing the measured voltage
and current values on the specified output channel(s). Each call to this function
blocks other function calls until the measurements are returned from the device.
The order of the measurements returned in the array corresponds to the order
on the specified output channel(s).

Fields in Measurement:

- **voltage** (float)
- **current** (float)
- **in_compliance** (bool) - Always None

''',
            'note': 'This function is not supported on all devices. Refer to `Supported Functions by Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm, supportedfunctions)>`__ for more information about supported devices.',
        },
    },
    # Public function that wraps driver function but returns datetime object instead of individual items
    'GetLastExtCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'returns': 'ViStatus',
        'python_name': 'get_ext_cal_last_date_and_time',
        'real_datetime_call': 'GetExtCalLastDateAndTime',
        'method_templates': [
            { 'session_filename': 'datetime_wrappers', 'documentation_filename': 'default_method', 'method_python_name_suffix': '', },
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.',
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
            'description': 'Returns the date and time of the last successful calibration.',
        },
    },
    'GetLastSelfCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'returns': 'ViStatus',
        'python_name': 'get_self_cal_last_date_and_time',
        'real_datetime_call': 'GetSelfCalLastDateAndTime',
        'method_templates': [
            { 'session_filename': 'datetime_wrappers', 'documentation_filename': 'default_method', 'method_python_name_suffix': '', },
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.',
                },
            },
            {
                'direction': 'out',
                'name': 'Month',
                'type': 'datetime.datetime',
                'documentation': {
                    'description': 'Returns the date and time the device was last calibrated.',
                },
            },
        ],
        'documentation':
        {
            'description': 'Returns the date and time of the oldest successful self-calibration from among the channels in the session.',
            'note': 'This function is not supported on all devices.',
        },
    },
}

# Converted parameters
functions_converters = {
    'FetchMultiple':                    { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                               'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'FancyFetchMultiple':               { 'parameters': { 3: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                               'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'WaitForEvent':                     { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                               'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'InitializeWithChannels':           { 'parameters': { 3: { 'python_api_converter_name': 'convert_init_with_options_dictionary',
                                                               'type_in_documentation': 'dict', },
                                                          1: { 'is_repeated_capability': False,
                                                               'python_api_converter_name': 'convert_repeated_capabilities_from_init',
                                                               'type_in_documentation': 'str, list, range, tuple', }, }, },
    'GetExtCalRecommendedInterval':     { 'parameters': { 1: { 'python_api_converter_name': 'convert_month_to_timedelta',
                                                               'type_in_documentation': 'datetime.timedelta', }, }, },
}


