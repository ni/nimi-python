# -*- coding: utf-8 -*-
# This file is generated from NI-RFSG API metadata version 25.5.0d9999
enums = {
    '5696AmpBand': {
        'values': [
            {
                'name': 'NIRFSG_VAL_250_KHZ_-_250_MHZ',
                'value': 96000
            },
            {
                'name': 'NIRFSG_VAL_250_MHZ_-_1_GHZ',
                'value': 96001
            },
            {
                'name': 'NIRFSG_VAL_1_GHZ_-_2.4_GHZ',
                'value': 96002
            },
            {
                'name': 'NIRFSG_VAL_2.4_GHZ_-_3.86_GHZ',
                'value': 96003
            },
            {
                'name': 'NIRFSG_VAL_3.86_GHZ_-_5.37_GHZ',
                'value': 96004
            },
            {
                'name': 'NIRFSG_VAL_5.37_GHZ_-_7.45_GHZ',
                'value': 96005
            },
            {
                'name': 'NIRFSG_VAL_7.45_GHZ_-_10.4_GHZ',
                'value': 96006
            },
            {
                'name': 'NIRFSG_VAL_10.4_GHZ_-_14.4_GHZ',
                'value': 96007
            },
            {
                'name': 'NIRFSG_VAL_14.4GHZ_-_20_GHZ',
                'value': 96008
            },
            {
                'name': 'NIRFSG_VAL_LOW_GROUP_DELAY_14.4_GHZ_-_17_GHZ',
                'value': 96009
            },
            {
                'name': 'NIRFSG_VAL_LOW_GROUP_DELAY_17_GHZ_-_20_GHZ',
                'value': 96010
            }
        ]
    },
    '5840Modulator': {
        'values': [
            {
                'name': 'NIRFSG_VAL_BYPASS',
                'value': 95000
            },
            {
                'name': 'NIRFSG_VAL_ENABLED',
                'value': 95001
            }
        ]
    },
    'AllowOutOfSpecificationUserSettings': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables out-of-specification user settings.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Enables out-of-specification user settings.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'AmpPath': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Sets the amplification path to use the high power path.'
                },
                'name': 'NIRFSG_VAL_HIGH_POWER',
                'value': 16000
            },
            {
                'documentation': {
                    'description': 'Sets the amplification path to use the low harmonic path.'
                },
                'name': 'NIRFSG_VAL_LOW_HARMONIC',
                'value': 16001
            }
        ]
    },
    'AnlgModFmBand': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies narrowband frequency modulation.'
                },
                'name': 'NIRFSG_VAL_NARROWBAND',
                'value': 17000
            },
            {
                'documentation': {
                    'description': 'Specifies wideband frequency modulation.'
                },
                'name': 'NIRFSG_VAL_WIDEBAND',
                'value': 17001
            }
        ]
    },
    'AnlgModFmNarrowbandIntegrator': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies a range from 100Hz to 1kHz.'
                },
                'name': 'NIRFSG_VAL_100HZ_TO_1KHZ',
                'python_name': '_100hzto1khz',
                'value': 18000
            },
            {
                'documentation': {
                    'description': 'Specifies a range from 1kHz to 10kHz.'
                },
                'name': 'NIRFSG_VAL_1KHZ_TO_10KHZ',
                'python_name': '_1khzto10khz',
                'value': 18001
            },
            {
                'documentation': {
                    'description': 'Specifies a range from 10kHz to 100kHz.'
                },
                'name': 'NIRFSG_VAL_10KHZ_TO_100KHZ',
                'python_name': '_10khzto100khz',
                'value': 18002
            }
        ]
    },
    'AnlgModPmMode': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies high deviation. High deviation comes at the expense of a higher phase noise.'
                },
                'name': 'NIRFSG_VAL_HIGH_DEVIATION',
                'value': 19000
            },
            {
                'documentation': {
                    'description': 'Specifies low phase noise. Low phase noise comes at the expense of a lower maximum deviation.'
                },
                'name': 'NIRFSG_VAL_LOW_PHASE_NOISE',
                'value': 19001
            }
        ]
    },
    'AnlgModType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables analog modulation.'
                },
                'name': 'NIRFSG_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies that the analog modulation type is FM.'
                },
                'name': 'NIRFSG_VAL_FM',
                'value': 2000
            },
            {
                'documentation': {
                    'description': 'Specifies that the analog modulation type is PM.'
                },
                'name': 'NIRFSG_VAL_PM',
                'value': 2001
            },
            {
                'documentation': {
                    'description': 'Specifies that the analog modulation type is AM.'
                },
                'name': 'NIRFSG_VAL_AM',
                'value': 2002
            }
        ]
    },
    'AnlgModWfmType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that the analog modulation waveform type is sine.'
                },
                'name': 'NIRFSG_VAL_SINE',
                'value': 3000
            },
            {
                'documentation': {
                    'description': 'Specifies that the analog modulation waveform type is square.'
                },
                'name': 'NIRFSG_VAL_SQUARE',
                'value': 3001
            },
            {
                'documentation': {
                    'description': 'Specifies that the analog modulation waveform type is triangle.'
                },
                'name': 'NIRFSG_VAL_TRIANGLE',
                'value': 3002
            }
        ]
    },
    'ArbAmplitudeCorrectionMethod': {
        'values': [
            {
                'name': 'NIRFSG_VAL_ANALOG',
                'value': 98000
            },
            {
                'name': 'NIRFSG_VAL_DIGITAL',
                'value': 98001
            }
        ]
    },
    'ArbOnboardSampleClockMode': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Sample rates are generated by a high-resolution clock.'
                },
                'name': 'NIRFSG_VAL_HIGH_RESOLUTION',
                'value': 6000
            },
            {
                'documentation': {
                    'description': 'Sample rates are generated by dividing the source frequency.'
                },
                'name': 'NIRFSG_VAL_DIVIDE_DOWN',
                'value': 6001
            }
        ]
    },
    'AutomaticLevelControl': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables ALC.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Enables the ALC.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'AutomaticPowerSearch': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables automatic power search.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Enables automatic power search.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'AutomaticThermalCorrection': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Automatic thermal correction is disabled.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Automatic thermal correction is enabled.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'CoercePowerLevelToMaxPower': {
        'values': [
            {
                'name': 'NIRFSG_VAL_DISABLED',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_ENABLED',
                'value': 1
            }
        ]
    },
    'ConfigListTrigDigEdgeEdge': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the rising edge as the active edge. The rising edge occurs when the signal transitions from low level to high level.'
                },
                'name': 'NIRFSG_VAL_RISING_EDGE',
                'value': 0
            }
        ]
    },
    'ConfigListTrigType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Generation starts immediately, but the list does not advance.'
                },
                'name': 'NIRFSG_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Data operation does not start until a digital edge is detected. The source of the digital edge is specified in the NIRFSG_ATTR_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE attribute, and the active edge is always rising.'
                },
                'name': 'NIRFSG_VAL_DIGITAL_EDGE',
                'value': 1
            }
        ]
    },
    'ConfigurationListRepeat': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'NI-RFSG runs the configuration list continuously.'
                },
                'name': 'NIRFSG_VAL_CONFIGURATION_LIST_REPEAT_CONTINUOUS',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_MANUAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'NI-RFSG runs the configuration list only once.'
                },
                'name': 'NIRFSG_VAL_CONFIGURATION_LIST_REPEAT_SINGLE',
                'value': 1
            },
            {
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER',
                'value': 1
            }
        ]
    },
    'DacDecoderMode': {
        'values': [
            {
                'name': 'NIRFSG_VAL_MAX_SNR',
                'value': 28001
            },
            {
                'name': 'NIRFSG_VAL_MAX_LINEARITY',
                'value': 28002
            }
        ]
    },
    'DebuggingOptions': {
        'values': [
            {
                'name': 'NIRFSG_VAL_PLL_LOCK_COUNT',
                'value': 1
            },
            {
                'name': 'NIRFSG_VAL_MEASURE_IO_TIME',
                'value': 2
            }
        ]
    },
    'DeembeddingTypeAttrVals': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'De-embedding is not applied to the measurement.'
                },
                'name': 'NIRFSG_VAL_DEEMBEDDING_TYPE_NONE',
                'value': 25000
            },
            {
                'documentation': {
                    'description': 'De-embeds the measurement using only the gain term.'
                },
                'name': 'NIRFSG_VAL_DEEMBEDDING_TYPE_SCALAR',
                'value': 25001
            },
            {
                'documentation': {
                    'description': 'De-embeds the measurement using the gain term and the reflection term.'
                },
                'name': 'NIRFSG_VAL_DEEMBEDDING_TYPE_VECTOR',
                'value': 25002
            }
        ]
    },
    'DigModType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables digital modulation.'
                },
                'name': 'NIRFSG_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Specifies that the digital modulation type is frequency-shift keying (FSK).'
                },
                'name': 'NIRFSG_VAL_FSK',
                'value': 4000
            },
            {
                'documentation': {
                    'description': 'Specifies that the digital modulation type is on-off keying (OOK).'
                },
                'name': 'NIRFSG_VAL_OOK',
                'value': 4001
            },
            {
                'documentation': {
                    'description': 'Specifies that the digital modulation type is phase-shift keying (PSK).'
                },
                'name': 'NIRFSG_VAL_PSK',
                'value': 4002
            }
        ]
    },
    'DigModWfmType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that the digital modulation waveform type is pseudorandom bit sequence (PRBS).'
                },
                'name': 'NIRFSG_VAL_PRBS',
                'value': 5000
            },
            {
                'documentation': {
                    'description': 'Specifies that the digital modulation waveform type is user defined. To specify the user-defined waveform, call the nirfsg_ConfigureDigitalModulationUserDefinedWaveform function.'
                },
                'name': 'NIRFSG_VAL_USER_DEFINED',
                'value': 5001
            }
        ]
    },
    'DigitalEqualizationEnabled': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Filter is not applied'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Filter is applied.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'DirectDownload': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The RF In local oscillator signal is not present at the front panel LO OUT connector.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The RF In local oscillator signal is present at the front panel LO OUT connector.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'The RF IN local oscillator signal may or may not be present at the front panel LO OUT connector, because NI-RFSA may be controlling it.'
                },
                'name': 'NIRFSG_VAL_UNSPECIFIED',
                'value': -2
            }
        ]
    },
    'FilterType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'No filter type is applied.'
                },
                'name': 'NIRFSG_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Applies a root-raised cosine filter to the data with the alpha value specified with the NIRFSG_ATTR_ARB_FILTER_ROOT_RAISED_COSINE_ALPHA attribute.'
                },
                'name': 'NIRFSG_VAL_ARB_FILTER_TYPE_ROOT_RAISED_COSINE',
                'value': 10001
            },
            {
                'documentation': {
                    'description': 'Applies a raised cosine filter to the data with the alpha value specified with the NIRFSG_ATTR_ARB_FILTER_RAISED_COSINE_ALPHA attribute.'
                },
                'name': 'NIRFSG_VAL_ARB_FILTER_TYPE_RAISED_COSINE',
                'value': 10002
            }
        ]
    },
    'Format': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Results in a linear interpolation of the magnitude and a separate linear interpolation of the phase.'
                },
                'name': 'NIRFSG_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_AND_PHASE',
                'value': 26001
            },
            {
                'documentation': {
                    'description': 'Results in a linear interpolation of the magnitude, in decibels, and a separate linear interpolation of the phase.'
                },
                'name': 'NIRFSG_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_DB_AND_PHASE',
                'value': 26002
            },
            {
                'documentation': {
                    'description': 'Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion.'
                },
                'name': 'NIRFSG_VAL_LINEAR_INTERPOLATION_FORMAT_REAL_AND_IMAGINARY',
                'value': 26000
            }
        ]
    },
    'FrequencyResponseFilterEnabled': {
        'values': [
            {
                'name': 'NIRFSG_VAL_DISABLED',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_ENABLED',
                'value': 1
            }
        ]
    },
    'FrequencySettlingUnits': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the time to wait after the frequency PLL locks.'
                },
                'name': 'NIRFSG_VAL_TIME_AFTER_LOCK',
                'value': 12000
            },
            {
                'documentation': {
                    'description': 'Specifies the time to wait after all writes occur to change the frequency'
                },
                'name': 'NIRFSG_VAL_TIME_AFTER_IO',
                'value': 12001
            },
            {
                'documentation': {
                    'description': 'Specifies the minimum frequency accuracy when settling completes. Units are in parts per million (PPM or 1E-6).'
                },
                'name': 'NIRFSG_VAL_PPM',
                'value': 12002
            }
        ]
    },
    'GainStateFromSelfCal': {
        'values': [
            {
                'name': 'NIRFSG_VAL_DISABLED',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_ENABLED',
                'value': 1
            }
        ]
    },
    'GenerationMode': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Configures the RF signal generator to generate a CW signal.'
                },
                'name': 'NIRFSG_VAL_CW',
                'value': 1000
            },
            {
                'documentation': {
                    'description': 'Configures the RF signal generator to generate the arbitrary waveform specified by the NIRFSG_ATTR_ARB_SELECTED_WAVEFORM attribute.'
                },
                'name': 'NIRFSG_VAL_ARB_WAVEFORM',
                'value': 1001
            },
            {
                'documentation': {
                    'description': 'Configures the RF signal generator to generate arbitrary waveforms as directed by the NIRFSG_ATTR_SELECTED_SCRIPT attribute.'
                },
                'name': 'NIRFSG_VAL_SCRIPT',
                'value': 1002
            }
        ]
    },
    'IQOutPortTermCfg': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Sets the terminal configuration to differential.'
                },
                'name': 'NIRFSG_VAL_DIFFERENTIAL',
                'value': 15000
            },
            {
                'documentation': {
                    'description': 'Sets the terminal configuration to single-ended.'
                },
                'name': 'NIRFSG_VAL_SINGLE_ENDED',
                'value': 15001
            }
        ]
    },
    'ImpairmentsFilterEnabled': {
        'values': [
            {
                'name': 'NIRFSG_VAL_DISABLED',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_ENABLED',
                'value': 1
            }
        ]
    },
    'Lo1OutputFilter': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'yet to be defined'
                },
                'name': 'NIRFSG_VAL_MANUAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'yet to be defined'
                },
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER',
                'value': 1
            }
        ]
    },
    'LoOutEnabled': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The local oscillator signal is present at the LO OUT front panel connector.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_MANUAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The local oscillator signal is  not present at the LO OUT front panel connector..'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            },
            {
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER',
                'value': 1
            }
        ]
    },
    'LoOutExportConfigureFromRFSaEnable': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Do not allow NI-RFSA to control the NI-RFSG local oscillator export.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_MANUAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Allow NI-RFSA to control the NI-RFSG local oscillator export.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            },
            {
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER',
                'value': 1
            }
        ]
    },
    'LoOutSource': {
        'values': [
            {
                'name': 'NIRFSG_VAL_INTERNAL_LO',
                'value': 'Internal_LO'
            },
            {
                'name': 'NIRFSG_VAL_ONBOARD',
                'value': 'Onboard'
            }
        ]
    },
    'LoPlLfractionalModeEnabled': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables fractional mode for the LO PLL.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_MANUAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Enables fractional mode for the LO PLL.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            },
            {
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER',
                'value': 1
            }
        ]
    },
    'LoadOptions': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'NI-RFSG loads all the configurations to the session.'
                },
                'name': 'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS_SKIP_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'NI-RFSG skips loading the waveform configurations to the session.'
                },
                'name': 'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS_SKIP_WAVEFORMS',
                'value': 1
            }
        ]
    },
    'LoopBandwidth': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Uses the narrowest loop bandwidth setting for the PLL.'
                },
                'name': 'NIRFSG_VAL_NARROW',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Uses the medium loop bandwidth setting for the PLL.'
                },
                'name': 'NIRFSG_VAL_MEDIUM',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Uses the widest loop bandwidth setting for the PLL.'
                },
                'name': 'NIRFSG_VAL_WIDE',
                'value': 2
            }
        ]
    },
    'MarkerEventOutputBehavior': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the Marker Event output behavior as pulse.'
                },
                'name': 'NIRFSG_VAL_PULSE',
                'value': 23000
            },
            {
                'documentation': {
                    'description': 'Specifies the Marker Event output behavior as toggle.'
                },
                'name': 'NIRFSG_VAL_TOGGLE',
                'value': 23001
            }
        ]
    },
    'MarkerEventPulseWidthUnits': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the Marker Event pulse width units as seconds.'
                },
                'name': 'NIRFSG_VAL_SECONDS',
                'value': 22000
            },
            {
                'documentation': {
                    'description': 'Specifies the Marker Event pulse width units as Sample Clock periods.'
                },
                'name': 'NIRFSG_VAL_SAMPLE_CLOCK_PERIODS',
                'value': 22001
            }
        ]
    },
    'MarkerEventToggleInitialState': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the initial state of the Marker Event toggle behavior as digital low.'
                },
                'name': 'NIRFSG_VAL_DIGITAL_LOW',
                'value': 21000
            },
            {
                'documentation': {
                    'description': 'Specifies the initial state of the Marker Event toggle behavior as digital high.'
                },
                'name': 'NIRFSG_VAL_DIGITAL_HIGH',
                'value': 21001
            }
        ]
    },
    'MismatchCorrectionEnabled': {
        'values': [
            {
                'name': 'NIRFSG_VAL_DISABLED',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_ENABLED',
                'value': 1
            }
        ]
    },
    'Module': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The AWG associated with the primary module.'
                },
                'name': 'NIRFSG_VAL_AWG',
                'value': 13001
            },
            {
                'documentation': {
                    'description': 'The LO associated with the primary module.'
                },
                'name': 'NIRFSG_VAL_LO',
                'value': 13002
            },
            {
                'documentation': {
                    'description': 'The stand-alone device or the main module in a multi-module device.'
                },
                'name': 'NIRFSG_VAL_PRIMARY_MODULE',
                'value': 13000
            }
        ]
    },
    'OffsetUnits': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the unit in percentage.'
                },
                'name': 'NIRFSG_VAL_PERCENT',
                'value': 11000
            },
            {
                'documentation': {
                    'description': 'Specifies the unit in volts.'
                },
                'name': 'NIRFSG_VAL_VOLTS',
                'value': 11001
            }
        ]
    },
    'OptimizePathForSignalBandwidth': {
        'values': [
            {
                'name': 'NIRFSG_VAL_DISABLED',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_ENABLED',
                'value': 1
            }
        ]
    },
    'OutputPort': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Enables the RF OUT port. This value is not valid for the PXIe-5820.'
                },
                'name': 'NIRFSG_VAL_RF_OUT',
                'value': 14000
            },
            {
                'documentation': {
                    'description': 'Enables the I/Q OUT port. This value is valid on only the PXIe-5645 and PXIe-5820.'
                },
                'name': 'NIRFSG_VAL_IQ_OUT',
                'value': 14001
            },
            {
                'documentation': {
                    'description': 'Enables the CAL OUT port.'
                },
                'name': 'NIRFSG_VAL_CAL_OUT',
                'value': 14002
            },
            {
                'documentation': {
                    'description': 'Enables the I connectors of the I/Q OUT port. This value is valid on only the PXIe-5645.'
                },
                'name': 'NIRFSG_VAL_I_ONLY',
                'value': 14003
            }
        ]
    },
    'OverflowErrorReporting': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'NI-RFSG returns a warning when an OSP overflow occurs.'
                },
                'name': 'NIRFSG_VAL_ERROR_REPORTING_WARNING',
                'value': 1301
            },
            {
                'documentation': {
                    'description': 'NI-RFSG does not return an error or a warning when an OSP overflow occurs.'
                },
                'name': 'NIRFSG_VAL_ERROR_REPORTING_DISABLED',
                'value': 1302
            }
        ]
    },
    'PhaseContinuityEnabled': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The arbitrary waveform may be repeated to ensure phase continuity after upconversion. This setting could cause waveform size to increase.'
                },
                'name': 'NIRFSG_VAL_AUTO',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'The arbitrary waveform plays back without regard to any possible phase discontinuities introduced by upconversion. The time duration of the original waveform is maintained.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The arbitrary waveform may be repeated to ensure phase continuity after upconversion. Enabling this attribute could cause waveform size to increase.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'PortTypes': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the PXIe-5840 RF OUT port.'
                },
                'name': 'NIRFSG_VAL_PORT_RF_OUT',
                'value': 14501
            },
            {
                'documentation': {
                    'description': 'Specifies the PXIe-5840 RF IN port. This value is not supported as the first element of an array.'
                },
                'name': 'NIRFSG_VAL_PORT_RF_IN',
                'value': 14500
            }
        ]
    },
    'PowerLevelType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Indicates the desired power averaged in time. The driver maximizes the dynamic range by scaling the I/Q waveform so that its peak magnitude is equal to one. If your write more than one waveform, NI-RFSG scales each waveform without preserving the power level ratio between the waveforms. This value is not valid for the PXIe-5820.'
                },
                'name': 'NIRFSG_VAL_AVERAGE_POWER',
                'value': 7000
            },
            {
                'documentation': {
                    'description': 'Indicates the maximum power level of the RF signal averaged over one period of the RF carrier frequency (the peak envelope power). This setting requires that the magnitude of the I/Q waveform must always be less than or equal to one. When using peak power, the power level of the RF signal matches the specified power level at moments when the magnitude of the I/Q waveform equals one. If you write more than one waveform, the relative scaling between waveforms is preserved. In peak power mode, waveforms are scaled according to the NIRFSG_ATTR_ARB_WAVEFORM_SOFTWARE_SCALING_FACTOR attribute. You can use the NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT attribute in conjunction with the NIRFSG_ATTR_POWER_LEVEL attribute when the NIRFSG_ATTR_POWER_LEVEL_TYPE attribute is set to NIRFSG_VAL_PEAK_POWER.'
                },
                'name': 'NIRFSG_VAL_PEAK_POWER',
                'value': 7001
            }
        ]
    },
    'PpaInheritance': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Errors out if different values are detected in the script.'
                },
                'name': 'NIRFSG_VAL_EXACT_MATCH',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Uses the minimum value found in the script.'
                },
                'name': 'NIRFSG_VAL_MINIMUM',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Uses the maximum value found in the script.'
                },
                'name': 'NIRFSG_VAL_MAXIMUM',
                'value': 2
            }
        ]
    },
    'PulseModulationMode': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Provides for a more optimal power output match for the device during the off cycle of the pulse mode operation. Not supported on PXIe-5842'
                },
                'name': 'NIRFSG_VAL_OPTIMAL_MATCH',
                'value': 20000
            },
            {
                'documentation': {
                    'description': 'Allows for the best on/off power ratio of the pulsed signal.'
                },
                'name': 'NIRFSG_VAL_HIGH_ISOLATION',
                'value': 20001
            },
            {
                'documentation': {
                    'description': 'Analog switch blanking. Balance between switching speed and on/off power ratio of the pulsed signal.'
                },
                'name': 'NIRFSG_VAL_ANALOG',
                'value': 20002
            },
            {
                'documentation': {
                    'description': 'Digital only modulation. Provides the best on/off switching speed of the pulsed signal at the cost of signal isolation.'
                },
                'name': 'NIRFSG_VAL_DIGITAL',
                'value': 20003
            }
        ]
    },
    'RFBlanking': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'RF blanking is disabled.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'RF blanking is enabled.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'RFFilter': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'yet to be defined'
                },
                'name': 'NIRFSG_VAL_HI_FREQ_MOD',
                'value': '0'
            },
            {
                'name': 'NIRFSG_VAL_CONFIGURATION_SETTLED_EVENT',
                'value': 7
            },
            {
                'documentation': {
                    'description': 'yet to be defined'
                },
                'name': 'NIRFSG_VAL_LO_FREQ_MOD_4000',
                'value': '1'
            },
            {
                'documentation': {
                    'description': 'yet to be defined'
                },
                'name': 'NIRFSG_VAL_LO_FREQ_MOD_2500',
                'value': '2'
            }
        ]
    },
    'RFInLoExportEnabled': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The RF IN local oscillator signal may or may not be present at the front panel LO OUT connector, because NI-RFSA may'
                },
                'name': 'NIRFSG_VAL_UNSPECIFIED',
                'value': -2
            },
            {
                'documentation': {
                    'description': 'The RF In local oscillator signal is not present at the front panel LO OUT connector.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_MANUAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The RF In local oscillator signal is present at the front panel LO OUT connector.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            },
            {
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER',
                'value': 1
            }
        ]
    },
    'RFPowerMeterEnabled': {
        'values': [
            {
                'name': 'NIRFSG_VAL_DISABLED',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_ENABLED',
                'value': 1
            }
        ]
    },
    'RFPowerProtectionEnabled': {
        'values': [
            {
                'name': 'NIRFSG_VAL_DISABLED',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_ENABLED',
                'value': 1
            }
        ]
    },
    'ReferenceClockExportedRate': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Uses a 10MHz Reference Clock rate.'
                },
                'name': 'NIRFSG_VAL_10MHZ',
                'python_name': '_10mhz',
                'value': 10000000
            },
            {
                'documentation': {
                    'description': 'Uses a 100MHz Reference Clock rate.'
                },
                'name': 'NIRFSG_VAL_100MHZ',
                'python_name': '_100mhz',
                'value': 100000000.0
            },
            {
                'documentation': {
                    'description': 'Uses a 1GHz Reference Clock rate.'
                },
                'name': 'NIRFSG_VAL_1GHZ',
                'python_name': '_1ghz',
                'value': 1000000000.0
            }
        ]
    },
    'ReferenceClockRate': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Uses the default Reference Clock rate for the device or automatically detects the Reference Clock rate if the device supports it.'
                },
                'name': 'NIRFSG_VAL_AUTO',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'Uses a 10MHz Reference Clock rate.'
                },
                'name': 'NIRFSG_VAL_10MHZ',
                'python_name': '_10mhz',
                'value': 10000000
            }
        ]
    },
    'RelativeTo': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The reference position is relative to the current position.'
                },
                'name': 'NIRFSG_VAL_CURRENT_POSITION',
                'value': 8001
            },
            {
                'documentation': {
                    'description': 'The reference position is relative to the start of the waveform.'
                },
                'name': 'NIRFSG_VAL_START_OF_WAVEFORM',
                'value': 8000
            }
        ]
    },
    'ResetOptions': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'NI-RFSG skips resetting the waveform configurations.'
                },
                'name': 'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_WAVEFORMS',
                'value': 1
            },
            {
                'name': 'NIRFSG_VAL_MANUAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'NI-RFSG skips resetting the de-embedding tables.'
                },
                'name': 'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_DEEMBEDDING_TABLES',
                'value': 8
            },
            {
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'NI-RFSG skips resetting the scripts.'
                },
                'name': 'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_SCRIPTS',
                'value': 2
            },
            {
                'name': 'NIRFSG_VAL_MARKER_EVENT',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'NI-RFSG resets all configurations.'
                },
                'name': 'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_NONE',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_SELF_CAL_IMAGE_SUPPRESSION',
                'value': 8
            }
        ]
    },
    'ResetWithOptionsStepsToOmit': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Omits deleting de-embedding tables. This step is valid only for the PXIe-5830/5831/5832/5840.'
                },
                'name': 'NIRFSG_VAL_RESET_WITH_OPTIONS_DEEMBEDDING_TABLES',
                'value': 8
            },
            {
                'documentation': {
                    'description': 'No step is omitted during reset.'
                },
                'name': 'NIRFSG_VAL_RESET_WITH_OPTIONS_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after a reset.'
                },
                'name': 'NIRFSG_VAL_RESET_WITH_OPTIONS_ROUTES',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Omits clearing scripts.'
                },
                'name': 'NIRFSG_VAL_RESET_WITH_OPTIONS_SCRIPTS',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Omits clearing waveforms.'
                },
                'name': 'NIRFSG_VAL_RESET_WITH_OPTIONS_WAVEFORMS',
                'value': 1
            }
        ]
    },
    'ScriptTrigDigEdgeEdge': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Asserts the trigger when the signal transitions from low level to high level.'
                },
                'name': 'NIRFSG_VAL_RISING_EDGE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Asserts the trigger when the signal transitions from high level to low level.'
                },
                'name': 'NIRFSG_VAL_FALLING_EDGE',
                'value': 1
            }
        ]
    },
    'ScriptTrigDigLevelActiveLevel': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Trigger when the digital trigger signal is high.'
                },
                'name': 'NIRFSG_VAL_ACTIVE_HIGH',
                'value': 9000
            },
            {
                'documentation': {
                    'description': 'Trigger when the digital trigger signal is low.'
                },
                'name': 'NIRFSG_VAL_ACTIVE_LOW',
                'value': 9001
            }
        ]
    },
    'ScriptTrigType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'No trigger is configured. Signal generation starts immediately.'
                },
                'name': 'NIRFSG_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The data operation does not start until a digital edge is detected. The source of the digital edge is specified with the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute, and the active edge is specified with the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE attribute.'
                },
                'name': 'NIRFSG_VAL_DIGITAL_EDGE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'The data operation does not start until the digital level is detected. The source of the digital level is specified in the NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE attribute, and the active level is specified in the NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL attribute.'
                },
                'name': 'NIRFSG_VAL_DIGITAL_LEVEL',
                'value': 8000
            },
            {
                'documentation': {
                    'description': 'The data operation does not start until a software trigger occurs. You can create a software event by calling the nirfsg_SendSoftwareEdgeTrigger function.'
                },
                'name': 'NIRFSG_VAL_SOFTWARE',
                'value': 2
            }
        ]
    },
    'SelfCalibrateRangeStepsToOmit': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted.'
                },
                'name': 'NIRFSG_VAL_SELF_CAL_IMAGE_SUPPRESSION',
                'value': 8
            },
            {
                'documentation': {
                    'description': 'Omits the LO Self Cal step. If you omit this step, the power level of the LO is not adjusted.'
                },
                'name': 'NIRFSG_VAL_SELF_CAL_LO_SELF_CAL',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'No calibration steps are omitted.'
                },
                'name': 'NIRFSG_VAL_SELF_CAL_OMIT_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Omits the Power Level Accuracy step. If you omit this step, the power level accuracy of the device is not adjusted.'
                },
                'name': 'NIRFSG_VAL_SELF_CAL_POWER_LEVEL_ACCURACY',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.'
                },
                'name': 'NIRFSG_VAL_SELF_CAL_RESIDUAL_LO_POWER',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                },
                'name': 'NIRFSG_VAL_SELF_CAL_SYNTHESIZER_ALIGNMENT',
                'value': 16
            }
        ]
    },
    'Signal': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Exports a Configuration Settled Event.'
                },
                'name': 'NIRFSG_VAL_CONFIGURATION_SETTLED_EVENT',
                'value': 7
            },
            {
                'documentation': {
                    'description': 'Exports a Start Trigger.'
                },
                'name': 'NIRFSG_VAL_START_TRIGGER',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Exports a Script Trigger.'
                },
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Exports a Marker Event.'
                },
                'name': 'NIRFSG_VAL_MARKER_EVENT',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Exports the Reference Clock.'
                },
                'name': 'NIRFSG_VAL_REF_CLOCK',
                'value': 3
            },
            {
                'documentation': {
                    'description': 'Exports a Started Event.'
                },
                'name': 'NIRFSG_VAL_STARTED_EVENT',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Exports a Done Event.'
                },
                'name': 'NIRFSG_VAL_DONE_EVENT',
                'value': 5
            },
            {
                'documentation': {
                    'description': 'Exports a Configuration List Step Trigger.'
                },
                'name': 'NIRFSG_VAL_CONFIGURATION_LIST_STEP_TRIGGER',
                'value': 6
            }
        ]
    },
    'SoftwareTriggerType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the Script Trigger.'
                },
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Specifies the Start Trigger.'
                },
                'name': 'NIRFSG_VAL_START_TRIGGER',
                'value': 0
            }
        ]
    },
    'SparameterOrientation': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Port 1 of the S2P is oriented towards the DUT port.'
                },
                'name': 'NIRFSG_VAL_PORT1_TOWARDS_DUT',
                'value': 24000
            },
            {
                'documentation': {
                    'description': 'Port 2 of the S2P is oriented towards the DUT port.'
                },
                'name': 'NIRFSG_VAL_PORT2_TOWARDS_DUT',
                'value': 24001
            }
        ]
    },
    'StartTrigDigEdgeEdge': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Occurs when the signal transitions from low level to high level.'
                },
                'name': 'NIRFSG_VAL_RISING_EDGE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Occurs when the signal transitions from high level to low level.'
                },
                'name': 'NIRFSG_VAL_FALLING_EDGE',
                'value': 1
            }
        ]
    },
    'StartTrigType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'No trigger is configured.'
                },
                'name': 'NIRFSG_VAL_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'The data operation does not start until a digital edge is detected. The source of the digital edge is specified with the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute, and the active edge is specified in the NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE attribute.'
                },
                'name': 'NIRFSG_VAL_DIGITAL_EDGE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'The data operation does not start until a software event occurs. You may create a software trigger by calling the nirfsg_SendSoftwareEdgeTrigger function.'
                },
                'name': 'NIRFSG_VAL_SOFTWARE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'The data operation does not start until the endpoint reaches the threshold specified in the NIRFSG_ATTR_P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL attribute.'
                },
                'name': 'NIRFSG_VAL_P2P_ENDPOINT_FULLNESS',
                'value': 3
            }
        ]
    },
    'StatusChecksDisabled': {
        'values': [
            {
                'name': 'NIRFSG_VAL_NONE',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_POWER_PROTECTION',
                'value': 1
            },
            {
                'name': 'NIRFSG_VAL_DSP',
                'value': 2
            },
            {
                'name': 'NIRFSG_VAL_LO_PLL',
                'value': 4
            },
            {
                'name': 'NIRFSG_VAL_ALL',
                'value': -1
            }
        ]
    },
    'Sts5532SignalPath': {
        'values': [
            {
                'name': 'NIRFSG_VAL_DIRECT',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_GAIN',
                'value': 1
            },
            {
                'name': 'NIRFSG_VAL_LOOP',
                'value': 2
            },
            {
                'name': 'NIRFSG_VAL_AUTO',
                'value': -1
            }
        ]
    },
    'TimerStartSource': {
        'values': [
            {
                'name': 'NIRFSG_VAL_STARTTRIGGER',
                'value': 'StartTrigger'
            },
            {
                'name': 'NIRFSG_VAL_SCRIPTTRIGGER0',
                'value': 'ScriptTrigger0'
            }
        ]
    },
    'UpconverterFrequencyOffsetMode': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute has been set and can be avoided.'
                },
                'name': 'NIRFSG_VAL_AUTO',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute has been set and can be avoided. NI-RFSG returns an error if the NIRFSG_ATTR_SIGNAL_BANDWIDTH attribute has not been set, or if the signal bandwidth is too large.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'NI-RFSG uses the offset that you specified with the NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET or NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY attributes.'
                },
                'name': 'NIRFSG_VAL_USER_DEFINED',
                'value': 5001
            }
        ]
    },
    'UseCalibration': {
        'values': [
            {
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'VcoSelfCalEnabled': {
        'values': [
            {
                'name': 'NIRFSG_VAL_DISABLED',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_ENABLED',
                'value': 1
            }
        ]
    },
    'WaveformSource': {
        'values': [
            {
                'name': 'NIRFSG_VAL_NONE',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_WGEN',
                'value': 27000
            },
            {
                'name': 'NIRFSG_VAL_P2P',
                'value': 27001
            },
            {
                'name': 'NIRFSG_VAL_USER',
                'value': 27002
            }
        ]
    },
    'WriteWaveformBurstDetection': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Burst detection is disabled.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Burst detection is enabled.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'WriteWaveformBurstDetectionMode': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'NI-RFSG automatically detects the burst start and burst stop locations by analyzing the waveform.'
                },
                'name': 'NIRFSG_VAL_AUTO',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'User sets the burst detection parameters.'
                },
                'name': 'NIRFSG_VAL_MANUAL',
                'value': 0
            }
        ]
    },
    'WriteWaveformNormalization': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables normalization on the waveform.'
                },
                'name': 'NIRFSG_VAL_DISABLE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Enables normalization on a waveform to transform the waveform data so that its maximum is 1.00 and its minimum is -1.00'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            }
        ]
    },
    'YigMainCoilDrive': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Adjusts the YIG main coil for an underdamped response.'
                },
                'name': 'NIRFSG_VAL_MANUAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Adjusts the YIG main coil for an overdamped response.'
                },
                'name': 'NIRFSG_VAL_FAST',
                'value': 1
            }
        ]
    }
}
