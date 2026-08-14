# -*- coding: utf-8 -*-
# This file is generated from NI-RFSA API metadata version 26.5.0d9999
enums = {
    'AcquisitionType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Configures NI-RFSA for I/Q acquisitions.'
                },
                'name': 'NIRFSA_VAL_IQ',
                'value': 100
            },
            {
                'documentation': {
                    'description': 'Configures NI-RFSA for spectrum acquisitions.'
                },
                'name': 'NIRFSA_VAL_SPECTRUM',
                'value': 101
            }
        ]
    },
    'Action': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The new calibration constants are stored in the EEPROM.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_COMMIT',
                'value': 1501
            },
            {
                'documentation': {
                    'description': 'The old calibration constants are kept, and the new ones are discarded.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_ABORT',
                'value': 1500
            }
        ]
    },
    'AdvanceTriggerType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'No Advance Trigger is configured.'
                },
                'name': 'NIRFSA_VAL_NONE',
                'value': 600
            },
            {
                'documentation': {
                    'description': 'The Advance Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the NIRFSA_ATTR_DIGITAL_EDGE_ADVANCE_TRIGGER_SOURCE attribute.'
                },
                'name': 'NIRFSA_VAL_DIGITAL_EDGE',
                'value': 601
            },
            {
                'documentation': {
                    'description': 'The Advance Trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the nirfsa_SendSoftwareEdgeTrigger function and selecting NIRFSA_VAL_ADVANCE_TRIGGER as the **trigger** parameter.'
                },
                'name': 'NIRFSA_VAL_SOFTWARE_EDGE',
                'value': 604
            }
        ]
    },
    'AdvanceTriggerDigitalEdgeEdge': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The trigger asserts on the rising edge of the signal.'
                },
                'name': 'NIRFSA_VAL_RISING_EDGE',
                'value': 900
            },
            {
                'documentation': {
                    'description': 'The trigger asserts on the falling edge of the signal.'
                },
                'name': 'NIRFSA_VAL_FALLING_EDGE',
                'value': 901
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
                'name': 'NIRFSA_VAL_DISABLED',
                'value': 1900
            },
            {
                'documentation': {
                    'description': 'Enables out-of-specification user settings.'
                },
                'name': 'NIRFSA_VAL_ENABLED',
                'value': 1901
            }
        ]
    },
    'ArmReferenceTriggerType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'No Arm Reference Trigger is configured.'
                },
                'name': 'NIRFSA_VAL_NONE',
                'value': 600
            },
            {
                'documentation': {
                    'description': 'The Arm Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the NIRFSA_ATTR_DIGITAL_EDGE_ARM_REF_TRIGGER_SOURCE attribute.'
                },
                'name': 'NIRFSA_VAL_DIGITAL_EDGE',
                'value': 601
            },
            {
                'documentation': {
                    'description': 'The Arm Reference Trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the nirfsa_SendSoftwareEdgeTrigger function and selecting NIRFSA_VAL_ARM_REF_TRIGGER as the **trigger** parameter.'
                },
                'name': 'NIRFSA_VAL_SOFTWARE_EDGE',
                'value': 604
            }
        ]
    },
    'CalToneMode': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables the calibration tone for the associated signal path. '
                },
                'name': 'NIRFSA_VAL_DISABLED',
                'value': 1900
            },
            {
                'documentation': {
                    'description': 'Injects the calibration tone into the low band RF signal path. '
                },
                'name': 'NIRFSA_VAL_CAL_TONE_LOWBAND_RF',
                'value': 2701
            },
            {
                'documentation': {
                    'description': 'Injects the calibration tone into the high band RF signal path. '
                },
                'name': 'NIRFSA_VAL_CAL_TONE_HIGHBAND_RF',
                'value': 2702
            },
            {
                'documentation': {
                    'description': 'Injects the calibration tone into the high band IF signal path.'
                },
                'name': 'NIRFSA_VAL_CAL_TONE_HIGHBAND_IF',
                'value': 2703
            },
            {
                'documentation': {
                    'description': 'Injects the calibration tone into the low band RF signal path, bypassing the ALC.'
                },
                'name': 'NIRFSA_VAL_CAL_TONE_LOWBAND_RF_WITHOUT_ALC',
                'value': 2704
            },
            {
                'documentation': {
                    'description': 'Injects the calibration tone into the high band RF signal path through the Comb Generator. '
                },
                'name': 'NIRFSA_VAL_CAL_TONE_COMB_GENERATOR',
                'value': 2705
            }
        ]
    },
    'CalibrateStep': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Initializes the IF Attenuation Calibration step. This step is not supported for the PXIe-5693.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_IF_ATTENUATION_CALIBRATION',
                'value': 1600
            },
            {
                'documentation': {
                    'description': 'Initializes the IF Response Calibration step. This step is not supported for the PXIe-5603/5605 or PXIe-5693/5698.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_IF_RESPONSE_CALIBRATION',
                'value': 1601
            },
            {
                'documentation': {
                    'description': 'Initializes the Ref Level Calibration step. This step is not supported on the PXIe-5694. '
                },
                'name': 'NIRFSA_VAL_EXT_CAL_IF_REF_LEVEL_CALIBRATION',
                'value': 1602
            },
            {
                'documentation': {
                    'description': 'Initializes the LO Export Calibration step. This step calibrates the output power of each LO to be within specification. This step is not supported on the PXIe-5601 or the PXIe-5693/5694/5698.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_LO_EXPORT_CALIBRATION',
                'value': 1603
            },
            {
                'documentation': {
                    'description': 'Initializes the Gain Reference Calibration step. This step calibrates the calibration tone amplitude across supported calibration tone frequencies. This step is not supported on the PXIe-5601/5603/5605 or PXIe-5694.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_GAIN_REFERENCE_CALIBRATION',
                'value': 1604
            }
        ]
    },
    'ChannelCoupling': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that the RF input channel is AC-coupled. For low frequencies (<10 MHz), accuracy decreases because NI-RFSA does not calibrate the configuration.'
                },
                'name': 'NIRFSA_VAL_AC',
                'value': 3001
            },
            {
                'documentation': {
                    'description': 'Specifies that the RF input channel is DC-coupled. NI-RFSA enforces a minimum RF attenuation for device protection.'
                },
                'name': 'NIRFSA_VAL_DC',
                'value': 3002
            }
        ]
    },
    'ConditioningCalToneMode': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables the calibration tone for the associated signal path.'
                },
                'name': 'NIRFSA_VAL_DISABLED',
                'value': 1900
            },
            {
                'documentation': {
                    'description': 'Injects the calibration tone into the low band RF signal path.'
                },
                'name': 'NIRFSA_VAL_CAL_TONE_LOWBAND_RF',
                'value': 2701
            },
            {
                'documentation': {
                    'description': 'Injects the calibration tone into the high band RF signal path.'
                },
                'name': 'NIRFSA_VAL_CAL_TONE_HIGHBAND_RF',
                'value': 2702
            }
        ]
    },
    'DeembeddingType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'De-embedding is not applied to the measurement.'
                },
                'name': 'NIRFSA_VAL_DEEMBEDDING_TYPE_NONE',
                'value': 3900
            },
            {
                'documentation': {
                    'description': 'De-embeds the measurement using only the gain term.'
                },
                'name': 'NIRFSA_VAL_DEEMBEDDING_TYPE_SCALAR',
                'value': 3901
            },
            {
                'documentation': {
                    'description': 'De-embeds the measurement using the gain term and the reflection term.'
                },
                'name': 'NIRFSA_VAL_DEEMBEDDING_TYPE_VECTOR',
                'value': 3902
            }
        ]
    },
    'DeviceResponseType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Returns the IF response of the downconverter.'
                },
                'name': 'NIRFSA_VAL_DOWNCONVERTER_IF_RESPONSE',
                'value': 2800
            },
            {
                'documentation': {
                    'description': 'Returns the RF response of the downconverter. This value is supported only for the PXIe-5603/5605/5665/5667/5693..'
                },
                'name': 'NIRFSA_VAL_DOWNCONVERTER_RF_RESPONSE',
                'value': 2801
            },
            {
                'documentation': {
                    'description': 'Returns the combined RF and IF response of the downconverter. The combined response is in terms of IF frequency. This value is supported only for the PXIe-5603/5605/5665/5667.'
                },
                'name': 'NIRFSA_VAL_DOWNCONVERTER_COMBINED_RESPONSE',
                'value': 2802
            },
            {
                'documentation': {
                    'description': 'Returns the IF response of the entire NI-RFSA device. This value is supported only for the PXIe-5665/5667.'
                },
                'name': 'NIRFSA_VAL_VSA_IF_RESPONSE',
                'value': 2803
            },
            {
                'documentation': {
                    'description': 'Returns the combined IF and RF response of the entire NI-RFSA device. The combined response is in terms of IF frequency. This value is supported only for the PXIe-5665/5667.'
                },
                'name': 'NIRFSA_VAL_VSA_COMBINED_RESPONSE',
                'value': 2804
            }
        ]
    },
    'DigitizerDitherEnabled': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables dither on the digitizer.'
                },
                'name': 'NIRFSA_VAL_DISABLED',
                'value': 1900
            },
            {
                'documentation': {
                    'description': 'Enables dither on the digitizer.'
                },
                'name': 'NIRFSA_VAL_ENABLED',
                'value': 1901
            }
        ]
    },
    'DigitizerSampleClockExportedTerminal': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The Reference Clock is not exported. This value is not valid for the PXIe-5644/5645/5646.'
                },
                'name': 'NIRFSA_VAL_NONE',
                'value': 'None'
            },
            {
                'documentation': {
                    'description': 'Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.'
                },
                'name': 'NIRFSA_VAL_CLK_OUT',
                'value': 'ClkOut'
            }
        ]
    },
    'DigitizerSampleClockTimebaseSource': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The digitizer uses its onboard clock as the Sample Clock timebase.'
                },
                'name': 'NIRFSA_VAL_ONBOARD_CLOCK',
                'value': 'OnboardClock'
            },
            {
                'documentation': {
                    'description': 'The digitizer uses the signal present on the CLK IN connector as the Sample Clock timebase.'
                },
                'name': 'NIRFSA_VAL_CLK_IN',
                'value': 'ClkIn'
            },
            {
                'documentation': {
                    'description': 'The digitizer uses the signal generated on the 100 MHz REF OUT terminal on the PXIe-5653 as the Sample Clock timebase. This value is supported only for the PXIe-5665.'
                },
                'name': 'NIRFSA_VAL_LO_REF_CLK',
                'value': 'LORefClk'
            },
            {
                'documentation': {
                    'description': 'The digitizer uses the signal present at the PXI star trigger line as the Sample Clock timebase. This value is not supported for the PXIe-5668.'
                },
                'name': 'NIRFSA_VAL_PXI_STAR',
                'value': 'PXI_STAR'
            },
            {
                'documentation': {
                    'description': 'The digitizer uses the signal present on the LO2 OUT connector on the downconverter as the Sample Clock timebase. This value is supported only for the PXIe-5668.'
                },
                'name': 'NIRFSA_VAL_DOWNCONVERTER_LO2_OUT',
                'value': 'DownconverterLO2Out'
            }
        ]
    },
    'DownconverterFrequencyOffsetMode': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'NI-RFSA places the downconverter center frequency outside of the signal bandwidth if the NIRFSA_ATTR_SIGNAL_BANDWIDTH attribute has been set and can be avoided.'
                },
                'name': 'NIRFSA_VAL_AUTOMATIC',
                'value': 1903
            },
            {
                'documentation': {
                    'description': 'NI-RFSA places the downconverter center frequency outside of the signal bandwidth if the NIRFSA_ATTR_SIGNAL_BANDWIDTH attribute has been set and can be avoided. NI-RFSA returns an error if the NIRFSA_ATTR_SIGNAL_BANDWIDTH attribute has not been set, or if the signal bandwidth is too large.'
                },
                'name': 'NIRFSA_VAL_ENABLED',
                'value': 1901
            },
            {
                'documentation': {
                    'description': 'NI-RFSA uses the offset that you specified with the NIRFSA_ATTR_DOWNCONVERTER_FREQUENCY_OFFSET or NIRFSA_ATTR_DOWNCONVERTER_CENTER_FREQUENCY attributes.'
                },
                'name': 'NIRFSA_VAL_USER_DEFINED',
                'value': 1904
            }
        ]
    },
    'DownconverterLoopBandwidth': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that the downconverter module uses a narrow loop bandwidth.'
                },
                'name': 'NIRFSA_VAL_NARROW',
                'value': 800
            },
            {
                'documentation': {
                    'description': 'Specifies that the downconverter module uses a medium loop bandwidth.'
                },
                'name': 'NIRFSA_VAL_MEDIUM',
                'value': 801
            },
            {
                'documentation': {
                    'description': 'Specifies that the downconverter module uses a wide loop bandwidth.'
                },
                'name': 'NIRFSA_VAL_WIDE',
                'value': 802
            }
        ]
    },
    'EnableAttrVals': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The attribute is disabled.'
                },
                'name': 'NIRFSA_VAL_DISABLED',
                'value': 1900
            },
            {
                'documentation': {
                    'description': 'The attribute is enabled.'
                },
                'name': 'NIRFSA_VAL_ENABLED',
                'value': 1901
            }
        ]
    },
    'DownconverterPreselectorEnabled': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables the preselector.'
                },
                'name': 'NIRFSA_VAL_PRESELECTOR_DISABLED',
                'value': 2600
            },
            {
                'documentation': {
                    'description': 'The preselector is automatically enabled when it is in the signal path and is automatically disabled when it is not in the signal path. Use the NIRFSA_ATTR_PRESELECTOR_PRESENT attribute to determine if the downconverter has an preselector.'
                },
                'name': 'NIRFSA_VAL_PRESELECTOR_ENABLED_WHEN_IN_SIGNAL_PATH',
                'value': 2601
            },
            {
                'documentation': {
                    'description': 'Enables the preselector. If the preselector is not in the signal path or if the preselector is not supported on the device, NI-RFSA returns an error. Select the NIRFSA_VAL_PRESELECTOR_ENABLED_WHEN_IN_SIGNAL_PATH whenever possible avoid an error.'
                },
                'name': 'NIRFSA_VAL_PRESELECTOR_ENABLED',
                'value': 2602
            }
        ]
    },
    'EnableRfPreamp': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables the RF preamplifier.'
                },
                'name': 'NIRFSA_VAL_RF_PREAMP_DISABLED',
                'value': 2500
            },
            {
                'documentation': {
                    'description': 'Enables the RF preamplifier when the RF preamplifier is present in the signal path and disables the preamplifier when it is not in the signal path. Only devices with an RF preamplifier on the downconverter and an RF preselector support this option. Use the NIRFSA_ATTR_RF_PREAMP_PRESENT attribute to determine whether the downconverter has a preamplifier.'
                },
                'name': 'NIRFSA_VAL_RF_PREAMP_ENABLED_WHEN_IN_SIGNAL_PATH',
                'value': 2501
            },
            {
                'documentation': {
                    'description': 'Enables the RF preamplifier. If the RF preamplifier is not in a signal path, NI-RFSA returns an error. Select the NIRFSA_VAL_RF_PREAMP_ENABLED_WHEN_IN_SIGNAL_PATH value whenever possible to avoid an error.'
                },
                'name': 'NIRFSA_VAL_RF_PREAMP_ENABLED',
                'value': 2502
            },
            {
                'documentation': {
                    'description': 'Automatically enables the RF preamplifier based on the value of the NIRFSA_ATTR_REFERENCE_LEVEL attribute. This value is valid only for the PXIe-5644/5645/5646, PXIe-5667, and PXIe-5830/5831/5832/5840/5841.'
                },
                'name': 'NIRFSA_VAL_RF_PREAMP_AUTOMATIC',
                'value': 2503
            }
        ]
    },
    'RfOutLoExport': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The LO signal is not exported from the RF OUT LO OUT terminal.'
                },
                'name': 'NIRFSA_VAL_DISABLED',
                'value': 1900
            },
            {
                'documentation': {
                    'description': 'The LO signal is exported from the RF OUT LO OUT terminal.'
                },
                'name': 'NIRFSA_VAL_ENABLED',
                'value': 1901
            },
            {
                'documentation': {
                    'description': 'The LO signal may or may not be exported to the RF OUT LO OUT terminal, because NI-RFSG may be controlling it.'
                },
                'name': 'NIRFSA_VAL_UNSPECIFIED',
                'value': 1902
            }
        ]
    },
    'ExportOutputTerminal': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The signal is not exported.'
                },
                'name': 'NIRFSA_VAL_DO_NOT_EXPORT',
                'value': ''
            },
            {
                'documentation': {
                    'description': 'Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.'
                },
                'name': 'NIRFSA_VAL_CLK_OUT',
                'value': 'ClkOut'
            },
            {
                'documentation': {
                    'description': 'Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841.'
                },
                'name': 'NIRFSA_VAL_REF_OUT',
                'value': 'RefOut'
            },
            {
                'documentation': {
                    'description': 'Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.'
                },
                'name': 'NIRFSA_VAL_REF_OUT2',
                'value': 'RefOut2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.'
                },
                'name': 'NIRFSA_VAL_PFI0',
                'value': 'PFI0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI 1.'
                },
                'name': 'NIRFSA_VAL_PFI1',
                'value': 'PFI1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 0.'
                },
                'name': 'NIRFSA_VAL_PXI_TRIG0',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 1.'
                },
                'name': 'NIRFSA_VAL_PXI_TRIG1',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 2.'
                },
                'name': 'NIRFSA_VAL_PXI_TRIG2',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 3.'
                },
                'name': 'NIRFSA_VAL_PXI_TRIG3',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 4.'
                },
                'name': 'NIRFSA_VAL_PXI_TRIG4',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 5.'
                },
                'name': 'NIRFSA_VAL_PXI_TRIG5',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 6.'
                },
                'name': 'NIRFSA_VAL_PXI_TRIG6',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 7.'
                },
                'name': 'NIRFSA_VAL_PXI_TRIG7',
                'value': 'PXI_Trig7'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.'
                },
                'name': 'NIRFSA_VAL_PXI_STAR',
                'value': 'PXI_STAR'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the PXIe DStar C trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.'
                },
                'name': 'NIRFSA_VAL_PXIE_DSTARC',
                'value': 'PXIe_DStarC'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI0 from the front panel DIO terminal.'
                },
                'name': 'NIRFSA_VAL_DIO_PFI0',
                'value': 'DIO/PFI0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI1 from the front panel DIO terminal.'
                },
                'name': 'NIRFSA_VAL_DIO_PFI1',
                'value': 'DIO/PFI1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI2 from the front panel DIO terminal.'
                },
                'name': 'NIRFSA_VAL_DIO_PFI2',
                'value': 'DIO/PFI2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI3 from the front panel DIO terminal.'
                },
                'name': 'NIRFSA_VAL_DIO_PFI3',
                'value': 'DIO/PFI3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI4 from the front panel DIO terminal.'
                },
                'name': 'NIRFSA_VAL_DIO_PFI4',
                'value': 'DIO/PFI4'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI5 from the front panel DIO terminal.'
                },
                'name': 'NIRFSA_VAL_DIO_PFI5',
                'value': 'DIO/PFI5'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI6 from the front panel DIO terminal.'
                },
                'name': 'NIRFSA_VAL_DIO_PFI6',
                'value': 'DIO/PFI6'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI7 from the front panel DIO terminal.'
                },
                'name': 'NIRFSA_VAL_DIO_PFI7',
                'value': 'DIO/PFI7'
            }
        ]
    },
    'FetchRelativeTo': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Fetching occurs relative to the most recently acquired data. The value of the NIRFSA_ATTR_FETCH_OFFSET attribute must be negative.'
                },
                'name': 'NIRFSA_VAL_MOST_RECENT_SAMPLE',
                'value': 700
            },
            {
                'documentation': {
                    'description': 'Fetching occurs at the first sample acquired by the device. If the device wraps its buffer, the first sample is no longer available. In this case, NI-RFSA returns an error if the fetch offset is in the overwritten data.'
                },
                'name': 'NIRFSA_VAL_FIRST_SAMPLE',
                'value': 701
            },
            {
                'documentation': {
                    'description': 'Fetching occurs relative to the Reference Trigger. This value behaves like NIRFSA_VAL_FIRST_SAMPLE if no Reference Trigger is configured.'
                },
                'name': 'NIRFSA_VAL_REFERENCE_TRIGGER',
                'value': 702
            },
            {
                'documentation': {
                    'description': 'Fetching occurs relative to the first pretrigger sample acquired.'
                },
                'name': 'NIRFSA_VAL_FIRST_PRETRIGGER_SAMPLE',
                'value': 703
            },
            {
                'documentation': {
                    'description': 'Fetching occurs after the last fetched sample.'
                },
                'name': 'NIRFSA_VAL_CURRENT_READ_POSITION',
                'value': 704
            }
        ]
    },
    'FrequencySettlingUnits': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies the frequency settling time in parts per million (PPM).'
                },
                'name': 'NIRFSA_VAL_FSU_PPM',
                'python_name': 'PPM',
                'value': 2000
            },
            {
                'documentation': {
                    'description': 'Specifies the frequency settling in time after lock (seconds).'
                },
                'name': 'NIRFSA_VAL_FSU_SECONDS_AFTER_LOCK',
                'python_name': 'SECONDS_AFTER_LOCK',
                'value': 2001
            },
            {
                'documentation': {
                    'description': 'Specifies the frequency settling time after I/O (seconds).'
                },
                'name': 'NIRFSA_VAL_FSU_SECONDS_AFTER_IO',
                'python_name': 'SECONDS_AFTER_IO',
                'value': 2002
            }
        ]
    },
    'IFattenTableSel': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that the standard IF attenuation table is used for the external calibration.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_IF_ATTENUATION_TABLE_STANDARD',
                'value': 2900
            },
            {
                'documentation': {
                    'description': 'Specifies that the adjacent channel power ratio (ACPR) IF attenuation table is used for the external calibration. You can only select this value if you set the NIRFSA_ATTR_CAL_IF_FILTER_SELECTION attribute to NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_1 or NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_2.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_IF_ATTENUATION_TABLE_ACPR',
                'value': 2901
            }
        ]
    },
    'IFfilter': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The device uses the 187.5 MHz wide bandwidth filter.'
                },
                'name': 'NIRFSA_VAL_187_5_MHZ_WIDE',
                'python_name': '_187_5_MHZ_WIDE',
                'value': 1400
            },
            {
                'documentation': {
                    'description': 'The device uses the 187.5 MHz narrow bandwidth filter.'
                },
                'name': 'NIRFSA_VAL_187_5_MHZ_NARROW',
                'python_name': '_187_5_MHZ_NARROW',
                'value': 1401
            },
            {
                'documentation': {
                    'description': 'The device uses the 53 MHz filter.'
                },
                'name': 'NIRFSA_VAL_53_MHZ',
                'python_name': '_53_MHZ',
                'value': 1402
            },
            {
                'documentation': {
                    'description': 'The device bypasses the IF filter.'
                },
                'name': 'NIRFSA_VAL_BYPASS',
                'value': 1403
            }
        ]
    },
    'IFfilterSelection': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that the 5 MHz filter path is used during calibration.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_1',
                'python_name': 'EXT_CAL_IF_FILTER_PATH_1',
                'value': 2100
            },
            {
                'documentation': {
                    'description': 'Specifies that the 300 kHz filter path is used during calibration. Not supported for the PXIe-5694.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_2',
                'python_name': 'EXT_CAL_IF_FILTER_PATH_2',
                'value': 2101
            },
            {
                'documentation': {
                    'description': 'None of the IF filter paths are used during calibration.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_3',
                'python_name': 'EXT_CAL_IF_FILTER_PATH_3',
                'value': 2102
            },
            {
                'documentation': {
                    'description': 'Specifies that the 20 MHz filter path is used during calibration.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_4',
                'python_name': 'EXT_CAL_IF_FILTER_PATH_4',
                'value': 2103
            },
            {
                'documentation': {
                    'description': 'Specifies that the 1.4 MHz filter path is used during calibration.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_5',
                'python_name': 'EXT_CAL_IF_FILTER_PATH_5',
                'value': 2104
            },
            {
                'documentation': {
                    'description': 'Specifies that the 400 kHz filter path is used during calibration.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_6',
                'python_name': 'EXT_CAL_IF_FILTER_PATH_6',
                'value': 2105
            },
            {
                'documentation': {
                    'description': 'Specifies that the 110 kHz filter path is used during calibration.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_7',
                'python_name': 'EXT_CAL_IF_FILTER_PATH_7',
                'value': 2106
            },
            {
                'documentation': {
                    'description': 'Specifies that the 30 kHz filter path is used during calibration.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_IF_FILTER_PATH_8',
                'python_name': 'EXT_CAL_IF_FILTER_PATH_8',
                'value': 2107
            }
        ]
    },
    'InputIsolationEnabled': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables input isolation.'
                },
                'name': 'NIRFSA_VAL_DISABLED',
                'value': 1900
            },
            {
                'documentation': {
                    'description': 'Enables input isolation.'
                },
                'name': 'NIRFSA_VAL_ENABLED',
                'value': 1901
            }
        ]
    },
    'IfConditioningDownConversionEnabled': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables IF conditioning downconversion.'
                },
                'name': 'NIRFSA_VAL_DISABLED',
                'value': 1900
            },
            {
                'documentation': {
                    'description': 'Enables IF conditioning downconversion.'
                },
                'name': 'NIRFSA_VAL_ENABLED',
                'value': 1901
            }
        ]
    },
    'InputPort': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Enables the RF IN port.'
                },
                'name': 'NIRFSA_VAL_RF_IN',
                'value': 2000
            },
            {
                'documentation': {
                    'description': 'Enables the I/Q IN port.'
                },
                'name': 'NIRFSA_VAL_IQ_IN',
                'value': 2001
            },
            {
                'documentation': {
                    'description': 'Enables the CAL IN port.'
                },
                'name': 'NIRFSA_VAL_CAL_IN',
                'value': 2002
            },
            {
                'documentation': {
                    'description': 'Enables the I terminals of the I/Q IN port. It is supported only for PXIe-5645.'
                },
                'name': 'NIRFSA_VAL_I_ONLY',
                'value': 2003
            }
        ]
    },
    'IqInPortTerminalConfiguration': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Sets the terminal configuration to differential.'
                },
                'name': 'NIRFSA_VAL_DIFFERENTIAL',
                'value': 2100
            },
            {
                'documentation': {
                    'description': 'Sets the terminal configuration to single-ended.'
                },
                'name': 'NIRFSA_VAL_SINGLE_ENDED',
                'value': 2101
            }
        ]
    },
    'SelfCalSteps': {
        'class': 'IntFlag',
        'values': [
            {
                'documentation': {
                    'description': 'Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_DIGITIZER_SELF_CAL',
                'value': 8
            },
            {
                'documentation': {
                    'description': 'Omits the LO Self Cal step. If you omit this step, the power level of the LO is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_PRESELECTOR_ALIGNMENT',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'No calibration steps are omitted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_OMIT_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Omits the Power Level Accuracy step. If you omit this step, the power level accuracy of the device is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_GAIN_REFERENCE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_IF_FLATNESS',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_LO_SELF_CAL',
                'value': 10
            },
            {
                'documentation': {
                    'description': 'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_AMPLITUDE_ACCURACY',
                'value': 20
            },
            {
                'documentation': {
                    'description': 'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_RESIDUAL_LO_POWER',
                'value': 40
            },
            {
                'documentation': {
                    'description': 'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_IMAGE_SUPPRESSION',
                'value': 80
            },
            {
                'documentation': {
                    'description': 'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_SYNTHESIZER_ALIGNMENT',
                'value': 100
            },
            {
                'documentation': {
                    'description': 'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_DC_OFFSET',
                'value': 200
            }
        ]
    },
    'LinearInterpolationFormat': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': ' Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion.'
                },
                'name': 'NIRFSA_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_AND_PHASE',
                'value': 4001
            },
            {
                'documentation': {
                    'description': 'Results in a linear interpolation of the magnitude and a separate linear interpolation of the phase.'
                },
                'name': 'NIRFSA_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_DB_AND_PHASE',
                'value': 4002
            },
            {
                'documentation': {
                    'description': 'Results in a linear interpolation of the magnitude, in decibels, and a separate linear interpolation of the phase.'
                },
                'name': 'NIRFSA_VAL_LINEAR_INTERPOLATION_FORMAT_REAL_AND_IMAGINARY',
                'value': 4000
            }
        ]
    },
    'Lo2ExportEnabled': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables LO2 export.'
                },
                'name': 'NIRFSA_VAL_DISABLED',
                'value': 1900
            },
            {
                'documentation': {
                    'description': 'Enables LO2 export.'
                },
                'name': 'NIRFSA_VAL_ENABLED',
                'value': 1901
            }
        ]
    },
    'LoInjection': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Configures the LO signal that the NI-RFSA device generates at a frequency higher than the RF frequency. This LO frequency is given by the formula f<sub>LO</sub> = f<sub>RF</sub> + f<sub>IF</sub>.'
                },
                'name': 'NIRFSA_VAL_LO_INJECTION_HIGH_SIDE',
                'value': 1300
            },
            {
                'documentation': {
                    'description': 'Configures the LO signal that the NI-RFSA device generates at a frequency lower than the RF frequency. This LO frequency is given by the formula f<sub>LO</sub> = f<sub>RF</sub> - f<sub>IF</sub>.'
                },
                'name': 'NIRFSA_VAL_LO_INJECTION_LOW_SIDE',
                'value': 1301
            }
        ]
    },
    'LoNumber': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Selects LO2, which is the 4 GHz signal path.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_LO2',
                'value': 2201
            },
            {
                'documentation': {
                    'description': 'Selects LO3, which is the 800 MHz signal path.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_LO3',
                'value': 2202
            },
            {
                'documentation': {
                    'description': 'Selects LO1, which is the 3.2 GHz to 8.3 GHz variable signal path.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_LO1',
                'value': 2200
            }
        ]
    },
    'LoOutExportConfigureFromRfsg': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Do not allow NI-RFSG to control the NI-RFSA local oscillator export.'
                },
                'name': 'NIRFSA_VAL_DISABLED',
                'value': 1900
            },
            {
                'documentation': {
                    'description': 'Allow NI-RFSG to control the NI-RFSA local oscillator export.'
                },
                'name': 'NIRFSA_VAL_ENABLED',
                'value': 1901
            }
        ]
    },
    'LoPathSel': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that the LO path 1 is used.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_LO_PATH_1',
                'python_name': 'EXT_CAL_LO_PATH_1',
                'value': 2300
            },
            {
                'documentation': {
                    'description': 'Specifies that the LO path 2 is used.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_LO_PATH_2',
                'python_name': 'EXT_CAL_LO_PATH_2',
                'value': 2301
            },
            {
                'documentation': {
                    'description': 'Specifies that the LO path 3 is used.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_LO_PATH_3',
                'python_name': 'EXT_CAL_LO_PATH_3',
                'value': 2302
            },
            {
                'documentation': {
                    'description': 'Specifies that the LO path 4 is used.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_LO_PATH_4',
                'python_name': 'EXT_CAL_LO_PATH_4',
                'value': 2303
            },
            {
                'documentation': {
                    'description': 'Specifies that the LO path 5 is used.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_LO_PATH_5',
                'python_name': 'EXT_CAL_LO_PATH_5',
                'value': 2304
            }
        ]
    },
    'LoPllFractionalModeEnabled': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables fractional mode for the LO PLL.'
                },
                'name': 'NIRFSA_VAL_DISABLED',
                'value': 1900
            },
            {
                'documentation': {
                    'description': 'Enables fractional mode for the LO PLL.'
                },
                'name': 'NIRFSA_VAL_ENABLED',
                'value': 1901
            }
        ]
    },
    'LoSource': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Specifies that no LO source is required to downconvert the RF input signal.'
                },
                'name': 'NIRFSA_VAL_NONE',
                'value': 'None'
            },
            {
                'documentation': {
                    'description': 'Specifies that the onboard synthesizer is used to generate the LO signal that downconverts the RF input signal.**PXIe-5831/5832** This configuration uses the onboard LO of the PXIe-3622, using the LO2 stage.**PXIe-5831/5832 with PXIe-5653** This configuration uses the onboard LO of the PXIe-5653 when associated with the PXIe-3622.**PXIe-5841 with PXIe-5655** This configuration uses the onboard LO of the PXIe-5655.'
                },
                'name': 'NIRFSA_VAL_ONBOARD',
                'value': 'Onboard'
            },
            {
                'documentation': {
                    'description': 'Specifies that the LO source used to downconvert the RF input signal is connected to the LO IN connector on the front panel.'
                },
                'name': 'NIRFSA_VAL_LO_IN',
                'value': 'LO_In'
            },
            {
                'documentation': {
                    'description': 'Uses the PXIe-5831/5840 internal LO as the LO source. This value is valid on only the PXIe-5831 with PXIe-5653 (LO1 stage only) or PXIe-5832 with PCIe-5653 (LO1 stage only).'
                },
                'name': 'NIRFSA_VAL_LO_SOURCE_SECONDARY',
                'value': 'Secondary'
            },
            {
                'documentation': {
                    'description': 'Uses the same internal LO during NI-RFSA and NI-RFSG sessions. NI-RFSA selects an internal synthesizer and the synthesizer signal is switched to both the RF Out and RF In mixers. This value is valid on only the PXIe-5830/5831/5832/5841 with PXIe-5655.'
                },
                'name': 'NIRFSA_VAL_LO_SOURCE_SG_SA_SHARED',
                'value': 'SG_SA_Shared'
            }
        ]
    },
    'LoYigMainCoilDrive': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Adjusts the YIG main coil on the LO for an underdamped response.'
                },
                'name': 'NIRFSA_VAL_LO_YIG_MAIN_COIL_DRIVE_NORMAL',
                'value': 2400
            },
            {
                'documentation': {
                    'description': 'Adjusts the YIG main coil on the LO for an overdamped response.'
                },
                'name': 'NIRFSA_VAL_LO_YIG_MAIN_COIL_DRIVE_FAST',
                'value': 2401
            }
        ]
    },
    'LoadConfigurationResetOptions': {
        'values': [
            {
                'documentation': {
                    'description': 'NI-RFSA resets all configurations.'
                },
                'name': 'NIRFSA_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'NI-RFSA skips resetting the de-embedding tables.'
                },
                'name': 'NIRFSA_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_DEEMBEDDING_TABLES',
                'value': 2
            }
        ]
    },
    'NoiseSourcePowerEnabled': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables the noise source power.'
                },
                'name': 'NIRFSA_VAL_DISABLED',
                'value': 1900
            },
            {
                'documentation': {
                    'description': 'Enables the noise source power.'
                },
                'name': 'NIRFSA_VAL_ENABLED',
                'value': 1901
            }
        ]
    },
    'NotchFilterEnabled': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables the notch filter.'
                },
                'name': 'NIRFSA_VAL_NOTCH_FILTER_DISABLED',
                'value': 3400
            },
            {
                'documentation': {
                    'description': 'The notch filter is automatically enabled when it is in the signal path and automatically disabled when it is not in the signal path.'
                },
                'name': 'NIRFSA_VAL_NOTCH_FILTER_ENABLED_WHEN_IN_SIGNAL_PATH',
                'value': 3401
            },
            {
                'documentation': {
                    'description': 'Enables the notch filter. If the notch filter is not in the signal path or if the notch filter is not supported on the device, NI-RFSA returns an error. Select NIRFSA_VAL_NOTCH_FILTER_ENABLED_WHEN_IN_SIGNAL_PATH whenever possible to avoid an error.'
                },
                'name': 'NIRFSA_VAL_NOTCH_FILTER_ENABLED',
                'value': 3402
            }
        ]
    },
    'OutputTerm': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The signal is not exported.'
                },
                'name': 'NIRFSA_VAL_DO_NOT_EXPORT',
                'value': ''
            },
            {
                'documentation': {
                    'description': 'Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.'
                },
                'name': 'NIRFSA_VAL_CLK_OUT',
                'value': 'ClkOut'
            },
            {
                'documentation': {
                    'description': 'Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841.'
                },
                'name': 'NIRFSA_VAL_REF_OUT',
                'value': 'RefOut'
            },
            {
                'documentation': {
                    'description': 'Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.'
                },
                'name': 'NIRFSA_VAL_REF_OUT2',
                'value': 'RefOut2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0.'
                },
                'name': 'NIRFSA_VAL_PFI0',
                'value': 'PFI0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI 1.'
                },
                'name': 'NIRFSA_VAL_PFI1',
                'value': 'PFI1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 0.'
                },
                'name': 'NIRFSA_VAL_PXI_TRIG0',
                'value': 'PXI_Trig0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 1.'
                },
                'name': 'NIRFSA_VAL_PXI_TRIG1',
                'value': 'PXI_Trig1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 2.'
                },
                'name': 'NIRFSA_VAL_PXI_TRIG2',
                'value': 'PXI_Trig2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 3.'
                },
                'name': 'NIRFSA_VAL_PXI_TRIG3',
                'value': 'PXI_Trig3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 4.'
                },
                'name': 'NIRFSA_VAL_PXI_TRIG4',
                'value': 'PXI_Trig4'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 5.'
                },
                'name': 'NIRFSA_VAL_PXI_TRIG5',
                'value': 'PXI_Trig5'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 6.'
                },
                'name': 'NIRFSA_VAL_PXI_TRIG6',
                'value': 'PXI_Trig6'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PXI trigger line 7.'
                },
                'name': 'NIRFSA_VAL_PXI_TRIG7',
                'value': 'PXI_Trig7'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646.'
                },
                'name': 'NIRFSA_VAL_PXI_STAR',
                'value': 'PXI_STAR'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on the PXIe DStar B trigger line. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841.'
                },
                'name': 'NIRFSA_VAL_PXIE_DSTARB',
                'value': 'PXIe_DStarB'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI0 from the front panel DIO terminal.'
                },
                'name': 'NIRFSA_VAL_DIO_PFI0',
                'value': 'DIO/PFI0'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI1 from the front panel DIO terminal.'
                },
                'name': 'NIRFSA_VAL_DIO_PFI1',
                'value': 'DIO/PFI1'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI2 from the front panel DIO terminal.'
                },
                'name': 'NIRFSA_VAL_DIO_PFI2',
                'value': 'DIO/PFI2'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI3 from the front panel DIO terminal.'
                },
                'name': 'NIRFSA_VAL_DIO_PFI3',
                'value': 'DIO/PFI3'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI4 from the front panel DIO terminal.'
                },
                'name': 'NIRFSA_VAL_DIO_PFI4',
                'value': 'DIO/PFI4'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI5 from the front panel DIO terminal.'
                },
                'name': 'NIRFSA_VAL_DIO_PFI5',
                'value': 'DIO/PFI5'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI6 from the front panel DIO terminal.'
                },
                'name': 'NIRFSA_VAL_DIO_PFI6',
                'value': 'DIO/PFI6'
            },
            {
                'documentation': {
                    'description': 'The trigger is received on PFI7 from the front panel DIO terminal.'
                },
                'name': 'NIRFSA_VAL_DIO_PFI7',
                'value': 'DIO/PFI7'
            },
            {
                'documentation': {
                    'description': 'The trigger is received from the Timer Event. This value is valid on only the PXIe-5820/5830/5831/5832/5840/5841, and for digital edge Advance Triggers on the PXIe-5663E/5665.'
                },
                'name': 'NIRFSA_VAL_TIMER_EVENT',
                'value': 'TimerEvent'
            }
        ]
    },
    'OverflowErrorReporting': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Configures NI-RFSA to return a warning when an ADC or onboard signal processing (OSP) overflow occurs.'
                },
                'name': 'NIRFSA_VAL_ERROR_REPORTING_WARNING',
                'value': 1301
            },
            {
                'documentation': {
                    'description': 'Configures NI-RFSA to not return an error or a warning when an ADC or OSP overflow occurs.'
                },
                'name': 'NIRFSA_VAL_ERROR_REPORTING_DISABLED',
                'value': 1302
            }
        ]
    },
    'PowerSpectrumUnits': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Units are dB with reference to 1 milliwatt.'
                },
                'name': 'NIRFSA_VAL_DBM',
                'value': 200
            },
            {
                'documentation': {
                    'description': 'Units are in volts squared.'
                },
                'name': 'NIRFSA_VAL_VOLTS_SQUARED',
                'value': 201
            },
            {
                'documentation': {
                    'description': 'Units are dB with reference to 1 millivolt.'
                },
                'name': 'NIRFSA_VAL_DBMV',
                'value': 202
            },
            {
                'documentation': {
                    'description': 'Units are dB with reference to 1 microvolt.'
                },
                'name': 'NIRFSA_VAL_DBUV',
                'value': 203
            },
            {
                'documentation': {
                    'description': 'Units are in volts.'
                },
                'name': 'NIRFSA_VAL_VOLTS',
                'value': 204
            },
            {
                'documentation': {
                    'description': 'Units are in watts.'
                },
                'name': 'NIRFSA_VAL_WATTS',
                'value': 205
            }
        ]
    },
    'PxiChassisClk10Source': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The device does not drive the PXI 10 MHz backplane Reference Clock.'
                },
                'name': 'NIRFSA_VAL_NONE',
                'value': 'None'
            },
            {
                'documentation': {
                    'description': 'The device drives the PXI 10 MHz backplane Reference Clock with the PXI-5600 onboard clock. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O connector on the PXI-5600 front panel to use this option.'
                },
                'name': 'NIRFSA_VAL_ONBOARD_CLOCK',
                'value': 'OnboardClock'
            },
            {
                'documentation': {
                    'description': 'The device drives the PXI 10 MHz backplane Reference Clock with the reference source attached to the PXI-5600 FREQ REF IN connector. You must connect the 10 MHz OUT connector to the PXI 10 MHz I/O connector on the PXI-5600 front panel to use this option.'
                },
                'name': 'NIRFSA_VAL_REF_IN',
                'value': 'RefIn'
            }
        ]
    },
    'ReferenceTriggerOspDelayEnabled': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables OSP delay for the Reference Trigger.'
                },
                'name': 'NIRFSA_VAL_DISABLED',
                'value': 1900
            },
            {
                'documentation': {
                    'description': 'Enables OSP delay for the Reference Trigger.'
                },
                'name': 'NIRFSA_VAL_ENABLED',
                'value': 1901
            }
        ]
    },
    'ReferenceClockExportedRate': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Exports a 10 MHz Reference Clock.'
                },
                'name': 'NIRFSA_VAL_10MHZ',
                'python_name': '_10MHZ',
                'value': 10000000
            },
            {
                'documentation': {
                    'description': 'Exports a 100 MHz Reference Clock.'
                },
                'name': 'NIRFSA_VAL_100MHZ',
                'python_name': '_100MHZ',
                'value': 100000000
            },
            {
                'documentation': {
                    'description': 'Exports a 1 GHz Reference Clock.'
                },
                'name': 'NIRFSA_VAL_1GHZ',
                'python_name': '_1GHZ',
                'value': 1000000000.0
            }
        ]
    },
    'ReferenceClockExportedTerminal': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The Reference Clock is not exported. This value is not valid for the PXIe-5644/5645/5646.'
                },
                'name': 'NIRFSA_VAL_NONE',
                'value': 'None'
            },
            {
                'documentation': {
                    'description': 'Export the clock on the REF IN/OUT terminal on the PXI/PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, PXIe-5694, or PXIe-5820/5830/5831/5832/5840/5841.'
                },
                'name': 'NIRFSA_VAL_REF_OUT',
                'value': 'RefOut'
            },
            {
                'documentation': {
                    'description': 'Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E.'
                },
                'name': 'NIRFSA_VAL_REF_OUT2',
                'value': 'RefOut2'
            },
            {
                'documentation': {
                    'description': 'Export the clock on the CLK OUT terminal on the IF digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841.'
                },
                'name': 'NIRFSA_VAL_CLK_OUT',
                'value': 'ClkOut'
            },
            {
                'documentation': {
                    'description': 'Export the clock on the REF OUT terminal on the PXIe-5694. This value is valid only for the PXIe-5667.'
                },
                'name': 'NIRFSA_VAL_IF_COND_REF_OUT',
                'value': 'IFCondRefOut'
            }
        ]
    },
    'ReferenceClockSource': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'No Reference Clock is required for the current device configuration. This value is valid only for the PXIe-5694 or the PXIe-5668.'
                },
                'name': 'NIRFSA_VAL_NONE',
                'value': 'None'
            },
            {
                'documentation': {
                    'description': '**PXI-5661 **NI-RFSA locks the NI-RFSA device to the PXI-5600 RF downconverter onboard clock.**PXIe-5663/5663E **NI-RFSA locks the PXIe-5663/5663E to the PXI/PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXI/PXIe-5652 to the CLK IN terminal on the PXIe-5622. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXI/PXIe-5652, connect the REF IN/OUT connector on the PXI/PXIe-5652 to the CLK IN terminal on the PXI5622.**PXIe-5665 **NI-RFSA locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622.**PXIe-5667 **NI-RFSA locks the PXIe-5667 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622, and connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694.**PXIe-5668 **Lock the PXIe-5668 to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624.**PXIe-5830/5831 **For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831/5832, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector.**PXIe-5831/5832 with PXIe-5653 **Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector.**PXIe-5644/5645/5646, PXIe-5820/5840/5841 **Lock the NI-RFSA device to its onboard clock.**PXIe-5841 with PXIe-5655 **Lock to the PXIe-5655 onboard clock. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector.**PXIe-5842 **Lock to the PXIe-5655 onboard clock. Cables between modules are required as shown in the User Manual for the instrument.**PXIe-5860 **Lock to the PXIe-5860 onboard clock.'
                },
                'name': 'NIRFSA_VAL_ONBOARD_CLOCK',
                'value': 'OnboardClock'
            },
            {
                'documentation': {
                    'description': '**PXI-5661 **NI-RFSA locks the NI-RFSA device to the signal at the external FREQ REF IN connector on the PXI-5600**PXIe-5663/5663E **Connect the external signal to the PXI/PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXI/PXIe-5652 to the CLK IN terminal on the PXIe-5622. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXI/PXIe-5652, this configuration can only be used in external digitizer mode.**PXIe-5665 **Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the NIRFSA_ATTR_REF_CLOCK_RATE attribute according to the frequency of your external clock signal.**PXIe-5667 **Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the CLK IN terminal on the PXIe-5622, and connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. If your external clock signal frequency is set to a frequency other than 10 MHz, set the NIRFSA_ATTR_REF_CLOCK_RATE attribute according to the frequency of your external clock signal.**PXIe-5668 **Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT on the PXIe-5606 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the **clock rate** parameter according to the frequency of your external clock signal.**PXIe-5694 **Connect the Reference Clock signal to the REF/LO IN connector on the PXIe-5694 front panel.**PXIe-5644/5645/5646, PXIe-5820/5840/5841 **Lock the NI-RFSA device to the signal at the external REF IN connector.**PXIe-5830/5831 **For the PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For the PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For the PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For the PXIe-5831/5832, lock the external signal to the PXIe-3622 REF IN connector.**PXIe-5831/5832 with PXIe-5653 **Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector.**PXIe-5841 with PXIe-5655 **Lock to the signal at the REF IN connector on the associated PXIe-5655. Connect the REF OUT connector on the PXIe-5655 to the PXIe-5841 REF IN connector. **PXIe-5842 **Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the User Manual for the instrument. PXIe-5860 Lock to the signal at the REF IN connector on the PXIe-5860.'
                },
                'name': 'NIRFSA_VAL_REF_IN',
                'value': 'RefIn'
            },
            {
                'documentation': {
                    'description': '**PXI-5661 **NI-RFSA locks the NI-RFSA device to the PXI backplane clock using the PXI-5600. You must connect the PXI 10 MHz connector to the REF IN connector on the PXI-5600 front panel to use this option. **PXIe-5668 **Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624.**PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5667, PXIe-5694, PXIe-5820/5830/5831/5831/5832 with PXIe-5653/5840/5840 with PXIe-5653/5841/5841 with PXIe-5655/5842/5860 **Lock the device to the PXI backplane clock.'
                },
                'name': 'NIRFSA_VAL_PXI_CLK',
                'value': 'PXI_Clk'
            },
            {
                'documentation': {
                    'description': '**PXI-5661 **This configuration does not apply to the PXI-5661.**PXIe-5663/5663E **NI-RFSA locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXI/PXIe-5652.**PXIe-5665 **NI-RFSA locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the NIRFSA_ATTR_REF_CLOCK_RATE attribute to 100 MHz.**PXIe-5667 **NI-RFSA locks the PXIe-5667 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5622, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Connect the 10 MHZ REF OUT terminal on the PXIe-5653 to the REF/LO IN connector on the PXIe-5694. Set the NIRFSA_ATTR_REF_CLOCK_RATE attribute to 100 MHz.**PXIe-5668 **Lock the PXIe-5668 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the **clock rate** parameter to 100 MHz.**PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831/5832 with PXIe-5653/5840/5840 with PXIe-5653/5841/5841 with PXIe-5655/5842/5860 **This configuration does not apply.'
                },
                'name': 'NIRFSA_VAL_CLK_IN',
                'value': 'ClkIn'
            },
            {
                'documentation': {
                    'description': '**PXIe-5831/5832 with PXIe-5653 **NI-RFSA configures the PXIe-5653 to export the Reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the Reference Clock source. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector.**PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5644/5645/5646, PXIe-5820/5840/5841/5841 with PXIe-5655 /5842/5860**This configuration does not apply.'
                },
                'name': 'NIRFSA_VAL_PXI_CLK_MASTER',
                'value': 'PXI_ClkMaster'
            },
            {
                'documentation': {
                    'description': '**PXI-5661, PXIe-5663/5663E/5665/5667/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831/5832 with PXIe-5653/5840/5841/5841 with PXIe-5655 **This configuration does not apply.'
                },
                'name': 'NIRFSA_VAL_REF_IN_2',
                'value': 'RefIn2'
            }
        ]
    },
    'ReferenceLevelDataType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The data is the configuration data when the mechanical relay is disabled. Use this option to save uncalibrated measurements for more advanced operations.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_MECHANICAL_ATTENUATOR_DISABLED',
                'value': 1801
            },
            {
                'documentation': {
                    'description': ' The data is the default configuration data.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_DEFAULT',
                'value': 1800
            }
        ]
    },
    'ReferenceTriggerDigitalEdgeEdge': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The trigger asserts on the rising edge of the signal.'
                },
                'name': 'NIRFSA_VAL_RISING_EDGE',
                'value': 900
            },
            {
                'documentation': {
                    'description': 'The trigger asserts on the falling edge of the signal'
                },
                'name': 'NIRFSA_VAL_FALLING_EDGE',
                'value': 901
            }
        ]
    },
    'ReferenceTriggerIqPowerEdgeSlope': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The trigger asserts when the signal power is rising.'
                },
                'name': 'NIRFSA_VAL_RISING_SLOPE',
                'value': 1000
            },
            {
                'documentation': {
                    'description': 'The trigger asserts when the signal power is falling.'
                },
                'name': 'NIRFSA_VAL_FALLING_SLOPE',
                'value': 1001
            }
        ]
    },
    'ReferenceTriggerType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'No Reference Trigger is configured.'
                },
                'name': 'NIRFSA_VAL_NONE',
                'value': 600
            },
            {
                'documentation': {
                    'description': 'The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the NIRFSA_ATTR_DIGITAL_EDGE_REF_TRIGGER_SOURCE attribute.'
                },
                'name': 'NIRFSA_VAL_DIGITAL_EDGE',
                'value': 601
            },
            {
                'documentation': {
                    'description': 'The Reference Trigger is asserted when the signal is changing past the level specified with the slope (rising or falling) configured with the NIRFSA_ATTR_IQ_POWER_EDGE_REF_TRIGGER_SLOPE attribute.'
                },
                'name': 'NIRFSA_VAL_IQ_POWER_EDGE',
                'value': 603
            },
            {
                'documentation': {
                    'description': 'The Reference Trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the nirfsa_SendSoftwareEdgeTrigger function and selecting NIRFSA_VAL_REF_TRIGGER as the **trigger** parameter.'
                },
                'name': 'NIRFSA_VAL_SOFTWARE_EDGE',
                'value': 604
            },
            {
                'documentation': {
                    'description': 'The Reference Trigger is asserted when the I or Q signal is changed past the level specified with the slope configured with the NIRFSA_ATTR_IQ_ANALOG_EDGE_REF_TRIGGER_SLOPE attribute. This value is valid only for PXIe-5644/5645 devices.'
                },
                'name': 'NIRFSA_VAL_IQ_ANALOG_EDGE',
                'value': 605
            }
        ]
    },
    'ResetWithOptionsStepsToOmit': {
        'codegen_method': 'public',
        'class': 'IntFlag',
        'values': [
            {
                'documentation': {
                    'description': 'Omits deleting de-embedding tables. This step is valid only for the PXIe-5830/5831/5832/5840.'
                },
                'name': 'NIRFSA_VAL_RESET_WITH_OPTIONS_DEEMBEDDING_TABLES',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'No step is omitted during reset.'
                },
                'name': 'NIRFSA_VAL_RESET_WITH_OPTIONS_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after a reset.'
                },
                'name': 'NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES',
                'value': 1
            }
        ]
    },
    'RfLbSigCondPathSel': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'yet to be defined '
                },
                'name': 'NIRFSA_VAL_EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_1',
                'python_name': 'EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_1',
                'value': 3700
            },
            {
                'documentation': {
                    'description': 'yet to be defined '
                },
                'name': 'NIRFSA_VAL_EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_2',
                'python_name': 'EXT_CAL_RF_LOWBAND_SIGNAL_CONDITIONING_PATH_2',
                'value': 3701
            }
        ]
    },
    'RfPathSelection': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': ' The data is the default configuration data.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_RF_BAND_1',
                'python_name': 'EXT_CAL_RF_BAND_1',
                'value': 1700
            },
            {
                'documentation': {
                    'description': 'The data is the configuration data when the mechanical relay is disabled. Use this option to save uncalibrated measurements for more advanced operations.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_RF_BAND_2',
                'python_name': 'EXT_CAL_RF_BAND_2',
                'value': 1701
            },
            {
                'documentation': {
                    'description': ' The data is the default configuration data.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_RF_BAND_3',
                'python_name': 'EXT_CAL_RF_BAND_3',
                'value': 1702
            },
            {
                'documentation': {
                    'description': ' The data is the default configuration data.'
                },
                'name': 'NIRFSA_VAL_EXT_CAL_RF_BAND_4',
                'python_name': 'EXT_CAL_RF_BAND_4',
                'value': 1703
            }
        ]
    },
    'SelfCalibrationStep': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Calls for preselector alignment. '
                },
                'name': 'NIRFSA_VAL_SELF_CAL_PRESELECTOR_ALIGNMENT',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'Measures the changes in gain since the last external calibration was run.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_GAIN_REFERENCE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Measures the IF response of the entire system for each of the supported IF filters'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_IF_FLATNESS',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Calls for digitizer self-calibration, if the digitizer is associated with the RF downconverter.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_DIGITIZER_SELF_CAL',
                'value': 8
            },
            {
                'documentation': {
                    'description': 'Calls for LO self-calibration, if the LO source module is associated with the RF downconverter.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_LO_SELF_CAL',
                'value': 16
            },
            {
                'documentation': {
                    'description': 'Selects the Amplitude Accuracy self-calibration step.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_AMPLITUDE_ACCURACY',
                'value': 32
            },
            {
                'documentation': {
                    'description': 'Selects the Residual LO Power self-calibration step.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_RESIDUAL_LO_POWER',
                'value': 64
            },
            {
                'documentation': {
                    'description': 'Selects the Image Suppression self-calibration step.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_IMAGE_SUPPRESSION',
                'value': 128
            },
            {
                'documentation': {
                    'description': 'Selects the Synthesizer Alignment self-calibration step.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_SYNTHESIZER_ALIGNMENT',
                'value': 256
            },
            {
                'documentation': {
                    'description': 'Selects the DC Offset self-calibration step.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_DC_OFFSET',
                'value': 512
            }
        ]
    },
    'SelfCalibrateRangeStepsToOmit': {
        'class': 'IntFlag',
        'values': [
            {
                'documentation': {
                    'description': 'Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_DIGITIZER_SELF_CAL',
                'value': 8
            },
            {
                'documentation': {
                    'description': 'Omits the LO Self Cal step. If you omit this step, the power level of the LO is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_PRESELECTOR_ALIGNMENT',
                'value': 1
            },
            {
                'documentation': {
                    'description': 'No calibration steps are omitted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_OMIT_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Omits the Power Level Accuracy step. If you omit this step, the power level accuracy of the device is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_GAIN_REFERENCE',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_IF_FLATNESS',
                'value': 4
            },
            {
                'documentation': {
                    'description': 'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_LO_SELF_CAL',
                'value': 10
            },
            {
                'documentation': {
                    'description': 'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_AMPLITUDE_ACCURACY',
                'value': 20
            },
            {
                'documentation': {
                    'description': 'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_RESIDUAL_LO_POWER',
                'value': 40
            },
            {
                'documentation': {
                    'description': 'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_IMAGE_SUPPRESSION',
                'value': 80
            },
            {
                'documentation': {
                    'description': 'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_SYNTHESIZER_ALIGNMENT',
                'value': 100
            },
            {
                'documentation': {
                    'description': 'Omits the Voltage Controlled Oscillator (VCO) Alignment step. If you omit this step, the LO PLL is not adjusted.'
                },
                'name': 'NIRFSA_VAL_SELF_CAL_DC_OFFSET',
                'value': 200
            }
        ]
    },
    'Signal': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'NI-RFSA routes a Start Trigger.'
                },
                'name': 'NIRFSA_VAL_START_TRIGGER',
                'value': 1100
            },
            {
                'documentation': {
                    'description': 'NI-RFSA routes a Reference'
                },
                'name': 'NIRFSA_VAL_REF_TRIGGER',
                'value': 702
            },
            {
                'documentation': {
                    'description': 'NI-RFSA routes an Advance'
                },
                'name': 'NIRFSA_VAL_ADVANCE_TRIGGER',
                'value': 1102
            },
            {
                'documentation': {
                    'description': 'NI-RFSA routes a Ready for Start Event.'
                },
                'name': 'NIRFSA_VAL_READY_FOR_START_EVENT',
                'value': 1200
            },
            {
                'documentation': {
                    'description': 'NI-RFSA routes a Ready for Reference Event..'
                },
                'name': 'NIRFSA_VAL_READY_FOR_REF_EVENT',
                'value': 1201
            },
            {
                'documentation': {
                    'description': 'NI-RFSA routes a End of Record Event.'
                },
                'name': 'NIRFSA_VAL_END_OF_RECORD_EVENT',
                'value': 1203
            },
            {
                'documentation': {
                    'description': 'NI-RFSA routes a Done Event.'
                },
                'name': 'NIRFSA_VAL_DONE_EVENT',
                'value': 1204
            },
            {
                'documentation': {
                    'description': 'NI-RFSA routes a Reference Clock.'
                },
                'name': 'NIRFSA_VAL_REF_CLOCK',
                'value': 1205
            },
            {
                'documentation': {
                    'description': 'NI-RFSA routes a User Defined Signal.'
                },
                'name': 'NIRFSA_VAL_USER',
                'value': 1206
            }
        ]
    },
    'SignalConditioningEnabled': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Enables signal conditioning.'
                },
                'name': 'NIRFSA_VAL_SIGNAL_CONDITIONING_ENABLED',
                'value': 3600
            },
            {
                'documentation': {
                    'description': 'Bypasses all signal conditioning.'
                },
                'name': 'NIRFSA_VAL_SIGNAL_CONDITIONING_BYPASSED',
                'value': 3601
            }
        ]
    },
    'SmoothSpectrumEnabled': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables spectrum smoothing.'
                },
                'name': 'NIRFSA_VAL_DISABLED',
                'value': 1900
            },
            {
                'documentation': {
                    'description': 'Enables spectrum smoothing.'
                },
                'name': 'NIRFSA_VAL_ENABLED',
                'value': 1901
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
                'name': 'NIRFSA_VAL_PORT1_TOWARDS_DUT',
                'value': 3800
            },
            {
                'documentation': {
                    'description': 'Port 2 of the S2P is oriented towards the DUT port.'
                },
                'name': 'NIRFSA_VAL_PORT2_TOWARDS_DUT',
                'value': 3801
            }
        ]
    },
    'SpectrumAveragingMode': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Configures NI-RFSA to perform no averaging on acquisitions.'
                },
                'name': 'NIRFSA_VAL_NO_AVERAGING',
                'value': 400
            },
            {
                'documentation': {
                    'description': 'Configures NI-RFSA for root-mean-square (RMS) averaging. RMS averaging reduces signal fluctuations but not the noise floor. RMS averaging averages the energy, or power, of the signal. This averaging prevents noise floor reduction and gives averaged RMS quantities of single-channel measurements zero phase. RMS averaging for dual-channel measurements preserves important phase information.'
                },
                'name': 'NIRFSA_VAL_RMS_AVERAGING',
                'value': 401
            },
            {
                'documentation': {
                    'description': 'Configures NI-RFSA for vector averaging. Vector averaging reduces noise from synchronous signals. Vector averaging computes the average of complex quantities directly, which means that it allows separate averaging for real and imaginary parts. Complex averaging such as vector averaging reduces noise and usually requires a trigger to improve block-to-block phase coherence.'
                },
                'name': 'NIRFSA_VAL_VECTOR_AVERAGING',
                'value': 402
            },
            {
                'documentation': {
                    'description': 'Configures NI-RFSA for peak-hold averaging. Peak-hold averaging retains the RMS peak levels of the averaged quantities. The peak-hold averaging process performs peak-hold at each frequency bin separately to retain peak RMS levels from one FFT record to the next.'
                },
                'name': 'NIRFSA_VAL_PEAK_HOLD_AVERAGING',
                'value': 403
            },
            {
                'documentation': {
                    'description': 'Configures NI-RFSA to perform no averaging on acquisitions.'
                },
                'name': 'NIRFSA_VAL_MIN_HOLD_AVERAGING',
                'value': 404
            },
            {
                'documentation': {
                    'description': 'Configures NI-RFSA to perform no averaging on acquisitions.'
                },
                'name': 'NIRFSA_VAL_SCALAR_AVERAGING',
                'value': 405
            },
            {
                'documentation': {
                    'description': 'Configures NI-RFSA to perform no averaging on acquisitions.'
                },
                'name': 'NIRFSA_VAL_LOG_AVERAGING',
                'value': 406
            }
        ]
    },
    'SpectrumFftWindowType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'No window is applied.'
                },
                'name': 'NIRFSA_VAL_UNIFORM',
                'value': 500
            },
            {
                'documentation': {
                    'description': 'The Hanning window is useful for analyzing transients longer than the time duration of the window, and also for general-purpose applications.'
                },
                'name': 'NIRFSA_VAL_HANNING',
                'value': 501
            },
            {
                'documentation': {
                    'description': 'A Hamming window is applied to the waveform using the following equation: y[i] = x[i] * (0.54 - 0.46cos(w)) where w = (2)i/n and n = the waveform size. Note: Hanning and Hamming windows are somewhat similar. However, in the time domain, the Hamming window does not get as close to zero near the edges as does the Hanning window.'
                },
                'name': 'NIRFSA_VAL_HAMMING',
                'value': 502
            },
            {
                'documentation': {
                    'description': 'A Blackman-Harris window is applied to the waveform using the following equation: y[i] = x[i] * (0.42323 - 0.49755*cos(w) + 0.07922*cos(2w))'
                },
                'name': 'NIRFSA_VAL_BLACKMAN_HARRIS',
                'value': 503
            },
            {
                'documentation': {
                    'description': 'An Exact Blackman window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w))'
                },
                'name': 'NIRFSA_VAL_EXACT_BLACKMAN',
                'value': 504
            },
            {
                'documentation': {
                    'description': 'A Blackman window is useful for analyzing transient signals, and provides similar windowing to Hanning and Hamming windows but adds one additional cosine term to reduce ripple. A Blackman window is applied to the waveform using the following equation: y[i] = x[i] * (0.42 - 0.50*cos(w) + 0.08*cos(2w))'
                },
                'name': 'NIRFSA_VAL_BLACKMAN',
                'value': 505
            },
            {
                'documentation': {
                    'description': 'The fifth-order Flat Top window has the best amplitude accuracy of all the window functions. The increased amplitude accuracy (0.02 dB for signals exactly between integral cycles) is at the expense of frequency selectivity. The Flat Top window is most useful in accurately measuring the amplitude of single frequency components with little nearby spectral energy in the signal. A fifth-order Flat Top window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w) - a3*cos(3w) + a4*cos(4w))'
                },
                'name': 'NIRFSA_VAL_FLAT_TOP',
                'value': 506
            },
            {
                'documentation': {
                    'description': 'A 4-term Blackman-Harris window is a general purpose window; it has side-lobe rejection in the upper 90 dB, with moderately wide side lobe. A 4-term Blackman Harris window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w) - a3*cos(3w))'
                },
                'name': 'NIRFSA_VAL_4_TERM_BLACKMAN_HARRIS',
                'python_name': '_4_TERM_BLACKMAN_HARRIS',
                'value': 507
            },
            {
                'documentation': {
                    'description': 'A 7-term Blackman-Harris window has the highest dynamic range; it is ideal for signal-to-noise ratio applications. A 7-term Blackman Harris window is applied to the waveform using the following equation: y[i] = x[i] * (a0 - a1*cos(w) + a2*cos(2w) - a3*cos(3w) + a4*cos(4w) - a5*cos(5w) + a6*cos(6w))'
                },
                'name': 'NIRFSA_VAL_7_TERM_BLACKMAN_HARRIS',
                'python_name': '_7_TERM_BLACKMAN_HARRIS',
                'value': 508
            },
            {
                'documentation': {
                    'description': 'The Low Side Lobe window further reduces the size of the main lobe. The following equation defines the Low Side Lobe window. where   *N* is the length of window'
                },
                'name': 'NIRFSA_VAL_LOW_SIDE_LOBE',
                'value': 509
            },
            {
                'documentation': {
                    'description': 'A Gaussian window is applied to the waveform using the following equation: y[i] = x[i] * exp(-0.5*(i - (N-1)/2)^2 / ((N-1)/2)^2) where N is the length of the window'
                },
                'name': 'NIRFSA_VAL_GAUSSIAN',
                'value': 510
            },
            {
                'documentation': {
                    'description': 'A Kaiser-Bessel window is applied to the waveform using the following equation: y[i] = x[i] * I0(β*sqrt(1 - (2i/(N-1) - 1)^2))/I0(β) where i is between 0 and N-1, N is the length of the window, β determines the shape of the window, and I0 is the zeroth order Modified Bessel function of the first kind'
                },
                'name': 'NIRFSA_VAL_KAISER_BESSEL',
                'value': 511
            }
        ]
    },
    'SpectrumResolutionBandwidthType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Defines the resolution bandwidth (RBW) in terms of the 3 dB bandwidth of the window specified by the NIRFSA_ATTR_FFT_WINDOW_TYPE attribute.'
                },
                'name': 'NIRFSA_VAL_RBW_THREE_DECIBELS',
                'value': 300
            },
            {
                'documentation': {
                    'description': 'Defines the RBW in terms of the 6 dB bandwidth of the window specified by the NIRFSA_ATTR_FFT_WINDOW_TYPE attribute.'
                },
                'name': 'NIRFSA_VAL_RBW_SIX_DECIBELS',
                'value': 301
            },
            {
                'documentation': {
                    'description': 'Defines the RBW in terms of the display resolution, which is the ratio of the sampling frequency to the number of samples that you acquire.'
                },
                'name': 'NIRFSA_VAL_RBW_BIN_WIDTH',
                'value': 302
            },
            {
                'documentation': {
                    'description': 'Defines the RBW in terms of the equivalent noise bandwidth (ENBW) of the window specified by the NIRFSA_ATTR_FFT_WINDOW_TYPE attribute.'
                },
                'name': 'NIRFSA_VAL_RBW_EQUIVALENT_NOISE_BANDWIDTH',
                'value': 303
            }
        ]
    },
    'StartTriggerDigitalEdgeEdge': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'The trigger asserts on the rising edge of the signal.PXI-5661, PXIe-5663/5663E/5665/5668'
                },
                'name': 'NIRFSA_VAL_RISING_EDGE',
                'value': 900
            },
            {
                'documentation': {
                    'description': 'The trigger asserts on the falling edge of the signal | PXIe-5668 '
                },
                'name': 'NIRFSA_VAL_FALLING_EDGE',
                'value': 901
            }
        ]
    },
    'StartTriggerType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'No Start Trigger is configured.'
                },
                'name': 'NIRFSA_VAL_NONE',
                'value': 600
            },
            {
                'documentation': {
                    'description': 'The Start Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the NIRFSA_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE attribute.'
                },
                'name': 'NIRFSA_VAL_DIGITAL_EDGE',
                'value': 601
            },
            {
                'documentation': {
                    'description': 'The Start Trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the nirfsa_SendSoftwareEdgeTrigger function and selecting NIRFSA_VAL_START_TRIGGER as the value of the **trigger** parameter.'
                },
                'name': 'NIRFSA_VAL_SOFTWARE_EDGE',
                'value': 604
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
                'name': 'NIRFSA_VAL_RESET_WITH_OPTIONS_DEEMBEDDING_TABLES',
                'value': 2
            },
            {
                'documentation': {
                    'description': 'No step is omitted during reset.'
                },
                'name': 'NIRFSA_VAL_RESET_WITH_OPTIONS_NONE',
                'value': 0
            },
            {
                'documentation': {
                    'description': 'Omits the routing reset step. Routing is preserved after a reset. However, routing related properties are reset to default, and routing is released if the default properties are committed after a reset.'
                },
                'name': 'NIRFSA_VAL_RESET_WITH_OPTIONS_ROUTES',
                'value': 1
            }
        ]
    },
    'SyncRefTriggerDelayEnabled': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Disables synchronization reference trigger delay.'
                },
                'name': 'NIRFSA_VAL_DISABLED',
                'value': 1900
            },
            {
                'documentation': {
                    'description': 'Enables synchronization reference trigger delay.'
                },
                'name': 'NIRFSA_VAL_ENABLED',
                'value': 1901
            }
        ]
    },
    'SoftwareTriggerType': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'NI-RFSA sends a Start software trigger.'
                },
                'name': 'NIRFSA_VAL_START_TRIGGER',
                'value': 1100
            },
            {
                'documentation': {
                    'description': 'NI-RFSA sends a Reference software trigger. '
                },
                'name': 'NIRFSA_VAL_REF_TRIGGER',
                'value': 702
            },
            {
                'documentation': {
                    'description': 'NI-RFSA sends an Advance software trigger.'
                },
                'name': 'NIRFSA_VAL_ADVANCE_TRIGGER',
                'value': 1102
            },
            {
                'documentation': {
                    'description': 'NI-RFSA sends an Arm Reference software trigger. This trigger is not valid for the PXIe-5668.'
                },
                'name': 'NIRFSA_VAL_ARM_REF_TRIGGER',
                'value': 1103
            }
        ]
    },
    'UserSourcePulseWidthUnits': {
        'codegen_method': 'public',
        'values': [
            {
                'documentation': {
                    'description': 'Units are seconds.'
                },
                'name': 'NIRFSA_VAL_PULSE_WIDTH_UNITS_SECONDS',
                'value': 6200
            },
            {
                'documentation': {
                    'description': 'Units are clock periods.'
                },
                'name': 'NIRFSA_VAL_PULSE_WIDTH_UNITS_CLOCK_PERIODS',
                'value': 6201
            }
        ]
    }
}
