# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
}

functions_additional_get_self_cal_last_date_and_time = {
    'FancyGetSelfCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the date and time of the last self calibration performed.',
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_cal_last_date'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **date** of the last calibration. A hightime.datetime object is returned, but only contains resolution to the day.'
                },
                'name': 'last_cal_datetime',
                'type': 'hightime.datetime'
            }
        ],
        'python_name': 'get_self_cal_last_date_and_time',
        'returns': 'ViStatus'
    }
}

functions_additional_get_ext_cal_last_date_and_time = {
    'FancyGetExtCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the date and time of the last external calibration performed.',
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_cal_last_date'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **date** of the last calibration. A hightime.datetime object is returned, but only contains resolution to the day.'
                },
                'name': 'last_cal_datetime',
                'type': 'hightime.datetime'
            }
        ],
        'python_name': 'get_ext_cal_last_date_and_time',
        'returns': 'ViStatus'
    }
}

functions_additional_get_self_cal_last_temp = {
    'FancyGetSelfCalLastTemp': {
        'codegen_method': 'python-only',
        'python_name': 'get_self_cal_last_temp',
        'documentation': {
            'description': 'Returns the onboard temperature, in degrees Celsius, of an oscilloscope at the time of the last successful external calibration.\nThe temperature returned by this node is an onboard temperature read from a sensor on the surface of the oscilloscope. This temperature should not be confused with the environmental temperature of the oscilloscope surroundings. During operation, the onboard temperature is normally higher than the environmental temperature.\nTemperature-sensitive parameters are calibrated during self-calibration. Therefore, the self-calibration temperature is usually more important to read than the external calibration temperature.',
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_cal_last_temp'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **temperature** in degrees Celsius during the last calibration.'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    }
}

functions_additional_get_ext_cal_last_temp = {
    'FancyGetExtCalLastTemp': {
        'codegen_method': 'python-only',
        'python_name': 'get_ext_cal_last_temp',
        'documentation': {
            'description': 'Returns the onboard temperature, in degrees Celsius, of an oscilloscope at the time of the last successful external calibration.\nThe temperature returned by this node is an onboard temperature read from a sensor on the surface of the oscilloscope. This temperature should not be confused with the environmental temperature of the oscilloscope surroundings. During operation, the onboard temperature is normally higher than the environmental temperature.\nTemperature-sensitive parameters are calibrated during self-calibration. Therefore, the self-calibration temperature is usually more important to read than the external calibration temperature.',
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_cal_last_temp'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niScope_init.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **temperature** in degrees Celsius during the last calibration.'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    }
}

functions_additional_fetch_array_measurement = {
    'FancyFetchArrayMeasurement': {
        'codegen_method': 'python-only',
        'python_name': 'fetch_array_measurement',
        'documentation': {
            'description': '\nObtains a waveform from the digitizer and returns the specified\nmeasurement array. This function may return multiple waveforms depending\non the number of channels, the acquisition type, and the number of\nrecords you specify.\n',
            'note': '\nSome functionality, such as time stamping, is not supported in all\ndigitizers. Refer to `Features Supported by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_1(features_supported_main)>`__ for\nmore information.\n'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
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
                    'description': "\nThe channel to configure. For more information, refer to `Channel String\nSyntax <REPLACE_DRIVER_SPECIFIC_URL_2(scopefunc.chm','cvichannelstringsyntaxforc)>`__.\n"
                },
                'name': 'channelList',
                'type': 'ViConstString'
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
                'direction': 'in',
                'documentation': {
                    'description': '\nThe `array\nmeasurement <REPLACE_DRIVER_SPECIFIC_URL_2(array_measurements_refs)>`__\nto perform.\n'
                },
                'enum': 'ArrayMeasurement',
                'name': 'arrayMeasFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe maximum number of samples returned in the measurement waveform array\nfor each waveform measurement. Use niScope_ActualMeasWfmSize to\ndetermine the number of available samples.\n',
                    'note': '\nUse the attribute NISCOPE_ATTR_FETCH_MEAS_NUM_SAMPLES to set the\nnumber of samples to fetch when performing a measurement. For more\ninformation about when to use this attribute, refer to the `NI\nKnowledgeBase <javascript:WWW(WWW_KB_MEAS)>`__.\n'
                },
                'name': 'measWfmSize',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._actual_meas_wfm_size(array_meas_function)'
                },
                'type': 'ViInt32'
            },
            {
                'default_value': 'None',
                'direction': 'in',
                'documentation': {
                    'description': '\nThe identifier for the "other channel" for multi-channel measurements such as Add Channels or Multiply Channels.'
                },
                'name': 'otherChannel',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array whose length is the number of waveforms times\n**measWfmSize**; call niScope_ActualNumWfms to determine the number of\nwaveforms; call niScope_ActualMeasWfmSize to determine the size of each\nwaveform.\n\nNI-SCOPE returns this data sequentially, so all record 0 waveforms are\nfirst. For example, with channel list of 0, 1, you would have the\nfollowing index values:\n\nindex 0 = record 0, channel 0\n\nindex *x* = record 0, channel 1\n\nindex 2\\ *x* = record 1, channel 0\n\nindex 3\\ *x* = record 1, channel 1\n\nWhere *x* = the record length\n'
                },
                'name': 'measWfm',
                'size': {
                    'mechanism': 'python-code',
                    'value': '(self._actual_meas_wfm_size(array_meas_function) * self._actual_num_wfms())'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a list of class instances with the following timing and scaling\ninformation about each waveform:\n\n-  **relativeInitialX**—the time (in seconds) from the trigger to the\n   first sample in the fetched waveform\n-  **absoluteInitialX**—timestamp (in seconds) of the first fetched\n   sample. This timestamp is comparable between records and\n   acquisitions; devices that do not support this parameter use 0 for\n   this output.\n-  **xIncrement**—the time between points in the acquired waveform in\n   seconds\n-  **actualSamples**—the actual number of samples fetched and placed in\n   the waveform array\n-  **gain**—the gain factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\n-  **offset**—the offset factor of the given channel; useful for scaling\n   binary data with the following formula:\n\nvoltage = binary data × gain factor + offset\n\nCall niScope_ActualNumWfms to determine the size of this array.\n'
                },
                'name': 'wfmInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._actual_num_wfms()'
                },
                'type': 'struct niScope_wfmInfo[]'
            }
        ],
        'returns': 'ViStatus'
    }
}
