# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
    'InitWithOptions':                  { 'codegen_method': 'private', 'method_name_for_documentation': '__init__', },
    'InitiateAcquisition':              { 'codegen_method': 'private',  },
    'close':                            { 'codegen_method': 'private',  },
    'CheckAttribute.+':                 { 'codegen_method': 'no',       },  # We do not include any Check Attribute functions
    '.etAttribute.+':                   { 'codegen_method': 'private',  },  # All Set/Get Attribute functions are private
    'init':                             { 'codegen_method': 'no',       },
    'IsDeviceReady':                    { 'codegen_method': 'no',       },  # Used by SFP to address a very slow to come up digitizer.
    'error_message':                    { 'codegen_method': 'private',  },
    'GetError':                         { 'codegen_method': 'private',  },
    'ClearError':                       { 'codegen_method': 'no',       },
    # '.+ExtCal':                         { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    # 'CalAdjust.+':                      { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    # '.+UserDefined.+':                  { 'codegen_method': 'no',       },
    'SetAttributeViSession':            { 'codegen_method': 'no',       },
    'GetAttributeViSession':            { 'codegen_method': 'no',       },
    'GetNextInterchangeWarning':        { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ResetInterchangeCheck':            { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ClearInterchangeWarnings':         { 'codegen_method': 'no',       },  # Not applicable to Python API
    'GetNextCoercionRecord':            { 'codegen_method': 'no',       },  # Not applicable to Python API
    'error_query':                      { 'codegen_method': 'no',       },
    'revision_query':                   { 'codegen_method': 'no',       },
    'SampleMode':                       { 'codegen_method': 'no',       },  # Equivalent attribute is available
    'GetNormalizationCoefficients':     { 'codegen_method': 'no',       },  # Has void param
    'GetScalingCoefficients':           { 'codegen_method': 'no',       },  # Has void param
    'ActualRecordLength':               { 'codegen_method': 'no',       },
    'AdjustSampleClockRelativeDelay':   { 'codegen_method': 'no',       },  # This is used internally by NI-TClk, but not by end users.
    'ConfigureAcquisition':             { 'codegen_method': 'no',       },
    'ConfigureAcquisitionRecord':       { 'codegen_method': 'no',       },
    'ConfigureChannel':                 { 'codegen_method': 'no',       },
    'ConfigureClock':                   { 'codegen_method': 'no',       },  # use export_signal
    'ConfigureEdgeTriggerSource':       { 'codegen_method': 'no',       },
    'ConfigureTVTriggerLineNumber':     { 'codegen_method': 'no',       },
    'ConfigureTVTriggerSource':         { 'codegen_method': 'no',       },
    'ConfigureTrigger':                 { 'codegen_method': 'no',       },
    'ConfigureTriggerCoupling':         { 'codegen_method': 'no',       },
    'ConfigureTriggerOutput':           { 'codegen_method': 'no',       },  # use export_signal
    'FetchWaveform':                    { 'codegen_method': 'no',       },
    'FetchWaveformMeasurement':         { 'codegen_method': 'no',       },
    'GetChannelName':                   { 'codegen_method': 'no',       },
    'GetErrorMessage':                  { 'codegen_method': 'no',       },
    'GetStreamEndpointHandle':          { 'codegen_method': 'no',       },
    'IsInvalidWfmElement':              { 'codegen_method': 'no',       },
    'ReadWaveform':                     { 'codegen_method': 'no',       },
    'ReadWaveformMeasurement':          { 'codegen_method': 'no',       },
    'SampleRate':                       { 'codegen_method': 'no',       },
    'SendSWTrigger':                    { 'codegen_method': 'no',       },
    'errorHandler':                     { 'codegen_method': 'no',       },
    'FetchComplex':                     { 'codegen_method': 'no',       },  # No support for complex numbers. Issue #514
    'FetchComplexBinary16':             { 'codegen_method': 'no',       },  # No support for complex numbers. Issue #514
    'GetFrequencyResponse':             { 'codegen_method': 'no',       },  # Per #823, not supporting on board processing (complex numbers #514)
    'FetchBinary8':                     { 'codegen_method': 'private', 'method_name_for_documentation': 'fetch_into', },  # 'FetchDispatcher' Public wrapper for numpy + ease of use
    'FetchBinary16':                    { 'codegen_method': 'private', 'method_name_for_documentation': 'fetch_into', },  # 'FetchDispatcher' Public wrapper for numpy + ease of use
    'FetchBinary32':                    { 'codegen_method': 'private', 'method_name_for_documentation': 'fetch_into', },  # 'FetchDispatcher' Public wrapper for numpy + ease of use
    'Fetch':                            { 'codegen_method': 'private', 'method_name_for_documentation': 'fetch',      },  # 'FancyFetch' Public wrapper
    'Read':                             { 'codegen_method': 'private', 'method_name_for_documentation': 'read',       },  # 'FancyRead' Public wrapper
    'ActualNumWfms':                    { 'codegen_method': 'private',  },  # We use it internally so the customer doesn't have to.
    'ClearWaveformProcessing':          { 'codegen_method': 'private',  },  # Per #809, making measurement library methods private
    'AddWaveformProcessing':            { 'codegen_method': 'private',  },  # Per #809, making measurement library methods private
    'FetchArrayMeasurement':            { 'codegen_method': 'private',  },  # Per #809, making measurement library methods private
    'ActualMeasWfmSize':                { 'codegen_method': 'private',  },  # Per #809, making measurement library methods private
    'ClearWaveformMeasurementStats':    { 'codegen_method': 'private',  },  # Per #809, making measurement library methods private
    'FetchMeasurement':                 { 'codegen_method': 'private',  },  # Per #809, making measurement library methods private
    'FetchMeasurementStats':            { 'codegen_method': 'private',  },  # Per #809, making measurement library methods private
    'ReadMeasurement':                  { 'codegen_method': 'private',  },  # Per #809, making measurement library methods private
    'ConfigureRefLevels':               { 'codegen_method': 'private',  },  # Per #809, making measurement library methods private
    'self_test':                        { 'codegen_method': 'private', 'method_name_for_documentation': 'self_test', },  # 'fancy_self_test' Public wrapper that raises
    'GetEqualizationFilterCoefficients': { 'codegen_method': 'private',  },  # 'FancyGetEqualizationFilterCoefficients' Public wrapper
    'ExportSignal':                     { 'codegen_method': 'no',       },  # remove export signal #828
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
    'CalSelfCalibrate':                                { 'parameters': { 2: { 'enum': 'Option',                          }, }, },
    'ClearWaveformMeasurementStats':                   { 'parameters': { 2: { 'enum': 'ClearableMeasurement',            }, }, },
    'ConfigureVertical':                               { 'parameters': { 4: { 'enum': 'VerticalCoupling',                }, }, },
    'ConfigureTriggerDigital':                         { 'parameters': { 2: { 'enum': 'TriggerSlope',                    }, }, },
    'ConfigureTriggerEdge':                            { 'parameters': { 4: { 'enum': 'TriggerCoupling',                 },
                                                                         3: { 'enum': 'TriggerSlope',                    }, }, },
    'ConfigureTriggerHysteresis':                      { 'parameters': { 4: { 'enum': 'TriggerSlope',                    },
                                                                         5: { 'enum': 'TriggerCoupling',                 }, }, },
    'ConfigureTriggerVideo':                           { 'parameters': { 3: { 'enum': 'VideoSignalFormat',               },
                                                                         4: { 'enum': 'VideoTriggerEvent',               },
                                                                         6: { 'enum': 'VideoPolarity',                   },
                                                                         7: { 'enum': 'TriggerCoupling',                 }, }, },
    'ConfigureTriggerWindow':                          { 'parameters': { 4: { 'enum': 'TriggerWindowMode',               },
                                                                         5: { 'enum': 'TriggerCoupling',                 }, }, },
    'ExportSignal':                                    { 'parameters': { 1: { 'enum': 'ExportableSignals',               }, }, },
    'SendSoftwareTriggerEdge':                         { 'parameters': { 1: { 'enum': 'WhichTrigger',                    }, }, },
    'FetchMeasurement':                                { 'parameters': { 3: { 'enum': 'ScalarMeasurement',               }, }, },
    'FetchMeasurementStats':                           { 'parameters': { 3: { 'enum': 'ScalarMeasurement',               }, }, },
    'ReadMeasurement':                                 { 'parameters': { 3: { 'enum': 'ScalarMeasurement',               }, }, },
    'AcquisitionStatus':                               { 'parameters': { 1: { 'enum': 'AcquisitionStatus',               }, }, },
    'AddWaveformProcessing':                           { 'parameters': { 2: { 'enum': 'ArrayMeasurement',                }, }, },  # Private measurement library
    'ActualMeasWfmSize':                               { 'parameters': { 1: { 'enum': 'ArrayMeasurement',                }, }, },  # Private measurement library
    'FetchArrayMeasurement':                           { 'parameters': { 3: { 'enum': 'ArrayMeasurement',                }, }, },  # Private measurement library
}

