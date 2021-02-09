# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

functions_override_metadata = {
}

functions_additional_burst_pattern = {
    'FancyBurstPattern': {
        'python_name': 'burst_pattern',
        'codegen_method': 'python-only',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_burst_pattern',
            }
        ],
        'documentation': {
            'description': """\nUses the start_label you specify to burst the pattern on the sites you specify. If you
specify wait_until_done as True, waits for the burst to complete, and returns comparison results for each site.

Digital pins retain their state at the end of a pattern burst until the first vector of the pattern burst, a call to
niDigital_WriteStatic, or a call to niDigital_ApplyLevelsAndTiming.

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
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pattern name or exported pattern label from which to start bursting the pattern.'
                },
                'name': 'startLabel',
                'type': 'ViConstString'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that specifies whether to select the digital method for the pins in the pattern prior to bursting.'
                },
                'name': 'selectDigitalFunction',
                'type': 'ViBoolean'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that indicates whether to wait until the bursting is complete.'
                },
                'name': 'waitUntilDone',
                'type': 'ViBoolean'
            },
            {
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'Maximum time (in seconds) allowed for this method to complete. If this method does not complete within this time interval, this method returns an error.'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds',
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nDictionary where each key is a site number and value is pass/fail,\nif wait_until_done is specified as True. Else, None.\n'
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
            'description': 'Writes one waveform per site. Use this write function if you set the parameter of the create source waveform function to Site Unique.\n'
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
                    'description': 'The name to assign to the waveform. Use the waveform_name with source_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nDictionary where each key is a site number and value is a collection of samples to use as source data\n'
                },
                'name': 'waveform_data',
                'type': 'ViUInt32',  # This type is ignored since this function isn't code generated
                'type_in_documentation': '{ int: basic sequence of unsigned int, int: basic sequence of unsigned int, ... }',
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
            'description': 'Returns the pin names, site numbers, and channel names that correspond to per-pin data read from the digital pattern instrument. The function returns pin information in the same order as values read using the niDigital_ReadStatic function, niDigital_PPMU_Measure function, and niDigital_GetFailCount function. Use this function to match values the previously listed functions return with pins, sites, and instrument channels.',
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
            'description': '\nReturns dictionary where each key is a site number and value is a collection of digital states representing capture waveform data\n\n',
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
                'documentation': {
                    'description': 'Waveform name you create with the create capture waveform function. Use the waveform_name parameter with capture_start opcode in your pattern.',
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of samples to fetch.',
                },
                'name': 'samplesToRead',
                'type': 'ViInt32'
            },
            {
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'Maximum time (in seconds) allowed for this function to complete. If this function does not complete within this time interval, this function returns an error.',
                },
                'name': 'timeout',
                'type': 'ViReal64',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds',
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nDictionary where each key is a site number and value is a collection of digital states representing capture waveform data\n'
                },
                'name': 'waveform',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'ViUInt32',
                'type_in_documentation': '{ int: memoryview of array.array of unsigned int, int: memoryview of array.array of unsigned int, ... }',
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

Site number on which to retrieve pattern information must be specified via sites repeated capability.
The method returns an error if more than one site is specified.

Pins for which to retrieve pattern information must be specified via pins repeated capability.
If pins are not specified, pin list from the pattern containing the start label is used. Call
niDigital_GetPatternPinList with the start label to retrieve the pins associated with the pattern burst:

.. code:: python

 session.sites[0].pins['PinA', 'PinB'].fetch_history_ram_cycle_information(0, -1)
""",
            'note': """\nBefore bursting a pattern, you must configure the History RAM trigger and specify which cycles to acquire. 

NIDIGITAL_ATTR_HISTORY_RAM_TRIGGER_TYPE should be used to specify the trigger condition on which History RAM
starts acquiring pattern information.

If History RAM trigger is configured as NIDIGITAL_VAL_CYCLE_NUMBER,
NIDIGITAL_ATTR_CYCLE_NUMBER_HISTORY_RAM_TRIGGER_CYCLE_NUMBER should be used to specify the cycle number on which
History RAM starts acquiring pattern information.

If History RAM trigger is configured as NIDIGITAL_VAL_PATTERN_LABEL,
NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_LABEL should be used to specify the pattern label from which to
start acquiring pattern information. 
NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_VECTOR_OFFSET should be used to specify the number of vectors
following the specified pattern label from which to start acquiring pattern information. 
NIDIGITAL_ATTR_PATTERN_LABEL_HISTORY_RAM_TRIGGER_CYCLE_OFFSET should be used to specify the number of cycles
following the specified pattern label and vector offset from which to start acquiring pattern information.

For all History RAM trigger conditions, NIDIGITAL_ATTR_HISTORY_RAM_PRETRIGGER_SAMPLES should be used to specify
the number of samples to acquire before the trigger conditions are met. If you configure History RAM to only
acquire failed cycles, you must set NIDIGITAL_ATTR_HISTORY_RAM_PRETRIGGER_SAMPLES to 0. 

NIDIGITAL_ATTR_HISTORY_RAM_CYCLES_TO_ACQUIRE should be used to specify which cycles History RAM acquires after
the trigger conditions are met.
""",
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
                    'description': 'Site on which to retrieve History RAM data. The method returns an error if more than one site is specified.'
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'name': 'site',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pins for which to retrieve History RAM data. If empty, the pin list from the pattern\ncontaining the start label is used. Call niDigital_GetPatternPinList with the start\nlabel to retrieve the pins associated with the pattern burst.'
                },
                'is_repeated_capability': True,
                'repeated_capability_type': 'pins',
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
-  **expected_pin_states** (list of list of enums.PinState) Pin states as expected by the loaded
   pattern in the order specified in the pin list. Pins without defined edges in the specified DUT cycle
   will have a value of NIDIGITAL_VAL_PIN_STATE_NOT_ACQUIRED.
   Length of the outer list will be equal to the value of edge multiplier for the given vector.
   Length of the inner list will be equal to the number of pins requested.
