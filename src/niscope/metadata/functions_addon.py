# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
    # TODO (ni-jfitzger): delete this override once functions.py lists "default_method" for library_interpreter_filename. See https://github.com/ni/nimi-python/issues/1938
    'FetchArrayMeasurement': {
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            }
        ]
    }
}
functions_additional_get_channel_name = {
    'GetChannelNameFromString': {
        'documentation': {
            'description': 'Returns a list of channel names for given channel indices.\n'
        },
        'included_in_proto': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:\n\n-   A comma-separated list—for example, "0,2,3,1"\n-   A range using a hyphen—for example, "0-3"\n-   A range using a colon—for example, "0:3 "\n\nYou can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0," "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.\n'
                },
                'grpc_name': 'index',
                'name': 'index',
                'python_api_converter_name': 'convert_repeated_capabilities_without_prefix',
                'python_name': 'indices',
                'type': 'ViConstString',
                'type_in_documentation': 'basic sequence types or str or int',
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViChar array you specify for name.\n'
                },
                'name': 'nameBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The channel name(s) at the specified indices.\n'
                },
                'grpc_name': 'name',
                'name': 'name',
                'python_api_converter_name': 'convert_comma_separated_string_to_list',
                'python_name': 'names',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'nameBufferSize'
                },
                'type': 'ViChar[]',
                'type_in_documentation': 'list of str',
            }
        ],
        'python_name': 'get_channel_names',
        'render_in_session_base': True,
        'returns': 'ViStatus'
    }
}
functions_additional_fetch_array_measurement = {
    'FancyFetchArrayMeasurement': {
        'codegen_method': 'python-only',
        'python_name': 'fetch_array_measurement',
        'documentation': {
            'description': '\nObtains a waveform from the digitizer and returns the specified\nmeasurement array. This function may return multiple waveforms depending\non the number of channels, the acquisition type, and the number of\nrecords you specify.\n',
            'note': '\nSome functionality, such as time stamping, is not supported in all\ndigitizers.\n'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_fetch_array_measurement'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe array measurement to perform.\n'
                },
                'enum': 'ArrayMeasurement',
                'name': 'arrayMeasFunction',
                'type': 'ViInt32'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': '\nThe maximum number of samples returned in the measurement waveform array\nfor each waveform measurement. Default Value: None (returns all available samples).\n',
                },
                'name': 'measWfmSize',
                'type': 'ViInt32'
            },
            {
                'default_value': 'FetchRelativeTo.PRETRIGGER',
                'direction': 'in',
                'documentation': {
                    'description': 'Position to start fetching within one record.'
                },
                'enum': 'FetchRelativeTo',
                'name': 'relativeTo',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Offset in samples to start fetching data within each record. The offset can be positive or negative.'
                },
                'name': 'offset',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Zero-based index of the first record to fetch.'
                },
                'name': 'recordNumber',
                'type': 'ViInt32'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'Number of records to fetch. Use `None` to fetch all configured records.'
                },
                'name': 'numRecords',
                'type': 'ViInt32'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'Number of samples to fetch when performing a measurement. Use `None` to fetch the actual record length.'
                },
                'name': 'measNumSamples',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a list of class instances with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **channel**-channel name this waveform was acquired from\n-  **record**-record number of this waveform\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **samples**-floating point array of samples. Length will be of actual samples acquired.\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    }
}

functions_additional_fetch_array_measurement_stats = {
    'FancyFetchMeasurementStats': {
        'codegen_method': 'python-only',
        'python_name': 'fetch_measurement_stats',
        'documentation': {
            'description': '\nObtains a waveform measurement and returns the measurement value. This\nfunction may return multiple statistical results depending on the number\nof channels, the acquisition type, and the number of records you\nspecify.\n\nYou specify a particular measurement type, such as rise time, frequency,\nor voltage peak-to-peak. The waveform on which the digitizer calculates\nthe waveform measurement is from an acquisition that you previously\ninitiated. The statistics for the specified measurement function are\nreturned, where the statistics are updated once every acquisition when\nthe specified measurement is fetched by any of the Fetch Measurement\nfunctions. If a Fetch Measurement function has not been called, this\nfunction fetches the data on which to perform the measurement. The\nstatistics are cleared by calling\nniScope_ClearWaveformMeasurementStats.\n\nMany of the measurements use the low, mid, and high reference levels.\nYou configure the low, mid, and high references with\nNISCOPE_ATTR_MEAS_CHAN_LOW_REF_LEVEL,\nNISCOPE_ATTR_MEAS_CHAN_MID_REF_LEVEL, and\nNISCOPE_ATTR_MEAS_CHAN_HIGH_REF_LEVEL to set each channel\ndifferently.\n'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_fetch_measurement_stats'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe instrument handle you obtain from niScope_init that identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nThe channel to configure.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe scalar measurement to be performed on each fetched waveform.\n'
                },
                'enum': 'ScalarMeasurement',
                'name': 'scalarMeasFunction',
                'type': 'ViInt32'
            },
            {
                'default_value': 'FetchRelativeTo.PRETRIGGER',
                'direction': 'in',
                'documentation': {
                    'description': 'Position to start fetching within one record.'
                },
                'enum': 'FetchRelativeTo',
                'name': 'relativeTo',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Offset in samples to start fetching data within each record. The offset can be positive or negative.'
                },
                'name': 'offset',
                'type': 'ViInt32'
            },
            {
                'default_value': 0,
                'direction': 'in',
                'documentation': {
                    'description': 'Zero-based index of the first record to fetch.'
                },
                'name': 'recordNumber',
                'type': 'ViInt32'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': 'Number of records to fetch. Use `None` to fetch all configured records.'
                },
                'name': 'numRecords',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=5.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe time to wait in seconds for data to be acquired; using 0 for this\nparameter tells NI-SCOPE to fetch whatever is currently available. Using\n-1 for this parameter implies infinite timeout.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns a list of class instances with the following measurement statistics\nabout the specified measurement:\n\n-	**result** (float): the resulting measurement\n-	**mean** (float): the mean scalar value, which is obtained by\naveraging each fetch_measurement_stats call\n-	**stdev** (float): the standard deviations of the most recent\n**numInStats** measurements\n-	**min_val** (float): the smallest scalar value acquired (the minimum\nof the **numInStats** measurements)\n-	**max_val** (float): the largest scalar value acquired (the maximum\nof the **numInStats** measurements)\n-	**num_in_stats** (int): the number of times fetch_measurement_stats has been called\n-	**channel** (str): channel name this result was acquired from\n-	**record** (int): record number of this result'
                },
                'name': 'measurement_stats',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'MeasurementStats[]'
            }
        ],
        'returns': 'ViStatus'
    }
}