# This is the additional metadata needed by the code generator in order create code that can properly handle buffer allocation.
functions_buffer_info = {
    'GetError':                                 { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'self_test':                                { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'GetAttributeViString':                     { 'parameters': { 4: { 'size': {'mechanism':'ivi-dance', 'value':'bufSize'}, }, }, },
    # 'GetCalUserDefinedInfo':                    { 'parameters': { 1: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From LabVIEW VI, even though niDMM_GetCalUserDefinedInfoMaxSize() exists.
    'error_message':                            { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'ConfigureEqualizationFilterCoefficients':  { 'parameters': { 3: { 'size': {'mechanism':'len', 'value':'numberOfCoefficients'}, }, }, },
    'GetEqualizationFilterCoefficients':        { 'parameters': { 3: { 'size': {'mechanism':'passed-in', 'value':'numberOfCoefficients'}, }, }, },
    'GetFrequencyResponse':                     { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, },
                                                                  4: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, },
                                                                  5: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'FetchMeasurement':                         { 'parameters': { 4: { 'size': {'mechanism':'python-code', 'value':'self._actual_num_wfms()'}, }, }, },
    'FetchMeasurementStats':                    { 'parameters': { 4: { 'size': {'mechanism':'python-code', 'value':'self._actual_num_wfms()'}, },
                                                                  5: { 'size': {'mechanism':'python-code', 'value':'self._actual_num_wfms()'}, },
                                                                  6: { 'size': {'mechanism':'python-code', 'value':'self._actual_num_wfms()'}, },
                                                                  7: { 'size': {'mechanism':'python-code', 'value':'self._actual_num_wfms()'}, },
                                                                  8: { 'size': {'mechanism':'python-code', 'value':'self._actual_num_wfms()'}, },
                                                                  9: { 'size': {'mechanism':'python-code', 'value':'self._actual_num_wfms()'}, }, }, },
    'ReadMeasurement':                          { 'parameters': { 4: { 'size': {'mechanism':'python-code', 'value':'self._actual_num_wfms()'}, }, }, },
    'Read':                                     { 'parameters': { 4: { 'size': {'mechanism':'python-code', 'value':'(num_samples * self._actual_num_wfms())'}, },
                                                                  5: { 'size': {'mechanism':'python-code', 'value':'self._actual_num_wfms()'}, }, }, },
    'Fetch':                                    { 'parameters': { 4: { 'size': {'mechanism':'python-code', 'value':'(num_samples * self._actual_num_wfms())'}, },
                                                                  5: { 'size': {'mechanism':'python-code', 'value':'self._actual_num_wfms()'}, }, }, },
    'FetchBinary8':                             { 'parameters': { 4: { 'size': {'mechanism':'python-code', 'value':'(num_samples * self._actual_num_wfms())'}, },
                                                                  5: { 'size': {'mechanism':'python-code', 'value':'self._actual_num_wfms()'}, }, }, },
    'FetchBinary16':                            { 'parameters': { 4: { 'size': {'mechanism':'python-code', 'value':'(num_samples * self._actual_num_wfms())'}, },
                                                                  5: { 'size': {'mechanism':'python-code', 'value':'self._actual_num_wfms()'}, }, }, },
    'FetchBinary32':                            { 'parameters': { 4: { 'size': {'mechanism':'python-code', 'value':'(num_samples * self._actual_num_wfms())'}, },
                                                                  5: { 'size': {'mechanism':'python-code', 'value':'self._actual_num_wfms()'}, }, }, },
    'FetchArrayMeasurement':                    { 'parameters': { 4: { 'size': {'mechanism':'python-code', 'value':'self._actual_meas_wfm_size(array_meas_function)'}, },  # Private measurement library
                                                                  5: { 'size': {'mechanism':'python-code', 'value':'(self._actual_meas_wfm_size(array_meas_function) * self._actual_num_wfms())'}, },
                                                                  6: { 'size': {'mechanism':'python-code', 'value':'self._actual_num_wfms()'}, }, }, },
    'ExportAttributeConfigurationBuffer':       { 'parameters': { 2: { 'size': {'mechanism':'ivi-dance', 'value':'sizeInBytes'}, }, }, },
    'ImportAttributeConfigurationBuffer':       { 'parameters': { 2: { 'size': {'mechanism':'len', 'value':'sizeInBytes'}, }, }, },
}

functions_render_in_session_base = {
    'ActualMeasWfmSize':               { 'render_in_session_base': True, },  # Internally called by function with a repeated capability.
}

# The extracted metadata is incorrect. Patch it here.
# TODO(marcoskirsch): Tracked by NI internal bug 677141. Remove when that's fixed and new metadata is extracted.
functions_bad_source_metadata = {
    'GetFrequencyResponse':                     { 'parameters': { 3: { 'direction': 'out'},
                                                                  4: { 'direction': 'out'},
                                                                  5: { 'direction': 'out'}, }, },
    'ExportAttributeConfigurationBuffer':       { 'parameters': { 2: { 'direction': 'out', 'type': 'ViInt8[]'}, }, },
    'ImportAttributeConfigurationBuffer':       { 'parameters': { 2: { 'type': 'ViInt8[]'}, }, },
}

# These are functions we mark as "error_handling":True. The generator uses this information to
# change how error handling is done within those functions themselves - basically, if an error occurs,
# dont try to handle it, since the functions are only used within the context of error handling.
functions_is_error_handling = {
    'error_message':                { 'is_error_handling': True },
    'GetError':                     { 'is_error_handling': True },
}

# Default values for method parameters
functions_default_value = {
    'InitWithOptions':                               { 'parameters': { 1: { 'default_value': False, },
                                                                       2: { 'default_value': False, },
                                                                       3: { 'default_value': '""', }, }, },
    'ExportSignal':                                  { 'parameters': { 2: { 'default_value': '"None"', }, }, },
    'ConfigureTriggerWindow':                        { 'parameters': { 6: { 'default_value': 'datetime.timedelta(seconds=0.0)', },
                                                                       7: { 'default_value': 'datetime.timedelta(seconds=0.0)', }, }, },
    'ConfigureTriggerVideo':                         { 'parameters': { 2: { 'default_value': False, },
                                                                       5: { 'default_value': 1, },
                                                                       8: { 'default_value': 'datetime.timedelta(seconds=0.0)', },
                                                                       9: { 'default_value': 'datetime.timedelta(seconds=0.0)', }, }, },
    'ConfigureTriggerSoftware':                      { 'parameters': { 1: { 'default_value': 'datetime.timedelta(seconds=0.0)', },
                                                                       2: { 'default_value': 'datetime.timedelta(seconds=0.0)', }, }, },
    'Read':                                          { 'parameters': { 2: { 'default_value': 'datetime.timedelta(seconds=5.0)', }, }, },
    'Fetch':                                         { 'parameters': { 2: { 'default_value': 'datetime.timedelta(seconds=5.0)', }, }, },
    'FetchBinary8':                                  { 'parameters': { 2: { 'default_value': 'datetime.timedelta(seconds=5.0)', }, }, },
    'FetchBinary16':                                 { 'parameters': { 2: { 'default_value': 'datetime.timedelta(seconds=5.0)', }, }, },
    'FetchBinary32':                                 { 'parameters': { 2: { 'default_value': 'datetime.timedelta(seconds=5.0)', }, }, },
    'ReadMeasurement':                               { 'parameters': { 2: { 'default_value': 'datetime.timedelta(seconds=5.0)', }, }, },
    'FetchMeasurement':                              { 'parameters': { 2: { 'default_value': 'datetime.timedelta(seconds=5.0)', }, }, },
    'FetchMeasurementStats':                         { 'parameters': { 2: { 'default_value': 'datetime.timedelta(seconds=5.0)', }, }, },
    'ConfigureVertical':                             { 'parameters': { 3: { 'default_value': 0.0, },
                                                                       5: { 'default_value': 1.0, },
                                                                       6: { 'default_value': True, }, }, },
    'ConfigureRefLevels':                            { 'parameters': { 1: { 'default_value': 10.0, },
                                                                       2: { 'default_value': 50.0, },
                                                                       3: { 'default_value': 90.0, }, }, },
    'CalSelfCalibrate':                              { 'parameters': { 2: { 'default_value': 'Option.SELF_CALIBRATE_ALL_CHANNELS', }, }, },
    'ClearWaveformMeasurementStats':                 { 'parameters': { 2: { 'default_value': '_ClearableMeasurement.ALL_MEASUREMENTS', }, }, },
    'ConfigureTriggerDigital':                       { 'parameters': { 2: { 'default_value': 'TriggerSlope.POSITIVE', },
                                                                       3: { 'default_value': 'datetime.timedelta(seconds=0.0)', },
                                                                       4: { 'default_value': 'datetime.timedelta(seconds=0.0)', }, }, },
    'ConfigureTriggerEdge':                          { 'parameters': { 3: { 'default_value': 'TriggerSlope.POSITIVE', },
                                                                       5: { 'default_value': 'datetime.timedelta(seconds=0.0)', },
                                                                       6: { 'default_value': 'datetime.timedelta(seconds=0.0)', }, }, },
    'ConfigureTriggerHysteresis':                    { 'parameters': { 4: { 'default_value': 'TriggerSlope.POSITIVE', },
                                                                       6: { 'default_value': 'datetime.timedelta(seconds=0.0)', },
                                                                       7: { 'default_value': 'datetime.timedelta(seconds=0.0)', }, }, },
    'FetchArrayMeasurement':                         { 'parameters': { 2: { 'default_value': 'datetime.timedelta(seconds=5.0)', }, }, },  # Private measurement library
}

# Converted parameters
functions_converters = {
    'ConfigureTriggerDigital':              { 'parameters': { 3: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', },
                                                              4: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'ConfigureTriggerEdge':                 { 'parameters': { 5: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', },
                                                              6: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'ConfigureTriggerHysteresis':           { 'parameters': { 6: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', },
                                                              7: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'ConfigureTriggerSoftware':             { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', },
                                                              2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'ConfigureTriggerVideo':                { 'parameters': { 8: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', },
                                                              9: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'ConfigureTriggerWindow':               { 'parameters': { 6: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', },
                                                              7: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'Fetch':                                { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'FetchArrayMeasurement':                { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'FetchBinary16':                        { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'FetchBinary32':                        { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'FetchBinary8':                         { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'FetchComplex':                         { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'FetchComplexBinary16':                 { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'FetchMeasurement':                     { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'FetchMeasurementStats':                { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'Read':                                 { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'ReadMeasurement':                      { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
    'InitWithOptions':                      { 'parameters': { 3: { 'python_api_converter_name': 'convert_init_with_options_dictionary', 
                                                                   'type_in_documentation': 'dict', }, }, },
    'FetchArrayMeasurement':                { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',  # Private measurement library
                                                                   'type_in_documentation': 'float in seconds or datetime.timedelta', }, }, },
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
                    'description': 'The instrument handle you obtain from niScope_init that identifies a particular instrument session.',
                },
            },
        ],
        'documentation': {
            'description': '''
Runs the instrument self-test routine and returns the test result(s). Refer to the
device-specific help topics for an explanation of the message contents.

Raises `SelfTestError` on self test failure. Attributes on exception object:

- code - failure code from driver
- message - status message from driver
''',
            'table_body': [['0', 'Passed self-test'], ['1', 'Self-test failed']],
            'table_header': ['Self-Test Code', 'Description'],
},
    },
    'FancyFetch': {
        'codegen_method': 'python-only',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'The instrument handle you obtain from niScope_init that identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
                'documentation': {
                    'description': 'The channel(s) to fetch from.',
                },
            },
            {
                'direction': 'in',
                'default_value': None,
                'name': 'numSamples',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the function raises.',
                },
            },
            {
                'direction': 'in',
                'enum': 'FetchRelativeTo',
                'default_value': 'FetchRelativeTo.PRETRIGGER',
                'name': 'relativeTo',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Position to start fetching within one record.',
                },
            },
            {
                'direction': 'in',
                'default_value': 0,
                'name': 'offset',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Offset in samples to start fetching data within each record. The offset can be positive or negative.',
                },
            },
            {
                'direction': 'in',
                'default_value': 0,
                'name': 'recordNumber',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Zero-based index of the first record to fetch.',
                },
            },
            {
                'direction': 'in',
                'default_value': None,
                'name': 'numRecords',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Number of records to fetch. Use -1 to fetch all configured records.',
                },
            },
            {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'ViReal64',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'python_type': 'float or datetime.timedelta',
                'default_value': 'datetime.timedelta(seconds=5.0)',
                'documentation': {
                    'description': 'The time to wait for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 seconds for this parameter implies infinite timeout.',
                },
            },
            {
                'direction': 'out',
                'name': 'wfmInfo',
                'type': 'struct niScope_wfmInfo[]',
                'documentation': {
                    'description': '''
Returns an array of classes with the following timing and scaling information about each waveform:

-  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform
-  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
-  **x_increment** (float) the time between points in the acquired waveform in seconds
-  **channel** (str) channel name this waveform was asquire from
-  **record** (int) record number of this waveform
-  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:

    .. math::

        voltage = binary data * gain factor + offset

-  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:

    .. math::

        voltage = binary data * gain factor + offset

- **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired
''',
                },
            },
        ],
        'documentation': {
            'description': '''
Returns the waveform from a previously initiated acquisition that the
digitizer acquires for the specified channel. This function returns
scaled voltage waveforms.

This function may return multiple waveforms depending on the number of
channels, the acquisition type, and the number of records you specify.''',
            'note': 'Some functionality, such as time stamping, is not supported in all digitizers.',
        },
    },
    'FancyRead': {
        'codegen_method': 'python-only',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'The instrument handle you obtain from niScope_init that identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
                'documentation': {
                    'description': 'The channel(s) to read from.',
                },
            },
            {
                'direction': 'in',
                'default_value': None,
                'name': 'numSamples',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the function raises.',
                },
            },
            {
                'direction': 'in',
                'enum': 'FetchRelativeTo',
                'default_value': 'FetchRelativeTo.PRETRIGGER',
                'name': 'relativeTo',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Position to start fetching within one record.',
                },
            },
            {
                'direction': 'in',
                'default_value': 0,
                'name': 'offset',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Offset in samples to start fetching data within each record. The offset can be positive or negative.',
                },
            },
            {
                'direction': 'in',
                'default_value': 0,
                'name': 'recordNumber',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Zero-based index of the first record to fetch.',
                },
            },
            {
                'direction': 'in',
                'default_value': None,
                'name': 'numRecords',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Number of records to fetch. Use -1 to fetch all configured records.',
                },
            },
            {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'ViReal64',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'python_type': 'float or datetime.timedelta',
                'default_value': 'datetime.timedelta(seconds=5.0)',
                'documentation': {
                    'description': 'The time to wait for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 seconds for this parameter implies infinite timeout.',
                },
            },
            {
                'direction': 'out',
                'name': 'wfmInfo',
                'type': 'struct niScope_wfmInfo[]',
                'documentation': {
                    'description': '''
Returns an array of classes with the following timing and scaling information about each waveform:

-  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform
-  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
-  **x_increment** (float) the time between points in the acquired waveform in seconds
-  **channel** (str) channel name this waveform was asquire from
-  **record** (int) record number of this waveform
-  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:

    .. math::

        voltage = binary data * gain factor + offset

-  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:

    .. math::

        voltage = binary data * gain factor + offset

- **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired
''',
                },
            },
        ],
        'documentation': {
            'description': '''
Initiates an acquisition, waits for it to complete, and retrieves the
data. The process is similar to calling niScope_InitiateAcquisition,
niScope_AcquisitionStatus, and niScope_Fetch. The only difference is
that with niScope_Read, you enable all channels specified with
**channelList** before the acquisition; in the other method, you enable
the channels with niScope_ConfigureVertical.

This function may return multiple waveforms depending on the number of
channels, the acquisition type, and the number of records you specify.''',
            'note': 'Some functionality, such as time stamping, is not supported in all digitizers.',
        },
    },
    'FetchDispatcher': {
        'codegen_method': 'python-only',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'The instrument handle you obtain from niScope_init that identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViChar[]',
                'documentation': {
                    'description': 'The channel(s) to fetch from.',
                },
            },
            {
                'direction': 'in',
                'name': 'Wfm',
                'type': 'ViReal64[]', # Type doesn't really matter for this function
                'documentation': {
                    'description': '''
numpy array of the appropriate type and size the should be acquired as a 1D array. Size should be **num_samples** times number of waveforms. Call niScope_ActualNumWfms to determine the number of waveforms.

Types supported are

- `numpy.float64`
- `numpy.int8`
- `numpy.in16`
- `numpy.int32`

Example:

.. code-block:: python

    waveform = numpy.ndarray(num_samples * session.actual_num_wfms(), dtype=numpy.float64)
    wfm_info = session['0,1'].fetch_into(num_samples, waveform, timeout=5.0)''',
                },
            },
            {
                'direction': 'in',
                'enum': 'FetchRelativeTo',
                'default_value': 'FetchRelativeTo.PRETRIGGER',
                'name': 'relativeTo',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Position to start fetching within one record.',
                },
            },
            {
                'direction': 'in',
                'default_value': 0,
                'name': 'offset',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Offset in samples to start fetching data within each record.The offset can be positive or negative.',
                },
            },
            {
                'direction': 'in',
                'default_value': 0,
                'name': 'recordNumber',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Zero-based index of the first record to fetch.',
                },
            },
            {
                'direction': 'in',
                'default_value': None,
                'name': 'numRecords',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Number of records to fetch. Use -1 to fetch all configured records.',
                },
            },
            {
                'direction': 'in',
                'name': 'Timeout',
                'type': 'ViReal64',
                'default_value': 'datetime.timedelta(seconds=5.0)',
                'documentation': {
                    'description': 'The time to wait in seconds for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 for this parameter implies infinite timeout.',
                },
            },
            {
                'direction': 'out',
                'name': 'wfmInfo',
                'type': 'struct niScope_wfmInfo[]',
                'documentation': {
                    'description': '''
Returns an array of classed with the following timing and scaling information about each waveform:

-  **relative_initial_x** (float) the time (in seconds) from the trigger to the first sample in the fetched waveform
-  **absolute_initial_x** (float) timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
-  **x_increment** (float) the time between points in the acquired waveform in seconds
-  **channel** (str) channel name this waveform was asquire from
-  **record** (int) record number of this waveform
-  **gain** (float) the gain factor of the given channel; useful for scaling binary data with the following formula:

    .. math::

        voltage = binary data * gain factor + offset

-  **offset** (float) the offset factor of the given channel; useful for scaling binary data with the following formula:

    .. math::

        voltage = binary data * gain factor + offset

- **samples** (array of float) floating point array of samples. Length will be of the actual samples acquired
''',
                },
            },
        ],
        'documentation': {
            'description': '''
Returns the waveform from a previously initiated acquisition that the
digitizer acquires for the specified channel. This function returns
scaled voltage waveforms.

This function may return multiple waveforms depending on the number of
channels, the acquisition type, and the number of records you specify.''',
            'note': 'Some functionality, such as time stamping, is not supported in all digitizers.',
        },
    },
    'FancyGetEqualizationFilterCoefficients': {
        'codegen_method': 'python-only',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'The instrument handle you obtain from niScope_init that identifies a particular instrument session.',
                },
            },
            {
                'direction': 'in',
                'name': 'channel',
                'type': 'ViChar[]',
                'documentation': {
                    'description': 'The channel to configure.',
                },
            },
        ],
        'documentation': {
            'description': 'Retrieves the custom coefficients for the equalization FIR filter on the device. This filter is designed to compensate the input signal for artifacts introduced to the signal outside of the digitizer. Because this filter is a generic FIR filter, any coefficients are valid. Coefficient values should be between +1 and –1.',
        },
    },
    # niScope metadata is missing error_message but we need it for error handling - NI internal CAR #700582
    'error_message': {
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init or niScope_InitWithOptions. The default is None.',
                },
            },
            {
                'direction': 'in',
                'name': 'errorCode',
                'type': 'ViStatus',
                'documentation': {
                    'description': 'The **error_code** returned from the instrument. The default is 0, indicating VI_SUCCESS.',
                },
            },
            {
                'direction': 'out',
                'name': 'errorMessage',
                'type': 'ViChar[ ]',
                'documentation': {
                    'description': 'The error information formatted into a string.',
                },
            },
        ],
        'documentation': {
            'description': 'Takes the **Error_Code** returned by the instrument driver functions, interprets it, and returns it as a user-readable string.',
        },
    },
}

