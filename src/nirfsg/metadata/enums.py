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
    'ArbSampleClockSource': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Uses the AWG module onboard clock as the Sample Clock source.'
                },
                'name': 'NIRFSG_VAL_ONBOARD_CLOCK_STR',
                'value': 'OnboardClock'
            },
            {
                'documentation': {
                    'description': 'Uses the external clock as the Sample Clock source.'
                },
                'name': 'NIRFSG_VAL_CLK_IN_STR',
                'value': 'ClkIn'
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
    'ConfigListTrigDigEdgeSource': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The trigger is received on PFI 0.'
                },
                'name': 'NIRFSG_VAL_PFI0_STR',
                'value': 'PFI0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI 1.'
                },
                'name': 'NIRFSG_VAL_PFI1_STR',
                'value': 'PFI1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 0.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG0_STR',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 1.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG1_STR',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 2.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG2_STR',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 3.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG3_STR',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 4.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG4_STR',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 5.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG5_STR',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 6.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG6_STR',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 7.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG7_STR',
                'value': 'PXI_Trig7'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.'
                },
                'name': 'NIRFSG_VAL_PXI_STAR_STR',
                'value': 'PXI_Star'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5840/5841/5842.'
                },
                'name': 'NIRFSG_VAL_PXIE_DSTARB_STR',
                'value': 'PXIe_DStarB'
            },
            {
                'documentation': {
                    'description': 'The trigger is received from the Marker Event 0.'
                },
                'name': 'NIRFSG_VAL_MARKER0_EVENT_STR',
                'value': 'Marker0Event'
            },
            {
                'documentation': {
                    'description': 'The trigger is received from the Marker Event 1.'
                },
                'name': 'NIRFSG_VAL_MARKER1_EVENT_STR',
                'value': 'Marker1Event'
            },
            {
                'documentation': {
                    'description': 'The trigger is received from the Marker Event 2.'
                },
                'name': 'NIRFSG_VAL_MARKER2_EVENT_STR',
                'value': 'Marker2Event'
            },
            {
                'documentation': {
                    'description': 'The trigger is received from the Marker Event 3.'
                },
                'name': 'NIRFSG_VAL_MARKER3_EVENT_STR',
                'value': 'Marker3Event'
            },
            {
                'documentation': {
                    'description': 'The trigger is received from the Timer Event.'
                },
                'name': 'NIRFSG_VAL_TIMER_EVENT_STR',
                'value': 'TimerEvent'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the TRIG IN/OUT terminal. This value is valid on only the PXIe-5654/5654 with PXIe-5696.'
                },
                'name': 'NIRFSG_VAL_TRIG_IN_STR',
                'value': 'TrigIn'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI0 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO0_STR',
                'value': 'DIO/PFI0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI1 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO1_STR',
                'value': 'DIO/PFI1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI2 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO2_STR',
                'value': 'DIO/PFI2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI3 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO3_STR',
                'value': 'DIO/PFI3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI4 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO4_STR',
                'value': 'DIO/PFI4'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI5 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO5_STR',
                'value': 'DIO/PFI5'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI6 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO6_STR',
                'value': 'DIO/PFI6'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI7 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO7_STR',
                'value': 'DIO/PFI7'
            }
        ]
    },
    'ConfigListTrigExportOutputTerm': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The signal is not exported.'
                },
                'name': 'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                'value': ''
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. '
                },
                'name': 'NIRFSG_VAL_PFI0_STR',
                'value': 'PFI0'
            },
            {
                'documentation': {
                    'description': 'The signal is exported on PFI 1 connector.'
                },
                'name': 'NIRFSG_VAL_PFI1_STR',
                'value': 'PFI1'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 0. .'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG0_STR',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 0. '
                },
                'name': 'NIRFSG_VAL_PXI_TRIG1_STR',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 2.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG2_STR',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 3.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG3_STR',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 4.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG4_STR',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 5.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG5_STR',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 6.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG6_STR',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5840/5841/5842.'
                },
                'name': 'NIRFSG_VAL_PXIE_DSTARC_STR',
                'value': 'PXIe_DStarC'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the TRIG IN/OUT terminal. This value is valid on only the PXIe-5654/5654 with PXIe-5696.'
                },
                'name': 'NIRFSG_VAL_TRIG_OUT_STR',
                'value': 'TrigOut'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI0 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO0_STR',
                'value': 'DIO/PFI0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI1 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO1_STR',
                'value': 'DIO/PFI1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI2 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO2_STR',
                'value': 'DIO/PFI2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI3 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO3_STR',
                'value': 'DIO/PFI3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI4 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO4_STR',
                'value': 'DIO/PFI4'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI5 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO5_STR',
                'value': 'DIO/PFI5'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI6 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO6_STR',
                'value': 'DIO/PFI6'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI7 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO7_STR',
                'value': 'DIO/PFI7'
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
                    'description': 'Data operation does not start until a digital edge is detected. The source of the digital edge is specified in the %attribute{digital edge configuration list step trigger source} attribute, and the active edge is always rising.'
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
    'ConfigurationSettledEventExportOutputTerm': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The signal is not exported.'
                },
                'name': 'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                'value': ''
            },
            {
                'documentation': {
                    'description': 'PXI trigger line 0.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG0_STR',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': 'PXI trigger line 1.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG1_STR',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': 'PXI trigger line 2.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG2_STR',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': 'PXI trigger line 3.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG3_STR',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': 'PXI trigger line 4.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG4_STR',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': 'PXI trigger line 5.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG5_STR',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': 'PXI trigger line 6.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG6_STR',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': 'PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842.'
                },
                'name': 'NIRFSG_VAL_PXIE_DSTARC_STR',
                'value': 'PXIe_DStarC'
            },
            {
                'documentation': {
                    'description': 'TRIG IN/OUT terminal.'
                },
                'name': 'NIRFSG_VAL_TRIG_OUT_STR',
                'value': 'TrigOut'
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
                'name': 'NIRFSG_VAL_NONE',
                'value': 0
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
                    'description': 'Specifies that the digital modulation waveform type is user defined. To specify the user-defined waveform, call the %function{configure digital modulation user defined waveform} function.'
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
    'DoneEventExportOutputTerm': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The signal is not exported.'
                },
                'name': 'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                'value': ''
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.'
                },
                'name': 'NIRFSG_VAL_PFI0_STR',
                'value': 'PFI0'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 1 connector.'
                },
                'name': 'NIRFSG_VAL_PFI1_STR',
                'value': 'PFI1'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 4 connector.'
                },
                'name': 'NIRFSG_VAL_PFI4_STR',
                'value': 'PFI4'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 5 connector.'
                },
                'name': 'NIRFSG_VAL_PFI5_STR',
                'value': 'PFI5'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 0.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG0_STR',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 1.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG1_STR',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 2.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG2_STR',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 3.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG3_STR',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 4.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG4_STR',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 5.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG5_STR',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 6.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG6_STR',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.'
                },
                'name': 'NIRFSG_VAL_PXIE_DSTARC_STR',
                'value': 'PXIe_DStarC'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI0 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO0_STR',
                'value': 'DIO/PFI0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI1 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO1_STR',
                'value': 'DIO/PFI1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI2 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO2_STR',
                'value': 'DIO/PFI2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI3 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO3_STR',
                'value': 'DIO/PFI3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI4 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO4_STR',
                'value': 'DIO/PFI4'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI5 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO5_STR',
                'value': 'DIO/PFI5'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI6 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO6_STR',
                'value': 'DIO/PFI6'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI7 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO7_STR',
                'value': 'DIO/PFI7'
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
                    'description': 'Applies a root-raised cosine filter to the data with the alpha value specified with the %attribute{arb filter root raised cosine alpha} attribute.'
                },
                'name': 'NIRFSG_VAL_ARB_FILTER_TYPE_ROOT_RAISED_COSINE',
                'value': 10001
            },
            {
                'documentation': {
                    'description': 'Applies a raised cosine filter to the data with the alpha value specified with the %attribute{arb filter raised cosine alpha} attribute.'
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
                    'description': 'Configures the RF signal generator to generate the arbitrary waveform specified by the %attribute{arb selected waveform} attribute.'
                },
                'name': 'NIRFSG_VAL_ARB_WAVEFORM',
                'value': 1001
            },
            {
                'documentation': {
                    'description': 'Configures the RF signal generator to generate arbitrary waveforms as directed by the %attribute{selected script} attribute.'
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
    'LoFilter': {
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
                    'description': 'Exports a Configuration List Step Trigger.'
                },
                'name': 'NIRFSG_VAL_CONFIGURATION_LIST_STEP_TRIGGER',
                'value': 6
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
                    'description': 'Exports a Script Trigger.'
                },
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER',
                'value': 1
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
                    'description': 'Exports a Started Event.'
                },
                'name': 'NIRFSG_VAL_STARTED_EVENT',
                'value': 4
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
    'LoSource': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Uses an internal LO as the LO source. If you specify an internal LO source, the LO is generated inside the device itself.'
                },
                'name': 'NIRFSG_VAL_LO_SOURCE_ONBOARD_STR',
                'value': 'Onboard'
            },
            {
                'documentation': {
                    'description': 'Uses an external LO as the LO source. Connect a signal to the LO IN connector on the device and use the %attribute{upconverter center frequency} attribute to specify the LO frequency.'
                },
                'name': 'NIRFSG_VAL_LO_SOURCE_LO_IN_STR',
                'value': 'LO_In'
            },
            {
                'documentation': {
                    'description': 'Uses the PXIe-5831/5840 internal LO as the LO source. This value is valid only on the PXIe-5831 with PXIe-5653 and PXIe-5832 with PXIe-5653.'
                },
                'name': 'NIRFSG_VAL_LO_SOURCE_SECONDARY_STR',
                'value': 'Secondary'
            },
            {
                'documentation': {
                    'description': 'Uses the same internal LO during NI-RFSA and NI-RFSG sessions. NI-RFSG selects an internal synthesizer and the synthesizer signal is switched to both the RF In and RF Out mixers. This value is valid only on the PXIe-5830/5831/5832/5841 with PXIe-5655/5842.'
                },
                'name': 'NIRFSG_VAL_LO_SOURCE_SG_SA_SHARED_STR',
                'value': 'SG_SA_Shared'
            },
            {
                'documentation': {
                    'description': 'NI-RFSG internally makes the configuration to share the LO between NI-RFSA and NI-RFSG. This value is valid only on the PXIe-5820/5830/5831/5832/5840/5841/5842.'
                },
                'name': 'NIRFSG_VAL_LO_SOURCE_AUTOMATIC_SG_SA_SHARED_STR',
                'value': 'Automatic_SG_SA_Shared'
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
                'name': 'NIRFSG_VAL_MANUAL',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'NI-RFSG skips loading the waveform configurations to the session.'
                },
                'name': 'RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS_SKIP_WAVEFORM',
                'value': 1
            },
            {
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER',
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
    'MarkerEventExportOutputTerm': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The signal is not exported.'
                },
                'name': 'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                'value': ''
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.'
                },
                'name': 'NIRFSG_VAL_PFI0_STR',
                'value': 'PFI0'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 1 connector.'
                },
                'name': 'NIRFSG_VAL_PFI1_STR',
                'value': 'PFI1'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 4 connector.'
                },
                'name': 'NIRFSG_VAL_PFI4_STR',
                'value': 'PFI4'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 5 connector.'
                },
                'name': 'NIRFSG_VAL_PFI5_STR',
                'value': 'PFI5'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to PXI trigger line 0.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG0_STR',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to PXI trigger line 1.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG1_STR',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to PXI trigger line 2.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG2_STR',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to PXI trigger line 3.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG3_STR',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to PXI trigger line 4.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG4_STR',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to PXI trigger line 5.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG5_STR',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to PXI trigger line 6.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG6_STR',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.'
                },
                'name': 'NIRFSG_VAL_PXIE_DSTARC_STR',
                'value': 'PXIe_DStarC'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI0 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO0_STR',
                'value': 'DIO/PFI0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI1 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO1_STR',
                'value': 'DIO/PFI1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI2 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO2_STR',
                'value': 'DIO/PFI2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI3 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO3_STR',
                'value': 'DIO/PFI3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI4 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO4_STR',
                'value': 'DIO/PFI4'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI5 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO5_STR',
                'value': 'DIO/PFI5'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI6 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO6_STR',
                'value': 'DIO/PFI6'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI7 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO7_STR',
                'value': 'DIO/PFI7'
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
                    'description': 'Indicates the maximum power level of the RF signal averaged over one period of the RF carrier frequency (the peak envelope power). This setting requires that the magnitude of the I/Q waveform must always be less than or equal to one. When using peak power, the power level of the RF signal matches the specified power level at moments when the magnitude of the I/Q waveform equals one. If you write more than one waveform, the relative scaling between waveforms is preserved. In peak power mode, waveforms are scaled according to the %attribute{arb waveform software scaling factor} attribute. You can use the %attribute{peak power adjustment} attribute in conjunction with the %attribute{power level} attribute when the %attribute{power level type} attribute is set to %enum_value{power level type.peak power}.'
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
    'PulseModulationOutputTerm': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'yet to be defined'
                },
                'name': 'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                'value': ''
            },
            {
                'documentation': {
                    'description': 'yet to be defined'
                },
                'name': 'NIRFSG_VAL_PULSE_OUT_STR',
                'value': 'PulseOut'
            }
        ]
    },
    'PulseModulationSource': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842.'
                },
                'name': 'NIRFSG_VAL_PULSE_IN_STR',
                'value': 'PulseIn'
            },
            {
                'documentation': {
                    'description': 'The trigger is received from the Marker  0.'
                },
                'name': 'NIRFSG_VAL_MARKER0_STR',
                'value': 'Marker0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received from the Marker 1.'
                },
                'name': 'NIRFSG_VAL_MARKER1_STR',
                'value': 'Marker1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received from the Marker 2.'
                },
                'name': 'NIRFSG_VAL_MARKER2_STR',
                'value': 'Marker2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received from the Marker 3.'
                },
                'name': 'NIRFSG_VAL_MARKER3_STR',
                'value': 'Marker3'
            }
        ]
    },
    'PxiChassisClk10Source': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Do not drive the PXI_CLK10 signal.'
                },
                'name': 'NIRFSG_VAL_NONE',
                'value': 0
            },
            {
                'name': 'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                'value': ''
            },
            {
                'documentation': {
                    'description': 'Uses the highly stable oven-controlled onboard Reference Clock to drive the PXI_CLK signal.'
                },
                'name': 'NIRFSG_VAL_ONBOARD_CLOCK_STR',
                'value': 'OnboardClock'
            },
            {
                'documentation': {
                    'description': 'Uses the clock present at the front panel REF IN connector to drive the PXI_CLK signal.'
                },
                'name': 'NIRFSG_VAL_REF_IN_STR',
                'value': 'RefIn'
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
    'ReferenceClockExportOutputTerminal': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The Reference Clock signal is not exported.'
                },
                'name': 'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                'value': ''
            },
            {
                'documentation': {
                    'description': 'Exports the Reference Clock signal to the REF OUT connector of the device.'
                },
                'name': 'NIRFSG_VAL_REF_OUT_STR',
                'value': 'RefOut'
            },
            {
                'documentation': {
                    'description': 'Exports the Reference Clock signal to the REF OUT2 connector of the device, if applicable.'
                },
                'name': 'NIRFSG_VAL_REF_OUT2_STR',
                'value': 'RefOut2'
            },
            {
                'documentation': {
                    'description': 'Exports the Reference Clock signal to the CLK OUT connector of the device.'
                },
                'name': 'NIRFSG_VAL_CLK_OUT_STR',
                'value': 'ClkOut'
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
    'ReferenceClockSource': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Uses the onboard Reference Clock as the clock source.'
                },
                'name': 'NIRFSG_VAL_ONBOARD_CLOCK_STR',
                'value': 'OnboardClock'
            },
            {
                'documentation': {
                    'description': 'Uses the clock signal present at the front panel REF IN connector as the Reference Clock source.'
                },
                'name': 'NIRFSG_VAL_REF_IN_STR',
                'value': 'RefIn'
            },
            {
                'documentation': {
                    'description': 'Uses the PXI_CLK signal, which is present on the PXI backplane, as the Reference Clock source.'
                },
                'name': 'NIRFSG_VAL_PXI_CLK_STR',
                'value': 'PXI_CLK'
            },
            {
                'documentation': {
                    'description': 'Uses the clock signal present at the front panel CLK IN connector as the Reference Clock source. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5841 with PXIe-5655.'
                },
                'name': 'NIRFSG_VAL_CLK_IN_STR',
                'value': 'ClkIn'
            },
            {
                'documentation': {
                    'description': 'This value is not valid on any supported devices.'
                },
                'name': 'NIRFSG_VAL_REF_IN_2_STR',
                'value': 'RefIn2'
            },
            {
                'documentation': {
                    'description': 'This value is valid on only the PXIe-5831/5832 with PXIe-5653. **PXIe-5831/5832 with PXIe-5653 —** NI-RFSG configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use NIRFSG_VAL_PXI_CLK_STR %enum_value as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.'
                },
                'name': 'NIRFSG_VAL_PXI_CLK_MASTER_STR',
                'value': 'PXI_ClkMaster'
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
    'ScriptTrigDigEdgeSource': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The trigger is received on PFI 0.'
                },
                'name': 'NIRFSG_VAL_PFI0_STR',
                'value': 'PFI0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI 1.'
                },
                'name': 'NIRFSG_VAL_PFI1_STR',
                'value': 'PFI1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI 2.'
                },
                'name': 'NIRFSG_VAL_PFI2_STR',
                'value': 'PFI2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI 3.'
                },
                'name': 'NIRFSG_VAL_PFI3_STR',
                'value': 'PFI3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 0.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG0_STR',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 1.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG1_STR',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 2.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG2_STR',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 3.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG3_STR',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 4.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG4_STR',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 5.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG5_STR',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 6.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG6_STR',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 7.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG7_STR',
                'value': 'PXI_Trig7'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the PXI star trigger line. This value is not valid on the PXIe-5644/5645/5646.'
                },
                'name': 'NIRFSG_VAL_PXI_STAR_STR',
                'value': 'PXI_Star'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/'
                },
                'name': 'NIRFSG_VAL_PXIE_DSTARB_STR',
                'value': 'PXIe_DStarB'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842.'
                },
                'name': 'NIRFSG_VAL_PULSE_IN_STR',
                'value': 'PulseIn'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI0 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO0_STR',
                'value': 'DIO/PFI0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI1 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO1_STR',
                'value': 'DIO/PFI1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI2 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO2_STR',
                'value': 'DIO/PFI2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI3 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO3_STR',
                'value': 'DIO/PFI3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI4 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO4_STR',
                'value': 'DIO/PFI4'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI5 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO5_STR',
                'value': 'DIO/PFI5'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI6 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO6_STR',
                'value': 'DIO/PFI6'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI7 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO7_STR',
                'value': 'DIO/PFI7'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the Sync Script trigger line. This value is valid on only the PXIe-5644/5645/5646.'
                },
                'name': 'NIRFSG_VAL_SYNC_SCRIPT_TRIGGER_STR',
                'value': 'Sync_Script'
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
    'ScriptTrigDigLevelSource': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The trigger is received on PFI 0.'
                },
                'name': 'NIRFSG_VAL_PFI0_STR',
                'value': 'PFI0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI 1.'
                },
                'name': 'NIRFSG_VAL_PFI1_STR',
                'value': 'PFI1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI 2.'
                },
                'name': 'NIRFSG_VAL_PFI2_STR',
                'value': 'PFI2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI 3.'
                },
                'name': 'NIRFSG_VAL_PFI3_STR',
                'value': 'PFI3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 0.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG0_STR',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 1.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG1_STR',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 2.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG2_STR',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 3.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG3_STR',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 4.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG4_STR',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 5.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG5_STR',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 6.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG6_STR',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 7.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG7_STR',
                'value': 'PXI_Trig7'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the PXI star trigger line. This value is not valid on the PXIe-5644/5645/5646.'
                },
                'name': 'NIRFSG_VAL_PXI_STAR_STR',
                'value': 'PXI_Star'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/'
                },
                'name': 'NIRFSG_VAL_PXIE_DSTARB_STR',
                'value': 'PXIe_DStarB'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the PULSE IN terminal. This value is valid on only the PXIe-5842.'
                },
                'name': 'NIRFSG_VAL_PULSE_IN_STR',
                'value': 'PulseIn'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI0 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO0_STR',
                'value': 'DIO/PFI0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI1 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO1_STR',
                'value': 'DIO/PFI1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI2 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO2_STR',
                'value': 'DIO/PFI2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI3 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO3_STR',
                'value': 'DIO/PFI3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI4 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO4_STR',
                'value': 'DIO/PFI4'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI5 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO5_STR',
                'value': 'DIO/PFI5'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI6 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO6_STR',
                'value': 'DIO/PFI6'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI7 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO7_STR',
                'value': 'DIO/PFI7'
            }
        ]
    },
    'ScriptTrigExportOutputTerm': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The signal is not exported.'
                },
                'name': 'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                'value': ''
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.'
                },
                'name': 'NIRFSG_VAL_PFI0_STR',
                'value': 'PFI0'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 1 connector.'
                },
                'name': 'NIRFSG_VAL_PFI1_STR',
                'value': 'PFI1'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 4 connector.'
                },
                'name': 'NIRFSG_VAL_PFI4_STR',
                'value': 'PFI4'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 5 connector.'
                },
                'name': 'NIRFSG_VAL_PFI5_STR',
                'value': 'PFI5'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 0.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG0_STR',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 1.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG1_STR',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 2.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG2_STR',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 3.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG3_STR',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 4.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG4_STR',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 5.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG5_STR',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 6.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG6_STR',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/'
                },
                'name': 'NIRFSG_VAL_PXIE_DSTARC_STR',
                'value': 'PXIe_DStarC'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI0 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO0_STR',
                'value': 'DIO/PFI0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI1 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO1_STR',
                'value': 'DIO/PFI1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI2 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO2_STR',
                'value': 'DIO/PFI2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI3 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO3_STR',
                'value': 'DIO/PFI3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI4 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO4_STR',
                'value': 'DIO/PFI4'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI5 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO5_STR',
                'value': 'DIO/PFI5'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI6 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO6_STR',
                'value': 'DIO/PFI6'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI7 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO7_STR',
                'value': 'DIO/PFI7'
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
                    'description': 'The data operation does not start until a digital edge is detected. The source of the digital edge is specified with the %attribute{digital edge start trigger source} attribute, and the active edge is specified with the %attribute{digital edge start trigger edge} attribute.'
                },
                'name': 'NIRFSG_VAL_DIGITAL_EDGE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'The data operation does not start until the digital level is detected. The source of the digital level is specified in the %attribute{digital level script trigger source} attribute, and the active level is specified in the %attribute{digital level script trigger active level} attribute.'
                },
                'name': 'NIRFSG_VAL_DIGITAL_LEVEL',
                'value': 8000
            },
            {
                'documentation': {
                    'description': 'The data operation does not start until a software trigger occurs. You can create a software event by calling the %function{send software edge trigger} function.'
                },
                'name': 'NIRFSG_VAL_SOFTWARE',
                'value': 2
            }
        ]
    },
    'SelfCalibrateRange': {
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
    'SignalIdentifier': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies Marker 0.'
                },
                'name': 'NIRFSG_VAL_MARKER_EVENT0',
                'value': 'marker0'
            },
            {
                'documentation': {
                    'description': 'Specifies Marker 1.'
                },
                'name': 'NIRFSG_VAL_MARKER_EVENT1',
                'value': 'marker1'
            },
            {
                'documentation': {
                    'description': 'Specifies Marker 2.'
                },
                'name': 'NIRFSG_VAL_MARKER_EVENT2',
                'value': 'marker2'
            },
            {
                'documentation': {
                    'description': 'Specifies Marker 3.'
                },
                'name': 'NIRFSG_VAL_MARKER_EVENT3',
                'value': 'marker3'
            },
            {
                'documentation': {
                    'description': 'Specifies Script Trigger 0.'
                },
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER0',
                'value': 'scriptTrigger0'
            },
            {
                'documentation': {
                    'description': 'Specifies Script Trigger 1.'
                },
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER1',
                'value': 'scriptTrigger1'
            },
            {
                'documentation': {
                    'description': 'Specifies Script Trigger 2.'
                },
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER2',
                'value': 'scriptTrigger2'
            },
            {
                'documentation': {
                    'description': 'Specifies Script Trigger 3.'
                },
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER3',
                'value': 'scriptTrigger3'
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
    'StartTrigDigEdgeSource': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The trigger is received on PFI 0.'
                },
                'name': 'NIRFSG_VAL_PFI0_STR',
                'value': 'PFI0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI 1.'
                },
                'name': 'NIRFSG_VAL_PFI1_STR',
                'value': 'PFI1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI 2.'
                },
                'name': 'NIRFSG_VAL_PFI2_STR',
                'value': 'PFI2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI 3.'
                },
                'name': 'NIRFSG_VAL_PFI3_STR',
                'value': 'PFI3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 0.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG0_STR',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 1.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG1_STR',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 2.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG2_STR',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 3.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG3_STR',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 4.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG4_STR',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 5.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG5_STR',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 6.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG6_STR',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 7.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG7_STR',
                'value': 'PXI_Trig7'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the PXI star trigger line. This value is not valid on the PXIe-5644/5645/5646.'
                },
                'name': 'NIRFSG_VAL_PXI_STAR_STR',
                'value': 'PXI_Star'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the PXI DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.'
                },
                'name': 'NIRFSG_VAL_PXIE_DSTARB_STR',
                'value': 'PXIe_DStarB'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the TRIG IN/OUT terminal. This value is valid on only the PXIe-5654/5654 with PXIe-5696.'
                },
                'name': 'NIRFSG_VAL_TRIG_IN_STR',
                'value': 'TrigIn'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI0 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO0_STR',
                'value': 'DIO/PFI0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI1 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO1_STR',
                'value': 'DIO/PFI1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI2 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO2_STR',
                'value': 'DIO/PFI2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI3 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO3_STR',
                'value': 'DIO/PFI3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI4 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO4_STR',
                'value': 'DIO/PFI4'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI5 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO5_STR',
                'value': 'DIO/PFI5'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI6 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO6_STR',
                'value': 'DIO/PFI6'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI7 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO7_STR',
                'value': 'DIO/PFI7'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the Sync Start trigger line. This value is valid on only the PXIe-5644/5645/5646.'
                },
                'name': 'NIRFSG_VAL_SYNC_START_TRIGGER_STR',
                'value': 'Sync_Start'
            }
        ]
    },
    'StartTrigExportOutputTerm': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The signal is not exported.'
                },
                'name': 'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                'value': ''
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.'
                },
                'name': 'NIRFSG_VAL_PFI0_STR',
                'value': 'PFI0'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 1 connector.'
                },
                'name': 'NIRFSG_VAL_PFI1_STR',
                'value': 'PFI1'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 4 connector.'
                },
                'name': 'NIRFSG_VAL_PFI4_STR',
                'value': 'PFI4'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 5 connector.'
                },
                'name': 'NIRFSG_VAL_PFI5_STR',
                'value': 'PFI5'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 0.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG0_STR',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 1.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG1_STR',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 2.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG2_STR',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 3.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG3_STR',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 4.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG4_STR',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 5.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG5_STR',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 6.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG6_STR',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.'
                },
                'name': 'NIRFSG_VAL_PXIE_DSTARC_STR',
                'value': 'PXIe_DStarC'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the TRIG IN/OUT terminal. This value is valid on only the PXIe-5654/5654 with PXIe-5696.'
                },
                'name': 'NIRFSG_VAL_TRIG_OUT_STR',
                'value': 'TrigOut'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI0 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO0_STR',
                'value': 'DIO/PFI0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI1 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO1_STR',
                'value': 'DIO/PFI1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI2 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO2_STR',
                'value': 'DIO/PFI2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI3 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO3_STR',
                'value': 'DIO/PFI3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI4 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO4_STR',
                'value': 'DIO/PFI4'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI5 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO5_STR',
                'value': 'DIO/PFI5'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI6 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO6_STR',
                'value': 'DIO/PFI6'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI7 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO7_STR',
                'value': 'DIO/PFI7'
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
                    'description': 'The data operation does not start until a digital edge is detected. The source of the digital edge is specified with the %attribute{digital edge start trigger source} attribute, and the active edge is specified in the %attribute{digital edge start trigger edge} attribute.'
                },
                'name': 'NIRFSG_VAL_DIGITAL_EDGE',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'The data operation does not start until a software event occurs. You may create a software trigger by calling the %function{send software edge trigger} function.'
                },
                'name': 'NIRFSG_VAL_SOFTWARE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'The data operation does not start until the endpoint reaches the threshold specified in the %attribute{p2p endpoint fullness start trigger level} attribute.'
                },
                'name': 'NIRFSG_VAL_P2P_ENDPOINT_FULLNESS',
                'value': 3
            }
        ]
    },
    'StartedEventExportOutputTerm': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The signal is not exported.'
                },
                'name': 'NIRFSG_VAL_DO_NOT_EXPORT_STR',
                'value': ''
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0.'
                },
                'name': 'NIRFSG_VAL_PFI0_STR',
                'value': 'PFI0'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 1 connector.'
                },
                'name': 'NIRFSG_VAL_PFI1_STR',
                'value': 'PFI1'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 4 connector.'
                },
                'name': 'NIRFSG_VAL_PFI4_STR',
                'value': 'PFI4'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PFI 5 connector.'
                },
                'name': 'NIRFSG_VAL_PFI5_STR',
                'value': 'PFI5'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 0.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG0_STR',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 1.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG1_STR',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 2.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG2_STR',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 3.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG3_STR',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 4.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG4_STR',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 5.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG5_STR',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXI trigger line 6.'
                },
                'name': 'NIRFSG_VAL_PXI_TRIG6_STR',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': 'The signal is exported to the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841/5842/5860.'
                },
                'name': 'NIRFSG_VAL_PXIE_DSTARC_STR',
                'value': 'PXIe_DStarC'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI0 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO0_STR',
                'value': 'DIO/PFI0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI1 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO1_STR',
                'value': 'DIO/PFI1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI2 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO2_STR',
                'value': 'DIO/PFI2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI3 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO3_STR',
                'value': 'DIO/PFI3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI4 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO4_STR',
                'value': 'DIO/PFI4'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI5 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO5_STR',
                'value': 'DIO/PFI5'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI6 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO6_STR',
                'value': 'DIO/PFI6'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI7 from the front panel DIO terminal.'
                },
                'name': 'NIRFSG_VAL_DIO7_STR',
                'value': 'DIO/PFI7'
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
    'StepsToOmit': {
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
    'Trigger': {
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
    'TriggerIdentifier': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies Script Trigger 0.'
                },
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER0',
                'value': 'scriptTrigger0'
            },
            {
                'documentation': {
                    'description': 'Specifies Script Trigger 1.'
                },
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER1',
                'value': 'scriptTrigger1'
            },
            {
                'documentation': {
                    'description': 'Specifies Script Trigger 2.'
                },
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER2',
                'value': 'scriptTrigger2'
            },
            {
                'documentation': {
                    'description': 'Specifies Script Trigger 3.'
                },
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER3',
                'value': 'scriptTrigger3'
            }
        ]
    },
    'UpconverterFrequencyOffsetMode': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the %attribute{signal bandwidth} attribute has been set and can be avoided.'
                },
                'name': 'NIRFSG_VAL_AUTO',
                'value': -1
            },
            {
                'name': 'NIRFSG_VAL_AUTOMATIC',
                'value': -1
            },
            {
                'documentation': {
                    'description': 'NI-RFSG places the upconverter center frequency outside of the signal bandwidth if the %attribute{signal bandwidth} attribute has been set and can be avoided. NI-RFSG returns an error if the %attribute{signal bandwidth} attribute has not been set, or if the signal bandwidth is too large.'
                },
                'name': 'NIRFSG_VAL_ENABLE',
                'value': 1
            },
            {
                'name': 'NIRFSG_VAL_SCRIPT_TRIGGER',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'NI-RFSG uses the offset that you specified with the %attribute{upconverter frequency offset} or %attribute{upconverter center frequency} attributes.'
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
