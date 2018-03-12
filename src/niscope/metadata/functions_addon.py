# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
    'InitWithOptions':                  { 'codegen_method': 'private',  },
    'InitiateAcquisition':              { 'codegen_method': 'private',  },
    'close':                            { 'codegen_method': 'private',  },
    'CheckAttribute.+':                 { 'codegen_method': 'no',       },  # We do not include any Check Attribute functions
    '.etAttribute.+':                   { 'codegen_method': 'private',  },  # All Set/Get Attribute functions are private
    'init':                             { 'codegen_method': 'no',       },
    'IsDeviceReady':                    { 'codegen_method': 'no',       },  # Used by SFP to address a very slow to come up digitizer.
    'error_message':                    { 'codegen_method': 'private',  },
    'GetError':                         { 'codegen_method': 'private',  },
    'ClearError':                       { 'codegen_method': 'no',       },
    'LockSession':                      { 'codegen_method': 'no',       },
    'UnlockSession':                    { 'codegen_method': 'no',       },
    '.+ExtCal':                         { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'CalAdjust.+':                      { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    '.+UserDefined.+':                  { 'codegen_method': 'no',       },
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
    'GetFrequencyResponse':             { 'codegen_method': 'no',       },  # TODO(marcoskirsch): add back when #606 is fixed
    'FetchComplex':                     { 'codegen_method': 'no',       },  # TODO(marcoskirsch): No support for complex numbers. Issue #514
    'FetchComplexBinary16':             { 'codegen_method': 'no',       },  # TODO(marcoskirsch):No support for complex numbers. Issue #514
    'FetchBinary8':                     { 'codegen_method': 'private',  },
    'FetchBinary16':                    { 'codegen_method': 'private',  },
    'FetchBinary32':                    { 'codegen_method': 'private',  },
    'Fetch':                            { 'codegen_method': 'private',  },
    'ActualNumWfms':                    { 'codegen_method': 'private',  },  # We use it internally so the customer doesn't have to.
    '.etAttributeViInt64':              { 'codegen_method': 'no',       },  # NI-SCOPE has no ViInt64 attributes.
    'ClearWaveformProcessing':          { 'codegen_method': 'no',       },  # Per #667, removing waveform measurement methods
    'AddWaveformProcessing':            { 'codegen_method': 'no',       },  # Per #667, removing waveform measurement methods
    'FetchArrayMeasurement':            { 'codegen_method': 'no',       },  # Per #667, removing waveform measurement methods
    'ActualMeasWfmSize':                { 'codegen_method': 'no',       },  # Per #667, removing waveform measurement methods
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
}

# This is the additional metadata needed by the code generator in order create code that can properly handle buffer allocation.
functions_buffer_info = {
    'GetError':                                 { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'self_test':                                { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'GetAttributeViString':                     { 'parameters': { 4: { 'size': {'mechanism':'ivi-dance', 'value':'bufSize'}, }, }, },
    'GetCalUserDefinedInfo':                    { 'parameters': { 1: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From LabVIEW VI, even though niDMM_GetCalUserDefinedInfoMaxSize() exists.
    'error_message':                            { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'ConfigureEqualizationFilterCoefficients':  { 'parameters': { 3: { 'size': {'mechanism':'len', 'value':'numberOfCoefficients'}, }, }, },
    'GetEqualizationFilterCoefficients':        { 'parameters': { 3: { 'size': {'mechanism':'passed-in', 'value':'numberOfCoefficients'}, }, }, },
    # TODO(marcoskirsch): Won't work until we fix #606
    # 'GetFrequencyResponse':                     { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, },
    #                                                               4: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, },
    #                                                               5: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
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
}

# The extracted metadata is incorrect. Patch it here.
# TODO(marcoskirsch): Tracked by NI internal bug 677141. Remove when that's fixed and new metadata is extracted.
functions_bad_source_metadata = {
    'GetFrequencyResponse':                     { 'parameters': { 3: { 'direction': 'out'},
                                                                  4: { 'direction': 'out'},
                                                                  5: { 'direction': 'out'}, }, },
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
    'ClearWaveformMeasurementStats':                 { 'parameters': { 2: { 'default_value': 'ClearableMeasurement.ALL_MEASUREMENTS', }, }, },
    'ConfigureTriggerDigital':                       { 'parameters': { 2: { 'default_value': 'TriggerSlope.POSITIVE', },
                                                                       3: { 'default_value': 'datetime.timedelta(seconds=0.0)', },
                                                                       4: { 'default_value': 'datetime.timedelta(seconds=0.0)', }, }, },
    'ConfigureTriggerEdge':                          { 'parameters': { 2: { 'default_value': 0.0, },
                                                                       3: { 'default_value': 'TriggerSlope.POSITIVE', },
                                                                       5: { 'default_value': 'datetime.timedelta(seconds=0.0)', },
                                                                       6: { 'default_value': 'datetime.timedelta(seconds=0.0)', }, }, },
    'ConfigureTriggerHysteresis':                    { 'parameters': { 2: { 'default_value': 0.0, },
                                                                       3: { 'default_value': 0.05, },
                                                                       4: { 'default_value': 'TriggerSlope.POSITIVE', },
                                                                       6: { 'default_value': 'datetime.timedelta(seconds=0.0)', },
                                                                       7: { 'default_value': 'datetime.timedelta(seconds=0.0)', }, }, },
}

# Converted parameters
functions_converters = {
    'ConfigureTriggerDigital':              { 'parameters': { 3: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', },
                                                              4: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', }, }, },
    'ConfigureTriggerEdge':                 { 'parameters': { 5: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', },
                                                              6: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', }, }, },
    'ConfigureTriggerHysteresis':           { 'parameters': { 6: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', },
                                                              7: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', }, }, },
    'ConfigureTriggerSoftware':             { 'parameters': { 1: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', },
                                                              2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', }, }, },
    'ConfigureTriggerVideo':                { 'parameters': { 8: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', },
                                                              9: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', }, }, },
    'ConfigureTriggerWindow':               { 'parameters': { 6: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', },
                                                              7: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', }, }, },
    'Fetch':                                { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', }, }, },
    'FetchArrayMeasurement':                { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', }, }, },
    'FetchBinary16':                        { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', }, }, },
    'FetchBinary32':                        { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', }, }, },
    'FetchBinary8':                         { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', }, }, },
    'FetchComplex':                         { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', }, }, },
    'FetchComplexBinary16':                 { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', }, }, },
    'FetchMeasurement':                     { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', }, }, },
    'FetchMeasurementStats':                { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', }, }, },
    'FancyFetch':                           { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', }, }, },
    'Read':                                 { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', }, }, },
    'ReadMeasurement':                      { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds',
                                                                   'python_type': 'datetime.timedelta', }, }, },
    'InitWithOptions':                      { 'parameters': { 3: { 'python_api_converter_name': 'convert_init_with_options_dictionary', 
                                                                   'python_type': 'dict', }, }, },
}

# Functions not in original metadata.
functions_additional_functions = {
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
                    'description': 'The channel to configure.',
                },
            },
            {
                'direction': 'in',
                'default_value': None,
                'name': 'numSamples',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'The maximum number of samples to fetch for each waveform. If the acquisition finishes with fewer points than requested, some devices return partial data if the acquisition finished, was aborted, or a timeout of 0 was used. If it fails to complete within the timeout period, the function throws an exception.',
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
                    'description': 'Offset in samples to start fetching data within each record. The offset is applied relative to NISCOPE_ATTR_FETCH_RELATIVE_TO. The offset can be positive or negative.',
                },
            },
            {
                'direction': 'in',
                'default_value': 0,
                'name': 'recordNumber',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Zero-based index of the first record to fetch.  Use NISCOPE_ATTR_NUM_RECORDS to set the number of records to fetch.',
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
                    'description': 'The time to wait for data to be acquired; using 0 for this parameter tells NI-SCOPE to fetch whatever is currently available. Using -1 seconds for this parameter implies infinite timeout.',
                },
            },
            {
                'direction': 'out',
                'name': 'wfmInfo',
                'type': 'struct niScope_wfmInfo[]',
                'documentation': {
                    'description': '''
Returns an array of classed with the following timing and scaling information about each waveform:

-  **relative_initial_x** the time (in seconds) from the trigger to the first sample in the fetched waveform
-  **absolute_initial_x** timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
-  **x_increment** the time between points in the acquired waveform in seconds -  **actual_samples** the actual number of samples fetched and placed in the waveform array
-  **gain** the gain factor of the given channel; useful for scaling binary data with the following formula:

    .. math::

        voltage = binary data * gain factor + offset

-  **offset** the offset factor of the given channel; useful for scaling binary data with the following formula:

    .. math::

        voltage = binary data * gain factor + offset

- **waveform** waveform array whose length is the **numSamples**

Call niScope_ActualNumWfms to determine the size of this array.''',
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
                    'description': 'The channel to configure.',
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
                    'description': 'Offset in samples to start fetching data within each record. The offset is applied relative to NISCOPE_ATTR_FETCH_RELATIVE_TO. The offset can be positive or negative.',
                },
            },
            {
                'direction': 'in',
                'default_value': 0,
                'name': 'recordNumber',
                'type': 'ViInt32',
                'documentation': {
                    'description': 'Zero-based index of the first record to fetch.  Use NISCOPE_ATTR_NUM_RECORDS to set the number of records to fetch.',
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

-  **relative_initial_x** the time (in seconds) from the trigger to the first sample in the fetched waveform
-  **absolute_initial_x** timestamp (in seconds) of the first fetched sample. This timestamp is comparable between records and acquisitions; devices that do not support this parameter use 0 for this output.
-  **x_increment** the time between points in the acquired waveform in seconds -  **actual_samples** the actual number of samples fetched and placed in the waveform array
-  **gain** the gain factor of the given channel; useful for scaling binary data with the following formula:

    .. math::

        voltage = binary data * gain factor + offset

-  **offset** the offset factor of the given channel; useful for scaling binary data with the following formula:

    .. math::

        voltage = binary data * gain factor + offset

Call niScope_ActualNumWfms to determine the size of this array.''',
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
}

# Override the 'python' name for some functions.
functions_python_name = {
    'FetchDispatcher':            { 'python_name': 'fetch', },
    'FancyFetch':                 { 'python_name': 'fetch', },
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
}