# Override the 'python' name for some functions.
functions_python_name = {
    'FetchDispatcher':                        { 'python_name': 'fetch', },
    'FancyFetch':                             { 'python_name': 'fetch', },
    'FancyRead':                              { 'python_name': 'read', },
    'FancyGetEqualizationFilterCoefficients': { 'python_name': 'get_equalization_filter_coefficients', },
    'CalSelfCalibrate':                       { 'python_name': 'self_cal', },  # We want to use a common name for self_cal across all drivers
}

# Set parameter name to Waveform instead of Wfm, even for private functions (for consistency)
functions_parameter_names = {
    'FetchBinary8':               { 'parameters': { 4: { 'name': 'Waveform', }, }, },
    'FetchBinary8':               { 'parameters': { 4: { 'name': 'Waveform', }, }, },
    'FetchBinary16':              { 'parameters': { 4: { 'name': 'Waveform', }, }, },
    'FetchBinary32':              { 'parameters': { 4: { 'name': 'Waveform', }, }, },
    'Fetch':                      { 'parameters': { 4: { 'name': 'Waveform', }, }, },
    'FetchDispatcher':            { 'parameters': { 2: { 'name': 'Waveform', }, }, },
    'Read':                       { 'parameters': { 4: { 'name': 'Waveform', }, }, },
}

