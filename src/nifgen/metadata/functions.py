# -*- coding: utf-8 -*-
# This file is generated from API metadata for NI-FGEN version 19.1.0d0
functions = {
    'AbortGeneration': {
        'documentation': {
            'description': '\nAborts any previously initiated signal generation. Call the\nnifgen_InitiateGeneration function to cause the signal generator to\nproduce a signal again.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'abort',
        'returns': 'ViStatus'
    },
    'AdjustSampleClockRelativeDelay': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nDelays (or phase shifts) the Sample Clock, which delays the generated\nsignal. Delaying the Sample Clock can be useful when synchronizing the\noutput of multiple modules or when intentionally phase shifting the\noutput relative to a fixed reference, such as the PLL Reference Clock.\n\nAdjustment time can be positive or negative, but it must be less than or\nequal to the Sample Clock period. The delay takes effect immediately\nafter this function is called. To delay an external Sample Clock, use\nthe NIFGEN_ATTR_SAMPLE_CLOCK_ABSOLUTE_DELAY attribute.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the amount of time to adjust the Sample Clock delay.\n\n**Units**: Seconds\n\n**Default Value**: 0\n'
                },
                'name': 'adjustmentTime',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'AllocateNamedWaveform': {
        'documentation': {
            'description': '\nSpecifies the size of a named waveform up front so that it can be\nallocated in onboard memory before loading the associated data. Data can\nthen be loaded in smaller blocks with the niFgen Write (Binary16)\nWaveform functions.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to allocate the named\nwaveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name to associate with the allocated waveform.'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size of the waveform to allocate in samples.\n\n**Default Value**: "4096"\n'
                },
                'name': 'waveformSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'AllocateServer': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'serverName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'AllocateWaveform': {
        'documentation': {
            'description': '\nSpecifies the size of a waveform so that it can be allocated in onboard\nmemory before loading the associated data. Data can then be loaded in\nsmaller blocks with the Write Binary 16 Waveform functions.\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to allocate the waveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies, in samples, the size of the waveform to allocate.'
                },
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe handle that identifies the new waveform. This handle is used later\nwhen referring to this waveform.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'AttributeWasSetByUser': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'repCapName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            }
        ],
        'returns': 'ViBoolean'
    },
    'CalAdjustAdc': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCalculates calibration constants pertaining to the gain and offset of\nthe onboard calibration ADC. During external calibration, you can\ngenerate voltages and measure them both externally and with the\ncalibration ADC. Pass the measured voltages to this function to allow\nNI-FGEN to calculate the appropriate calibration constants and store\nthem in the onboard EEPROM when the calibration session is committed.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel being calibrated.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the main path configuration.'
                },
                'name': 'configuration',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of analog output voltages measured with an external\ninstrument.\n'
                },
                'name': 'voltagesMeasuredExternally',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of analog output voltages measured with the onboard\ncalibration ADC.\n'
                },
                'name': 'voltagesMeasuredWithCaladc',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustCalAdc': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCalculates calibration constants pertaining to the gain and offset of\nthe onboard calibration ADC. During external calibration, you can\ngenerate voltages and measure them both externally and with the\ncalibration ADC. Pass the measured voltages to this function to allow\nNI-FGEN to calculate the appropriate calibration constants and store\nthem in the onboard EEPROM when the calibration session is committed.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_InitExtCal function and identifies a particular instrument\nsession.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of analog output voltages measured with an external\ninstrument.\n'
                },
                'name': 'voltagesMeasuredExternally',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of analog output voltages measured with the onboard\ncalibration ADC.\n'
                },
                'name': 'voltagesMeasuredWithCaladc',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustDirectPathGain': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCalculates calibration constants pertaining to the gain of the direct\nanalog path. During external calibration, you can put the device in\ndifferent configurations; program different gain and main DAC values;\nand take measurements of the resulting output voltage. Pass the\nconfiguration data, as well as the measurements, to this function to\nallow NI-FGEN to calculate the appropriate calibration constants and\nstore them in the onboard EEPROM when the calibration session is\ncommitted.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_InitExtCal function and identifies a particular instrument\nsession.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel being calibrated.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the values programmed to the main output DAC\nduring this calibration stage.\n'
                },
                'name': 'mainDacValues',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the values programmed to the gain calibration DAC\nduring this calibration stage.\n'
                },
                'name': 'gainDacValues',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the analog output voltages measured during this\ncalibration stage.\n'
                },
                'name': 'measuredOutputs',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustDirectPathOutputImpedance': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCalculates calibration constants pertaining to direct analog path output\nimpedance. During external calibration, you can put the device in\ndifferent configurations and take measurements of the resulting output\nvoltage across different loads. Pass the configuration data, as well as\nthe measurements, to this function to allow NI-FGEN to calculate the\nappropriate calibration constants and store them in the onboard EEPROM\nwhen the calibration session is committed.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_InitExtCal function and identifies a particular instrument\nsession.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel being calibrated.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the direct path output impedance configuration. Refer to the\nnifgen_Related_Documentation for your device for information on what\nconfigurations must be calibrated.\n'
                },
                'name': 'configuration',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the impedance of the load across which the measurement passed\nin as **measuredVoltageAcrossLoad** is taken.\n'
                },
                'name': 'loadImpedance',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the analog output voltage measured across a very\nhigh-impedance load.\n'
                },
                'name': 'measuredSourceVoltage',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the analog output voltage measured across the load impedance\nspecified in the **loadImpedance** parameter.\n'
                },
                'name': 'measuredVoltageAcrossLoad',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustFlatness': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nDuring external calibration, the device is configured with the different\nanalog settings. Measurements are taken of the resulting output voltage\nacross different frequencies. The configuration data, as well as the\nmeasurements, are passed to this function so that NI-FGEN can calculate\nthe appropriate calibration constants and, when the calibration session\nis committed, store them in the onboard EEPROM.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_InitExtCal function and identifies a particular instrument\nsession.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel being calibrated.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the analog path configuration of the device for this stage of\ncalibration. Refer to the nifgen_Related_Documentation for your device\nfor information on which configurations must be calibrated.\n'
                },
                'name': 'configuration',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the amplitude, in volts, that was used to configure NI-FGEN to\ngenerate the sine tones at different frequencies.\n'
                },
                'name': 'requestedAmplitude',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the frequencies of the output waveform in hertz.'
                },
                'name': 'frequencies',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the actual (measured) amplitudes of the output waveform in\nvolts.\n'
                },
                'name': 'measuredAmplitudes',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of measurements to take.'
                },
                'name': 'numberOfMeasurements',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustMainPathOutputImpedance': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCalculates calibration constants pertaining to main analog path output\nimpedance. During external calibration, you can put the device in\ndifferent configurations and take measurements of the resulting output\nvoltage across different loads. Pass the configuration data, as well as\nthe measurements, to this function to allow NI-FGEN to calculate the\nappropriate calibration constants and store them in the onboard EEPROM\nwhen the calibration session is committed.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_InitExtCal function and identifies a particular instrument\nsession.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel being calibrated.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the main path output impedance configuration. Refer to the\nnifgen_Related_Documentation for your device for information on what\nconfigurations must be calibrated.\n'
                },
                'name': 'configuration',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the impedance of the load across which the measurement passed\nin as **measuredVoltageAcrossLoad** is taken.\n'
                },
                'name': 'loadImpedance',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the analog output voltage measured across a very\nhigh-impedance load.\n'
                },
                'name': 'measuredSourceVoltage',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the analog output voltage measured across the load impedance\nspecified in the **loadImpedance** parameter.\n'
                },
                'name': 'measuredVoltageAcrossLoad',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustMainPathPostAmpGainAndOffset': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCalculates calibration constants pertaining to the postamplifier gain\nand offset of the main analog path. During external calibration, you can\nput the device in different configurations; program different gain,\noffset, and main DAC values; and take measurements of the resulting\noutput voltage. Pass the configuration data, as well as the measurements\nto this function to allow NI-FGEN to calculate the appropriate\ncalibration constants and store them in the onboard EEPROM when the\ncalibration session is committed.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_InitExtCal function and identifies a particular instrument\nsession.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel being calibrated.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the postamplifier stage configuration. Refer to the\nnifgen_Related_Documentation for your device for information on what\nconfigurations must be calibrated.\n'
                },
                'name': 'configuration',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the values programmed to the main output DAC\nduring this calibration stage.\n'
                },
                'name': 'mainDacValues',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the values programmed to the gain calibration DAC\nduring this calibration stage.\n'
                },
                'name': 'gainDacValues',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the values programmed to the offset calibration\nDAC during this calibration stage.\n'
                },
                'name': 'offsetDacValues',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the analog output voltages measured during this\ncalibration stage.\n'
                },
                'name': 'measuredOutputs',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustMainPathPreAmpGain': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCalculates calibration constants pertaining to the preamplifier gain of\nthe main analog path. During external calibration, you can put the\ndevice in different configurations; program different gain, offset, and\nmain DAC values; and take measurements of the resulting output voltage.\nPass the configuration data, as well as the measurements to this\nfunction to allow NI-FGEN to calculate the appropriate calibration\nconstants and store them in the onboard EEPROM when the calibration\nsession is committed.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_InitExtCal function and identifies a particular instrument\nsession.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel being calibrated.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the preamplifier stage configuration. Refer to the\nnifgen_Related_Documentation for your device for information on what\nconfigurations must be calibrated.\n'
                },
                'name': 'configuration',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the values programmed to the main output DAC\nduring this calibration stage.\n'
                },
                'name': 'mainDacValues',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the values programmed to the gain calibration DAC\nduring this calibration stage.\n'
                },
                'name': 'gainDacValues',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the values programmed to the offset calibration\nDAC during this calibration stage.\n'
                },
                'name': 'offsetDacValues',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the analog output voltages measured during this\ncalibration stage.\n'
                },
                'name': 'measuredOutputs',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustMainPathPreAmpOffset': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCalculates calibration constants pertaining to the preamplifier offset\nof the main analog path. During external calibration, you can put the\ndevice in different configurations; program different gain, offset, and\nmain DAC values; and take measurements of the resulting output voltage.\nPass the configuration data, as well as the measurements, to this\nfunction to allow NI-FGEN to calculate the appropriate calibration\nconstants and store them in the onboard EEPROM when the calibration\nsession is committed.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_InitExtCal function and identifies a particular instrument\nsession.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel being calibrated.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the preamplifier stage configuration. Refer to the\nnifgen_Related_Documentation for your device for information about\nwhat configurations must be calibrated.\n'
                },
                'name': 'configuration',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the values programmed to the gain calibration DAC\nduring this calibration stage.\n'
                },
                'name': 'gainDacValues',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the values programmed to the offset calibration\nDAC during this calibration stage.\n'
                },
                'name': 'offsetDacValues',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the analog output voltages measured during this\ncalibration stage.\n'
                },
                'name': 'measuredOutputs',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustOscillatorFrequency': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCalculates calibration constants pertaining to the VCXO. During external\ncalibration, you can generate sine waves and take measurements of the\nresulting output frequency. Pass the desired and measured frequencies to\nthis function to allow NI-FGEN to calculate the appropriate calibration\nconstants and store them in the onboard EEPROM when the calibration\nsession is committed.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_InitExtCal function and identifies a particular instrument\nsession.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the expected frequency of the output waveform.'
                },
                'name': 'desiredFrequency',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the actual measured frequency of the output waveform.'
                },
                'name': 'measuredFrequency',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ChangeExtCalPassword': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nChanges the password that is required to initialize an external\ncalibration session. The password may be up to four characters long.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_init or the nifgen_InitExtCal function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the old (current) external calibration password.'
                },
                'name': 'oldPassword',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the new (desired) external calibration password. The password\nmay be up to four characters long.\n'
                },
                'name': 'newPassword',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViBoolean': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Checks the validity of a value you specify for a ViBoolean attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or an empty string ("").\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. **Default\nValue**: None\n',
                    'note': '\nSome of the values might not be valid depending on the current\nsettings of the instrument session.\n'
                },
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViInt32': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Checks the validity of a value you specify for a ViInt32 attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or an empty string ("").\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. **Default\nValue**: None\n',
                    'note': '\nSome of the values might not be valid depending on the current\nsettings of the instrument session.\n'
                },
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViInt64': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Checks the validity of a value you specify for a ViInt64 attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or an empty string ("").\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. **Default\nValue**: None\n',
                    'note': '\nSome of the values might not be valid depending on the current\nsettings of the instrument session.\n'
                },
                'name': 'attributeValue',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViReal64': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Checks the validity of a value you specify for a ViReal64 attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or an empty string ("").\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. **Default\nValue**: None\n',
                    'note': '\nSome of the values might not be valid depending on the current\nsettings of the instrument session.\n'
                },
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViSession': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Checks the validity of a value you specify for a ViSession attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or an empty string ("").\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. **Default\nValue**: None\n',
                    'note': '\nSome of the values might not be valid depending on the current\nsettings of the instrument session.\n'
                },
                'name': 'attributeValue',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViString': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Checks the validity of a value you specify for a ViString attribute.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or an empty string ("").\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value which you want to verify as a valid value for the\nattribute.\n\n**Default Value**: None\n',
                    'note': '\nSome of the values might not be valid depending on the current\nsettings of the instrument session.\n'
                },
                'name': 'attributeValue',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckWfmNameSize': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'wfmName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearArbMemory': {
        'documentation': {
            'description': '\nRemoves all previously created arbitrary waveforms, sequences, and\nscripts from the signal generator memory and invalidates all waveform\nhandles, sequence handles, and waveform names.\n',
            'note': '\nThe signal generator must not be in the Generating state when you\ncall this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearArbSequence': {
        'documentation': {
            'description': '\nRemoves a previously created arbitrary sequence from the signal\ngenerator memory and invalidates the sequence handle.\n',
            'note': '\nThe signal generator must not be in the Generating state when you\ncall this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the arbitrary sequence that you want the signal\ngenerator to remove. You can create an arbitrary sequence using the\nnifgen_CreateArbSequence or nifgen_CreateAdvancedArbSequence function.\nThese functions return a handle that you use to identify the sequence.\n\n| **Defined Value**:\n| NIFGEN_VAL_ALL_SEQUENCES—Remove all sequences from the signal\n  generator\n\n**Default Value**: None\n'
                },
                'name': 'sequenceHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearArbWaveform': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nRemoves a previously created arbitrary waveform from the signal\ngenerator memory and invalidates the waveform handle.\n',
            'note': '\nThe signal generator must not be in the Generating state when you\ncall this function.\n'
        },
        'method_name_for_documentation': 'delete_waveform',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the arbitrary waveform that you want the signal\ngenerator to remove.\n\nYou can create multiple arbitrary waveforms using one of the following\nniFgen Create Waveform functions:\n\n-  niFgen_CreateWaveformF64\n-  niFgen_CreateWaveformI16\n-  niFgen_CreateWaveformFromFileI16\n-  niFgen_CreateWaveformFromFileF64\n-  niFgen_CreateWaveformFromFileHWS\n\n**Defined Value**:\n\nNIFGEN_VAL_ALL_WAVEFORMS—Remove all waveforms from the signal\ngenerator.\n\n**Default Value**: None\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearError': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nClears the error information for the current execution thread and the\nIVI session you specify. If you pass VI_NULL for the **vi** parameter,\nthis function clears the error information only for the current\nexecution thread.\n\nThis function sets the error code to VI_SUCCESS (0), and sets the error\ndescription string to "" (empty string).\n\nThe IVI Engine also maintains this error information separately for each\nthread. This feature is useful if you do not have a session handle to\npass to the nifgen_ClearError or the nifgen_GetError function. This\nsituation occurs when a call to the nifgen_init or\nnifgen_InitWithOptions function fails.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearErrorInfo': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearFreqList': {
        'documentation': {
            'description': '\nRemoves a previously created frequency list from the signal generator\nmemory and invalidates the frequency list handle.\n',
            'note': '\nThe signal generator must not be in the Generating state when you\ncall this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the frequency list you want the signal generator\nto remove. You create multiple frequency lists using\nniFgen_CreateFreqList. niFgen_CreateFreqList returns a handle that you\nuse to identify each list. Specify a value of -1 to clear all frequency\nlists.\n\n**Defined Value**\n\nNIFGEN_VAL_ALL_FLISTS—Remove all frequency lists from the signal\ngenerator.\n\n**Default Value**: None\n'
                },
                'name': 'frequencyListHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearInterchangeWarnings': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Clears the list of current interchange warnings.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearUserStandardWaveform': {
        'documentation': {
            'description': '\nClears the user-defined waveform created by the\nnifgen_DefineUserStandardWaveform function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name from which you want to clear a user standard\nwaveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'CloseExtCal': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCloses an NI-FGEN external calibration session and, if specified, stores\nthe new calibration constants and calibration data, such as time and\ntemperature, in the onboard EEPROM.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_InitExtCal function and identifies a particular instrument\nsession.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies he action to perform upon closing.\n\n**Defined Values**\n\n**Default Value**: NIFGEN_VAL_EXT_CAL_ABORT\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_EXT_CAL_ABORT',
                            'No changes are made to the calibration constants and data in the EEPROM.'
                        ],
                        [
                            'NIFGEN_VAL_EXT_CAL_COMMIT',
                            'The new calibration constants and data determined during the external calibration session are stored in the onboard EEPROM.'
                        ]
                    ]
                },
                'name': 'action',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Commit': {
        'documentation': {
            'description': '\nCauses a transition to the Committed state. This function verifies\nattribute values, reserves the device, and commits the attribute values\nto the device. If the attribute values are all valid, NI-FGEN sets the\ndevice hardware configuration to match the session configuration. This\nfunction does not support the NI 5401/5404/5411/5431 signal generators.\n\nIn the Committed state, you can load waveforms, scripts, and sequences\ninto memory. If any attributes are changed, NI-FGEN implicitly\ntransitions back to the Idle state, where you can program all session\nproperties before applying them to the device. This function has no\neffect if the device is already in the Committed or Generating state and\nreturns a successful status value.\n\nCalling this VI before the niFgen Initiate Generation VI is optional but\nhas the following benefits:\n\n-  Routes are committed, so signals are exported or imported.\n-  Any Reference Clock and external clock circuits are phase-locked.\n-  A subsequent niFgen_InitiateGeneration function can run faster\n   because the device is already configured.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureAmplitude': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the amplitude of the standard waveform that you want the\nsignal generator to produce.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to configure a standard\nwaveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the amplitude of the standard waveform that you want the\nsignal generator to produce. This value is the amplitude at the output\nterminal. NI-FGEN sets the NIFGEN_ATTR_FUNC_AMPLITUDE attribute to\nthis value.\n\nFor example, to produce a waveform ranging from –5.00 V to +5.00 V, set\nthe amplitude to 10.00 V.\n\n**Units**: peak-to-peak voltage\n\n**Default Value**: None\n',
                    'note': '\nThis parameter does not affect signal generator behavior when you set\nthe **waveform** parameter of the niFgen_ConfigureStandardWaveform\nfunction to NIFGEN_VAL_WFM_DC.\n'
                },
                'name': 'amplitude',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureArbSequence': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the signal generator attributes that affect arbitrary\nsequence generation. Sets the NIFGEN_ATTR_ARB_SEQUENCE_HANDLE,\nNIFGEN_ATTR_ARB_GAIN, and NIFGEN_ATTR_ARB_OFFSET attributes.\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name from which you want to configure an arbitrary\nsequence.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the arbitrary sequence that you want the signal\ngenerator to produce. NI-FGEN sets the\nNIFGEN_ATTR_ARB_SEQUENCE_HANDLE attribute to this value. You can\ncreate an arbitrary sequence using the niFgen_CreateArbSequence or\nniFgen_CreateAdvancedArbSequence function. These functions return a\nhandle that you use to identify the sequence.\n\n**Default Value**: None\n'
                },
                'name': 'sequenceHandle',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the factor by which the signal generator scales the arbitrary\nwaveforms in the sequence. When you create an arbitrary waveform, you\nmust first normalize the data points to a range of –1.00 to +1.00. You\ncan use this parameter to scale the waveform to other ranges. The gain\nis applied before the offset is added.\n\nFor example, to configure the output signal to range from –2.00 to\n+2.00 V, set **gain** to 2.00.\n\n**Units**: unitless\n\n**Default Value**: None\n'
                },
                'name': 'gain',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value the signal generator adds to the arbitrary waveform\ndata. When you create arbitrary waveforms, you must first normalize the\ndata points to a range of –1.00 to +1.00 V. You can use this parameter\nto shift the range of the arbitrary waveform. NI-FGEN sets the\nNIFGEN_ATTR_ARB_OFFSET attribute to this value.\n\nFor example, to configure the output signal to range from 0.00 to 2.00 V\ninstead of –1.00 to 1.00 V, set the offset to 1.00.\n\n**Units**: volts\n\n**Default Value**: None\n'
                },
                'name': 'offset',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureArbWaveform': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the attributes of the signal generator that affect arbitrary\nwaveform generation. Sets the NIFGEN_ATTR_ARB_WAVEFORM_HANDLE,\nNIFGEN_ATTR_ARB_GAIN, and NIFGEN_ATTR_ARB_OFFSET attributes.\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to configure an arbitrary\nwaveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the arbitrary waveform you want the signal\ngenerator to produce. NI-FGEN sets the\nNIFGEN_ATTR_ARB_WAVEFORM_HANDLE attribute to this value. You can\ncreate an arbitrary waveform using one of the following niFgen Create\nWaveform functions:\n\n-  niFgen_CreateWaveformF64\n-  niFgen_CreateWaveformI16\n-  niFgen_CreateWaveformFromFileI16\n-  niFgen_CreateWaveformFromFileF64\n-  niFgen_CreateWaveformFromFileHWS\n\nThese functions return a handle that you use to identify the waveform.\n\n**Default Value**: None\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the factor by which the signal generator scales the arbitrary\nwaveforms in the sequence. When you create an arbitrary waveform, you\nmust first normalize the data points to a range of –1.00 to +1.00. You\ncan use this parameter to scale the waveform to other ranges. The gain\nis applied before the offset is added.\n\nFor example, to configure the output signal to range from –2.00 to\n+2.00 V, set **gain** to 2.00.\n\n**Units**: unitless\n\n**Default Value**: None\n'
                },
                'name': 'gain',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value the signal generator adds to the arbitrary waveform\ndata. When you create arbitrary waveforms, you must first normalize the\ndata points to a range of –1.00 to +1.00 V. You can use this parameter\nto shift the range of the arbitrary waveform. NI-FGEN sets the\nNIFGEN_ATTR_ARB_OFFSET attribute to this value.\n\nFor example, to configure the output signal to range from 0.00 to 2.00 V\ninstead of –1.00 to 1.00 V, set the offset to 1.00.\n\n**Units**: volts\n\n**Default Value**: None\n'
                },
                'name': 'offset',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureChannels': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the channels to use with the instrument specified in the\n**vi** parameter. If you call this function, you must call it\nimmediately after initializing your session and before configuring\nattributes or writing data.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel on which all subsequent channel-based attributes\nin the session are set. Valid values are non-negative integers. For\nexample, 0 is the only valid value on devices with one channel, while\ndevices with two channels support values of 0 and 1. You can specify\nmore than one channel by inserting commas between values (for example,\n0,1).\n'
                },
                'name': 'channels',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureClockMode': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSelects the clock mode for the signal generator.\n\nSome signal generators allow you to switch the Sample Clock to\nHigh-Resolution or Automatic Sampling mode with this function.\n\nWhen you select NIFGEN_VAL_DIVIDE_DOWN, NI-FGEN rounds the sample\nrate to a frequency that can be achieved by dividing down the board\nclock (Sample Clock timebase). However, if you select\nNIFGEN_VAL_HIGH_RESOLUTION, you can set the sample rate to any value.\nIf you select NIFGEN_VAL_AUTOMATIC, NI-FGEN selects the clock mode\nbased on the sample rate, using divide-down sampling when possible.\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSets the clock mode of the signal generator.\n\n****Defined Values****\n\n**Default Value**: NIFGEN_VAL_HIGH_RESOLUTION (NI 5450, NI 5451),\nNIFGEN_VAL_DIVIDE_DOWN (all other devices)\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_DIVIDE_DOWN',
                            '**Divide down sampling**—Sample rates are generated by dividing the source frequency.'
                        ],
                        [
                            'NIFGEN_VAL_HIGH_RESOLUTION',
                            '**High resolution sampling**—Sample rate is generated by a high-resolution clock source.'
                        ],
                        [
                            'NIFGEN_VAL_AUTOMATIC',
                            '**Automatic Selection**—NI-FGEN selects between the divide-down and high-resolution clocking modes.'
                        ]
                    ]
                },
                'name': 'clockMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureCustomFIRFilterCoefficients': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nSets the FIR filter coefficients used by the onboard signal processing\nblock. The values are coerced to the closest settings achievable by the\nsignal generator.\n\nRefer to the *FIR Filter* topic for your device in the *NI Signal\nGenerators Help* for more information about FIR filter coefficients.\nThis function is supported only for the NI 5441.\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to configure the operation\nmode.\n\n**Defined Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of coefficients. The NI 5441 requires 95.'
                },
                'name': 'numberOfCoefficients',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data the onboard signal processor uses for the\nFIR filter coefficients. For the NI 5441, provide a symmetric array of\n95 coefficients to this parameter. The array must have at least as many\nelements as the value that you specify in the **numberOfCoefficients**\nparameter in this function.\nThe coefficients should range between –1.00 and +1.00.\n'
                },
                'name': 'coefficientsArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'numberOfCoefficients'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeScriptTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Configures the specified Script Trigger for digital edge triggering.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Script Trigger used for triggering.\n\n**Defined Values**\n\n**Default Value**: "ScriptTrigger0"\n',
                    'table_body': [
                        [
                            '"ScriptTrigger0"',
                            'Script Trigger 0'
                        ],
                        [
                            '"ScriptTrigger1"',
                            'Script Trigger 1'
                        ],
                        [
                            '"ScriptTrigger2"',
                            'Script Trigger 2'
                        ],
                        [
                            '"ScriptTrigger3"',
                            'Script Trigger 3'
                        ]
                    ]
                },
                'name': 'triggerId',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies which trigger source the signal generator uses.\n\n**Defined Values**\n\n**Default Value**: "PFI0"\n',
                    'table_body': [
                        [
                            '"PFI0"',
                            'PFI 0'
                        ],
                        [
                            '"PFI1"',
                            'PFI 1'
                        ],
                        [
                            '"PFI2"',
                            'PFI 2'
                        ],
                        [
                            '"PFI3"',
                            'PFI 3'
                        ],
                        [
                            '"PFI4"',
                            'PFI 4'
                        ],
                        [
                            '"PFI5"',
                            'PFI 5'
                        ],
                        [
                            '"PFI6"',
                            'PFI 6'
                        ],
                        [
                            '"PFI7"',
                            'PFI 7'
                        ],
                        [
                            '"PXI_Trig0"',
                            'PXI trigger line 0 or RTSI line 0'
                        ],
                        [
                            '"PXI_Trig1"',
                            'PXI trigger line 1 or RTSI line 1'
                        ],
                        [
                            '"PXI_Trig2"',
                            'PXI trigger line 2 or RTSI line 2'
                        ],
                        [
                            '"PXI_Trig3"',
                            'PXI trigger line 3 or RTSI line 3'
                        ],
                        [
                            '"PXI_Trig4"',
                            'PXI trigger line 4 or RTSI line 4'
                        ],
                        [
                            '"PXI_Trig5"',
                            'PXI trigger line 5 or RTSI line 5'
                        ],
                        [
                            '"PXI_Trig6"',
                            'PXI trigger line 6 or RTSI line 6'
                        ],
                        [
                            '"PXI_Trig7"',
                            'PXI trigger line 7 or RTSI line 7'
                        ],
                        [
                            '"PXI_Star"',
                            'PXI star trigger line'
                        ]
                    ]
                },
                'name': 'source',
                'type': 'ViConstString'
            },
            {
                'default_value': 'ScriptTriggerDigitalEdgeEdge.RISING',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the edge to detect.\n\n****Defined Values****\n\n****Default Value**:** NIFGEN_VAL_RISING_EDGE\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_RISING_EDGE',
                            'Occurs when the signal transitions from low level to high level.'
                        ],
                        [
                            'NIFGEN_VAL_FALLING_EDGE',
                            'Occurs when the signal transitions from high level to low level.'
                        ]
                    ]
                },
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeStartTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Configures the Start Trigger for digital edge triggering.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies which trigger source the signal generator uses.\n\n**Defined Values**\n\n**Default Value**: "PFI0"\n',
                    'table_body': [
                        [
                            '"PFI0"',
                            'PFI 0'
                        ],
                        [
                            '"PFI1"',
                            'PFI 1'
                        ],
                        [
                            '"PFI2"',
                            'PFI 2'
                        ],
                        [
                            '"PFI3"',
                            'PFI 3'
                        ],
                        [
                            '"PFI4"',
                            'PFI 4'
                        ],
                        [
                            '"PFI5"',
                            'PFI 5'
                        ],
                        [
                            '"PFI6"',
                            'PFI 6'
                        ],
                        [
                            '"PFI7"',
                            'PFI 7'
                        ],
                        [
                            '"PXI_Trig0"',
                            'PXI trigger line 0 or RTSI line 0'
                        ],
                        [
                            '"PXI_Trig1"',
                            'PXI trigger line 1 or RTSI line 1'
                        ],
                        [
                            '"PXI_Trig2"',
                            'PXI trigger line 2 or RTSI line 2'
                        ],
                        [
                            '"PXI_Trig3"',
                            'PXI trigger line 3 or RTSI line 3'
                        ],
                        [
                            '"PXI_Trig4"',
                            'PXI trigger line 4 or RTSI line 4'
                        ],
                        [
                            '"PXI_Trig5"',
                            'PXI trigger line 5 or RTSI line 5'
                        ],
                        [
                            '"PXI_Trig6"',
                            'PXI trigger line 6 or RTSI line 6'
                        ],
                        [
                            '"PXI_Trig7"',
                            'PXI trigger line 7 or RTSI line 7'
                        ],
                        [
                            '"PXI_Star"',
                            'PXI star trigger line'
                        ]
                    ]
                },
                'name': 'source',
                'type': 'ViConstString'
            },
            {
                'default_value': 'StartTriggerDigitalEdgeEdge.RISING',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the edge to detect.\n\n****Defined Values****\n\n****Default Value**:** NIFGEN_VAL_RISING_EDGE\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_RISING_EDGE',
                            'Occurs when the signal transitions from low level to high level.'
                        ],
                        [
                            'NIFGEN_VAL_FALLING_EDGE',
                            'Occurs when the signal transitions from high level to low level.'
                        ]
                    ]
                },
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalGainAndOffset': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'arraySizes',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'digitalGain',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'digitalCrossGain',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'digitalOffset',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalLevelPauseTrigger': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'source',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'level',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalLevelScriptTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Configures the specified Script Trigger for digital level triggering.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Script Trigger used for triggering.\n\n**Defined Values**\n\n**Default Value**: "ScriptTrigger0"\n',
                    'table_body': [
                        [
                            '"ScriptTrigger0"',
                            'Script Trigger 0'
                        ],
                        [
                            '"ScriptTrigger1"',
                            'Script Trigger 1'
                        ],
                        [
                            '"ScriptTrigger2"',
                            'Script Trigger 2'
                        ],
                        [
                            '"ScriptTrigger3"',
                            'Script Trigger 3'
                        ]
                    ]
                },
                'name': 'triggerId',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies which trigger source the signal generator uses.\n\n**Defined Values**\n\n**Default Value**: "PFI0"\n',
                    'table_body': [
                        [
                            '"PFI0"',
                            'PFI 0'
                        ],
                        [
                            '"PFI1"',
                            'PFI 1'
                        ],
                        [
                            '"PFI2"',
                            'PFI 2'
                        ],
                        [
                            '"PFI3"',
                            'PFI 3'
                        ],
                        [
                            '"PFI4"',
                            'PFI 4'
                        ],
                        [
                            '"PFI5"',
                            'PFI 5'
                        ],
                        [
                            '"PFI6"',
                            'PFI 6'
                        ],
                        [
                            '"PFI7"',
                            'PFI 7'
                        ],
                        [
                            '"PXI_Trig0"',
                            'PXI trigger line 0 or RTSI line 0'
                        ],
                        [
                            '"PXI_Trig1"',
                            'PXI trigger line 1 or RTSI line 1'
                        ],
                        [
                            '"PXI_Trig2"',
                            'PXI trigger line 2 or RTSI line 2'
                        ],
                        [
                            '"PXI_Trig3"',
                            'PXI trigger line 3 or RTSI line 3'
                        ],
                        [
                            '"PXI_Trig4"',
                            'PXI trigger line 4 or RTSI line 4'
                        ],
                        [
                            '"PXI_Trig5"',
                            'PXI trigger line 5 or RTSI line 5'
                        ],
                        [
                            '"PXI_Trig6"',
                            'PXI trigger line 6 or RTSI line 6'
                        ],
                        [
                            '"PXI_Trig7"',
                            'PXI trigger line 7 or RTSI line 7'
                        ],
                        [
                            '"PXI_Star"',
                            'PXI star trigger line'
                        ]
                    ]
                },
                'name': 'source',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether the Script Trigger asserts on a high or low digital\nlevel.\n\n**Defined Values**\n\n**Default Value**: "HighLevel"\n',
                    'table_body': [
                        [
                            '"HighLevel"',
                            'Script Trigger asserts on a high digital level.'
                        ],
                        [
                            '"LowLevel"',
                            'Script Trigger asserts on a low digital level.'
                        ]
                    ]
                },
                'name': 'triggerWhen',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureFreqList': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the attributes of the signal generator that affect frequency\nlist generation (the NIFGEN_ATTR_FREQ_LIST_HANDLE,\nNIFGEN_ATTR_FUNC_AMPLITUDE, NIFGEN_ATTR_FUNC_DC_OFFSET, and\nNIFGEN_ATTR_FUNC_START_PHASE attributes).\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to configure the frequency\nlist.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the frequency list that you want the signal\ngenerator to produce. NI-FGEN sets the NIFGEN_ATTR_FREQ_LIST_HANDLE\nattribute to this value. You can create a frequency list using the\nniFgen_CreateFreqList function, which returns a handle that you use to\nidentify the list.\n**Default Value**: None\n'
                },
                'name': 'frequencyListHandle',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the amplitude of the standard waveform that you want the\nsignal generator to produce. This value is the amplitude at the output\nterminal. NI-FGEN sets the NIFGEN_ATTR_FUNC_AMPLITUDE attribute to\nthis value.\n\nFor example, to produce a waveform ranging from –5.00 V to +5.00 V, set\nthe amplitude to 10.00 V.\n\n**Units**: peak-to-peak voltage\n\n**Default Value**: None\n',
                    'note': '\nThis parameter does not affect signal generator behavior when you set\nthe **waveform** parameter of the niFgen_ConfigureStandardWaveform\nfunction to NIFGEN_VAL_WFM_DC.\n'
                },
                'name': 'amplitude',
                'type': 'ViReal64'
            },
            {
                'default_value': 0.0,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the DC offset of the standard waveform that you want the\nsignal generator to produce. The value is the offset from ground to the\ncenter of the waveform you specify with the **waveform** parameter,\nobserved at the output terminal. For example, to configure a waveform\nwith an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the\n**dcOffset** to 5.00 V. NI-FGEN sets the NIFGEN_ATTR_FUNC_DC_OFFSET\nattribute to this value.\n\n**Units**: volts\n\n**Default Value**: None\n'
                },
                'name': 'dcOffset',
                'type': 'ViReal64'
            },
            {
                'default_value': 0.0,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the horizontal offset of the standard waveform you want the\nsignal generator to produce. Specify this attribute in degrees of one\nwaveform cycle. NI-FGEN sets the NIFGEN_ATTR_FUNC_START_PHASE\nattribute to this value. A start phase of 180 degrees means output\ngeneration begins halfway through the waveform. A start phase of 360\ndegrees offsets the output by an entire waveform cycle, which is\nidentical to a start phase of 0 degrees.\n\n**Units**: degrees of one cycle\n\n**Default Value**: None degrees\n',
                    'note': '\nThis parameter does not affect signal generator behavior when you set\nthe **waveform** parameter to NIFGEN_VAL_WFM_DC.\n'
                },
                'name': 'startPhase',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureFrequency': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the frequency of the standard waveform that you want the\nsignal generator to produce.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to configure a standard\nwaveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\n| Specifies the frequency of the standard waveform that you want the\n  signal generator to produce. NI-FGEN sets the\n  NIFGEN_ATTR_FUNC_FREQUENCY attribute to this value.\n\n**Units**: hertz\n\n**Default Value**: None\n',
                    'note': '\nThis parameter does not affect signal generator behavior when you set\nthe **waveform** parameter of the niFgen_ConfigureStandardWaveform\nfunction to NIFGEN_VAL_WFM_DC.\n'
                },
                'name': 'frequency',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureGain': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Configures the amount of gain to apply to the waveform.',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to configure the gain.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the factor by which the signal generator scales the arbitrary\nwaveforms in the sequence. When you create an arbitrary waveform, you\nmust first normalize the data points to a range of –1.00 to +1.00. You\ncan use this parameter to scale the waveform to other ranges. The gain\nis applied before the offset is added.\n\nFor example, to configure the output signal to range from –2.00 to\n+2.00 V, set **gain** to 2.00.\n\n**Units**: unitless\n\n**Default Value**: None\n'
                },
                'name': 'gain',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOperationMode': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nDetermines how the signal generator produces waveforms. NI signal\ngenerators support only Continuous operation mode. To control trigger\nmode, use the nifgen_ConfigureTriggerMode function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to configure the operation\nmode.\n\n**Defined Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the operation mode you want the signal generator to use.\nNI-FGEN sets the NIFGEN_ATTR_OPERATION_MODE attribute to this value.\nNI-FGEN supports only one value.\n\n**Defined Value**: NIFGEN_VAL_OPERATE_CONTINUOUS\n'
                },
                'name': 'operationMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOutputEnabled': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the signal generator to generate a signal at the channel\noutput connector.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to enable the output.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether you want to enable or disable the output. NI-FGEN uses\nthis value to set the NIFGEN_ATTR_OUTPUT_ENABLED attribute.\n\n****Defined Values****\n\n**Default Value**: VI_TRUE\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'Enable the output.'
                        ],
                        [
                            'VI_FALSE',
                            'Disable the output.'
                        ]
                    ]
                },
                'name': 'enabled',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOutputImpedance': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Configures the output impedance for the channel you specify.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to set the output\nimpedance.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the impedance value that you want the signal generator to use.\nNI-FGEN sets the NIFGEN_ATTR_OUTPUT_IMPEDANCE attribute to this\nvalue.\n\n**Units**: Ω (ohms)\n\n****Defined Values****:\n\n**Default Value**: NIFGEN_VAL_50_OHMS\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_50_OHMS',
                            'Specifies that 50 Ω of impedance is used'
                        ],
                        [
                            'NIFGEN_VAL_75_OHMS',
                            'Specifies that 75 Ω of impedance is used'
                        ]
                    ]
                },
                'name': 'impedance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOutputMode': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the output mode of the signal generator. The output mode\ndetermines how the signal generator produces waveforms. For example, you\ncan select to generate a standard waveform, an arbitrary waveform, or a\nsequence of arbitrary waveforms.\n',
            'note': '\nThe signal generator must not be in the Generating state when you\ncall this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output mode that you want the signal generator to use. The\nvalue you specify determines which functions and attributes you can use\nto configure the waveform the signal generator produces.\nRefer to the NIFGEN_ATTR_OUTPUT_MODE attribute for more information\nabout setting this parameter.\n****Defined Values****\n**Default Value**: NIFGEN_VAL_OUTPUT_FUNC\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_OUTPUT_FUNC',
                            '**Standard Function mode**—Generates standard function waveforms such as sine, square, triangle, and so on.'
                        ],
                        [
                            'NIFGEN_VAL_OUTPUT_FREQ_LIST',
                            '**Frequency List mode**—Generates a standard function using a list of frequencies you define.'
                        ],
                        [
                            'NIFGEN_VAL_OUTPUT_ARB',
                            '**Arbitrary waveform mode**—Generates waveforms from user-created/provided waveform arrays of numeric data.'
                        ],
                        [
                            'NIFGEN_VAL_OUTPUT_SEQ',
                            '**Arbitrary sequence mode**—Generates downloaded waveforms in an order your specify.'
                        ],
                        [
                            'NIFGEN_VAL_OUTPUT_SCRIPT',
                            '**Script mode**—Allows you to use scripting to link and loop multiple waveforms in complex combinations.'
                        ]
                    ]
                },
                'name': 'outputMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureP2PEndpointFullnessStartTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the Start Trigger for to detect peer-to-peer endpoint\nfullness. Generation begins when the number of samples in the\npeer-to-peer endpoint reaches the threshold indicated by the\n**p2pEndpointFullnessLevel** parameter.\n',
            'note': '\nBecause there is an additional internal FIFO in the signal generator,\nthe writer peer must actually write 2,304 bytes more than the quantity\nof data specified by this function to satisfy the trigger level.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the quantity of data in the FIFO endpoint that asserts the\ntrigger. The value –1 specifies that NI-FGEN uses a default value based\non your endpoint configuration.\n\n**Units**: samples per channel\n'
                },
                'name': 'p2pEndpointFullnessLevel',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureRefClockFrequency': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the signal generator reference clock frequency. The signal\ngenerator uses the reference clock to derive frequencies and sample\nrates when generating waveforms.\n',
            'note': '\nThe signal generator must not be in the Generating state when you\ncall this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe reference clock frequency in Hz.\n\n**Default Value**: 10000000\n'
                },
                'name': 'referenceClockFrequency',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureRefClockSource': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the signal generator reference clock source. The signal\ngenerator uses the reference clock to derive frequencies and sample\nrates when generating waveforms.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the reference clock source that you want the signal generator\nto use. NI-FGEN sets the NIFGEN_ATTR_REF_CLOCK_SOURCE attribute to\nthis value.\n\nThe signal generator derives the frequencies and sample rates that it\nuses to generate waveforms from the source you specify.\n\nFor example, when you set this parameter to\nNIFGEN_VAL_REF_CLOCK_EXTERNAL, the signal generator uses the signal\nit receives at its external clock terminal as the reference clock.\n\n****Defined Values****\n\n**Default Value**: NIFGEN_VAL_REF_CLOCK_INTERNAL\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_REF_CLOCK_INTERNAL',
                            'Internal clock source'
                        ],
                        [
                            'NIFGEN_VAL_REF_CLOCK_EXTERNAL',
                            'External clock source'
                        ],
                        [
                            'NIFGEN_VAL_REF_CLOCK_RTSI_CLOCK',
                            'RTSI clock'
                        ],
                        [
                            'NIFGEN_VAL_REF_CLOCK_TTL7',
                            'TTL 7'
                        ],
                        [
                            'NIFGEN_VAL_PXI_CLK10',
                            'PXI 10 MHz clock'
                        ],
                        [
                            'NIFGEN_VAL_REF_IN',
                            'External clock source'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_0',
                            'RTSI 0'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_1',
                            'RTSI 1'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_2',
                            'RTSI 2'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_3',
                            'RTSI 3'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_4',
                            'RTSI 4'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_5',
                            'RTSI 5'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_6',
                            'RTSI 6'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_7',
                            'RTSI 7'
                        ],
                        [
                            'NIFGEN_VAL_CLK_IN',
                            'CLK IN front panel connector'
                        ]
                    ]
                },
                'name': 'referenceClockSource',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureReferenceClock': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the signal generator Reference Clock source and frequency.\nThe signal generator uses the Reference Clock to tune the Sample Clock\ntimebase of the signal generator so that the frequency stability and\naccuracy of the Sample Clock timebase matches that of the Reference\nClock.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the source for the Reference Clock. For example, when you set\nthis parameter to "ClkIn," the signal generator uses the signal it\nreceives at its CLK IN front panel connector as the Reference Clock. The\nReference Clock phase-locks with the signal generator Sample Clock\ntimebase to allow the frequency stability and accuracy of the Sample\nClock timebase to match that of the Reference Clock.\n****Defined Values****\n**Default Value**: "None"\n',
                    'note': '\nThe following **Defined Values** are examples of possible Reference\nClock sources. For a complete list of the Reference Clock sources\navailable on your device, refer to the Routes topic for your device or\nthe **Device Routes** tab in MAX.\n',
                    'table_body': [
                        [
                            '"None"',
                            'No Reference Clock'
                        ],
                        [
                            '"PXI_Clk"',
                            '10 MHz backplane Reference Clock'
                        ],
                        [
                            '"ClkIn"',
                            'CLK IN front panel connector'
                        ],
                        [
                            '"OnboardReferenceClock"',
                            'Onboard Reference Clock'
                        ],
                        [
                            '"RTSI7"',
                            'RTSI line 7'
                        ],
                        [
                            '"RefIn"',
                            'REF IN front panel connector'
                        ]
                    ]
                },
                'name': 'referenceClockSource',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe Reference Clock frequency in hertz.\n\n**Default Value**: 10000000\n'
                },
                'name': 'referenceClockFrequency',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSampleClockInputSource': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'source',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSampleClockOutputEnabled': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'enabled',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSampleClockSource': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the source of the Sample Clock (Update Clock) of the signal\ngenerator.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Sample Clock source the signal generator uses.\n****Defined Values****\n**Default Value**: "OnboardClock"\n',
                    'note': '\nThe following **Defined Values** are examples of possible Sample\nClock sources. For a complete list of the Sample Clock sources available\non your device, refer to the Routes topic for your device or the\n**Device Routes** tab in MAX.\n',
                    'table_body': [
                        [
                            '"OnboardClock"',
                            'Onboard Clock'
                        ],
                        [
                            '"ClkIn"',
                            'CLK IN front panel connector'
                        ],
                        [
                            '"PXI_Star"',
                            'PXI star trigger line'
                        ],
                        [
                            '"PXI_Trig0"',
                            'PXI trigger line 0 or RTSI line 0'
                        ],
                        [
                            '"PXI_Trig1"',
                            'PXI trigger line 1 or RTSI line 1'
                        ],
                        [
                            '"PXI_Trig2"',
                            'PXI trigger line 2 or RTSI line 2'
                        ],
                        [
                            '"PXI_Trig3"',
                            'PXI trigger line 3 or RTSI line 3'
                        ],
                        [
                            '"PXI_Trig4"',
                            'PXI trigger line 4 or RTSI line 4'
                        ],
                        [
                            '"PXI_Trig5"',
                            'PXI trigger line 5 or RTSI line 5'
                        ],
                        [
                            '"PXI_Trig6"',
                            'PXI trigger line 6 or RTSI line 6'
                        ],
                        [
                            '"PXI_Trig7"',
                            'PXI trigger line 7 or RTSI line 7'
                        ],
                        [
                            '"DDC_ClkIn"',
                            'Sample Clock from DDC connector'
                        ]
                    ]
                },
                'name': 'sampleClockSource',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSampleRate': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the NIFGEN_ATTR_ARB_SAMPLE_RATE attribute, which\ndetermines the rate at which the signal generator produces arbitrary\nwaveforms. When you configure the signal generator to produce an\narbitrary sequence, this value is the sample rate for all arbitrary\nwaveforms in the sequence.\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the sample rate at which you want the signal generator to\ngenerate arbitrary waveforms. NI-FGEN sets the\nNIFGEN_ATTR_ARB_SAMPLE_RATE attribute to this value.\n\n**Units**: Samples/s\n\n**Default Value**: None\n'
                },
                'name': 'sampleRate',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeScriptTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Configures the specified Script Trigger for software edge triggering.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Script Trigger used for triggering.\n\n**Defined Values**\n\n**Default Value**: "ScriptTrigger0"\n',
                    'table_body': [
                        [
                            '"ScriptTrigger0"',
                            'Script Trigger 0'
                        ],
                        [
                            '"ScriptTrigger1"',
                            'Script Trigger 1'
                        ],
                        [
                            '"ScriptTrigger2"',
                            'Script Trigger 2'
                        ],
                        [
                            '"ScriptTrigger3"',
                            'Script Trigger 3'
                        ]
                    ]
                },
                'name': 'triggerId',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeStartTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Configures the Start Trigger for software edge triggering.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSparseMarker': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'name',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'wfmHandle',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'numIndexes',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'indexes',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'destination',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureStandardWaveform': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nConfigures the following attributes of the signal generator that affect\nstandard waveform generation:\n\n-  NIFGEN_ATTR_FUNC_WAVEFORM\n-  NIFGEN_ATTR_FUNC_AMPLITUDE\n-  NIFGEN_ATTR_FUNC_DC_OFFSET\n-  NIFGEN_ATTR_FUNC_FREQUENCY\n-  NIFGEN_ATTR_FUNC_START_PHASE\n',
            'note': '\nYou must call the niFgen_ConfigureOutputMode function with the\n**outputMode** parameter set to NIFGEN_VAL_OUTPUT_FUNC before calling\nthis function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to configure a standard\nwaveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the standard waveform that you want the signal generator to\nproduce. NI-FGEN sets the NIFGEN_ATTR_FUNC_WAVEFORM attribute to this\nvalue.\n\n****Defined Values****\n\n**Default Value**: NIFGEN_VAL_WFM_SINE\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_WFM_SINE',
                            'Specifies that the signal generator produces a sinusoid waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_SQUARE',
                            'Specifies that the signal generator produces a square waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_TRIANGLE',
                            'Specifies that the signal generator produces a triangle waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_RAMP_UP',
                            'Specifies that the signal generator produces a positive ramp waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_RAMP_DOWN',
                            'Specifies that the signal generator produces a negative ramp waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_DC',
                            'Specifies that the signal generator produces a constant voltage.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_NOISE',
                            'Specifies that the signal generator produces white noise.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_USER',
                            'Specifies that the signal generator produces a user-defined waveform as defined with the nifgen_DefineUserStandardWaveform function.'
                        ]
                    ]
                },
                'enum': 'Waveform',
                'name': 'waveform',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the amplitude of the standard waveform that you want the\nsignal generator to produce. This value is the amplitude at the output\nterminal. NI-FGEN sets the NIFGEN_ATTR_FUNC_AMPLITUDE attribute to\nthis value.\n\nFor example, to produce a waveform ranging from –5.00 V to +5.00 V, set\nthe amplitude to 10.00 V.\n\n**Units**: peak-to-peak voltage\n\n**Default Value**: None\n',
                    'note': '\nThis parameter does not affect signal generator behavior when you set\nthe **waveform** parameter of the niFgen_ConfigureStandardWaveform\nfunction to NIFGEN_VAL_WFM_DC.\n'
                },
                'name': 'amplitude',
                'type': 'ViReal64'
            },
            {
                'default_value': 0.0,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the DC offset of the standard waveform that you want the\nsignal generator to produce. The value is the offset from ground to the\ncenter of the waveform you specify with the **waveform** parameter,\nobserved at the output terminal. For example, to configure a waveform\nwith an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the\n**dcOffset** to 5.00 V. NI-FGEN sets the NIFGEN_ATTR_FUNC_DC_OFFSET\nattribute to this value.\n\n**Units**: volts\n\n**Default Value**: None\n'
                },
                'name': 'dcOffset',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\n| Specifies the frequency of the standard waveform that you want the\n  signal generator to produce. NI-FGEN sets the\n  NIFGEN_ATTR_FUNC_FREQUENCY attribute to this value.\n\n**Units**: hertz\n\n**Default Value**: None\n',
                    'note': '\nThis parameter does not affect signal generator behavior when you set\nthe **waveform** parameter of the niFgen_ConfigureStandardWaveform\nfunction to NIFGEN_VAL_WFM_DC.\n'
                },
                'name': 'frequency',
                'type': 'ViReal64'
            },
            {
                'default_value': 0.0,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the horizontal offset of the standard waveform that you want\nthe signal generator to produce. Specify this parameter in degrees of\none waveform cycle. NI-FGEN sets the NIFGEN_ATTR_FUNC_START_PHASE\nattribute to this value. A start phase of 180 degrees means output\ngeneration begins halfway through the waveform. A start phase of 360\ndegrees offsets the output by an entire waveform cycle, which is\nidentical to a start phase of 0 degrees.\n\n**Units**: degrees of one cycle\n\n**Default Value**: 0.00\n',
                    'note': '\nThis parameter does not affect signal generator behavior when you set\nthe **waveform** parameter to NIFGEN_VAL_WFM_DC.\n'
                },
                'name': 'startPhase',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureStartTrigger': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'source',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'slope',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSynchronization': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the signal generator to receive a synchronization signal to\nsynchronize two or more NI 5401/5411/5431 signal generators. One signal\ngenerator should route a SYNC signal to a RTSI line by calling the\nnifgen_ExportSignal function (use the nifgen_RouteSignalOut function\nfor the NI 5404), and other signal generators should receive the signal\nby calling the niFgen_ConfigureSynchronization function.\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\nOnly the NI 5401/5411/5431 signal generators require this function to be\ncalled for proper synchronization.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to configure the\nsynchronization signal.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecify the source of the synchronization signal you want to use.\n\n****Defined Values****\n\n**Default Value**: NIFGEN_VAL_NONE\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_NONE',
                            'Specifies that no synchronization source is used.'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_0',
                            'Specifies that RTSI 0 or PXI_Trig 0 is used as the synchronization source.'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_1',
                            'Specifies that RTSI 1 or PXI_Trig 1 is used as the synchronization source.'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_2',
                            'Specifies that RTSI 2 or PXI_Trig 2 is used as the synchronization source.'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_3',
                            'Specifies that RTSI 3 or PXI_Trig 3 is used as the synchronization source.'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_4',
                            'Specifies that RTSI 4 or PXI_Trig 4 is used as the synchronization source.'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_5',
                            'Specifies that RTSI 5 or PXI_Trig 5 is used as the synchronization source.'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_6',
                            'Specifies that RTSI 6 or PXI_Trig 6 is used as the synchronization source.'
                        ],
                        [
                            'NIFGEN_VAL_TTL0',
                            'Specifies that TTL 0 is used as the synchronization source.'
                        ],
                        [
                            'NIFGEN_VAL_TTL1',
                            'Specifies that TTL 1 is used as the synchronization source.'
                        ],
                        [
                            'NIFGEN_VAL_TTL2',
                            'Specifies that TTL 2 is used as the synchronization source.'
                        ],
                        [
                            'NIFGEN_VAL_TTL3',
                            'Specifies that TTL 3 is used as the synchronization source.'
                        ],
                        [
                            'NIFGEN_VAL_TTL4',
                            'Specifies that TTL 4 is used as the synchronization source.'
                        ],
                        [
                            'NIFGEN_VAL_TTL5',
                            'Specifies that TTL 5 is used as the synchronization source.'
                        ],
                        [
                            'NIFGEN_VAL_TTL6',
                            'Specifies that TTL 6 is used as the synchronization source.'
                        ]
                    ]
                },
                'name': 'synchronizationSource',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTrigger': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'trigSource',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'cycleCount',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerMode': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the trigger mode for your device. Refer to the *Trigger Modes*\ntopic for your device in the *NI Signal Generators Help* for\ndescriptions of the specific behavior for supported trigger modes.\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\nIn Frequency List output mode, Stepped trigger mode is the same as Burst\ntrigger mode.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to configure the trigger\nmode.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the trigger mode.\n\n****Defined Values****\n\n**Default Value**: NIFGEN_VAL_CONTINUOUS\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_SINGLE',
                            'The waveform that you describe in the sequence list generates only once by going through the entire staging list. Only one trigger is required to start the waveform generation. You can use Single trigger mode in any output mode. After a trigger is received, the waveform generation starts from the first stage and continues through to the last stage.'
                        ],
                        [
                            'NIFGEN_VAL_CONTINUOUS',
                            'The waveform that you describe in the staging list generates infinitely by repeatedly cycling through the staging list. After a trigger is received, the waveform generation starts from the first stage and continues through to the last stage. After the last stage is completed, the waveform generation loops back to the start of the first stage and continues until it is stopped. Only one trigger is required to start the waveform generation.'
                        ],
                        [
                            'NIFGEN_VAL_STEPPED',
                            'After a Start Trigger is received, the waveform described by the first stage generates. Then, the device waits for the next trigger signal. On the next trigger, the waveform described by the second stage generates, and so on. After the staging list is exhausted, the waveform generation returns to the first stage and continues to repeat the cycle.'
                        ],
                        [
                            'NIFGEN_VAL_BURST',
                            'After a Start Trigger is received, the waveform described by the first stage generates until another trigger is received. At the next trigger, the buffer of the previous stage completes, then the waveform described by the second stage generates. After the staging list is exhausted, the waveform generation returns to the first stage and continues to repeat the cycle. In Frequency List mode, the duration instruction is ignored, and the trigger switches the frequency to the next frequency in the list.'
                        ]
                    ]
                },
                'name': 'triggerMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerSource': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the trigger source. The signal generator responds to a\ntrigger depending on the operation mode in which the signal generator is\noperating.\n',
            'note': '\nThe signal generator must not be in the Generating state when you\ncall this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to configure the trigger\nsource.\n\n**Defined Value:**"0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nControls which trigger source the signal generator uses.\n\n****Defined Values****\n\n**Default Value**: NIFGEN_VAL_IMMEDIATE\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_IMMEDIATE',
                            'Immediate'
                        ],
                        [
                            'NIFGEN_VAL_EXTERNAL',
                            'External (maps to PFI 0)'
                        ],
                        [
                            'NIFGEN_VAL_SOFTWARE_TRIG',
                            'Software trigger'
                        ],
                        [
                            'NIFGEN_VAL_PXI_STAR',
                            'PXI star'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_0',
                            'RTSI 0 or PXI_Trig 0'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_1',
                            'RTSI 1 or PXI_Trig 1'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_2',
                            'RTSI 2 or PXI_Trig 2'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_3',
                            'RTSI 3 or PXI_Trig 3'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_4',
                            'RTSI 4 or PXI_Trig 4'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_5',
                            'RTSI 5 or PXI_Trig 5'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_6',
                            'RTSI 6 or PXI_Trig 6'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_7',
                            'RTSI 7 or PXI_Trig 7'
                        ],
                        [
                            'NIFGEN_VAL_TTL0',
                            'TTL 0'
                        ],
                        [
                            'NIFGEN_VAL_TTL1',
                            'TTL 1'
                        ],
                        [
                            'NIFGEN_VAL_TTL2',
                            'TTL 2'
                        ],
                        [
                            'NIFGEN_VAL_TTL3',
                            'TTL 3'
                        ],
                        [
                            'NIFGEN_VAL_TTL4',
                            'TTL 4'
                        ],
                        [
                            'NIFGEN_VAL_TTL5',
                            'TTL 5'
                        ],
                        [
                            'NIFGEN_VAL_TTL6',
                            'TTL 6'
                        ],
                        [
                            'NIFGEN_VAL_PFI_0',
                            'PFI 0'
                        ],
                        [
                            'NIFGEN_VAL_PFI_1',
                            'PFI 1'
                        ],
                        [
                            'NIFGEN_VAL_PFI_2',
                            'PFI 2'
                        ],
                        [
                            'NIFGEN_VAL_PFI_3',
                            'PFI 3'
                        ]
                    ]
                },
                'name': 'triggerSource',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureUpdateClockSource': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the source of the update clock of the signal generator. The source\ncan be internal or external.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the update clock source.\n\n****Defined Values****\n\n**Default Value**: NIFGEN_VAL_INTERNAL\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_INTERNAL',
                            'Internal clock source'
                        ],
                        [
                            'NIFGEN_VAL_EXTERNAL',
                            'External clock source'
                        ],
                        [
                            'NIFGEN_VAL_PXI_STAR',
                            'PXI star'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_0',
                            'RTSI 0 or PXI_Trig 0'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_1',
                            'RTSI 1 or PXI_Trig 1'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_2',
                            'RTSI 2 or PXI_Trig 2'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_3',
                            'RTSI 3 or PXI_Trig 3'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_4',
                            'RTSI 4 or PXI_Trig 4'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_5',
                            'RTSI 5 or PXI_Trig 5'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_6',
                            'RTSI 6 or PXI_Trig 6'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_7',
                            'RTSI 7 or PXI_Trig 7'
                        ],
                        [
                            'NIFGEN_VAL_CLK_IN',
                            'CLK IN front panel connector'
                        ],
                        [
                            'NIFGEN_VAL_DDC_CLK_IN',
                            'Digital Data & Control clock in'
                        ]
                    ]
                },
                'name': 'updateClockSource',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateAdvancedArbSequence': {
        'documentation': {
            'description': '\nCreates an arbitrary sequence from an array of waveform handles and an\narray of corresponding loop counts. This function returns a handle that\nidentifies the sequence. You pass this handle to the\nniFgen_ConfigureArbSequence function to specify what arbitrary sequence\nyou want the signal generator to produce.\n\nThe niFgen_CreateAdvancedArbSequence function extends on the\nniFgen_CreateArbSequence function by adding the ability to set the\nnumber of samples in each sequence step and to set marker locations.\n\nAn arbitrary sequence consists of multiple waveforms. For each waveform,\nyou specify the number of times the signal generator produces the\nwaveform before proceeding to the next waveform. The number of times to\nrepeat a specific waveform is called the loop count.\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\nYou must call the nifgen_ConfigureOutputMode function to set the\n**outputMode** parameter to NIFGEN_VAL_OUTPUT_SEQ before calling this\nfunction.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of waveforms in the new arbitrary sequence that you\nwant to create. The value you pass must be between the minimum and\nmaximum sequence lengths that the signal generator allows. You can\nobtain the minimum and maximum sequence lengths from\n**minimumSequenceLength** and **maximumSequenceLength** in the\nnifgen_QueryArbSeqCapabilities function.\n\n**Default Value**: None\n'
                },
                'name': 'sequenceLength',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of waveform handles from which you want to create a\nnew arbitrary sequence. The array must have at least as many elements as\nthe value that you specify in **sequenceLength**. Each\n**waveformHandlesArray** element has a corresponding **loopCountsArray**\nelement that indicates how many times that waveform is repeated. You\nobtain waveform handles when you create arbitrary waveforms with the\nnifgen_AllocateWaveform function or one of the following niFgen\nCreateWaveform functions:\n\n-  nifgen_CreateWaveformF64\n-  nifgen_CreateWaveformI16\n-  nifgen_CreateWaveformFromFileI16\n-  nifgen_CreateWaveformFromFileF64\n-  nifgen_CreateWaveformFromFileHWS\n\n**Default Value**: None\n'
                },
                'name': 'waveformHandlesArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'sequenceLength'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of loop counts you want to use to create a new\narbitrary sequence. The array must have at least as many elements as the\nvalue that you specify in the **sequenceLength** parameter. Each\n**loopCountsArray** element corresponds to a **waveformHandlesArray**\nelement and indicates how many times to repeat that waveform. Each\nelement of the **loopCountsArray** must be less than or equal to the\nmaximum number of loop counts that the signal generator allows. You can\nobtain the maximum loop count from **maximumLoopCount** in the\nnifgen_QueryArbSeqCapabilities function.\n\n**Default Value**: None\n'
                },
                'name': 'loopCountsArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'sequenceLength'
                },
                'type': 'ViInt32[]'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of sample counts that you want to use to create a\nnew arbitrary sequence. The array must have at least as many elements as\nthe value you specify in the **sequenceLength** parameter. Each\n**sampleCountsArray** element corresponds to a **waveformHandlesArray**\nelement and indicates the subset, in samples, of the given waveform to\ngenerate. Each element of the **sampleCountsArray** must be larger than\nthe minimum waveform size, a multiple of the waveform quantum and no\nlarger than the number of samples in the corresponding waveform. You can\nobtain these values by calling the nifgen_QueryArbWfmCapabilities\nfunction.\n\n**Default Value**: None\n'
                },
                'name': 'sampleCountsArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'sequenceLength'
                },
                'type': 'ViInt32[]'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of marker locations to where you want a marker to be\ngenerated in the sequence. The array must have at least as many elements\nas the value you specify in the **sequenceLength** parameter. Each\n**markerLocationArray** element corresponds to a\n**waveformHandlesArray** element and indicates where in the waveform a\nmarker is to generate. The marker location must be less than the size of\nthe waveform the marker is in. The markers are coerced to the nearest\nmarker quantum and the coerced values are returned in the\n**coercedMarkersArray** parameter.\n\nIf you do not want a marker generated for a particular sequence stage,\nset this parameter to NIFGEN_VAL_NO_MARKER.\n\n**Defined Value**: NIFGEN_VAL_NO_MARKER\n\n**Default Value**: None\n'
                },
                'name': 'markerLocationArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'sequenceLength'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of all given markers that are coerced (rounded) to the\nnearest marker quantum. Not all devices coerce markers.\n\n**Default Value**: None\n'
                },
                'name': 'coercedMarkersArray',
                'size': {
                    'mechanism': 'python-code',
                    'value': '(0 if marker_location_array is None else len(marker_location_array))'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the handle that identifies the new arbitrary sequence. You can\npass this handle to nifgen_ConfigureArbSequence to generate the\narbitrary sequence.\n'
                },
                'name': 'sequenceHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateAdvancedFreqList': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'waveform',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'fListLength',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'frequencies',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'durations',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'markers',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'amplitudes',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'offsets',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'phases',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'fListHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateArbSequence': {
        'documentation': {
            'description': '\nCreates an arbitrary sequence from an array of waveform handles and an\narray of corresponding loop counts. This function returns a handle that\nidentifies the sequence. You pass this handle to the\nnifgen_ConfigureArbSequence function to specify what arbitrary sequence\nyou want the signal generator to produce.\n\nAn arbitrary sequence consists of multiple waveforms. For each waveform,\nyou can specify the number of times that the signal generator produces\nthe waveform before proceeding to the next waveform. The number of times\nto repeat a specific waveform is called the loop count.\n',
            'note': '\nYou must call the nifgen_ConfigureOutputMode function to set the\n**outputMode** parameter to NIFGEN_VAL_OUTPUT_SEQ before calling this\nfunction.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of waveforms in the new arbitrary sequence that you\nwant to create. The value you pass must be between the minimum and\nmaximum sequence lengths that the signal generator allows. You can\nobtain the minimum and maximum sequence lengths from\n**minimumSequenceLength** and **maximumSequenceLength** in the\nnifgen_QueryArbSeqCapabilities function.\n\n**Default Value**: None\n'
                },
                'name': 'sequenceLength',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of waveform handles from which you want to create a\nnew arbitrary sequence. The array must have at least as many elements as\nthe value that you specify in **sequenceLength**. Each\n**waveformHandlesArray** element has a corresponding **loopCountsArray**\nelement that indicates how many times that waveform is repeated. You\nobtain waveform handles when you create arbitrary waveforms with the\nnifgen_AllocateWaveform function or one of the following niFgen\nCreateWaveform functions:\n\n-  nifgen_CreateWaveformF64\n-  nifgen_CreateWaveformI16\n-  nifgen_CreateWaveformFromFileI16\n-  nifgen_CreateWaveformFromFileF64\n-  nifgen_CreateWaveformFromFileHWS\n\n**Default Value**: None\n'
                },
                'name': 'waveformHandlesArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'sequenceLength'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of loop counts you want to use to create a new\narbitrary sequence. The array must have at least as many elements as the\nvalue that you specify in the **sequenceLength** parameter. Each\n**loopCountsArray** element corresponds to a **waveformHandlesArray**\nelement and indicates how many times to repeat that waveform. Each\nelement of the **loopCountsArray** must be less than or equal to the\nmaximum number of loop counts that the signal generator allows. You can\nobtain the maximum loop count from **maximumLoopCount** in the\nnifgen_QueryArbSeqCapabilities function.\n\n**Default Value**: None\n'
                },
                'name': 'loopCountsArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'sequenceLength'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the handle that identifies the new arbitrary sequence. You can\npass this handle to nifgen_ConfigureArbSequence to generate the\narbitrary sequence.\n'
                },
                'name': 'sequenceHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateArbWaveform': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\n[OBSOLETE] This function is obsolete. Use the nifgen_CreateWaveformF64,\nnifgen_CreateWaveformI16, or nifgen_CreateWaveformComplexF64 function\ninstead of this function.\n\nCreates an arbitrary waveform and returns a handle that identifies that\nwaveform. You can pass this handle to the nifgen_ConfigureArbWaveform\nfunction to produce that waveform. You can also use the handles this\nfunction returns to specify a sequence of arbitrary waveforms with the\nnifgen_CreateArbSequence function.\n',
            'note': '\nYou must scale the data between –1.00 and +1.00. Use the **arbGain**\nparameter to generate different output voltages.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\n| Specifies the size of the arbitrary waveform that you want created.\n| The size must meet the following restrictions:\n\n-  The size must be less than or equal to the maximum waveform size that\n   the device allows.\n-  The size must be greater than or equal to the minimum waveform size\n   that the device allows.\n-  The size must be an integer multiple of the device waveform quantum.\n\n| \n| You can obtain these values from the **maximumWaveformSize**,\n  **minimumWaveformSize**, and **waveformQuantum** parameters in the\n  nifgen_QueryArbWfmCapabilities function.\n| ****Default Value**:** None\n'
                },
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data you want to use for the new arbitrary\nwaveform. The array must have at least as many elements as the value\nthat you specify in **waveformSize**.\n\nYou must normalize the data points in the array to be between –1.00 and\n+1.00.\n\n**Default Value**: None\n'
                },
                'name': 'waveformDataArray',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe handle that identifies the new waveform. This handle is used later\nwhen referring to this waveform.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateBinary16ArbWaveform': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\n[OBSOLETE] This function is obsolete. Use the nifgen_CreateWaveformI16\nfunction instead of this function.\n\nCreates an arbitrary waveform from binary data and returns a handle that\nidentifies that waveform. You can pass this handle to the\nnifgen_ConfigureArbWaveform function to produce that waveform. You can\nalso use the handles this function returns to specify a sequence of\narbitrary waveforms with the nifgen_CreateArbSequence function.\n',
            'note': '\nYou must set the output mode to NIFGEN_VAL_OUTPUT_ARB or\nNIFGEN_VAL_OUTPUT_SEQ before calling this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\n| Specifies the size of the arbitrary waveform that you want created.\n| The size must meet the following restrictions:\n\n-  The size must be less than or equal to the maximum waveform size that\n   the device allows.\n-  The size must be greater than or equal to the minimum waveform size\n   that the device allows.\n-  The size must be an integer multiple of the device waveform quantum.\n\n| \n| You can obtain these values from the **maximumWaveformSize**,\n  **minimumWaveformSize**, and **waveformQuantum** parameters in\n  nifgen_QueryArbWfmCapabilities.\n| ****Default Value**:** None\n'
                },
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data you want to use for the new arbitrary\nwaveform. The array must have at least as many elements as the value\nthat you specify in **waveformSize**.\n\nYou must normalize the data points in the array to be between –32768 and\n32767.\n\n**Default Value**: None\n'
                },
                'name': 'waveformDataArray',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe handle that identifies the new waveform. This handle is used later\nwhen referring to this waveform.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateChannelArbWaveform': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'wfmHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateChannelArbWaveform16': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'name': 'wfmHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateChannelArbWaveform32': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'wfmHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateFreqList': {
        'documentation': {
            'description': '\nCreates a frequency list from an array of frequencies\n(**frequencyArray**) and an array of durations (**durationArray**). The\ntwo arrays should have the same number of elements, and this value must\nalso be the size of the **frequencyListLength**. The function returns a\nhandle that identifies the frequency list (the **frequencyListHandle**).\nYou can pass this handle to nifgen_ConfigureFreqList to specify what\nfrequency list you want the signal generator to produce.\n\nA frequency list consists of a list of frequencies and durations. The\nsignal generator generates each frequency for the given amount of time\nand then proceeds to the next frequency. When the end of the list is\nreached, the signal generator starts over at the beginning of the list.\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the standard waveform that you want the signal generator to\nproduce. NI-FGEN sets the NIFGEN_ATTR_FUNC_WAVEFORM attribute to this\nvalue.\n\n****Defined Values****\n\n**Default Value**: NIFGEN_VAL_WFM_SINE\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_WFM_SINE',
                            'Specifies that the signal generator produces a sinusoid waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_SQUARE',
                            'Specifies that the signal generator produces a square waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_TRIANGLE',
                            'Specifies that the signal generator produces a triangle waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_RAMP_UP',
                            'Specifies that the signal generator produces a positive ramp waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_RAMP_DOWN',
                            'Specifies that the signal generator produces a negative ramp waveform.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_DC',
                            'Specifies that the signal generator produces a constant voltage.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_NOISE',
                            'Specifies that the signal generator produces white noise.'
                        ],
                        [
                            'NIFGEN_VAL_WFM_USER',
                            'Specifies that the signal generator produces a user-defined waveform as defined with the nifgen_DefineUserStandardWaveform function.'
                        ]
                    ]
                },
                'enum': 'Waveform',
                'name': 'waveform',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of steps in the frequency list you want to create.\nThe value must be between the minimum and maximum frequency list lengths\nthat the signal generator allows. You can obtain the minimum and maximum\nfrequency list lengths from the **minimumFrequencyListLength** and\n**maximumFrequencyListLength** parameters in the\nnifgen_QueryFreqListCapabilities function.\n\n**frequency** and **duration** must each be at least as long as this\nfrequency list length.\n\n**Default Value**: None\n'
                },
                'name': 'frequencyListLength',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of frequencies to form the frequency list. The array\nmust have at least as many elements as the value you specify in\n**frequencyListLength**. Each **frequencyArray** element has a\ncorresponding **durationArray** element that indicates how long that\nfrequency is repeated.\n\n**Units**: hertz\n\n**Default Value**: None\n'
                },
                'name': 'frequencyArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'frequencyListLength'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of durations to form the frequency list. The array\nmust have at least as many elements as the value that you specify in\n**frequencyListLength**. Each **durationArray** element has a\ncorresponding **frequencyArray** element and indicates how long in\nseconds to generate the corresponding frequency.\n\n**Units**: seconds\n\n**Default Value**: None\n'
                },
                'name': 'durationArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'frequencyListLength'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the handle that identifies the new frequency list. You can pass\nthis handle to nifgen_ConfigureFreqList to generate the arbitrary\nsequence.\n'
                },
                'name': 'frequencyListHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateWaveformComplexF64': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCreates an onboard waveform from complex double-precision floating-point\n(F64) data for use with the NIFGEN_ATTR_OUTPUT_MODE attribute set to\nArbitrary Waveform or Arbitrary Sequence output mode on devices with the\nNIFGEN_ATTR_OUTPUT_ENABLED attribute set to VI_TRUE and the\nNIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute set to\nNIFGEN_VAL_OSP_COMPLEX. The **waveformHandle** returned by the\nfunction can be used later for setting the active waveform, changing the\ndata in the waveform, building sequences of waveforms, or deleting the\nwaveform when it is no longer needed.\n',
            'note': '\nYou must call the nifgen_ConfigureOutputMode function to set the\n**outputMode** parameter to NIFGEN_VAL_OUTPUT_ARB or\nNIFGEN_VAL_OUTPUT_SEQ before calling this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to create the waveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size of the arbitrary waveform that you want to create.\n\nThe size must meet the following restrictions:\n\n-  The size must be less than or equal to the maximum waveform size that\n   the device allows.\n-  The size must be greater than or equal to the minimum waveform size\n   that the device allows.\n-  The size must be an integer multiple of the device waveform quantum.\n\nYou can obtain these values from the **maximumWaveformSize**,\n**minimumWaveformSize**, and **waveformQuantum** parameters of the\nniFgen_QueryArbWfmCapabilities function.\n\n| \n| **Default Value**: None\n'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data you want to use for the new arbitrary\nwaveform. The array must have at least as many elements as the value\nthat you specify in **waveformSize**.\n\nYou must normalize the data points in the array to be between –1.00 and\n+1.00.\n\n**Default Value**: None\n'
                },
                'name': 'waveformDataArray',
                'type': 'ni_complex_number'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe handle that identifies the new waveform. This handle is used later\nwhen referring to this waveform.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateWaveformDispatcher': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Creates an onboard waveform for use in Arbitrary Waveform output mode or Arbitrary Sequence output mode.',
            'note': 'You must set NIFGEN_ATTR_OUTPUT_MODE to NIFGEN_VAL_OUTPUT_ARB or NIFGEN_VAL_OUTPUT_SEQ before calling this function.'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '_numpy',
                'session_filename': 'create_waveform'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Array of data for the new arbitrary waveform. This may be an iterable of float or int16, or for best performance a numpy.ndarray of dtype int16 or float64.'
                },
                'name': 'waveformDataArray',
                'type': 'ViReal64',
                'type_in_documentation': 'iterable of float or int16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The handle that identifies the new waveform. This handle is used in other methods when referring to this waveform.'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'python_name': 'create_waveform',
        'returns': 'ViStatus'
    },
    'CreateWaveformF64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCreates an onboard waveform from binary F64 (floating point double) data\nfor use in Arbitrary Waveform output mode or Arbitrary Sequence output\nmode. The **waveformHandle** returned can later be used for setting the\nactive waveform, changing the data in the waveform, building sequences\nof waveforms, or deleting the waveform when it is no longer needed.\n',
            'note': '\nYou must call the nifgen_ConfigureOutputMode function to set the\n**outputMode** parameter to NIFGEN_VAL_OUTPUT_ARB or\nNIFGEN_VAL_OUTPUT_SEQ before calling this function.\n'
        },
        'method_name_for_documentation': 'create_waveform',
        'method_templates': [
            {
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            },
            {
                'method_python_name_suffix': '_numpy',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to create the waveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\n| Specifies the size of the arbitrary waveform that you want to create.\n| The size must meet the following restrictions:\n\n-  The size must be less than or equal to the maximum waveform size that\n   the device allows.\n-  The size must be greater than or equal to the minimum waveform size\n   that the device allows.\n-  The size must be an integer multiple of the device waveform quantum.\n\nYou can obtain these values from the **maximumWaveformSize**,\n**minimumWaveformSize**, and **waveformQuantum** parameters of the\nnifgen_QueryArbWfmCapabilities function.\n\n| ****Default Value**:** None\n'
                },
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data you want to use for the new arbitrary\nwaveform. The array must have at least as many elements as the value\nthat you specify in **waveformSize**.\n\nYou must normalize the data points in the array to be between –1.00 and\n+1.00.\n\n**Default Value**: None\n'
                },
                'name': 'waveformDataArray',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'waveformSize'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe handle that identifies the new waveform. This handle is used later\nwhen referring to this waveform.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateWaveformFromFileF64': {
        'documentation': {
            'description': '\nThis function takes the floating point double (F64) data from the\nspecified file and creates an onboard waveform for use in Arbitrary\nWaveform or Arbitrary Sequence output mode. The **waveformHandle**\nreturned by this function can later be used for setting the active\nwaveform, changing the data in the waveform, building sequences of\nwaveforms, or deleting the waveform when it is no longer needed.\n',
            'note': '\nThe F64 data must be between –1.0 and +1.0 V. Use the\nNIFGEN_ATTR_DIGITAL_GAIN attribute to generate different voltage\noutputs.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to create the waveform.\n\n**Defined Value**: "0"\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The full path and name of the file where the waveform data resides.'
                },
                'name': 'fileName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the byte order of the data in the file.\n\n****Defined Values****\n\n| \n| ****Default Value**:** NIFGEN_VAL_LITTLE_ENDIAN\n',
                    'note': '\nData written by most applications in Windows (including\nLabWindows™/CVI™) is in Little Endian format. Data written to a file\nfrom LabVIEW is in Big Endian format by default on all platforms. Big\nEndian and Little Endian refer to the way data is stored in memory,\nwhich can differ on different processors.\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_LITTLE_ENDIAN',
                            'Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance.'
                        ],
                        [
                            'NIFGEN_VAL_BIG_ENDIAN',
                            'Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.'
                        ]
                    ]
                },
                'enum': 'ByteOrder',
                'name': 'byteOrder',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe handle that identifies the new waveform. This handle is used later\nwhen referring to this waveform.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateWaveformFromFileHws': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\n| Takes the waveform data from the specified HWS (Hierarchical Waveform\n  Storage) file and creates an onboard waveform for use in Arbitrary\n  Waveform or Arbitrary Sequence output mode. The **waveformHandle**\n  returned by this function can be used later for setting the active\n  waveform, changing the data in the waveform, building sequences of\n  waveforms, or deleting the waveform when it is no longer needed.\n| When the Analog Waveform Editor saves data in an HWS file, it also\n  stores the rate, gain, and offset with the data. If the\n  **useRateFromWaveform** and **useGain&OffsetFromWaveform;** parameters\n  are set to VI_TRUE, this function also sets those properties.\n\n|\n',
            'note': '\nIf you choose to have this function set the gain and offset properties\nfor you, you should **not** use the niFgen_ConfigureArbWaveform or\nniFgen_ConfigureArbSequence functions, as they also set the gain and\noffset, thereby overriding the values set by this function. Instead, use\nthe NIFGEN_ATTR_ARB_WAVEFORM_HANDLE or\nNIFGEN_ATTR_ARB_SEQUENCE_HANDLE attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to create the waveform.\n\n**Defined Value**: "0"\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The full path and name of the file where the waveform data resides.'
                },
                'name': 'fileName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\n| If you set this parameter input to VI_TRUE and if onboard signal\n  processing (OSP) is enabled, the rate from the waveform is interpreted\n  as the data rate, and FGEN sets the data rate attribute for you. In\n  all other cases, it is interpreted as the sample rate, and FGEN sets\n  the sample rate attribute for you.\n\n****Defined Values****\n\n| \n| ****Default Value**:** VI_TRUE\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'Use rate from waveform.'
                        ],
                        [
                            'VI_FALSE',
                            'Do not use rate from waveform.'
                        ]
                    ]
                },
                'name': 'useRateFromWaveform',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\n| If this input is set to VI_TRUE, NI-FGEN retrieves the gain and\n  offset values from the specified HWS file and applies them to the\n  NI-FGEN driver.\n\n****Defined Values****\n\n| \n| ****Default Value**:** VI_TRUE\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'Use gain and offset from waveform.'
                        ],
                        [
                            'VI_FALSE',
                            'Do not use gain and offset from waveform.'
                        ]
                    ]
                },
                'name': 'useGainAndOffsetFromWaveform',
                'type': 'ViBoolean'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe handle that identifies the new waveform. This handle is used later\nwhen referring to this waveform.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateWaveformFromFileI16': {
        'documentation': {
            'description': '\nTakes the binary 16-bit signed integer (I16) data from the specified\nfile and creates an onboard waveform for use in Arbitrary Waveform or\nArbitrary Sequence output mode. The **waveformHandle** returned by this\nfunction can later be used for setting the active waveform, changing the\ndata in the waveform, building sequences of waveforms, or deleting the\nwaveform when it is no longer needed.\n',
            'note': '\nThe I16 data (values between –32768 and +32767) is assumed to\nrepresent –1 to +1 V. Use the NIFGEN_ATTR_DIGITAL_GAIN attribute to\ngenerate different voltage outputs.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to create the waveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The full path and name of the file where the waveform data resides.'
                },
                'name': 'fileName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the byte order of the data in the file.\n\n****Defined Values****\n\n| \n| ****Default Value**:** NIFGEN_VAL_LITTLE_ENDIAN\n',
                    'note': '\nData written by most applications in Windows (including\nLabWindows™/CVI™) is in Little Endian format. Data written to a file\nfrom LabVIEW is in Big Endian format by default on all platforms. Big\nEndian and Little Endian refer to the way data is stored in memory,\nwhich can differ on different processors.\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_LITTLE_ENDIAN',
                            'Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance.'
                        ],
                        [
                            'NIFGEN_VAL_BIG_ENDIAN',
                            'Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.'
                        ]
                    ]
                },
                'enum': 'ByteOrder',
                'name': 'byteOrder',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe handle that identifies the new waveform. This handle is used later\nwhen referring to this waveform.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateWaveformI16': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCreates an onboard waveform from binary 16-bit signed integer (I16) data\nfor use in Arbitrary Waveform or Arbitrary Sequence output mode. The\n**waveformHandle** returned can later be used for setting the active\nwaveform, changing the data in the waveform, building sequences of\nwaveforms, or deleting the waveform when it is no longer needed.\n',
            'note': '\nYou must call the nifgen_ConfigureOutputMode function to set the\n**outputMode** parameter to NIFGEN_VAL_OUTPUT_ARB or\nNIFGEN_VAL_OUTPUT_SEQ before calling this function.\n'
        },
        'method_name_for_documentation': 'create_waveform',
        'method_templates': [
            {
                'method_python_name_suffix': '_numpy',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to create the waveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\n| Specifies the size of the arbitrary waveform that you want to create.\n| The size must meet the following restrictions:\n\n-  The size must be less than or equal to the maximum waveform size that\n   the device allows.\n-  The size must be greater than or equal to the minimum waveform size\n   that the device allows.\n-  The size must be an integer multiple of the device waveform quantum.\n\nYou can obtain these values from the **maximumWaveformSize**,\n**minimumWaveformSize**, and **waveformQuantum** parameters of the\nnifgen_QueryArbWfmCapabilities function.\n\n| \n| ****Default Value**:** None\n'
                },
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecify the array of data that you want to use for the new arbitrary\nwaveform. The array must have at least as many elements as the value\nthat you specify in the Waveform Size parameter.\nYou must normalize the data points in the array to be between -32768 and\n+32767.\n****Default Value**:** None\n'
                },
                'name': 'waveformDataArray',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'waveformSize'
                },
                'type': 'ViInt16[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe handle that identifies the new waveform. This handle is used later\nwhen referring to this waveform.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'DefineUserStandardWaveform': {
        'documentation': {
            'description': '\nDefines a user waveform for use in either Standard Function or Frequency\nList output mode.\n\nTo select the waveform, set the **waveform** parameter to\nNIFGEN_VAL_WFM_USER with either the nifgen_ConfigureStandardWaveform\nor the nifgen_CreateFreqList function.\n\nThe waveform data must be scaled between –1.0 and 1.0. Use the\n**amplitude** parameter in the niFgen_ConfigureStandardWaveform\nfunction to generate different output voltages.\n',
            'note': '\nYou must call the nifgen_ConfigureOutputMode function to set the\n**outputMode** parameter to NIFGEN_VAL_OUTPUT_FUNC or\nNIFGEN_VAL_OUTPUT_FREQ_LIST before calling this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to define a user standard\nwaveform.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size of the waveform in samples.\n**Default Value**: 16384\n'
                },
                'name': 'waveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data you want to use for the new arbitrary\nwaveform. The array must have at least as many elements as the value\nthat you specify in **waveformSize**.\n\nYou must normalize the data points in the array to be between –1.00 and\n+1.00.\n\n**Default Value**: None\n'
                },
                'name': 'waveformDataArray',
                'size': {
                    'mechanism': 'len',
                    'value': 'waveformSize'
                },
                'type': 'ViReal64[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteNamedWaveform': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nRemoves a previously created arbitrary waveform from the signal\ngenerator memory and invalidates the waveform handle.\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\n'
        },
        'method_name_for_documentation': 'delete_waveform',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel onto which the named waveform is loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name to associate with the allocated waveform.'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteScript': {
        'documentation': {
            'description': 'Deletes the specified script from onboard memory.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel onto which the script is loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the script you want to delete. The script name\nappears in the text of the script following the script keyword.\n'
                },
                'name': 'scriptName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteWaveformDispatch': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Removes a previously created arbitrary waveform from the signal generator memory.',
            'note': 'The signal generator must not be in the Generating state when you call this function.'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'delete_waveform'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. **vi** is obtained from niFgen_InitializeWithChannels function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the channel onto which the named waveform is loaded.'
                },
                'name': 'channelName',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The name (str) or handle (int) of an arbitrary waveform previously allocated with niFgen_AllocateNamedWaveform, niFgen_AllocateWaveform or niFgen_CreateWaveformF64.'
                },
                'name': 'waveformNameOrHandle',
                'type': 'ViInt32',
                'type_in_documentation': 'str or int'
            }
        ],
        'python_name': 'delete_waveform',
        'returns': 'ViStatus'
    },
    'Disable': {
        'documentation': {
            'description': '\nPlaces the instrument in a quiescent state where it has minimal or no\nimpact on the system to which it is connected. The analog output and all\nexported signals are disabled.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableAllSparseMarkers': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableAnalogFilter': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nDisables the analog filter. This function sets the\nNIFGEN_ATTR_ANALOG_FILTER_ENABLED attribute to VI_FALSE. This\nsetting can be applied in Arbitrary Waveform, Arbitrary Sequence, or\nScript output modes. You also can use this setting in Standard Function\nand Frequency List output modes for user-defined waveforms.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to disable the analog\nfilter.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableDigitalFilter': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nDisables the digital filter. This function sets the\nNIFGEN_ATTR_DIGITAL_FILTER_ENABLED attribute to VI_FALSE. This\nsetting can be applied in Arbitrary Waveform, Arbitrary Sequence, or\nScript output modes. You also can use this setting in Standard Function\nand Frequency List output modes for user-defined waveforms.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to disable the digital\nfilter.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableDigitalPatterning': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nDisables digital pattern output on the signal generator. This function\nsets the NIFGEN_ATTR_DIGITAL_PATTERN_ENABLED attribute to VI_FALSE.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to disable digital pattern\noutput.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableOutput': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisablePauseTrigger': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableScriptTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Disables the specified Script Trigger.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Script Trigger used for triggering.\n\n**Defined Values**\n\n**Default Value**: "ScriptTrigger0"\n',
                    'table_body': [
                        [
                            '"ScriptTrigger0"',
                            'Script Trigger 0'
                        ],
                        [
                            '"ScriptTrigger1"',
                            'Script Trigger 1'
                        ],
                        [
                            '"ScriptTrigger2"',
                            'Script Trigger 2'
                        ],
                        [
                            '"ScriptTrigger3"',
                            'Script Trigger 3'
                        ]
                    ]
                },
                'name': 'triggerId',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableStartTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Disables the Start Trigger.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnableAnalogFilter': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the analog filter for the device. This function sets the\nNIFGEN_ATTR_ANALOG_FILTER_ENABLED attribute to VI_TRUE. This\nsetting can be applied in Arbitrary Waveform, Arbitrary Sequence, or\nScript output modes. You also can use this setting in Standard Function\nand Frequency List output modes for user-defined waveforms.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to enable the analog\nfilter.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the filter correction frequency of the analog filter. On the\nNI 5411 and NI 5431, NI-FGEN adjusts signal amplitude to compensate for\nthe filter attenuation at that frequency. To disable amplitude\ncorrection, set **filterCorrectionFrequency** to 0. For Standard\nFunction output mode, **filterCorrectionFrequency** typically should be\nset to the same value as the frequency of the standard waveform.\n\n**Units**: hertz\n\n**Default Value**: 0\n'
                },
                'name': 'filterCorrectionFrequency',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnableDigitalFilter': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEnables the digital filter by setting the\nNIFGEN_ATTR_DIGITAL_FILTER_ENABLED attribute to VI_TRUE. This\nsetting can be applied in Arbitrary Waveform, Arbitrary Sequence, or\nScript output modes. You also can use this setting in Standard Function\nand Frequency List output modes for user-defined waveforms.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to enable the digital\nfilter.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnableDigitalPatterning': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEnables digital pattern output on the signal generator. This function\nsets the NIFGEN_ATTR_DIGITAL_PATTERN_ENABLED attribute to VI_TRUE.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to enable the digital\npattern output.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnableOutput': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ErrorHandler': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConverts a status code returned by an NI-FGEN function into a\nuser-readable string and returns any error elaborations.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init or the niFgen_InitWithOptions functions and identifies a\nparticular instrument session.\n\nYou can pass VI_NULL for this parameter. Passing VI_NULL is useful\nwhen one of the initialize functions fails.\n\n**Default Value**: VI_NULL\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **status** parameter that is returned from any of the\nNI-FGEN functions.\n\n**Default Value**: 0 (VI_SUCCESS)\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the error message string read from the instrument error message\nqueue.\n\nYou must pass a ViChar array with at least 256 bytes.\n'
                },
                'name': 'errorMessage',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationFile': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportSignal': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nRoutes signals (clocks, triggers, and events) to the output terminal you\nspecify.\n\nAny routes created within a session persist after the session closes to\nprevent signal glitching. To unconfigure signal routes created in\nprevious sessions, set **resetDevice** in the niFgen_init function to\nVI_TRUE or use the niFgen_ResetDevice function.\n\nIf you export a signal with this function and commit the session, the\nsignal is routed to the output terminal you specify.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the source of the signal to route.\n****Defined Values****\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK',
                            'Onboard 10 MHz synchronization clock (PCI only)'
                        ],
                        [
                            'NIFGEN_VAL_SYNC_OUT',
                            'SYNC OUT signal The SYNC OUT signal is normally generated on the SYNC OUT front panel connector.'
                        ],
                        [
                            'NIFGEN_VAL_START_TRIGGER',
                            'Start Trigger'
                        ],
                        [
                            'NIFGEN_VAL_MARKER_EVENT',
                            'Marker Event'
                        ],
                        [
                            'NIFGEN_VAL_SAMPLE_CLOCK_TIMEBASE',
                            'The clock from which the Sample Clock is derived'
                        ],
                        [
                            'NIFGEN_VAL_SYNCHRONIZATION',
                            'Synchronization strobe (NI 5404/5411/5431 only) A synchronization strobe is used to guarantee absolute synchronization between two or more signal generators.'
                        ],
                        [
                            'NIFGEN_VAL_SAMPLE_CLOCK',
                            'Sample Clock'
                        ],
                        [
                            'NIFGEN_VAL_REFERENCE_CLOCK',
                            'PLL Reference Clock'
                        ],
                        [
                            'NIFGEN_VAL_SCRIPT_TRIGGER',
                            'Script Trigger'
                        ],
                        [
                            'NIFGEN_VAL_READY_FOR_START_EVENT',
                            'Ready For Start Event'
                        ],
                        [
                            'NIFGEN_VAL_STARTED_EVENT',
                            'Started Event'
                        ],
                        [
                            'NIFGEN_VAL_DONE_EVENT',
                            'Done Event'
                        ],
                        [
                            'NIFGEN_VAL_DATA_MARKER_EVENT',
                            'Data Marker Event'
                        ]
                    ]
                },
                'name': 'signal',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies which instance of the selected signal to export.\n****Defined Values****\n',
                    'table_body': [
                        [
                            '"" (empty string)',
                            'Default (for non instance-based signals)'
                        ],
                        [
                            '"ScriptTrigger0"',
                            'Script Trigger 0'
                        ],
                        [
                            '"ScriptTrigger1"',
                            'Script Trigger 1'
                        ],
                        [
                            '"ScriptTrigger2"',
                            'Script Trigger 2'
                        ],
                        [
                            '"ScriptTrigger3"',
                            'Script Trigger 3'
                        ],
                        [
                            '"Marker0"',
                            'Marker 0'
                        ],
                        [
                            '"Marker1"',
                            'Marker 1'
                        ],
                        [
                            '"Marker2"',
                            'Marker 2'
                        ],
                        [
                            '"Marker3"',
                            'Marker 3'
                        ],
                        [
                            '"DataMarker0"',
                            'Data Marker 0\\*'
                        ],
                        [
                            '"DataMarker1"',
                            'Data Marker 1\\*'
                        ],
                        [
                            '"DataMarker2"',
                            'Data Marker 2\\*'
                        ],
                        [
                            '"DataMarker3"',
                            'Data Marker 3\\*'
                        ],
                        [
                            '\\* These Data Marker values apply only to single-channel devices or to multichannel devices that are configured for single-channel operation. When using a device that is configured for multichannel operation, specify the channel number along with the signal identifier. For example, to export Data Marker 0 on channel 1 of a device configured for multichannel operation, use the value "1/ DataMarker0." If you do not specify a channel when using a device configured for multichannel generation, DataMarker0 generates on all channels.'
                        ]
                    ]
                },
                'name': 'signalIdentifier',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output terminal to export the signal.\n****Defined Values****\n',
                    'note': '\nThe following **Defined Values** are examples of possible output\nterminals. For a complete list of the output terminals available on your\ndevice, refer to the Routes topic for your device or the **Device\nRoutes** tab in MAX.\n',
                    'table_body': [
                        [
                            '"" (empty string)',
                            'Do not export signal'
                        ],
                        [
                            '"PFI0"',
                            'PFI line 0'
                        ],
                        [
                            '"PFI1"',
                            'PFI line 1'
                        ],
                        [
                            '"PFI4"',
                            'PFI line 4'
                        ],
                        [
                            '"PFI5"',
                            'PFI line 5'
                        ],
                        [
                            '"PXI_Trig0"',
                            'PXI or RTSI line 0'
                        ],
                        [
                            '"PXI_Trig1"',
                            'PXI or RTSI line 1'
                        ],
                        [
                            '"PXI_Trig2"',
                            'PXI or RTSI line 2'
                        ],
                        [
                            '"PXI_Trig3"',
                            'PXI or RTSI line 3'
                        ],
                        [
                            '"PXI_Trig4"',
                            'PXI or RTSI line 4'
                        ],
                        [
                            '"PXI_Trig5"',
                            'PXI or RTSI line 5'
                        ],
                        [
                            '"PXI_Trig6"',
                            'PXI or RTSI line 6'
                        ],
                        [
                            '"PXI_Trig7"',
                            'PXI or RTSI line 7'
                        ],
                        [
                            '"DDC_ClkOut"',
                            'Clock out from DDC connector'
                        ],
                        [
                            '"PXI_Star"',
                            'PXI star trigger line'
                        ]
                    ]
                },
                'name': 'outputTerminal',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'FreeServer': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViBoolean attribute.\n\nYou can use this function to get the values of instrument-specific\nattributes and inherent IVI attributes. If the attribute represents an\ninstrument state, this function performs instrument I/O in the following\ncases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or an empty string ("").\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViBoolean variable.\n'
                },
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViInt32 attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes. If the attribute represents an instrument state, this\nfunction performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or an empty string ("").\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViInt32 variable.\n'
                },
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt64': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nQueries the value of a ViInt64 attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes. If the attribute represents an instrument state, this\nfunction performs instrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or an empty string ("").\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViInt64 variable.\n'
                },
                'name': 'attributeValue',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViReal64 attribute.\n\nYou can use this function to get the values of instrument-specific\nattributes and inherent IVI attributes. If the attribute represents an\ninstrument state, this function performs instrument I/O in the following\ncases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or an empty string ("").\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViReal64 variable.\n'
                },
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViSession': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nQueries the value of a ViSession attribute.\n\nYou can use this function to get the values of instrument-specific\nattributes and inherent IVI attributes. If the attribute represents an\ninstrument state, this function performs instrument I/O in the following\ncases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or an empty string ("").\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Pass the address of a\nViSession variable.\n'
                },
                'name': 'attributeValue',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViString attribute.\n\nYou can use this function to get the values of instrument-specific\nattributes and inherent IVI attributes. If the attribute represents an\ninstrument state, this function performs instrument I/O in the following\ncases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid.\n\nYou must provide a ViChar array to serve as a buffer for the value. You\npass the number of bytes in the buffer as the **arraySize** parameter.\nIf the current value of the attribute, including the terminating NUL\nbyte, is larger than the size you indicate in the **arraySize**\nparameter, the function copies **arraySize** – 1 bytes into the buffer,\nplaces an ASCII NUL byte at the end of the buffer, and returns the array\nsize you must pass to get the entire value. For example, if the value is\n123456 and **arraySize** is 4, the function places 123 into the buffer\nand returns 7.\n\nIf you want to call this function just to get the required array size,\nyou can pass 0 for **arraySize** and VI_NULL for the **attributeValue**\nbuffer.\n\nIf you want the function to fill in the buffer regardless of the number\nof bytes in the value, pass a negative number for the **arraySize**\nparameter.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or an empty string ("").\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of bytes in the ViChar array you specify for the\n**attributeValue** parameter.\n\nIf the current value of the attribute, including the terminating NUL\nbyte, contains more bytes than you indicate in this parameter, the\nfunction copies **arraySize** – 1 bytes into the buffer, places an ASCII\nNUL byte at the end of the buffer, and returns the array size you must\npass to get the entire value. For example, if the value is 123456 and\n**arraySize** is 4, the function places 123 into the buffer and returns\n7.\n\nIf you pass a negative number, the function copies the value to the\nbuffer regardless of the number of bytes in the value.\n\nIf you pass 0, you can pass VI_NULL for the **attributeValue** buffer\nparameter.\n'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe buffer in which the function returns the current value of the\nattribute. The buffer must be a ViChar data type and have at least as\nmany bytes as indicated in the **arraySize** parameter.\n\nIf the current value of the attribute, including the terminating NUL\nbyte, contains more bytes than you indicate in this parameter, the\nfunction copies **arraySize** – 1 bytes into the buffer, places an ASCII\nNUL byte at the end of the buffer, and returns the array size you must\npass to get the entire value. For example, if the value is 123456 and\n**arraySize** is 4, the function places 123 into the buffer and returns\n7.\n\nIf you specify 0 for the **arraySize** parameter, you can pass VI_NULL\nfor this parameter.\n'
                },
                'name': 'attributeValue',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'arraySize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeWithOptionsViBoolean': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'retrievalMode',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeWithOptionsViInt32': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'retrievalMode',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeWithOptionsViInt64': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'retrievalMode',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeWithOptionsViReal64': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'retrievalMode',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeWithOptionsViSession': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'retrievalMode',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeWithOptionsViString': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'name': 'retrievalMode',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'bufSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'value',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCalUserDefinedInfo': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nRetrieves user-defined information from the onboard EEPROM. Call the\nnifgen_GetCalUserDefinedInfoMaxSize function to determine the number of\ncharacters that can be retrieved. The buffer you provide should be the\nsize of the maximum number of characters stored plus one termination\ncharacter.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_init or the nifgen_InitExtCal function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies a string into which the user information is copied. This\nparameter must point to a character buffer large enough to hold the\ninformation string.\n'
                },
                'name': 'info',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCalUserDefinedInfoMaxSize': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the maximum number of characters, excluding the termination\ncharacter, of user-defined information that can be stored in the onboard\nEEPROM.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_init or the nifgen_InitExtCal function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSpecifies the maximum number of characters of user defined info that can\nbe stored in the onboard EEPROM.\n'
                },
                'name': 'infoSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetChannelName': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'name',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetDaQmxTask': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'taskId',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'sizeOfString',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'stringHandle',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the error information associated with an IVI session or with the\ncurrent execution thread. If you specify a valid IVI session for the\n**vi** parameter, this function retrieves and then clears the error\ninformation for the session. If you pass VI_NULL for the **vi**\nparameter, this function retrieves and then clears the error information\nfor the current execution thread.\n\nThe IVI Engine also maintains this error information separately for each\nthread. This feature is useful if you do not have a session handle to\npass to the niFgen_GetError or nifgen_ClearError functions. This\nsituation occurs when a call to the nifgen_init or\nnifgen_InitWithOptions function fails.\n'
        },
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init or the nifgen_InitWithOptions functions and identifies a\nparticular instrument session.\n\nYou can pass VI_NULL for this parameter. Passing VI_NULL is useful\nwhen one of the initialize functions fail.\n\n**Default Value**: VI_NULL\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe error code for the session or execution thread.\n\nA value of VI_SUCCESS (0) indicates that no error occurred. A positive\nvalue indicates a warning. A negative value indicates an error.\n\nYou can call nifgen_error_message to get a text description of the\nvalue.\n\nIf you are not interested in this value, you can pass VI_NULL.\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size of the **errorDescription** array.\n\nYou can determine the array size needed to store the entire error\ndescription by setting this parameter to 0. The function then ignores\nthe **errorDescription** buffer, which may be set to VI_NULL, and gives\nas its return value the required buffer size. You can then call the\nfunction a second time using the correct buffer size.\n'
                },
                'name': 'errorDescriptionBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe error description string for the session or execution thread. If the\nerror code is nonzero, the description string can further describe the\nerror or warning condition.\n\nIf you are not interested in this value, you can pass VI_NULL.\nOtherwise, you must pass a ViChar array of a size specified with the\n**errorDescriptionBufferSize** parameter.\n'
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
    'GetErrorInfo': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'primaryError',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'name': 'secondaryError',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'name': 'errorElaboration',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalLastDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the date and time of the last successful external calibration.\nThe time returned is 24-hour (military) local time; for example, if the\ndevice was calibrated at 2:30 PM, this function returns 14 for the\n**hour** parameter and 30 for the **minute** parameter.\n'
        },
        'method_name_for_documentation': 'get_ext_cal_last_date_and_time',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_init or the nifgen_InitExtCal function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the year of the last successful calibration.'
                },
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the month of the last successful calibration.'
                },
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the day of the last successful calibration.'
                },
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the hour of the last successful calibration.'
                },
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the minute of the last successful calibration.'
                },
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalLastTemp': {
        'documentation': {
            'description': '\nReturns the temperature at the last successful external calibration. The\ntemperature is returned in degrees Celsius.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_init or the nifgen_InitExtCal function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSpecifies the temperature at the last successful calibration in degrees\nCelsius.\n'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalRecommendedInterval': {
        'documentation': {
            'description': '\nReturns the recommended interval between external calibrations in\nmonths.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_init or the nifgen_InitExtCal function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSpecifies the recommended interval between external calibrations in\nmonths.\n'
                },
                'name': 'months',
                'python_api_converter_name': 'convert_month_to_timedelta',
                'type': 'ViInt32',
                'type_in_documentation': 'datetime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetFIRFilterCoefficients': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\n| Returns the FIR filter coefficients used by the onboard signal\n  processing block. These coefficients are determined by NI-FGEN and\n  based on the FIR filter type and corresponding attribute (Alpha,\n  Passband, BT) unless you are using the custom filter. If you are using\n  a custom filter, the coefficients returned are those set with the\n  nifgen_ConfigureCustomFIRFilterCoefficients function coerced to the\n  quantized values used by the device.\n| To use this function, first call an instance of the\n  niFgen_GetFIRFilterCoefficients function with the\n  **coefficientsArray** parameter set to VI_NULL. Calling the function\n  in this state returns the current size of the **coefficientsArray** as\n  the value of the **numberOfCoefficientsRead** parameter. Create an\n  array of this size, and call the niFgen_GetFIRFilterCoefficients\n  function a second time, passing the new array as the\n  **coefficientsArray** parameter and the size as the **arraySize**\n  parameter. This second function call populates the array with the FIR\n  filter coefficients.\n| Refer to the FIR Filter topic for your device in the *NI Signal\n  Generators Help* for more information about FIR filter coefficients.\n  This function is supported only for the NI 5441.\n| **Default Value**: None\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to configure the operation\nmode.\n\n**Defined Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the size of the coefficient array'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data the onboard signal processor uses for the\nFIR filter coefficients. For the NI 5441, provide a symmetric array of\n95 coefficients to this parameter. The array must have at least as many\nelements as the value that you specify in the **numberOfCoefficients**\nparameter in this function.\nThe coefficients should range between –1.00 and +1.00.\n'
                },
                'name': 'coefficientsArray',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data containing the number of coefficients you\nwant to read.\n'
                },
                'name': 'numberOfCoefficientsRead',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetHardwareState': {
        'documentation': {
            'description': '\nReturns the current hardware state of the device and, if the device is\nin the hardware error state, the current hardware error.\n',
            'note': 'Hardware states do not necessarily correspond to NI-FGEN states.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the hardware state of the signal generator.\n\n**Defined Values**\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_IDLE',
                            'The device is in the Idle state.'
                        ],
                        [
                            'NIFGEN_VAL_WAITING_FOR_START_TRIGGER',
                            'The device is waiting for Start Trigger.'
                        ],
                        [
                            'NIFGEN_VAL_RUNNING',
                            'The device is in the Running state.'
                        ],
                        [
                            'NIFGEN_VAL_DONE',
                            'The generation has completed successfully.'
                        ],
                        [
                            'NIFGEN_VAL_HARDWARE_ERROR',
                            'There is a hardware error.'
                        ]
                    ]
                },
                'enum': 'HardwareState',
                'name': 'state',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetLastExtCalLastDateAndTime': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the date and time of the last successful external calibration. The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30 PM, this function returns 14 for the **hour** parameter and 30 for the **minute** parameter.'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'datetime_wrappers'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. **vi** is obtained from the nifgen_init or the nifgen_InitExtCal function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates date and time of the last calibration.'
                },
                'name': 'month',
                'type': 'datetime.datetime'
            }
        ],
        'python_name': 'get_ext_cal_last_date_and_time',
        'real_datetime_call': 'GetExtCalLastDateAndTime',
        'returns': 'ViStatus'
    },
    'GetLastSelfCalLastDateAndTime': {
        'codegen_method': 'public',
        'documentation': {
            'description': 'Returns the date and time of the last successful self-calibration.'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'datetime_wrappers'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. **vi** is obtained from the nifgen_init or the nifgen_InitExtCal function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the date and time the device was last calibrated.'
                },
                'name': 'month',
                'type': 'datetime.datetime'
            }
        ],
        'python_name': 'get_self_cal_last_date_and_time',
        'real_datetime_call': 'GetSelfCalLastDateAndTime',
        'returns': 'ViStatus'
    },
    'GetNextCoercionRecord': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the coercion information associated with the IVI session. This\nfunction retrieves and clears the oldest instance in which the NI-FGEN\ncoerced a value you specified to another value.\n\nIf you set the NIFGEN_ATTR_RECORD_COERCIONS attribute to VI_TRUE,\nNI-FGEN keeps a list of all coercions it makes on ViInt32 or ViReal64\nvalues that you pass to NI-FGEN functions. You use this function to\nretrieve information from that list.\n\nIf the next coercion record string, including the terminating NUL byte,\ncontains more bytes than you indicate in this parameter, the function\ncopies **bufferSize** – 1 bytes into the buffer, places an ASCII NUL\nbyte at the end of the buffer, and returns the buffer size you must pass\nto get the entire value. For example, if the value is 123456 and\n**bufferSize** is 4, the function places 123 into the buffer and returns\n7.\n\nIf you pass a negative number, the function copies the value to the\nbuffer regardless of the number of bytes in the value.\n\nIf you pass 0, you can pass VI_NULL for the **coercionRecord** buffer\nparameter.\n\nThe function returns an empty string in the **coercionRecord** parameter\nif no coercion records remain for the session.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of bytes in the ViChar array you specify for the\n**coercionRecord** parameter.\n\nIf the next coercion record string, including the terminating NUL byte,\ncontains more bytes than you indicate in this parameter, the function\ncopies **bufferSize** – 1 bytes into the buffer, places an ASCII NUL\nbyte at the end of the buffer, and returns the buffer size that you must\npass to get the entire value. For example, if the value is 123456 and\nthe buffer size is 4, the function places 123 into the buffer and\nreturns 7.\n\nIf you pass a negative number, the function copies the value to the\nbuffer regardless of the number of bytes in the value.\n\nIf you pass 0, you can pass VI_NULL for the **coercionRecord** buffer\nparameter.\n\n**Default Value**: None\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the next coercion record for the IVI session. If there are no\ncoercion records, the function returns an empty string.\n\nThe buffer must contain at least as many elements as the value you\nspecify with the **bufferSize** parameter. If the next coercion record\nstring, including the terminating NUL byte, contains more bytes than you\nindicate with the **bufferSize** parameter, the function copies\n**bufferSize** – 1 bytes into the buffer, places an ASCII NUL byte at\nthe end of the buffer, and returns the buffer size that you must pass to\nget the entire value. For example, if the value is "123456" and\n**bufferSize** is 4, the function places "123" into the buffer and\nreturns 7.\n\nThis parameter returns an empty string if no coercion records remain for\nthe session.\n'
                },
                'name': 'coercionRecord',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetNextInterchangeWarning': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the interchangeability warnings associated with the IVI session.\nIt retrieves and clears the oldest instance in which the class driver\nrecorded an interchangeability warning. Interchangeability warnings\nindicate that using your application with a different instrument might\ncause different behavior. Use this function to retrieve\ninterchangeability warnings.\n\nNI-FGEN performs interchangeability checking when the\nNIFGEN_ATTR_INTERCHANGE_CHECK attribute is set to VI_TRUE.\n\nThe function returns an empty string in the **interchangeWarning**\nparameter if no interchangeability warnings remain for the session.\n\nIn general, NI-FGEN generates interchangeability warnings when an\nattribute that affects the behavior of the instrument is in a state that\nyou did not specify.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of bytes in the ViChar array you specify for the\n**interchangeWarning** parameter.\n\nIf the next interchangeability warning string, including the terminating\nNUL byte, contains more bytes than you indicate in this parameter, the\nfunction copies **bufferSize** – 1 bytes into the buffer, places an\nASCII NUL byte at the end of the buffer, and returns the buffer size\nthat you must pass to get the entire value. For example, if the value is\n123456 and **bufferSize** is 4, the function places 123 into the buffer\nand returns 7.\n\nIf you pass a negative number, the function copies the value to the\nbuffer regardless of the number of bytes in the value.\n\nIf you pass 0, you can pass VI_NULL for the **interchangeWarning**\nbuffer parameter.\n\n**Default Value**: None\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the next interchange warning for the IVI session. If there are\nno interchange warnings, the function returns an empty string.\n\nThe buffer must contain at least as many elements as the value you\nspecify with the **bufferSize** parameter. If the next\ninterchangeability warning string, including the terminating NUL byte,\ncontains more bytes than you indicate with the **bufferSize** parameter,\nthe function copies **bufferSize** – 1 bytes into the buffer, places an\nASCII NUL byte at the end of the buffer, and returns the buffer size\nthat you must pass to get the entire value. For example, if the value is\n123456 and **bufferSize** is 4, the function places 123 into the buffer\nand returns 7.\n\nThis parameter returns an empty string if no interchangeability warnings\nremain for the session.\n'
                },
                'name': 'interchangeWarning',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetOpenSessionsInformation': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'name': 'infoJson',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViUInt64'
            },
            {
                'direction': 'out',
                'name': 'bufferSizeNeededInBytes',
                'type': 'ViUInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalLastDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the date and time of the last successful self-calibration.\n\nAll values are returned as separate parameters. Each parameter is\nreturned as an integer, including the year, month, day, hour, minute,\nand second. For example, if the device is calibrated in September 2013,\nthis function returns 9 for the **month** parameter and 2013 for the\n**year** parameter.\n\nThe time returned is 24-hour (military) local time. For example, if the\ndevice was calibrated at 2:30 PM, this function returns 14 for the\n**hours** parameter and 30 for the **minutes** parameter.\n'
        },
        'method_name_for_documentation': 'get_self_cal_last_date_and_time',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_init or the nifgen_InitExtCal function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the year of the last successful calibration.'
                },
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the month of the last successful calibration.'
                },
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the day of the last successful calibration.'
                },
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the hour of the last successful calibration.'
                },
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Specifies the minute of the last successful calibration.'
                },
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalLastTemp': {
        'documentation': {
            'description': '\nReturns the temperature at the last successful self-calibration. The\ntemperature is returned in degrees Celsius.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_init or the nifgen_InitExtCal function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSpecifies the temperature at the last successful calibration in degrees\nCelsius.\n'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalSupported': {
        'documentation': {
            'description': 'Returns whether the device supports self–calibration.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_init or the nifgen_InitWithOptions function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns whether the device supports self-calibration.\n\n****Defined Values****\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'Self–calibration is supported.'
                        ],
                        [
                            'VI_FALSE',
                            'Self–calibration is not supported.'
                        ]
                    ]
                },
                'name': 'selfCalSupported',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSparseMarkerIndexes': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'name',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'indexesArraySize',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'indexes',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViInt64'
            },
            {
                'direction': 'out',
                'name': 'indexesActualSize',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSparseMarkerName': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'nameBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'name',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetStreamEndpointHandle': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns a reader endpoint handle that can be used with NI-P2P to\nconfigure a peer-to-peer stream with a signal generator endpoint.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the stream endpoint FIFO to configure. Refer to the\ndevice-specific documentation for peer-to-peer streaming in the *NI\nSignal Generators Help* for more information.\n'
                },
                'name': 'streamEndpoint',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSpecifies the reader endpoint handle that is used with NI-P2P to create\na stream with the signal generator as an endpoint.\n'
                },
                'name': 'readerHandle',
                'type': 'void'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationFile': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitExtCal': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCreates and initializes a special NI-FGEN external calibration session.\nThe ViSession returned is an NI-FGEN session that can be used to\nconfigure the device using normal attributes and functions. However,\nflags have been set that allow you to program an external calibration\nprocedure using the special calibration attributes and functions. The\nNI 5401/5404/5411/5431 have different calibration functions. Refer to\nthe nifgen_Related_Documentation for the signal generator for more\ninformation.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'caution': '\nTraditional NI-DAQ and NI-DAQmx device names are not case-sensitive.\nHowever, all IVI names, such as logical names, are case-sensitive. If\nyou use logical names, driver session names, or virtual names in your\nprogram, you must ensure that the name you use matches the name in the\nIVI Configuration Store file exactly, without any variations in the case\nof the characters.\n',
                    'description': '\n| Specifies the resource name of the device to initialize.\n\nFor Traditional NI-DAQ devices, the syntax is DAQ::\\ *n*, where *n* is\nthe device number assigned by MAX, as shown in Example 1.\n\nFor NI-DAQmx devices, the syntax is just the device name specified in\nMAX, as shown in Example 2. Typical default names for NI-DAQmx devices\nin MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by\nright-clicking on the name in MAX and entering a new name.\n\nAn alternate syntax for NI-DAQmx devices consists of DAQ::\\ *NI-DAQmx\ndevice name*, as shown in Example 3. This naming convention allows for\nthe use of an NI-DAQmx device in an application that was originally\ndesigned for a Traditional NI-DAQ device. For example, if the\napplication expects DAQ::1, you can rename the NI-DAQmx device to 1 in\nMAX and pass in DAQ::1 for the resource name, as shown in Example 4.\n\nIf you use the DAQ::\\ *n* syntax and an NI-DAQmx device name already\nexists with that same name, the NI-DAQmx device is matched first.\n\nYou can also pass in the name of an IVI logical name or an IVI virtual\nname configured with the IVI Configuration utility, as shown in Example\n5. A logical name identifies a particular virtual instrument. A virtual\nname identifies a specific device and specifies the initial settings for\nthe session.\n',
                    'table_body': [
                        [
                            '1',
                            'Traditional NI-DAQ device',
                            'DAQ::\\ *1*',
                            '(*1* = device number)'
                        ],
                        [
                            '2',
                            'NI-DAQmx device',
                            '*myDAQmxDevice*',
                            '(*myDAQmxDevice* = device name)'
                        ],
                        [
                            '3',
                            'NI-DAQmx device',
                            'DAQ::\\ *myDAQmxDevice*',
                            '(*myDAQmxDevice* = device name)'
                        ],
                        [
                            '4',
                            'NI-DAQmx device',
                            'DAQ::\\ *2*',
                            '(*2* = device name)'
                        ],
                        [
                            '5',
                            'IVI logical name or IVI virtual name',
                            '*myLogicalName*',
                            '(*myLogicalName* = name)'
                        ]
                    ],
                    'table_header': [
                        'Example #',
                        'Device Type',
                        'Syntax',
                        'Variable'
                    ]
                },
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe calibration password required to open an external calibration\nsession to the device.\n'
                },
                'name': 'password',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a session handle that you can use to identify the device in all\nsubsequent NI-FGEN function calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitWithOptions': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nPerforms the following initialization actions:\n\n-  Creates a new IVI instrument session and optionally sets the initial\n   state of the following session attributes:\n   NIFGEN_ATTR_RANGE_CHECK, NIFGEN_ATTR_QUERY_INSTRUMENT_STATUS,\n   NIFGEN_ATTR_CACHE, NIFGEN_ATTR_SIMULATE, and\n   NIFGEN_ATTR_RECORD_COERCIONS.\n-  Opens a session to the specified device using the interface and\n   address that you specify for **resourceName**.\n-  If **IDQuery** is set to VI_TRUE, this function queries the device\n   ID and checks that it is valid for NI-FGEN.\n-  If **resetDevice** is set to VI_TRUE, this function resets the\n   device to a known state.\n-  Sends initialization commands to set the instrument to the state\n   necessary for NI-FGEN operation.\n-  Returns a session handle that you can use to identify the device in\n   all subsequent NI-FGEN function calls.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'caution': '\nTraditional NI-DAQ and NI-DAQmx device names are not case-sensitive.\nHowever, all IVI names, such as logical names, are case-sensitive. If\nyou use logical names, driver session names, or virtual names in your\nprogram, you must ensure that the name you use matches the name in the\nIVI Configuration Store file exactly, without any variations in the case\nof the characters.\n',
                    'description': '\n| Specifies the resource name of the device to initialize.\n\nFor Traditional NI-DAQ devices, the syntax is DAQ::\\ *n*, where *n* is\nthe device number assigned by MAX, as shown in Example 1.\n\nFor NI-DAQmx devices, the syntax is just the device name specified in\nMAX, as shown in Example 2. Typical default names for NI-DAQmx devices\nin MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by\nright-clicking on the name in MAX and entering a new name.\n\nAn alternate syntax for NI-DAQmx devices consists of DAQ::\\ *NI-DAQmx\ndevice name*, as shown in Example 3. This naming convention allows for\nthe use of an NI-DAQmx device in an application that was originally\ndesigned for a Traditional NI-DAQ device. For example, if the\napplication expects DAQ::1, you can rename the NI-DAQmx device to 1 in\nMAX and pass in DAQ::1 for the resource name, as shown in Example 4.\n\nIf you use the DAQ::\\ *n* syntax and an NI-DAQmx device name already\nexists with that same name, the NI-DAQmx device is matched first.\n\nYou can also pass in the name of an IVI logical name or an IVI virtual\nname configured with the IVI Configuration utility, as shown in Example\n5. A logical name identifies a particular virtual instrument. A virtual\nname identifies a specific device and specifies the initial settings for\nthe session.\n',
                    'table_body': [
                        [
                            '1',
                            'Traditional NI-DAQ device',
                            'DAQ::\\ *1*',
                            '(*1* = device number)'
                        ],
                        [
                            '2',
                            'NI-DAQmx device',
                            '*myDAQmxDevice*',
                            '(*myDAQmxDevice* = device name)'
                        ],
                        [
                            '3',
                            'NI-DAQmx device',
                            'DAQ::\\ *myDAQmxDevice*',
                            '(*myDAQmxDevice* = device name)'
                        ],
                        [
                            '4',
                            'NI-DAQmx device',
                            'DAQ::\\ *2*',
                            '(*2* = device name)'
                        ],
                        [
                            '5',
                            'IVI logical name or IVI virtual name',
                            '*myLogicalName*',
                            '(*myLogicalName* = name)'
                        ]
                    ],
                    'table_header': [
                        'Example #',
                        'Device Type',
                        'Syntax',
                        'Variable'
                    ]
                },
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether you want NI-FGEN to perform an ID query.\n\nWhen you set this parameter to VI_TRUE, NI-FGEN verifies that the\ndevice that you initialize is a type that it supports.\n\nCircumstances can arise where sending an ID query to the device is\nundesirable. When you set this parameter to VI_FALSE, the function\ninitializes the device without performing an ID query.\n\n****Defined Values****\n\n**Default Value**: VI_TRUE\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'Perform ID query'
                        ],
                        [
                            'VI_FALSE',
                            'Skip ID query'
                        ]
                    ]
                },
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether you want to reset the device during the initialization\nprocedure. VI_TRUE specifies that the device is reset and performs the\nsame function as the nifgen_Reset function.\n\n****Defined Values****\n\n**Default Value**: VI_TRUE\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'Reset device'
                        ],
                        [
                            'VI_FALSE',
                            'Do not reset device'
                        ]
                    ]
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSets the initial value of certain session attributes.\n\nThe syntax for **optionString** is\n\n<*attributeName*> = <*value*>\n\nwhere\n\n*attributeName* is the name of the attribute and *value* is the value to\nwhich the attribute is set\n\nTo set multiple attributes, separate them with a comma.\n\nIf you pass NULL or an empty string for this parameter, the session uses\nthe default values for these attributes. You can override the default\nvalues by assigning a value explicitly in a string that you pass for\nthis parameter.\n\nYou do not have to specify all of the attributes and may leave any of\nthem out. However, if you do not specify one of the attributes, its\ndefault value is used.\n\nIf simulation is enabled (Simulate=1), you may specify the device that\nyou want to simulate. To specify a device, enter the following syntax in\n**optionString**.\n\nDriverSetup=Model:<*driver model number*>;Channels:<*channel\nnames*>;BoardType:<*module type*>;MemorySize:<*size of onboard memory in\nbytes*>\n\n**Syntax Examples**\n\n**Attributes and **Defined Values****\n\n**Default Values**: "Simulate=0,RangeCheck=1,QueryInstrStatus=1,Cache=1"\n',
                    'table_body': [
                        [
                            'RangeCheck',
                            'NIFGEN_ATTR_RANGE_CHECK',
                            'VI_TRUE, VI_FALSE'
                        ],
                        [
                            'QueryInstrStatus',
                            'NIFGEN_ATTR_QUERY_INSTRUMENT_STATUS',
                            'VI_TRUE, VI_FALSE'
                        ],
                        [
                            'Cache',
                            'NIFGEN_ATTR_CACHE',
                            'VI_TRUE, VI_FALSE'
                        ],
                        [
                            'Simulate',
                            'NIFGEN_ATTR_SIMULATE',
                            'VI_TRUE, VI_FALSE'
                        ]
                    ],
                    'table_header': [
                        'Attribute Name',
                        'Attribute',
                        'Values'
                    ]
                },
                'name': 'optionString',
                'type': 'ViString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a session handle that you can use to identify the device in all\nsubsequent NI-FGEN function calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitializeAnalogOutputCalibration': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Sets up the device to start the analog output calibration.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_InitExtCal function and identifies a particular instrument\nsession.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitializeCalAdcCalibration': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nInitializes an external calibration session for ADC calibration. For the\nNI 5421/5422/5441, ADC calibration involves characterizing the gain and\noffset of the onboard ADC.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_InitExtCal function and identifies a particular instrument\nsession.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitializeFlatnessCalibration': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Initializes an external calibration session to calibrate flatness.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_InitExtCal function and identifies a particular instrument\nsession.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitializeOscillatorFrequencyCalibration': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets up the device to start the VCXO calibration.\n\nThe session handle should be the handle returned by the\nnifgen_InitExtCal function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_InitExtCal function and identifies a particular instrument\nsession.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitializeSessionForServer': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'reset',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'optionsString',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'additionalOptions',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'newVi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitializeWithChannels': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCreates and returns a new NI-FGEN session to the specified channel of a\nwaveform generator that is used in all subsequent NI-FGEN function\ncalls.\n'
        },
        'method_name_for_documentation': '__init__',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'caution': '\nTraditional NI-DAQ and NI-DAQmx device names are not case-sensitive.\nHowever, all IVI names, such as logical names, are case-sensitive. If\nyou use logical names, driver session names, or virtual names in your\nprogram, you must ensure that the name you use matches the name in the\nIVI Configuration Store file exactly, without any variations in the case\nof the characters.\n',
                    'description': '\n| Specifies the resource name of the device to initialize.\n\nFor Traditional NI-DAQ devices, the syntax is DAQ::\\ *n*, where *n* is\nthe device number assigned by MAX, as shown in Example 1.\n\nFor NI-DAQmx devices, the syntax is just the device name specified in\nMAX, as shown in Example 2. Typical default names for NI-DAQmx devices\nin MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by\nright-clicking on the name in MAX and entering a new name.\n\nAn alternate syntax for NI-DAQmx devices consists of DAQ::\\ *NI-DAQmx\ndevice name*, as shown in Example 3. This naming convention allows for\nthe use of an NI-DAQmx device in an application that was originally\ndesigned for a Traditional NI-DAQ device. For example, if the\napplication expects DAQ::1, you can rename the NI-DAQmx device to 1 in\nMAX and pass in DAQ::1 for the resource name, as shown in Example 4.\n\nIf you use the DAQ::\\ *n* syntax and an NI-DAQmx device name already\nexists with that same name, the NI-DAQmx device is matched first.\n\nYou can also pass in the name of an IVI logical name or an IVI virtual\nname configured with the IVI Configuration utility, as shown in Example\n5. A logical name identifies a particular virtual instrument. A virtual\nname identifies a specific device and specifies the initial settings for\nthe session.\n',
                    'table_body': [
                        [
                            '1',
                            'Traditional NI-DAQ device',
                            'DAQ::\\ *1*',
                            '(*1* = device number)'
                        ],
                        [
                            '2',
                            'NI-DAQmx device',
                            '*myDAQmxDevice*',
                            '(*myDAQmxDevice* = device name)'
                        ],
                        [
                            '3',
                            'NI-DAQmx device',
                            'DAQ::\\ *myDAQmxDevice*',
                            '(*myDAQmxDevice* = device name)'
                        ],
                        [
                            '4',
                            'NI-DAQmx device',
                            'DAQ::\\ *2*',
                            '(*2* = device name)'
                        ],
                        [
                            '5',
                            'IVI logical name or IVI virtual name',
                            '*myLogicalName*',
                            '(*myLogicalName* = name)'
                        ]
                    ],
                    'table_header': [
                        'Example #',
                        'Device Type',
                        'Syntax',
                        'Variable'
                    ]
                },
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel that this VI uses.\n\n**Default Value**: "0"\n'
                },
                'is_repeated_capability': False,
                'name': 'channelName',
                'python_api_converter_name': 'convert_repeated_capabilities_from_init',
                'type': 'ViString',
                'type_in_documentation': 'str, list, range, tuple'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether you want to reset the device during the initialization\nprocedure. VI_TRUE specifies that the device is reset and performs the\nsame function as the nifgen_Reset function.\n\n****Defined Values****\n\n**Default Value**: VI_FALSE\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'Reset device'
                        ],
                        [
                            'VI_FALSE',
                            'Do not reset device'
                        ]
                    ]
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': '\nSets the initial value of certain session attributes.\n\nThe syntax for **optionString** is\n\n<*attributeName*> = <*value*>\n\nwhere\n\n*attributeName* is the name of the attribute and *value* is the value to\nwhich the attribute is set\n\nTo set multiple attributes, separate them with a comma.\n\nIf you pass NULL or an empty string for this parameter, the session uses\nthe default values for these attributes. You can override the default\nvalues by assigning a value explicitly in a string that you pass for\nthis parameter.\n\nYou do not have to specify all of the attributes and may leave any of\nthem out. However, if you do not specify one of the attributes, its\ndefault value is used.\n\nIf simulation is enabled (Simulate=1), you may specify the device that\nyou want to simulate. To specify a device, enter the following syntax in\n**optionString**.\n\nDriverSetup=Model:<*driver model number*>;Channels:<*channel\nnames*>;BoardType:<*module type*>;MemorySize:<*size of onboard memory in\nbytes*>\n\n**Syntax Examples**\n\n**Attributes and **Defined Values****\n\n**Default Values**: "Simulate=0,RangeCheck=1,QueryInstrStatus=1,Cache=1"\n',
                    'table_body': [
                        [
                            'RangeCheck',
                            'NIFGEN_ATTR_RANGE_CHECK',
                            'VI_TRUE, VI_FALSE'
                        ],
                        [
                            'QueryInstrStatus',
                            'NIFGEN_ATTR_QUERY_INSTRUMENT_STATUS',
                            'VI_TRUE, VI_FALSE'
                        ],
                        [
                            'Cache',
                            'NIFGEN_ATTR_CACHE',
                            'VI_TRUE, VI_FALSE'
                        ],
                        [
                            'Simulate',
                            'NIFGEN_ATTR_SIMULATE',
                            'VI_TRUE, VI_FALSE'
                        ]
                    ],
                    'table_header': [
                        'Attribute Name',
                        'Attribute',
                        'Values'
                    ]
                },
                'name': 'optionString',
                'python_api_converter_name': 'convert_init_with_options_dictionary',
                'type': 'ViString',
                'type_in_documentation': 'dict'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a session handle that you can use to identify the device in all\nsubsequent NI-FGEN function calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'InitiateGeneration': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nInitiates signal generation. If you want to abort signal generation,\ncall the nifgen_AbortGeneration function. After the signal generation\nis aborted, you can call the niFgen_InitiateGeneration function to\ncause the signal generator to produce a signal again.\n'
        },
        'method_name_for_documentation': 'initiate',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InvalidateAllAttributes': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsAttributeValid': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'repCapName',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'name': 'isValid',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsDone': {
        'documentation': {
            'description': '\nDetermines whether the current generation is complete. This function\nsets the **done** parameter to VI_TRUE if the session is in the Idle or\nCommitted states.\n',
            'note': '\nNI-FGEN only reports the **done** parameter as VI_TRUE after the\ncurrent generation is complete in Single trigger mode.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns information about the completion of waveform generation.\n\n**Defined Values**\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'Generation is complete.'
                        ],
                        [
                            'VI_FALSE',
                            'Generation is not complete.'
                        ]
                    ]
                },
                'name': 'done',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'IsSessionInitialized': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'out',
                'name': 'isInitialized',
                'type': 'ViBoolean'
            },
            {
                'direction': 'out',
                'name': 'isCalibrationSession',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'IviClose': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'IviInit': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'instrName',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'documentation': {
            'description': '\nObtains a multithread lock on the instrument session. Before it does so,\nthis function waits until all other execution threads have released\ntheir locks on the instrument session.\n\nOther threads might have obtained a lock on this session in the\nfollowing ways:\n\n-  Your application called the niFgen_LockSession function.\n-  A call to the NI-FGEN locked the session.\n-  A call to the IVI Engine locked the session.\n\nAfter your call to the niFgen_LockSession function returns\nsuccessfully, no other threads can access the instrument session until\nyou call the nifgen_UnlockSession function.\n\nUse the niFgen_LockSession function and the niFgen_UnlockSession\nfunction around a sequence of calls to NI-FGEN functions if you require\nthat the instrument retain its settings through the end of the sequence.\n\nYou can safely make nested calls to the niFgen_LockSession function\nwithin the same thread. To completely unlock the session, you must\nbalance each call to the niFgen_LockSession function with a call to the\nniFgen_UnlockSession function. If, however, you use the\n**callerHasLock** parameter in all calls to the niFgen_LockSession\nfunction and the niFgen_UnlockSession function within a function, the\nIVI Engine locks the session only once within the function regardless of\nthe number of calls you make to the niFgen_LockSession function. This\nconfiguration allows you to call the niFgen_UnlockSession function just\nonce at the end of the function.\n'
        },
        'method_templates': [
            {
                'documentation_filename': 'lock',
                'method_python_name_suffix': '',
                'session_filename': 'lock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nKeeps track of whether you obtained a lock and therefore need to unlock\nthe session. Pass the address of a local ViBoolean variable. In the\ndeclaration of the local variable, initialize it to VI_FALSE. Pass the\naddress of the same local variable to any other calls you make to the\nniFgen_LockSession function or the nifgen_UnlockSession function in\nthe same function.\n\nThis parameter serves as a convenience. If you do not want to use this\nparameter, pass VI_NULL.\n\nThis parameter is an input/output parameter. The niFgen_LockSession\nfunction and the niFgen_UnlockSession function each inspect the current\nvalue and take the following actions:\n\n-  If the value is VI_TRUE, the niFgen_LockSession function does not\n   lock the session again. If the value is VI_FALSE, the\n   niFgen_LockSession function obtains the lock and sets the value of\n   the parameter to VI_TRUE.\n-  If the value is VI_FALSE, the niFgen_UnlockSession function does\n   not attempt to unlock the session. If the value is VI_TRUE, the\n   niFgen_UnlockSession function releases the lock and sets the value\n   of the parameter to VI_FALSE.\n\nThus, you can call the niFgen_UnlockSession function at the end of your\nfunction without worrying about whether you actually have the lock.\n\nExample:\n\nViStatus TestFunc (ViSession vi, ViInt32 flags)\n{\n\nViStatus error = VI_SUCCESS;\nViBoolean haveLock = VI_FALSE;\nif (flags & BIT_1)\n{\n\nviCheckErr( niFgen_LockSession(vi, &haveLock;));\nviCheckErr( TakeAction1(vi));\nif (flags & BIT_2)\n{\n\n viCheckErr( niFgen_UnlockSession(vi, &haveLock;));\nviCheckErr( TakeAction2(vi));\nviCheckErr( niFgen_LockSession(vi, &haveLock;);\n\n}\nif (flags & BIT_3)\n\n viCheckErr( TakeAction3(vi));\n\n}\n\nError:\n\n| \n\n/\\*\nAt this point, you cannot really be sure that\nyou have the lock. Fortunately, the haveLock\nvariable takes care of that for you.\n\\*/\nniFgen_UnlockSession(vi, &haveLock;);\nreturn error;\n\n| }\n'
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
    'LvClose': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'errorBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'errorBuffer',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvCloseExtCal': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'action',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'errorBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'errorBuffer',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvGetError': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'statusCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'name': 'errorBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'errorDescription',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvGetErrorMessage': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'statusCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'name': 'errorMessageBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvInit': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'direction': 'out',
                'name': 'newVi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'errorBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'errorBuffer',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvInitExtCal': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'name': 'password',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'newVi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'errorBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'errorBuffer',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvInitWithOptions': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'optionsString',
                'type': 'ViString'
            },
            {
                'direction': 'out',
                'name': 'newVi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'errorBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'errorBuffer',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvInitializeWithChannels': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'optionsString',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'newVi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'errorBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'errorBuffer',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ManualEnableP2PStream': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Enables a peer-to-peer data stream using manual flow control.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the stream endpoint FIFO to configure. Refer to the\n`Peer-to-Peer Data\nStreaming <REPLACE_DRIVER_SPECIFIC_URL_2(p2p_streaming)>`__\ndocumentation in the *NI Signal Generators Help* for more information.\n'
                },
                'name': 'endpointName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryArbSeqCapabilities': {
        'documentation': {
            'description': '\nReturns the attributes of the signal generator that are related to\ncreating arbitrary sequences (the NIFGEN_ATTR_MAX_NUM_SEQUENCES,\nNIFGEN_ATTR_MIN_SEQUENCE_LENGTH,\nNIFGEN_ATTR_MAX_SEQUENCE_LENGTH, and NIFGEN_ATTR_MAX_LOOP_COUNT\nattributes).\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum number of arbitrary waveform sequences that the\nsignal generator allows. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MAX_NUM_SEQUENCES attribute.\n'
                },
                'name': 'maximumNumberOfSequences',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the minimum number of arbitrary waveforms the signal generator\nallows in a sequence. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MIN_SEQUENCE_LENGTH attribute.\n'
                },
                'name': 'minimumSequenceLength',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum number of arbitrary waveforms the signal generator\nallows in a sequence. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MAX_SEQUENCE_LENGTH attribute.\n'
                },
                'name': 'maximumSequenceLength',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum number of times the signal generator can repeat an\narbitrary waveform in a sequence. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MAX_LOOP_COUNT attribute.\n'
                },
                'name': 'maximumLoopCount',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryArbWfmCapabilities': {
        'documentation': {
            'description': '\nReturns the attributes of the signal generator that are related to\ncreating arbitrary waveforms. These attributes are the maximum number of\nwaveforms, waveform quantum, minimum waveform size, and maximum waveform\nsize.\n',
            'note': '\nIf you do not want to obtain the waveform quantum, pass a value of\nVI_NULL for this parameter.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum number of arbitrary waveforms that the signal\ngenerator allows. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MAX_NUM_WAVEFORMS attribute.\n'
                },
                'name': 'maximumNumberOfWaveforms',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe size (number of points) of each waveform must be a multiple of a\nconstant quantum value. This parameter obtains the quantum value that\nthe signal generator uses. NI-FGEN returns this value from the\nNIFGEN_ATTR_WAVEFORM_QUANTUM attribute.\n\nFor example, when this attribute returns a value of 8, all waveform\nsizes must be a multiple of 8.\n'
                },
                'name': 'waveformQuantum',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the minimum number of points that the signal generator allows in\na waveform. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MIN_WAVEFORM_SIZE attribute.\n'
                },
                'name': 'minimumWaveformSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum number of points that the signal generator allows in\na waveform. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MAX_WAVEFORM_SIZE attribute.\n'
                },
                'name': 'maximumWaveformSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryFreqListCapabilities': {
        'documentation': {
            'description': '\nReturns the attributes of the signal generator that are related to\ncreating frequency lists. These attributes are\nNIFGEN_ATTR_MAX_NUM_FREQ_LISTS,\nNIFGEN_ATTR_MIN_FREQ_LIST_LENGTH,\nNIFGEN_ATTR_MAX_FREQ_LIST_LENGTH,\nNIFGEN_ATTR_MIN_FREQ_LIST_DURATION,\nNIFGEN_ATTR_MAX_FREQ_LIST_DURATION, and\nNIFGEN_ATTR_FREQ_LIST_DURATION_QUANTUM.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum number of frequency lists that the signal generator\nallows. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MAX_NUM_FREQ_LISTS attribute.\n'
                },
                'name': 'maximumNumberOfFreqLists',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the minimum number of steps that the signal generator allows in\na frequency list. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MIN_FREQ_LIST_LENGTH attribute.\n'
                },
                'name': 'minimumFrequencyListLength',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum number of steps that the signal generator allows in\na frequency list. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MAX_FREQ_LIST_LENGTH attribute.\n'
                },
                'name': 'maximumFrequencyListLength',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the minimum duration that the signal generator allows in a step\nof a frequency list. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MIN_FREQ_LIST_DURATION attribute.\n'
                },
                'name': 'minimumFrequencyListDuration',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum duration that the signal generator allows in a step\nof a frequency list. NI-FGEN obtains this value from the\nNIFGEN_ATTR_MAX_FREQ_LIST_DURATION attribute.\n'
                },
                'name': 'maximumFrequencyListDuration',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the quantum of which all durations must be a multiple in a\nfrequency list. NI-FGEN obtains this value from the\nNIFGEN_ATTR_FREQ_LIST_DURATION_QUANTUM attribute.\n'
                },
                'name': 'frequencyListDurationQuantum',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadCalAdc': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nTakes one or more voltage measurements from the onboard calibration ADC\nand returns the value or the average value. The signal that the ADC\nactually measures can be specified using the\nNIFGEN_ATTR_CAL_ADC_INPUT attribute. The ADC has some inherent gain\nand offset. These values can be determined during an external\ncalibration session and stored in the calibration EEPROM.\n\nIf the **returnCalibratedValue** parameter is VI_TRUE, NI-FGEN adjusts\nthe value that is returned to account for the gain and offset of the\nADC. Otherwise, the raw voltage value reported by the ADC is returned.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_init or the nifgen_InitExtCal function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of measurements to be taken and averaged to\ndetermine the return value.\n'
                },
                'name': 'numberOfReadsToAverage',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether the voltage returned from the ADC should be adjusted\nto account for the gain and offset of the ADC.\n'
                },
                'name': 'returnCalibratedValue',
                'type': 'ViBoolean'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSpecifies the average of the voltage measurements taken from the onboard\ncalibration ADC.\n'
                },
                'name': 'calAdcValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadCurrentTemperature': {
        'documentation': {
            'description': '\nReads the current onboard temperature of the device. The temperature is\nreturned in degrees Celsius.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_init or the nifgen_InitExtCal function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current temperature read from onboard temperature sensors,\nin degrees Celsius.\n'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadScarabMemory': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'numberOfSamples',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'name': 'startingAddress',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'name': 'data',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReleaseSessionForServer': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'RequestPrivilege': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'privilegeLevel',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetAttribute': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Resets the attribute to its default value.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or an empty string ("").\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetDevice': {
        'documentation': {
            'description': '\nPerforms a hard reset on the device. Generation is stopped, all routes\nare released, external bidirectional terminals are tristated, FPGAs are\nreset, hardware is configured to its default state, and all session\nattributes are reset to their default states.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetInterchangeCheck': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis function tests the current test module for dependencies on the\noperation of previously executed test modules. If your module depends on\nthe operation of previous modules, your test system has less\nflexibility.\n\nWhen developing a complex test system that consists of multiple test\nmodules, NI recommends that you design the test modules so that they can\nrun in any order. To do so, ensure that each test module completely\nconfigures the state of each instrument it uses. If a particular test\nmodule does not completely configure the state of an instrument, the\nstate of the instrument depends on the configuration from a previously\nexecuted test module. If you execute the test modules in a different\norder, the behavior of the instrument and the test module may change.\nThis change in behavior is generally instrument specific and represents\nan interchangeability problem.\n\nAfter you call this function, the interchangeability checking algorithms\nin the specific driver ignore all previous configuration operations. By\ncalling this function at the beginning of a test module, you can\ndetermine whether the test module has dependencies on the operation of\npreviously executed test modules.\n\nThis function does not clear the interchangeability warnings from the\nlist of previously recorded interchangeability warnings. If you want to\nguarantee that the nifgen_GetNextInterchangeWarning function only\nreturns those interchangeability warnings that are generated after\ncalling this function, you must clear the list of interchangeability\nwarnings. You can clear the interchangeability warnings list by\nrepeatedly calling the niFgen_GetNextInterchangeWarning function until\nno more interchangeability warnings are returned. If you are not\ninterested in the content of those warnings, you can call the\nnifgen_ClearInterchangeWarnings function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithDefaults': {
        'documentation': {
            'description': '\nResets the instrument and reapplies initial user–specified settings from\nthe logical name that was used to initialize the session. If the session\nwas created without a logical name, this function is equivalent to the\nnifgen_reset function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'RestoreAttributes': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'RestoreLastExtCalConstants': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nOverwrites the current calibration constants with those from the last\nsuccessful external calibration. This action effectively undoes any\nself-calibrations performed since the last time an external calibration\nwas performed. This function should be used if a self-calibration\nproduced invalid calibration constants.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_InitExtCal function and identifies a particular instrument\nsession.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'RevokeControl': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'clientWasRevoked',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'RouteSignalOut': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nRoutes various signals in the signal generator to the RTSI lines and\nfront panel terminals.\n',
            'note': '\nThe signal generator must not be in the Generating state when you call\nthis function.\n',
            'table_body': [
                [
                    ' ',
                    'You can clear a previously routed signal by routing NIFGEN_VAL_NONE to the destination terminal.'
                ]
            ]
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to route a signal.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nVarious signals can be routed out the RTSI lines.\n\n****Defined Values****\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_NONE',
                            'Nothing Sending this value clears the line.'
                        ],
                        [
                            'NIFGEN_VAL_MARKER',
                            'Marker Event'
                        ],
                        [
                            'NIFGEN_VAL_SYNC_OUT',
                            'SYNC signal This signal normally appears on the SYNC OUT front panel connector.'
                        ],
                        [
                            'NIFGEN_VAL_OUT_START_TRIGGER',
                            'Start Trigger The Start Trigger is normally generated at the start of the sequence. Call the nifgen_ConfigureTriggerSource function to receive this trigger.'
                        ],
                        [
                            'NIFGEN_VAL_BOARD_CLOCK',
                            'Signal generator board clock The signal generator board clock is 20 MHz for the NI PCI-5401/5411/5431. The NI PXI-5404 has a 20 MHz board clock, and the NI PXI-5421 has integer divisors of 100 MHz. The NI PXI-5401/5411/5431 does not support routing a Board Clock to RTSI lines or front panel connectors.'
                        ],
                        [
                            'NIFGEN_VAL_SYNCHRONIZATION',
                            'Synchronization strobe A synchronization strobe is used to guarantee absolute synchronization between two or more signal generators. Call the nifgen_ConfigureSynchronization function to receive the strobe.'
                        ],
                        [
                            'NIFGEN_VAL_SOFTWARE_TRIG',
                            'Software trigger'
                        ],
                        [
                            'NIFGEN_VAL_OUT_UPDATE',
                            '—'
                        ],
                        [
                            'NIFGEN_VAL_REF_OUT',
                            'Reference Clock out front panel connector'
                        ],
                        [
                            'NIFGEN_VAL_PXI_CLK10',
                            'PXI 10 MHz backplane Reference Clock'
                        ],
                        [
                            'NIFGEN_VAL_PXI_STAR',
                            'PXI star trigger line'
                        ],
                        [
                            'NIFGEN_VAL_PFI_0',
                            'PFI 0'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_0',
                            'RTSI 0 or PXI_Trig 0'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_1',
                            'RTSI 1 or PXI_Trig 1'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_2',
                            'RTSI 2 or PXI_Trig 2'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_3',
                            'RTSI 3 or PXI_Trig 3'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_4',
                            'RTSI 4 or PXI_Trig 4'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_5',
                            'RTSI 5 or PXI_Trig 5'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_6',
                            'RTSI 6 or PXI_Trig 6'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_7',
                            'RTSI 7 or PXI_Trig 7'
                        ],
                        [
                            'NIFGEN_VAL_REF_CLOCK_RTSI_CLOCK',
                            'RTSI clock'
                        ],
                        [
                            'NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK',
                            'Onboard Reference Clock'
                        ],
                        [
                            'NIFGEN_VAL_UPDATE_CLOCK',
                            'Sample Clock'
                        ],
                        [
                            'NIFGEN_VAL_PLL_REF_SOURCE',
                            'PLL Reference Clock'
                        ]
                    ]
                },
                'name': 'routeSignalFrom',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe possible RTSI lines to which you can route a signal.\n\n****Defined Values****\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_RTSI_0',
                            'RTSI 0 or PXI_Trig 0'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_1',
                            'RTSI 1 or PXI_Trig 1'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_2',
                            'RTSI 2 or PXI_Trig 2'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_3',
                            'RTSI 3 or PXI_Trig 3'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_4',
                            'RTSI 4 or PXI_Trig 4'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_5',
                            'RTSI 5 or PXI_Trig 5'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_6',
                            'RTSI 6 or PXI_Trig 6'
                        ],
                        [
                            'NIFGEN_VAL_RTSI_7',
                            'RTSI 7 or PXI_Trig 7'
                        ],
                        [
                            'NIFGEN_VAL_REF_CLOCK_RTSI_CLOCK',
                            'RTSI clock'
                        ],
                        [
                            'NIFGEN_VAL_REF_OUT',
                            'Reference Clock out front panel connector'
                        ],
                        [
                            'NIFGEN_VAL_PFI_0',
                            'PFI 0'
                        ],
                        [
                            'NIFGEN_VAL_PFI_1',
                            'PFI 1'
                        ],
                        [
                            'NIFGEN_VAL_PFI_4',
                            'PFI 4'
                        ],
                        [
                            'NIFGEN_VAL_PFI_5',
                            'PFI 5'
                        ],
                        [
                            'NIFGEN_VAL_PXI_STAR',
                            'PXI star trigger line'
                        ],
                        [
                            'NIFGEN_VAL_PXI_CLK10',
                            'PXI 10 MHz backplane Reference Clock'
                        ]
                    ]
                },
                'name': 'routeSignalTo',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SaveAttributes': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfCal': {
        'documentation': {
            'description': '\nPerforms a full internal self-calibration on the device. If the\ncalibration is successful, new calibration data and constants are stored\nin the onboard EEPROM.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init or the nifgen_InitWithOptions functions and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareEdgeTrigger': {
        'documentation': {
            'description': '\nSends a command to trigger the signal generator. This VI can act as an\noverride for an external edge trigger.\n',
            'note': '\nThis VI does not override external digital edge triggers of the\nNI 5401/5411/5431.\n'
        },
        'method_templates': [
            {
                'documentation_filename': 'send_software_edge_trigger',
                'method_python_name_suffix': '',
                'session_filename': 'send_software_edge_trigger'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSets the clock mode of the signal generator.\n\n****Defined Values****\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_DIVIDE_DOWN'
                        ],
                        [
                            'NIFGEN_VAL_HIGH_RESOLUTION'
                        ],
                        [
                            'NIFGEN_VAL_AUTOMATIC'
                        ]
                    ]
                },
                'name': 'trigger',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'triggerId',
                'type': 'ViString'
            }
        ],
        'render_in_session_base': True,
        'returns': 'ViStatus'
    },
    'SendSoftwareTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Sends a command to trigger the signal generator.',
            'note': '\nThis function can act as an override for an external edge trigger.\nHowever, the NI 5401/5411/5431 do not support overriding an external\ndigital edge trigger.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSwTrigger': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViBoolean attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes. If the\nattribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n\nNI-FGEN contains high-level functions that set most of the instrument\nattributes. NI recommends that you use the high-level driver functions\nas much as possible. They handle order dependencies and multithread\nlocking for you. In addition, they perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the Set Attribute functions, the functions check the\ninstrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or "" (empty string).\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. **Default\nValue**: None\n',
                    'note': '\nSome of the values might not be valid depending on the current\nsettings of the instrument session.\n'
                },
                'name': 'attributeValue',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt32': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViInt32 attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes. If the\nattribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n\nNI-FGEN contains high-level functions that set most of the instrument\nattributes. NI recommends that you use the high-level driver functions\nas much as possible. They handle order dependencies and multithread\nlocking for you. In addition, they perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the Set Attribute functions, the functions check the\ninstrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or "" (empty string).\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. **Default\nValue**: None\n',
                    'note': '\nSome of the values might not be valid depending on the current\nsettings of the instrument session.\n'
                },
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt64': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the value of a ViInt64 attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes. If the\nattribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n\nNI-FGEN contains high-level functions that set most of the instrument\nattributes. NI recommends that you use the high-level driver functions\nas much as possible. They handle order dependencies and multithread\nlocking for you. In addition, they perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the Set Attribute functions, the functions check the\ninstrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or "" (empty string).\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. **Default\nValue**: None\n',
                    'note': '\nSome of the values might not be valid depending on the current\nsettings of the instrument session.\n'
                },
                'name': 'attributeValue',
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViReal64 attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes. If the\nattribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n\nNI-FGEN contains high-level functions that set most of the instrument\nattributes. NI recommends that you use the high-level driver functions\nas much as possible. They handle order dependencies and multithread\nlocking for you. In addition, they perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the Set Attribute functions, the functions check the\ninstrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or "" (empty string).\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. **Default\nValue**: None\n',
                    'note': '\nSome of the values might not be valid depending on the current\nsettings of the instrument session.\n'
                },
                'name': 'attributeValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViSession': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the value of a ViSession attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes. If the\nattribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n\nNI-FGEN contains high-level functions that set most of the instrument\nattributes. It is best to use the high-level driver functions as much as\npossible. They handle order dependencies and multithread locking for\nyou. In addition, they perform status checking only after setting all of\nthe attributes. In contrast, when you set multiple attributes using the\nSet Attribute functions, the functions check the instrument status after\neach call.\n\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or an empty string ("").\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. **Default\nValue**: None\n',
                    'note': '\nSome of the values might not be valid depending on the current\nsettings of the instrument session.\n'
                },
                'name': 'attributeValue',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViString': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the value of a ViString attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes. If the\nattribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled and the currently cached value is invalid or\n   is different than the value you specify.\n\nNI-FGEN contains high-level functions that set most of the instrument\nattributes. NI recommends that you use the high-level driver functions\nas much as possible. They handle order dependencies and multithread\nlocking for you. In addition, they perform status checking only after\nsetting all of the attributes. In contrast, when you set multiple\nattributes using the Set Attribute functions, the functions check the\ninstrument status after each call.\n\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the channel on which to check the attribute value\nif the attribute is channel-based. If the attribute is not\nchannel-based, then pass VI_NULL or "" (empty string).\n\n**Default Value**: "" (empty string)\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. **Default\nValue**: None\n',
                    'note': '\nSome of the values might not be valid depending on the current\nsettings of the instrument session.\n'
                },
                'name': 'attributeValue',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetCalUserDefinedInfo': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nStores user-defined information in the onboard EEPROM. Call the\nnifgen_GetCalUserDefinedInfoMaxSize function to determine the maximum\nnumber of characters that can be stored.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_init or the nifgen_InitExtCal function and identifies a\nparticular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the information string that should be stored in the EEPROM.'
                },
                'name': 'info',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetConfigList': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'numCommands',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'opCodes',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'channelNumbers',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'values',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetNamedWaveformNextWritePosition': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the position in the waveform to which data is written at the next\nwrite. This function allows you to write to arbitrary locations within\nthe waveform. These settings apply only to the next write to the\nwaveform specified by the **waveformHandle** parameter. Subsequent\nwrites to that waveform begin where the last write left off, unless this\nfunction is called again. The **waveformHandle** passed in must have\nbeen created with a call to one of the following functions:\n\n-  nifgen_AllocateWaveform\n-  nifgen_CreateWaveformF64\n-  nifgen_CreateWaveformI16\n-  nifgen_CreateWaveformFromFileI16\n-  nifgen_CreateWaveformFromFileF64\n-  nifgen_CreateWaveformFromFileHWS\n'
        },
        'method_name_for_documentation': 'set_next_write_position',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel onto which the waveform data should be loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name to associate with the allocated waveform.'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the reference position in the waveform. This position and\n**offset** together determine where to start loading data into the\nwaveform.\n\n****Defined Values****\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_WAVEFORM_POSITION_START (0)',
                            'Use the start of the waveform as the reference position.'
                        ],
                        [
                            'NIFGEN_VAL_WAVEFORM_POSITION_CURRENT (1)',
                            'Use the current position within the waveform as the reference position.'
                        ]
                    ]
                },
                'enum': 'RelativeTo',
                'name': 'relativeTo',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the offset from the **relativeTo** parameter at which to start\nloading the data into the waveform.\n'
                },
                'name': 'offset',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetNextWritePositionDispatcher': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nSets the position in the waveform at which the next waveform data is\nwritten. This function allows you to write to arbitrary locations within\nthe waveform. These settings apply only to the next write to the\nwaveform specified by the waveformHandle parameter. Subsequent writes to\nthat waveform begin where the last write left off, unless this function\nis called again. The waveformHandle passed in must have been created by\na call to the nifgen_AllocateWaveform function or one of the following\nniFgen_CreateWaveformF64 function.\n'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'set_next_write_position'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. **vi** is obtained from the niFgen_InitializeWithChannels function and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the channel on which to the waveform data should be loaded.'
                },
                'name': 'channelName',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The name (str) or handle (int) of an arbitrary waveform previously allocated with niFgen_AllocateNamedWaveform, niFgen_AllocateWaveform or niFgen_CreateWaveformF64.'
                },
                'name': 'waveformNameOrHandle',
                'type': 'ViInt32',
                'type_in_documentation': 'str or int'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the reference position in the waveform. This position and\n**offset** together determine where to start loading data into the\nwaveform.\n\n****Defined Values****\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_WAVEFORM_POSITION_START (0)',
                            'Use the start of the waveform as the reference position.'
                        ],
                        [
                            'NIFGEN_VAL_WAVEFORM_POSITION_CURRENT (1)',
                            'Use the current position within the waveform as the reference position.'
                        ]
                    ]
                },
                'enum': 'RelativeTo',
                'name': 'relativeTo',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the offset from **relativeTo** at which to start loading the\ndata into the waveform.\n'
                },
                'name': 'offset',
                'type': 'ViInt32'
            }
        ],
        'python_name': 'set_next_write_position',
        'returns': 'ViStatus'
    },
    'SetSparseMarkerIndexes': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'name',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'indexesArraySize',
                'type': 'ViInt64'
            },
            {
                'direction': 'in',
                'name': 'indexes',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViInt64'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetWaveformNextWritePosition': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nSets the position in the waveform at which the next waveform data is\nwritten. This function allows you to write to arbitrary locations within\nthe waveform. These settings apply only to the next write to the\nwaveform specified by the waveformHandle parameter. Subsequent writes to\nthat waveform begin where the last write left off, unless this function\nis called again. The waveformHandle passed in must have been created by\na call to the nifgen_AllocateWaveform function or one of the following\nniFgen CreateWaveform functions:\n\n-  nifgen_CreateWaveformF64\n-  nifgen_CreateWaveformI16\n-  nifgen_CreateWaveformFromFileI16\n-  nifgen_CreateWaveformFromFileF64\n-  nifgen_CreateWaveformFromFileHWS\n'
        },
        'method_name_for_documentation': 'set_next_write_position',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel on which to the waveform data should be loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the arbitrary waveform previously allocated with\nthe nifgen_AllocateWaveform function.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the reference position in the waveform. This position and\n**offset** together determine where to start loading data into the\nwaveform.\n\n****Defined Values****\n',
                    'table_body': [
                        [
                            'NIFGEN_VAL_WAVEFORM_POSITION_START (0)',
                            'Use the start of the waveform as the reference position.'
                        ],
                        [
                            'NIFGEN_VAL_WAVEFORM_POSITION_CURRENT (1)',
                            'Use the current position within the waveform as the reference position.'
                        ]
                    ]
                },
                'enum': 'RelativeTo',
                'name': 'relativeTo',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the offset from **relativeTo** at which to start loading the\ndata into the waveform.\n'
                },
                'name': 'offset',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'documentation': {
            'description': '\nReleases a lock that you acquired on an instrument session using the\nnifgen_LockSession function.\n'
        },
        'method_templates': [
            {
                'documentation_filename': 'unlock',
                'method_python_name_suffix': '',
                'session_filename': 'unlock'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nKeeps track of whether you obtain a lock and therefore need to unlock\nthe session.\n\nThis parameter serves as a convenience. If you do not want to use this\nparameter, pass VI_NULL.\n\nPass the address of a local ViBoolean variable. In the declaration of\nthe local variable, initialize it to VI_FALSE. Pass the address of the\nsame local variable to any other calls you make to the\nniFgen_LockSession function or the niFgen_UnlockSession function in\nthe same function.\n\nThe parameter is an input/output parameter. The niFgen_LockSession\nfunction and the niFgen_UnlockSession function each inspect the current\nvalue and take the following actions:\n\n-  If the value is VI_TRUE, the niFgen_LockSession function does not\n   lock the session again. If the value is VI_FALSE, the\n   niFgen_LockSession function obtains the lock and sets the value of\n   the parameter to VI_TRUE.\n-  If the value is VI_FALSE, the niFgen_UnlockSession function does\n   not attempt to unlock the session. If the value is VI_TRUE, the\n   niFgen_UnlockSession function releases the lock and sets the value\n   of the parameter to VI_FALSE.\n\nThus, you can, call the niFgen_UnlockSession function at the end of\nyour function without worrying about whether you actually have the lock.\n\nExample:\n\nViStatus TestFunc (ViSession vi, ViInt32 flags)\n{\n\nViStatus error = VI_SUCCESS;\nViBoolean haveLock = VI_FALSE;\nif (flags & BIT_1)\n{\n\nviCheckErr(niFgen_LockSession(vi, &haveLock;));\nviCheckErr( TakeAction1(vi));\nif (flags & BIT_2)\n{\n\nviCheckErr( niFgen_UnlockSession(vi, &haveLock;));\nviCheckErr( TakeAction2(vi));\nviCheckErr( niFgen_LockSession(vi, &haveLock;);\n\n}\nif (flags & BIT_3)\n\n viCheckErr( TakeAction3(vi));\n\n}\n\nError:\n\n| \n\n/\\*\nAt this point, you cannot really be sure that\nyou have the lock. Fortunately, the haveLock\nvariable takes care of that for you.\n\\*/\nniFgen_UnlockSession(vi, &haveLock;);\nreturn error;\n\n}\n'
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
            'description': '\nWaits until the device is done generating or until the maximum time has\nexpired.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'datetime.timedelta(seconds=10.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the timeout value in milliseconds.'
                },
                'name': 'maxTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                'type': 'ViInt32',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteBinary16AnalogStaticValue': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\n| Writes the 16-bit value to the DAC, which could be output as a DC\n  Voltage.\n| This function writes to the DAC only when in an external calibration\n  session.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nnifgen_InitExtCal function and identifies a particular instrument\nsession.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel name for which you want to write the value.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The value to write.'
                },
                'name': 'value',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteBinary16Waveform': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nWrites binary data to the waveform in onboard memory. The waveform\nhandle passed must have been created by a call to the\nnifgen_AllocateWaveform or the nifgen_CreateWaveformI16 function.\n\nBy default, the subsequent call to the niFgen_WriteBinary16Waveform\nfunction continues writing data from the position of the last sample\nwritten. You can set the write position and offset by calling the\nnifgen_SetWaveformNextWritePosition function. If streaming is enabled,\nyou can write more data than the allocated waveform size in onboard\nmemory. Refer to the\n`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more\ninformation about streaming data.\n'
        },
        'method_name_for_documentation': 'write_waveform',
        'method_templates': [
            {
                'method_python_name_suffix': '_numpy',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel on which to the waveform data should be loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the arbitrary waveform previously allocated with\nthe nifgen_AllocateWaveform function.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of samples to load into the waveform.\n\n**Default Value**: 0\n'
                },
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data to load into the waveform. The array must\nhave at least as many elements as the value in **size**. The binary data\nis left-justified.\n'
                },
                'name': 'data',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViInt16[]',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteComplexBinary16Waveform': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nWrites binary data to the waveform in onboard memory. The waveform\nhandle passed in must have been created by a call to the\nnifgen_AllocateWaveform or the nifgen_CreateWaveformI16 function.\n\nBy default, the subsequent call to the\nniFgen_WriteComplexBinary16Waveform function continues writing data\nfrom the position of the last sample written. You can set the write\nposition and offset by calling the nifgen_SetWaveformNextWritePosition\nfunction. If streaming is enabled, you can write more data than the\nallocated waveform size in onboard memory. Refer to the\n`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more\ninformation about streaming data.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies channel on which to the waveform data should be loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the arbitrary waveform previously allocated with\nthe nifgen_AllocateWaveform function.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of samples to load into the waveform.\n\n**Default Value**: 0\n'
                },
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data to load into the waveform. The array must\nhave at least as many elements as the value in **size**. The binary data\nis left-justified.\n'
                },
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ni_complex_i16[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteNamedWaveformComplexF64': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nWrites complex floating–point data to the named waveform in onboard\nmemory on devices with the NIFGEN_ATTR_OSP_ENABLED attribute set to\nVI_TRUE and the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute set\nto NIFGEN_VAL_OSP_COMPLEX. The waveform handle passed in must have\nbeen created by a call to the nifgen_AllocateWaveform function or to\none of the following niFgen Create Waveform functions:\n\n-  nifgen_CreateWaveformF64\n-  nifgen_CreateWaveformI16\n-  nifgen_CreateWaveformFromFileI16\n-  nifgen_CreateWaveformFromFileF64\n-  nifgen_CreateWaveformFromFileHWS\n\nBy default, the subsequent call to the\nniFgen_WriteNamedWaveformComplexF64 function continues writing data\nfrom the position of the last sample written. You can set the write\nposition and offset by calling the\nnifgen_SetNamedWaveformNextWritePosition function. If streaming is\nenabled, you can write more data than the allocated waveform size in\nonboard memory. Refer to the\n`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more\ninformation about streaming data.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel onto which the waveform data should be loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name to associate with the allocated waveform.'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of samples to load into the waveform.\n\n**Default Value**: 0\n'
                },
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data to load into the waveform. The array must\nhave at least as many elements as the value in **size**.\n'
                },
                'name': 'data',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ni_complex_number[]',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteNamedWaveformComplexI16': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nWrites complex binary data to the named waveform in onboard memory on\ndevices with the NIFGEN_ATTR_OSP_ENABLED attribute set to VI_TRUE\nand the NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute set to\nNIFGEN_VAL_OSP_COMPLEX. The waveform handle passed in must have been\ncreated by a call to the nifgen_AllocateWaveform function or to one of\nthe following niFgen Create Waveform functions:\n\n-  nifgen_CreateWaveformF64\n-  nifgen_CreateWaveformI16\n-  nifgen_CreateWaveformFromFileI16\n-  nifgen_CreateWaveformFromFileF64\n-  nifgen_CreateWaveformFromFileHWS\n\nBy default, the subsequent call to the\nniFgen_WriteNamedWaveformComplexi16 function continues writing data\nfrom the position of the last sample written. You can set the write\nposition and offset by calling the\nnifgen_SetNamedWaveformNextWritePosition function. If streaming is\nenabled, you can write more data than the allocated waveform size in\nonboard memory. Refer to the\n`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more\ninformation about streaming data.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel onto which the waveform data should be loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name to associate with the allocated waveform.'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of samples to load into the waveform.\n\n**Default Value**: 0\n'
                },
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data to load into the waveform. The array must\nhave at least as many elements as the value in **size**.\n'
                },
                'name': 'data',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ni_complex_i16[]',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteNamedWaveformF64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nWrites floating-point data to the waveform in onboard memory. The\nwaveform handle passed in must have been created by a call to the\nnifgen_AllocateWaveform function or to one of the following niFgen\nCreate Waveform functions:\n\n-  nifgen_CreateWaveformF64\n-  nifgen_CreateWaveformI16\n-  nifgen_CreateWaveformFromFileI16\n-  nifgen_CreateWaveformFromFileF64\n-  nifgen_CreateWaveformFromFileHWS\n\nBy default, the subsequent call to the niFgen_WriteNamedWaveformF64\nfunction continues writing data from the position of the last sample\nwritten. You can set the write position and offset by calling the\nnifgen_SetNamedWaveformNextWritePosition function. If streaming is\nenabled, you can write more data than the allocated waveform size in\nonboard memory. Refer to the\n`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more\ninformation about streaming data.\n'
        },
        'method_name_for_documentation': 'write_waveform',
        'method_templates': [
            {
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            },
            {
                'method_python_name_suffix': '_numpy',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel onto which the waveform data should be loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name to associate with the allocated waveform.'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of samples to load into the waveform.\n\n**Default Value**: 0\n'
                },
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data to load into the waveform. The array must\nhave at least as many elements as the value in **size**.\n'
                },
                'name': 'data',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteNamedWaveformI16': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nWrites binary data to the named waveform in onboard memory.\n\nBy default, the subsequent call to the niFgen_WriteNamedWaveformI16\nfunction continues writing data from the position of the last sample\nwritten. You can set the write position and offset by calling the\nnifgen_SetNamedWaveformNextWritePosition function. If streaming is\nenabled, you can write more data than the allocated waveform size in\nonboard memory. Refer to the\n`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more\ninformation about streaming data.\n'
        },
        'method_name_for_documentation': 'write_waveform',
        'method_templates': [
            {
                'method_python_name_suffix': '_numpy',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel onto which the waveform data should be loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name to associate with the allocated waveform.'
                },
                'name': 'waveformName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of samples to load into the waveform.\n\n**Default Value**: 0\n'
                },
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data to load into the waveform. The array must\nhave at least as many elements as the value in **size**.\n'
                },
                'name': 'data',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViInt16[]',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteP2PEndpointI16': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nWrites I16 data to the peer-to-peer endpoint. Use this function to write\ninitial data from the host to the endpoint before starting generation to\navoid an underflow at start.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the name of the FIFO endpoint. Data is written to the endpoint\nFIFO.\n'
                },
                'name': 'endpointName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of samples to write into the endpoint FIFO.'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data to write into the endpoint FIFO. The binary\ndata is left-justified.\n'
                },
                'name': 'endpointData',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteScript': {
        'documentation': {
            'description': '\nWrites a string containing one or more scripts that govern the\ngeneration of waveforms.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel on which the script is loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': "\nContains the text of the script you want to use for your generation\noperation. Refer to `scripting\nInstructions <REPLACE_DRIVER_SPECIFIC_URL_2(niscripted.chm',%20'scripting_instructions)>`__\nfor more information about writing scripts.\n"
                },
                'name': 'script',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteWaveform': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nWrites floating-point data to the waveform in onboard memory. The\nwaveform handle passed in must have been created by a call to the\nnifgen_AllocateWaveform function or one of the following niFgen\nCreateWaveform functions:\n\n-  nifgen_CreateWaveformF64\n-  nifgen_CreateWaveformI16\n-  nifgen_CreateWaveformFromFileI16\n-  nifgen_CreateWaveformFromFileF64\n-  nifgen_CreateWaveformFromFileHWS\n\nBy default, the subsequent call to the niFgen_WriteWaveform function\ncontinues writing data from the position of the last sample written. You\ncan set the write position and offset by calling the\nnifgen_SetWaveformNextWritePosition function. If streaming is enabled,\nyou can write more data than the allocated waveform size in onboard\nmemory. Refer to the\n`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more\ninformation about streaming data.\n'
        },
        'method_name_for_documentation': 'write_waveform',
        'method_templates': [
            {
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            },
            {
                'method_python_name_suffix': '_numpy',
                'session_filename': 'numpy_write_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe channel onto which the waveform data should be loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the arbitrary waveform previously allocated with\nthe nifgen_AllocateWaveform function.\n'
                },
                'name': 'waveformHandle',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of samples to load into the waveform.\n\n**Default Value**: 0\n'
                },
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data to load into the waveform. The array must\nhave at least as many elements as the value in **size**.\n'
                },
                'name': 'data',
                'numpy': True,
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteWaveformComplexF64': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nWrites complex data to the waveform in onboard memory on devices with\nthe NIFGEN_ATTR_OUTPUT_ENABLED attribute set to VI_TRUE and the\nNIFGEN_ATTR_OSP_DATA_PROCESSING_MODE attribute set to\nNIFGEN_VAL_OSP_COMPLEX. The waveform handle passed in must have been\ncreated by a call to the nifgen_AllocateWaveform function or to one of\nthe following niFgen Create Waveform functions:\n\n-  nifgen_CreateWaveformF64\n-  nifgen_CreateWaveformI16\n-  nifgen_CreateWaveformFromFileI16\n-  nifgen_CreateWaveformFromFileF64\n-  nifgen_CreateWaveformFromFileHWS\n\nBy default, the subsequent call to the niFgen_WriteWaveformComplexF64\nfunction continues writing data from the position of the last sample\nwritten. You can set the write position and offset by calling the\nnifgen_SetWaveformNextWritePosition function. If streaming is enabled,\nyou can write more data than the allocated waveform size in onboard\nmemory. Refer to the\n`Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more\ninformation about streaming data.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the channel onto which the waveform data should be loaded.\n\n**Default Value**: "0"\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of samples to load into the waveform.\n**Default Value**: 0\n'
                },
                'name': 'numberOfSamples',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the array of data to load into the waveform. You must\nnormalize the data points in the array to be between –1.00 and +1.00.\nThe array must have at least as many elements as the value in the\n**numberOfSamples** parameter.\n'
                },
                'name': 'data',
                'type': 'ni_complex_number'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the handle of the arbitrary waveform previously allocated with\nthe niFgen_AllocateWaveform function.\n'
                },
                'name': 'waveformHandle',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteWaveformDispatcher': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Writes data to the waveform in onboard memory.\n\nBy default, subsequent calls to this function\ncontinue writing data from the position of the last sample written. You\ncan set the write position and offset by calling the nifgen_SetNamedWaveformNextWritePosition\nnifgen_SetWaveformNextWritePosition function.'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'write_waveform'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelName',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The name (str) or handle (int) of an arbitrary waveform previously allocated with niFgen_AllocateNamedWaveform, niFgen_AllocateWaveform or niFgen_CreateWaveformF64.'
                },
                'name': 'waveformNameOrHandle',
                'type': 'ViInt32',
                'type_in_documentation': 'str or int'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Array of data to load into the waveform. This may be an iterable of float, or for best performance a numpy.ndarray of dtype int16 or float64.'
                },
                'name': 'data',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            }
        ],
        'python_name': 'write_waveform',
        'returns': 'ViStatus'
    },
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nPerforms the following operations:\n\n-  Closes the instrument I/O session.\n-  Destroys the NI-FGEN session and all of its attributes.\n-  Deallocates any memory resources NI-FGEN uses.\n\nNot all signal routes established by calling the nifgen_ExportSignal\nand nifgen_RouteSignalOut functions are released when the NI-FGEN\nsession is closed. The following table shows what happens to a signal\nroute on your device when you call the niFgen_close function.\n',
            'note': '\nAfter calling niFgen_close, you cannot use NI-FGEN again until you\ncall the nifgen_init or nifgen_InitWithOptions functions.\n',
            'table_body': [
                [
                    'Front Panel',
                    'Remain connected',
                    'Remain connected'
                ],
                [
                    'RTSI/PXI Backplane',
                    'Remain connected',
                    'Disconnected'
                ]
            ],
            'table_header': [
                'Routes To',
                'NI 5401/5411/5431',
                'Other Devices'
            ]
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'error_message': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nConverts a status code returned by an NI-FGEN function into a\nuser-readable string.\n'
        },
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init or the niFgen_InitWithOptions functions and identifies a\nparticular instrument session.\n\nYou can pass VI_NULL for this parameter. Passing VI_NULL is useful\nwhen one of the initialize functions fails.\n\n**Default Value**: VI_NULL\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **status** parameter that is returned from any of the\nNI-FGEN functions.\n\n**Default Value**: 0 (VI_SUCCESS)\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the error message string read from the instrument error message\nqueue.\n\nYou must pass a ViChar array with at least 256 bytes.\n'
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
    'error_query': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Reads an error code and a message from the instrument error queue.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the error code read from the instrument error queue.'
                },
                'name': 'errorCode',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the error message string read from the instrument error message\nqueue.\n\nYou must pass a ViChar array with at least 256 bytes.\n'
                },
                'name': 'errorMessage',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'fancy_self_test': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nRuns the instrument self-test routine and returns the test result(s).\n\nRaises `SelfTestError` on self test failure. Attributes on exception object:\n\n- code - failure code from driver\n- message - status message from driver\n',
            'note': '\nWhen used on some signal generators, the device is reset after the\nniFgen_self_test function runs. If you use the niFgen_self_test\nfunction, your device may not be in its previously configured state\nafter the function runs.\n',
            'table_body': [
                [
                    '0',
                    'Passed self-test'
                ],
                [
                    '1',
                    'Self-test failed'
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
                'method_python_name_suffix': '',
                'session_filename': 'fancy_self_test'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies your instrument session. **vi** is obtained from the niFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels functions and identifies a particular instrument session.'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'python_name': 'self_test',
        'returns': 'ViStatus'
    },
    'init': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nPerforms the following initialization actions:\n\n-  Creates a new IVI instrument driver session.\n-  Opens a session to the specified device using the interface and\n   address that you specify for the **resourceName** parameter.\n-  If the **IDQuery** parameter is set to VI_TRUE, this function\n   queries the device ID and checks that the ID is valid for NI-FGEN.\n-  If the **resetDevice** parameter is set to VI_TRUE, this function\n   resets the device to a known state.\n-  Sends initialization commands to set the device to the state\n   necessary for the operation of NI-FGEN.\n-  Returns a session handle that you can use to identify the device in\n   all subsequent NI-FGEN function calls.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'caution': '\nTraditional NI-DAQ and NI-DAQmx device names are not case-sensitive.\nHowever, all IVI names, such as logical names, are case-sensitive. If\nyou use logical names, driver session names, or virtual names in your\nprogram, you must ensure that the name you use matches the name in the\nIVI Configuration Store file exactly, without any variations in the case\nof the characters.\n',
                    'description': '\n| Specifies the resource name of the device to initialize.\n\nFor Traditional NI-DAQ devices, the syntax is DAQ::\\ *n*, where *n* is\nthe device number assigned by MAX, as shown in Example 1.\n\nFor NI-DAQmx devices, the syntax is just the device name specified in\nMAX, as shown in Example 2. Typical default names for NI-DAQmx devices\nin MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by\nright-clicking on the name in MAX and entering a new name.\n\nAn alternate syntax for NI-DAQmx devices consists of DAQ::\\ *NI-DAQmx\ndevice name*, as shown in Example 3. This naming convention allows for\nthe use of an NI-DAQmx device in an application that was originally\ndesigned for a Traditional NI-DAQ device. For example, if the\napplication expects DAQ::1, you can rename the NI-DAQmx device to 1 in\nMAX and pass in DAQ::1 for the resource name, as shown in Example 4.\n\nIf you use the DAQ::\\ *n* syntax and an NI-DAQmx device name already\nexists with that same name, the NI-DAQmx device is matched first.\n\nYou can also pass in the name of an IVI logical name or an IVI virtual\nname configured with the IVI Configuration utility, as shown in Example\n5. A logical name identifies a particular virtual instrument. A virtual\nname identifies a specific device and specifies the initial settings for\nthe session.\n',
                    'table_body': [
                        [
                            '1',
                            'Traditional NI-DAQ device',
                            'DAQ::\\ *1*',
                            '(*1* = device number)'
                        ],
                        [
                            '2',
                            'NI-DAQmx device',
                            '*myDAQmxDevice*',
                            '(*myDAQmxDevice* = device name)'
                        ],
                        [
                            '3',
                            'NI-DAQmx device',
                            'DAQ::\\ *myDAQmxDevice*',
                            '(*myDAQmxDevice* = device name)'
                        ],
                        [
                            '4',
                            'NI-DAQmx device',
                            'DAQ::\\ *2*',
                            '(*2* = device name)'
                        ],
                        [
                            '5',
                            'IVI logical name or IVI virtual name',
                            '*myLogicalName*',
                            '(*myLogicalName* = name)'
                        ]
                    ],
                    'table_header': [
                        'Example #',
                        'Device Type',
                        'Syntax',
                        'Variable'
                    ]
                },
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether you want NI-FGEN to perform an ID query.\n\nWhen you set this parameter to VI_TRUE, NI-FGEN verifies that the\ndevice that you initialize is supported.\n\nCircumstances can arise where sending an ID query to the device is\nundesirable. When you set this parameter to VI_FALSE, the function\ninitializes the device without performing an ID query.\n\n****Defined Values****\n\n**Default Value**: VI_TRUE\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'Perform ID query'
                        ],
                        [
                            'VI_FALSE',
                            'Skip ID query'
                        ]
                    ]
                },
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether you want to reset the device during the initialization\nprocedure. VI_TRUE specifies that the device is reset and performs the\nsame function as the nifgen_Reset function.\n\n****Defined Values****\n\n**Default Value**: VI_TRUE\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'Reset device'
                        ],
                        [
                            'VI_FALSE',
                            'Do not reset device'
                        ]
                    ]
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a session handle that you can use to identify the device in all\nsubsequent NI-FGEN function calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'reset': {
        'documentation': {
            'description': '\nResets the instrument to a known state. This function aborts the\ngeneration, clears all routes, and resets session attributes to the\ndefault values. This function does not, however, commit the session\nproperties or configure the device hardware to its default state.\n',
            'note': '\nFor the NI 5401/5404/5411/5431, this function exhibits the same\nbehavior as the nifgen_ResetDevice function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'revision_query': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Returns the revision numbers of the NI-FGEN and instrument firmware.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the NI-FGEN software revision numbers in the form of a string.\n\nYou must pass a ViChar array with at least 256 bytes.\n'
                },
                'name': 'instrumentDriverRevision',
                'type': 'ViChar[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the instrument firmware revision numbers in the form of a\nstring.\n\nYou must pass a ViChar array with at least 256 bytes.\n'
                },
                'name': 'firmwareRevision',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'self_test': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Runs the instrument self-test routine and returns the test result(s).',
            'note': '\nWhen used on some signal generators, the device is reset after the\nniFgen_self_test function runs. If you use the niFgen_self_test\nfunction, your device may not be in its previously configured state\nafter the function runs.\n'
        },
        'method_name_for_documentation': 'self_test',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies your instrument session. **vi** is obtained from the\nniFgen_init, nifgen_InitWithOptions, or nifgen_InitializeWithChannels\nfunctions and identifies a particular instrument session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nContains the value returned from the instrument self-test. A value of 0\nindicates success.\n',
                    'table_body': [
                        [
                            '0',
                            'Passed self-test'
                        ],
                        [
                            '1',
                            'Self-test failed'
                        ]
                    ],
                    'table_header': [
                        'Self-Test Code',
                        'Description'
                    ]
                },
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the self-test response string from the instrument.\n\nYou must pass a ViChar array with at least 256 bytes.\n'
                },
                'name': 'selfTestMessage',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    }
}
