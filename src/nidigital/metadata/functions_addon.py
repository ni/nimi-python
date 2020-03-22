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

functions_additional_get_site_pass_fail = {
    'FancyGetSitePassFail': {
        'python_name': 'get_site_pass_fail',
        'codegen_method': 'python-only',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_get_site_pass_fail',
            }
        ],
        'documentation': {
            'description': '\nReturns dictionary where each key is a site number and value is pass/fail\n\n',
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nDictionary where each key is a site number and value is pass/fail\n'
                },
                'name': 'passFail',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'ViBoolean',
                'type_in_documentation': '{ int: bool, int: bool, ... }',
            },
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
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
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
                'default_value': 'datetime.timedelta(seconds=10.0)',
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
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
            'description': """\nReturns the pattern information acquired for the specified cycles.
            
If the pattern is using the edge multiplier feature, cycle numbers represent tester cycles, each of which may
consist of multiple DUT cycles. When using pins with mixed edge multipliers, pins may return
NIDIGITAL_VAL_PIN_STATE_NOT_ACQUIRED for DUT cycles where those pins do not have edges defined.

If pins are not specified, pin list from the pattern containing the start label is used. Call
niDigital_GetPatternPinList with the start label to retrieve the pins
associated with the pattern burst.
"""
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
                'python_api_converter_name': 'convert_site_to_string',  # This won't actually change any code generation but is here for completeness
                'type_in_documentation': 'str or int',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'pins',
                'documentation': {
                    'description': 'Pins for which to retrieve History RAM data. If empty, the pin list from the pattern\ncontaining the start label is used. Call niDigital_GetPatternPinList with the start\nlabel to retrieve the pins associated with the pattern burst.'
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
                    'description': """Returns a list of class instances with
the following information about each pattern cycle:

-  **pattern_name** (str)  Name of the pattern for the acquired cycle.
-  **time_set_name** (str) Time set for the acquired cycle.
-  **vector_number** (int) Vector number within the pattern for the acquired cycle. Vector numbers start
   at 0 from the beginning of the pattern.
-  **cycle_number** (int) Cycle number acquired by this History RAM sample. Cycle numbers start at 0
   from the beginning of the pattern burst.
-  **scan_cycle_number** (int) Scan cycle number acquired by this History RAM sample. Scan cycle numbers
   start at 0 from the first cycle of the scan vector. Scan cycle numbers are -1 for cycles that do not
   have a scan opcode.
-  **expected_pin_states** (list of list of enums.DigitalState) Pin states as expected by the loaded
   pattern in the order specified in the pin list. Pins without defined edges in the specified DUT cycle
   will have a value of NIDIGITAL_VAL_PIN_STATE_NOT_ACQUIRED.
   Length of the outer list will be equal to the value of edge multiplier for the given vector.
   Length of the inner list will be equal to the number of pins requested.
-  **actual_pin_states** (list of list of enums.DigitalState) Pin states acquired by History RAM in the
   order specified in the pin list. Pins without defined edges in the specified DUT cycle will have a
   value of NIDIGITAL_VAL_PIN_STATE_NOT_ACQUIRED.
   Length of the outer list will be equal to the value of edge multiplier for the given vector.
   Length of the inner list will be equal to the number of pins requested.
-  **per_pin_pass_fail** (list of list of bool) Pass fail information for pins in the order specified in
   the pin list. Pins without defined edges in the specified DUT cycle will have a value of pass (True).
   Length of the outer list will be equal to the value of edge multiplier for the given vector.
   Length of the inner list will be equal to the number of pins requested.
"""
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
