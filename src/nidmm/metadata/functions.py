# -*- coding: utf-8 -*-
# This file is generated from API metadata for NI-DMM version 19.1.0d11
functions = {
    '4022Control': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'name': 'configuration',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Abort': {
        'documentation': {
            'description': '\nAborts a previously initiated measurement and returns the DMM to the\nIdle state.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
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
    'CachedFetch': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'reading',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CachedReadStatus': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'acqBacklog',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'acqDone',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustAcFilter': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nFor the NI 4080/4081/4082 and the NI 4070/4071/4072, calibrates the\nfilter coefficients used for AC measurements of the supplied **Mode**\nand **Range**.\n',
            'note': '\nRefer to the calibration procedure for your device before using this\nfunction.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niDMM_InitExtCal. The handle\nidentifies a particular instrument calibration session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the calibration **mode** used to acquire the measurement.\n\nFor valid modes, refer to the calibration procedure for your device.\n'
                },
                'name': 'mode',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **range** to calibrate.\n\nFor valid ranges, refer to the calibration procedure for your device.\nAuto-ranging is not supported for calibration operations.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the **frequency** of the input signal.'
                },
                'name': 'frequency',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the **expected_value** of the measurement.'
                },
                'name': 'expectedValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustGain': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCalibrates the gain coefficient for the supplied **Mode**, **Range**,\nand **Input_Resistance**.\n',
            'note': '\nThe NI 4050 and NI 4060 are not supported.\nRefer to the calibration procedure for your device before using this\nfunction.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niDMM_InitExtCal. The handle\nidentifies a particular instrument calibration session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the calibration **mode** used to acquire the measurement.\n\nFor valid modes, refer to the calibration procedure for your device.\n'
                },
                'name': 'mode',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **range** to calibrate.\n\nFor valid ranges, refer to the calibration procedure for your device.\nAuto-ranging is not supported for calibration operations.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **input_resistance** that the device should use.\n**input_resistance** values are coerced up to the closest\n**input_resistance**.\n'
                },
                'name': 'inputResistance',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the **expected_value** of the measurement.'
                },
                'name': 'expectedValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustLC': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nFor the NI 4082 and NI 4072 only, performs a specialized LC calibration\nstep depending on the specified **Type**.\n',
            'note': '\nRefer to the calibration procedure for your device before using this\nfunction.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niDMM_InitExtCal. The handle\nidentifies a particular instrument calibration session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies which of the LC calibration steps to perform.',
                    'table_body': [
                        [
                            'L & C Open (default)',
                            'Calibrates the open compensation.'
                        ],
                        [
                            'L & C Short',
                            'Calibrates the short compensation.'
                        ],
                        [
                            'L & C 25 Ω',
                            'Calibrates the 25 Ω resistance.'
                        ],
                        [
                            'L & C 1 kΩ',
                            'Calibrates the 1 kΩ resistance.'
                        ],
                        [
                            'L & C 5 kΩ',
                            'Calibrates the 5 kΩ resistance.'
                        ],
                        [
                            'L & C 100 kΩ',
                            'Calibrates the 100 kΩ resistance.'
                        ]
                    ]
                },
                'name': 'type',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustLinearization': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'For the NI 4065 only, compensates for any non-linearities.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niDMM_InitExtCal. The handle\nidentifies a particular instrument calibration session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the calibration **function** used to acquire the measurement.\n\nFor valid modes, refer to the *NI 4065 6½ Digit DMM Calibration\nProcedure*.\n'
                },
                'name': 'function',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **range** to calibrate. **range** values are coerced up to\nthe closest **range**.\n\nFor valid ranges, refer to the *NI 4065 6½ Digit DMM Calibration\nProcedure*. Auto-ranging is not supported for calibration operations.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **input_resistance** that the device should use.\n**input_resistance** values are coerced up to the closest\n**input_resistance**.\n'
                },
                'name': 'inputResistance',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the **expected_value** of the measurement.'
                },
                'name': 'expectedValue',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustMisc': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nPerforms a specialized calibration step depending on the specified\n**Type**.\n',
            'note': '\nThe NI 4050 and NI 4060 are not supported.\nRefer to the calibration procedure for your device before using this\nfunction.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niDMM_InitExtCal. The handle\nidentifies a particular instrument calibration session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies which of the miscellaneous calibration steps to perform.',
                    'table_body': [
                        [
                            'NIDMM_EXTCAL_MISCCAL_VREF (default)',
                            'Calibrate the Voltage Reference.'
                        ],
                        [
                            'NIDMM_EXTCAL_MISCCAL_RREF',
                            'Calibrate the Resistance Reference.'
                        ],
                        [
                            'NIDMM_EXTCAL_MISCCAL_ZINT',
                            'Calibrate the Internal Impedance.'
                        ],
                        [
                            'NIDMM_EXTCAL_MISCCAL_2WIRELEAKAGE',
                            'Calibrate the 2-wire Leakage resistance.'
                        ],
                        [
                            'NIDMM_EXTCAL_MISCCAL_4WIRELEAKAGE',
                            'Calibrate the 4-wire Leakage resistance.'
                        ],
                        [
                            'NIDMM_EXTCAL_MISCCAL_SECTION',
                            'Update calibration information and verify calibration completeness.'
                        ]
                    ]
                },
                'name': 'type',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustOffset': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCalibrates the offset and Auto Zero offset for the supplied **Mode**,\n**Range**, and **Input_Resistance**.\n',
            'note': '\nThe NI 4050 and NI 4060 are not supported.\nRefer to the calibration procedure for your device before using this\nfunction.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niDMM_InitExtCal. The handle\nidentifies a particular instrument calibration session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the calibration **mode** used to acquire the measurement.\n\nFor valid modes, refer to the calibration procedure for your device.\n'
                },
                'name': 'mode',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **range** to calibrate.\n\nFor valid ranges, refer to the calibration procedure for your device.\nAuto-ranging is not supported for calibration operations.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **input_resistance** that the device should use.\n**input_resistance** values are coerced up to the closest\n**input_resistance**.\n'
                },
                'name': 'inputResistance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalculateAccuracy': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'frequency',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'multiplier',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'offset',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViBoolean': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis function checks the validity of a value you specify for a ViBoolean\nattribute.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. National Instruments DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
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
            'description': '\nThis function checks the validity of a value you specify for a ViInt32\nattribute.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. National Instruments DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
                },
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CheckAttributeViReal64': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis function checks the validity of a value you specify for a ViReal64\nattribute.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. National Instruments DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
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
            'description': '\nThis function checks the validity of a value you specify for a ViSession\nattribute.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. National Instruments DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
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
            'description': '\nThis function checks the validity of a value you specify for a ViString\nattribute.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. National Instruments DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
                },
                'name': 'attributeValue',
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearError': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nClears the error information for the current execution thread and the\nIVI session you specify. If you pass VI_NULL for the\n**Instrument_Handle** parameter, this function clears the error\ninformation only for the current execution thread.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
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
    'ClearInterchangeWarnings': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Clears the list of current interchange warnings.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CloseExtCal': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nPerforms the specified **Action**, closes the specified external\ncalibration session obtained from niDMM_InitExtCal, and deallocates\nresources that it reserved.\n',
            'note': '\nThe NI 4050 and NI 4060 are not supported.\nRefer to the calibration procedure for your device before using this\nfunction.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niDMM_InitExtCal. The handle\nidentifies a particular instrument calibration session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies whether the driver saves the updated calibration constants.',
                    'table_body': [
                        [
                            'NIDMM_EXTCAL_ACTION_ABORT (default)',
                            'Restores the calibration constants to what they were before starting the external calibration procedure.'
                        ],
                        [
                            'NIDMM_EXTCAL_ACTION_SAVE',
                            'Saves the new calibration constants to the device.'
                        ]
                    ]
                },
                'name': 'action',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Configure': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'measFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'resolution',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'minFrequency',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'maxFrequency',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureADCCalibration': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nFor the NI 4080/4081/4082 and NI 4070/4071/4072, allows the DMM to\ncompensate for gain drift since the last external calibration or\nself-calibration. When **ADC_Calibration** is ON, the DMM measures an\ninternal reference to calculate the correct gain for the measurement.\nWhen **ADC_Calibration** is OFF, the DMM does not compensate for\nchanges to the gain.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **ADC_Calibration** setting. The driver sets\nNIDMM_ATTR_ADC_CALIBRATION to this value.\nNIDMM_VAL_ADC_CALIBRATION_ON enables **ADC_Calibration**.\nNIDMM_VAL_ADC_CALIBRATION_OFF disables **ADC_Calibration**. If you\nset the value to NIDMM_VAL_ADC_CALIBRATION_AUTO, the driver\ndetermines whether to enable **ADC_Calibration** based on the\nmeasurement function and resolution that you configure. If you configure\nthe NI 4080/4081/4082 or NI 4070/4071/4072 for a 6½–digit and greater\nresolution DC measurement, the driver enables ADC Calibration. For all\nother measurement configurations, the driver disables\n**ADC_Calibration**.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_ADC_CALIBRATION_AUTO (default)',
                            '-1.0',
                            'The DMM enables or disables **ADC_Calibration** based on the configured function and resolution.'
                        ],
                        [
                            'NIDMM_VAL_ADC_CALIBRATION_OFF',
                            '0',
                            'The DMM does not compensate for changes to the gain.'
                        ],
                        [
                            'NIDMM_VAL_ADC_CALIBRATION_ON',
                            '1',
                            'The DMM measures an internal reference to calculate the correct gain for the measurement.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'name': 'adcCalibration',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureAcBandwidth': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the NIDMM_ATTR_AC_MIN_FREQ and NIDMM_ATTR_AC_MAX_FREQ\nattributes, which the DMM uses for AC measurements.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the minimum expected frequency component of the input signal\nin hertz. This parameter affects the DMM only when you set the\nNIDMM_ATTR_FUNCTION attribute to AC measurements. NI-DMM uses this\nparameter to calculate the proper aperture for the measurement.\nThe driver sets the NIDMM_ATTR_AC_MIN_FREQ attribute to this value.\nThe valid range is 1 Hz–300 kHz for the NI 4080/4081/4082 and the NI\n4070/4071/4072, 10 Hz–100 Hz for the NI 4065, and 20 Hz–25 kHz for the\nNI 4050 and NI 4060.\n'
                },
                'name': 'acMinimumFrequencyHz',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the maximum expected frequency component of the input signal\nin hertz within the device limits. This parameter is used only for error\nchecking and verifies that the value of this parameter is less than the\nmaximum frequency of the device.\n\nThis parameter affects the DMM only when you set the\nNIDMM_ATTR_FUNCTION attribute to AC measurements. The driver sets the\nNIDMM_ATTR_AC_MAX_FREQ attribute to this value. The valid range is 1\nHz–300 kHz for the NI 4080/4081/4082 and the NI 4070/4071/4072, 10\nHz–100 Hz for the NI 4065, and 20 Hz–25 kHz for the NI 4050 and NI 4060.\n'
                },
                'name': 'acMaximumFrequencyHz',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureAutoZeroMode': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the DMM for **Auto_Zero_Mode**. When **Auto_Zero_Mode**\nis ON, the DMM internally disconnects the input signal and takes a zero\nreading. It then subtracts the zero reading from the measurement. This\nprevents offset voltages present on the input circuitry of the DMM from\naffecting measurement accuracy. When **Auto_Zero_Mode** is OFF, the\nDMM does not compensate for zero reading offset.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **auto_zero_mode**. NI-DMM sets the\nNIDMM_ATTR_AUTO_ZERO attribute to this value.\n\nON enables **auto_zero_mode** for each measurement. ONCE enables\n**auto_zero_mode** before the next measurement. The\n**auto_zero_mode** value is stored and used in subsequent measurements\nuntil the device is reconfigured.\n\nOFF disables **auto_zero_mode**. If you set this parameter to AUTO,\nNI-DMM determines whether to enable Auto Zero based on the measurement\nfunction that you configure. If you configure the NI 4080/4081/4082 or\nthe NI 4070/4071/4072 for a 6½–digit and greater resolution DC\nmeasurement, NI-DMM sets **auto_zero_mode** to ON.\n\nFor all other DC measurement configurations on the NI 4080/4081/4082 or\nthe NI 4070/4071/4072, NI-DMM sets **auto_zero_mode** to ONCE. For all\nAC measurements or waveform acquisitions on the NI 4080/4081/4082 or the\nNI 4070/4071/4072, NI-DMM sets **auto_zero_mode** to OFF. For NI 4060,\n**auto_zero_mode** is set to OFF when AUTO is selected.\n\nFor NI 4065 devices, **auto_zero_mode** is always ON.\n**auto_zero_mode** is an integral part of the signal measurement phase\nand adds no extra time to the overall measurement.\n',
                    'note': 'The NI 4060/4065 does *not* support this setting.',
                    'table_body': [
                        [
                            'NIDMM_VAL_AUTO_ZERO_AUTO (default)',
                            '-1',
                            'NI-DMM chooses the Auto Zero setting based on the configured function and resolution.'
                        ],
                        [
                            'NIDMM_VAL_AUTO_ZERO_OFF',
                            '0',
                            'Disables Auto Zero.'
                        ],
                        [
                            'NIDMM_VAL_AUTO_ZERO_ON',
                            '1',
                            'The DMM internally disconnects the input signal following each measurement and takes a zero reading. It then subtracts the zero reading from the preceding reading.'
                        ],
                        [
                            'NIDMM_VAL_AUTO_ZERO_ONCE',
                            '2',
                            'The DMM internally disconnects the input signal following the first measurement and takes a zero reading. It then subtracts the zero reading from the preceding reading and each measurement that follows.'
                        ]
                    ]
                },
                'name': 'autoZeroMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureCableCompType': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nFor the NI 4082 and NI 4072 only, sets the\nNIDMM_ATTR_CABLE_COMP_TYPE attribute for the current\ncapacitance/inductance mode range.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of cable compensation that is used for the current\nrange.\n'
                },
                'name': 'cableCompType',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureCurrentSource': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThe NI 4050 and NI 4060 are not supported. Configures the\n**Current_Source** for diode measurements.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **current_source** provided during diode measurements.\nFor valid ranges, refer to the device sections for your device. The\ndriver sets NIDMM_ATTR_CURRENT_SOURCE to this value.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_1_MICROAMP',
                            '1 µA',
                            'NI 4080/4081/4082 and NI 4070/4071/4072'
                        ],
                        [
                            'NIDMM_VAL_10_MICROAMP',
                            '10 µA',
                            'NI 4080/4081/4082 and NI 4070/4071/4072 only'
                        ],
                        [
                            'NIDMM_VAL_100_MICROAMP',
                            '100 µA',
                            'NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065'
                        ],
                        [
                            'NIDMM_VAL_1_MILLIAMP (default)',
                            '1 mA',
                            'NI 4080/4081/4082, NI 4070/4071/4072, and NI 4065'
                        ]
                    ]
                },
                'name': 'currentSource',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeSampleTrigger': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'trigSource',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeStartTrigger': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'trigSource',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'triggerDelay',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureFixedRefJunction': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the fixed reference junction temperature for a thermocouple\nwith a fixed reference junction type.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the reference junction temperature when a fixed reference\njunction is used to take a thermocouple measurement. The units are\ndegrees Celsius. NI-DMM uses this value to set the Fixed Reference\nJunction property. The default is 25.00 (°C).\n'
                },
                'name': 'fixedReferenceJunction',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureFrequencyVoltageRange': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nFor the NI 4080/4081/4082 and the NI 4070/4071/4072 only, specifies the\nexpected maximum amplitude of the input signal for frequency and period\nmeasurements.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSets the expected maximum amplitude of the input signal. Refer to the\n`NI 4080 <REPLACE_DRIVER_SPECIFIC_URL_1(4080_functional_overview)>`__,\n`NI 4081 <REPLACE_DRIVER_SPECIFIC_URL_1(4081_functional_overview)>`__,\n`NI 4072 <REPLACE_DRIVER_SPECIFIC_URL_1(4082)>`__,\n`NI 4070 <REPLACE_DRIVER_SPECIFIC_URL_1(4070_functional_overview)>`__,\n`NI 4071 <REPLACE_DRIVER_SPECIFIC_URL_1(4071_functional_overview)>`__,\nand `NI 4072 <REPLACE_DRIVER_SPECIFIC_URL_1(4072)>`__ sections for a\nlist of valid values. NI-DMM sets NIDMM_ATTR_FREQ_VOLTAGE_RANGE to\nthis value. The minimum peak-to-peak signal amplitude that can be\ndetected is 10% of the specified **voltage_range**.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_AUTO_RANGE_ON (default)',
                            '-1.0',
                            'Configures the DMM to take an Auto Range measurement to calculate the voltage range before each frequency or period measurement.'
                        ],
                        [
                            'NIDMM_VAL_AUTO_RANGE_OFF',
                            '-2.0',
                            'Disables Auto Ranging. The driver sets the voltage range to the last calculated voltage range.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'name': 'voltageRange',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureIntervalSampleTrigger': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'sampleInterval',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMeasCompleteDest': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the destination of the DMM Measurement Complete (MC) signal.\nRefer to `Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__ for\nmore information.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the destination of the Measurement Complete signal. This\nsignal is issued when the DMM completes a single measurement. The driver\nsets the NIDMM_ATTR_MEAS_COMPLETE_DEST attribute to this value. This\nsignal is commonly referred to as Voltmeter Complete.\n',
                    'note': '\nTo determine which values are supported by each device, refer to the\n`LabWindows/CVI Trigger\nRouting <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.\n'
                },
                'name': 'measCompleteDestination',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMeasCompleteSlope': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the Measurement Complete signal to either rising edge (positive) or\nfalling edge (negative) polarity.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the polarity of the signal that is generated. The driver sets\nNIDMM_ATTR_MEAS_DEST_SLOPE to this value.\n',
                    'table_body': [
                        [
                            'Rising Edge',
                            '0',
                            'NIDMM_VAL_POSITIVE',
                            'The driver triggers on the rising edge of the trigger signal.'
                        ],
                        [
                            'Falling Edge (default)',
                            '1',
                            'NIDMM_VAL_NEGATIVE',
                            'The driver triggers on the falling edge of the trigger signal.'
                        ]
                    ]
                },
                'name': 'measCompleteSlope',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMeasurement': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'measFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'resolution',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMeasurementAbsolute': {
        'documentation': {
            'description': '\nConfigures the common attributes of the measurement. These attributes\ninclude NIDMM_ATTR_FUNCTION, NIDMM_ATTR_RANGE, and\nNIDMM_ATTR_RESOLUTION_ABSOLUTE.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **measurement_function** used to acquire the measurement.\nThe driver sets NIDMM_ATTR_FUNCTION to this value.\n'
                },
                'enum': 'Function',
                'name': 'measurementFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **range** for the function specified in the\n**Measurement_Function** parameter. When frequency is specified in the\n**Measurement_Function** parameter, you must supply the minimum\nfrequency expected in the **range** parameter. For example, you must\ntype in 100 Hz if you are measuring 101 Hz or higher.\nFor all other functions, you must supply a **range** that exceeds the\nvalue that you are measuring. For example, you must type in 10 V if you\nare measuring 9 V. **range** values are coerced up to the closest input\n**range**. Refer to the `Devices\nOverview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a list of valid\nranges. The driver sets NIDMM_ATTR_RANGE to this value. The default is\n0.02 V.\n',
                    'note': '\nThe NI 4050, NI 4060, and NI 4065 only support Auto Range when the\ntrigger and sample trigger are set to IMMEDIATE.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_AUTO_RANGE_ON',
                            '-1.0',
                            'NI-DMM performs an Auto Range before acquiring the measurement.'
                        ],
                        [
                            'NIDMM_VAL_AUTO_RANGE_OFF',
                            '-2.0',
                            'NI-DMM sets the Range to the current NIDMM_ATTR_AUTO_RANGE_VALUE and uses this range for all subsequent measurements until the measurement configuration is changed.'
                        ],
                        [
                            'NIDMM_VAL_AUTO_RANGE_ONCE',
                            '-3.0',
                            'NI-DMM performs an Auto Range before acquiring the measurement. The NIDMM_ATTR_AUTO_RANGE_VALUE is stored and used for all subsequent measurements until the measurement configuration is changed.'
                        ]
                    ]
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute resolution for the measurement. NI-DMM sets\nNIDMM_ATTR_RESOLUTION_ABSOLUTE to this value. The PXIe-4080/4081/4082\nuses the resolution you specify. The NI 4065 and NI 4070/4071/4072\nignore this parameter when the **Range** parameter is set to\nNIDMM_VAL_AUTO_RANGE_ON (-1.0) or NIDMM_VAL_AUTO_RANGE_ONCE\n(-3.0). The default is 0.001 V.\n',
                    'note': '\nNI-DMM ignores this parameter for capacitance and inductance\nmeasurements on the NI 4072. To achieve better resolution for such\nmeasurements, use the NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE\nattribute.\n'
                },
                'name': 'resolutionAbsolute',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMeasurementComplete': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'destination',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'slope',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMeasurementDigits': {
        'documentation': {
            'description': '\nConfigures the common attributes of the measurement. These attributes\ninclude NIDMM_ATTR_FUNCTION, NIDMM_ATTR_RANGE, and\nNIDMM_ATTR_RESOLUTION_DIGITS.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **measurement_function** used to acquire the measurement.\nThe driver sets NIDMM_ATTR_FUNCTION to this value.\n'
                },
                'enum': 'Function',
                'name': 'measurementFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the range for the function specified in the\n**Measurement_Function** parameter. When frequency is specified in the\n**Measurement_Function** parameter, you must supply the minimum\nfrequency expected in the **range** parameter. For example, you must\ntype in 100 Hz if you are measuring 101 Hz or higher.\nFor all other functions, you must supply a range that exceeds the value\nthat you are measuring. For example, you must type in 10 V if you are\nmeasuring 9 V. range values are coerced up to the closest input range.\nRefer to the `Devices\nOverview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a list of valid\nranges. The driver sets NIDMM_ATTR_RANGE to this value. The default is\n0.02 V.\n',
                    'note': '\nThe NI 4050, NI 4060, and NI 4065 only support Auto Range when the\ntrigger and sample trigger are set to IMMEDIATE.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_AUTO_RANGE_ON',
                            '-1.0',
                            'NI-DMM performs an Auto Range before acquiring the measurement.'
                        ],
                        [
                            'NIDMM_VAL_AUTO_RANGE_OFF',
                            '-2.0',
                            'NI-DMM sets the Range to the current NIDMM_ATTR_AUTO_RANGE_VALUE and uses this range for all subsequent measurements until the measurement configuration is changed.'
                        ],
                        [
                            'NIDMM_VAL_AUTO_RANGE_ONCE',
                            '-3.0',
                            'NI-DMM performs an Auto Range before acquiring the measurement. The NIDMM_ATTR_AUTO_RANGE_VALUE is stored and used for all subsequent measurements until the measurement configuration is changed.'
                        ]
                    ]
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the resolution of the measurement in digits. The driver sets\nthe `Devices Overview <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__ for a\nlist of valid ranges. The driver sets NIDMM_ATTR_RESOLUTION_DIGITS\nattribute to this value. The PXIe-4080/4081/4082 uses the resolution you\nspecify. The NI 4065 and NI 4070/4071/4072 ignore this parameter when\nthe **Range** parameter is set to NIDMM_VAL_AUTO_RANGE_ON (-1.0) or\nNIDMM_VAL_AUTO_RANGE_ONCE (-3.0). The default is 5½.\n',
                    'note': '\nNI-DMM ignores this parameter for capacitance and inductance\nmeasurements on the NI 4072. To achieve better resolution for such\nmeasurements, use the NIDMM_ATTR_LC_NUMBER_MEAS_TO_AVERAGE\nattribute.\n'
                },
                'name': 'resolutionDigits',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMultiPoint': {
        'documentation': {
            'description': '\nConfigures the attributes for multipoint measurements. These attributes\ninclude NIDMM_ATTR_TRIGGER_COUNT, NIDMM_ATTR_SAMPLE_COUNT,\nNIDMM_ATTR_SAMPLE_TRIGGER, and NIDMM_ATTR_SAMPLE_INTERVAL.\n\nFor continuous acquisitions, set NIDMM_ATTR_TRIGGER_COUNT or\nNIDMM_ATTR_SAMPLE_COUNT to zero. For more information, refer to\n`Multiple Point\nAcquisitions <REPLACE_DRIVER_SPECIFIC_URL_1(multi_point)>`__,\n`Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__, and `Using\nSwitches <REPLACE_DRIVER_SPECIFIC_URL_1(switch_selection)>`__.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSets the number of triggers you want the DMM to receive before returning\nto the Idle state. The driver sets NIDMM_ATTR_TRIGGER_COUNT to this\nvalue. The default value is 1.\n'
                },
                'name': 'triggerCount',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSets the number of measurements the DMM makes in each measurement\nsequence initiated by a trigger. The driver sets\nNIDMM_ATTR_SAMPLE_COUNT to this value. The default value is 1.\n'
                },
                'name': 'sampleCount',
                'type': 'ViInt32'
            },
            {
                'default_value': 'SampleTrigger.IMMEDIATE',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **sample_trigger** source you want to use. The driver\nsets NIDMM_ATTR_SAMPLE_TRIGGER to this value. The default is\nImmediate.\n',
                    'note': '\nTo determine which values are supported by each device, refer to the\n`LabWindows/CVI Trigger\nRouting <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.\n'
                },
                'enum': 'SampleTrigger',
                'name': 'sampleTrigger',
                'type': 'ViInt32'
            },
            {
                'default_value': 'datetime.timedelta(seconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSets the amount of time in seconds the DMM waits between measurement\ncycles. The driver sets NIDMM_ATTR_SAMPLE_INTERVAL to this value.\nSpecify a sample interval to add settling time between measurement\ncycles or to decrease the measurement rate. **sample_interval** only\napplies when the **Sample_Trigger** is set to INTERVAL.\n\nOn the NI 4060, the **sample_interval** value is used as the settling\ntime. When sample interval is set to 0, the DMM does not settle between\nmeasurement cycles. The NI 4065 and NI 4070/4071/4072 use the value\nspecified in **sample_interval** as additional delay. The default value\n(-1) ensures that the DMM settles for a recommended time. This is the\nsame as using an Immediate trigger.\n',
                    'note': 'This attribute is not used on the NI 4080/4081/4082 and the NI 4050.'
                },
                'name': 'sampleInterval',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureMultiPointAcquisition': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'triggerCount',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'sampleCount',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOffsetCompOhms': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nFor NI 4080/4081/4082 and NI 4070/4071/4072, allows the DMM to\ncompensate for voltage offsets in resistance measurements. When\n**Offset_Comp_Ohms** is enabled, the DMM measures the resistance twice\n(once with the current source on and again with it turned off). Any\nvoltage offset present in both measurements is cancelled out.\n**Offset_Comp_Ohms** is useful when measuring resistance values less\nthan 10 KΩ.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nEnables or disables **offset_comp_ohms**. The driver sets\nNIDMM_ATTR_OFFSET_COMP_OHMS to this value.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_OFFSET_COMP_OHMS_OFF (default)',
                            '0',
                            'Off disables **Offset_Comp_Ohms**.'
                        ],
                        [
                            'NIDMM_VAL_OFFSET_COMP_OHMS_ON',
                            '1',
                            'On enables **Offset_Comp_Ohms**.'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'name': 'offsetCompOhms',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOpenCableCompValues': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nFor the NI 4082 and NI 4072 only, configures the\nNIDMM_ATTR_OPEN_CABLE_COMP_CONDUCTANCE and\nNIDMM_ATTR_OPEN_CABLE_COMP_SUSCEPTANCE attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the open cable compensation **conductance**.'
                },
                'name': 'conductance',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the open cable compensation **susceptance**.'
                },
                'name': 'susceptance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePowerLineFrequency': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Specifies the powerline frequency.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\n**Powerline Frequency** specifies the powerline frequency in hertz.\nNI-DMM sets the Powerline Frequency property to this value.\n'
                },
                'name': 'powerLineFrequencyHz',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureRTDCustom': {
        'documentation': {
            'description': 'Configures the A, B, and C parameters for a custom RTD.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Callendar-Van Dusen A coefficient for RTD scaling when RTD\nType parameter is set to Custom in the niDMM_ConfigureRTDType function.\nThe default is 3.9083e-3 (Pt3851)\n'
                },
                'name': 'rtdA',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Callendar-Van Dusen B coefficient for RTD scaling when RTD\nType parameter is set to Custom in the niDMM_ConfigureRTDType function.\nThe default is -5.775e-7 (Pt3851).\n'
                },
                'name': 'rtdB',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Callendar-Van Dusen C coefficient for RTD scaling when RTD\nType parameter is set to Custom in the niDMM_ConfigureRTDType function.\nThe default is -4.183e-12 (Pt3851).\n'
                },
                'name': 'rtdC',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureRTDType': {
        'documentation': {
            'description': 'Configures the RTD Type and RTD Resistance parameters for an RTD.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of RTD used to measure the temperature resistance.\nNI-DMM uses this value to set the RTD Type property. The default is\nNIDMM_VAL_TEMP_RTD_PT3851.\n',
                    'table_body': [
                        [
                            'Callendar-Van Dusen Coefficient'
                        ],
                        [
                            'NIDMM_VAL_TEMP_RTD_PT3851',
                            'IEC-751 DIN 43760 BS 1904 ASTM-E1137 EN-60751',
                            'Platinum',
                            '.003851',
                            '100 Ω 1000 Ω',
                            'A = 3.9083 × 10\\ :sup:`–3` B = –5.775×10:sup:`–7` C = –4.183×10:sup:`–12`',
                            'Most common RTDs'
                        ],
                        [
                            'NIDMM_VAL_TEMP_RTD_PT3750',
                            'Low-cost vendor compliant RTD\\*',
                            'Platinum',
                            '.003750',
                            '1000 Ω',
                            'A = 3.81 × 10\\ :sup:`–3` B = –6.02×10:sup:`–7` C = –6.0×10:sup:`–12`',
                            'Low-cost RTD'
                        ],
                        [
                            'NIDMM_VAL_TEMP_RTD_PT3916',
                            'JISC 1604',
                            'Platinum',
                            '.003916',
                            '100 Ω',
                            'A = 3.9739 × 10\\ :sup:`–3` B = –5.870×10:sup:`–7` C = –4.4 ×10\\ :sup:`–12`',
                            'Used in primarily in Japan'
                        ],
                        [
                            'NIDMM_VAL_TEMP_RTD_PT3920',
                            'US Industrial Standard D-100 American',
                            'Platinum',
                            '.003920',
                            '100 Ω',
                            'A = 3.9787 × 10\\ :sup:`–3` B = –5.8686×10:sup:`–7` C = –4.167 ×10\\ :sup:`–12`',
                            'Low-cost RTD'
                        ],
                        [
                            'NIDMM_VAL_TEMP_RTD_PT3911',
                            'US Industrial Standard American',
                            'Platinum',
                            '.003911',
                            '100 Ω',
                            'A = 3.9692 × 10\\ :sup:`–3` B = –5.8495×10:sup:`–7` C = –4.233 ×10\\ :sup:`–12`',
                            'Low-cost RTD'
                        ],
                        [
                            'NIDMM_VAL_TEMP_RTD_PT3928',
                            'ITS-90',
                            'Platinum',
                            '.003928',
                            '100 Ω',
                            'A = 3.9888 × 10\\ :sup:`–3` B = –5.915×10:sup:`–7` C = –3.85 ×10\\ :sup:`–12`',
                            'The definition of temperature'
                        ],
                        [
                            '\\*No standard. Check the TCR.'
                        ]
                    ],
                    'table_header': [
                        'Enum',
                        'Standards',
                        'Material',
                        'TCR (α)',
                        'Typical R\\ :sub:`0` (Ω)',
                        'Notes'
                    ]
                },
                'enum': 'RTDType',
                'name': 'rtdType',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the RTD resistance in ohms at 0 °C. NI-DMM uses this value to\nset the RTD Resistance property. The default is 100 (Ω).\n'
                },
                'name': 'rtdResistance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSampleDelayMode': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'sampleDelayMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSampleTriggerSlope': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the NIDMM_ATTR_SAMPLE_TRIGGER_SLOPE to either rising edge\n(positive) or falling edge (negative) polarity.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the polarity of the Trigger signal on which the measurement is\ntriggered for values of either NIDMM_VAL_POSITIVE or\nNIDMM_VAL_NEGATIVE. The driver sets\nNIDMM_ATTR_SAMPLE_TRIGGER_SLOPE to this value.\n',
                    'table_body': [
                        [
                            'Rising Edge',
                            '0',
                            'NIDMM_VAL_POSITIVE',
                            'The driver triggers on the rising edge of the trigger signal.'
                        ],
                        [
                            'Falling Edge (default)',
                            '1',
                            'NIDMM_VAL_NEGATIVE',
                            'The driver triggers on the falling edge of the trigger signal.'
                        ]
                    ]
                },
                'name': 'sampleTriggerSlope',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureShortCableCompValues': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nFor the NI 4082 and NI 4072 only, configures the\nNIDMM_ATTR_SHORT_CABLE_COMP_RESISTANCE and\nNIDMM_ATTR_SHORT_CABLE_COMP_REACTANCE attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the short cable compensation **resistance**.'
                },
                'name': 'resistance',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the short cable compensation **reactance**.'
                },
                'name': 'reactance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareSampleTrigger': {
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
    'ConfigureSoftwareStartTrigger': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'triggerDelay',
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
                'name': 'source',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'slope',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureThermistorCustom': {
        'documentation': {
            'description': 'Configures the A, B, and C parameters for a custom thermistor.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Steinhart-Hart A coefficient for thermistor scaling when\nThermistor Type is set to Custom in the niDMM_ConfigureThermistorType\nfunction. The default is 1.0295e-3 (44006).\n'
                },
                'name': 'thermistorA',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Steinhart-Hart B coefficient for thermistor scaling when\nThermistor Type is set to Custom in the niDMM_ConfigureThermistorType\nfunction. The default is 2.391e-4 (44006).\n'
                },
                'name': 'thermistorB',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the Steinhart-Hart C coefficient for thermistor scaling when\nThermistor Type is set to Custom in the niDMM_ConfigureThermistorType\nfunction. The default is 1.568e-7 (44006).\n'
                },
                'name': 'thermistorC',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureThermistorType': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Configures the thermistor type.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of thermistor used to measure the temperature. NI-DMM\nuses this value to set the Thermistor Type property. The default is\nNIDMM_VAL_TEMP_THERMISTOR_44006.\n\n+--------------------+--------------------+--------------------+--------------------+\n| **Defined Values** | **Thermistor       | **Value**          | **25 °C            |\n|                    | Type**             |                    | Resistance**       |\n+--------------------+--------------------+--------------------+--------------------+\n| NIDMM_VAL_TEMP_ | Custom             | 0                  | —                  |\n| THERMISTOR_CUSTOM |                    |                    |                    |\n+--------------------+--------------------+--------------------+--------------------+\n| NIDMM_VAL_TEMP_ | 44004              | 1                  | 2.25 kΩ            |\n| THERMISTOR_44004  |                    |                    |                    |\n+--------------------+--------------------+--------------------+--------------------+\n| NIDMM_VAL_TEMP_ | 44006              | 2                  | 10 kΩ              |\n| THERMISTOR_44006  |                    |                    |                    |\n+--------------------+--------------------+--------------------+--------------------+\n| NIDMM_VAL_TEMP_ | 44007              | 3                  | 5 kΩ               |\n| THERMISTOR_44007  |                    |                    |                    |\n+--------------------+--------------------+--------------------+--------------------+\n'
                },
                'name': 'thermistorType',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureThermocouple': {
        'documentation': {
            'description': '\nConfigures the thermocouple type and reference junction type for a\nchosen thermocouple.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of thermocouple used to measure the temperature.\nNI-DMM uses this value to set the Thermocouple Type property. The\ndefault is NIDMM_VAL_TEMP_TC_J.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_TEMP_TC_B',
                            'Thermocouple type B'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_E',
                            'Thermocouple type E'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_J',
                            'Thermocouple type J'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_K',
                            'Thermocouple type K'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_N',
                            'Thermocouple type N'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_R',
                            'Thermocouple type R'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_S',
                            'Thermocouple type S'
                        ],
                        [
                            'NIDMM_VAL_TEMP_TC_T',
                            'Thermocouple type T'
                        ]
                    ]
                },
                'enum': 'ThermocoupleType',
                'name': 'thermocoupleType',
                'type': 'ViInt32'
            },
            {
                'default_value': 'ThermocoupleReferenceJunctionType.FIXED',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of reference junction to be used in the reference\njunction compensation of a thermocouple measurement. NI-DMM uses this\nvalue to set the Reference Junction Type property. The only supported\nvalue is NIDMM_VAL_TEMP_REF_JUNC_FIXED.\n'
                },
                'enum': 'ThermocoupleReferenceJunctionType',
                'name': 'referenceJunctionType',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTransducerType': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Configures the transducer type.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of device used to measure the temperature. NI-DMM\nuses this value to set the Transducer Type property. The default is\nNIDMM_VAL_THERMOCOUPLE.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_2_WIRE_RTD',
                            '2-wire RTD'
                        ],
                        [
                            'NIDMM_VAL_4_WIRE_RTD',
                            '4-wire RTD'
                        ],
                        [
                            'NIDMM_VAL_THERMISTOR',
                            'Thermistor'
                        ],
                        [
                            'NIDMM_VAL_THERMOCOUPLE',
                            'Thermocouple'
                        ]
                    ]
                },
                'name': 'transducerType',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTrigger': {
        'documentation': {
            'description': '\nConfigures the DMM **Trigger_Source** and **Trigger_Delay**. Refer to\n`Triggering <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__ and `Using\nSwitches <REPLACE_DRIVER_SPECIFIC_URL_1(switch_selection)>`__ for more\ninformation.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **trigger_source** that initiates the acquisition. The\ndriver sets NIDMM_ATTR_TRIGGER_SOURCE to this value. Software\nconfigures the DMM to wait until niDMM_SendSoftwareTrigger is called\nbefore triggering the DMM.\n',
                    'note': '\nTo determine which values are supported by each device, refer to the\n`LabWindows/CVI Trigger\nRouting <REPLACE_DRIVER_SPECIFIC_URL_1(cvitrigger_routing)>`__ section.\n'
                },
                'enum': 'TriggerSource',
                'name': 'triggerSource',
                'type': 'ViInt32'
            },
            {
                'default_value': 'datetime.timedelta(seconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the time that the DMM waits after it has received a trigger\nbefore taking a measurement. The driver sets the\nNIDMM_ATTR_TRIGGER_DELAY attribute to this value. By default,\n**trigger_delay** is NIDMM_VAL_AUTO_DELAY (-1), which means the DMM\nwaits an appropriate settling time before taking the measurement. On the\nNI 4060, if you set **trigger_delay** to 0, the DMM does not settle\nbefore taking the measurement. The NI 4065 and NI 4070/4071/4072 use the\nvalue specified in **trigger_delay** as additional settling time.\n',
                    'note': '\nWhen using the NI 4050, **Trigger_Delay** must be set to\nNIDMM_VAL_AUTO_DELAY (-1).\n'
                },
                'name': 'triggerDelay',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureTriggerSlope': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSets the NIDMM_ATTR_TRIGGER_SLOPE attribute to either rising edge\n(positive) or falling edge (negative) polarity.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the polarity of the trigger signal on which the measurement is\ntriggered for values of either NIDMM_VAL_POSITIVE or\nNIDMM_VAL_NEGATIVE. The driver sets the NIDMM_ATTR_TRIGGER_SLOPE\nattribute to this value.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_POSITIVE',
                            '0',
                            'The driver triggers on the rising edge of the trigger signal.'
                        ],
                        [
                            'NIDMM_VAL_NEGATIVE (default)',
                            '1',
                            'The driver triggers on the falling edge of the trigger signal.'
                        ]
                    ]
                },
                'name': 'triggerSlope',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureWaveformAcquisition': {
        'documentation': {
            'description': '\nConfigures the DMM for waveform acquisitions. This feature is supported\non the NI 4080/4081/4082 and the NI 4070/4071/4072.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **measurement_function** used in a waveform acquisition.\nThe driver sets NIDMM_ATTR_FUNCTION to this value.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_WAVEFORM_VOLTAGE (default)',
                            '1003',
                            'Voltage Waveform'
                        ],
                        [
                            'NIDMM_VAL_WAVEFORM_CURRENT',
                            '1004',
                            'Current Waveform'
                        ]
                    ]
                },
                'enum': 'Function',
                'name': 'measurementFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the expected maximum amplitude of the input signal and sets\nthe **range** for the **Measurement_Function**. NI-DMM sets\nNIDMM_ATTR_RANGE to this value. **range** values are coerced up to the\nclosest input **range**. The default is 10.0.\n\nFor valid ranges refer to the topics in\n`Devices <REPLACE_DRIVER_SPECIFIC_URL_1(devices)>`__.\n\nAuto-ranging is not supported during waveform acquisitions.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **rate** of the acquisition in samples per second. NI-DMM\nsets NIDMM_ATTR_WAVEFORM_RATE to this value.\n\nThe valid **Range** is 10.0–1,800,000 S/s. **rate** values are coerced\nto the closest integer divisor of 1,800,000. The default value is\n1,800,000.\n'
                },
                'name': 'rate',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of points to acquire before the waveform\nacquisition completes. NI-DMM sets NIDMM_ATTR_WAVEFORM_POINTS to this\nvalue.\n\nTo calculate the maximum and minimum number of waveform points that you\ncan acquire in one acquisition, refer to the `Waveform Acquisition\nMeasurement Cycle <REPLACE_DRIVER_SPECIFIC_URL_1(waveform_cycle)>`__.\n\nThe default value is 500.\n'
                },
                'name': 'waveformPoints',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureWaveformCoupling': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nFor the NI 4080/4081/4082 and the NI 4070/4071/4072, configures\ninstrument coupling for voltage waveforms.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSelects DC or AC coupling. The driver sets\nNIDMM_ATTR_WAVEFORM_COUPLING to this value.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_WAVEFORM_COUPLING_AC',
                            '0',
                            'AC coupling'
                        ],
                        [
                            'NIDMM_VAL_WAVEFORM_COUPLING_DC (default)',
                            '1',
                            'DC coupling'
                        ]
                    ],
                    'table_header': [
                        'Name',
                        'Value',
                        'Description'
                    ]
                },
                'name': 'waveformCoupling',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'Control': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nControls the DMM. Use this function if you want a parameter change to be\nimmediately reflected in the hardware. Use this function before calling\nnidMM_Initiate to make the initiate call as quickly as possible.\n',
            'note': '\nThe NI 4050 and NI 4060 are not supported.\nCalling this function while the DMM is taking measurements results in an\nerror. After the DMM is finished taking measurements, calling this\nfunction will make any unfetched data points unavailable.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe action you want the driver to perform. Only\nNIDMM_VAL_CONTROL_COMMIT (0) is supported, which commits to hardware\nall of the configured attributes associated with the session.\n'
                },
                'name': 'controlAction',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConvertAbsToDigits': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'resolution',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'newResolution',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'Disable': {
        'documentation': {
            'description': '\nPlaces the instrument in a quiescent state where it has minimal or no\nimpact on the system to which it is connected. If a measurement is in\nprogress when this function is called, the measurement is aborted.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableSampleTrigger': {
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
    'DisableStartTrigger': {
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
    'DoCompMeasurement': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'modes',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'calcModel',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'real',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'imaginary',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationBuffer': {
        'documentation': {
            'description': '\nExports the attribute configuration of the session to the specified\nconfiguration buffer.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers.\n\nThis function verifies that the attributes you have configured for the\nsession are valid. If the configuration is invalid, NI‑DMM returns an\nerror.\n\n**Coercion Behavior for Certain Devices**\n\nImported and exported attribute configurations contain coerced values\nfor the following NI‑DMM devices:\n\n-  PXI/PCI/PCIe/USB‑4065\n-  PXI/PCI‑4070\n-  PXI‑4071\n-  PXI‑4072\n\nNI‑DMM coerces attribute values when the value you set is within the\nallowed range for the attribute but is not one of the discrete valid\nvalues the attribute supports. For example, for an attribute that\ncoerces values up, if you choose a value of 4 when the adjacent valid\nvalues are 1 and 10, the attribute coerces the value to 10.\n\n**Related Topics:**\n\n`Using Attributes and Properties with\nNI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(attributes)>`__\n\n`Setting Attributes Before Reading\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': 'Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size, in bytes, of the byte array to export. If you enter\n0, this function returns the needed size.\n'
                },
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSpecifies the byte array buffer to be populated with the exported\nattribute configuration.\n'
                },
                'name': 'configuration',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationFile': {
        'documentation': {
            'description': '\nExports the attribute configuration of the session to the specified\nfile.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers.\n\nThis function verifies that the attributes you have configured for the\nsession are valid. If the configuration is invalid, NI‑DMM returns an\nerror.\n\n**Coercion Behavior for Certain Devices**\n\nImported and exported attribute configurations contain coerced values\nfor the following NI‑DMM devices:\n\n-  PXI/PCI/PCIe/USB‑4065\n-  PXI/PCI‑4070\n-  PXI‑4071\n-  PXI‑4072\n\nNI‑DMM coerces attribute values when the value you set is within the\nallowed range for the attribute but is not one of the discrete valid\nvalues the attribute supports. For example, for an attribute that\ncoerces values up, if you choose a value of 4 when the adjacent valid\nvalues are 1 and 10, the attribute coerces the value to 10.\n\n**Related Topics:**\n\n`Using Attributes and Properties with\nNI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(attributes)>`__\n\n`Setting Attributes Before Reading\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': 'Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute path to the file to contain the exported\nattribute configuration. If you specify an empty or relative path, this\nfunction returns an error.\n**Default file extension:**\\  .nidmmconfig\n'
                },
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportSignal': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'signal',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'destination',
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Fetch': {
        'documentation': {
            'description': '\nReturns the value from a previously initiated measurement. You must call\nniDMM_Initiate before calling this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'datetime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **maximum_time** allowed for this function to complete in\nmilliseconds. If the function does not complete within this time\ninterval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED\nerror code. This may happen if an external trigger has not been\nreceived, or if the specified timeout is not long enough for the\nacquisition to complete.\n\nThe valid range is 0–86400000. The default value is\nNIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout\nautomatically.\n'
                },
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                'type': 'ViInt32',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The measured value returned from the DMM.'
                },
                'name': 'reading',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchMultiPoint': {
        'documentation': {
            'description': '\nReturns an array of values from a previously initiated multipoint\nmeasurement. The number of measurements the DMM makes is determined by\nthe values you specify for the **Trigger_Count** and **Sample_Count**\nparameters of niDMM_ConfigureMultiPoint. You must first call\nniDMM_Initiate to initiate a measurement before calling this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'datetime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **maximum_time** allowed for this function to complete in\nmilliseconds. If the function does not complete within this time\ninterval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED\nerror code. This may happen if an external trigger has not been\nreceived, or if the specified timeout is not long enough for the\nacquisition to complete.\n\nThe valid range is 0–86400000. The default value is\nNIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout\nautomatically.\n'
                },
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                'type': 'ViInt32',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of measurements to acquire. The maximum number of\nmeasurements for a finite acquisition is the (**Trigger Count** x\n**Sample Count**) parameters in niDMM_ConfigureMultiPoint.\n\nFor continuous acquisitions, up to 100,000 points can be returned at\nonce. The number of measurements can be a subset. The valid range is any\npositive ViInt32. The default value is 1.\n'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An array of measurement values.',
                    'note': '\nThe size of the **Reading_Array** must be at least the size that you\nspecify for the **Array_Size** parameter.\n'
                },
                'name': 'readingArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the number of measured values actually retrieved from the DMM.'
                },
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'use_in_python_api': False
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchMultiPointWithCaching': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'maxTime',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'readingArray',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'actualPts',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'isMonitoring',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'FetchWaveform': {
        'documentation': {
            'description': '\nFor the NI 4080/4081/4082 and the NI 4070/4071/4072, returns an array of\nvalues from a previously initiated waveform acquisition. You must call\nniDMM_Initiate before calling this function.\n'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'default_method'
            },
            {
                'documentation_filename': 'numpy_method',
                'method_python_name_suffix': '_into',
                'session_filename': 'numpy_read_method'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'datetime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **maximum_time** allowed for this function to complete in\nmilliseconds. If the function does not complete within this time\ninterval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED\nerror code. This may happen if an external trigger has not been\nreceived, or if the specified timeout is not long enough for the\nacquisition to complete.\n\nThe valid range is 0–86400000. The default value is\nNIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout\nautomatically.\n'
                },
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                'type': 'ViInt32',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of waveform points to return. You specify the total\nnumber of points that the DMM acquires in the **Waveform Points**\nparameter of niDMM_ConfigureWaveformAcquisition. The default value is\n1.\n'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\n**Waveform Array** is an array of measurement values stored in waveform\ndata type.\n'
                },
                'name': 'waveformArray',
                'numpy': True,
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the number of measured values actually retrieved from the DMM.'
                },
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'use_in_python_api': False
            }
        ],
        'returns': 'ViStatus'
    },
    'FormatMeas': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'function',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'resolution',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'reading',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'modeString',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'name': 'rangeString',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'name': 'dataString',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'FormatMeasAbsolute': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nFormats the **Measurement** to the proper number of displayed digits\naccording to the **Measurement_Function**, **Range**, and\n**Resolution**. Returns the formatted data, range, and mode strings.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **measurement_function** used to acquire the measurement.\nThe driver sets NIDMM_ATTR_FUNCTION to this value.\n'
                },
                'name': 'measurementFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the NIDMM_ATTR_RANGE used to acquire the **Measurement**.'
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the NIDMM_ATTR_RESOLUTION_ABSOLUTE of the **Measurement**.'
                },
                'name': 'resolution',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the measured value returned from the DMM.'
                },
                'name': 'measurement',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns a string containing the units of the **Measurement** mode.'
                },
                'name': 'modeString',
                'type': 'ViChar[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the NIDMM_ATTR_RANGE of the **Measurement**, formatted into a\nstring with the correct number of display digits.\n'
                },
                'name': 'rangeString',
                'type': 'ViChar[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the **Measurement**, formatted according to the\nNIDMM_ATTR_FUNCTION, NIDMM_ATTR_RANGE, and\nNIDMM_ATTR_RESOLUTION_ABSOLUTE.\n'
                },
                'name': 'dataString',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'FormatMeasAbsoluteResolution': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'productId',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'function',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'resolution',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'reading',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'modeString',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'name': 'rangeString',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'name': 'dataString',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'FormatMeasDigitsResolution': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'productId',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'function',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'resolution',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'reading',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'name': 'modeString',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'name': 'rangeString',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'name': 'dataString',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString'
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
    'GetApertureTimeInfo': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Returns the DMM **Aperture_Time** and **Aperture_Time_Units**.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSpecifies the amount of time the DMM digitizes the input signal for a\nsingle measurement. This parameter does not include settling time.\nReturns the value of the NIDMM_ATTR_APERTURE_TIME attribute. The\nunits of this attribute depend on the value of the\nNIDMM_ATTR_APERTURE_TIME_UNITS attribute.\nOn the NI 4070/4071/4072, the minimum aperture time is 8.89 µs, and the\nmaximum aperture time is 149 s. Any number of powerline cycles (PLCs)\nwithin the minimum and maximum ranges is allowed on the\nNI 4070/4071/4072.\nOn the NI 4065 the minimum aperture time is 333 µs, and the maximum\naperture time is 78.2 s. If setting the number of averages directly, the\ntotal measurement time is aperture time X the number of averages, which\nmust be less than 72.8 s. The aperture times allowed are 333 µs, 667 µs,\nor multiples of 1.11 ms—for example 1.11 ms, 2.22 ms, 3.33 ms, and so\non. If you set an aperture time other than 333 µs, 667 µs, or multiples\nof 1.11 ms, the value will be coerced up to the next supported aperture\ntime.\nOn the NI 4060, when the powerline frequency is 60, the PLCs allowed are\n1 PLC, 6 PLC, 12 PLC, and 120 PLC. When the powerline frequency is 50,\nthe PLCs allowed are 1 PLC, 5 PLC, 10 PLC, and 100 PLC.\n'
                },
                'name': 'apertureTime',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nIndicates the units of aperture time as powerline cycles (PLCs) or\nseconds. Returns the value of the NIDMM_ATTR_APERTURE_TIME_UNITS\nattribute.\n',
                    'table_body': [
                        [
                            'NIDMM_VAL_SECONDS',
                            '0',
                            'Seconds'
                        ],
                        [
                            'NIDMM_VAL_POWER_LINE_CYCLES',
                            '1',
                            'Powerline Cycles'
                        ]
                    ]
                },
                'enum': 'ApertureTimeUnits',
                'name': 'apertureTimeUnits',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViBoolean attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. National Instruments DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
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
            'description': '\nQueries the value of a ViInt32 attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. National Instruments DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
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
    'GetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nQueries the value of a ViReal64 attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. National Instruments DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
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
            'description': '\nQueries the value of a ViSession attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. National Instruments DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
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
            'description': '\nQueries the value of a ViString attribute. You can use this function to\nget the values of instrument-specific attributes and inherent IVI\nattributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid.\n   You must provide a ViChar array to serve as a buffer for the value.\n   You pass the number of bytes in the buffer as the Array Size\n   parameter.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. National Instruments DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPass the number of bytes in the ViChar array you specify for the\n**Attribute_Value** parameter.\n\nIf the current value of the attribute, including the terminating NULL\nbyte, contains more bytes that you indicate in this parameter, the\nfunction copies **buffer_size**—1 bytes into the buffer, places an\nASCII NUL byte at the end of the buffer, and returns the buffer size you\nmust pass to get the entire value. For example, if the value is "123456"\nand the **buffer_size** is 4, the function places "123" into the buffer\nand returns 7.\n\nIf you pass a negative number, the function copies the value to the\nbuffer regardless of the number of bytes in the value. If you pass 0,\nyou can pass VI_NULL for the **Attribute_Value** buffer parameter.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe buffer in which the function returns the current value of the\nattribute. The buffer must be of type ViChar and have at least as many\nbytes as indicated in the **Buffer_Size** parameter.\n\nIf you specify 0 for the **Buffer_Size** parameter, you can pass\nVI_NULL for this parameter.\n'
                },
                'name': 'attributeValue',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
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
    'GetAutoRangeValue': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the **Actual_Range** that the DMM is using, even when Auto\nRange is off.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nIndicates the **actual_range** the DMM is using. Returns the value of\nthe NIDMM_ATTR_AUTO_RANGE_VALUE attribute. The units of the returned\nvalue depend on the function.\n'
                },
                'name': 'actualRange',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCalCount': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Returns the calibration **Count** for the specified type of calibration.',
            'note': 'The NI 4050, NI 4060, and NI 4080/4081/4082 are not supported.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of calibration performed (external or\nself-calibration).\n',
                    'note': 'The NI 4065 does not support self-calibration.',
                    'table_body': [
                        [
                            'NIDMM_VAL_INTERNAL_AREA (default)',
                            '0',
                            'Self-Calibration'
                        ],
                        [
                            'NIDMM_VAL_EXTERNAL_AREA',
                            '1',
                            'External Calibration'
                        ]
                    ]
                },
                'name': 'calType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The number of times calibration has been performed.'
                },
                'name': 'count',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCalDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the date and time of the last calibration performed.',
            'note': 'The NI 4050 and NI 4060 are not supported.'
        },
        'method_name_for_documentation': 'get_cal_date_and_time',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of calibration performed (external or\nself-calibration).\n',
                    'note': 'The NI 4065 does not support self-calibration.',
                    'table_body': [
                        [
                            'NIDMM_VAL_INTERNAL_AREA (default)',
                            '0',
                            'Self-Calibration'
                        ],
                        [
                            'NIDMM_VAL_EXTERNAL_AREA',
                            '1',
                            'External Calibration'
                        ]
                    ]
                },
                'name': 'calType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **month** of the last calibration.'
                },
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **day** of the last calibration.'
                },
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **year** of the last calibration.'
                },
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **hour** of the last calibration.'
                },
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the **minute** of the last calibration.'
                },
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCalUserDefinedInfo': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Returns the user-defined calibration information stored in the EEPROM.',
            'note': 'The NI 4050 and NI 4060 are not supported.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPasses the number of bytes in the ViString you specify for the **Info**\nparameter.\n\nIf zero is passed for this parameter, the **buffer_size** needed to\nstore the information is returned. If the Info parameter, including the\nterminating NULL byte, contains more bytes than you indicate in this\nparameter, the function copies **buffer_size** - 1 bytes into the\nbuffer, places an ASCII NULL byte at the end of the buffer, and returns\nthe **buffer_size** you must pass to get the entire value.\n\nFor example, if the value is "123456" and the **buffer_size** is 4, the\nfunction places "123" into the buffer and returns 7. If you pass a\nnegative number, the function copies the value to the buffer regardless\nof the number of bytes in the value.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the user-defined calibration information stored in the EEPROM.\nIf this is NULL, the **Buffer_Size** needed to store the information is\nreturned.\n'
                },
                'name': 'info',
                'size': {
                    'mechanism': 'fixed',
                    'value': 256
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCalUserDefinedInfoMaxSize': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the maximum string length that can be stored in the EEPROM. Use\nniDMM_SetCalUserDefinedInfo to store user-defined information.\n',
            'note': 'The NI 4050 and NI 4060 are not supported.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the value of maximum string length that can be stored in the\nEEPROM using niDMM_SetCalUserDefinedInfo. The **info_size** value is\ngiven in characters, but it does not include the termination character.\n'
                },
                'name': 'infoSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetChannelName': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the **Channel_String** that is in the channel table at an\n**Index** you specify. Not applicable to National Instruments DMMs.\nIncluded for compliance with the *IviDmm Class Specification*.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'A 1–based **index** into the channel table.'
                },
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPasses the number of bytes in the ViChar array you specify for the\n**Channel_String** parameter. If the next **Channel_String**,\nincluding the terminating NULL byte, contains more bytes than you\nindicate in this parameter, the function copies\n**buffer_size** –1 bytes into the buffer, places an ASCII NULL byte at\nthe end of the buffer, and returns the buffer size you must pass to get\nthe entire value.\n\nFor example, if the value is "123456" and the **buffer_size** is 4, the\nfunction places "123" into the buffer and returns 7. If you pass a\nnegative number, the function copies the value to the buffer regardless\nof the number of bytes in the value. If you pass 0, you can pass\nVI_NULL for the **Channel_String** buffer parameter. The default value\nis None.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the **channel_string** that is in the channel table at the\n**Index** you specify. Do not modify the contents of the\n**channel_string**.\n'
                },
                'name': 'channelString',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetDevTemp': {
        'documentation': {
            'description': 'Returns the current **Temperature** of the device.',
            'note': 'The NI 4050 and NI 4060 are not supported.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': 'Reserved.'
                },
                'name': 'options',
                'type': 'ViString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the current **temperature** of the device.'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetDigitsOfPrecision': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'digits',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the error information associated with the\n**Instrument_Handle**. This function retrieves and then clears the\nerror information for the session. If you leave the\n**Instrument_Handle** unwired, this function retrieves and then clears\nthe error information for the process.\n'
        },
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the **error_code** for the session or execution thread. If you\npass 0 for the **Buffer_Size**, you can pass VI_NULL for this\nparameter.\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPasses the number of bytes in the ViChar array you specify for the\n**Description** parameter. If the error description, including the\nterminating NULL byte, contains more bytes than you indicate in this\nparameter, the function copies **buffer_size** –1 bytes into the\nbuffer, places an ASCII NULL byte at the end of the buffer, and returns\nthe **buffer_size** you must pass to get the entire value.\n\nFor example, if the value is "123456" and the **buffer_size** is 4, the\nfunction places "123" into the buffer and returns 7. If you pass a\nnegative number, the function copies the value to the buffer regardless\nof the number of bytes in the value. If you pass 0, you can pass\nVI_NULL for the **Description** buffer parameter. The default value is\nNone.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the error **description** for the IVI session or execution\nthread. If there is no **description**, the function returns an empty\nstring. The buffer must contain at least as many elements as the value\nyou specify with the **Buffer_Size** parameter. If you pass 0 for the\n**Buffer_Size**, you can pass VI_NULL for this parameter.\n'
                },
                'name': 'description',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
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
    'GetErrorMessage': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the **Error_Message** as a user-readable string for the\nprovided **Error_Code**. Calling this function with a **Buffer_Size**\nof 0 returns the size needed for the **Error_Message**.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. You can also use\nVI_NULL if you do not have a valid **vi**.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe error code returned from the instrument for which you want to get a\nuser-readable string.\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of bytes allocated for the **Error_Message**\nViChar array. If the error description that this function returns\n(including terminating NULL byte) is larger than you indicated in\n**buffer__size**, the error description will be truncated to fit. If\nyou pass 0 for **buffer__size**, the function returns the buffer size\nneeded for **Error_Message**.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nContains the error information formatted into a user-readable string.\nThe buffer must contain at least as many elements as the value you\nspecify with the **Buffer_Size** parameter. If you pass 0 for\n**Buffer_Size**, you can pass VI_NULL for this parameter.\n'
                },
                'name': 'errorMessage',
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalRecommendedInterval': {
        'codegen_method': 'public',
        'documentation': {
            'description': '\nReturns the recommended interval between external recalibration in\n**Months**.\n',
            'note': 'The NI 4050 and NI 4060 are not supported.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the recommended number of **months** between external\ncalibrations.\n'
                },
                'name': 'months',
                'python_api_converter_name': 'convert_month_to_timedelta',
                'type': 'ViInt32',
                'type_in_documentation': 'datetime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetLastCalDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the date and time of the last calibration performed.',
            'note': 'The NI 4050 and NI 4060 are not supported.'
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
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niDMM_init or niDMM_InitWithOptions. The default is None.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the type of calibration performed (external or self-calibration).',
                    'note': 'The NI 4065 does not support self-calibration.',
                    'table_body': [
                        [
                            'NIDMM_VAL_INTERNAL_AREA (default)',
                            '0',
                            'Self-Calibration'
                        ],
                        [
                            'NIDMM_VAL_EXTERNAL_AREA',
                            '1',
                            'External Calibration'
                        ]
                    ]
                },
                'name': 'calType',
                'type': 'ViInt32'
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
        'python_name': 'get_cal_date_and_time',
        'real_datetime_call': 'GetCalDateAndTime',
        'returns': 'ViStatus'
    },
    'GetLastCalTemp': {
        'documentation': {
            'description': 'Returns the **Temperature** during the last calibration procedure.',
            'note': 'The NI 4050 and NI 4060 are not supported.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of calibration performed (external or\nself-calibration).\n',
                    'note': 'The NI 4065 does not support self-calibration.',
                    'table_body': [
                        [
                            'NIDMM_VAL_INTERNAL_AREA (default)',
                            '0',
                            'Self-Calibration'
                        ],
                        [
                            'NIDMM_VAL_EXTERNAL_AREA',
                            '1',
                            'External Calibration'
                        ]
                    ]
                },
                'name': 'calType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **temperature** during the last calibration.'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetLastRetrievedMeasurement': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'name': 'acqBacklog',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'changeCounter',
                'type': 'ViUInt64'
            },
            {
                'direction': 'out',
                'name': 'reading',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'measFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'reserved',
                'type': 'void'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetMeasurementPeriod': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the measurement **Period**, which is the amount of time it takes\nto complete one measurement with the current configuration. Use this\nfunction right before you begin acquiring data—after you have completely\nconfigured the measurement and after all configuration functions have\nbeen called.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the number of seconds it takes to make one measurement.\n\nThe first measurement in a multipoint acquisition requires additional\nsettling time. This function does not include this additional time or\nany NIDMM_ATTR_TRIGGER_DELAY associated with the first measurement.\nTime required for internal measurements, such as\nNIDMM_ATTR_AUTO_ZERO, is included.\n'
                },
                'name': 'period',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetNextCoercionRecord': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis function returns the coercion information associated with the IVI\nsession, and it retrieves and clears the oldest instance in which NI-DMM\ncoerced a value you specified to another value.\n\nIf you set NIDMM_ATTR_RECORD_COERCIONS to VI_TRUE (1), NI-DMM keeps\na list of all coercions it makes on ViInt32 or ViReal64 values that you\npass to NI-DMM functions. Use this function to retrieve information from\nthat list.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPasses the number of bytes in the ViChar array you specify for the\n**Coercion_Record** parameter. If the next coercion record string,\nincluding the terminating NULL byte, contains more bytes than you\nindicate in this parameter, the function copies **buffer_size** – 1\nbytes into the buffer, places an ASCII NULL byte at the end of the\nbuffer, and returns the buffer size you must pass to get the entire\nvalue.\n\nFor example, if the value is "123456" and the **buffer_size** is 4, the\nfunction places "123" into the buffer and returns 7. If you pass a\nnegative number, the function copies the value to the buffer regardless\nof the number of bytes in the value.\n\nIf you pass 0, you can pass VI_NULL for the **Coercion_Record** buffer\nparameter.\n\nThe default value is None.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the next **coercion_record** for the IVI session.\n\nIf there are no coercions records, the function returns an empty string.\nThe buffer must contain at least as many elements as the value you\nspecify with the **Buffer_Size** parameter.\n'
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
            'description': '\nThis function returns the interchangeability warnings associated with\nthe IVI session. It retrieves and clears the oldest instance in which\nthe class driver recorded an interchangeability warning.\nInterchangeability warnings indicate that using your application with a\ndifferent instrument might cause different behavior.\n\nThe driver performs interchangeability checking when\nNIDMM_ATTR_INTERCHANGE_CHECK is set to VI_TRUE (1). The function\nreturns an empty string in the **Interchange_Warning** parameter if no\ninterchangeability warnings remain for the session. In general, the\ninstrument driver generates interchangeability warnings when an\nattribute that affects the behavior of the instrument is in a state that\nyou did not specify.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPasses the number of bytes in the ViChar array you specify for the\n**Interchange_Warning** parameter. If the next interchangeability\nwarning string, including the terminating NULL byte, contains more bytes\nthan you indicate in this parameter, the function copies\n**buffer_size** –1 bytes into the buffer, places an ASCII NULL byte at\nthe end of the buffer, and returns the buffer size you must pass to get\nthe entire value.\n\nFor example, if the value is "123456" and the **buffer_size** is 4, the\nfunction places "123" into the buffer and returns 7. If you pass a\nnegative number, the function copies the value to the buffer regardless\nof the number of bytes in the value. If you pass 0, you can pass\nVI_NULL for the **Interchange_Warning** buffer parameter. The default\nvalue is None.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the next interchange warning for the IVI session. If there are\nno interchange warnings, the function returns an empty string. The\nbuffer must contain at least as many elements as the value you specify\nwith the **Buffer_Size** parameter.\n'
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
    'GetSelfCalSupported': {
        'documentation': {
            'description': '\nReturns a Boolean value that expresses whether or not the DMM that you\nare using can perform self-calibration.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns whether Self Cal is supported for the device specified by the\ngiven session.\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            '1',
                            'The DMM that you are using can perform self-calibration.'
                        ],
                        [
                            'VI_FALSE',
                            '0',
                            'The DMM that you are using cannot perform self-calibration.'
                        ]
                    ]
                },
                'name': 'selfCalSupported',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetViReal64Type': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'type',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationBuffer': {
        'documentation': {
            'description': '\nImports an attribute configuration to the session from the specified\nconfiguration buffer.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers.\n\n**Coercion Behavior for Certain Devices**\n\nImported and exported attribute configurations contain coerced values\nfor the following NI‑DMM devices:\n\n-  PXI/PCI/PCIe/USB‑4065\n-  PXI/PCI‑4070\n-  PXI‑4071\n-  PXI‑4072\n\nNI‑DMM coerces attribute values when the value you set is within the\nallowed range for the attribute but is not one of the discrete valid\nvalues the attribute supports. For example, for an attribute that\ncoerces values up, if you choose a value of 4 when the adjacent valid\nvalues are 1 and 10, the attribute coerces the value to 10.\n\n**Related Topics:**\n\n`Using Attributes and Properties with\nNI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(attributes)>`__\n\n`Setting Attributes Before Reading\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': 'Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the size, in bytes, of the byte array to import. If you enter\n0, this function returns the needed size.\n'
                },
                'name': 'size',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the byte array buffer that contains the attribute\nconfiguration to import.\n'
                },
                'name': 'configuration',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationFile': {
        'documentation': {
            'description': "\nImports an attribute configuration to the session from the specified\nfile.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers.\n\n**Coercion Behavior for Certain Devices**\n\nImported and exported attribute configurations contain coerced values\nfor the following NI‑DMM devices:\n\n-  PXI/PCI/PCIe/USB‑4065\n-  PXI/PCI‑4070\n-  PXI‑4071\n-  PXI‑4072\n\nNI‑DMM coerces attribute values when the value you set is within the\nallowed range for the attribute but is not one of the discrete valid\nvalues the attribute supports. For example, for an attribute that\ncoerces values up, if you choose a value of 4 when the adjacent valid\nvalues are 1 and 10, the attribute coerces the value to 10.\n\n**Related Topics:**\n\n`Using Attributes and Properties with\nNI‑DMM <REPLACE_DRIVER_SPECIFIC_URL_1(attributes)>`__\n\n`Setting Attributes Before Reading\nAttributes <javascript:LaunchHelp('DMM.chm::/setting_before_reading_attributes')>`__\n",
            'note': 'Not supported on the PCMCIA‑4050 or the PXI/PCI‑4060.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute path to the file containing the attribute\nconfiguration to import. If you specify an empty or relative path, this\nfunction returns an error.\n**Default File Extension:**\\  .nidmmconfig\n'
                },
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitExtCal': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThe following operations are performed if the **Calibration_Password**\nis valid:\n\n-  Creates a new session for external calibration to the device you\n   specify for the **Resource_Name** parameter.\n-  Resets the device and prepares the EEPROM for new calibration\n   coefficients.\n-  Returns a ViSession handle that you use to identify the instrument in\n   all calibration adjustments and post-adjustment verification steps.\n\nAfter opening a calibration session, the device cannot take valid\nmeasurements using this session until the device has been properly\nadjusted. Once the adjustment phase is complete, you can use this\nsession to verify the new calibration constants. After verification, you\nhave the option of saving the new calibration constants or reverting to\nthe previous calibration constants by specifying the **Action**\nparameter in niDMM_CloseExtCal.\n\nIf you encounter a fatal error such as a power failure or system crash\nwhile performing an external calibration, you can call\nniDMM_RestoreLastExtCalConstants to return the device to a usable\nstate.\n',
            'note': '\nThe NI 4050 and NI 4060 are not supported.\nRefer to the *NI 4065 6½ Digit DMM Calibration Procedure*, the\n*NI 4070/4072 6½ Digit FlexDMM Calibration Procedure*, or the *NI 4071\n7½–Digit FlexDMM Calibration Procedure* before using this function.\nThis function creates a new session the first time you invoke it for a\ndevice. If you call this function on the same resource, an error is\nreturned. You should use niDMM_CloseExtCal to close a session obtained\nusing this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'caution': '\nAll IVI names for the **Resource_Name**, such as logical names or\nvirtual names, are case-sensitive. If you use logical names, driver\nsession names, or virtual names in your program, you must make sure that\nthe name you use matches the name in the IVI Configuration Store file\nexactly, without any variations in the case of the characters in the\nname.\n',
                    'description': '\n| Contains the **resource_name** of the device to initialize. The\n  **resource_name** is assigned in Measurement & Automation Explorer\n  (MAX). Refer to `Related\n  Documentation <REPLACE_DRIVER_SPECIFIC_URL_1(related_documentation)>`__\n  for the *NI Digital Multimeters Getting Started Guide* for more\n  information about configuring and testing the DMM in MAX.\n| Valid Syntax:\n\n-  NI-DAQmx name\n-  DAQ::NI-DAQmx name[::INSTR]\n-  DAQ::Traditional NI-DAQ device number[::INSTR]\n-  IVI logical name\n'
                },
                'name': 'resourceName',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the password required to enable external calibration\nfunctionality.\n\nThe maximum password string length is eight characters, excluding the\ntermination character. "NI" is the factory-default password.\n'
                },
                'name': 'calibrationPassword',
                'type': 'ViString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe session handle that you obtain from niDMM_InitExtCal. The handle\nidentifies a particular instrument calibration session.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitWithOptions': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function completes the following tasks:\n\n-  Creates a new IVI instrument driver session and, optionally, sets the\n   initial state of the following session attributes:\n   NIDMM_ATTR_RANGE_CHECK, NIDMM_ATTR_QUERY_INSTR_STATUS,\n   NIDMM_ATTR_CACHE, NIDMM_ATTR_SIMULATE,\n   NIDMM_ATTR_RECORD_COERCIONS.\n-  Opens a session to the device you specify for the **Resource_Name**\n   parameter. If the **ID_Query** parameter is set to VI_TRUE, this\n   function queries the instrument ID and checks that it is valid for\n   this instrument driver.\n-  If the **Reset_Device** parameter is set to VI_TRUE, this function\n   resets the instrument to a known state. Sends initialization commands\n   to set the instrument to the state necessary for the operation of the\n   instrument driver.\n-  Returns a ViSession handle that you use to identify the instrument in\n   all subsequent instrument driver function calls.\n'
        },
        'method_name_for_documentation': '__init__',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'caution': '\nAll IVI names for the **Resource_Name**, such as logical names or\nvirtual names, are case-sensitive. If you use logical names, driver\nsession names, or virtual names in your program, you must make sure that\nthe name you use matches the name in the IVI Configuration Store file\nexactly, without any variations in the case of the characters in the\nname.\n',
                    'description': '\n| Contains the **resource_name** of the device to initialize. The\n  **resource_name** is assigned in Measurement & Automation Explorer\n  (MAX). Refer to `Related\n  Documentation <REPLACE_DRIVER_SPECIFIC_URL_1(related_documentation)>`__\n  for the *NI Digital Multimeters Getting Started Guide* for more\n  information about configuring and testing the DMM in MAX.\n| Valid Syntax:\n\n-  NI-DAQmx name\n-  DAQ::NI-DAQmx name[::INSTR]\n-  DAQ::Traditional NI-DAQ device number[::INSTR]\n-  IVI logical name\n'
                },
                'name': 'resourceName',
                'type': 'ViString'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nVerifies that the device you initialize is one that the driver supports.\nNI-DMM automatically performs this query, so setting this parameter is\nnot necessary.\nDefined Values:\n',
                    'table_body': [
                        [
                            'VI_TRUE (default)',
                            '1',
                            'Perform ID Query'
                        ],
                        [
                            'VI_FALSE',
                            '0',
                            'Skip ID Query'
                        ]
                    ]
                },
                'name': 'idQuery',
                'type': 'ViBoolean',
                'use_in_python_api': False
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to reset the instrument during the initialization\nprocedure.\nDefined Values:\n',
                    'table_body': [
                        [
                            'VI_TRUE (default)',
                            '1',
                            'Reset Device'
                        ],
                        [
                            'VI_FALSE',
                            '0',
                            "Don't Reset"
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
                    'description': '\n| Sets the initial value of certain attributes for the session. The\n  following table specifies the attribute name, attribute constant, and\n  default value for each attribute that you can use in this parameter:\n\nThe format of this string is, "AttributeName=Value." To set multiple\nattributes, separate their assignments with a comma.\n\nIf you pass NULL or an empty string for this parameter, the session uses\nthe default values for the attributes. You can override the default\nvalues by assigning a value explicitly in an **option_string**\nparameter. You do not have to specify all of the attributes and may\nleave any of them out (those left out use the default value).\n\nRefer to `Simulating NI Digital\nMultimeters <REPLACE_DRIVER_SPECIFIC_URL_1(simulation)>`__ for more\ninformation.\n',
                    'table_body': [
                        [
                            'Check',
                            'NIDMM_ATTR_RANGE_CHECK',
                            'VI_TRUE',
                            '1'
                        ],
                        [
                            'QueryInstrStatus',
                            'NIDMM_ATTR_QUERY_INSTR_STATUS',
                            'VI_FALSE',
                            '0'
                        ],
                        [
                            'Cache',
                            'NIDMM_ATTR_CACHE',
                            'VI_TRUE',
                            '1'
                        ],
                        [
                            'Simulate',
                            'NIDMM_ATTR_SIMULATE',
                            'VI_FALSE',
                            '0'
                        ],
                        [
                            'RecordCoercions',
                            'NIDMM_ATTR_RECORD_COERCIONS',
                            'VI_FALSE',
                            '0'
                        ],
                        [
                            'DriverSetup',
                            'NIDMM_ATTR_DRIVER_SETUP',
                            '"" (empty string)',
                            '""'
                        ]
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
                    'description': '\nReturns a ViSession handle that you use to identify the instrument in\nall subsequent instrument driver function calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
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
    'Initiate': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nInitiates an acquisition. After you call this function, the DMM leaves\nthe Idle state and enters the Wait-for-Trigger state. If trigger is set\nto Immediate mode, the DMM begins acquiring measurement data. Use\nniDMM_Fetch, niDMM_FetchMultiPoint, or niDMM_FetchWaveform to\nretrieve the measurement data.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InternalControl': {
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
                'name': 'calledBy',
                'type': 'ViInt32'
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
    'IsOverRange': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nTakes a **Measurement_Value** and determines if the value is a valid\nmeasurement or a value indicating that an overrange condition occurred.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The measured value returned from the DMM.',
                    'note': '\nIf an overrange condition occurs, the **Measurement_Value** contains\nan IEEE-defined NaN (Not a Number) value.\n'
                },
                'name': 'measurementValue',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns whether the measurement value is a valid measurement or an\noverrange condition.\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            '1',
                            'The value indicates that an overrange condition occurred.'
                        ],
                        [
                            'VI_FALSE',
                            '0',
                            'The value is a valid measurement.'
                        ]
                    ]
                },
                'name': 'isOverRange',
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
    'IsUnderRange': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nTakes a **Measurement_Value** and determines if the value is a valid\nmeasurement or a value indicating that an underrange condition occurred.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'The measured value returned from the DMM.',
                    'note': '\nIf an overrange condition occurs, the **Measurement_Value** contains\nan IEEE-defined NaN (Not a Number) value.\n'
                },
                'name': 'measurementValue',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns whether the **Measurement_Value** is a valid measurement or an\nunderrange condition.\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            '1',
                            'The value indicates that an underrange condition occurred.'
                        ],
                        [
                            'VI_FALSE',
                            '0',
                            'The value is a valid measurement.'
                        ]
                    ]
                },
                'name': 'isUnderRange',
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
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'LockSession': {
        'documentation': {
            'description': '\nThis function obtains a multithread lock on the instrument session.\nBefore it does so, it waits until all other execution threads have\nreleased their locks on the instrument session.\n\nOther threads might have obtained a lock on this session in the\nfollowing ways:\n\n-  The user application called this function.\n-  A call to the instrument driver locked the session.\n-  A call to the IVI Library locked the session.\n\nAfter your call to this function returns successfully, no other threads\ncan access the instrument session until you call niDMM_UnlockSession.\n\nUse this function and niDMM_UnlockSession around a sequence of calls to\ninstrument driver functions if you require that the instrument retain\nits settings through the end of the sequence. You can safely make nested\ncalls to this function within the same thread.\n\nTo completely unlock the session, you must balance each call to this\nfunction with a call to niDMM_UnlockSession. If, however, you use the\n**Caller_Has_Lock** parameter in all calls to this function and\nniDMM_UnlockSession within a function, the IVI Library locks the\nsession only once within the function regardless of the number of calls\nyou make to this function. This feature allows you to call\nniDMM_UnlockSession just once at the end of the function.\n'
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
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter serves as a convenience. If you do not want to use this\nparameter, pass VI_NULL. Use this parameter in complex functions to\nkeep track of whether you obtain a lock and, therefore, need to unlock\nthe session. To use this parameter, complete the following steps:\n\n#. Pass the address of a local ViBoolean variable.\n#. In the declaration of the local variable, initialize it to VI_FALSE\n   (0).\n#. Pass the address of the same local variable to any other calls you\n   make to this function or niDMM_UnlockSession in the same function.\n\nThe parameter is an input/output parameter. This function and\nniDMM_UnlockSession each inspect the current value and take the\nfollowing actions:\n\nIf the value is VI_TRUE (1), this function does not lock the session\nagain. If the value is VI_FALSE, this function obtains the lock and\nsets the value of the parameter to VI_TRUE.\n\nIf the value is VI_FALSE, niDMM_UnlockSession does not attempt to\nunlock the session. If the value is VI_TRUE, niDMM_UnlockSession\nreleases the lock and sets the value of the parameter to VI_FALSE.\nThus, you can, call niDMM_UnlockSession at the end of your function\nwithout worrying about whether you actually have the lock.\n\n**Example**\n\nViStatus TestFunc (ViSession vi, ViInt32 flags)\n\n{\n\n| ViStatus error = VI_SUCCESS;\n| ViBoolean haveLock = VI_FALSE;\n| if (flags & BIT_1)\n\n| {\n| viCheckErr( NIDMM_LockSession(vi, &haveLock;));\n| viCheckErr( TakeAction1(vi));\n| if (flags & BIT_2)\n\n{\n\nviCheckErr( NIDMM_UnlockSession(vi, &haveLock;));\n\nviCheckErr( TakeAction2(vi));\n\nviCheckErr( NIDMM_LockSession(vi, &haveLock;);\n\n}\n\nif (flags & BIT_3)\n\nviCheckErr( TakeAction3(vi));\n\n}\n\nError:\n\n/\\*\n\nAt this point, you cannot really be sure that you have the lock.\nFortunately, the haveLock variable takes care of that for you.\n\n\\*/\n\nniDMM_UnlockSession(vi, &haveLock;);\n\nreturn error;\n\n}\n'
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
    'MaxDigits': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViReal64'
    },
    'Measure': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'measFunction',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'maxTime',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'reading',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'MeasureMultiPoint': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'function',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'maxTime',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'readingArray',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'actualPts',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'PerformOpenCableComp': {
        'documentation': {
            'description': '\nFor the NI 4082 and NI 4072 only, performs the open cable compensation\nmeasurements for the current capacitance/inductance range, and returns\nopen cable compensation **Conductance** and **Susceptance** values. You\ncan use the return values of this function as inputs to\nniDMM_ConfigureOpenCableCompValues.\n\nThis function returns an error if the value of the NIDMM_ATTR_FUNCTION\nattribute is not set to NIDMM_VAL_CAPACITANCE (1005) or\nNIDMM_VAL_INDUCTANCE (1006).\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\n**conductance** is the measured value of open cable compensation\n**conductance**.\n'
                },
                'name': 'conductance',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\n**susceptance** is the measured value of open cable compensation\n**susceptance**.\n'
                },
                'name': 'susceptance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'PerformShortCableComp': {
        'documentation': {
            'description': '\nPerforms the short cable compensation measurements for the current\ncapacitance/inductance range, and returns short cable compensation\n**Resistance** and **Reactance** values. You can use the return values\nof this function as inputs to niDMM_ConfigureShortCableCompValues.\n\nThis function returns an error if the value of the NIDMM_ATTR_FUNCTION\nattribute is not set to NIDMM_VAL_CAPACITANCE (1005) or\nNIDMM_VAL_INDUCTANCE (1006).\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\n**resistance** is the measured value of short cable compensation\n**resistance**.\n'
                },
                'name': 'resistance',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\n**reactance** is the measured value of short cable compensation\n**reactance**.\n'
                },
                'name': 'reactance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReInit': {
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
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Read': {
        'documentation': {
            'description': 'Acquires a single measurement and returns the measured value.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'datetime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **maximum_time** allowed for this function to complete in\nmilliseconds. If the function does not complete within this time\ninterval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED\nerror code. This may happen if an external trigger has not been\nreceived, or if the specified timeout is not long enough for the\nacquisition to complete.\n\nThe valid range is 0–86400000. The default value is\nNIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout\nautomatically.\n'
                },
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                'type': 'ViInt32',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The measured value returned from the DMM.'
                },
                'name': 'reading',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadMultiPoint': {
        'documentation': {
            'description': '\nAcquires multiple measurements and returns an array of measured values.\nThe number of measurements the DMM makes is determined by the values you\nspecify for the **Trigger_Count** and **Sample_Count** parameters in\nniDMM_ConfigureMultiPoint.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'datetime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **maximum_time** allowed for this function to complete in\nmilliseconds. If the function does not complete within this time\ninterval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED\nerror code. This may happen if an external trigger has not been\nreceived, or if the specified timeout is not long enough for the\nacquisition to complete.\n\nThe valid range is 0–86400000. The default value is\nNIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout\nautomatically.\n'
                },
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                'type': 'ViInt32',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of measurements to acquire. The maximum number of\nmeasurements for a finite acquisition is the (**Trigger Count** x\n**Sample Count**) parameters in niDMM_ConfigureMultiPoint.\n\nFor continuous acquisitions, up to 100,000 points can be returned at\nonce. The number of measurements can be a subset. The valid range is any\npositive ViInt32. The default value is 1.\n'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An array of measurement values.',
                    'note': '\nThe size of the **Reading_Array** must be at least the size that you\nspecify for the **Array_Size** parameter.\n'
                },
                'name': 'readingArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the number of measured values actually retrieved from the DMM.'
                },
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'use_in_python_api': False
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadStatus': {
        'documentation': {
            'description': '\nReturns measurement backlog and acquisition status. Use this function to\ndetermine how many measurements are available before calling\nniDMM_Fetch, niDMM_FetchMultiPoint, or niDMM_FetchWaveform.\n',
            'note': 'The NI 4050 is not supported.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe number of measurements available to be read. If the backlog\ncontinues to increase, data is eventually overwritten, resulting in an\nerror.\n',
                    'note': '\nOn the NI 4060, the **Backlog** does not increase when autoranging. On\nthe NI 4065, the **Backlog** does not increase when Range is set to AUTO\nRANGE ON (-1), or before the first point is fetched when Range is set to\nAUTO RANGE ONCE (-3). These behaviors are due to the autorange model of\nthe devices.\n'
                },
                'name': 'acquisitionBacklog',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nIndicates status of the acquisition. The following table shows the\nacquisition states:\n',
                    'table_body': [
                        [
                            '0',
                            'Running'
                        ],
                        [
                            '1',
                            'Finished with backlog'
                        ],
                        [
                            '2',
                            'Finished with no backlog'
                        ],
                        [
                            '3',
                            'Paused'
                        ],
                        [
                            '4',
                            'No acquisition in progress'
                        ]
                    ]
                },
                'enum': 'AcquisitionStatus',
                'name': 'acquisitionStatus',
                'type': 'ViInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadWaveform': {
        'documentation': {
            'description': '\nFor the NI 4080/4081/4082 and the NI 4070/4071/4072, acquires a waveform\nand returns data as an array of values or as a waveform data type. The\nnumber of elements in the **Waveform_Array** is determined by the\nvalues you specify for the **Waveform_Points** parameter in\nniDMM_ConfigureWaveformAcquisition.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': 'datetime.timedelta(milliseconds=-1)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **maximum_time** allowed for this function to complete in\nmilliseconds. If the function does not complete within this time\ninterval, the function returns the NIDMM_ERROR_MAX_TIME_EXCEEDED\nerror code. This may happen if an external trigger has not been\nreceived, or if the specified timeout is not long enough for the\nacquisition to complete.\n\nThe valid range is 0–86400000. The default value is\nNIDMM_VAL_TIME_LIMIT_AUTO (-1). The DMM calculates the timeout\nautomatically.\n'
                },
                'name': 'maximumTime',
                'python_api_converter_name': 'convert_timedelta_to_milliseconds',
                'type': 'ViInt32',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of waveform points to return. You specify the total\nnumber of points that the DMM acquires in the **Waveform Points**\nparameter of niDMM_ConfigureWaveformAcquisition. The default value is\n1.\n'
                },
                'name': 'arraySize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'An array of measurement values.',
                    'note': '\nThe size of the **Waveform_Array** must be at least the size that you\nspecify for the **Array_Size** parameter.\n'
                },
                'name': 'waveformArray',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'arraySize'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Indicates the number of measured values actually retrieved from the DMM.'
                },
                'name': 'actualNumberOfPoints',
                'type': 'ViInt32',
                'use_in_python_api': False
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
    'ResetAttributes': {
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
    'ResetInterchangeCheck': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nWhen developing a complex test system that consists of multiple test\nmodules, it is generally a good idea to design the test modules so that\nthey can run in any order. To do so requires ensuring that each test\nmodule completely configures the state of each instrument it uses.\n\nIf a particular test module does not completely configure the state of\nan instrument, the state of the instrument depends on the configuration\nfrom a previously executed test module. If you execute the test modules\nin a different order, the behavior of the instrument and therefore the\nentire test module is likely to change. This change in behavior is\ngenerally instrument specific and represents an interchangeability\nproblem. You can use this function to test for such cases. After you\ncall this function, the interchangeability checking algorithms in NI-DMM\nignore all previous configuration operations. By calling this function\nat the beginning of a test module, you can determine whether the test\nmodule has dependencies on the operation of previously executed test\nmodules.\n\nThis function does not clear the interchangeability warnings from the\nlist of previously recorded interchangeability warnings. If you want to\nguarantee that niDMM_GetNextInterchangeWarning only returns those\ninterchangeability warnings that are generated after calling this\nfunction, you must clear the list of interchangeability warnings. You\ncan clear the interchangeability warnings list by repeatedly calling\nniDMM_GetNextInterchangeWarning until no more interchangeability\nwarnings are returned. If you are not interested in the content of those\nwarnings, you can call niDMM_ClearInterchangeWarnings.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithDefaults': {
        'documentation': {
            'description': '\nResets the instrument to a known state and sends initialization commands\nto the DMM. The initialization commands set the DMM settings to the\nstate necessary for the operation of NI-DMM. All user-defined default\nvalues associated with a logical name are applied after setting the DMM.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
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
            'description': '\nReverts the device to the calibration constants from the last complete\nexternal calibration. This function recovers the hardware if a fatal\nsystem error should occur during an external or self-calibration\nprocedure.\n\nAfter calling this function, you should call niDMM_SelfCal before\ntaking measurements with the device to adjust the device for any\ntemperature drifts since the last external calibration.\n',
            'note': 'The NI 4050, NI 4060, and NI 4080/4081/4082 are not supported.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'RevertAttributes': {
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
            'description': '\nFor the NI 4080/4081/4082 and the NI 4070/4071/4072, executes the\nself-calibration routine to maintain measurement accuracy.\n',
            'note': '\nThis function calls niDMM_reset, and any configurations previous to\nthe call will be lost. All attributes will be set to their default\nvalues after the call returns.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfTestPrep': {
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
                'name': 'password',
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SelfTestPrepImpl': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'password',
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareTrigger': {
        'documentation': {
            'description': '\nSends a command to trigger the DMM. Call this function if you have\nconfigured either the NIDMM_ATTR_TRIGGER_SOURCE or\nNIDMM_ATTR_SAMPLE_TRIGGER attributes. If the\nNIDMM_ATTR_TRIGGER_SOURCE and/or NIDMM_ATTR_SAMPLE_TRIGGER\nattributes are set to NIDMM_VAL_EXTERNAL or NIDMM_VAL_TTL\\ *n*, you\ncan use this function to override the trigger source that you configured\nand trigger the device. The NI 4050 and NI 4060 are not supported.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
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
            'description': '\nThis function sets the value of a ViBoolean attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid\n   or is different than the value you specify.\n\nThis instrument driver contains high-level functions that set most of\nthe instrument attributes. It is best to use the high-level driver\nfunctions as much as possible. They handle order dependencies and\nmultithread locking for you. In addition, they perform status checking\nonly after setting all of the attributes.\n\nIn contrast, when you set multiple attributes using the SetAttribute\nfunctions, the functions check the instrument status after each call.\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. National Instruments DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
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
            'description': '\nThis function sets the value of a ViInt32 attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid\n   or is different than the value you specify.\n\nThis instrument driver contains high-level functions that set most of\nthe instrument attributes. It is best to use the high-level driver\nfunctions as much as possible. They handle order dependencies and\nmultithread locking for you. In addition, they perform status checking\nonly after setting all of the attributes.\n\nIn contrast, when you set multiple attributes using the SetAttribute\nfunctions, the functions check the instrument status after each call.\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. National Instruments DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
                },
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViReal64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nThis function sets the value of a ViReal64 attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid\n   or is different than the value you specify.\n\nThis instrument driver contains high-level functions that set most of\nthe instrument attributes. It is best to use the high-level driver\nfunctions as much as possible. They handle order dependencies and\nmultithread locking for you. In addition, they perform status checking\nonly after setting all of the attributes.\n\nIn contrast, when you set multiple attributes using the SetAttribute\nfunctions, the functions check the instrument status after each call.\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. National Instruments DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
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
            'description': '\nThis function sets the value of a ViSession attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid\n   or is different than the value you specify.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. National Instruments DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
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
            'description': '\nThis function sets the value of a ViString attribute.\n\nThis is a low-level function that you can use to set the values of\ninstrument-specific attributes and inherent IVI attributes.\n\nIf the attribute represents an instrument state, this function performs\ninstrument I/O in the following cases:\n\n-  State caching is disabled for the entire session or for the\n   particular attribute.\n-  State caching is enabled, and the currently cached value is invalid\n   or is different than the value you specify.\n\nThis instrument driver contains high-level functions that set most of\nthe instrument attributes. It is best to use the high-level driver\nfunctions as much as possible. They handle order dependencies and\nmultithread locking for you. In addition, they perform status checking\nonly after setting all of the attributes.\n\nIn contrast, when you set multiple attributes using the SetAttribute\nfunctions, the functions check the instrument status after each call.\nAlso, when state caching is enabled, the high-level functions that\nconfigure multiple attributes perform instrument I/O only for the\nattributes whose value you change. Thus, you can safely call the\nhigh-level functions without the penalty of redundant instrument I/O.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThis parameter is ignored. National Instruments DMMs do not support\nchannel names since they only have a single channel. This parameter is\nincluded in order to support interchangeability and upgradability to\nmultiple channel DMMs.\n\nThe default value is " " (an empty string).\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the ID of an attribute.'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Pass the value that you want to set the attribute to.'
                },
                'name': 'attributeValue',
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAutoZero': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'enable',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetCalPassword': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nChanges the password required to enable external calibration\nfunctionality for the specified instrument. The maximum password string\nlength is eight characters, excluding the termination character. "NI" is\nthe default password.\n',
            'note': '\nThe NI 4050 and NI 4060 are not supported.\nA password is required for external calibration. Be sure to record the\npassword in a secure location.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the current password required to enable external calibration\nfunctionality. The maximum password string length is eight characters,\nexcluding the termination character.\n'
                },
                'name': 'oldPassword',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **new_password** required to enable external calibration\nfunctionality. The maximum password string length is eight characters,\nexcluding the termination character.\n'
                },
                'name': 'newPassword',
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetCalUserDefinedInfo': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nStores the user-defined information in the EEPROM. Use\nniDMM_GetCalUserDefinedInfoMaxSize to learn the maximum string size\nthat is allowed. If the **Info** string size is larger than the maximum\nstring size, NI-DMM stores as much of the information as possible,\ntruncates the remainder, and returns a warning.\n',
            'note': 'The NI 4050 and NI 4060 are not supported.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the user-defined information to be stored in the EEPROM such\nas the operator who performed the calibration operation or system\ninformation. Use niDMM_GetCalUserDefinedinfoMaxSize to learn the\nmaximum string size that is allowed. If the **info** string size is\nlarger than the maximum string size, NI-DMM stores as much of the\ninformation as possible, truncates the remainder, and return a warning.\n'
                },
                'name': 'info',
                'type': 'ViString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetPowerlineFrequency': {
        'codegen_method': 'no',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'frequency',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'documentation': {
            'description': '\nThis function releases a lock that you acquired on an instrument session\nusing niDMM_LockSession. Refer to niDMM_LockSession for additional\ninformation on session locks.\n'
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
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter serves as a convenience. If you do not want to use this\nparameter, pass VI_NULL.\n\nUse this parameter in complex functions to keep track of whether you\nobtain a lock and, therefore, need to unlock the session.\n\nTo use this parameter, complete the following steps:\n\n#. Pass the address of a local ViBoolean variable.\n#. In the declaration of the local variable, initialize it to VI_FALSE\n   (0).\n#. Pass the address of the same local variable to any other calls you\n   make to niDMM_LockSession or this function in the same function.\n\nThe parameter is an input/output parameter. niDMM_LockSession and this\nfunction each inspect the current value and take the following actions:\n\nIf the value is VI_TRUE (1), niDMM_LockSession does not lock the\nsession again. If the value is VI_FALSE, niDMM_LockSession obtains the\nlock and sets the value of the parameter to VI_TRUE.\n\nIf the value is VI_FALSE, this function does not attempt to unlock the\nsession. If the value is VI_TRUE, this function releases the lock and\nsets the value of the parameter to VI_FALSE. Thus, you can, call this\nfunction at the end of your function without worrying about whether you\nactually have the lock.\n\n**Example**\n\nViStatus TestFunc (ViSession vi, ViInt32 flags)\n\n{\n\nViStatus error = VI_SUCCESS;\n\nViBoolean haveLock = VI_FALSE;\n\nif (flags & BIT_1)\n\n{\n\nviCheckErr( NIDMM_LockSession(vi, &haveLock;));\n\nviCheckErr( TakeAction1(vi));\n\nif (flags & BIT_2)\n\n{\n\nviCheckErr( NIDMM_UnlockSession(vi, &haveLock;));\n\nviCheckErr( TakeAction2(vi));\n\nviCheckErr( NIDMM_LockSession(vi, &haveLock;);\n\n}\n\nif (flags & BIT_3)\n\nviCheckErr( TakeAction3(vi));\n\n}\n\nError:\n\n/\\*\n\nAt this point, you cannot really be sure that you have the lock.\nFortunately, the haveLock variable takes care of that for you.\n\n\\*/\n\nniDMM_UnlockSession(vi, &haveLock;);\n\nreturn error;\n\n}\n'
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
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Closes the specified session and deallocates resources that it reserved.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
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
            'description': '\nTakes the **Error_Code** returned by the instrument driver functions,\ninterprets it, and returns it as a user-readable string.\n'
        },
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe **error_code** returned from the instrument. The default is 0,\nindicating VI_SUCCESS.\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'The error information formatted into a string.'
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
            'description': '\nReads an **Error_Code** and message from the DMM error queue. National\nInstruments DMMs do not contain an error queue. Errors are reported as\nthey occur. Therefore, this function does not detect errors; it is\nincluded for compliance with the *IviDmm Class Specification*.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe **error_code** returned from the instrument.\n\nThe default value is VI_SUCCESS (0).\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Formats the **Error_Code** into a user-readable message string.',
                    'note': 'The array must contain at least 256 elements ViChar[256].'
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
            'description': '\nPerforms a self-test on the DMM to ensure that the DMM is functioning\nproperly. Self-test does not calibrate the DMM. Zero\nindicates success. \n\nOn the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that\nyou should check the fuse and replace it, if necessary.\n\nRaises `SelfTestError` on self test failure. Attributes on exception object:\n\n- code - failure code from driver\n- message - status message from driver\n',
            'note': [
                'Self-test does not check the fuse on the NI 4065, NI 4071, and NI 4081. Hence, even if the fuse is blown on the device, self-test does not return error code 1013.',
                'This function calls niDMM_reset, and any configurations previous to the call will be lost. All attributes will be set to their default values after the call returns.'
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
                    'description': 'Identifies a particular instrument session. You obtain the **vi** parameter from niDMM_init or niDMM_InitWithOptions.'
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
            'description': '\nThis function completes the following tasks:\n\n-  Creates a new IVI instrument driver session.\n-  Opens a session to the device you specify for the **Resource_Name**\n   parameter.\n\n-  If the **ID_Query** parameter is set to VI_TRUE (1), this function\n   queries the instrument ID and checks that it is valid for this\n   instrument driver.\n\n-  If the **Reset_Device** parameter is set to VI_TRUE (1), this\n   function resets the instrument to a known state. Sends initialization\n   commands to set the instrument to the state necessary for the\n   operation of the instrument driver.\n\n-  Returns a ViSession handle that you use to identify the instrument in\n   all subsequent instrument driver function calls.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'caution': '\nAll IVI names for the **Resource_Name**, such as logical names or\nvirtual names, are case-sensitive. If you use logical names, driver\nsession names, or virtual names in your program, you must make sure that\nthe name you use matches the name in the IVI Configuration Store file\nexactly, without any variations in the case of the characters in the\nname.\n',
                    'description': '\n| Contains the **resource_name** of the device to initialize. The\n  **resource_name** is assigned in Measurement & Automation Explorer\n  (MAX). Refer to `Related\n  Documentation <REPLACE_DRIVER_SPECIFIC_URL_1(related_documentation)>`__\n  for the *NI Digital Multimeters Getting Started Guide* for more\n  information about configuring and testing the DMM in MAX.\n| Valid Syntax:\n\n-  NI-DAQmx name\n-  DAQ::NI-DAQmx name[::INSTR]\n-  DAQ::Traditional NI-DAQ device number[::INSTR]\n-  IVI logical name\n'
                },
                'name': 'resourceName',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nVerifies that the device you initialize is one that the driver supports.\nNI-DMM automatically performs this query, so setting this parameter is\nnot necessary.\nDefined Values:\n',
                    'table_body': [
                        [
                            'VI_TRUE (default)',
                            '1',
                            'Perform ID Query'
                        ],
                        [
                            'VI_FALSE',
                            '0',
                            'Skip ID Query'
                        ]
                    ]
                },
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to reset the instrument during the initialization\nprocedure.\nDefined Values:\n',
                    'table_body': [
                        [
                            'VI_TRUE (default)',
                            '1',
                            'Reset Device'
                        ],
                        [
                            'VI_FALSE',
                            '0',
                            "Don't Reset"
                        ]
                    ]
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a ViSession handle that you use to identify the instrument in\nall subsequent instrument driver function calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'reset': {
        'documentation': {
            'description': '\nResets the instrument to a known state and sends initialization commands\nto the instrument. The initialization commands set instrument settings\nto the state necessary for the operation of the instrument driver.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
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
            'description': '\nReturns the revision numbers of the instrument driver and instrument\nfirmware.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a string containing the instrument driver software revision\nnumbers.\n',
                    'note': 'The array must contain at least 256 elements ViChar[256].'
                },
                'name': 'instrumentDriverRevision',
                'type': 'ViChar[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a string containing the instrument **firmware_revision**\nnumbers.\n',
                    'note': 'The array must contain at least 256 elements ViChar[256].'
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
            'description': '\nPerforms a self-test on the DMM to ensure that the DMM is functioning\nproperly. Self-test does not calibrate the DMM.\n',
            'note': '\nThis function calls niDMM_reset, and any configurations previous to\nthe call will be lost. All attributes will be set to their default\nvalues after the call returns.\n'
        },
        'method_name_for_documentation': 'self_test',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. You obtain the **vi**\nparameter from niDMM_init or niDMM_InitWithOptions. The default is\nNone.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nContains the value returned from the instrument self-test. Zero\nindicates success.\n\nOn the NI 4080/4082 and NI 4070/4072, the error code 1013 indicates that\nyou should check the fuse and replace it, if necessary.\n',
                    'note': '\nSelf-test does not check the fuse on the NI 4065, NI 4071, and\nNI 4081. Hence, even if the fuse is blown on the device, self-test does\nnot return error code 1013.\n'
                },
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThis parameter contains the string returned from the instrument\nself-test. The array must contain at least 256 elements.\n\nFor the NI 4050 and NI 4060, the error codes returned for self-test\nfailures include the following:\n\n-  NIDMM_ERROR_AC_TEST_FAILURE\n-  NIDMM_ERROR_DC_TEST_FAILURE\n-  NIDMM_ERROR_RESISTANCE_TEST_FAILURE\n\nThese error codes indicate that the DMM should be repaired.\n\nFor the NI 4080/4081/4082 and the NI 4070/4071/4072, the error code\nreturned for a self-test failure is NIDMM_ERROR_SELF_TEST_FAILURE.\nThis error code indicates that the DMM should be repaired.\n'
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