functions_method_templates = {
    'FetchBinary8':    { 'method_templates': [
        { 'session_filename': 'numpy_read_method', 'method_python_name_suffix': '_into_numpy', },
    ], },
    'FetchBinary16':   { 'method_templates': [
        { 'session_filename': 'numpy_read_method', 'method_python_name_suffix': '_into_numpy', },
    ], },
    'FetchBinary32':   { 'method_templates': [
        { 'session_filename': 'numpy_read_method', 'method_python_name_suffix': '_into_numpy', },
    ], },
    'Fetch':           { 'method_templates': [
        { 'session_filename': 'default_method', 'method_python_name_suffix': '', },
        { 'session_filename': 'numpy_read_method', 'method_python_name_suffix': '_into_numpy', },
    ], },
    'FetchDispatcher': { 'method_templates': [
        { 'session_filename': 'fetch_waveform', 'documentation_filename': 'default_method', 'method_python_name_suffix': '_into', },
    ], },
    'FancyFetch':      { 'method_templates': [
        { 'session_filename': 'fancy_fetch', 'documentation_filename': 'default_method', 'method_python_name_suffix': '', },
    ], },
    'FancyRead':      { 'method_templates': [
        { 'session_filename': 'fancy_fetch', 'documentation_filename': 'default_method', 'method_python_name_suffix': '', },
    ], },
    'FancyGetEqualizationFilterCoefficients':      { 'method_templates': [
        { 'session_filename': 'get_equalization_filter_coefficients', 'documentation_filename': 'default_method', 'method_python_name_suffix': '', },
    ], },
}