-  **actual_pin_states** (list of list of enums.PinState) Pin states acquired by History RAM in the
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

functions_additional_load_specifications_levels_and_timing = {
    'FancyLoadSpecificationsLevelsAndTiming': {
        'python_name': 'load_specifications_levels_and_timing',
        'codegen_method': 'python-only',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_load_specifications_levels_and_timing',
            }
        ],
        'documentation': {
            'description': """\nLoads settings in specifications, levels, and timing sheets. These settings are not
applied to the digital pattern instrument until niDigital_ApplyLevelsAndTiming is called.

If the levels and timing sheets contains formulas, they are evaluated at load time.
If the formulas refer to variables, the specifications sheets that define those
variables must be loaded either first, or at the same time as the levels and timing sheets.

"""
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': '\nAbsolute file path of one or more specifications files.\n'
                },
                'name': 'specificationsFilePaths',
                'type': 'ViConstString[]',  # Value is unused, but required by code generator
                'type_in_documentation': 'str or basic sequence of str',
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': '\nAbsolute file path of one or more levels sheet files.\n'
                },
                'name': 'levelsFilePaths',
                'type': 'ViConstString[]',  # Value is unused, but required by code generator
                'type_in_documentation': 'str or basic sequence of str',
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': '\nAbsolute file path of one or more timing sheet files.\n'
                },
                'name': 'timingFilePaths',
                'type': 'ViConstString[]',  # Value is unused, but required by code generator
                'type_in_documentation': 'str or basic sequence of str',
            },
        ],
    },
}

functions_additional_unload_specifications = {
    'FancyUnloadSpecifications': {
        'python_name': 'unload_specifications',
        'codegen_method': 'python-only',
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_unload_specifications',
            }
        ],
        'documentation': {
            'description': """\nUnloads the given specifications sheets present in the previously loaded
specifications files that you select.

You must call niDigital_FancyLoadSpecificationsLevelsAndTiming to reload the files with updated
specifications values. You must then call niDigital_ApplyLevelsAndTiming in order to apply
the levels and timing values that reference the updated specifications values.

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
                    'description': '\nAbsolute file path of one or more loaded specifications files.\n'
                },
                'name': 'filePaths',
                'type': 'ViConstString[]',  # Value is unused, but required by code generator
                'type_in_documentation': 'str or basic sequence of str',
            },
        ],
    },
}
