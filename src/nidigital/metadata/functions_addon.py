# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
    'ConfigureCycleNumberHistoryRAMTrigger': {
        'codegen_method': 'no'
    },
    'ConfigureDigitalEdgeConditionalJumpTrigger': {
        'codegen_method': 'no'
    },
    'ConfigureDigitalEdgeStartTrigger': {
        'codegen_method': 'no'
    },
    'ConfigureFirstFailureHistoryRAMTrigger': {
        'codegen_method': 'no'
    },
    'ConfigureHistoryRAMCyclesToAcquire': {
        'codegen_method': 'no'
    },
    'ConfigurePatternLabelHistoryRAMTrigger': {
        'codegen_method': 'no'
    },
    'ConfigureSoftwareEdgeConditionalJumpTrigger': {
        'codegen_method': 'no'
    },
    'ConfigureSoftwareEdgeStartTrigger': {
        'codegen_method': 'no'
    },
    'ConfigureStartLabel': {
        'codegen_method': 'no'
    },
    'ConfigureTerminationMode': {
        'codegen_method': 'no'
    },
    'DisableConditionalJumpTrigger': {
        'codegen_method': 'no'
    },
    'DisableStartTrigger': {
        'codegen_method': 'no'
    },
    'FrequencyCounter_ConfigureMeasurementTime': {
        'codegen_method': 'no'
    },
    'PPMU_ConfigureApertureTime': {
        'codegen_method': 'no'
    },
    'PPMU_ConfigureCurrentLevel': {
        'codegen_method': 'no'
    },
    'PPMU_ConfigureCurrentLevelRange': {
        'codegen_method': 'no'
    },
    'PPMU_ConfigureCurrentLimit': {
        'codegen_method': 'no'
    },
    'PPMU_ConfigureCurrentLimitRange': {
        'codegen_method': 'no'
    },
    'PPMU_ConfigureOutputFunction': {
        'codegen_method': 'no'
    },
    'PPMU_ConfigureVoltageLevel': {
        'codegen_method': 'no'
    },
    'PPMU_ConfigureVoltageLimits': {
        'codegen_method': 'no'
    },
    'SelectFunction': {
        'codegen_method': 'no'
    }
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
