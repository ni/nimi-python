# -*- coding: utf-8 -*-
# This file is generated from NI-DCPower API metadata version 20.2.0d17
functions = {
    'Abort': {
        'documentation': {
            'description': '\nTransitions the NI-DCPower session from the Running state to the\nUncommitted state. If a sequence is running, it is stopped. Any\nconfiguration functions called after this function are not applied until\nthe niDCPower_Initiate function is called. If power output is enabled\nwhen you call the niDCPower_Abort function, the output channels remain\nin their current state and continue providing power.\n\nUse the niDCPower_ConfigureOutputEnabled function to disable power\noutput on a per channel basis. Use the niDCPower_reset function to\ndisable output on all channels.\n\nRefer to the `Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in\nthe *NI DC Power Supplies and SMUs Help* for information about the\nspecific NI-DCPower software states.\n\n**Related Topics:**\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n'
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
                    'description': '\nSpecifies the attributes you reconfigure per step in the advanced\nsequence. The following table lists which attributes can be configured\nin an advanced sequence for each NI-DCPower device that supports\nadvanced sequencing. A Yes indicates that the attribute can be configured\nin advanced sequencing. An No indicates that the attribute cannot be\nconfigured in advanced sequencing.\n',
                    'table_body': [
                        [
                            'NIDCPOWER_ATTR_DC_NOISE_REJECTION',
                            'Yes',
                            'No',
                            'Yes',
                            'No',
                            'Yes',
                            'No',
                            'No',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_APERTURE_TIME',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_SENSE',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_OVP_ENABLED',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_OVP_LIMIT',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_BIAS_DELAY',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_OFF_TIME',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_ON_TIME',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_SOURCE_DELAY',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY',
                            'Yes',
                            'No',
                            'Yes',
                            'No',
                            'Yes',
                            'No',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH',
                            'Yes',
                            'No',
                            'Yes',
                            'No',
                            'Yes',
                            'No',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO',
                            'Yes',
                            'No',
                            'Yes',
                            'No',
                            'Yes',
                            'No',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY',
                            'Yes',
                            'No',
                            'Yes',
                            'No',
                            'Yes',
                            'No',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH',
                            'Yes',
                            'No',
                            'Yes',
                            'No',
                            'Yes',
                            'No',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO',
                            'Yes',
                            'No',
                            'Yes',
                            'No',
                            'Yes',
                            'No',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_CURRENT_LEVEL',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_VOLTAGE_LIMIT',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_CURRENT_LIMIT',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_CURRENT_LIMIT_LOW',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_VOLTAGE_LEVEL',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_OUTPUT_ENABLED',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_OUTPUT_FUNCTION',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes'
                        ],
                        [
                            'NIDCPOWER_ATTR_OUTPUT_RESISTANCE',
                            'Yes',
                            'No',
                            'Yes',
                            'No',
                            'Yes',
                            'No',
                            'Yes',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'No',
                            'No',
                            'No'
                        ],
                        [
                            'NIDCPOWER_ATTR_TRANSIENT_RESPONSE',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes',
                            'Yes'
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
    'CreateAdvancedSequenceStep': {
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
                'python_api_converter_name': 'convert_to_bytes',
                'type_in_documentation': 'bytes',
                'size': {
                    'mechanism': 'ivi-dance',
                    'value': 'size'
                },
                'type': 'ViInt8[]',
                'use_array': True
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
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
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
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
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
                'is_repeated_capability': False,
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
                'python_api_converter_name': 'convert_to_bytes',
                'type_in_documentation': 'bytes',
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
    'Initiate': {
        'codegen_method': 'private',
        'documentation': {
            'description': '\nStarts generation or acquisition, causing the NI-DCPower session to\nleave the Uncommitted state or Committed state and enter the Running\nstate. To return to the Uncommitted state call the niDCPower_Abort\nfunction. Refer to the `Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__ topic in\nthe *NI DC Power Supplies and SMUs Help* for information about the\nspecific NI-DCPower software states.\n\n**Related Topics:**\n\n`Programming\nStates <REPLACE_DRIVER_SPECIFIC_URL_1(programmingstates)>`__\n'
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
                'python_api_converter_name': 'convert_timedelta_to_seconds_real64',
                'type': 'ViReal64',
                'type_in_documentation': 'float in seconds or datetime.timedelta'
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
        'python_name': '_close',
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
