# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
}

functions_additional_write_source_waveform_site_unique = {
    'FancyWriteSourceWaveformSiteUnique': {
        'python_name': 'write_source_waveform_site_unique',
        'codegen_method': 'python-only',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_write_source_waveform_site_unique',
            }
        ],
        'documentation': {
            'description': 'TBD'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nDictionary where each key is the site number and the value is array.array of unsigned int\n'
                },
                'name': 'waveform_data',
                'type': 'ViUInt32',  # This type is ignored since this function isn't code generated
                'type_in_documentation': '{ site: data, site: data, ... }',
            },
        ],
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
            'description': '\nReturns a list of named tuples (PinInfo) that <FILL IN THE BLANK HERE>\n\nFields in PinInfo:\n\n- **pin_name** (str)\n- **site_number** (int)\n- **channel_name** (str)\n\n',
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
                    'description': '\nList of named tuples with fields:\n\n- **pin_name** (str)\n- **site_number** (int)\n- **channel_name** (str)\n'
                },
                'name': 'pin_info',
                'python_type': 'PinInfo',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'ViInt32[]'
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
            'description': '\nReturns dictionary where each key is the site number and the value is array.array of unsigned int\n\n',
        },
        'parameters': [
            {
                'direction': 'in',
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
                'documentation': {
                    'description': '\nDictionary where each key is the site number and the value is array.array of unsigned int\n'
                },
                'name': 'waveform',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'ViUInt32',
                'type_in_documentation': '{ site: data, site: data, ... }',
            },
        ],
    },
}

functions_additional_fetch_history_ram_cycle_information = {
    'FancyFetchHistoryRAMCycleInformation': {
        'python_name': 'fetch_history_ram_cycle_information',
        'codegen_method': 'python-only',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_fetch_history_ram_cycle_information',
            }
        ],
        'documentation': {
            'description': '\nReturns the pattern information acquired for the specified cycles.\n\nIf the pattern is using the edge multiplier feature, cycle numbers represent tester cycles, each of which may\nconsist of multiple DUT cycles. When using pins with mixed edge multipliers, pins may return\nNIDIGITAL_VAL_PIN_STATE_NOT_ACQUIRED for DUT cycles where those pins do not have edges defined.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Site on which to retrieve History RAM data. Specify site as a string in the form of siteN,\nwhere N is the site number. The VI returns an error if more than one site is specified.'
                },
                'name': 'site',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pins for which to retrieve History RAM data. If empty, the pin list from the pattern\ncontaining the start label is used. Call get_pattern_pin_list or get_pattern_pin_names with the start\nlabel to retrieve the pins associated with the pattern burst.'
                },
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Sample index from which to start fetching pattern information.'
                },
                'name': 'position',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of samples to fetch. A value of -1 specifies to fetch all available samples.'
                },
                'name': 'samples_to_read',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a list of class instances with\nthe following information about each pattern cycle:\n\n-  **pattern_name** (str)  Name of the pattern for the acquired cycle.\n-  **time_set_name** (str) Time set for the acquired cycle.\n-  **vector_number** (int) Vector number within the pattern for the acquired cycle. Vector numbers start\nat 0 from the beginning of the pattern.\n-  **cycle_number** (int) Cycle number acquired by this History RAM sample. Cycle numbers start at 0\nfrom the beginning of the pattern burst.\n-  **scan_cycle_number** (int) Scan cycle number acquired by this History RAM sample. Scan cycle numbers\nstart at 0 from the first cycle of the scan vector. Scan cycle numbers are -1 for cycles that do not\nhave a scan opcode.\n-  **expected_pin_states** (list) Pin state as expected by the loaded pattern in the order specified in\nthe pin list. Pins without defined edges in the specified DUT cycle will have a value of\nNIDIGITAL_VAL_PIN_STATE_NOT_ACQUIRED.\n-  **actual_pin_states** (list) Pin state acquired by History RAM in the order specified in the pin\nlist. Pins without defined edges in the specified DUT cycle will have a value of\nNIDIGITAL_VAL_PIN_STATE_NOT_ACQUIRED.\n-  **per_pin_pass_fail** (list) pass fail information for pins in the order specified in the pin list.\nPins without defined edges in the specified DUT cycle will have a value of pass (True).\n'
                },
                'name': 'history_ram_cycle_information',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'HistoryRAMCycleInformation[]'
            }
        ],
    },
}