functions_numpy = {
    'FetchBinary8':                                  { 'parameters': { 4: { 'numpy': True, }, }, },
    'FetchBinary16':                                 { 'parameters': { 4: { 'numpy': True, }, }, },
    'FetchBinary32':                                 { 'parameters': { 4: { 'numpy': True, }, }, },
    'Fetch':                                         { 'parameters': { 4: { 'numpy': True, }, }, },
    'FetchDispatcher':                               { 'parameters': { 2: { 'numpy': True, }, }, },
}

# Parameter that need to be array.array
functions_array = {
    'FetchBinary8':                                  { 'parameters': { 4: { 'use_array': True, }, }, },
    'FetchBinary16':                                 { 'parameters': { 4: { 'use_array': True, }, }, },
    'FetchBinary32':                                 { 'parameters': { 4: { 'use_array': True, }, }, },
    'Fetch':                                         { 'parameters': { 4: { 'use_array': True, }, }, },
    'FetchDispatcher':                               { 'parameters': { 2: { 'use_array': True, }, }, },
    'Read':                                          { 'parameters': { 4: { 'use_array': True, }, }, },
    'ReadMeasurement':                               { 'parameters': { 4: { 'use_array': True, }, }, },
    'GetFrequencyResponse':                          { 'parameters': { 3: { 'use_array': True, },
                                                                       4: { 'use_array': True, },
                                                                       5: { 'use_array': True, }, }, },
}

# There are some parameters that are needed in the C function call we use under the hood, but that we do not want in the Python API
functions_remove_from_python_api = {
    'GetFrequencyResponse':                          { 'parameters': { 6: { 'use_in_python_api': False, }, }, },
}


