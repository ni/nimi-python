# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
    'GetPinResultsPinInformation': {
        'codegen_method': 'private',
    },
    'FetchCaptureWaveformU32': {
        'codegen_method': 'library-only',  # We have a "fancy" wrapper for this so and we cannot use the generated python method, so only generate into the library
    },
}

functions_additional_get_pin_results_pin_information = {
    'FancyGetPinResultsPinInformation': {
        'python_name': 'get_pin_results_pin_information',
        'codegen_method': 'python-only',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_pin_results_pin_information',
            }
        ],
        'documentation': {
            'description': '\nReturns a list of named tuples (PinInfo) that <FILL IN THE BLANK HERE>\n\nFields in PinInfo:\n\n- **pin_indexes** (int)\n- **site_numbers** (int)\n- **channel_indexes** (int)\n\n',
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nList of named tuples with fields:\n\n- **pin_indexes** (int)\n- **site_numbers** (int)\n- **channel_indexes** (int)\n'
                },
                'name': 'pin_info',
                'python_type': 'PinInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'ViReal64[]'
            }
        ],
    },
}

functions_additional_fetch_capture_waveform = {
    'FancyFetchCaptureWaveform': {
        'python_name': 'fetch_capture_waveform',
        'codegen_method': 'python-only',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_fetch_capture_waveform',
            }
        ],
        'documentation': {
            'description': 'TBD'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The instrument handle you obtain from niScope_init that identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'samplesToRead',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'python_type': 'float or datetime.timedelta',
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'ViUInt32[]'
            },
        ],
    },
}
