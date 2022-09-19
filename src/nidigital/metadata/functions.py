# -*- coding: utf-8 -*-
# This file is generated from NI-Digital Pattern Driver API metadata version 21.3.0d40
functions = {
    'Abort': {
        'documentation': {
            'description': 'Stops bursting the pattern.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'AbortKeepAlive': {
        'documentation': {
            'description': 'Stops the keep alive pattern if it is currently running. If a pattern burst is in progress, the function aborts the pattern burst. If you start a new pattern burst while a keep alive pattern is running, the keep alive pattern runs to the last keep alive vector, and the new pattern burst starts on the next cycle.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ApplyLevelsAndTiming': {
        'documentation': {
            'description': 'Applies digital levels and timing values defined in previously loaded levels and timing sheets. When applying a levels sheet, only the levels specified in the sheet are affected. Any levels not specified in the sheet remain unchanged. When applying a timing sheet, all existing time sets are deleted before the new time sets are loaded.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'documentation': {
                    'description': 'Comma-delimited list of strings in the form of ``siteN`` , where ``N`` is the site number. If you enter an empty string, this function applies the levels and initial states to all sites.\n'
                },
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Name of the levels sheet to apply. Use the name of the sheet or pass the absolute file path you use in the niDigital_FancyLoadSpecificationsLevelsAndTiming function. The name of the levels sheet is the file name without the directory and file extension.\n'
                },
                'name': 'levelsSheet',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Name of the timing sheet to apply. Use the name of the sheet or pass the absolute file path that you use in the niDigital_FancyLoadSpecificationsLevelsAndTiming function. The name of the timing sheet is the file name without the directory and file extension.\n'
                },
                'name': 'timingSheet',
                'type': 'ViConstString'
            },
            {
                'default_value': 'None',
                'direction': 'in',
                'documentation': {
                    'description': 'Comma-delimited list of pins, pin groups, or channels to initialize to a high state.\n'
                },
                'name': 'initialStateHighPins',
                'python_api_converter_name': 'convert_repeated_capabilities_without_prefix',
                'type': 'ViConstString',
                'type_in_documentation': 'basic sequence types or str',
            },
            {
                'default_value': 'None',
                'direction': 'in',
                'documentation': {
                    'description': 'Comma-delimited list of pins, pin groups, or channels to initialize to a low state.\n'
                },
                'name': 'initialStateLowPins',
                'python_api_converter_name': 'convert_repeated_capabilities_without_prefix',
                'type': 'ViConstString',
                'type_in_documentation': 'basic sequence types or str',
            },
            {
                'default_value': 'None',
                'direction': 'in',
                'documentation': {
                    'description': 'Comma-delimited list of pins, pin groups, or channels to initialize to a non-drive state (X)\n'
                },
                'name': 'initialStateTristatePins',
                'python_api_converter_name': 'convert_repeated_capabilities_without_prefix',
                'type': 'ViConstString',
                'type_in_documentation': 'basic sequence types or str',
            }
        ],
        'returns': 'ViStatus'
    },
    'ApplyTDROffsets': {
        'documentation': {
            'description': 'Applies the correction for propagation delay offsets to a digital pattern instrument. Use this function to apply TDR offsets that are stored from a past measurement or are measured by means other than the niDigital_TDR function. Also use this function to apply correction for offsets if the **applyOffsets** input of the niDigital_TDR function was set to False at the time of measurement.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of offsets.\n'
                },
                'name': 'numOffsets',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'TDR offsets to apply, in seconds. Specify an offset for each pin or channel in the repeated capabilities. If the repeated capabilities contain pin names, you must specify offsets for each site in the channel map per pin.\n'
                },
                'name': 'offsets',
                'python_api_converter_name': 'convert_timedeltas_to_seconds_real64',
                'size': {
                    'mechanism': 'len',
                    'value': 'numOffsets'
                },
                'type': 'ViReal64[]',
                'type_in_documentation': 'basic sequence of hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'BurstPattern': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Uses the **startLabel** you specify to burst the pattern on the sites you specify and provides the option to wait for the burst to complete. Digital pins retain their state at the end of a pattern burst until the first vector of a subsequent pattern burst, a call to niDigital_WriteStatic, or a call to niDigital_ApplyLevelsAndTiming.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'documentation': {
                    'description': 'The sites on which to burst the pattern as a comma-delimited list of strings in the form site\\ ``N``, where ``N`` is the site number. If you specify an empty string, the pattern is burst on all sites.\n'
                },
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pattern name or exported pattern label from which to start bursting the pattern.\n'
                },
                'name': 'startLabel',
                'type': 'ViConstString'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that specifies whether to select the digital function for the pins in the pattern prior to bursting.\n'
                },
                'name': 'selectDigitalFunction',
                'type': 'ViBoolean'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that indicates whether to wait until the bursting is complete.\n'
                },
                'name': 'waitUntilDone',
                'type': 'ViBoolean'
            },
            {
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'Maximum time (in seconds) allowed for this function to complete. If this function does not complete within this time interval, this function returns an error.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearError': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Clears the error information for the current execution thread and the IVI session you specify. If you pass VI_NULL for the **vi** parameter, this function clears the error information only for the current execution thread.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClockGenerator_Abort': {
        'documentation': {
            'description': 'Stops clock generation on the specified channel(s) or pin(s) and pin group(s).\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            }
        ],
        'python_name': 'clock_generator_abort',
        'returns': 'ViStatus'
    },
    'ClockGenerator_GenerateClock': {
        'documentation': {
            'description': 'Configures clock generator frequency and initiates clock generation on the specified channel(s) or pin(s) and pin group(s).\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The frequency of the clock generation, in Hz.\n'
                },
                'name': 'frequency',
                'type': 'ViReal64'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that specifies whether to select the digital function for the pins specified prior to starting clock generation.\n'
                },
                'name': 'selectDigitalFunction',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'clock_generator_generate_clock',
        'returns': 'ViStatus'
    },
    'ClockGenerator_Initiate': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Initiates clock generation on the specified channel(s) or pin(s) and pin group(s).\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            }
        ],
        'python_name': 'clock_generator_initiate',
        'returns': 'ViStatus'
    },
    'Commit': {
        'documentation': {
            'description': 'Applies all previously configured pin levels, termination modes, clocks, triggers, and pattern timing to a digital pattern instrument. If you do not call the niDigital_Commit function, then the initiate function or the niDigital_FancyBurstPattern function will implicitly call this function for you. Calling this function moves the session from the Uncommitted state to the Committed state.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureActiveLoadLevels': {
        'documentation': {
            'description': 'Configures I\\ :sub:`OL`, I\\ :sub:`OH`, and V\\ :sub:`COM` levels for the active load on the pins you specify. The DUT sources or sinks current based on the level values. To enable active load, set the termination mode to NIDIGITAL_VAL_ACTIVE_LOAD. To disable active load, set the termination mode of the instrument to NIDIGITAL_VAL_HIGH_Z or NIDIGITAL_VAL_VTERM.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Maximum current that the DUT sinks while outputting a voltage below V\\ :sub:`COM`.\n'
                },
                'name': 'iol',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Maximum current that the DUT sources while outputting a voltage above V\\ :sub:`COM`.\n'
                },
                'name': 'ioh',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Commutating voltage level at which the active load circuit switches between sourcing current and sinking current.\n'
                },
                'name': 'vcom',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePatternBurstSites': {
        'documentation': {
            'description': 'Configures which sites burst the pattern on the next call to the initiate function. The pattern burst sites can also be modified through the repeated capabilities for the niDigital_FancyBurstPattern function. If a site has been disabled through the niDigital_DisableSites function, the site does not burst a pattern even if included in the pattern burst sites.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'documentation': {
                    'description': 'A comma-delimited list of strings in the form of site\\ ``N``, where ``N`` is the site number. If you specify an empty string, the function returns pass or fail results for all sites. If the string is empty, all sites are configured for pattern bursting.\n'
                },
                'name': 'siteList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetCompareEdgesStrobe': {
        'documentation': {
            'description': 'Configures the strobe edge time for the specified pins. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital_ApplyLevelsAndTiming; it only affects the values of the current timing context.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'pins',
                'documentation': {
                    'description': 'List of pin and pin group names for which to configure the time set edges.\n'
                },
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeSetName',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Time when the comparison happens within a vector period.\n'
                },
                'name': 'strobeEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetCompareEdgesStrobe2x': {
        'documentation': {
            'description': 'Configures the compare strobes for the specified pins in the time set, including the 2x strobe. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital_ApplyLevelsAndTiming; it only affects the values of the current timing context.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'pins',
                'documentation': {
                    'description': 'List of pin and pin group names for which to configure the time set edges.\n'
                },
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeSetName',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Time when the comparison happens within a vector period.\n'
                },
                'name': 'strobeEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Time when the comparison happens for the second DUT cycle within a vector period.\n'
                },
                'name': 'strobe2Edge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetDriveEdges': {
        'documentation': {
            'description': 'Configures the drive format and drive edge placement for the specified pins. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital_ApplyLevelsAndTiming; it only affects the values of the current timing context.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'pins',
                'documentation': {
                    'description': 'List of pin and pin group names for which to configure the time set edges.\n'
                },
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeSetName',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Drive format of the time set.\n\n-   NIDIGITAL_VAL_NR: Non-return.\n-   NIDIGITAL_VAL_RL: Return to low.\n-   NIDIGITAL_VAL_RH: Return to high.\n-   NIDIGITAL_VAL_SBC: Surround by complement.\n'
                },
                'enum': 'DriveFormat',
                'name': 'format',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period for turning on the pin driver.This option applies only when the prior vector left the pin in a non-drive pin state (L, H, X, V, M, E). For the SBC format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven.\n'
                },
                'name': 'driveOnEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period until the pattern data is driven to the pattern value.The ending state from the previous vector persists until this point.\n'
                },
                'name': 'driveDataEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format.\n'
                },
                'name': 'driveReturnEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive symbol (L, H, X, V, M, E).\n'
                },
                'name': 'driveOffEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetDriveEdges2x': {
        'documentation': {
            'description': 'Configures the drive edges of the pins in the time set, including 2x edges. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital_ApplyLevelsAndTiming; it only affects the values of the current timing context.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'pins',
                'documentation': {
                    'description': 'List of pin and pin group names for which to configure the time set edges.\n'
                },
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeSetName',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Drive format of the time set.\n\n-   NIDIGITAL_VAL_NR: Non-return.\n-   NIDIGITAL_VAL_RL: Return to low.\n-   NIDIGITAL_VAL_RH: Return to high.\n-   NIDIGITAL_VAL_SBC: Surround by complement.\n'
                },
                'enum': 'DriveFormat',
                'name': 'format',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period for turning on the pin driver.This option applies only when the prior vector left the pin in a non-drive pin state (L, H, X, V, M, E). For the SBC format, this option specifies the delay from the beginning of the vector period at which the complement of the pattern value is driven.\n'
                },
                'name': 'driveOnEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period until the pattern data is driven to the pattern value.The ending state from the previous vector persists until this point.\n'
                },
                'name': 'driveDataEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data to the return value, as specified in the format.\n'
                },
                'name': 'driveReturnEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period to turn off the pin driver when the next vector period uses a non-drive symbol (L, H, X, V, M, E).\n'
                },
                'name': 'driveOffEdge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period until the pattern data in the second DUT cycle is driven to the pattern value.\n'
                },
                'name': 'driveData2Edge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Delay, in seconds, from the beginning of the vector period until the pin changes from the pattern data in the second DUT cycle to the return value, as specified in the format.\n'
                },
                'name': 'driveReturn2Edge',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetDriveFormat': {
        'documentation': {
            'description': 'Configures the drive format for the pins specified in the **pinList**. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital_ApplyLevelsAndTiming; it only affects the values of the current timing context.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'pins',
                'documentation': {
                    'description': 'List of pin and pin group names for which to configure the time set edges.\n'
                },
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeSetName',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Drive format of the time set.\n\n-   NIDIGITAL_VAL_NR: Non-return.\n-   NIDIGITAL_VAL_RL: Return to low.\n-   NIDIGITAL_VAL_RH: Return to high.\n-   NIDIGITAL_VAL_SBC: Surround by complement.\n'
                },
                'enum': 'DriveFormat',
                'name': 'driveFormat',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetEdge': {
        'documentation': {
            'description': 'Configures the edge placement for the pins specified in the pin list. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital_ApplyLevelsAndTiming; it only affects the values of the current timing context.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified digital pattern instrument handle\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'pins',
                'documentation': {
                    'description': 'List of pin and pin group names for which to configure the time set edges.\n'
                },
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeSetName',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Name of the edge.\n\n-   NIDIGITAL_VAL_DRIVE_ON\n-   NIDIGITAL_VAL_DRIVE_DATA\n-   NIDIGITAL_VAL_DRIVE_RETURN\n-   NIDIGITAL_VAL_DRIVE_OFF\n-   NIDIGITAL_VAL_COMPARE_STROBE\n-   NIDIGITAL_VAL_DRIVE_DATA2\n-   NIDIGITAL_VAL_DRIVE_RETURN2\n-   NIDIGITAL_VAL_COMPARE_STROBE2\n'
                },
                'enum': 'TimeSetEdgeType',
                'name': 'edge',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The time from the beginning of the vector period in which to place the edge.\n'
                },
                'name': 'time',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetEdgeMultiplier': {
        'documentation': {
            'description': 'Configures the edge multiplier of the pins in the time set. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital_ApplyLevelsAndTiming; it only affects the values of the current timing context.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified digital pattern instrument handle\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'pins',
                'documentation': {
                    'description': 'List of pin and pin group names for which to configure the time set edges.\n'
                },
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeSetName',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified edge multiplier for the pins in the pin list.\n'
                },
                'name': 'edgeMultiplier',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTimeSetPeriod': {
        'documentation': {
            'description': 'Configures the period of a time set. Use this function to modify time set values after applying a timing sheet with the niDigital_ApplyLevelsAndTiming function, or to create time sets programmatically without the use of timing sheets. This function does not modify the timing sheet file or the timing sheet contents that will be used in future calls to niDigital_ApplyLevelsAndTiming; it only affects the values of the current timing context.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'timeSetName',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Period for this time set, in seconds.\n'
                },
                'name': 'period',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureVoltageLevels': {
        'documentation': {
            'description': 'Configures voltage levels for the pins you specify.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Voltage that the instrument will apply to the input of the DUT when the pin driver drives a logic low (0).\n'
                },
                'name': 'vil',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Voltage that the instrument will apply to the input of the DUT when the test instrument drives a logic high (1).\n'
                },
                'name': 'vih',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Output voltage below which the comparator on the pin driver interprets a logic low (L).\n'
                },
                'name': 'vol',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Output voltage above which the comparator on the pin driver interprets a logic high (H).\n'
                },
                'name': 'voh',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Termination voltage the instrument applies during non-drive cycles when the termination mode is set to V\\ :sub:`term`. The instrument applies the termination voltage through a 50 ohm parallel termination resistance.\n'
                },
                'name': 'vterm',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateCaptureWaveformFromFileDigicapture': {
        'documentation': {
            'description': 'Creates a capture waveform with the configuration information from a Digicapture file generated by the Digital Pattern Editor.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Waveform name you want to use. You must specify waveform_name if the file contains multiple waveforms. Use the waveform_name with the capture_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Absolute file path to the capture waveform file (.digicapture) you want to load.\n'
                },
                'name': 'waveformFilePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateCaptureWaveformParallel': {
        'documentation': {
            'description': 'Sets the capture waveform settings for parallel acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'pins',
                'documentation': {
                    'description': 'List of capture pins from the waveform. The **pinList** must match the capture pins in the pattern that references the waveform. The pin order in the **pinList** determines the bit positions of the data captured by the niDigital_FetchCaptureWaveform function.\n'
                },
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Waveform name you want to use. Use the waveform_name with the capture_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateCaptureWaveformSerial': {
        'documentation': {
            'description': 'Sets the capture waveform settings for serial acquisition. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'pins',
                'documentation': {
                    'description': 'List of capture pins from the waveform. The **pinList** must match the capture pins in the pattern that references the waveform. The pin order in the **pinList** determines the bit positions of the data captured by the niDigital_FetchCaptureWaveform function.\n'
                },
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Waveform name you want to use. Use the waveform_name with the capture_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Width in bits of each serial sample. Valid values are between 1 and 32.\n'
                },
                'name': 'sampleWidth',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Order in which to shift the bits.\n\n-   NIDIGITAL_VAL_MSB_FIRST: Specifies the bit order by most significant bit first.\n-   NIDIGITAL_VAL_LSB_FIRST: Specifies the bit order by least significant bit first.\n'
                },
                'enum': 'BitOrder',
                'name': 'bitOrder',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateSourceWaveformFromFileTDMS': {
        'documentation': {
            'description': 'Creates a source waveform with configuration information from a TDMS file generated by the Digital Pattern Editor. It also optionally writes waveform data from the file.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The waveform name you want to use from the file. You must specify waveform_name if the file contains multiple waveforms. Use the waveform_name with the source_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Absolute file path to the load source waveform file (.tdms).\n'
                },
                'name': 'waveformFilePath',
                'type': 'ViConstString'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that writes waveform data to source memory if True and the waveform data is in the file.\n'
                },
                'name': 'writeWaveformData',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateSourceWaveformParallel': {
        'documentation': {
            'description': 'Sets the source waveform settings required for parallel sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'pins',
                'documentation': {
                    'description': 'Source pins for the waveform. The **pinList** must match the source pins in the pattern that references the waveform. The pin order in the **pinList** determines the bit positions of the data written by the niDigital_WriteSourceWaveform function.\n'
                },
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Parameter that specifies how to map data on multiple sites.\n\n-   NIDIGITAL_VAL_BROADCAST: Broadcasts the waveform you specify to all sites.\n-   NIDIGITAL_VAL_SITE_UNIQUE: Sources unique waveform data to each site.\n'
                },
                'enum': 'SourceDataMapping',
                'name': 'dataMapping',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateSourceWaveformSerial': {
        'documentation': {
            'description': 'Sets the source waveform settings required for serial sourcing. Settings apply across all sites if multiple sites are configured in the pin map. You cannot reconfigure settings after waveforms are created.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'pins',
                'documentation': {
                    'description': 'Source pins for the waveform. The **pinList** must match the source pins in the pattern that references the waveform. The pin order in the **pinList** determines the bit positions of the data written by the niDigital_WriteSourceWaveform function.\n'
                },
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Parameter that specifies how to map data on multiple sites.\n\n-   NIDIGITAL_VAL_BROADCAST: Broadcasts the waveform you specify to all sites.\n-   NIDIGITAL_VAL_SITE_UNIQUE: Sources unique waveform data to each site.\n'
                },
                'enum': 'SourceDataMapping',
                'name': 'dataMapping',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Width in bits of each serial sample. Valid values are between 1 and 32.\n'
                },
                'name': 'sampleWidth',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Order in which to shift the bits.\n\n-   NIDIGITAL_VAL_MSB_FIRST: Specifies the bit order by most significant bit first.\n-   NIDIGITAL_VAL_LSB_FIRST: Specifies the bit order by least significant bit first.\n'
                },
                'enum': 'BitOrder',
                'name': 'bitOrder',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateTimeSet': {
        'documentation': {
            'description': 'Creates a time set with the name that you specify. Use this function when you want to create time sets programmatically rather than with a timing sheet.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified name of the new time set.\n'
                },
                'name': 'name',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteAllTimeSets': {
        'documentation': {
            'description': 'Deletes all time sets from instrument memory.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableSites': {
        'documentation': {
            'description': 'Disables specified sites. Disabled sites are not included in pattern bursts initiated by the initiate function or the niDigital_FancyBurstPattern function, even if the site is specified in the list of pattern burst sites in niDigital_ConfigurePatternBurstSites function or in the repeated capabilities for the niDigital_FancyBurstPattern function. Additionally, if you specify a list of pin or pin group names in repeated capabilities in any NI-Digital function, digital pattern instrument channels mapped to disabled sites are not affected by the function. The functions that return per-pin data, such as the niDigital_PPMU_Measure function, do not return data for channels mapped to disabled sites. The digital pattern instrument channels mapped to the sites specified are left in their current state. NI TestStand Semiconductor Module requires all sites to always be enabled, and manages the set of active sites without disabling the sites in the digital instrument session. Do not use this function with the Semiconductor Module.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'documentation': {
                    'description': 'Comma-delimited list of strings in the form of site\\ ``N``, where ``N`` is the site number. If you enter an empty string, the function disables all sites.\n'
                },
                'name': 'siteList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnableSites': {
        'documentation': {
            'description': 'Enables the sites you specify. All sites are enabled by default.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'documentation': {
                    'description': 'Comma-delimited list of strings in the form of site\\ ``N``, where ``N`` is the site number. If you enter an empty string, the function enables all sites.\n'
                },
                'name': 'siteList',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'FancySelfTest': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns self test results from a digital pattern instrument. This test requires several minutes to execute.\n\nRaises `SelfTestError` on self test failure. Attributes on exception object:\n\n- code - failure code from driver\n- message - status message from driver\n',
            'table_body': [
                [
                    '0',
                    'Self test passed.'
                ],
                [
                    '1',
                    'Self test failed.'
                ]
            ],
            'table_header': [
                'Self-Test Code',
                'Description'
            ]
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'none',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_self_test'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'self_test',
        'returns': 'ViStatus'
    },
    'FetchCaptureWaveformU32': {
        'codegen_method': 'library-only',
        'documentation': {
            'description': 'Fetches a defined number of samples for a specific list of sites. This function only returns data from sites that are enabled when fetch is called.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'documentation': {
                    'description': 'Site numbers listed as a comma-delimited list of strings of form site\\ ``N``, where ``N`` is the site number. If you enter an empty string, the function fetches data from all sites.\n'
                },
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Waveform name you create with the create capture waveform function. Use the waveform_nam parameter with capture_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of samples to fetch.\n'
                },
                'name': 'samplesToRead',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Maximum time (in seconds) allowed for this function to complete. If this function does not complete within this time interval, this function returns an error.\n'
                },
                'name': 'timeout',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViUInt32 array you specify for data. To determine the size of the buffer to allocate for the data array, pass a value of 0 to the **dataBufferSize** parameter and a value of VI_NULL to the **data** parameter. In this case, the value returned by the **actualNumWaveforms** and **actualSamplesPerWaveform** parameters determine the size of the array necessary to hold the data. The data buffer size should be the number of samples per waveform multiplied by the number of waveforms.\n'
                },
                'name': 'dataBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An array of digital states read from the sites in the repeated capabilities. Each row in the array corresponds to a site in the list. If a site is disabled, not enabled for burst, or the current instrument does not include any capture pins, the function does not return data for that site. Data for each site in the repeated capabilities are returned sequentially (non-interleaved). If you are using a list of pin names to read data from multiple instruments, use the niDigital_SortSiteResultsViUInt32Waveform function to order and combine the data to match the repeated capabilities. You can also use the niDigital_GetSiteResultsSiteNumbers function to obtain a list of returned sites.\n'
                },
                'name': 'data',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'dataBufferSize',
                    'value_twist': 'actualNumWaveforms'
                },
                'type': 'ViUInt32[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of waveforms written to the data array.\n'
                },
                'name': 'actualNumWaveforms',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of samples per waveform written to the data array.\n'
                },
                'name': 'actualSamplesPerWaveform',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchHistoryRAMCycleInformation': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Gets the per-cycle pattern information acquired for the specified cycle.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'documentation': {
                    'description': 'Site specified as a string in the form of ``siteN``, where ``N`` is the site number. The function returns an error if more than one site is specified.\n'
                },
                'name': 'site',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The index of the History RAM sample to fetch. Each History RAM sample contains information about a single cycle in the pattern burst.\n'
                },
                'name': 'sampleIndex',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned index of the pattern for the acquired cycle. Use niDigital_GetPatternName to get the name of the pattern from its index.\n'
                },
                'name': 'patternIndex',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned time set for the acquired cycle. Use niDigital_GetTimeSetName to get the name of the time set from its index.\n'
                },
                'name': 'timeSetIndex',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned vector number within the pattern for the acquired cycle. Vector numbers start at 0 from the beginning of the pattern.\n'
                },
                'name': 'vectorNumber',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the cycle number acquired by this History RAM sample. Cycle numbers start at 0 from the beginning of the pattern burst.\n'
                },
                'name': 'cycleNumber',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned number of DUT cycles contained in the cycle acquired by this History RAM sample. This is only needed if the pattern uses the edge multiplier feature.\n'
                },
                'name': 'numDutCycles',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchHistoryRAMCyclePinData': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Gets the per-pin pattern data acquired for the specified cycle.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'documentation': {
                    'description': 'Site specified as a string in the form of ``siteN``, where ``N`` is the site number. The function returns an error if more than one site is specified.\n'
                },
                'name': 'site',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified pins for which to retrieve History RAM data. If empty, the pin list from the pattern containing the start label is used. Call niDigital_GetPatternPinList or niDigital_GetPatternPinIndexeswith the start label to retrieve the pins associated with the pattern burst.\n'
                },
                'name': 'pinList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The index of the History RAM sample to fetch. Each History RAM sample contains information about a single cycle in the pattern burst.\n'
                },
                'name': 'sampleIndex',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified index of the DUT cycle. If the pattern does not use the edge multiplier feature, pass 0 for this parameter. For History RAM samples that contain multiple DUT cycles, indicated by the **numDutCycles** value returned by niDigital_FetchHistoryRAMCycleInformation, call this function multiple times to retrieve pin states for each DUT cycle. The DUT cycle index should start at 0.\n'
                },
                'name': 'dutCycleIndex',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified number of elements in the **expectedPinStates**, **actualPinStates**, and **perPinPassFail** arrays. All three array parameters must be of the same size if they are not set to VI_NULL.\n\nTo determine the size of the buffer to allocate for the arrays, pass a value of 0 to the **pinDataBufferSize** parameter and a value of VI_NULL to the array parameters. In this case, the value returned by the **actualNumPinData** parameter is the size of the arrays necessary to hold the data.\n'
                },
                'name': 'pinDataBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned pin state as expected by the loaded pattern in the order specified in **pinList**. Pins without defined edges in the specified DUT cycle will return NIDIGITAL_VAL_NOT_A_PIN_STATE\n'
                },
                'enum': 'PinState',
                'name': 'expectedPinStates',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'pinDataBufferSize',
                    'value_twist': 'actualNumPinData'
                },
                'type': 'ViUInt8[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned pin state acquired by History RAM in the order specified in **pinList**. Pins without defined edges in the specified DUT cycle will return NIDIGITAL_VAL_NOT_A_PIN_STATE\n'
                },
                'enum': 'PinState',
                'name': 'actualPinStates',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'pinDataBufferSize',
                    'value_twist': 'actualNumPinData'
                },
                'type': 'ViUInt8[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned pass fail information for pins in the order specified in **pinList**. Pins without defined edges in the specified DUT cycle will return pass (VI_TRUE).\n'
                },
                'name': 'perPinPassFail',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'pinDataBufferSize',
                    'value_twist': 'actualNumPinData'
                },
                'type': 'ViBoolean[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of values written to the array parameters.\n'
                },
                'name': 'actualNumPinData',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchHistoryRAMScanCycleNumber': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Fetches the History RAM Scan Cycle Number for the sample index. If the sample is not from a scan vector, the scan cycle number will be returned as -1.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'documentation': {
                    'description': 'Site specified as a string in the form of ``siteN``, where ``N`` is the site number. The function returns an error if more than one site is specified.\n'
                },
                'name': 'site',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The index of the History RAM sample to fetch. Each History RAM sample contains information about a single cycle in the pattern burst.\n'
                },
                'name': 'sampleIndex',
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the scan cycle number acquired by this History RAM sample. Scan cycle numbers start at 0 from the first cycle of the scan vector. Scan cycle numbers are -1 for cycles that do not have a scan opcode.\n'
                },
                'name': 'scanCycleNumber',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FrequencyCounter_MeasureFrequency': {
        'documentation': {
            'description': 'Measures the frequency on the specified channel(s) over the specified measurement time. All channels in the repeated capabilities should have the same measurement time.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified number of elements in the ViReal64 array you specify for the frequency counter measurements.\n'
                },
                'name': 'frequenciesBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned frequency counter measurement, in Hz.This function returns -1 if the measurement is invalid for the channel.\n'
                },
                'name': 'frequencies',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'frequenciesBufferSize',
                    'value_twist': 'actualNumFrequencies'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned number of frequency counter measurements written to the measurements array.\n'
                },
                'name': 'actualNumFrequencies',
                'type': 'ViInt32'
            }
        ],
        'python_name': 'frequency_counter_measure_frequency',
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViBoolean attribute. Use this function to get the values of digital pattern instrument-specific attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned current value of the attribute; pass the address of a ViBoolean variable.\n'
                },
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViInt32 attribute. Use this function to get the values of digital pattern instrument-specific attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned current value of the attribute; pass the address of a ViInt32 variable.\n'
                },
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViInt64 attribute. Use this function to get the values of digital pattern instrument-specific attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned current value of the attribute; pass the address of a ViInt64 variable.\n'
                },
                'name': 'value',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'This function queries the value of a ViReal64 attribute. Use this function to get the values of digital pattern instrument-specific attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned current value of the attribute; pass the address of a ViReal64 variable.\n'
                },
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Queries the value of a ViString attribute. Use this function to get the values of digital pattern instrument-specific attributes and inherent IVI attributes. You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the **bufferSize**. If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **bufferSize**, the function copies (bufferSize - 1) bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the **bufferSize** you must pass to get the entire value. For example, if the value is "123456" and the **bufferSize** is 4, the function places "123" into the buffer and returns 7. If you want to call this function just to get the required buffer size, you can pass 0 for the **bufferSize** and VI_NULL for the value.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViChar array you specify for value.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The buffer in which the function returns the current value of the attribute; the buffer must be of type ViChar and have at least as many bytes as indicated in the **bufferSize**.\n'
                },
                'name': 'value',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetChannelName': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Returns the channel name that corresponds to the index you specify. Channel indexes are one-based. You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the **nameBufferSize**. If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the buffer size, the function copies (buffer size - 1) bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. If you want to call this function just to get the required buffer size, you can pass 0 for **nameBufferSize** and VI_NULL for the name.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies a one-based index for the desired channel in the session. Valid values are from one to the total number of channels in the session.\n'
                },
                'name': 'index',
                'type': 'ViInt32'
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
                    'description': 'The returned channel name(s) at the specified index.\n'
                },
                'name': 'name',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'nameBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetChannelNameFromString': {
        'documentation': {
            'description': 'Returns a list of channel names for given channel indices.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Index list for the channels in the session. Valid values are from zero to the total number of channels in the session minus one. The index string can be one of the following formats:\n\n-   A comma-separated list—for example, "0,2,3,1"\n-   A range using a hyphen—for example, "0-3"\n-   A range using a colon—for example, "0:3 "\n\nYou can combine comma-separated lists and ranges that use a hyphen or colon. Both out-of-order and repeated indices are supported ("2,3,0," "1,2,2,3"). White space characters, including spaces, tabs, feeds, and carriage returns, are allowed between characters. Ranges can be incrementing or decrementing.\n'
                },
                'name': 'indices',
                'python_api_converter_name': 'convert_repeated_capabilities_without_prefix',
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
                'name': 'names',
                'python_api_converter_name': 'convert_comma_separated_string_to_list',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'nameBufferSize'
                },
                'type': 'ViChar[]',
                'type_in_documentation': 'list of str',
            }
        ],
        'python_name': 'get_channel_names',
        'render_in_session_base': True,  # Used in FancyGetPinResultsPinInformation()
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the error information associated with the digital pattern instrument handle. This function retrieves and then clears the error information for the session. If **vi** is VI_NULL, this function retrieves and then clears the error information for the current thread. You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the buffer size. If the current value of the error description, including the terminating NULL byte, is larger than the size you indicate in the buffer size, the function copies (buffer size -1) bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. If you want to call this function just to get the required buffer size, you can pass 0 for the buffer size and VI_NULL for **errorDescription**.\n'
        },
        'is_error_handling': True,
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'none'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned error code for the session or execution thread.\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViChar array you specify for **errorDescription**.\n'
                },
                'name': 'errorDescriptionBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned error description for the IVI session or execution thread.\nIf there is no description, the function returns an empty string. The buffer must contain at least as many elements as the value you specify with the buffer size parameter.\nIf you pass 0 for **errorDescriptionBufferSize**, you can pass VI_NULL for this parameter.\n'
                },
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'errorDescriptionBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'GetFailCount': {
        'documentation': {
            'description': 'Returns the comparison fail count for pins in the repeated capabilities.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViInt64 array you specify for **failureCount**. To determine the size of the buffer to allocate for the **failureCount** array, pass a value of 0 to the **bufferSize** parameter and a value of VI_NULL to the **failureCount** parameter. In this case, the value returned by the **actualNumRead** parameter is the size of the array necessary to hold the failure counts.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of failures in an array. If a site is disabled or not enabled for burst, the function does not return data for that site. You can also use the niDigital_FancyGetPinResultsPinInformation function to obtain a sorted list of returned sites and channels.\n'
                },
                'name': 'failureCount',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualNumRead'
                },
                'type': 'ViInt64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of failure count values written to the **failureCount** array.\n'
                },
                'name': 'actualNumRead',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetHistoryRAMSampleCount': {
        'documentation': {
            'description': 'Returns the number of samples History RAM acquired on the last pattern burst.\n',
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
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'documentation': {
                    'description': 'Site specified as a string in the form of ``siteN``, where ``N`` is the site number. The function returns an error if more than one site is specified.\n'
                },
                'name': 'site',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned number of samples that History RAM acquired.\n'
                },
                'name': 'sampleCount',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetPatternName': {
        'codegen_method': 'private',
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
                'name': 'patternIndex',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'nameBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'name',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'nameBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'render_in_session_base': True,  # Called from FancyFetchHistoryRAMCycleInformation() which uses rep cap
        'returns': 'ViStatus'
    },
    'GetPatternPinList': {
        'documentation': {
            'description': 'Returns the pattern pin list.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pattern name or exported pattern label from which to get the pin names that the pattern references.\n'
                },
                'name': 'startLabel',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViChar array you specify for **pinList**.\n'
                },
                'name': 'pinListBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'List of pins referenced by the pattern with the **startLabel**.\n'
                },
                'name': 'pinList',
                'python_api_converter_name': 'convert_comma_separated_string_to_list',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'pinListBufferSize'
                },
                'type': 'ViChar[]',
                'type_in_documentation': 'list of str',
            }
        ],
        'python_name': 'get_pattern_pin_names',
        'returns': 'ViStatus'
    },
    'GetPinName': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the name of the pin at the index you specify. You must provide a ViChar array to serve as a buffer for the value. You pass the number of bytes in the buffer as the **nameBufferSize**. If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the buffer size, the function copies (buffer size - 1) bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7. If you want to call this function just to get the required buffer size, you can pass 0 for **nameBufferSize** and VI_NULL for the name.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Index of pin to query. Pin indexes begin at 0.\n'
                },
                'name': 'pinIndex',
                'type': 'ViInt32'
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
                    'description': 'Returns the pin name at the specified **pinIndex**.\n'
                },
                'name': 'name',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'nameBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'render_in_session_base': True,
        'returns': 'ViStatus'
    },
    'GetPinResultsPinInformation': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the pin names, site numbers, and channel names that correspond to per-pin data read from the digital pattern instrument. The function returns pin information in the same order as values read using the niDigital_ReadStatic function, niDigital_PPMU_Measure function, and niDigital_GetFailCount function. Use this function to match values the previously listed functions return with pins, sites, and instrument channels.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the arrays you specify for **pinIndexes**, **siteNumbers**, and **channelIndexes**, if they are not NULL. To determine the size of the buffer to allocate for the arrays, pass a value of 0 to the **bufferSize** parameter and a value of VI_NULL to the array parameters. In this case, the value returned by the **actualNumValues** parameter is the size of the arrays necessary to hold the output values.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned index of the pins corresponding to data read from the digital pattern instrument using the specified repeated capabilities. If you do not want to use this parameter, pass VI_NULL.\nCall niDigital_GetPinName to get the name of the pin associated with an index.\n'
                },
                'name': 'pinIndexes',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualNumValues'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned site numbers that correspond to data read from the digital pattern instrument using the specified repeated capabilities. If you do not want to use this parameter, pass VI_NULL.\n'
                },
                'name': 'siteNumbers',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualNumValues'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned index of channels corresponding to data read from the digital pattern instrument using the specified repeated capabilities. If you do not want to use this parameter, pass VI_NULL.\nCall niDigital_GetChannelName to get the name of the channel associated with an index. Channel indexes are one-based.\n'
                },
                'name': 'channelIndexes',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualNumValues'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The number of values written to the output arrays. This function always writes the same number of values to all output arrays, if they are not set to VI_NULL.\n'
                },
                'name': 'actualNumValues',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSitePassFail': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the pass or fail results for each site.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'documentation': {
                    'description': 'A comma-delimited list of strings in the form of site\\ ``N``, where ``N`` is the site number. If you specify an empty string, the function returns pass or fail results for all sites.\n'
                },
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViBoolean array you specify for **passFail**. To determine the size of the buffer to allocate for the **passFail** array, pass a value of 0 to the **passFailBufferSize** parameter and a value of VI_NULL to the **passFail** parameter. In this case, the value returned by the **actualNumSites** parameter is the size of the array necessary to hold the pass/fail values.\n'
                },
                'name': 'passFailBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned array of pass (VI_TRUE) and fail results for the sites you specify in the repeated capabilities. If sites span multiple digital pattern instruments, you must use an AND operator for the partial results for those sites returned by each instrument. If a site is disabled or not enabled for burst, the function does not return data for that site. Use the niDigital_SortSiteResultsViBoolean function to order and combine the data to match the repeated capabilities. You can also use the niDigital_GetSiteResultsSiteNumbers function to determine the order of the sites returned from this function call so that you can match the pass array with site numbers.\n'
                },
                'name': 'passFail',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'passFailBufferSize',
                    'value_twist': 'actualNumSites'
                },
                'type': 'ViBoolean[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of values written to the **passFailBufferSize** and **passFail** arrays.\n'
                },
                'name': 'actualNumSites',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSiteResultsSiteNumbers': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the site numbers that correspond to per-site data read from the digital pattern instrument. The function returns site numbers in the same order as values read using the niDigital_GetSitePassFail and niDigital_FetchCaptureWaveformU32 functions. Use this function to match values the previously listed functions return with site numbers.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'documentation': {
                    'description': 'Site numbers listed as a comma-delimited list of strings of form site\\ ``N``, where ``N`` is the site number.\n'
                },
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The type of data specified in the results array.\n\n-   NIDIGITAL_VAL_PASS_FAIL: Get site numbers for pass/fail data.\n-   NIDIGITAL_VAL_CAPTURE_WAVEFORM: Get site numbers for capture waveforms.\n'
                },
                'enum': 'SiteResultType',
                'name': 'siteResultType',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViInt32 array you specify for **siteNumbers**. To determine the size of the buffer to allocate for the **siteNumbers** array, pass a value of 0 to the **siteNumbersBufferSize** parameter and a value of VI_NULL to the **siteNumbers** parameter. In this case, the value returned by the **actualNumSiteNumbers** parameter is the size of the array necessary to hold the site numbers.\n'
                },
                'name': 'siteNumbersBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned array of site numbers that correspond to the values specified by **siteResultType**.\n'
                },
                'name': 'siteNumbers',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'siteNumbersBufferSize',
                    'value_twist': 'actualNumSiteNumbers'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of sites written in the **siteNumbers** array.\n'
                },
                'name': 'actualNumSiteNumbers',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetTimeSetDriveFormat': {
        'documentation': {
            'description': 'Returns the drive format of a pin in the specified time set.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified digital pattern instrument handle\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'pins',
                'documentation': {
                    'description': 'Name of the specified pin.\n'
                },
                'name': 'pin',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeSetName',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returned drive format of the time set for the specified pin.\n'
                },
                'enum': 'DriveFormat',
                'name': 'format',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetTimeSetEdge': {
        'documentation': {
            'description': 'Returns the edge time of a pin in the specified time set.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified digital pattern instrument handle\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'pins',
                'documentation': {
                    'description': 'Name of the specified pin.\n'
                },
                'name': 'pin',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeSetName',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Name of the edge.\n\n-   NIDIGITAL_VAL_DRIVE_ON\n-   NIDIGITAL_VAL_DRIVE_DATA\n-   NIDIGITAL_VAL_DRIVE_RETURN\n-   NIDIGITAL_VAL_DRIVE_OFF\n-   NIDIGITAL_VAL_COMPARE_STROBE\n-   NIDIGITAL_VAL_DRIVE_DATA2\n-   NIDIGITAL_VAL_DRIVE_RETURN2\n-   NIDIGITAL_VAL_COMPARE_STROBE2\n'
                },
                'enum': 'TimeSetEdgeType',
                'name': 'edge',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Time from the beginning of the vector period in which to place the edge.\n'
                },
                'name': 'time',
                'python_api_converter_name': 'convert_seconds_real64_to_timedelta',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetTimeSetEdgeMultiplier': {
        'documentation': {
            'description': 'Returns the edge multiplier of the specified time set.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'pins',
                'documentation': {
                    'description': 'Name of the specified pin.\n'
                },
                'name': 'pin',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'timeSetName',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returned edge multiplier of the time set for the specified pin.\n'
                },
                'name': 'edgeMultiplier',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetTimeSetName': {
        'codegen_method': 'private',
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
                'name': 'timeSetIndex',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'nameBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'name',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'nameBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'render_in_session_base': True,  # Called from FancyFetchHistoryRAMCycleInformation() which uses rep cap
        'returns': 'ViStatus'
    },
    'GetTimeSetPeriod': {
        'documentation': {
            'description': 'Returns the period of the specified time set.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified digital pattern instrument handle\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'timeSetName',
                'documentation': {
                    'description': 'The specified time set name.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returned period, in seconds, that the edge is configured to.\n'
                },
                'name': 'period',
                'python_api_converter_name': 'convert_seconds_real64_to_timedelta',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitWithOptions': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Creates and returns a new session to the specified digital pattern instrument to use in all subsequent function calls. To place the instrument in a known startup state when creating a new session, set the reset parameter to VI_TRUE, which is equivalent to calling the niDigital_reset function immediately after initializing the session.\n'
        },
        'method_name_for_documentation': '__init__',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified resource name shown in Measurement & Automation Explorer (MAX) for a digital pattern instrument, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. **resourceName** can also be a logical IVI name. This parameter accepts a comma-delimited list of strings in the form PXI1Slot2,PXI1Slot3, where ``PXI1Slot2`` is one instrument resource name and ``PXI1Slot3`` is another. When including more than one digital pattern instrument in the comma-delimited list of strings, list the instruments in the same order they appear in the pin map.\n\n+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n| |Note| | Note\xa0\xa0 You only can specify multiple instruments of the same model. For example, you can list two PXIe-6570s but not a PXIe-6570 and PXIe-6571. The instruments must be in the same chassis. |\n+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n\n.. |Note| image:: note.gif\n',
                    'note': '\n'
                },
                'name': 'resourceName',
                'type': 'ViConstString'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that verifies that the digital pattern instrument you initialize is supported by NI-Digital. NI-Digital automatically performs this query, so setting this parameter is not necessary.\n'
                },
                'name': 'idQuery',
                'type': 'ViBoolean',
                'use_in_python_api': False
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that specifies whether to reset a digital pattern instrument to a known state when the session is initialized. Setting the **resetDevice** value to VI_TRUE is equivalent to calling the niDigital_reset function immediately after initializing the session.\n'
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': 'The initial values of certain properties for the NI-Digital Pattern Driver session. The string can be empty. You can use the DriverSetup flag to simulate a digital pattern instrument. When simulating a digital pattern instrument, you must specify the model you want to simulate. For example, Simulate = 1, DriverSetup = Model:6570.\n'
                },
                'name': 'optionString',
                'python_api_converter_name': 'convert_init_with_options_dictionary',
                'type': 'ViConstString',
                'type_in_documentation': 'dict'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned instrument session.\n'
                },
                'name': 'newVi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'Initiate': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Starts bursting the pattern configured by NIDIGITAL_ATTR_START_LABEL, causing the NI-Digital session to be committed. To stop the pattern burst, call niDigital_Abort. If keep alive pattern is bursting when niDigital_Abort is called or upon exiting the context manager, keep alive pattern will not be stopped. To stop the keep alive pattern, call niDigital_AbortKeepAlive.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsDone': {
        'documentation': {
            'description': 'Checks the hardware to determine if the pattern burst has completed or if any errors have occurred.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'A Boolean that indicates whether the pattern burst completed.\n'
                },
                'name': 'done',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsSiteEnabled': {
        'documentation': {
            'description': 'Checks if a specified site is enabled.\n',
            'note': 'The function returns an error if more than one site is specified.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'documentation': {
                    'description': 'Site specified as a string in the form of ``siteN``, where ``N`` is the site number. The function returns an error if more than one site is specified.\n'
                },
                'name': 'site',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Boolean value that returns whether the site is enabled or disabled.\n'
                },
                'name': 'enable',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'LoadLevels': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Loads a levels sheet from a specified file.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'documentation': {
                    'description': 'Absolute file path to the specified levels sheet file.\n'
                },
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'LoadPattern': {
        'documentation': {
            'description': 'Loads the specified pattern file.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Absolute file path of the binary .digipat pattern file to load. Specify the pattern to burst using NIDIGITAL_ATTR_START_LABEL or the start_label parameter of the niDigital_FancyBurstPattern function.\n'
                },
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'LoadPinMap': {
        'documentation': {
            'description': 'Loads a pin map file. You can load only a single pin and channel map file during an NI-Digital Pattern Driver session. To switch pin maps, create a new session or call the niDigital_reset function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'documentation': {
                    'description': 'Absolute file path to a pin map file created with the Digital Pattern Editor or the NI TestStand Semiconductor Module.\n'
                },
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'LoadSpecifications': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Loads a specifications sheet from a specified file.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'documentation': {
                    'description': 'Absolute file path to a specifications file.\n'
                },
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'LoadTiming': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Loads a timing sheet from a specified file.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'documentation': {
                    'description': 'Absolute file path to the specified timing sheet file.\n'
                },
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'documentation': {
            'description': 'Obtains the multithreaded lock on the instrument session. Before doing so, the function waits until all other execution threads have released the lock on the instrument session. Other threads might have obtained the lock on this session in the following ways: niDigital_LockSession After the call to niDigital_LockSession returns successfully, no other threads can access the instrument session until you call niDigital_UnlockSession. Use niDigital_LockSession and niDigital_UnlockSession around a sequence of calls to instrument driver functions if you require exclusive access through the end of the sequence. You can safely make nested calls to niDigital_LockSession within the same thread. To completely unlock the session, you must balance each call to niDigital_LockSession with a call to niDigital_UnlockSession. If, however, you use the **callerHasLock** parameter in all calls to niDigital_LockSession and niDigital_UnlockSession within a function, the IVI Library locks the session only once within the function, regardless of the number of calls you make to niDigital_LockSession. This functionality allows you to call niDigital_UnlockSession just once at the end of the function.\n'
        },
        'method_templates': [
            {
                'documentation_filename': 'lock',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'lock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'This parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL. You can use this parameter in complex functions to track lock status and the need to unlock the session. Pass the address of a local ViBoolean variable in the declaration of the local variable and initialize it to VI_FALSE. Also, pass the address of the same local variable to any other calls you make to niDigital_LockSession or niDigital_UnlockSession in the same function.\n'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'lock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'PPMU_Measure': {
        'documentation': {
            'description': 'Instructs the PPMU to measure voltage or current. This function can be called to take a voltage measurement even if the pin function is not set to PPMU.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Parameter that specifies whether the PPMU measures voltage or current from the DUT.\n\n-   NIDIGITAL_VAL_MEASURE_CURRENT: The PPMU measures current from the DUT.\n-   NIDIGITAL_VAL_MEASURE_VOLTAGE: The PPMU measures voltage from the DUT.\n'
                },
                'enum': 'PPMUMeasurementType',
                'name': 'measurementType',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViReal64 array you specify for measurements. To determine the size of the buffer to allocate for the measurements array, pass a value of 0 to the **bufferSize** parameter and a value of VI_NULL to the **measurements** parameter. In this case, the value returned by the **actualNumRead** parameter is the size of the array necessary to hold the measurements.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned array of measurements in the order you specify in the repeated capabilities. If a site is disabled, the function does not return data for that site. You can also use the niDigital_FancyGetPinResultsPinInformation function to obtain a sorted list of returned sites and channels.\n'
                },
                'name': 'measurements',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualNumRead'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of measurements written to the measurements array.\n'
                },
                'name': 'actualNumRead',
                'type': 'ViInt32'
            }
        ],
        'python_name': 'ppmu_measure',
        'returns': 'ViStatus'
    },
    'PPMU_Source': {
        'documentation': {
            'description': 'Starts sourcing voltage or current from the PPMU. This function automatically selects the PPMU function. Changes to PPMU source settings do not take effect until you call this function. If you modify source settings after you call this function, you must call this function again for changes in the configuration to take effect.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            }
        ],
        'python_name': 'ppmu_source',
        'returns': 'ViStatus'
    },
    'ReadSequencerFlag': {
        'documentation': {
            'description': 'Reads the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The pattern sequencer flag you want to read.\n\n-   NIDIGITAL_VAL_SEQUENCER_FLAG0 ("seqflag0"): Reads pattern sequencer flag 0.\n-   NIDIGITAL_VAL_SEQUENCER_FLAG1 ("seqflag1"): Reads pattern sequencer flag 1.\n-   NIDIGITAL_VAL_SEQUENCER_FLAG2 ("seqflag2"): Reads pattern sequencer flag 2.\n-   NIDIGITAL_VAL_SEQUENCER_FLAG3 ("seqflag3"): Reads pattern sequencer flag 3.\n'
                },
                'enum': 'SequencerFlag',
                'name': 'flag',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'A Boolean that indicates the state of the pattern sequencer flag you specify.\n'
                },
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadSequencerRegister': {
        'documentation': {
            'description': 'Reads the value of a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program. For example, you can use this function to read a register modified by the write_reg opcode during a pattern burst.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The sequencer register to read from.\n\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER0 ("reg0"): Reads sequencer register 0.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER1 ("reg1"): Reads sequencer register 1.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER2 ("reg2"): Reads sequencer register 2.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER3 ("reg3"): Reads sequencer register 3.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER4 ("reg4"): Reads sequencer register 4.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER5 ("reg5"): Reads sequencer register 5.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER6 ("reg6"): Reads sequencer register 6.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER7 ("reg7"): Reads sequencer register 7.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER8 ("reg8"): Reads sequencer register 8.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER9 ("reg9"): Reads sequencer register 9.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER10 ("reg10"): Reads sequencer register 10.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER11 ("reg11"): Reads sequencer register 11.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER12 ("reg12"): Reads sequencer register 12.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER13 ("reg13"): Reads sequencer register 13.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER14 ("reg14"): Reads sequencer register 14.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER15 ("reg15"): Reads sequencer register 15.\n'
                },
                'enum': 'SequencerRegister',
                'name': 'reg',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Value read from the sequencer register.\n'
                },
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadStatic': {
        'documentation': {
            'description': 'Reads the current state of comparators for pins you specify in the repeated capabilities. If there are uncommitted changes to levels or the termination mode, this function commits the changes to the pins.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViUInt8 array you specify for data. To determine the size of the buffer to allocate for the data array, pass a value of 0 to the **bufferSize** parameter and a value of VI_NULL to the **data** parameter. In this case, the value returned by the **actualNumRead** parameter is the size of the array necessary to hold the data.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned array of pin states read from the channels in the repeated capabilities. Data is returned in the order you specify in the repeated capabilities. If a site is disabled, the function does not return data for that site. You can also use the niDigital_FancyGetPinResultsPinInformation function to obtain a sorted list of returned sites and channels.\n\n-   NIDIGITAL_VAL_L: The comparators read a logic low pin state.\n-   NIDIGITAL_VAL_H: The comparators read a logic high pin state.\n-   NIDIGITAL_VAL_M: The comparators read a midband pin state.\n-   NIDIGITAL_VAL_V: The comparators read a value that is above VOH and below VOL, which can occur when you set VOL higher than VOH.\n'
                },
                'enum': 'PinState',
                'name': 'data',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'bufferSize',
                    'value_twist': 'actualNumRead'
                },
                'type': 'ViUInt8[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The number of values written to the data array.\n'
                },
                'name': 'actualNumRead',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetAttribute': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Resets the attribute to its default value.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetDevice': {
        'documentation': {
            'description': 'Returns a digital pattern instrument to a known state. This function performs the following actions:\n\n- Aborts pattern execution.\n- Clears pin maps, time sets, source and capture waveforms, and patterns.\n- Resets all properties to default values, including the NIDIGITAL_ATTR_SELECTED_FUNCTION property that is set to NIDIGITAL_VAL_DISCONNECT, causing the I/O switches to open.\n- Stops export of all external signals and events.\n- Clears over-temperature and over-power conditions.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfCalibrate': {
        'documentation': {
            'description': 'Performs self-calibration on a digital pattern instrument.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareEdgeTrigger': {
        'documentation': {
            'description': 'Forces a particular edge-based trigger to occur regardless of how the specified trigger is configured. You can use this function as a software override.\n'
        },
        'parameters': [
            {
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Trigger specifies the trigger you want to override.',
                    'table_body': [
                        [
                            'NIDIGITAL_VAL_START_TRIGGER',
                            'Overrides the Start trigger. You must specify an empty string in the trigger_identifier parameter.'
                        ],
                        [
                            'NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER',
                            'Specifies to route a conditional jump trigger. You must specify a conditional jump trigger in the trigger_identifier parameter.'
                        ],
                    ],
                    'table_header': [
                        'Defined Values',
                    ],
                },
                'enum': 'SoftwareTrigger',
                'name': 'trigger',
                'type': 'ViInt32'
            },
            {
                'documentation': {
                    'description': """Trigger Identifier specifies the instance of the trigger you want to override.
If trigger is specified as NIDIGITAL_VAL_START_TRIGGER, this parameter must be an empty string. If trigger is
specified as NIDIGITAL_VAL_CONDITIONAL_JUMP_TRIGGER, allowed values are conditionalJumpTrigger0,
conditionalJumpTrigger1, conditionalJumpTrigger2, and conditionalJumpTrigger3.
"""
                },
                'direction': 'in',
                'name': 'triggerIdentifier',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Sets the value of a ViBoolean attribute. Use this function to set the values of digital pattern instrument-specific attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The value to which you want to set the attribute; some of the values might not be valid depending on the current settings of the instrument session.\n'
                },
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Sets the value of a ViInt32 attribute. Use this function to set the values of digital pattern instrument-specific attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The value to which you want to set the attribute; some of the values might not be valid depending on the current settings of the instrument session.\n'
                },
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Sets the value of a ViInt64 attribute. Use this function to set the values of digital pattern instrument-specific attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The value to which you want to set the attribute; some of the values might not be valid depending on the current settings of the instrument session.\n'
                },
                'name': 'value',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Sets the value of a ViIntReal64 attribute. Use this function to set the values of digital pattern instrument-specific attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The value to which you want to set the attribute; some of the values might not be valid depending on the current settings of the instrument session.\n'
                },
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Sets the value of a ViString attribute. Use this function to set the values of digital pattern instrument-specific attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The ID of an attribute.\n'
                },
                'name': 'attribute',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The value to which you want to set the attribute; some of the values might not be valid depending on the current settings of the instrument session.\n'
                },
                'name': 'value',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'TDR': {
        'documentation': {
            'description': 'Measures propagation delays through cables, connectors, and load boards using Time-Domain Reflectometry (TDR). Ensure that the channels and pins you select are connected to an open circuit.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that specifies whether to apply the measured TDR offsets. If you need to adjust the measured offsets prior to applying, set this input to VI_FALSE, and call the niDigital_ApplyTDROffsets function to specify the adjusted TDR offsets values.\n'
                },
                'name': 'applyOffsets',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The number of elements in the ViReal64 array you specify for offsets. To determine the size of the buffer to allocate for the offsets array, pass a value of 0 to the **offsetsBufferSize** parameter and a value of VI_NULL to the **offsets** parameter. In this case, the value returned by the **actualNumOffsets** parameter is the size of the array necessary to hold the TDR offsets.\n'
                },
                'name': 'offsetsBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Measured TDR offsets specified in seconds.\n'
                },
                'name': 'offsets',
                'python_api_converter_name': 'convert_seconds_real64_to_timedeltas',
                'size': {
                    'mechanism': 'ivi-dance-with-a-twist',
                    'value': 'offsetsBufferSize',
                    'value_twist': 'actualNumOffsets'
                },
                'type': 'ViReal64[]',
                'type_in_documentation': 'list of hightime.timedelta'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Number of offsets written to the offsets array.\n'
                },
                'name': 'actualNumOffsets',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnloadAllPatterns': {
        'documentation': {
            'description': 'Unloads all patterns, source waveforms, and capture waveforms from a digital pattern instrument.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that specifies whether to keep or unload the keep alive pattern.\n'
                },
                'name': 'unloadKeepAlivePattern',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnloadSpecifications': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Unloads the given specifications sheet present in the previously loaded specifications file that you select. You must call the niDigital_LoadSpecifications function to reload the file with updated specifications values. You must then call the niDigital_ApplyLevelsAndTiming function in order to apply the levels and timing values that reference the updated specifications values.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'documentation': {
                    'description': 'Absolute file path to a loaded specifications file.\n'
                },
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'documentation': {
            'description': 'Releases a lock that you acquired on an instrument session using the niDigital_LockSession function.\n'
        },
        'method_templates': [
            {
                'documentation_filename': 'unlock',
                'library_interpreter_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'unlock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'This parameter serves as a convenience. If you do not want to use this parameter, pass VI_NULL. You can use this parameter in complex functions to track lock status and the need to unlock the session. Pass the address of a local ViBoolean variable in the declaration of the local variable and initialize it to VI_FALSE. Also, pass the address of the same local variable to any other calls you make to niDigital_LockSession or niDigital_UnlockSession in the same function.\n'
                },
                'name': 'callerHasLock',
                'type': 'ViBoolean'
            }
        ],
        'python_name': 'unlock',
        'render_in_session_base': True,
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'WaitUntilDone': {
        'documentation': {
            'description': 'Waits until the pattern burst has completed or the timeout has expired.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'hightime.timedelta(seconds=10.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'Maximum time (in seconds) allowed for this function to complete. If this function does not complete within this time interval, this function returns an error.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'hightime.timedelta, datetime.timedelta, or float in seconds'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteSequencerFlag': {
        'documentation': {
            'description': 'Writes the state of a pattern sequencer flag. Use pattern sequencer flags to coordinate execution between the pattern sequencer and a runtime test program.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The pattern sequencer flag to write.\n\n-   NIDIGITAL_VAL_SEQUENCER_FLAG0 ("seqflag0"): Writes pattern sequencer flag 0.\n-   NIDIGITAL_VAL_SEQUENCER_FLAG1 ("seqflag1"): Writes pattern sequencer flag 1.\n-   NIDIGITAL_VAL_SEQUENCER_FLAG2 ("seqflag2"): Writes pattern sequencer flag 2.\n-   NIDIGITAL_VAL_SEQUENCER_FLAG3 ("seqflag3"): Writes pattern sequencer flag 3.\n'
                },
                'enum': 'SequencerFlag',
                'name': 'flag',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'A Boolean that assigns a state to the pattern sequencer flag you specify.\n'
                },
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteSequencerRegister': {
        'documentation': {
            'description': 'Writes a value to a pattern sequencer register. Use pattern sequencer registers to pass numeric values between the pattern sequencer and a runtime test program.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The sequencer register you want to write to.\n\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER0 ("reg0"): Writes sequencer register 0.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER1 ("reg1"): Writes sequencer register 1.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER2 ("reg2"): Writes sequencer register 2.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER3 ("reg3"): Writes sequencer register 3.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER4 ("reg4"): Writes sequencer register 4.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER5 ("reg5"): Writes sequencer register 5.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER6 ("reg6"): Writes sequencer register 6.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER7 ("reg7"): Writes sequencer register 7.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER8 ("reg8"): Writes sequencer register 8.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER9 ("reg9"): Writes sequencer register 9.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER10 ("reg10"): Writes sequencer register 10.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER11 ("reg11"): Writes sequencer register 11.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER12 ("reg12"): Writes sequencer register 12.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER13 ("reg13"): Writes sequencer register 13.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER14 ("reg14"): Writes sequencer register 14.\n-   NIDIGITAL_VAL_SEQUENCER_REGISTER15 ("reg15"): Writes sequencer register 15.\n'
                },
                'enum': 'SequencerRegister',
                'name': 'reg',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The value you want to write to the register.\n'
                },
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteSourceWaveformBroadcastU32': {
        'documentation': {
            'description': 'Writes the same waveform data to all sites. Use this write function if you set the data_mapping parameter of the create source waveform function to NIDIGITAL_VAL_BROADCAST.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Size of the data array.\n'
                },
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '1D array of samples to use as source data to apply to all sites.\n'
                },
                'name': 'waveformData',
                'size': {
                    'mechanism': 'len',
                    'value': 'waveformSize'
                },
                'type': 'ViUInt32[]'
            }
        ],
        'python_name': 'write_source_waveform_broadcast',
        'returns': 'ViStatus'
    },
    'WriteSourceWaveformDataFromFileTDMS': {
        'documentation': {
            'description': 'Writes a source waveform based on the waveform data and configuration information the file contains.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Absolute file path to the load source waveform file (.tdms).\n'
                },
                'name': 'waveformFilePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteSourceWaveformSiteUniqueU32': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Writes one waveform per site. Use this write function if you set the parameter of the create source waveform function to Site Unique.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'is_repeated_capability': True,
                'repeated_capability_type': 'sites',
                'documentation': {
                    'description': 'Site numbers listed as a comma-delimited list of strings of form site\\ ``N``, where ``N`` is the site number.\n'
                },
                'name': 'siteList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The name to assign to the waveform. Use the waveform_name  with source_start opcode in your pattern.\n'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of waveforms.\n'
                },
                'name': 'numWaveforms',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Number of samples per waveform.\n'
                },
                'name': 'samplesPerWaveform',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'An array of samples to use as source data. Data for each site must be appended sequentially in the array (non-interleaved).\n'
                },
                'name': 'waveformData',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'type': 'ViUInt32[]',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteStatic': {
        'documentation': {
            'description': 'Writes a static state to the specified pins. The selected pins remain in the specified state until the next pattern burst or call to this function. If there are uncommitted changes to levels or the termination mode, this function commits the changes to the pins. This function does not change the selected pin function. If you write a static state to a pin that does not have the Digital function selected, the new static state is stored by the instrument, and affects the state of the pin the next time you change the selected function to Digital.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'List of channel names or list of pins. Do not pass a mix of channel names and pin names. An empty string denotes all digital pattern instrument channels.\n\nPin names and pin groups apply to all enabled sites, unless the pin name explicitly specifies the site. You can specify a pin in a specific site using the form site\\ ``N``/pinName\\ ````, where ``N`` is the site number. This function ignores pins that are not mapped to the digital pattern instrument.\n\nSpecify channel names using the form ``PXI1Slot3``/``0``,\\ ``2-3`` or ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``, where ``PXI1Slot3`` is the instrument resource name and ``0``, ``2``, ``3`` are channel names. To specify channels from multiple instruments, use the form ``PXI1Slot3``/``0``,\\ ``PXI1Slot3``/``2-3``,\\ ``PXI1Slot4``/``2-3``. The instruments must be in the same chassis.\n'
                },
                'name': 'channelList',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Parameter that specifies one of the following digital states to assign to the pin.\n\n-   NIDIGITAL_VAL_0: Specifies to drive low.\n-   NIDIGITAL_VAL_1: Specifies to drive high.\n-   NIDIGITAL_VAL_X: Specifies to not drive.\n'
                },
                'enum': 'WriteStaticPinState',
                'name': 'state',
                'type': 'ViUInt8'
            }
        ],
        'returns': 'ViStatus'
    },
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Closes the specified instrument session to a digital pattern instrument, aborts pattern execution, and unloads pattern memory. The channels on a digital pattern instrument remain in their current state.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': '_close',
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'error_message': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Takes the error code returned by the digital pattern instrument driver functions, interprets it, and returns it as a user readable string.\n'
        },
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns. You may also specify VI_NULL as the instrument session to retrieve the error message even when the niDigital_init function or the niDigital_InitWithOptions function fails.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified error code.\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The error information formatted as a string. The array must contain at least 256 characters.\n'
                },
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'reset': {
        'documentation': {
            'description': 'Returns a digital pattern instrument to a known state. This function performs the following actions:\n\n- Aborts pattern execution.\n- Clears pin maps, time sets, source and capture waveforms, and patterns.\n- Resets all properties to default values, including the NIDIGITAL_ATTR_SELECTED_FUNCTION property that is set to NIDIGITAL_VAL_DISCONNECT, causing the I/O switches to open.\n- Stops exporting all external signals and events.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'self_test': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns self test results from a digital pattern instrument. This test requires several minutes to execute.\n'
        },
        'method_name_for_documentation': 'self_test',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The specified instrument session the niDigital_init or niDigital_InitWithOptions function returns.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'A parameter that indicates if the self test passed (0) or failed (!=0).\n'
                },
                'name': 'testResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The returned self test status message. The array must contain at least 256 characters.\n'
                },
                'name': 'testMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 2048
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    }
}
