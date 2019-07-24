# -*- coding: utf-8 -*-
# This file is generated from API metadata for NI-DCPower version 19.1.0d33
functions = {
    'Abort': {
        'documentation': {
            'description': '\nTransitions the NI-DCPower session from the Running state to the\nCommitted state. If a sequence is running, it is stopped. Any\nconfiguration functions called after this function are not applied until\nthe niDCPower_Initiate function is called. If power output is enabled\nwhen you call the niDCPower_Abort function, the output channels remain\nin their current state and continue providing power.\n\nUse the niDCPower_ConfigureOutputEnabled function to disable power\noutput on a per channel basis. Use the niDCPower_reset function to\ndisable output on all channels.\n\nRefer to the `Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in\nthe *NI DC Power Supplies and SMUs Help* for information about the\nspecific NI-DCPower software states.\n\n**Related Topics:**\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'AbortWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'AllocateServer': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'name': 'wasSetByUser',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustCurrentLimit': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCalculates the calibration constants for the current limit for the\nspecified output channel and range. This function compares the array in\n**requestedOutputs** to the array in **measuredOutputs** and calculates\nthe calibration constants for the current limit returned by the device.\nRefer to the calibration procedure for the device you are calibrating\nfor detailed instructions on the appropriate use of this function. This\nfunction can only be called from an external calibration session.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument calibration session. **vi** is\nobtained from the niDCPower_InitExtCal function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the channel name to which these calibration settings apply.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the range to calibrate with these settings. Only one channel\nat a time may be calibrated.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of elements in **requestedOutputs** and\n**measuredOutputs**.\n'
                },
                'name': 'numberOfMeasurements',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the output values that were requested in the\nniDCPower_ConfigureCurrentLimit function.\n'
                },
                'name': 'requestedOutputs',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the output values measured by an external\nprecision digital multimeter.\n'
                },
                'name': 'measuredOutputs',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustCurrentMeasurement': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCalibrates the current measurements returned by the niDCPower_Measure\nfunction for the specified output channel. This function calculates new\ncalibration coefficients for the specified current measurement range\nbased on the **reportedOutputs** and **measuredOutputs**. Refer to the\ncalibration procedure for the device you are calibrating for detailed\ninstructions about the appropriate use of this function. This function\ncan only be called in an external calibration session.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument calibration session. **vi** is\nobtained from the niDCPower_InitExtCal function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel name to which these calibration settings\napply.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the range to calibrate with these settings. Only one channel\nat a time may be calibrated.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of elements in **reportedOutputs** and\n**measuredOutputs**.\n'
                },
                'name': 'numberOfMeasurements',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the output values that were returned by the\nniDCPower_Measure function.\n'
                },
                'name': 'reportedOutputs',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the output values measured by an external\nprecision digital multimeter.\n'
                },
                'name': 'measuredOutputs',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustInternalReference': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nPrograms the adjusted reference value to the device. Refer to the\ncalibration procedure for the device you are calibrating for detailed\ninstructions on the appropriate use of this function. This function can\nonly be called from an external calibration session.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the internal reference to be adjusted.\n**Defined Values**:\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_INTERNAL_REFERENCE_5V (1054)',
                            'Calibration pin connected to 5 V internal reference.'
                        ],
                        [
                            'NIDCPOWER_VAL_INTERNAL_REFERENCE_100KOHM (1055)',
                            'Calibration pin connected to 100 kΩ internal reference.'
                        ]
                    ]
                },
                'name': 'internalReference',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the updated value of the internal reference that will be\nprogrammed to the device.\n'
                },
                'name': 'adjustedInternalReference',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustOutputResistance': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCompares the array in **requestedOutputs** to the array in\n**measuredOutputs** and calculates the calibration constants for the\noutput resistance of the specified channel. Refer to the calibration\nprocedure for the device you are calibrating for detailed instructions\non the appropriate use of this function. This function can only be\ncalled from an external calibration session.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument calibration session. **vi** is\nobtained from the niDCPower_InitExtCal function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel name to which these calibration settings\napply. Only one channel at a time can be calibrated.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of elements in **requestedOutputs** and\n**measuredOutputs**.\n'
                },
                'name': 'numberOfMeasurements',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the output values that were requested in the\nniDCPower_ConfigureOutputResistance function.\n'
                },
                'name': 'requestedOutputs',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the output values measured by an external\nprecision digital multimeter.\n'
                },
                'name': 'measuredOutputs',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustResidualCmrrAndRangeChange': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustResidualCurrentOffset': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCalculates the calibration constants for the residual current offsets\nfor the specified output channel. Residual offsets account for minor\noffset effects on the device that lie outside of the self-calibration\ncircuitry. These offsets can include multiplexer input offsets and\nleakage effects from internal switching.\n\nThis function requires that the output be open prior to it being\ninvoked.\n\nRefer to the calibration procedure for the device you are calibrating\nfor detailed instructions on the appropriate use of this function. This\nfunction can be called only in an external calibration session.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustResidualVoltageOffset': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCalculates the calibration constants for the residual voltage offsets\nfor the specified output channel. Residual offsets account for minor\noffset effects on the device that lie outside of the self-calibration\ncircuitry. These offsets can include multiplexer input offsets and\nleakage effects from internal switching.\n\nThis function requires that the output be shorted prior to it being\ninvoked.\n\nRefer to the calibration procedure for the device you are calibrating\nfor detailed instructions on the appropriate use of this function. This\nfunction can be called only in an external calibration session.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustResidualVoltageOffsetOnly': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustVoltageLevel': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCalculates the calibration constants for the voltage level for the\nspecified output channel. This function compares the array in\n**requestedOutputs** to the array in **measuredOutputs** and calculates\nthe calibration constants for the voltage level of the output channel.\nRefer to the calibration procedure of the device you are calibrating for\ndetailed instructions on the appropriate use of this function. This\nfunction can be called only in an external calibration session.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument calibration session. **vi** is\nobtained from the niDCPower_InitExtCal function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the output channel to which these calibration settings apply.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the range to calibrate with these settings. Only one channel\nat a time may be calibrated.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of elements in **requestedOutputs** and\n**measuredOutputs**.\n'
                },
                'name': 'numberOfMeasurements',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the output values requested in the\nniDCPower_ConfigureVoltageLevel function.\n'
                },
                'name': 'requestedOutputs',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the output values measured by an external\nprecision digital multimeter.\n'
                },
                'name': 'measuredOutputs',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalAdjustVoltageMeasurement': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nCalculates the calibration constants for the voltage measurements\nreturned by the niDCPower_Measure function for the specified output\nchannel. This function compares the array in **reportedOutputs** to the\narray in **measuredOutputs** and calculates the calibration constants\nfor the voltage measurements returned by the niDCPower_Measure\nfunction. Refer to the calibration procedure for the device you are\ncalibrating for detailed instructions on the appropriate use of this\nfunction. This function can only be called in an external calibration\nsession.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument calibration session. **vi** is\nobtained from the niDCPower_InitExtCal function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the channel name to which these calibration settings apply.'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the range to calibrate with these settings. Only one channel\nat a time may be calibrated.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of elements in **reportedOutputs** and\n**measuredOutputs**.\n'
                },
                'name': 'numberOfMeasurements',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the output values that were returned by the\nniDCPower_Measure function.\n'
                },
                'name': 'reportedOutputs',
                'type': 'ViReal64'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies an array of the output values measured by an external\nprecision digital multimeter.\n'
                },
                'name': 'measuredOutputs',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'CalSelfCalibrate': {
        'documentation': {
            'description': '\nPerforms a self-calibration upon the specified channel(s).\n\nThis function disables the output, performs several internal\ncalculations, and updates calibration values. The updated calibration\nvalues are written to the device hardware if the\nNIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE attribute is set to\nNIDCPOWER_VAL_WRITE_TO_EEPROM. Refer to the\nNIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE attribute topic for more\ninformation about the settings for this attribute.\n\nWhen calling niDCPower_CalSelfCalibrate with the PXIe-4162/4163,\nspecify all channels of your PXIe-4162/4163 with the channelName input.\nYou cannot self-calibrate a subset of PXIe-4162/4163 channels.\n\nRefer to the\n`Self-Calibration <REPLACE_DRIVER_SPECIFIC_URL_1(selfcal)>`__ topic for\nmore information about this function.\n\n**Related Topics:**\n\n`Self-Calibration <REPLACE_DRIVER_SPECIFIC_URL_1(selfcal)>`__\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'python_name': 'self_cal',
        'returns': 'ViStatus'
    },
    'ChangeExtCalPassword': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nChanges the **password** that is required to initialize an external\ncalibration session. The **password** can be a maximum of four\nalphanumeric characters. If you call this function in a session,\n**password** is changed immediately. If you call this function in an\nexternal calibration session, **password** is changed only after you\nclose the session using the niDCPower_CloseExtCal function with\n**action** set to NIDCPOWER_VAL_COMMIT.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the previous password used to protect the calibration values.'
                },
                'name': 'oldPassword',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the new password to use to protect the calibration values.'
                },
                'name': 'newPassword',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ClearError': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\n| Clears the error code and error description for the IVI session. If\n  the user specifies a valid IVI session for **vi**, this function\n  clears the error information for the session. If the user passes\n  VI_NULL for **vi**, this function clears the error information for\n  the current execution thread. If the ViSession parameter is an invalid\n  session, the function does nothing and returns an error.\n| The function clears the error code by setting it to VI_SUCCESS. If\n  the error description string is non-NULL, the function de-allocates\n  the error description string and sets the address to VI_NULL.\n| Maintaining the error information separately for each thread is useful\n  if the user does not have a session handle to pass to the\n  niDCPower_GetError function, which occurs when a call to\n  niDCPower_InitializeWithChannels fails.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
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
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
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
            'description': '\nCloses the session specified in **vi** and deallocates the resources\nthat NI-DCPower reserved for calibration. Refer to the calibration\nprocedure for the device you are calibrating for detailed instructions\non the appropriate use of this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument calibration session. **vi** is\nobtained from the niDCPower_InitExtCal function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies how to use the calibration values from this session as the\nsession is closed.\n\n**Defined Values**:\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_COMMIT (1002)',
                            'The new calibration constants are stored in the EEPROM.'
                        ],
                        [
                            'NIDCPOWER_VAL_CANCEL (1001)',
                            'The old calibration constants are kept, and the new ones are discarded.'
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
            'description': '\nApplies previously configured settings to the device. Calling this\nfunction moves the NI-DCPower session from the Uncommitted state into\nthe Committed state. After calling this function, modifying any\nattribute reverts the NI-DCPower session to the Uncommitted state. Use\nthe niDCPower_Initiate function to transition to the Running state.\nRefer to the `Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in\nthe *NI DC Power Supplies and SMUs Help* for details about the specific\nNI-DCPower software states.\n\n**Related Topics:**\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'CommitWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureApertureTime': {
        'documentation': {
            'description': '\nConfigures the aperture time on the specified channel(s).\n\nThe supported values depend on the **units**. Refer to the *Aperture\nTime* topic for your device in the *NI DC Power Supplies and SMUs Help*\nfor more information. In general, devices support discrete\n**apertureTime** values, and if you configure **apertureTime** to some\nunsupported value, NI-DCPower coerces it up to the next supported value.\n\nRefer to the *Measurement Configuration and Timing* or *DC Noise\nRejection* topic for your device in the *NI DC Power Supplies and SMUs\nHelp* for more information about how to configure your measurements.\n\n**Related Topics:**\n\n`Aperture Time <REPLACE_DRIVER_SPECIFIC_URL_1(aperture)>`__\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the aperture time. Refer to the *Aperture Time* topic for your\ndevice in the *NI DC Power Supplies and SMUs Help* for more information.\n'
                },
                'name': 'apertureTime',
                'type': 'ViReal64'
            },
            {
                'default_value': 'ApertureTimeUnits.SECONDS',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the units for **apertureTime**.\n**Defined Values**:\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_SECONDS (1028)',
                            'Specifies seconds.'
                        ],
                        [
                            'NIDCPOWER_VAL_POWER_LINE_CYCLES (1029)',
                            'Specifies Power Line Cycles.'
                        ]
                    ]
                },
                'enum': 'ApertureTimeUnits',
                'name': 'units',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureAutoZero': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures auto zero for the device.\n\nRefer to the `NI PXI-4132 Auto\nZero <REPLACE_DRIVER_SPECIFIC_URL_1(4132_autozero)>`__ and `NI PXI-4132\nMeasurement Configuration and\nTiming <REPLACE_DRIVER_SPECIFIC_URL_1(4132_measureconfigtiming)>`__\ntopics in the *NI DC Power Supplies and SMUs Help* for more information\nabout how to configure your measurements.\n\n**Related Topics:**\n\n`Auto Zero <REPLACE_DRIVER_SPECIFIC_URL_1(autozero)>`__\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the auto-zero setting. Refer to the *Measurement Configuration\nand Timing* topic and the *Auto Zero* topic for your device for more\ninformation about how to configure your measurements.\n**Defined Values:**\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_OFF (0)',
                            'Disables auto-zero.'
                        ],
                        [
                            'NIDCPOWER_VAL_ONCE (1024)',
                            'Makes zero conversions following the first measurement after initiating the device. The device uses these zero conversions for the preceding measurement and future measurements until the device is reinitiated.'
                        ],
                        [
                            'NIDCPOWER_VAL_ON (1)',
                            'Makes zero conversions for every measurement.'
                        ]
                    ]
                },
                'enum': 'AutoZero',
                'name': 'autoZero',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureCurrentLevel': {
        'codegen_method': 'no',
        'documentation': {
            'description': "\nConfigures the current level the device attempts to generate for the\nspecified channel(s). The channel must be enabled for the specified\ncurrent level to take effect. Refer to the\nniDCPower_ConfigureOutputEnabled function for more information about\nenabling the output channel.\n\nThe current level setting is applicable only if the output function of\nthe channel is set to NIDCPOWER_VAL_DC_CURRENT. Use\nnidcpower_ConfigureOutputFunction to set the output function. The\ndevice actively regulates the current at the specified level unless\ndoing so causes a voltage greater than the\nniDCPower_ConfigureVoltageLimit across the channels' output terminals.\n\n**Related Topics:**\n\n`Constant Current\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(constant_current)>`__\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the current level, in amps, to generate for the specified\nchannel(s).\n**Valid Values:**\nThe valid values for this parameter are defined by the current level\nrange that is configured using the niDCPower_ConfigureCurrentlevelRange\nfunction.\n'
                },
                'name': 'level',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureCurrentLevelRange': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the current level range for the specified channel(s). The\nconfigured range defines the valid values the current level can be set\nto using the niDCPower_ConfigureCurrentLevel function. The current\nlevel range setting is applicable only if the output function of the\nchannel is set to NIDCPOWER_VAL_DC_CURRENT. Use\nnidcpower_ConfigureOutputFunction to set the output function.\n\nUse the NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE attribute to enable\nautomatic selection of the current level range.\n\n**Related Topics:**\n\n`Ranges <REPLACE_DRIVER_SPECIFIC_URL_1(ranges)>`__\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the current level range, in amps, for the specified channel.\nFor valid ranges, refer to the *ranges* topic for your device in the *NI\nDC Power Supplies and SMUs Help*.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureCurrentLimit': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\n| Configures the current limit for the specified channel(s). The channel\n  must be enabled for the specified current limit to take effect. Refer\n  to the niDCPower_ConfigureOutputEnabled function for more information\n  about enabling the output channel.\n| The current limit is the current that the output should not exceed\n  when generating the desired niDCPower_ConfigureVoltageLevel. The\n  current limit setting is applicable only if the output function of the\n  channel is set to NIDCPOWER_VAL_DC_VOLTAGE. Use\n  nidcpower_ConfigureOutputFunction to set the output function.\n\n**Related Topics:**\n\n`Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies how the output should behave when the current limit is\nreached.\n**Defined Values:**\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_CURRENT_REGULATE',
                            'Controls output current so that it does not exceed the current limit. Power continues to generate even if the current limit is reached.'
                        ]
                    ]
                },
                'name': 'behavior',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the current limit, in amps, on the specified channel(s). The\nlimit is specified as a positive value, but symmetric positive and\nnegative limits are enforced simultaneously.\n**Valid Values:**\nThe valid values for this parameter are defined by the current limit\nrange that is configured using the niDCPower_ConfigureCurrentlimitRange\nfunction.\n'
                },
                'name': 'limit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureCurrentLimitRange': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the current limit range for the specified channel(s).The\nconfigured range defines the valid values the current limit can be set\nto using the niDCPower_ConfigureCurrentLimit function. The current\nlimit range setting is applicable only if the output function of the\nchannel is set to NIDCPOWER_VAL_DC_VOLTAGE. Use\nnidcpower_ConfigureOutputFunction to set the output function.\n\nUse the NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE attribute to enable\nautomatic selection of the current limit range.\n\n**Related Topics:**\n\n`Ranges <REPLACE_DRIVER_SPECIFIC_URL_1(ranges)>`__\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the current limit range, in amps, for the specified channel.\nFor valid ranges, refer to the *ranges* topic for your device in the *NI\nDC Power Supplies and SMUs Help*.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeMeasureTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Configures the Measure trigger for digital edge triggering.',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the input terminal for the digital edge Measure trigger.\n\nYou can specify any valid input terminal for this function. Valid\nterminals are listed in MAX under the **Device Routes** tab. For\nPXIe-4162/4163, refer to the Signal Routing topic for the device to\ndetermine which routes are available. This information is not available\non a Device Routes tab in MAX.\n\nInput terminals can be specified in one of two ways. If the device is\nnamed Dev1 and your terminal is PXI_Trig0, you can specify the terminal\nwith the fully qualified terminal name, /Dev1/PXI_Trig0, or with the\nshortened terminal name, PXI_Trig0. The input terminal can also be a\nterminal from another device. For example, you can set the input\nterminal on Dev1 to be /Dev2/SourceCompleteEvent.\n'
                },
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to configure the Measure trigger to assert on the\nrising or falling edge.\n**Defined Values:**\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_RISING (1016)',
                            'Asserts the trigger on the rising edge of the digital signal.'
                        ],
                        [
                            'NIDCPOWER_VAL_FALLING (1017)',
                            'Asserts the trigger on the falling edge of the digital signal.'
                        ]
                    ]
                },
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeMeasureTriggerWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgePulseTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Configures the Pulse trigger for digital edge triggering.',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the input terminal for the digital edge Pulse trigger.\n\nYou can specify any valid input terminal for this function. Valid\nterminals are listed in MAX under the **Device Routes** tab.\n\nInput terminals can be specified in one of two ways. If the device is\nnamed Dev1 and your terminal is PXI_Trig0, you can specify the terminal\nwith the fully qualified terminal name, /Dev1/PXI_Trig0, or with the\nshortened terminal name, PXI_Trig0. The input terminal can also be a\nterminal from another device. For example, you can set the input\nterminal on Dev1 to be /Dev2/SourceCompleteEvent.\n'
                },
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to configure the Pulse trigger to assert on the rising\nor falling edge.\n**Defined Values:**\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_RISING (1016)',
                            'Asserts the trigger on the rising edge of the digital signal.'
                        ],
                        [
                            'NIDCPOWER_VAL_FALLING (1017)',
                            'Asserts the trigger on the falling edge of the digital signal.'
                        ]
                    ]
                },
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgePulseTriggerWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeSequenceAdvanceTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Configures the Sequence Advance trigger for digital edge triggering.',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the input terminal for the digital edge Sequence Advance\ntrigger.\n\nYou can specify any valid input terminal for this function. Valid\nterminals are listed in MAX under the **Device Routes** tab. For\nPXIe-4162/4163, refer to the Signal Routing topic for the device to\ndetermine which routes are available. This information is not available\non a Device Routes tab in MAX.\n\nInput terminals can be specified in one of two ways. If the device is\nnamed Dev1 and your terminal is PXI_Trig0, you can specify the terminal\nwith the fully qualified terminal name, /Dev1/PXI_Trig0, or with the\nshortened terminal name, PXI_Trig0. The input terminal can also be a\nterminal from another device. For example, you can set the input\nterminal on Dev1 to be /Dev2/SourceCompleteEvent.\n'
                },
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to configure the Sequence Advance trigger to assert on\nthe rising or falling edge.\n**Defined Values:**\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_RISING (1016)',
                            'Asserts the trigger on the rising edge of the digital signal.'
                        ],
                        [
                            'NIDCPOWER_VAL_FALLING (1017)',
                            'Asserts the trigger on the falling edge of the digital signal.'
                        ]
                    ]
                },
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeSequenceAdvanceTriggerWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeSourceTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Configures the Source trigger for digital edge triggering.',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the input terminal for the digital edge Source trigger.\n\nYou can specify any valid input terminal for this function. Valid\nterminals are listed in MAX under the **Device Routes** tab. For\nPXIe-4162/4163, refer to the Signal Routing topic for the device to\ndetermine which routes are available. This information is not available\non a Device Routes tab in MAX.\n\nInput terminals can be specified in one of two ways. If the device is\nnamed Dev1 and your terminal is PXI_Trig0, you can specify the terminal\nwith the fully qualified terminal name, /Dev1/PXI_Trig0, or with the\nshortened terminal name, PXI_Trig0. The input terminal can also be a\nterminal from another device. For example, you can set the input\nterminal on Dev1 to be /Dev2/SourceCompleteEvent.\n'
                },
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to configure the Source trigger to assert on the\nrising or falling edge.\n**Defined Values:**\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_RISING (1016)',
                            'Asserts the trigger on the rising edge of the digital signal.'
                        ],
                        [
                            'NIDCPOWER_VAL_FALLING (1017)',
                            'Asserts the trigger on the falling edge of the digital signal.'
                        ]
                    ]
                },
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeSourceTriggerWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeStartTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Configures the Start trigger for digital edge triggering.',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the input terminal for the digital edge Start trigger.\n\nYou can specify any valid input terminal for this function. Valid\nterminals are listed in MAX under the **Device Routes** tab. For\nPXIe-4162/4163, refer to the Signal Routing topic for the device to\ndetermine which routes are available. This information is not available\non a Device Routes tab in MAX.\n\nInput terminals can be specified in one of two ways. If the device is\nnamed Dev1 and your terminal is PXI_Trig0, you can specify the terminal\nwith the fully qualified terminal name, /Dev1/PXI_Trig0, or with the\nshortened terminal name, PXI_Trig0. The input terminal can also be a\nterminal from another device. For example, you can set the input\nterminal on Dev1 to be /Dev2/SourceCompleteEvent.\n'
                },
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to configure the Start trigger to assert on the rising\nor falling edge.\n**Defined Values:**\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_RISING (1016)',
                            'Asserts the trigger on the rising edge of the digital signal.'
                        ],
                        [
                            'NIDCPOWER_VAL_FALLING (1017)',
                            'Asserts the trigger on the falling edge of the digital signal.'
                        ]
                    ]
                },
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureDigitalEdgeStartTriggerWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'inputTerminal',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'edge',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOutputEnabled': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nEnables or disables generation on the specified channel(s). Depending on\nthe selected output function, the voltage level, current level,or output\nresistance must be set in addition to enabling the output to generate\nthe desired level. For more information about configuring the output\nlevel, refer to niDCPower_ConfigureOutputFunction.\n',
            'note': "\nIf the device is in the\n`Uncommitted <javascript:LaunchHelp('NI_DC_Power_Supplies_Help.chm::/programmingStates.html#uncommitted')>`__\nstate, enabling the output does not take effect until you call the\nniDCPower_Initiate function.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether the output is enabled or disabled.\n**Defined Values**:\n',
                    'table_body': [
                        [
                            'VI_TRUE',
                            'Enables generation on the specified output channel(s).'
                        ],
                        [
                            'VI_FALSE',
                            'Disables generation on the specified output channel(s). This parameter has no effect on the output disconnect relay. To toggle the relay, use the NIDCPOWER_ATTR_OUTPUT_CONNECTED attribute.'
                        ]
                    ]
                },
                'name': 'enabled',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOutputFunction': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the function the device attempts to generate for the\nspecified channel(s).\n\nWhen NIDCPOWER_VAL_DC_VOLTAGE is selected, the device generates the\ndesired voltage level on the output as long as the output current is\nbelow the current limit. The following functions can be used to\nconfigure the channel when NIDCPOWER_VAL_DC_VOLTAGE is selected:\n\n-  niDCPower_ConfigureVoltageLevel\n-  niDCPower_ConfigureCurrentLimit\n-  niDCPower_ConfigureVoltageLevelRange\n-  niDCPower_ConfigureCurrentLimitRange\n\nWhen NIDCPOWER_VAL_DC_CURRENT is selected, the device generates the\ndesired current level on the output as long as the output voltage is\nbelow the voltage limit. The following functions can be used to\nconfigure the channel when NIDCPOWER_VAL_DC_CURRENT is selected:\n\n-  niDCPower_ConfigureCurrentLevel\n-  niDCPower_ConfigureVoltageLimit\n-  niDCPower_ConfigureCurrentLevelRange\n-  niDCPower_ConfigureVoltageLimitRange\n\nWhen NIDCPOWER_VAL_PULSE_VOLTAGE is selected, the device generates\npulses at the desired voltage levels on the output as long as the output\ncurrent is below the current limit. The following VIs can be used to\nconfigure the channel when NIDCPOWER_VAL_PULSE_VOLTAGE is selected:\n\n-  niDCPower_ConfigurePulseVoltageLevel\n-  niDCPower_ConfigurePulseBiasVoltageLevel\n-  niDCPower_ConfigurePulseCurrentLimit\n-  niDCPower_ConfigurePulseBiasCurrentLimit\n-  niDCPower_ConfigurePulseVoltageLevelRange\n-  niDCPower_ConfigurePulseCurrentLimitRange\n\nWhen NIDCPOWER_VAL_PULSE_CURRENT is selected, the device generates\npulses at the desired current levels on the output as long as the output\nvoltage is below the voltage limit. The following VIs can be used to\nconfigure the channel when NIDCPOWER_VAL_PULSE_CURRENT is selected:\n\n-  niDCPower_ConfigurePulseCurrentLevel\n-  niDCPower_ConfigurePulseBiasCurrentLevel\n-  niDCPower_ConfigurePulseVoltageLimit\n-  niDCPower_ConfigurePulseBiasVoltageLimit\n-  niDCPower_ConfigurePulseCurrentLevelRange\n-  niDCPower_ConfigurePulseVoltageLimitRange\n\n**Related Topics:**\n\n`Constant Voltage\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(constant_voltage)>`__\n\n`Constant Current\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(constant_current)>`__\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nConfigures the function to generate for the specified channel(s).\n**Defined Values**:\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_DC_VOLTAGE (1006)',
                            'Sets the output function to DC voltage.'
                        ],
                        [
                            'NIDCPOWER_VAL_DC_CURRENT (1007)',
                            'Sets the output function to DC current.'
                        ],
                        [
                            'NIDCPOWER_VAL_PULSE_VOLTAGE (1049)',
                            'Sets the output function to pulse voltage.'
                        ],
                        [
                            'NIDCPOWER_VAL_PULSE_CURRENT (1050)',
                            'Sets the output function to pulse current.'
                        ]
                    ]
                },
                'name': 'function',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOutputRange': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures either the voltage level range or the current limit range. If\n**range type** is Voltage, the voltage level range is configured. If\n**range type** is Current, the current limit range is configured.\n\nThis function does not configure any of the DC Current output function\nsettings. Refer to the niDCPower_ConfigureOutputFunction function for\nmore information.\n\nThis is a deprecated function. You must use the following functions\ninstead of theniDCPower_ConfigureOutputRange function:\n\n-  niDCPower_ConfigureVoltageLevel\n-  niDCPower_ConfigureVoltageLimit\n-  niDCPower_ConfigureCurrentLevel\n-  niDCPower_ConfigureCurrentLimit\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the type of the range: voltage or current.\n**Defined Values**:\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_RANGE_CURRENT (0)',
                            'NI-DCPower configures the current range.'
                        ],
                        [
                            'NIDCPOWER_VAL_RANGE_VOLTAGE (1)',
                            'NI-DCPower configures the voltage range.'
                        ]
                    ]
                },
                'name': 'rangeType',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the range to calibrate with these settings. Only one channel\nat a time may be calibrated.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOutputResistance': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the output resistance that the device attempts to generate\nfor the specified channel or channels. The channel must be enabled for\nthe specified output resistance to take effect.\n\nRefer to the nidcpower_ConfigureOutputEnabled function for more\ninformation about enabling the output channel.\n\nFor NI PXIe-4141/4143/4145 devices, output resistance is only supported\nif the output function of the channel is set to\nNIDCPOWER_VAL_DC_VOLTAGE using the niDCPower_ConfigureOutputFunction\nfunction.\n\nFor PXIe-4135, NI PXIe-4137, and NI PXIe-4139 devices, output resistance\nis supported if the output function of the channel is set to\nNIDCPOWER_VAL_DC_CURRENT or NIDCPOWER_VAL_DC_VOLTAGE using the\nniDCPower_ConfigureOutputFunction function.\n\nThe device actively regulates the current and voltage to reach the\nspecified output resistance, although in DC Voltage output mode, the\nvoltage at the output experiences a "virtual drop" that is proportional\nto its current. In DC Current output mode, the output experiences a\n"virtual leakage current" that is proportional to the output voltage.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output resistance, in ohms, for the specified channel.\nRefer to the `NI PXIe-4141 Programmable Output\nresistance <REPLACE_DRIVER_SPECIFIC_URL_1(4140_4141_progoutputresist)>`__,\n`NI PXIe-4143 Programmable Output\nresistance <REPLACE_DRIVER_SPECIFIC_URL_1(4142_4143_progoutputresist)>`__,\n`NI PXIe-4145 Programmable Output\nresistance <REPLACE_DRIVER_SPECIFIC_URL_1(4144_4145_progoutputresist)>`__,or\n`NI PXIe-4154 Programmable Output\nresistance <REPLACE_DRIVER_SPECIFIC_URL_1(4154_prog_output_resist)>`__\ntopic in the NI DC Power Supplies and SMUs Help for more information\nabout configuring output resistance.\n'
                },
                'name': 'resistance',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureOvp': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'enabled',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'limit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePowerLineFrequency': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies the power line frequency for specified channel(s). NI-DCPower\nuses this value to select a timebase for setting the\nniDCPower_ConfigureApertureTime function in power line cycles (PLCs).\n\nRefer to the *Measurement Configuration and Timing* topic for your\ndevice in the *NI DC Power Supplies and SMUs Help* for more information\nabout how to configure your measurements.\n\n**Related Topics:**\n\n`Measurement Noise\nRejection <REPLACE_DRIVER_SPECIFIC_URL_1(noiserejectmeasure)>`__\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the power line frequency in hertz for specified channel(s).\nNI-DCPower uses this value to select a timebase for the\nNIDCPOWER_ATTR_APERTURE_TIME attribute. Refer to the *Measurement\nConfiguration and Timing* topic for your device for more information\nabout how to configure your measurements.\n**Defined Values**:\n',
                    'note': 'Set this parameter to the frequency of the AC power line.',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_50_HERTZ (50.0)',
                            'Specifies 50 Hz.'
                        ],
                        [
                            'NIDCPOWER_VAL_60_HERTZ (60.0)',
                            'Specifies 60 Hz.'
                        ]
                    ]
                },
                'name': 'powerlineFrequency',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseBiasCurrentLevel': {
        'codegen_method': 'no',
        'documentation': {
            'description': "\nConfigures the pulse bias current level that the device attempts to\ngenerate for the specified channel(s) during the off phase of a pulse.\nThe channel must be enabled for the specified current level to take\neffect.\n\nRefer to the niDCPower_ConfigureOutputEnabled function for more\ninformation about enabling the output channel. The pulse current level\nsetting is applicable only if the channel is set to the\nNIDCPOWER_VAL_PULSE_CURRENT output function using the\nniDCPower_ConfigureOutputFunction function.\n\nThe device actively regulates the current at the specified level unless\ndoing so causes a voltage drop greater than the\nNIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT across the channels' output\nterminals.\n",
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the pulse bias current level, in amps, on the specified\nchannel(s).\n**Valid Values:**\nThe valid values for this parameter are defined by the pulse current\nlevel range that is configured using the\nniDCPower_ConfigurePulseCurrentlevelRange function.\n'
                },
                'name': 'level',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseBiasCurrentLimit': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the pulse bias current limit for the specified channel(s).\nThe channel must be enabled for the specified current limit to take\neffect.\n\nRefer to the niDCPower_ConfigureOutputEnabled function for more\ninformation about enabling the output channel. The pulse bias current\nlimit is the current that the output must not exceed when generating the\ndesired NIDCPOWER_ATTR_pULSE_bIAS_vOLTAGE_lEVEL. The pulse bias\ncurrent limit setting is only applicable if the channel is set to the\nNIDCPOWER_VAL_PULSE_VOLTAGE output function using the\nniDCPower_ConfigureOutputFunction function.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the pulse bias current limit, in amps, on the specified\nchannel(s). The limit is specified as a positive value, but symmetric\npositive and negative limits are enforced simultaneously.\n**Valid Values:**\nThe valid values for this parameter are defined by the pulse current\nlimit range that is configured using the\nniDCPower_ConfigurePulseCurrentlimitRange function.\n'
                },
                'name': 'limit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseBiasVoltageLevel': {
        'codegen_method': 'no',
        'documentation': {
            'description': "\nConfigures the pulse bias voltage level that the device attempts to\ngenerate for the specified channel(s) during the off phase of a pulse.\nThe channel must be enabled for the specified voltage level to take\neffect.\n\nRefer to the niDCPower_ConfigureOutputEnabled function for more\ninformation about enabling the output channel. The pulse bias voltage\nlevel setting is applicable only if the channel is set to the\nNIDCPOWER_VAL_PULSE_VOLTAGE output function using the\nniDCPower_ConfigureOutputFunction function.\n\nThe device actively regulates the voltage at the specified level unless\ndoing so causes a current greater than the\nNIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT through the channels'\noutput terminals.\n",
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the pulse bias voltage level, in volts, for the output channel\ngeneration.\n**Valid Values**:\nThe valid values for this parameter are defined by the pulse voltage\nlevel range that is selected using the\nniDCPower_ConfigurePulseVoltagelevelRange function.\n'
                },
                'name': 'level',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseBiasVoltageLimit': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the pulse bias voltage limit for the specified channel(s).\nThe channel must be enabled for the specified voltage limit to take\neffect.\n\nRefer to the niDCPower_ConfigureOutputEnabled function for more\ninformation about enabling the output channel. The pulse bias voltage\nlimit is the voltage that the output must not exceed when generating the\ndesired NIDCPOWER_ATTR_PULSE_bIAS_cURRENT_lEVEL. The pulse bias\nvoltage limit setting is only applicable if the channel is set to the\nNIDCPOWER_VAL_PULSE_CURRENT output function using the\nniDCPower_ConfigureOutputFunction function.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the pulse bias voltage limit, in volts, on the specified\nchannel(s). The limit is specified as a positive value, but symmetric\npositive and negative limits are enforced simultaneously.\n**Valid Values:**\nThe valid values for this parameter are defined by the pulse voltage\nlimit range that is configured using the\nniDCPower_ConfigurePulseVoltagelimitRange function.\n'
                },
                'name': 'limit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseCurrentLevel': {
        'codegen_method': 'no',
        'documentation': {
            'description': "\nConfigures the pulse current level that the device attempts to generate\nfor the specified channel(s) during the on phase of a pulse. The channel\nmust be enabled for the specified current level to take effect.\n\nRefer to the niDCPower_ConfigureOutputEnabled function for more\ninformation about enabling the output channel. The pulse current level\nsetting is applicable only if the channel is set to the\nNIDCPOWER_VAL_PULSE_CURRENT output function using the\nniDCPower_ConfigureOutputEnabled function.\n\nThe device actively regulates the current at the specified level unless\ndoing so causes a voltage drop greater than the\nNIDCPOWER_ATTR_PULSE_VOLTAGE_lIMIT across the channels' output\nterminals.\n",
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the pulse current level, in amps, on the specified channel(s).\n**Valid Values:**\nThe valid values for this parameter are defined by the pulse current\nlevel range that is configured using the\nniDCPower_ConfigurePulseCurrentlevelRange function.\n'
                },
                'name': 'level',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseCurrentLevelRange': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the pulse current level range for the specified channel(s).\n\nThe configured range defines the valid values to which you can set the\npulse current level and pulse bias current level using the\nniDCPower_ConfigurePulseCurrentLevel and\nniDCPower_ConfigurePulseBiasCurrentLevel functions. The pulse current\nlevel range setting is applicable only if the channel is set to the\nNIDCPOWER_VAL_PULSE_CURRENT output function using the\nniDCPower_ConfigureOutputFunction function.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the pulse current level range, in amps, on the specified\nchannel(s).\nFor valid ranges, refer to the *ranges* topic for your device in the *NI\nDC Power Supplies and SMUs Help*.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseCurrentLimit': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the pulse current limit for the specified channel(s). The\nchannel must be enabled for the specified current limit to take effect.\n\nRefer to the niDCPower_ConfigureOutputEnabled function for more\ninformation about enabling the output channel. The pulse current limit\nis the current that the output must not exceed when generating the\ndesired NIDCPOWER_ATTR_PULSE_vOLTAGE_lEVEL. The pulse current limit\nsetting is only applicable if the channel is set to the\nNIDCPOWER_VAL_PULSE_VOLTAGE output function using the\nniDCPower_ConfigureOutputFunction function.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the pulse current limit, in amps, on the specified channel(s).\nThe limit is specified as a positive value, but symmetric positive and\nnegative limits are enforced simultaneously.\n**Valid Values:**\nThe valid values for this parameter are defined by the pulse current\nlimit range that is configured using the\nniDCPower_ConfigurePulseCurrentlimitRange function.\n'
                },
                'name': 'limit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseCurrentLimitRange': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the pulse current limit range for the specified channel(s).\n\nThe configured range defines the valid values to which you can set the\npulse current limit and pulse bias current limit using the\nniDCPower_ConfigurePulseCurrentLimit and\nniDCPower_ConfigurePulseBiasCurrentLimit functions. The pulse current\nlimit range setting is applicable only if the channel is set to the\nNIDCPOWER_VAL_PULSE_VOLTAGE output function using the\nniDCPower_ConfigureOutputFunction function.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the pulse current limit range, in amps, on the specified\nchannel(s).\nFor valid ranges, refer to the *ranges* topic for your device in the *NI\nDC Power Supplies and SMUs Help*.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseVoltageLevel': {
        'codegen_method': 'no',
        'documentation': {
            'description': "\nConfigures the pulse voltage level that the device attempts to generate\nfor the specified channel(s) during the on phase of a pulse. The channel\nmust be enabled for the specified voltage level to take effect.\n\nRefer to the niDCPower_ConfigureOutputEnabled function for more\ninformation about enabling the output channel. The pulse voltage level\nsetting is applicable only if the channel is set to the\nNIDCPOWER_VAL_PULSE_VOLTAGE output function using the\nniDCPower_ConfigureOutputFunction function.\n\nThe device actively regulates the voltage at the specified level unless\ndoing so causes a current greater than the\nNIDCPOWER_ATTR_PULSE_cURRENT_lIMIT through the channels' output\nterminals.\n",
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the pulse voltage level, in volts, for the output channel\ngeneration.\n**Valid Values**:\nThe valid values for this parameter are defined by the voltage level\nrange that is selected using the\nniDCPower_ConfigurePulseVoltagelevelRange function.\n'
                },
                'name': 'level',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseVoltageLevelRange': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the pulse voltage level range for the specified channel(s).\n\nThe configured range defines the valid values to which you can set the\npulse voltage level and pulse bias voltage level using the\nniDCPower_ConfigurePulseVoltageLevel and\nniDCPower_ConfigurePulseBiasVoltageLevel functions. The pulse voltage\nlevel range setting is applicable only if the channel is set to the\nNIDCPOWER_VAL_PULSE_VOLTAGE output function using the\nniDCPower_ConfigureOutputFunction function.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the pulse voltage level range, in volts, on the specified\nchannel(s).\nFor valid ranges, refer to the *ranges* topic for your device in the *NI\nDC Power Supplies and SMUs Help*.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseVoltageLimit': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the pulse voltage limit for the specified channel(s). The\nchannel must be enabled for the specified voltage limit to take effect.\n\nRefer to the niDCPower_ConfigureOutputEnabled function for more\ninformation about enabling the output channel. The pulse voltage limit\nis the voltage that the output must not exceed when generating the\ndesired NIDCPOWER_ATTR_PULSE_cURRENT_lEVEL. The pulse voltage limit\nsetting is only applicable if the channel is set to the\nNIDCPOWER_VAL_PULSE_CURRENT output function using the\nniDCPower_ConfigureOutputFunction function.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the pulse voltage limit, in volts, on the specified output\nchannel(s). The limit is specified as a positive value, but symmetric\npositive and negative limits are enforced simultaneously.\n**Valid Values:**\nThe valid values for this parameter are defined by the pulse voltage\nlimit range that is configured using the\nniDCPower_ConfigurePulseVoltagelimitRange function.\n'
                },
                'name': 'limit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigurePulseVoltageLimitRange': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the pulse voltage limit range for the specified channel(s).\n\nThe configured range defines the valid values to which you can set the\npulse voltage limit and pulse bias voltage limit using the\nniDCPower_ConfigurePulseVoltageLimit and\nniDCPower_ConfigurePulseBiasVoltageLimit functions. The pulse voltage\nlimit range setting is applicable only if the channel is set to the\nNIDCPOWER_VAL_PULSE_CURRENT output function using the\nniDCPower_ConfigureOutputFunction function.\n\n.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the pulse voltage limit range, in volts, on the specified\nchannel(s).\nFor valid ranges, refer to the *ranges* topic for your device in the *NI\nDC Power Supplies and SMUs Help*.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSense': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nSpecifies whether to use\n`local <REPLACE_DRIVER_SPECIFIC_URL_2(local_and_remote_sense)>`__ or\n`remote <REPLACE_DRIVER_SPECIFIC_URL_2(local_and_remote_sense)>`__\nsensing of the output voltage on the specified channel(s). Refer to the\n*Devices* topic specific to your device in the *NI DC Power Supplies and\nSMUs* Help for more information about sensing voltage on supported\nchannels.\n\n**Related Topics:**\n\n`Local and Remote\nSense <REPLACE_DRIVER_SPECIFIC_URL_1(4112_localandremotesense)>`__\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies local or remote sensing on the specified channel(s).\n**Defined Values:**\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_LOCAL (1008)',
                            'Local sensing'
                        ],
                        [
                            'NIDCPOWER_VAL_REMOTE (1009)',
                            'Remote sensing'
                        ]
                    ]
                },
                'name': 'sense',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeMeasureTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the Measure trigger for software triggering. Use the\nniDCPower_SendSoftwareEdgeTrigger function to assert the trigger\ncondition.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeMeasureTriggerWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgePulseTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the Pulse trigger for software triggering. Use the\nniDCPower_SendSoftwareEdgeTrigger function to assert the trigger\ncondition.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgePulseTriggerWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeSequenceAdvanceTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the Sequence Advance trigger for software triggering. Use the\nniDCPower_SendSoftwareEdgeTrigger function to assert the trigger\ncondition.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeSequenceAdvanceTriggerWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeSourceTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the Source trigger for software triggering. Use the\nniDCPower_SendSoftwareEdgeTrigger function to assert the trigger\ncondition.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeSourceTriggerWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeStartTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the Start trigger for software triggering. Use the\nniDCPower_SendSoftwareEdgeTrigger function to assert the trigger\ncondition.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSoftwareEdgeStartTriggerWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSourceMode': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the NIDCPOWER_ATTR_SOURCE_MODE attribute. Specifies\nwhether to run a single output point or a sequence. Refer to the `Single\nPoint Source Mode <REPLACE_DRIVER_SPECIFIC_URL_1(singlept)>`__ and\n`Sequence Source Mode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__\ntopics in the *NI DC Power Supplies and SMUs Help* for more information\nabout using this function.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the source mode for the NI-DCPower session.\n**Defined Values**:\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_SINGLE_POINT (1020)',
                            'Applies a single source configuration.'
                        ],
                        [
                            'NIDCPOWER_VAL_SEQUENCE (1021)',
                            'Applies a list of voltage or current configurations sequentially.'
                        ]
                    ]
                },
                'name': 'sourceMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureSourceModeWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'sourceMode',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureVoltageLevel': {
        'codegen_method': 'no',
        'documentation': {
            'description': "\nConfigures the voltage level the device attempts to generate for the\nspecified channel(s). The channel must be enabled for the specified\nvoltage level to take effect. Refer to the\nniDCPower_ConfigureOutputEnabled function for more information about\nenabling the output channel.\n\nThe voltage level setting is applicable only if the output function of\nthe channel is set to NIDCPOWER_VAL_DC_VOLTAGE. Use\nnidcpower_ConfigureOutputFunction to set the output function.\n\nThe device actively regulates the voltage at the specified level unless\ndoing so causes a current output greater than the\nNIDCPOWER_ATTR_CURRENT_LIMIT across the channels' output terminals.\n\n**Related Topics:**\n\n`Constant Voltage\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(constant_voltage)>`__\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the voltage level, in volts, for the output channel\ngeneration.\n**Valid Values**:\nThe valid values for this parameter are defined by the voltage level\nrange that is selected using the niDCPower_ConfigureVoltagelevelRange\nfunction.\n'
                },
                'name': 'level',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureVoltageLevelRange': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the voltage level range for the specified channel(s). The\nconfigured range defines the valid values the voltage level can be set\nto using the niDCPower_ConfigureVoltageLevel function. The voltage\nlevel range setting is applicable only if the output function of the\nchannel is set to NIDCPOWER_VAL_DC_VOLTAGE. Use\nnidcpower_ConfigureOutputFunction to set the output function.\n\nUse the NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE attribute to enable\nautomatic selection of the voltage level range.\n\n**Related Topics:**\n\n`Ranges <REPLACE_DRIVER_SPECIFIC_URL_1(ranges)>`__\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the voltage level range, in volts, on the specified\nchannel(s).\nFor valid ranges, refer to the *ranges* topic for your device in the *NI\nDC Power Supplies and SMUs Help*.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureVoltageLimit': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the voltage limit for the specified channel(s). The channel\nmust be enabled for the specified voltage limit to take effect. Refer to\nthe niDCPower_ConfigureOutputEnabled function for more information\nabout enabling the output channel.\n\nThe voltage limit is the voltage that the output should not exceed when\ngenerating the desired niDCPower_ConfigureCurrentLevel. The voltage\nlimit setting is applicable only if the output function of the channel\nis set to NIDCPOWER_VAL_DC_CURRENT. Use\nnidcpower_ConfigureOutputFunction to set the output function.\n\n**Related Topics:**\n\n`Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the voltage limit, in volts, on the specified output\nchannel(s). The limit is specified as a positive value, but symmetric\npositive and negative limits are enforced simultaneously.\n**Valid Values:**\nThe valid values for this parameter are defined by the voltage limit\nrange that is configured using the niDCPower_ConfigureVoltagelimitRange\nfunction.\n'
                },
                'name': 'limit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConfigureVoltageLimitRange': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nConfigures the voltage limit range for the specified channel(s). The\nconfigured range defines the valid values the voltage limit can be set\nto using the niDCPower_ConfigureVoltageLimit function. The voltage\nlimit range setting is applicable only if the output function of the\nchannel is set to NIDCPOWER_VAL_DC_CURRENT. Use\nnidcpower_ConfigureOutputFunction to set the output function.\n\nUse the NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE attribute to enable\nautomatic selection of the voltage limit range.\n\n**Related Topics:**\n\n`Ranges <REPLACE_DRIVER_SPECIFIC_URL_1(ranges)>`__\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the voltage limit range, in volts, on the specified\nchannel(s).\nFor valid ranges, refer to the *ranges* topic for your device in the *NI\nDC Power Supplies and SMUs Help*.\n'
                },
                'name': 'range',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ConnectInternalReference': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nRoutes the internal reference to the calibration pin in preparation for\nadjustment. Refer to the calibration procedure for the device you are\ncalibrating for detailed instructions on the appropriate use of this\nfunction. This function can only be called from an external calibration\nsession.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the internal reference to be connected to the calibration pin.\n**Defined Values**:\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_INTERNAL_REFERENCE_5V (1054)',
                            'Calibration pin connected to 5 V internal reference.'
                        ],
                        [
                            'NIDCPOWER_VAL_INTERNAL_REFERENCE_100KOHM (1055)',
                            'Calibration pin connected to 100 kΩ internal reference.'
                        ],
                        [
                            'NIDCPOWER_VAL_INTERNAL_REFERENCE_GROUND (1056)',
                            'Calibration pin connected to ground reference.'
                        ],
                        [
                            'NIDCPOWER_VAL_INTERNAL_REFERENCE_NONE (1057)',
                            'Calibration pin disconnected from internal reference.'
                        ]
                    ]
                },
                'name': 'internalReference',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateAdvancedSequence': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCreates an empty advanced sequence. Call the\nniDCPower_CreateAdvancedSequenceStep function to add steps to the\nactive advanced sequence.\n\nYou can create multiple advanced sequences in a session.\n\n**Support for this function**\n\nYou must set the source mode to Sequence to use this function.\n\nUsing the niDCPower_SetSequence function with Advanced Sequence\nfunctions is unsupported.\n\nUse this function in the Uncommitted or Committed programming states.\nRefer to the `Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in\nthe *NI DC Power Supplies and SMUs Help* for more information about\nNI-DCPower programming states.\n\n**Related Topics**:\n\n`Advanced Sequence\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n\nniDCPower_CreateAdvancedSequenceStep\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the name of the sequence to create.'
                },
                'name': 'sequenceName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of attributes in the attributeIDs array.'
                },
                'name': 'attributeIdCount',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the attributes you reconfigure per step in the advanced\nsequence. The following table lists which attributes can be configured\nin an advanced sequence for each NI-DCPower device that supports\nadvanced sequencing. A ✓ indicates that the attribute can be configured\nin advanced sequencing. An ✕ indicates that the attribute cannot be\nconfigured in advanced sequencing.\n',
                    'table_body': [
                        [
                            'NIDCPOWER_ATTR_DC_NOISE_REJECTION',
                            '✓',
                            '✕',
                            '✓',
                            '✕',
                            '✓',
                            '✕',
                            '✕',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_APERTURE_TIME',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_SENSE',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_OVP_ENABLED',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_OVP_LIMIT',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_BIAS_DELAY',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_OFF_TIME',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_ON_TIME',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_SOURCE_DELAY',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY',
                            '✓',
                            '✕',
                            '✓',
                            '✕',
                            '✓',
                            '✕',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH',
                            '✓',
                            '✕',
                            '✓',
                            '✕',
                            '✓',
                            '✕',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO',
                            '✓',
                            '✕',
                            '✓',
                            '✕',
                            '✓',
                            '✕',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY',
                            '✓',
                            '✕',
                            '✓',
                            '✕',
                            '✓',
                            '✕',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH',
                            '✓',
                            '✕',
                            '✓',
                            '✕',
                            '✓',
                            '✕',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO',
                            '✓',
                            '✕',
                            '✓',
                            '✕',
                            '✓',
                            '✕',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_CURRENT_LEVEL',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_VOLTAGE_LIMIT',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_CURRENT_LIMIT',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_CURRENT_LIMIT_LOW',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_VOLTAGE_LEVEL',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_OUTPUT_ENABLED',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_OUTPUT_FUNCTION',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓'
                        ],
                        [
                            'NIDCPOWER_ATTR_OUTPUT_RESISTANCE',
                            '✓',
                            '✕',
                            '✓',
                            '✕',
                            '✓',
                            '✕',
                            '✓',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✕',
                            '✕',
                            '✕'
                        ],
                        [
                            'NIDCPOWER_ATTR_TRANSIENT_RESPONSE',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓',
                            '✓'
                        ]
                    ],
                    'table_header': [
                        'Attribute',
                        'PXIe-4135',
                        'PXIe-4136',
                        'PXIe-4137',
                        'PXIe-4138',
                        'PXIe-4139',
                        'PXIe-4140/4142/4144',
                        'PXIe-4141/4143/4145',
                        'PXIe-4162/4163'
                    ]
                },
                'name': 'attributeIds',
                'size': {
                    'mechanism': 'len',
                    'value': 'attributeIdCount'
                },
                'type': 'ViInt32[]'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies that this current sequence is active.'
                },
                'name': 'setAsActiveSequence',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateAdvancedSequenceCommitStepWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'setAsActiveStep',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateAdvancedSequenceStep': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCreates a new advanced sequence step in the advanced sequence specified\nby the Active advanced sequence. When you create an advanced sequence\nstep, each attribute you passed to the niDCPower_CreateAdvancedSequence\nfunction is reset to its default value for that step unless otherwise\nspecified.\n\n**Support for this Function**\n\nYou must set the source mode to Sequence to use this function.\n\nUsing the niDCPower_SetSequence function with Advanced Sequence\nfunctions is unsupported.\n\n**Related Topics**:\n\n`Advanced Sequence\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n\nniDCPower_CreateAdvancedSequence\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'default_value': True,
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies that this current step in the active sequence is active.'
                },
                'name': 'setAsActiveStep',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateAdvancedSequenceStepWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'setAsActiveStep',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'CreateAdvancedSequenceWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'sequenceName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'attributeIdCount',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'attributeIDs',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'in',
                'name': 'setAsActiveSequence',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteAdvancedSequence': {
        'documentation': {
            'description': '\nDeletes a previously created advanced sequence and all the advanced\nsequence steps in the advanced sequence.\n\n**Support for this Function**\n\nYou must set the source mode to Sequence to use this function.\n\nUsing the niDCPower_SetSequence function with Advanced Sequence\nfunctions is unsupported.\n\n**Related Topics**:\n\n`Advanced Sequence\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(advancedsequencemode)>`__\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'specifies the name of the sequence to delete.'
                },
                'name': 'sequenceName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DeleteAdvancedSequenceWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'sequenceName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'Disable': {
        'documentation': {
            'description': '\nThis function performs the same actions as the niDCPower_reset\nfunction, except that this function also immediately sets the\nNIDCPOWER_ATTR_OUTPUT_ENABLED attribute to VI_FALSE.\n\nThis function opens the output relay on devices that have an output\nrelay.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisablePulseTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nDisables the Pulse trigger. The device does not wait for a pulse trigger\nbefore performing a pulse operation. Refer to `Pulse\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(pulsemode)>`__ and `Sequence Source\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ for more information\nabout the Pulse trigger.\n\nThis function is necessary only if you configured a Pulse trigger in the\npast and now want to disable it.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisablePulseTriggerWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableSequenceAdvanceTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nDisables the Sequence Advance trigger. The device does not wait for a\nSequence Advance trigger before advancing to the next iteration of the\nsequence. Refer to the `Sequence Source\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ topic for more\ninformation about the Sequence Advance trigger.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableSequenceAdvanceTriggerWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableSourceTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nDisables the Source trigger. The device does not wait for a source\ntrigger before performing a source operation. Refer to the `Single Point\nSource Mode <REPLACE_DRIVER_SPECIFIC_URL_1(singlept)>`__ and `Sequence\nSource Mode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ topics for\nmore information about the Source trigger.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableSourceTriggerWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableStartTrigger': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nDisables the Start trigger. The device does not wait for a Start trigger\nwhen starting generation or acquisition.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'DisableStartTriggerWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'EnableSequenceInstructionCapturing': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'enable',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'EraseFlashEepromSector': {
        'codegen_method': 'no',
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
                'name': 'address',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ErrorQuery': {
        'codegen_method': 'no',
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
                'direction': 'out',
                'name': 'errorCode',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'errorMessage',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViString[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportAttributeConfigurationBuffer': {
        'documentation': {
            'description': '\nExports the attribute configuration of the session to the specified\nconfiguration buffer.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers and the same number of configured\nchannels.\n\nThis function verifies that the attributes you have configured for the\nsession are valid. If the configuration is invalid, NI‑DCPower returns\nan error.\n\n**Support for this Function**\n\nCalling this function in `Sequence Source\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.\n\n**Channel Mapping Behavior for Multichannel Sessions**\n\nWhen importing and exporting session attribute configurations between\nNI‑DCPower sessions that were initialized with different channels, the\nconfigurations of the exporting channels are mapped to the importing\nchannels in the order you specify in the **channelName** input to the\nniDCPower_InitializeWithChannels function.\n\nFor example, if your entry for **channelName** is 0,1 for the exporting\nsession and 1,2 for the importing session:\n\n-  The configuration exported from channel 0 is imported into channel 1.\n-  The configuration exported from channel 1 is imported into channel 2.\n\n**Related Topics:**\n\n`Using Properties and\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__\n\n`Setting Properties and Attributes Before Reading\nThem <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': '\nThis function will return an error if the total number of channels\ninitialized for the exporting session is not equal to the total number\nof channels initialized for the importing session.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
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
            'description': '\nExports the attribute configuration of the session to the specified\nfile.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers and the same number of configured\nchannels.\n\nThis function verifies that the attributes you have configured for the\nsession are valid. If the configuration is invalid, NI‑DCPower returns\nan error.\n\n**Support for this Function**\n\nCalling this function in `Sequence Source\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.\n\n**Channel Mapping Behavior for Multichannel Sessions**\n\nWhen importing and exporting session attribute configurations between\nNI‑DCPower sessions that were initialized with different channels, the\nconfigurations of the exporting channels are mapped to the importing\nchannels in the order you specify in the **channelName** input to the\nniDCPower_InitializeWithChannels function.\n\nFor example, if your entry for **channelName** is 0,1 for the exporting\nsession and 1,2 for the importing session:\n\n-  The configuration exported from channel 0 is imported into channel 1.\n-  The configuration exported from channel 1 is imported into channel 2.\n\n**Related Topics:**\n\n`Using Properties and\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__\n\n`Setting Properties and Attributes Before Reading\nThem <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': '\nThis function will return an error if the total number of channels\ninitialized for the exporting session is not equal to the total number\nof channels initialized for the importing session.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute path to the file to contain the exported\nattribute configuration. If you specify an empty or relative path, this\nfunction returns an error.\n**Default file extension:** .nidcpowerconfig\n'
                },
                'name': 'filePath',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportSignal': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nRoutes signals (triggers and events) to the output terminal you specify.\nThe route is created when the session is niDCPower_Commit.\n\n**Related Topics:**\n\n`Triggers <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies which trigger or event to export.\n**Defined Values:**\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_SOURCE_COMPLETE_EVENT (1030)',
                            'Exports the Source Complete event.'
                        ],
                        [
                            'NIDCPOWER_VAL_MEASURE_COMPLETE_EVENT (1031)',
                            'Exports the Measure Complete event.'
                        ],
                        [
                            'NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE_EVENT (1032)',
                            'Exports the Sequence Iteration Complete event.'
                        ],
                        [
                            'NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE_EVENT (1033)',
                            'Exports the Sequence Engine Done event.'
                        ],
                        [
                            'NIDCPOWER_VAL_PULSE_COMPLETE_EVENT (1051)',
                            'Exports the Pulse Complete event.'
                        ],
                        [
                            'NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER_EVENT (1052)',
                            'Exports the Ready Pulse Trigger event.'
                        ],
                        [
                            'NIDCPOWER_VAL_START_TRIGGER (1034)',
                            'Exports the Start trigger.'
                        ],
                        [
                            'NIDCPOWER_VAL_SOURCE_TRIGGER (1035)',
                            'Exports the Source trigger.'
                        ],
                        [
                            'NIDCPOWER_VAL_MEASURE_TRIGGER (1036)',
                            'Exports the Measure trigger.'
                        ],
                        [
                            'NIDCPOWER_VAL_SEQUENCE_ADVANCE_TRIGGER (1037)',
                            'Exports the Sequence Advance trigger.'
                        ],
                        [
                            'NIDCPOWER_VAL_PULSE_TRIGGER (1053)',
                            'Exports the Pulse trigger.'
                        ]
                    ]
                },
                'enum': 'ExportSignal',
                'name': 'signal',
                'type': 'ViInt32'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': 'Reserved for future use. Pass in an empty string for this parameter.'
                },
                'name': 'signalIdentifier',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies where to export the selected signal.\n**Relative Terminals**:\n',
                    'table_body': [
                        [
                            '""',
                            'Do not export signal'
                        ],
                        [
                            '"PXI_Trig0"',
                            'PXI trigger line 0'
                        ],
                        [
                            '"PXI_Trig1"',
                            'PXI trigger line 1'
                        ],
                        [
                            '"PXI_Trig2"',
                            'PXI trigger line 2'
                        ],
                        [
                            '"PXI_Trig3"',
                            'PXI trigger line 3'
                        ],
                        [
                            '"PXI_Trig4"',
                            'PXI trigger line 4'
                        ],
                        [
                            '"PXI_Trig5"',
                            'PXI trigger line 5'
                        ],
                        [
                            '"PXI_Trig6"',
                            'PXI trigger line 6'
                        ],
                        [
                            '"PXI_Trig7"',
                            'PXI trigger line 7'
                        ]
                    ]
                },
                'name': 'outputTerminal',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ExportSignalWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'signal',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'signalIdentifier',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'outputTerminal',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'FancyCreateAdvancedSequence': {
        'codegen_method': 'python-only',
        'returns': 'ViStatus',
        'python_name': 'create_advanced_sequence',
        'method_templates': [
            { 'session_filename': 'fancy_advanced_sequence', 'documentation_filename': 'default_method', 'method_python_name_suffix': '', },
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.',
                },
            },
            {
                'direction': 'in',
                'name': 'SequenceName',
                'type': 'ViString',
                'documentation': {
                    'description': 'Name of sequence.',
                },
            },
            {
                'direction': 'in',
                'name': 'Sequence',
                'type': 'ViInt32[]',  # Doesn't matter here
                'documentation': {
                    'description': 'Sequence.',
                },
            },
            {
                'direction': 'in',
                'name': 'setAsActiveSequence',
                'type': 'ViBoolean',
                'default_value': True,
                'documentation': { 'description': 'Specifies that this current sequence is active.', },
            },
        ],
        'documentation':
        {
            'description': 'Test.',
            'note': 'Test.',
        },
    },
    'FancyFetchMultiple': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nReturns a list of named tuples (Measurement) that were\npreviously taken and are stored in the NI-DCPower buffer. This function\nshould not be used when the NIDCPOWER_ATTR_MEASURE_WHEN attribute is\nset to NIDCPOWER_VAL_ON_DEMAND. You must first call\nniDCPower_Initiate before calling this function.\n\nFields in Measurement:\n\n- **voltage** (float)\n- **current** (float)\n- **in_compliance** (bool)\n\n',
            'note': 'This function is not supported on all devices. Refer to `Supported Functions by Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm, supportedfunctions)>`__ for more information about supported devices.'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_fetch'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitializeWithChannels function.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of measurements to fetch.'
                },
                'name': 'count',
                'type': 'ViInt32'
            },
            {
                'default_value': 'datetime.timedelta(seconds=1.0)',
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the maximum time allowed for this function to complete. If the function does not complete within this time interval, NI-DCPower returns an error.',
                    'note': 'When setting the timeout interval, ensure you take into account any triggers so that the timeout interval is long enough for your application.'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nList of named tuples with fields:\n\n- **voltage** (float)\n- **current** (float)\n- **in_compliance** (bool)\n'
                },
                'name': 'measurements',
                'python_type': 'Measurement',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'ViReal64[]'
            }
        ],
        'python_name': 'fetch_multiple',
        'returns': 'ViStatus'
    },
    'FancyMeasureMultiple': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nReturns a list of named tuples (Measurement) containing the measured voltage\nand current values on the specified output channel(s). Each call to this function\nblocks other function calls until the measurements are returned from the device.\nThe order of the measurements returned in the array corresponds to the order\non the specified output channel(s).\n\nFields in Measurement:\n\n- **voltage** (float)\n- **current** (float)\n- **in_compliance** (bool) - Always None\n\n',
            'note': 'This function is not supported on all devices. Refer to `Supported Functions by Device <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm, supportedfunctions)>`__ for more information about supported devices.'
        },
        'method_templates': [
            {
                'documentation_filename': 'default_method',
                'method_python_name_suffix': '',
                'session_filename': 'fancy_fetch'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitializeWithChannels function.'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nList of named tuples with fields:\n\n- **voltage** (float)\n- **current** (float)\n- **in_compliance** (bool) - Always None\n'
                },
                'name': 'measurements',
                'python_type': 'Measurement',
                'size': {
                    'mechanism': 'python-code',
                    'value': None
                },
                'type': 'ViReal64[]'
            }
        ],
        'python_name': 'measure_multiple',
        'returns': 'ViStatus'
    },
    'FetchMultiple': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns an array of voltage measurements, an array of current\nmeasurements, and an array of compliance measurements that were\npreviously taken and are stored in the NI-DCPower buffer. This function\nshould not be used when the NIDCPOWER_ATTR_MEASURE_WHEN attribute is\nset to NIDCPOWER_VAL_ON_DEMAND. You must first call\nniDCPower_Initiate before calling this function.\n\nRefer to the `Acquiring\nMeasurements <REPLACE_DRIVER_SPECIFIC_URL_1(acquiringmeasurements)>`__\nand `Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__ topics in\nthe *NI DC Power Supplies and SMUs Help* for more information about\nconfiguring this function.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'method_name_for_documentation': 'fetch_multiple',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the maximum time allowed for this function to complete, in\nseconds. If the function does not complete within this time interval,\nNI-DCPower returns an error.\n',
                    'note': '\nWhen setting the timeout interval, ensure you take into account any\ntriggers so that the timeout interval is long enough for your\napplication.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the number of measurements to fetch.'
                },
                'name': 'count',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of voltage measurements. Ensure that sufficient space\nhas been allocated for the returned array.\n'
                },
                'name': 'voltageMeasurements',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'count'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of current measurements. Ensure that sufficient space\nhas been allocated for the returned array.\n'
                },
                'name': 'currentMeasurements',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'count'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of Boolean values indicating whether the output was in\ncompliance at the time the measurement was taken. Ensure that sufficient\nspace has been allocated for the returned array.\n'
                },
                'name': 'inCompliance',
                'size': {
                    'mechanism': 'passed-in',
                    'value': 'count'
                },
                'type': 'ViBoolean[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nIndicates the number of measured values actually retrieved from the\ndevice.\n'
                },
                'name': 'actualCount',
                'type': 'ViInt32',
                'use_in_python_api': False
            }
        ],
        'returns': 'ViStatus'
    },
    'FreeServer': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeFlags': {
        'codegen_method': 'no',
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
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'name': 'attributeFlags',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'attributeSupported',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\n| Queries the value of a ViBoolean attribute.\n| You can use this function to get the values of device-specific\n  attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Help text is shown for each attribute.\n   Select an attribute by double-clicking on it or by selecting it and\n   then pressing **Enter**.\n-  A ring control at the top of the dialog box allows you to see all IVI\n   attributes or only the attributes of type ViBoolean. If you choose to\n   see all IVI attributes, the data types appear to the right of the\n   attribute names in the list box. Attributes with data types other\n   than ViBoolean are dim. If you select an attribute data type that is\n   dim, LabWindows/CVI transfers you to the function panel for the\n   corresponding function that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Passes the address of a\nViBoolean variable.\nIf the attribute currently showing in the attribute ring control has\nconstants as valid values, you can view a list of the constants by\npressing **Enter** on this control. Select a value by double-clicking on\nit or by selecting it and then pressing **Enter**.\n'
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
            'description': '\n| Queries the value of a ViInt32 attribute.\n| You can use this function to get the values of device-specific\n  attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Help text is shown for each attribute.\n   Select an attribute by double-clicking on it or by selecting it and\n   then pressing **Enter**.\n-  A ring control at the top of the dialog box allows you to see all IVI\n   attributes or only the attributes of type ViInt32. If you choose to\n   see all IVI attributes, the data types appear to the right of the\n   attribute names in the list box. Attributes with data types other\n   than ViInt32 are dim. If you select an attribute data type that is\n   dim, LabWindows/CVI transfers you to the function panel for the\n   corresponding function that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Passes the address of a\nViInt32 variable.\nIf the attribute currently showing in the attribute ring control has\nconstants as valid values, you can view a list of the constants by\npressing **Enter** on this control. Select a value by double-clicking on\nit or by selecting it and then pressing **Enter**.\n'
                },
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetAttributeViInt64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\n| Queries the value of a ViInt64 attribute.\n| You can use this function to get the values of device-specific\n  attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Help text is shown for each attribute.\n   Select an attribute by double-clicking on it or by selecting it and\n   then pressing **Enter**.\n-  A ring control at the top of the dialog box allows you to see all IVI\n   attributes or only the attributes of type ViReal64. If you choose to\n   see all IVI attributes, the data types appear to the right of the\n   attribute names in the list box. Attributes with data types other\n   than ViReal64 are dim. If you select an attribute data type that is\n   dim, LabWindows/CVI transfers you to the function panel for the\n   corresponding function that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Passes the address of a\nViReal64 variable.\nIf the attribute currently showing in the attribute ring control has\nconstants as valid values, you can view a list of the constants by\npressing **Enter** on this control. Select a value by double-clicking on\nit or by selecting it and then pressing **Enter**.\n'
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
            'description': '\n| Queries the value of a ViReal64 attribute.\n| You can use this function to get the values of device-specific\n  attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Help text is shown for each attribute.\n   Select an attribute by double-clicking on it or by selecting it and\n   then pressing **Enter**.\n-  A ring control at the top of the dialog box allows you to see all IVI\n   attributes or only the attributes of type ViReal64. If you choose to\n   see all IVI attributes, the data types appear to the right of the\n   attribute names in the list box. Attributes with data types other\n   than ViReal64 are dim. If you select an attribute data type that is\n   dim, LabWindows/CVI transfers you to the function panel for the\n   corresponding function that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Passes the address of a\nViReal64 variable.\nIf the attribute currently showing in the attribute ring control has\nconstants as valid values, you can view a list of the constants by\npressing **Enter** on this control. Select a value by double-clicking on\nit or by selecting it and then pressing **Enter**.\n'
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
            'description': '\n| Queries the value of a ViSession attribute.\n| You can use this function to get the values of device-specific\n  attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Help text is shown for each attribute.\n   Select an attribute by double-clicking on it or by selecting it and\n   then pressing **Enter**.\n-  A ring control at the top of the dialog box allows you to see all IVI\n   attributes or only the attributes of type ViSession. If you choose to\n   see all IVI attributes, the data types appear to the right of the\n   attribute names in the list box. Attributes with data types other\n   than ViSession are dim. If you select an attribute data type that is\n   dim, LabWindows/CVI transfers you to the function panel for the\n   corresponding function that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the current value of the attribute. Passes the address of a\nViSession variable.\nIf the attribute currently showing in the attribute ring control has\nconstants as valid values, you can view a list of the constants by\npressing **Enter** on this control. Select a value by double-clicking on\nit or by selecting it and then pressing **Enter**.\n'
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
            'description': '\n| Queries the value of a ViString attribute.\n| You can use this function to get the values of device-specific\n  attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press or the\n   spacebar to display a dialog box containing hierarchical list of the\n   available attributes. Help text is shown for each attribute. Select\n   an attribute by double-clicking on it or by selecting it and then\n   pressing .\n-  A ring control at the top of the dialog box allows you to see all IVI\n   attributes or only the attributes of type ViString. If you choose to\n   see all IVI attributes, the data types appear to the right of the\n   attribute names in the list box. Attributes with data types other\n   than ViString are dimmed. If you select an attribute data type that\n   is dimmed, LabWindows/CVI transfers you to the function panel for the\n   corresponding function that is consistent with the data type.\n-  If you want to enter a variable name, press to change this ring\n   control to a manual input control. If the attribute in this ring\n   control has named constants as valid values, you can view the\n   constants by moving to the value control and pressing .\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nPasses the number of bytes in the buffer and specifies the number of\nbytes in the ViChar array you specify for **value**. If the current\nvalue of **value**, including the terminating NUL byte, is larger than\nthe size you indicate in this parameter, the function copies (buffer\nsize - 1) bytes into the buffer, places an ASCII NUL byte at the end of\nthe buffer, and returns the buffer size you must pass to get the entire\nvalue. For example, if the value is 123456 and the buffer size is 4, the\nfunction places 123 into the buffer and returns 7.\nTo obtain the required buffer size, you can pass 0 for this attribute\nand VI_NULL for **value**. If you want the function to fill in the\nbuffer regardless of the number of bytes in the value, pass a negative\nnumber for this attribute.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nThe buffer in which the function returns the current value of the\nattribute. The buffer must be of type ViChar and have at least as many\nbytes as indicated in **bufSize**.\nIf the current value of the attribute, including the terminating NUL\nbyte, contains more bytes that you indicate in this attribute, the\nfunction copies (buffer size -1) bytes into the buffer, places an ASCII\nNUL byte at the end of the buffer, and returns the buffer size you must\npass to get the entire value. For example, if the value is 123456 and\nthe buffer size is 4, the function places 123 into the buffer and\nreturns 7.\nIf you specify 0 for **bufSize**, you can pass VI_NULL for this\nattribute.\nIf the attribute currently showing in the attribute ring control has\nconstants as valid values, you can view a list of the constants by\npressing on this control. Select a value by double-clicking on it or by\nselecting it and then pressing .\n'
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
                'type': 'ViString[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetCalUserDefinedInfo': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'Returns the user-defined information in the device onboard EEPROM.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the user-defined information stored in the device onboard\nEEPROM.\n'
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
            'description': '\nReturns the maximum number of characters that can be used to store\nuser-defined information in the device onboard EEPROM.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the number of characters that can be stored in the device\nonboard EEPROM.\n'
                },
                'name': 'infoSize',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetChannelName': {
        'documentation': {
            'description': '\nRetrieves the output **channelName** that corresponds to the requested\n**index**. Use the NIDCPOWER_ATTR_CHANNEL_COUNT attribute to\ndetermine the upper bound of valid values for **index**.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies which output channel name to return. The index values begin at\n1.\n'
                },
                'name': 'index',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of bytes in the ViChar array you specify for\n**channelName**. If the **channelName**, including the terminating NUL\nbyte, contains more bytes than you indicate in this attribute, the\nfunction copies (buffer size - 1) bytes into the buffer, places an ASCII\nNUL byte at the end of the buffer, and returns the buffer size you must\npass to get the entire value. For example, if the value is 123456 and\nthe buffer size is 4, the function places 123 into the buffer and\nreturns 7.\nIf you pass 0, you can pass VI_NULL for **channelName**.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the output channel name that corresponds to **index**.'
                },
                'name': 'channelName',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetChannelNameFromString': {
        'codegen_method': 'no',
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
                'name': 'index',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'channelName',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetDeviceSessionState': {
        'codegen_method': 'no',
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
                'direction': 'out',
                'name': 'sessionState',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetError': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\n| Retrieves and then clears the IVI error information for the session or\n  the current execution thread unless **bufferSize** is 0, in which case\n  the function does not clear the error information. By passing 0 for\n  the buffer size, you can ascertain the buffer size required to get the\n  entire error description string and then call the function again with\n  a sufficiently large buffer size.\n| If the user specifies a valid IVI session for **vi**, this function\n  retrieves and then clears the error information for the session. If\n  the user passes VI_NULL for **vi**, this function retrieves and then\n  clears the error information for the current execution thread. If\n  **vi** is an invalid session, the function does nothing and returns an\n  error. Normally, the error information describes the first error that\n  occurred since the user last called niDCPower_GetError or\n  niDCPower_ClearError.\n'
        },
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the error code for the session or execution thread.'
                },
                'name': 'code',
                'type': 'ViStatus'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of bytes in the ViChar array you specify for\n**description**.\nIf the error description, including the terminating NUL byte, contains\nmore bytes than you indicate in this attribute, the function copies\n(buffer size - 1) bytes into the buffer, places an ASCII NUL byte at the\nend of the buffer, and returns the buffer size you must pass to get the\nentire value. For example, if the value is 123456 and the buffer size is\n4, the function places 123 into the buffer and returns 7.\nIf you pass 0 for this attribute, you can pass VI_NULL for\n**description**.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the error description for the IVI session or execution thread.\nIf there is no description, the function returns an empty string.\nThe buffer must contain at least as many elements as the value you\nspecify with **bufferSize**. If the error description, including the\nterminating NUL byte, contains more bytes than you indicate with\n**bufferSize**, the function copies (buffer size - 1) bytes into the\nbuffer, places an ASCII NUL byte at the end of the buffer, and returns\nthe buffer size you must pass to get the entire value. For example, if\nthe value is 123456 and the buffer size is 4, the function places 123\ninto the buffer and returns 7.\nIf you pass 0 for **bufferSize**, you can pass VI_NULL for this\nattribute.\n'
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
    'GetExtCalLastDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the date and time of the last successful calibration. The time\nreturned is 24-hour (military) local time; for example, if the device\nwas calibrated at 2:30 PM, this function returns 14 for **hours** and 30\nfor **minutes**.\n'
        },
        'method_name_for_documentation': 'get_ext_cal_last_date_and_time',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **year** the device was last calibrated.'
                },
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **month** in which the device was last calibrated.'
                },
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **day** on which the device was last calibrated.'
                },
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the **hour** (in 24-hour time) in which the device was last\ncalibrated.\n'
                },
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **minute** in which the device was last calibrated.'
                },
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalLastTemp': {
        'documentation': {
            'description': '\nReturns the onboard **temperature** of the device, in degrees Celsius,\nduring the last successful external calibration.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the onboard **temperature** of the device, in degrees Celsius,\nduring the last successful external calibration.\n'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetExtCalRecommendedInterval': {
        'documentation': {
            'description': '\nReturns the recommended maximum interval, in **months**, between\nexternal calibrations.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nSpecifies the recommended maximum interval, in **months**, between\nexternal calibrations.\n'
                },
                'name': 'months',
                'python_api_converter_name': 'convert_month_to_timedelta',
                'type': 'ViInt32',
                'type_in_documentation': 'datetime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetLastExtCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the date and time of the last successful calibration.'
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
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.'
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
    'GetLastRetrievedMeasurement': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'voltageMeasurements',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'currentMeasurements',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'inCompliance',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViBoolean[]'
            },
            {
                'direction': 'in',
                'name': 'changeCounter',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViUInt64[]'
            },
            {
                'direction': 'in',
                'name': 'outputFunction',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViInt32[]'
            },
            {
                'direction': 'out',
                'name': 'reserved',
                'type': 'void'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetLastSelfCalLastDateAndTime': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': 'Returns the date and time of the oldest successful self-calibration from among the channels in the session.',
            'note': 'This function is not supported on all devices.'
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
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.'
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
    'GetLiveMeasurements': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'voltageMeasurement',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'currentMeasurement',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'inCompliance',
                'type': 'ViBoolean'
            },
            {
                'direction': 'out',
                'name': 'apertureTime',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'name': 'reserved',
                'type': 'void'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetMeasureEngineState': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'measureEngineState',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetNextCoercionRecord': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nReturns the coercion information associated with the IVI session and\nclears the earliest instance in which NI-DCPower coerced a value you\nspecified.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of bytes in the ViChar array you specify for\n**coercionRecord**. If the next coercion record string, including the\nterminating NUL byte, contains more bytes than you indicate in this\nattribute, the function copies (buffer size - 1) bytes into the buffer,\nplaces an ASCII NUL byte at the end of the buffer, and returns the\nbuffer size you must pass to get the entire value. For example, if the\nvalue is 123456 and the buffer size is 4, the function places 123 into\nthe buffer and returns 7.\nIf you pass 0, you can pass VI_NULL for **coercionRecord**.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the next **coercionRecord** for the IVI session. If there are no\n**coercionRecords**, the function returns an empty string.\n'
                },
                'name': 'coercionRecord',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetNextInterchangeWarning': {
        'codegen_method': 'no',
        'documentation': {
            'description': '\nThis function returns the interchangeability warning associated with the\nIVI session. It retrieves and clears the earliest instance in which the\nclass driver recorded an interchangeability warning. Interchangeability\nwarnings indicate that using your application with a different device\nmay cause a different behavior.\n\nNI-DCPower performs interchangeability checking when the\nNIDCPOWER_ATTR_INTERCHANGE_CHECK attribute is set to VI_TRUE. This\nfunction returns an empty string in warning if no interchangeability\nwarnings remain for the session. In general, NI-DCPower generates\ninterchangeability warnings when an attribute that affects the behavior\nof the device is in a state that you did not specify.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the number of bytes in the ViChar array you specify for\n**interchangeWarning**. If the next interchangeability warning string,\nincluding the terminating NUL byte, contains more bytes than you\nindicate in this attribute, the function copies (buffer size - 1) bytes\ninto the buffer, places an ASCII NUL byte at the end of the buffer, and\nreturns the buffer size you must pass to get the entire value. For\nexample, if the value is 123456 and the buffer size is 4, the function\nplaces 123 into the buffer and returns 7.\nIf you pass 0, you can pass VI_NULL for **interchangeWarning**.\n'
                },
                'name': 'bufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the next interchange warning for the IVI session. If there are\nno interchange warnings, the function returns an empty string.\n'
                },
                'name': 'interchangeWarning',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'bufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetOpenSessionsInformation': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
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
    'GetReservedResourcesForDevice': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'out',
                'name': 'reservedResourcesBitmapsActualSize',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'name': 'reservedResourcesBitmaps',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViUInt64[]'
            },
            {
                'direction': 'out',
                'name': 'allResourcesReserved',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalLastDateAndTime': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns the date and time of the oldest successful self-calibration from\namong the channels in the session.\n\nThe time returned is 24-hour (military) local time; for example, if you\nhave a session using channels 1 and 2, and a self-calibration was\nperformed on channel 1 at 2:30 PM, and a self-calibration was performed\non channel 2 at 3:00 PM on the same day, this function returns 14 for\n**hours** and 30 for **minutes**.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'method_name_for_documentation': 'get_self_cal_last_date_and_time',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **year** the device was last calibrated.'
                },
                'name': 'year',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **month** in which the device was last calibrated.'
                },
                'name': 'month',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **day** on which the device was last calibrated.'
                },
                'name': 'day',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the **hour** (in 24-hour time) in which the device was last\ncalibrated.\n'
                },
                'name': 'hour',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the **minute** in which the device was last calibrated.'
                },
                'name': 'minute',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSelfCalLastTemp': {
        'documentation': {
            'description': '\nReturns the onboard temperature of the device, in degrees Celsius,\nduring the oldest successful self-calibration from among the channels in\nthe session.\n\nFor example, if you have a session using channels 1 and 2, and you\nperform a self-calibration on channel 1 with a device temperature of 25\ndegrees Celsius at 2:00, and a self-calibration was performed on channel\n2 at 27 degrees Celsius at 3:00 on the same day, this function returns\n25 for the **temperature** parameter.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the onboard **temperature** of the device, in degrees Celsius,\nduring the oldest successful calibration.\n'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSequenceEngineState': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'sequencerState',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetSequenceStep': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'stepNumber',
                'type': 'ViUInt32'
            },
            {
                'direction': 'out',
                'name': 'hasSequenceStarted',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetTriggerState': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'waitingTriggerState',
                'type': 'ViUInt16'
            },
            {
                'direction': 'out',
                'name': 'missedTriggerState',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'GetTriggerStateByName': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'triggerName',
                'type': 'ViUInt16'
            },
            {
                'direction': 'out',
                'name': 'waitingTriggerState',
                'type': 'ViUInt16'
            },
            {
                'direction': 'out',
                'name': 'missedTriggerState',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'ImportAttributeConfigurationBuffer': {
        'documentation': {
            'description': '\nImports an attribute configuration to the session from the specified\nconfiguration buffer.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers and the same number of configured\nchannels.\n\n**Support for this Function**\n\nCalling this function in `Sequence Source\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.\n\n**Channel Mapping Behavior for Multichannel Sessions**\n\nWhen importing and exporting session attribute configurations between\nNI‑DCPower sessions that were initialized with different channels, the\nconfigurations of the exporting channels are mapped to the importing\nchannels in the order you specify in the **channelName** input to the\nniDCPower_InitializeWithChannels function.\n\nFor example, if your entry for **channelName** is 0,1 for the exporting\nsession and 1,2 for the importing session:\n\n-  The configuration exported from channel 0 is imported into channel 1.\n-  The configuration exported from channel 1 is imported into channel 2.\n\n**Related Topics:**\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n\n`Using Properties and\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__\n\n`Setting Properties and Attributes Before Reading\nThem <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': '\nThis function will return an error if the total number of channels\ninitialized for the exporting session is not equal to the total number\nof channels initialized for the importing session.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
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
            'description': '\nImports an attribute configuration to the session from the specified\nfile.\n\nYou can export and import session attribute configurations only between\ndevices with identical model numbers and the same number of configured\nchannels.\n\n**Support for this Function**\n\nCalling this function in `Sequence Source\nMode <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ is unsupported.\n\n**Channel Mapping Behavior for Multichannel Sessions**\n\nWhen importing and exporting session attribute configurations between\nNI‑DCPower sessions that were initialized with different channels, the\nconfigurations of the exporting channels are mapped to the importing\nchannels in the order you specify in the **channelName** input to the\nniDCPower_InitializeWithChannels function.\n\nFor example, if your entry for **channelName** is 0,1 for the exporting\nsession and 1,2 for the importing session:\n\n-  The configuration exported from channel 0 is imported into channel 1.\n-  The configuration exported from channel 1 is imported into channel 2.\n\n**Related Topics:**\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n\n`Using Properties and\nAttributes <REPLACE_DRIVER_SPECIFIC_URL_1(using_properties_and_attributes)>`__\n\n`Setting Properties and Attributes Before Reading\nThem <REPLACE_DRIVER_SPECIFIC_URL_1(setting_before_reading_attributes)>`__\n',
            'note': '\nThis function will return an error if the total number of channels\ninitialized for the exporting session is not equal to the total number\nof channels initialized for the importing session.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the absolute path to the file containing the attribute\nconfiguration to import. If you specify an empty or relative path, this\nfunction returns an error.\n**Default File Extension:** .nidcpowerconfig\n'
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
            'description': '\nIf **password** is valid, this function creates a new IVI instrument\ndriver session to the device specified in **resourceName** and returns\nan instrument handle you use to identify the device in all subsequent\nNI-DCPower function calls. This function also sends initialization\ncommands to set the device to the state necessary for the operation of\nNI-DCPower.\n\nOpening a calibration session always performs a reset. Refer to the\ncalibration procedure for the device you are calibrating for detailed\ninstructions on the appropriate use of this function. This function uses\nthe `deprecated programming state\nmodel <REPLACE_DRIVER_SPECIFIC_URL_1(initializedeprecatedmodel)>`__.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **resourceName** assigned by Measurement & Automation\nExplorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an\ninstrument\'s **resourceName**. **resourceName** can also be a logical\nIVI name.\n'
                },
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **password** for opening a calibration session. The\ninitial password is factory configured to "NI". **password** can be a\nmaximum of four alphanumeric characters.\n'
                },
                'name': 'password',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a handle that you use to identify the session in all subsequent\nNI-DCPower function calls.\n'
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
            'description': '\nThis function is deprecated. Use niDCPower_InitializeWithChannels\ninstead.\n\nCreates a new IVI instrument driver session to the device specified in\n**resourceName** and returns a session handle you use to identify the\ndevice in all subsequent NI-DCPower function calls. With this function,\nyou can optionally set the initial state of the following session\nattributes:\n\n-  NIDCPOWER_ATTR_SIMULATE\n-  NIDCPOWER_ATTR_DRIVER_SETUP\n-  NIDCPOWER_ATTR_RANGE_CHECK\n-  NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS\n-  NIDCPOWER_ATTR_CACHE\n-  NIDCPOWER_ATTR_RECORD_COERCIONS\n\nThis function also sends initialization commands to set the device to\nthe state necessary for NI-DCPower to operate.\n\nTo place the device in a known start-up state when creating a new\nsession, set **resetDevice** to VI_TRUE. This action is equivalent to\nusing the niDCPower_reset function.\n\nTo open a session and leave the device in its existing configuration\nwithout passing through a transitional output state, set **resetDevice**\nto VI_FALSE, and immediately call the niDCPower_Abort function. Then\nconfigure the device as in the previous session changing only the\ndesired settings, and then call the niDCPower_Initiate function.\n\nRefer to the `deprecated programming state\nmodel <REPLACE_DRIVER_SPECIFIC_URL_1(initializedeprecatedmodel)>`__ for\ninformation about the specific software states.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **resourceName** assigned by Measurement & Automation\nExplorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an\ninstrument\'s **resourceName**. **resourceName** can also be a logical\nIVI name.\n'
                },
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether the device is queried to determine if the device is a\nvalid instrument for NI-DCPower.\n'
                },
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to reset the device during the initialization\nprocedure.\n'
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the initial value of certain attributes for the session. The\nsyntax for **optionString** is a list of attributes with an assigned\nvalue where 1 is VI_TRUE and 0 is VI_FALSE. Each attribute/value\ncombination is delimited with a comma, as shown in the following\nexample:\n\n"Simulate=0,RangeCheck=1,QueryInstrStatus=0,Cache=1"\n\nIf you do not wire this input or pass an empty string, the session\nassigns the default values, shown in the example, for these attributes.\nYou do not have to specify a value for all the attributes. If you do not\nspecify a value for an attribute, the default value is used.\n\nFor more information about simulating a device, refer to `Simulating a\nPower Supply or SMU <REPLACE_DRIVER_SPECIFIC_URL_1(simulate)>`__.\n'
                },
                'name': 'optionString',
                'type': 'ViString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a handle that you use to identify the device in all subsequent\nNI-DCPower function calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitializeSessionForServer': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
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
            'description': '\nCreates and returns a new NI-DCPower session to the power supply or SMU\nspecified in **resource name** to be used in all subsequent NI-DCPower\nfunction calls. With this function, you can optionally set the initial\nstate of the following session attributes:\n\n-  NIDCPOWER_ATTR_SIMULATE\n-  NIDCPOWER_ATTR_DRIVER_SETUP\n\nAfter calling this function, the session will be in the Uncommitted\nstate. Refer to the `Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for\ndetails about specific software states.\n\nTo place the device in a known start-up state when creating a new\nsession, set **reset** to VI_TRUE. This action is equivalent to using\nthe niDCPower_reset function immediately after initializing the\nsession.\n\nTo open a session and leave the device in its existing configuration\nwithout passing through a transitional output state, set **reset** to\nVI_FALSE. Then configure the device as in the previous session,\nchanging only the desired settings, and then call the\nniDCPower_Initiate function.\n\n**Related Topics:**\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n'
        },
        'method_name_for_documentation': '__init__',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **resourceName** assigned by Measurement & Automation\nExplorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an\ninstrument\'s **resourceName**. **resourceName** can also be a logical\nIVI name.\n'
                },
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'default_value': None,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies which output channel(s) to include in a new session. Specify\nmultiple channels by using a channel list or a channel range. A channel\nlist is a comma (,) separated sequence of channel names (for example,\n0,2 specifies channels 0 and 2). A channel range is a lower bound\nchannel followed by a hyphen (-) or colon (:) followed by an upper bound\nchannel (for example, 0-2 specifies channels 0, 1, and 2). In the\nRunning state, multiple output channel configurations are performed\nsequentially based on the order specified in this parameter. If you do\nnot specify any channels, by default all channels on the device are\nincluded in the session.\n'
                },
                'is_repeated_capability': False,
                'name': 'channels',
                'python_api_converter_name': 'convert_repeated_capabilities_from_init',
                'type': 'ViConstString',
                'type_in_documentation': 'str, list, range, tuple'
            },
            {
                'default_value': False,
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to reset the device during the initialization\nprocedure.\n'
                },
                'name': 'reset',
                'type': 'ViBoolean'
            },
            {
                'default_value': '""',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the initial value of certain attributes for the session. The\nsyntax for **optionString** is a list of attributes with an assigned\nvalue where 1 is VI_TRUE and 0 is VI_FALSE. For example:\n\n"Simulate=0"\n\nYou do not have to specify a value for all the attributes. If you do not\nspecify a value for an attribute, the default value is used.\n\nFor more information about simulating a device, refer to `Simulating a\nPower Supply or SMU <REPLACE_DRIVER_SPECIFIC_URL_1(simulate)>`__.\n'
                },
                'name': 'optionString',
                'python_api_converter_name': 'convert_init_with_options_dictionary',
                'type': 'ViConstString',
                'type_in_documentation': 'dict'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a session handle that you use to identify the device in all\nsubsequent NI-DCPower function calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus',
        'use_session_lock': False
    },
    'InitializeWithIndependentChannels': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'name': 'reset',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'name': 'optionString',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'Initiate': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nStarts generation or acquisition, causing the NI-DCPower session to\nleave the Uncommitted state or Committed state and enter the Running\nstate. To return to the Committed state call the niDCPower_Abort\nfunction. Refer to the `Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in\nthe *NI DC Power Supplies and SMUs Help* for information about the\nspecific NI-DCPower software states.\n\n**Related Topics:**\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n'
        },
        'method_name_for_documentation': 'initiate',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'InitiateWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'InvalidateAllAttributes': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
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
        'documentation': {
            'description': 'TBD'
        },
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
            'description': '\n| Obtains a multithread lock on the device session. Before doing so, the\n  software waits until all other execution threads release their locks\n  on the device session.\n| Other threads may have obtained a lock on this session for the\n  following reasons:\n\n-  The application called the niDCPower_LockSession function.\n-  A call to NI-DCPower locked the session.\n-  A call to the IVI engine locked the session.\n-  After a call to the niDCPower_LockSession function returns\n   successfully, no other threads can access the device session until\n   you call the niDCPower_UnlockSession function.\n-  Use the niDCPower_LockSession function and the\n   niDCPower_UnlockSession function around a sequence of calls to\n   instrument driver functions if you require that the device retain its\n   settings through the end of the sequence.\n\nYou can safely make nested calls to the niDCPower_LockSession function\nwithin the same thread. To completely unlock the session, you must\nbalance each call to the niDCPower_LockSession function with a call to\nthe niDCPower_UnlockSession function. If, however, you use\n**Caller_Has_Lock** in all calls to the niDCPower_LockSession and\nniDCPower_UnlockSession function within a function, the IVI Library\nlocks the session only once within the function regardless of the number\nof calls you make to the niDCPower_LockSession function. This behavior\nallows you to call the niDCPower_UnlockSession function just once at\nthe end of the function.\n'
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
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\n| This parameter is optional. If you do not want to use this parameter,\n  pass VI_NULL.\n| Use this parameter in complex functions to keep track of whether you\n  obtain a lock and therefore need to unlock the session. Pass the\n  address of a local ViBoolean variable. In the declaration of the local\n  variable, initialize it to VI_FALSE. Pass the address of the same\n  local variable to any other calls you make to the\n  niDCPower_LockSession function or the niDCPower_UnlockSession\n  function in the same function.\n| The parameter is an input/output parameter. The niDCPower_LockSession\n  and niDCPower_UnlockSession functions each inspect the current value\n  and take the following actions.\n\n-  If the value is VI_TRUE, the niDCPower_LockSession function does\n   not lock the session again.\n-  If the value is VI_FALSE, the niDCPower_LockSession function\n   obtains the lock and sets the value of the parameter to VI_TRUE.\n-  If the value is VI_FALSE, the niDCPower_UnlockSession function does\n   not attempt to unlock the session.\n-  If the value is VI_TRUE, the niDCPower_UnlockSession function\n   releases the lock and sets the value of the parameter to VI_FALSE.\n\n| Thus, you can, call the niDCPower_UnlockSession function at the end\n  of your function without worrying about whether you actually have the\n  lock, as shown in the following example.\n| ViStatus TestFunc (ViSession vi, ViInt32 flags)\n  {\n  ViStatus error = VI_SUCCESS;\n  ViBoolean haveLock = VI_FALSE;\n  if (flags & BIT_1)\n  {\n  viCheckErr( niDCPower_LockSession(vi, &haveLock;));\n  viCheckErr( TakeAction1(vi));\n  if (flags & BIT_2)\n  {\n  viCheckErr( niDCPower_UnlockSession(vi, &haveLock;));\n  viCheckErr( TakeAction2(vi));\n  viCheckErr( niDCPower_LockSession(vi, &haveLock;);\n  }\n  if (flags & BIT_3)\n  viCheckErr( TakeAction3(vi));\n  }\n  Error:\n  /\\*At this point, you cannot really be sure that you have the lock.\n  Fortunately, the haveLock variable takes care of that for you.\\*/\n  niDCPower_UnlockSession(vi, &haveLock;);\n  return error;\n| }\n'
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
                'name': 'errorBufferSize',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'errorBuffer',
                'size': {
                    'mechanism': 'len',
                    'value': 'errorBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvCloseExtCal': {
        'codegen_method': 'no',
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
                'size': {
                    'mechanism': 'len',
                    'value': 'errorBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvInit': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
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
                'direction': 'out',
                'name': 'newViPtr',
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
                'size': {
                    'mechanism': 'len',
                    'value': 'errorBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvInitExtCal': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
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
                'name': 'newViPtr',
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
                'size': {
                    'mechanism': 'len',
                    'value': 'errorBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvInitWithOptions': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
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
                'direction': 'out',
                'name': 'newViPtr',
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
                'size': {
                    'mechanism': 'len',
                    'value': 'errorBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvInitializeWithChannels': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'name': 'channels',
                'type': 'ViConstString'
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
                'direction': 'out',
                'name': 'newViPtr',
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
                'size': {
                    'mechanism': 'len',
                    'value': 'errorBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvInitializeWithIndependentChannels': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'resourceName',
                'type': 'ViRsrc'
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
                'direction': 'out',
                'name': 'newViPtr',
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
                'size': {
                    'mechanism': 'len',
                    'value': 'errorBufferSize'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvMeasureMultiple': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'voltageMeasurements',
                'type': 'lvdataconv::LVArrayPrimitive<ViReal64>*'
            },
            {
                'direction': 'out',
                'name': 'currentMeasurements',
                'type': 'lvdataconv::LVArrayPrimitive<ViReal64>*'
            }
        ],
        'returns': 'ViStatus'
    },
    'LvMeasureMultipleWithCompliance': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'voltageMeasurements',
                'type': 'lvdataconv::LVArrayPrimitive<ViReal64>*'
            },
            {
                'direction': 'out',
                'name': 'currentMeasurements',
                'type': 'lvdataconv::LVArrayPrimitive<ViReal64>*'
            },
            {
                'direction': 'out',
                'name': 'inCompliance',
                'type': 'lvdataconv::LVArrayPrimitive<ViBoolean>*'
            },
            {
                'direction': 'in',
                'name': 'retrieveFromCache',
                'type': 'ViBoolean'
            }
        ],
        'returns': None
    },
    'Measure': {
        'documentation': {
            'description': '\nReturns the measured value of either the voltage or current on the\nspecified output channel. Each call to this function blocks other\nfunction calls until the hardware returns the **measurement**. To\nmeasure multiple output channels, use the niDCPower_MeasureMultiple\nfunction.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel to measure. Only one measurement at a time\nmay be made with the niDCPower_Measure function. Use the\nniDCPower_MeasureMultiple function to measure multiple channels.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether a voltage or current value is measured.\n**Defined Values**:\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_MEASURE_VOLTAGE (1)',
                            'The device measures voltage.'
                        ],
                        [
                            'NIDCPOWER_VAL_MEASURE_CURRENT (0)',
                            'The device measures current.'
                        ]
                    ]
                },
                'enum': 'MeasurementTypes',
                'name': 'measurementType',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the value of the measurement, either in volts for voltage or\namps for current.\n'
                },
                'name': 'measurement',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'MeasureMultiple': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nReturns arrays of the measured voltage and current values on the\nspecified output channel(s). Each call to this function blocks other\nfunction calls until the measurements are returned from the device. The\norder of the measurements returned in the array corresponds to the order\non the specified output channel(s).\n'
        },
        'method_name_for_documentation': 'measure_multiple',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channels to measure. You can specify multiple\nchannels by using a channel list or a channel range. A channel list is a\ncomma (,) separated sequence of channel names (e.g. 0,2 specifies\nchannels 0 and 2). A channel range is a lower bound channel followed by\na hyphen (-) or colon (:) followed by an upper bound channel (e.g. 0-2\nspecifies channels 0, 1, and 2). If you do not specify a channel name,\nthe function uses all channels in the session.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of voltage measurements. The measurements in the array\nare returned in the same order as the channels specified in\n**channelName**. Ensure that sufficient space has been allocated for the\nreturned array.\n'
                },
                'name': 'voltageMeasurements',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._parse_channel_count()'
                },
                'type': 'ViReal64[]',
                'use_array': True
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns an array of current measurements. The measurements in the array\nare returned in the same order as the channels specified in\n**channelName**. Ensure that sufficient space has been allocated for the\nreturned array.\n'
                },
                'name': 'currentMeasurements',
                'size': {
                    'mechanism': 'python-code',
                    'value': 'self._parse_channel_count()'
                },
                'type': 'ViReal64[]',
                'use_array': True
            }
        ],
        'returns': 'ViStatus'
    },
    'MeasureMultipleWithCompliance': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'voltageMeasurements',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'currentMeasurements',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'name': 'inCompliance',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViBoolean[]'
            },
            {
                'direction': 'in',
                'name': 'retrieveFromCache',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ParseChannelCount': {
        'codegen_method': 'private',
        'documentation': {
            'description': 'Returns the number of channels.'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'name': 'channelsString',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'name': 'numberOfChannels',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryInCompliance': {
        'documentation': {
            'description': '\nQueries the specified output device to determine if it is operating at\nthe `compliance <REPLACE_DRIVER_SPECIFIC_URL_2(compliance)>`__ limit.\n\nThe compliance limit is the current limit when the output function is\nset to NIDCPOWER_VAL_DC_VOLTAGE. If the output is operating at the\ncompliance limit, the output reaches the current limit before the\ndesired voltage level. Refer to the niDCPower_ConfigureOutputFunction\nfunction and the niDCPower_ConfigureCurrentLimit function for more\ninformation about output function and current limit, respectively.\n\nThe compliance limit is the voltage limit when the output function is\nset to NIDCPOWER_VAL_DC_CURRENT. If the output is operating at the\ncompliance limit, the output reaches the voltage limit before the\ndesired current level. Refer to the niDCPower_ConfigureOutputFunction\nfunction and the niDCPower_ConfigureVoltageLimit function for more\ninformation about output function and voltage limit, respectively.\n\n**Related Topics:**\n\n`Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel to query. Compliance status can only be\nqueried for one channel at a time.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns whether the device output channel is in compliance.'
                },
                'name': 'inCompliance',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryMaxCurrentLimit': {
        'documentation': {
            'description': '\nQueries the maximum current limit on an output channel if the output\nchannel is set to the specified **voltageLevel**.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel to query. The maximum current limit may\nonly be queried for one channel at a time.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the voltage level to use when calculating the\n**maxCurrentLimit**.\n'
                },
                'name': 'voltageLevel',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum current limit that can be set with the specified\n**voltageLevel**.\n'
                },
                'name': 'maxCurrentLimit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryMaxVoltageLevel': {
        'documentation': {
            'description': '\nQueries the maximum voltage level on an output channel if the output\nchannel is set to the specified **currentLimit**.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel to query. The maximum voltage level may\nonly be queried for one channel at a time.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the current limit to use when calculating the\n**maxVoltageLevel**.\n'
                },
                'name': 'currentLimit',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the maximum voltage level that can be set on an output channel\nwith the specified **currentLimit**.\n'
                },
                'name': 'maxVoltageLevel',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryMinCurrentLimit': {
        'documentation': {
            'description': '\nQueries the minimum current limit on an output channel if the output\nchannel is set to the specified **voltageLevel**.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel to query. The minimum current limit may\nonly be queried for one channel at a time.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the voltage level to use when calculating the\n**minCurrentLimit**.\n'
                },
                'name': 'voltageLevel',
                'type': 'ViReal64'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the minimum current limit that can be set on an output channel\nwith the specified **voltageLevel**.\n'
                },
                'name': 'minCurrentLimit',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'QueryOutputState': {
        'documentation': {
            'description': '\nQueries the specified output channel to determine if the output channel\nis currently in the state specified by **outputState**.\n\n**Related Topics:**\n\n`Compliance <REPLACE_DRIVER_SPECIFIC_URL_1(compliance)>`__\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel to query. The output state may only be\nqueried for one channel at a time.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output state of the output channel that is being queried.\n**Defined Values**:\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_OUTPUT_CONSTANT_VOLTAGE (0)',
                            'The device maintains a constant voltage by adjusting the current.'
                        ],
                        [
                            'NIDCPOWER_VAL_OUTPUT_CONSTANT_CURRENT (1)',
                            'The device maintains a constant current by adjusting the voltage.'
                        ]
                    ]
                },
                'enum': 'OutputStates',
                'name': 'outputState',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns whether the device output channel is in the specified output\nstate.\n'
                },
                'name': 'inState',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadCurrentTemperature': {
        'documentation': {
            'description': '\nReturns the current onboard **temperature**, in degrees Celsius, of the\ndevice.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the onboard **temperature**, in degrees Celsius, of the device.'
                },
                'name': 'temperature',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadFlashEepromBlock': {
        'codegen_method': 'no',
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
                'name': 'address',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViUInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReadRegister': {
        'codegen_method': 'no',
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
                'name': 'registerSize',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'name': 'offset',
                'type': 'ViUInt16'
            },
            {
                'direction': 'out',
                'name': 'value',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'ReleaseSessionForServer': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
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
                'name': 'privilegeLevel',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetDevice': {
        'documentation': {
            'description': '\nResets the device to a known state. The function disables power\ngeneration, resets session attributes to their default values, clears\nerrors such as overtemperature and unexpected loss of auxiliary power,\ncommits the session attributes, and leaves the session in the\nUncommitted state. This function also performs a hard reset on the\ndevice and driver software. This function has the same functionality as\nusing reset in Measurement & Automation Explorer. Refer to the\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for\nmore information about NI-DCPower software states.\n\nThis will also open the output relay on devices that have an output\nrelay.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
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
            'description': '\nWhen developing a complex test system that consists of multiple test\nmodules, it is generally a good idea to design the test modules so that\nthey can run in any order. To do so requires ensuring that each test\nmodule completely configures the state of each instrument it uses. If a\nparticular test module does not completely configure the state of an\ninstrument, the state of the instrument depends on the configuration\nfrom a previously executed test module. If you execute the test modules\nin a different order, the behavior of the instrument and therefore the\nentire test module is likely to change. This change in behavior is\ngenerally instrument specific and represents an interchangeability\nproblem.\n\nYou can use this function to test for such cases. After you call this\nfunction, the interchangeability checking algorithms in the specific\ndriver ignore all previous configuration operations. By calling this\nfunction at the beginning of a test module, you can determine whether\nthe test module has dependencies on the operation of previously executed\ntest modules.\n\nThis function does not clear the interchangeability warnings from the\nlist of previously recorded interchangeability warnings. If you want to\nguarantee that the niDCPower_GetNextInterchangeWarning function only\nreturns those interchangeability warnings that are generated after\ncalling this function, you must clear the list of interchangeability\nwarnings. You can clear the interchangeability warnings list by\nrepeatedly calling the niDCPower_GetNextInterchangeWarning function\nuntil no more interchangeability warnings are returned. If you are not\ninterested in the content of those warnings, you can call the\nniDCPower_ClearInterchangeWarnings function.\n',
            'note': '\nniDCPower_GetNextInterchangeWarning does not mark any attributes for\nan interchange check.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetOutputProtection': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithDefaults': {
        'documentation': {
            'description': "\nResets the device to a known state. This function disables power\ngeneration, resets session attributes to their default values, commits\nthe session attributes, and leaves the session in the\n`Running <javascript:LaunchHelp('NI_DC_Power_Supplies_Help.chm::/programmingStates.html#running')>`__\nstate. In addition to exhibiting the behavior of the niDCPower_reset\nfunction, this function can assign user-defined default values for\nconfigurable attributes from the IVI configuration.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'ResetWithDefaultsWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'RestoreAttributes': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
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
                'direction': 'out',
                'name': 'clientWasRevoked',
                'type': 'ViBoolean'
            },
            {
                'direction': 'out',
                'name': 'cachedSessionState',
                'type': 'ViInt32'
            },
            {
                'direction': 'out',
                'name': 'cachedSessionStateValid',
                'type': 'ViBoolean'
            }
        ],
        'returns': 'ViStatus'
    },
    'SaveAttributes': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareEdgeTrigger': {
        'documentation': {
            'description': '\nAsserts the specified trigger. This function can override an external\nedge trigger.\n\n**Related Topics:**\n\n`Triggers <REPLACE_DRIVER_SPECIFIC_URL_1(trigger)>`__\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies which trigger to assert.\n**Defined Values:**\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_START_TRIGGER (1034)',
                            'Asserts the Start trigger.'
                        ],
                        [
                            'NIDCPOWER_VAL_SOURCE_TRIGGER (1035)',
                            'Asserts the Source trigger.'
                        ],
                        [
                            'NIDCPOWER_VAL_MEASURE_TRIGGER (1036)',
                            'Asserts the Measure trigger.'
                        ],
                        [
                            'NIDCPOWER_VAL_SEQUENCE_ADVANCE_TRIGGER (1037)',
                            'Asserts the Sequence Advance trigger.'
                        ],
                        [
                            'NIDCPOWER_VAL_PULSE_TRIGGER (1053',
                            'Asserts the Pulse trigger.'
                        ]
                    ]
                },
                'enum': 'SendSoftwareEdgeTriggerType',
                'name': 'trigger',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SendSoftwareEdgeTriggerWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'trigger',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViBoolean': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\n| Sets the value of a ViBoolean attribute.\n| This is a low-level function that you can use to set the values of\n  device-specific attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Attributes whose value cannot be set are\n   dim. Help text is shown for each attribute. Select an attribute by\n   double-clicking on it or by selecting it and then pressing **Enter**.\n-  Read-only attributes appear dim in the list box. If you select a\n   read-only attribute, an error message appears. A ring control at the\n   top of the dialog box allows you to see all IVI attributes or only\n   the attributes of type ViBoolean. If you choose to see all IVI\n   attributes, the data types appear to the right of the attribute names\n   in the list box. Attributes with data types other than ViBoolean are\n   dim. If you select an attribute data type that is dim, LabWindows/CVI\n   transfers you to the function panel for the corresponding function\n   that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. If the\nattribute currently showing in the attribute ring control has constants\nas valid values, you can view a list of the constants by pressing\n**Enter** on this control. Select a value by double-clicking on it or by\nselecting it and then pressing **Enter**.\n',
                    'note': '\nSome of the values might not be valid depending upon the current\nsettings of the device session.\n'
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
            'description': '\n| Sets the value of a ViInt32 attribute.\n| This is a low-level function that you can use to set the values of\n  device-specific attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Attributes whose value cannot be set are\n   dim. Help text is shown for each attribute. Select an attribute by\n   double-clicking on it or by selecting it and then pressing **Enter**.\n-  Read-only attributes appear dim in the list box. If you select a\n   read-only attribute, an error message appears. A ring control at the\n   top of the dialog box allows you to see all IVI attributes or only\n   the attributes of type ViInt32. If you choose to see all IVI\n   attributes, the data types appear to the right of the attribute names\n   in the list box. Attributes with data types other than ViInt32 are\n   dim. If you select an attribute data type that is dim, LabWindows/CVI\n   transfers you to the function panel for the corresponding function\n   that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. If the\nattribute currently showing in the attribute ring control has constants\nas valid values, you can view a list of the constants by pressing\n**Enter** on this control. Select a value by double-clicking on it or by\nselecting it and then pressing **Enter**.\n',
                    'note': '\nSome of the values might not be valid depending upon the current\nsettings of the device session.\n'
                },
                'name': 'attributeValue',
                'type': 'ViInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetAttributeViInt64': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\n| Sets the value of a ViInt64 attribute.\n| This is a low-level function that you can use to set the values of\n  device-specific attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Attributes whose value cannot be set are\n   dim. Help text is shown for each attribute. Select an attribute by\n   double-clicking on it or by selecting it and then pressing **Enter**.\n-  Read-only attributes appear dim in the list box. If you select a\n   read-only attribute, an error message appears. A ring control at the\n   top of the dialog box allows you to see all IVI attributes or only\n   the attributes of type ViReal64. If you choose to see all IVI\n   attributes, the data types appear to the right of the attribute names\n   in the list box. Attributes with data types other than ViReal64 are\n   dim. If you select an attribute data type that is dim, LabWindows/CVI\n   transfers you to the function panel for the corresponding function\n   that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. If the\nattribute currently showing in the attribute ring control has constants\nas valid values, you can view a list of the constants by pressing\n**Enter** on this control. Select a value by double-clicking on it or by\nselecting it and then pressing **Enter**.\n',
                    'note': '\nSome of the values might not be valid depending upon the current\nsettings of the device session.\n'
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
            'description': '\n| Sets the value of a ViReal64 attribute.\n| This is a low-level function that you can use to set the values of\n  device-specific attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Attributes whose value cannot be set are\n   dim. Help text is shown for each attribute. Select an attribute by\n   double-clicking on it or by selecting it and then pressing **Enter**.\n-  Read-only attributes appear dim in the list box. If you select a\n   read-only attribute, an error message appears. A ring control at the\n   top of the dialog box allows you to see all IVI attributes or only\n   the attributes of type ViReal64. If you choose to see all IVI\n   attributes, the data types appear to the right of the attribute names\n   in the list box. Attributes with data types other than ViReal64 are\n   dim. If you select an attribute data type that is dim, LabWindows/CVI\n   transfers you to the function panel for the corresponding function\n   that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. If the\nattribute currently showing in the attribute ring control has constants\nas valid values, you can view a list of the constants by pressing\n**Enter** on this control. Select a value by double-clicking on it or by\nselecting it and then pressing **Enter**.\n',
                    'note': '\nSome of the values might not be valid depending upon the current\nsettings of the device session.\n'
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
            'description': '\n| Sets the value of a ViSession attribute.\n| This is a low-level function that you can use to set the values of\n  device-specific attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Attributes whose value cannot be set are\n   dim. Help text is shown for each attribute. Select an attribute by\n   double-clicking on it or by selecting it and then pressing **Enter**.\n-  Read-only attributes appear dim in the list box. If you select a\n   read-only attribute, an error message appears. A ring control at the\n   top of the dialog box allows you to see all IVI attributes or only\n   the attributes of type ViSession. If you choose to see all IVI\n   attributes, the data types appear to the right of the attribute names\n   in the list box. Attributes with data types other than ViSession are\n   dim. If you select an attribute data type that is dim, LabWindows/CVI\n   transfers you to the function panel for the corresponding function\n   that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. If the\nattribute currently showing in the attribute ring control has constants\nas valid values, you can view a list of the constants by pressing\n**Enter** on this control. Select a value by double-clicking on it or by\nselecting it and then pressing **Enter**.\n',
                    'note': '\nSome of the values might not be valid depending upon the current\nsettings of the device session.\n'
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
            'description': '\n| Sets the value of a ViString attribute.\n| This is a low-level function that you can use to set the values of\n  device-specific attributes and inherent IVI attributes.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel(s) to which this configuration value\napplies. Specify multiple channels by using a channel list or a channel\nrange. A channel list is a comma (,) separated sequence of channel names\n(for example, 0,2 specifies channels 0 and 2). A channel range is a\nlower bound channel followed by a hyphen (-) or colon (:) followed by an\nupper bound channel (for example, 0-2 specifies channels 0, 1, and 2).\nIn the Running state, multiple output channel configurations are\nperformed sequentially based on the order specified in this parameter.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the ID of an attribute. From the function panel window, you\ncan use this control as follows.\n\n-  In the function panel window, click on the control or press **Enter**\n   or the spacebar to display a dialog box containing hierarchical list\n   of the available attributes. Attributes whose value cannot be set are\n   dim. Help text is shown for each attribute. Select an attribute by\n   double-clicking on it or by selecting it and then pressing **Enter**.\n-  Read-only attributes appear dim in the list box. If you select a\n   read-only attribute, an error message appears. A ring control at the\n   top of the dialog box allows you to see all IVI attributes or only\n   the attributes of type ViString. If you choose to see all IVI\n   attributes, the data types appear to the right of the attribute names\n   in the list box. Attributes with data types other than ViString are\n   dim. If you select an attribute data type that is dim, LabWindows/CVI\n   transfers you to the function panel for the corresponding function\n   that is consistent with the data type.\n-  If you want to enter a variable name, press **Ctrl**\\ +\\ **T** to\n   change this ring control to a manual input box. If the attribute in\n   this ring control has named constants as valid values, you can view\n   the constants by moving to the value control and pressing **Enter**.\n'
                },
                'name': 'attributeId',
                'type': 'ViAttr'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the value to which you want to set the attribute. If the\nattribute currently showing in the attribute ring control has constants\nas valid values, you can view a list of the constants by pressing\n**Enter** on this control. Select a value by double-clicking on it or by\nselecting it and then pressing **Enter**.\n',
                    'note': '\nSome of the values might not be valid depending upon the current\nsettings of the device session.\n'
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
            'description': '\nStores a user-defined string of characters in the device onboard EEPROM.\nIf the string is longer than the maximum allowable size, it is\ntruncated. This function overwrites any existing user-defined\ninformation.\n\nIf you call this function in a session, **info** is immediately changed.\nIf you call this function in an external calibration session, **info**\nis changed only after you close the session using the\nniDCPower_CloseExtCal function with **action** set to\nNIDCPOWER_VAL_COMMIT.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitExtCal or niDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Specifies the string to store in the device onboard EEPROM.'
                },
                'name': 'info',
                'type': 'ViConstString'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetCloseFunctionPointer': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'closeFunctionPtr',
                'type': 'CloseFunctionType'
            }
        ],
        'returns': 'ViStatus'
    },
    'SetSequence': {
        'documentation': {
            'description': '\nConfigures a series of voltage or current outputs and corresponding\nsource delays. The source mode must be set to\n`Sequence <REPLACE_DRIVER_SPECIFIC_URL_1(sequencing)>`__ for this\nfunction to take effect.\n\nRefer to the `Configuring the Source\nUnit <REPLACE_DRIVER_SPECIFIC_URL_1(configuringthesourceunit)>`__ topic\nin the *NI DC Power Supplies and SMUs Help* for more information about\nhow to configure your device.\n\nUse this function in the Uncommitted or Committed programming states.\nRefer to the `Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in\nthe *NI DC Power Supplies and SMUs Help* for more information about\nNI-DCPower programming states.\n',
            'note': "\nThis function is not supported on all devices. Refer to `Supported\nFunctions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the output channel to which this configuration value applies.\nYou can only set a sequence for one channel at a time.\n'
                },
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the series of voltage levels or current levels, depending on\nthe configured `output\nfunction <REPLACE_DRIVER_SPECIFIC_URL_1(programming_output)>`__.\n**Valid values**:\nThe valid values for this parameter are defined by the voltage level\nrange or current level range.\n'
                },
                'name': 'values',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the source delay that follows the configuration of each value\nin the sequence.\n**Valid Values**:\nThe valid values are between 0 and 167 seconds.\n'
                },
                'name': 'sourceDelays',
                'size': {
                    'mechanism': 'len',
                    'value': 'size'
                },
                'type': 'ViReal64[]'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nThe number of elements in the Values and the Source Delays arrays. The\nValues and Source Delays arrays should have the same size.\n'
                },
                'name': 'size',
                'type': 'ViUInt32'
            }
        ],
        'returns': 'ViStatus'
    },
    'UnlockSession': {
        'documentation': {
            'description': '\nReleases a lock that you acquired on an device session using\nniDCPower_LockSession. Refer to niDCPower_LockSession for additional\ninformation on session locks.\n'
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
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\n| This attribute is optional. If you do not want to use this attribute,\n  pass VI_NULL.\n| Use this attribute in complex functions to keep track of whether you\n  obtain a lock and therefore need to unlock the session.\n| Pass the address of a local ViBoolean variable. In the declaration of\n  the local variable, initialize it to VI_FALSE. Pass the address of\n  the same local variable to any other calls you make to\n  niDCPower_LockSession or niDCPower_UnlockSessionin the same\n  function.\n| The parameter is an input/output parameter. niDCPower_LockSession and\n  niDCPower_UnlockSessioneach inspect the current value and take the\n  following actions.\n\n-  If the value is VI_TRUE, niDCPower_LockSession does not lock the\n   session again.\n-  If the value is VI_FALSE, niDCPower_LockSession obtains the lock\n   and sets the value of the parameter to VI_TRUE.\n-  If the value is VI_FALSE, niDCPower_UnlockSessiondoes not attempt\n   to unlock the session.\n-  If the value is VI_TRUE, niDCPower_UnlockSessionreleases the lock\n   and sets the value of the parameter to VI_FALSE.\n\n| Thus, you can, call niDCPower_UnlockSession at the end of your\n  function without worrying about whether you actually have the lock, as\n  the following example shows.\n| ViStatus TestFunc (ViSession vi, ViInt32 flags)\n  {\n  ViStatus error = VI_SUCCESS;\n  ViBoolean haveLock = VI_FALSE;\n  if (flags & BIT_1)\n  {\n  viCheckErr( niDCPower_LockSession(vi, &haveLock;));\n  viCheckErr( TakeAction1(vi));\n  if (flags & BIT_2)\n  {\n  viCheckErr( niDCPower_UnlockSession(vi, &haveLock;));\n  viCheckErr( TakeAction2(vi));\n  viCheckErr( niDCPower_LockSession(vi, &haveLock;);\n  }\n  if (flags & BIT_3)\n  viCheckErr( TakeAction3(vi));\n  }\n  Error:\n  /\\*At this point, you cannot really be sure that you have the lock.\n  Fortunately, the haveLock variable takes care of that for you.\\*/\n  niDCPower_UnlockSession(vi, &haveLock;);\n  return error;\n  }\n'
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
    'WaitForEvent': {
        'documentation': {
            'description': '\nWaits until the device has generated the specified event.\n\nThe session monitors whether each type of event has occurred at least\nonce since the last time this function or the niDCPower_Initiate\nfunction were called. If an event has only been generated once and you\ncall this function successively, the function times out. Individual\nevents must be generated between separate calls of this function.\n',
            'note': "\nRefer to `Supported Functions by\nDevice <REPLACE_DRIVER_SPECIFIC_URL_2(nidcpowercref.chm',%20'supportedfunctions)>`__\nfor more information about supported devices.\n"
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies which event to wait for.\n**Defined Values:**\n',
                    'table_body': [
                        [
                            'NIDCPOWER_VAL_SOURCE_COMPLETE_EVENT (1030)',
                            'Waits for the Source Complete event.'
                        ],
                        [
                            'NIDCPOWER_VAL_MEASURE_COMPLETE_EVENT (1031)',
                            'Waits for the Measure Complete event.'
                        ],
                        [
                            'NIDCPOWER_VAL_SEQUENCE_ITERATION_COMPLETE_EVENT (1032)',
                            'Waits for the Sequence Iteration Complete event.'
                        ],
                        [
                            'NIDCPOWER_VAL_SEQUENCE_ENGINE_DONE_EVENT (1033)',
                            'Waits for the Sequence Engine Done event.'
                        ],
                        [
                            'NIDCPOWER_VAL_PULSE_COMPLETE_EVENT (1051 )',
                            'Waits for the Pulse Complete event.'
                        ],
                        [
                            'NIDCPOWER_VAL_READY_FOR_PULSE_TRIGGER_EVENT (1052)',
                            'Waits for the Ready for Pulse Trigger event.'
                        ]
                    ]
                },
                'enum': 'Event',
                'name': 'eventId',
                'type': 'ViInt32'
            },
            {
                'default_value': 'datetime.timedelta(seconds=10.0)',
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the maximum time allowed for this function to complete, in\nseconds. If the function does not complete within this time interval,\nNI-DCPower returns an error.\n',
                    'note': '\nWhen setting the timeout interval, ensure you take into account any\ntriggers so that the timeout interval is long enough for your\napplication.\n'
                },
                'name': 'timeout',
                'python_api_converter_name': 'convert_timedelta_to_seconds',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
            }
        ],
        'returns': 'ViStatus'
    },
    'WaitForEventWithChannels': {
        'codegen_method': 'no',
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
                'name': 'channelName',
                'type': 'ViConstString'
            },
            {
                'direction': 'in',
                'name': 'eventId',
                'type': 'ViInt32'
            },
            {
                'direction': 'in',
                'name': 'timeout',
                'type': 'ViReal64'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteDefaultCalValues': {
        'codegen_method': 'no',
        'documentation': {
            'description': 'TBD'
        },
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteFlashEepromBlock': {
        'codegen_method': 'no',
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
                'name': 'address',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'name': 'size',
                'type': 'ViUInt32'
            },
            {
                'direction': 'in',
                'name': 'data',
                'size': {
                    'mechanism': 'TBD',
                    'value': 'TBD'
                },
                'type': 'ViUInt8[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'WriteRegister': {
        'codegen_method': 'no',
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
                'name': 'registerSize',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'name': 'offset',
                'type': 'ViUInt16'
            },
            {
                'direction': 'in',
                'name': 'value',
                'type': 'ViUInt16'
            }
        ],
        'returns': 'ViStatus'
    },
    'close': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nCloses the session specified in **vi** and deallocates the resources\nthat NI-DCPower reserves. If power output is enabled when you call this\nfunction, the output channels remain in their existing state and\ncontinue providing power. Use the niDCPower_ConfigureOutputEnabled\nfunction to disable power output on a per channel basis. Use the\nniDCPower_reset function to disable power output on all channel(s).\n\n**Related Topics:**\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
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
            'description': '\nConverts a status code returned by an instrument driver function into a\nuser-readable string.\n'
        },
        'is_error_handling': True,
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **status** parameter that is returned from any of the\nNI-DCPower functions.\n'
                },
                'name': 'errorCode',
                'type': 'ViStatus'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the user-readable message string that corresponds to the status\ncode you specify.\nYou must pass a ViChar array with at least 256 bytes.\n'
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
    'fancy_self_test': {
        'codegen_method': 'python-only',
        'documentation': {
            'description': '\nPerforms the device self-test routine and returns the test result(s).\nCalling this function implicitly calls the niDCPower_reset function.\n\nWhen calling niDCPower_self_test with the PXIe-4162/4163, specify all\nchannels of your PXIe-4162/4163 with the channels input of\nniDCPower_InitializeWithChannels. You cannot self test a subset of\nPXIe-4162/4163 channels.\n\nRaises `SelfTestError` on self test failure. Attributes on exception object:\n\n- code - failure code from driver\n- message - status message from driver\n',
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
                'method_python_name_suffix': '',
                'session_filename': 'fancy_self_test'
            }
        ],
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitializeWithChannels function.'
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
            'description': '\nThis function is deprecated. Use niDCPower_InitializeWithChannels\ninstead.\n\nCreates a new IVI instrument driver session to the device specified in\n**resourceName** and returns a session handle you use to identify the\ndevice in all subsequent NI-DCPower function calls. This function also\nsends initialization commands to set the device to the state necessary\nfor the operation of NI-DCPower.\n\nTo place the device in a known start-up state when creating a new\nsession, set **resetDevice** to VI_TRUE. This action is equivalent to\nusing the niDCPower_reset function.\n\nTo open a session and leave the device in its existing configuration\nwithout passing through a transitional output state, set **resetDevice**\nto VI_FALSE, and immediately call the niDCPower_Abort function. Then\nconfigure the device as in the previous session, changing only the\ndesired settings, and then call the niDCPower_Initiate function. Refer\nto the `deprecated programming state\nmodel <REPLACE_DRIVER_SPECIFIC_URL_1(initializedeprecatedmodel)>`__ for\ninformation about the specific software states.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies the **resourceName** assigned by Measurement & Automation\nExplorer (MAX), for example "PXI1Slot3" where "PXI1Slot3" is an\ninstrument\'s **resourceName**. **resourceName** can also be a logical\nIVI name.\n'
                },
                'name': 'resourceName',
                'type': 'ViRsrc'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether the device is queried to determine if the device is a\nvalid instrument for NI-DCPower.\n**Defined Values**:\n',
                    'table_body': [
                        [
                            'VI_TRUE (1)',
                            'Perform ID query.'
                        ],
                        [
                            'VI_FALSE (0)',
                            'Do not perform ID query.'
                        ]
                    ]
                },
                'name': 'idQuery',
                'type': 'ViBoolean'
            },
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nSpecifies whether to reset the device during the initialization\nprocedure.\n**Defined Values**:\n',
                    'table_body': [
                        [
                            'VI_TRUE (1)',
                            'Reset the device.'
                        ],
                        [
                            'VI_FALSE (0)',
                            'Do not reset the device.'
                        ]
                    ]
                },
                'name': 'resetDevice',
                'type': 'ViBoolean'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns a session handle that you use to identify the session in all\nsubsequent NI-DCPower function calls.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            }
        ],
        'returns': 'ViStatus'
    },
    'reset': {
        'documentation': {
            'description': '\nResets the device to a known state. This function disables power\ngeneration, resets session attributes to their default values, commits\nthe session attributes, and leaves the session in the Uncommitted state.\nRefer to the `Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic for\nmore information about NI-DCPower software states.\n'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
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
            'description': 'Returns the revision information of NI-DCPower and the device firmware.'
        },
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the driver revision information for NI-DCPower.'
                },
                'name': 'instrumentDriverRevision',
                'size': {
                    'mechanism': 'fixed',
                    'value': '256'
                },
                'type': 'ViChar[]'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns firmware revision information for the device you are using. The\nsize of this array must be at least 256 bytes.\n'
                },
                'name': 'firmwareRevision',
                'size': {
                    'mechanism': 'fixed',
                    'value': '256'
                },
                'type': 'ViChar[]'
            }
        ],
        'returns': 'ViStatus'
    },
    'self_test': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nPerforms the device self-test routine and returns the test result(s).\nCalling this function implicitly calls the niDCPower_reset function.\n\nWhen calling niDCPower_self_test with the PXIe-4162/4163, specify all\nchannels of your PXIe-4162/4163 with the channels input of\nniDCPower_InitializeWithChannels. You cannot self test a subset of\nPXIe-4162/4163 channels.\n'
        },
        'method_name_for_documentation': 'self_test',
        'parameters': [
            {
                'direction': 'in',
                'documentation': {
                    'description': '\nIdentifies a particular instrument session. **vi** is obtained from the\nniDCPower_InitializeWithChannels function.\n'
                },
                'name': 'vi',
                'type': 'ViSession'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': 'Returns the value result from the device self-test.',
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
                'name': 'selfTestResult',
                'type': 'ViInt16'
            },
            {
                'direction': 'out',
                'documentation': {
                    'description': '\nReturns the self-test result message. The size of this array must be at\nleast 256 bytes.\n'
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
